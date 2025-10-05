# Projekt zarządzania infrastrukturą za pomocą Ansible i Semaphore UI

Ten projekt opisuje, w jaki sposób na maszynie z Debianem 12 (bookworm) wyposażonej w Dockera można:

1. Zainstalować Ansible (CLI) oraz jego podstawowe zależności.
2. Uruchomić graficzny interfejs użytkownika w postaci [Ansible Semaphore](https://github.com/semaphoreui/semaphore).
3. Przygotować przykładowe inwentarze i playbooki do zarządzania innymi hostami.
4. Automatyzować dalszy rozwój i utrzymanie środowiska.

> **Uwaga**: Semaphore to lekki, otwartoźródłowy interfejs WWW dla Ansible. Do wygodnej pracy wystarczą 2 vCPU, 2–4 GB RAM i ok. 5 GB wolnej przestrzeni dyskowej.

---

## 1. Przygotowanie hosta (Debian 12 + Docker)

1. Upewnij się, że system jest zaktualizowany:
   ```bash
   sudo apt update && sudo apt full-upgrade -y
   ```
2. Zainstaluj podstawowe narzędzia:
   ```bash
   sudo apt install -y curl git python3 python3-venv python3-pip sshpass
   ```
3. Zweryfikuj wersję Dockera:
   ```bash
   docker --version
   ```
4. Dodaj bieżącego użytkownika do grupy `docker`, jeśli jeszcze nie zrobiłeś/aś:
   ```bash
   sudo usermod -aG docker $USER
   newgrp docker
   ```

---

## 2. Instalacja Ansible (CLI)

### 2.1 Instalacja z repozytorium Debian Backports (najłatwiejsza)

```bash
# dodanie repozytorium backports (jeśli jeszcze nie dodane)
echo "deb http://deb.debian.org/debian bookworm-backports main" | sudo tee /etc/apt/sources.list.d/backports.list
sudo apt update
sudo apt install -y ansible-core -t bookworm-backports
```

### 2.2 Instalacja w wirtualnym środowisku Python (zalecana dla izolacji)

```bash
python3 -m venv ~/.venvs/ansible
source ~/.venvs/ansible/bin/activate
pip install --upgrade pip
pip install ansible ansible-lint
```

> Po aktywacji wirtualnego środowiska polecenia `ansible`, `ansible-playbook`, `ansible-galaxy` będą dostępne z zainstalowanej wersji.

### 2.3 Konfiguracja podstawowa

1. Utwórz katalog roboczy, np. `/opt/ansible` (jeśli nie używasz repozytorium Git takiego jak ten projekt).
2. Skopiuj foldery `inventory/` i `playbooks/` z tego repozytorium jako bazę.
3. Ustal zmienne środowiskowe w pliku `~/.ansible.cfg` (opcjonalne):
   ```ini
   [defaults]
   inventory = ~/AnsibleProjects/inventory/hosts.ini
   host_key_checking = False
   retry_files_enabled = False
   forks = 20
   ```

---

## 3. Uruchomienie Semaphore (UI dla Ansible)

Semaphore uruchomisz przy pomocy dostarczonego pliku `docker-compose.yml`.

### 3.1 Wymagania
- Docker Engine ≥ 24
- Docker Compose v2 (polecenie `docker compose`)
- Co najmniej 2 vCPU oraz 2 GB RAM (dla większych środowisk zalecane 4 GB)
- Otworzony port 3000/TCP na hoście (panel WWW)

### 3.2 Szybki start

1. Skopiuj pliki z folderu `Ansible prj` na hosta, np. do `/opt/ansible-semaphore`.
2. Ustaw/zaktualizuj wartości w `env/semaphore.env` (login, hasło, adres e-mail, parametry bazy danych).
3. Uruchom Semaphore:
   ```bash
   cd /opt/ansible-semaphore
   docker compose up -d
   ```
4. Sprawdź status kontenerów i logi:
   ```bash
   docker compose ps
   docker compose logs -f semaphore
   ```
5. Po kilkudziesięciu sekundach interfejs powinien być dostępny na `http://<IP_DEBIANA>:3000`.

### 3.3 Domyślne dane logowania
- Użytkownik: `admin`
- Hasło: `changeme`
- E-mail: `admin@example.local`

Hasło i dane administratora zmienisz edytując plik `env/semaphore.env` przed uruchomieniem lub w panelu po pierwszym logowaniu.

### 3.4 Konfiguracja Semaphore po instalacji
1. Zaloguj się do panelu.
2. Przejdź przez kreator inicjalizacyjny i utwórz **Project**.
3. Dodaj **Inventory** korzystając z pliku `inventory/hosts.ini` (możesz wskazać repozytorium Git lub lokalną ścieżkę z wolumenu `/var/lib/semaphore`).
4. W sekcji **Credentials** skonfiguruj dane do logowania SSH (login + klucz lub hasło).
5. Dodaj **Repository** (np. to repozytorium Git) i przypisz do projektu.
6. Utwórz **Task Template**, wskazując projekt, credential, inventory i playbook (`playbooks/ping.yml`).
7. Uruchom zadanie i monitoruj logi w zakładce **Tasks**.

---

## 4. Struktura projektu

```
Ansible prj/
├── README.md                  # Ten plik z instrukcjami
├── docker-compose.yml         # Definicja stacka Semaphore + Postgres
├── env/semaphore.env          # Zmienne środowiskowe (dostosuj przed uruchomieniem)
├── inventory/
│   └── hosts.ini              # Przykładowy inwentarz
└── playbooks/
    ├── ping.yml               # Prosty playbook testujący połączenie
    └── update-packages.yml    # Przykład aktualizacji systemu
```

Folder `env/` oddziela dane konfiguracyjne. W środowisku produkcyjnym przechowuj hasła i tokeny w menedżerze sekretów.

---

## 5. Przykładowe inwentarze i playbooki

### 5.1 Inwentarz (`inventory/hosts.ini`)
Plik zawiera przykładową grupę hostów zarządzanych przez Ansible. Możesz go rozszerzać o kolejne sekcje oraz zmienne grupowe/hostowe.

### 5.2 Playbooki
- `playbooks/ping.yml`: testuje łączność (`ansible.builtin.ping`).
- `playbooks/update-packages.yml`: aktualizuje pakiety na hostach Ubuntu/Debian.

Uruchomienie przykładowego playbooka:
```bash
ansible-playbook -i inventory/hosts.ini playbooks/ping.yml
```

---

## 6. Najczęstsze zadania w Semaphore/Ansible

| Zadanie                           | Gdzie w Semaphore?                     | Komentarz |
|-----------------------------------|----------------------------------------|-----------|
| Dodanie hosta                     | *Projects → Inventories*               | Możesz importować pliki INI/YAML lub korzystać z Git. |
| Przechowywanie poświadczeń        | *Projects → Credentials*               | Obsługa wielu typów (SSH, Vault, Tokeny chmur publicznych). |
| Planowanie zadań                  | *Projects → Schedules*                 | Umożliwia cykliczne uruchamianie task templates. |
| Przegląd logów                    | *Tasks → <nazwa zadania>*              | Dostęp do szczegółowych logów i historii uruchomień. |
| Integracja z Git                  | *Projects → Repositories*              | Automatyczne pobieranie playbooków z repozytoriów. |
| Notyfikacje                       | *Projects → Notifications*             | Webhooki, e-mail i inne integracje. |

---
