#!/usr/bin/env python3
"""Simple link checker for markdown docs.

The script walks through the provided directories, finds Markdown files and
verifies that every HTTP/HTTPS link returns a 200 status code. When a server
rejects HEAD requests we automatically retry with GET.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Set
from urllib import error, request

URL_PATTERN = re.compile(r"\[(?:[^\[\]]+)\]\((https?://[^\s)]+)\)")
DEFAULT_PATHS = ["."]
REPO_ROOT = Path(__file__).resolve().parents[1]
USER_AGENT = "InfoHubLinkChecker/1.0 (+https://github.com/FTarkowski/InfoHub)"


@dataclass
class LinkStatus:
    url: str
    ok: bool
    status: int | None = None
    error: str | None = None
    source_files: List[Path] | None = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check HTTP links inside Markdown files.")
    parser.add_argument(
        "paths",
        nargs="*",
        default=DEFAULT_PATHS,
        help="Paths to scan (directories or files). Defaults to the entire repository.",
    )
    parser.add_argument(
        "--exclude",
        "-x",
        action="append",
        default=[],
        help="Directories to skip (e.g. scripts, venv). Can be used multiple times.",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=8,
        help="Number of concurrent requests (default: 8).",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="Timeout in seconds for each HTTP request (default: 10).",
    )
    return parser.parse_args()


def iter_markdown_files(paths: Iterable[str], excluded_dirs: Set[str]) -> Iterable[Path]:
    excluded = {Path(name).name for name in excluded_dirs}
    for raw in paths:
        path = Path(raw)
        if not path.exists():
            # allow running the script from any working directory by
            # resolving paths relative to the repository root as a fallback
            path = (REPO_ROOT / raw).resolve()
        if not path.exists():
            continue
        if path.is_file() and path.suffix.lower() == ".md":
            if not any(part in excluded for part in path.parts):
                yield path
            continue
        if path.is_dir():
            for md_file in path.rglob("*.md"):
                if any(part in excluded for part in md_file.parts):
                    continue
                yield md_file


def extract_links(file_path: Path) -> Set[str]:
    text = file_path.read_text(encoding="utf-8")
    return set(match.group(1) for match in URL_PATTERN.finditer(text))


def head_request(url: str, timeout: float) -> LinkStatus:
    req = request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with request.urlopen(req, timeout=timeout) as resp:
            return LinkStatus(url=url, ok=200 <= resp.status < 400, status=resp.status)
    except error.HTTPError as exc:  # fallback to GET for method not allowed
        if exc.code in {403, 405}:
            return get_request(url, timeout)
        return LinkStatus(url=url, ok=False, status=exc.code, error=str(exc))
    except Exception as exc:  # pragma: no cover - best effort logging
        return LinkStatus(url=url, ok=False, error=str(exc))


def get_request(url: str, timeout: float) -> LinkStatus:
    req = request.Request(url, method="GET", headers={"User-Agent": USER_AGENT})
    try:
        with request.urlopen(req, timeout=timeout) as resp:
            return LinkStatus(url=url, ok=200 <= resp.status < 400, status=resp.status)
    except error.HTTPError as exc:
        return LinkStatus(url=url, ok=False, status=exc.code, error=str(exc))
    except Exception as exc:  # pragma: no cover
        return LinkStatus(url=url, ok=False, error=str(exc))


def check_link(url: str, timeout: float) -> LinkStatus:
    result = head_request(url, timeout)
    if not result.ok and result.status is None and result.error:
        # retry with GET after short delay for transient errors
        time.sleep(0.2)
        return get_request(url, timeout)
    return result


def main() -> int:
    args = parse_args()
    md_files = list(iter_markdown_files(args.paths, set(args.exclude)))
    if not md_files:
        print("No markdown files found for the provided paths.")
        return 1

    link_map: dict[str, Set[Path]] = {}
    for file_path in md_files:
        for url in extract_links(file_path):
            link_map.setdefault(url, set()).add(file_path)

    print(f"Found {len(link_map)} unique links across {len(md_files)} Markdown files.")
    failures: List[LinkStatus] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_workers) as executor:
        futures = {
            executor.submit(check_link, url, args.timeout): url for url in link_map
        }
        for future in concurrent.futures.as_completed(futures):
            status = future.result()
            if not status.ok:
                status.source_files = sorted(link_map[status.url])
                failures.append(status)
                files_list = ", ".join(str(p) for p in status.source_files)
                print(f"[FAIL] {status.url} (files: {files_list}) -> status={status.status} error={status.error}")

    if failures:
        print(f"\nDetected {len(failures)} failing links out of {len(link_map)} checked.")
        return 2

    print("All links responded with HTTP 2xx/3xx.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
