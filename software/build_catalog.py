import json
from pathlib import Path

DATA_PATH = Path(__file__).with_name('tools.json')

SECTION_FILES = {
    'server.md': {
        'title': 'Serwerowe i storage',
        'sections': [
            ('Hiperwizor typu 1', 'Hiperwizory typu 1'),
            ('Hiperwizor typu 2', 'Hiperwizory typu 2'),
            ('NAS, Chmura, Synchronizacja', 'NAS, chmura i synchronizacja'),
            ('Zarządzanie Danymi i Backup', 'Zarządzanie danymi i backup'),
            ('ERP i Zarządzanie Firmą', 'ERP i zarządzanie firmą'),
            ('Serwery plików self-hosted', 'Serwery plików self-hosted'),
            ('Platformy IoT open-source', 'Platformy IoT open-source'),
        ],
    },
    'multimedia.md': {
        'title': 'Multimedia i edycja',
        'sections': [
            ('Aplikacje Multimedialne', 'Aplikacje multimedialne'),
            ('Edytory wideo', 'Edytory i narzędzia wideo'),
        ],
    },
    'it-tools.md': {
        'title': 'Systemy i narzędzia IT',
        'sections': [
            ('Systemy', 'Systemy i dashboardy'),
            ('Zarządzanie', 'Zarządzanie i produktywność zespołowa'),
            ('Komunikacja', 'Helpdesk i komunikacja'),
            ('Produktywność', 'Produktywność osobista'),
            ('Narzędzia', 'Narzędzia uniwersalne'),
        ],
    },
    'linux.md': {
        'title': 'Linux – aplikacje desktopowe',
        'sections': [
            ('System / Monitoring', 'System / Monitoring'),
            ('Zarządzanie plikami i obrazami', 'Zarządzanie plikami i obrazami'),
            ('Programistyczne i narzędzia', 'Programistyczne i narzędzia'),
            ('Notatki i organizacja', 'Notatki i organizacja'),
            ('Terminale i emulatory', 'Terminale i emulatory'),
            ('Menedżery plików', 'Menedżery plików'),
        ],
    },
    'security.md': {
        'title': 'Bezpieczeństwo i sieć',
        'sections': [
            ('Analiza malware i reverse engineering', 'Analiza malware i RE'),
            ('VPN self-hosted', 'VPN self-hosted'),
            ('Blokowanie reklam · Przeglądarki', 'Blokowanie reklam – przeglądarki'),
            ('Blokowanie reklam · Rozszerzenia', 'Blokowanie reklam – rozszerzenia'),
            ('Blokowanie reklam · DNS', 'Blokowanie reklam – DNS'),
            ('Blokowanie reklam · Zapory', 'Blokowanie reklam – zapory'),
            ('Blokowanie reklam · Proxy', 'Blokowanie reklam – proxy'),
        ],
    },
    'editors.md': {
        'title': 'Edytory i środowiska programistyczne',
        'sections': [
            ('Edytory i Środowiska Programistyczne', 'Edytory i IDE'),
        ],
    },
}

README_TEMPLATE = """# Software Hub\nCentralny katalog aplikacji, systemów i narzędzi wspierających codzienną pracę administratorów oraz zespołów IT.\n\n## Jak czytać tabelę\n- **Nazwa** – nazwa projektu; kliknij ikonę 🔗, aby przejść do strony domowej.\n- **Opis** – jednozdaniowy opis funkcji rozwiązania.\n- **Licencja** – `Open Source` oznacza dostęp do kodu, `Proprietary` rozwiązania zamknięte.\n- **Self-hosted** – ikona 🟢 oznacza możliwość instalacji we własnej infrastrukturze, ⚪️ – aplikacja desktopowa/SaaS.\n\n## Spis treści\n- [Serwerowe i storage](server.md)\n- [Multimedia i edycja](multimedia.md)\n- [Systemy i narzędzia IT](it-tools.md)\n- [Linux – aplikacje desktopowe](linux.md)\n- [Bezpieczeństwo i sieć](security.md)\n- [Edytory i środowiska programistyczne](editors.md)\n"""


def load_items():
    return json.loads(DATA_PATH.read_text())

def build_table(items):
    if not items:
        return 'Brak wpisów w tej kategorii.\n'
    header = '| Nazwa | Opis | Licencja | Self-hosted | Link |\n| --- | --- | --- | --- | --- |\n'
    rows = []
    for item in items:
        icon = '🟢' if item['self_hosted'] else '⚪️'
        link = f"[🔗]({item['url']})"
        desc = item['description'].replace('|', '\\|')
        rows.append(f"| **{item['name']}** | {desc} | {item['license']} | {icon} | {link} |")
    return header + '\n'.join(rows) + '\n'

def write_sections(data):
    base = Path('software')
    for filename, conf in SECTION_FILES.items():
        lines = [f"# {conf['title']}", 'Powrót: [Software Hub](README.md)', '']
        for category, label in conf['sections']:
            subset = [item for item in data if item['category'] == category]
            lines.append(f"## {label}")
            lines.append(build_table(subset))
        (base / filename).write_text('\n'.join(lines).rstrip() + '\n')

def write_readme():
    Path('software/README.md').write_text(README_TEMPLATE.strip() + '\n')

def main():
    data = load_items()
    write_sections(data)
    write_readme()

if __name__ == '__main__':
    main()
