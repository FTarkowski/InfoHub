# Porównanie Tailscale, NetBird, Netmaker, Zerotier i Twingate  
Kompleksowa analiza rozwiązań VPN/Overlay/Zero-Trust dla środowisk IT, DevOps i homelabów

## Wprowadzenie
Dynamiczny rozwój środowisk rozproszonych, Kubernetes, Proxmox, chmur publicznych i pracy zdalnej wymusza stosowanie nowoczesnych rozwiązań sieciowych: automatycznych, bezpiecznych, o wysokiej wydajności i niskiej złożoności utrzymania.  
W tym artykule porównano pięć najpopularniejszych narzędzi do budowy sieci prywatnych:

- **Tailscale**
- **NetBird**
- **Netmaker**
- **Zerotier**
- **Twingate**

Analiza obejmuje architekturę, bezpieczeństwo, funkcjonalności, możliwości skalowania, ograniczenia i przykładowe przypadki użycia.

---

# 1. Charakterystyka i model działania

## 1.1 Tailscale  
Tailscale to mesh VPN oparty na WireGuard. Łączy urządzenia bezpośrednio P2P, automatycznie przechodząc przez NAT. Używa kontrolera w chmurze Tailscale, który zarządza tożsamościami, ACL i sesjami.  
Możliwa jest alternatywa w postaci **Headscale**, która zapewnia pełne self-hosting.

**Cechy wyróżniające:**
- minimalna konfiguracja (logujesz się i działa),
- wsparcie dla routing podsieci, MagicDNS, Taildrop,
- dobre wsparcie dla systemów mobilnych.

**Zastosowania:** małe i średnie sieci, szybkie projekty DevOps, dostęp do węzłów.

---

## 1.2 NetBird  
NetBird to open-source’owe rozwiązanie Zero-Trust, oparte również na WireGuard. Oferuje zarządzanie politykami dostępu w sposób znacznie bardziej granularny niż Tailscale.

**Cechy wyróżniające:**
- pełne **ZTNA** w open-source,
- zaawansowane RBAC, OIDC, polityki zasobów,
- self-hosting dostępny natywnie.

**Zastosowania:** organizacje potrzebujące pełnej kontroli, homelaby z naciskiem na bezpieczeństwo, sieci hybrydowe.

---

## 1.3 Netmaker  
Netmaker to najbardziej wydajne i skalowalne podejście do budowy sieci WireGuard w modelu mesh lub hub-and-spoke.  
To narzędzie nie jest ZTNA, lecz klasyczną overlay network.

**Cechy wyróżniające:**
- ekstremalna wydajność i skalowalność,
- wsparcie site-to-site, zaawansowany routing,
- idealny dla setek lub tysięcy hostów.

**Zastosowania:** ogromne środowiska, multi-cloud, platformy DevOps.

---

## 1.4 Zerotier  
Zerotier używa własnego protokołu i umożliwia działanie w warstwie L2/L3.  
Może działać jak wirtualny bridge VLAN w Internecie – unikalna funkcja.

**Cechy wyróżniające:**
- możliwość mostkowania L2,
- bardzo łatwa konfiguracja,
- częściowo self-hosted (kontroler), ale bootstrap pozostaje w sieci Zerotier.

**Zastosowania:** skomplikowane sieci hybrydowe, integracje z VLAN, nietypowe topologie.

---

## 1.5 Twingate  
Twingate to komercyjny ZTNA bez klasycznej sieci VPN. Dostęp odbywa się tylko do konkretnych aplikacji/zasobów, a nie całych adresów IP.

**Cechy wyróżniające:**
- pełny model Zero-Trust,
- rozbudowane integracje korporacyjne (SSO, SIEM),
- brak opcji self-host.

**Zastosowania:** duże firmy, organizacje odchodzące od tradycyjnych VPN.

---

# 2. Architektura – porównanie techniczne

| Cecha | Tailscale | NetBird | Netmaker | Zerotier | Twingate |
|------|-----------|---------|----------|----------|----------|
| Protokół | WireGuard | WireGuard | WireGuard | Własny | Własny |
| Model | Mesh VPN | ZTNA + Mesh | Mesh/Site-to-Site | SD-WAN (L2/L3) | Zero-Trust |
| Kontroler | SaaS lub self-host (Headscale) | SaaS lub self-host | self-host | Kontroler self-host + globalny bootstrap | tylko SaaS |
| NAT Traversal | Bardzo dobry | Bardzo dobry | Dobry | Dobry | Bardzo dobry |
| Skalowalność | Średnia/Wysoka | Wysoka | Bardzo wysoka | Średnia/Wysoka | Wysoka |

---

# 3. Bezpieczeństwo i Zero-Trust

## Tailscale
- ACLs, logowanie przez SSO,
- model zero-trust, lecz oparty o chmurę Tailscale.

## NetBird
- najpełniejsza implementacja ZTNA w open-source,
- OIDC, RBAC, granularny dostęp do zasobów.

## Netmaker
- klasyczna sieć overlay, brak natywnego ZTNA,
- bezpieczeństwo zależy od architektury WireGuard.

## Zerotier
- kontrola dostępu na poziomie sieci,
- brak ZTNA.

## Twingate
- pełny Zero-Trust: użytkownik nigdy nie widzi „sieci”, tylko zasoby.

**Najlepsze w kategorii ZTNA:**  
1. Twingate  
2. NetBird  
3. Tailscale  
4. Zerotier  
5. Netmaker

---

# 4. Funkcjonalności

| Funkcja | Tailscale | NetBird | Netmaker | Zerotier | Twingate |
|--------|-----------|---------|----------|----------|----------|
| Mesh VPN | ✔️ | ✔️ | ✔️ | ✔️ | ❌ |
| Zero-Trust | częściowo | ✔️ | ❌ | ❌ | ✔️ |
| Routing podsieci | ✔️ | ✔️ | ✔️ (bardzo rozwinięte) | ✔️ | ✔️ |
| L2 Bridge | ❌ | ❌ | ❌ | ✔️ | ❌ |
| Self-host | ✔️ | ✔️ | ✔️ | ✔️ | ❌ |
| Integracje SSO | ✔️ | ✔️ | ✔️ | ❌ | ✔️ |
| Skalowanie powyżej 500 hostów | ✔️ | ✔️ | ✔️ (idealne) | częściowo | ✔️ |

---

# 5. Wydajność i realne osiągi

### WireGuard (Tailscale, NetBird, Netmaker)
- 500–1000 Mbit/s na typowym CPU,
- niskie opóźnienia,
- szyfrowanie nowoczesnymi algorytmami.

### Zerotier
- 150–300 Mbit/s,
- protokół bardziej ogólny, niższe osiągi.

### Twingate
- dynamiczny wybór tras,
- wydajność zależy od regionu i klasy subskrypcji.

**Ranking wydajności (ogólny):**
1. **Netmaker**  
2. **Tailscale**  
3. **NetBird**  
4. **Twingate**  
5. **Zerotier**

---

# 6. Trudność wdrożenia

### Najprostsze:
1. **Tailscale**
2. **Zerotier**

### Średnia trudność:
3. **Twingate**
4. **NetBird**

### Najtrudniejsze:
5. **Netmaker**  
(wymaga wiedzy sieciowej i admina)

---

# 7. Zalety i wady

## Tailscale
**Zalety:**  
- prostota, stabilność, bardzo duża społeczność, świetna dokumentacja.

**Wady:**  
- w wersji SaaS brak pełnej kontroli, część funkcji płatna.

---

## NetBird
**Zalety:**  
- najlepszy open-source ZTNA, pełny self-host, elastyczne polityki.

**Wady:**  
- mniejsza popularność, wymaga wiedzy o politykach dostępu.

---

## Netmaker
**Zalety:**  
- absolutnie najwyższa wydajność i skalowalność WireGuard,
- idealny dla dużych i złożonych środowisk.

**Wady:**  
- wysokie wymagania administracyjne, brak ZTNA.

---

## Zerotier
**Zalety:**  
- L2 bridging, elastyczne i szybkie wdrożenie,
- dobry do nietypowych topologii.

**Wady:**  
- protokół zamknięty, mniejsza wydajność.

---

## Twingate
**Zalety:**  
- pełny Zero-Trust dla firm, wysoka kontrola i bezpieczeństwo.

**Wady:**  
- brak self-host, mocno komercyjny model.

---

# 8. Skala możliwości – oceny 1–10

| Kategorie | Tailscale | NetBird | Netmaker | Zerotier | Twingate |
|----------|-----------|---------|----------|----------|----------|
| Wydajność | 9 | 8 | 10 | 6 | 7 |
| Zero-Trust | 6 | 9 | 5 | 6 | 10 |
| Prostota | 10 | 7 | 5 | 9 | 8 |
| Self-host | 8 | 10 | 10 | 9 | 0 |
| Mobilność | 10 | 8 | 7 | 9 | 8 |
| Routing podsieci | 8 | 8 | 10 | 8 | 9 |
| L2 bridging | 0 | 0 | 0 | 10 | 0 |
| Skalowalność | 8 | 8 | 10 | 7 | 9 |
| DevOps-friendly | 8 | 9 | 10 | 6 | 7 |

---

# 9. Rekomendacje według zastosowań

### Homelab, Proxmox, Docker, KVM  
→ **Tailscale** lub **NetBird**  
(szybko, stabilnie, nowocześnie)

### Multi-cloud, duże sieci, Kubernetes  
→ **Netmaker**

### Sieci warstwy L2 / bridging / VLAN w Internecie  
→ **Zerotier**

### Środowisko korporacyjne / Zero-Trust bez VPN  
→ **Twingate**

### Proste i bezproblemowe użycie  
→ **Tailscale**

---

# 10. Podsumowanie

Wybór zależy od potrzeb:

- **Tailscale** – najlepsze połączenie prostoty, funkcjonalności i wydajności.  
- **NetBird** – najlepsze darmowe Zero-Trust w pełni open-source.  
- **Netmaker** – idealny dla dużych, profesjonalnych infrastruktur z setkami hostów.  
- **Zerotier** – jedyny z L2 bridging, elastyczny, ale mniej wydajny.  
- **Twingate** – najlepszy Zero-Trust dla firm, ale zamknięty i SaaS-only.

Każda z technologii ma unikalne cechy – dlatego wybór powinien być podyktowany architekturą, skalą i poziomem bezpieczeństwa potrzebnym w środowisku.
