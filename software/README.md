# 🧩 Software Hub
Centralny katalog aplikacji, systemów i narzędzi wspierających codzienną pracę administratorów oraz zespołów IT.

## 🧭 Spis treści
- [Oprogramowania](#oprogramowania)
  - [Serwerowe](#serwerowe)
    - [Hiperwizor typu 1](#hiperwizor-typu-1)
    - [Hiperwizor typu 2](#hiperwizor-typu-2)
    - [NAS, Chmura, Synchronizacja](#nas-chmura-synchronizacja)
    - [Zarządzanie Danymi i Backup](#zarzadzanie-danymi-i-backup)
    - [ERP i Zarządzanie Firmą](#erp-i-zarzadzanie-firma)
  - [Aplikacje Multimedialne](#aplikacje-multimedialne)
  - [Aplikacje i Narzędzia IT](#aplikacje-i-narzedzia-it)
    - [Systemy](#systemy)
    - [Zarządzanie](#zarzadzanie)
    - [Komunikacja](#komunikacja)
    - [Produktywność](#produktywnosc)
    - [Narzędzia](#narzedzia)
  - [Linux – Aplikacje](#linux--aplikacje)
    - [System / Monitoring](#system--monitoring)
    - [Zarządzanie plikami i obrazami](#zarzadzanie-plikami-i-obrazami)
    - [Programistyczne i narzędzia](#programistyczne-i-narzedzia)
    - [Notatki i organizacja](#notatki-i-organizacja)
    - [Terminale i emulatory](#terminale-i-emulatory)
    - [Edytory wideo](#edytory-wideo)
    - [Serwery plików self-hosted](#serwery-plikow-self-hosted)
    - [Analiza malware i reverse engineering](#analiza-malware-i-reverse-engineering)
    - [VPN self-hosted](#vpn-self-hosted)
    - [Menedżery plików](#menedzery-plikow)
    - [Platformy IoT open-source](#platformy-iot-open-source)
    - [Blokowanie reklam](#blokowanie-reklam)
  - [Edytory i Środowiska Programistyczne](#edytory-i-srodowiska-programistyczne)

---

### Oprogramowania

#### Serwerowe

##### Hiperwizor typu 1
<!--<img src="https://cdn.simpleicons.org/proxmox/E57000" width="16" height="16"/> -->
- **Proxmox** – Platforma wirtualizacji serwerów <a href="https://www.proxmox.com/" target="_blank">(Link)</a>.
- **VMware ESXi** – Rozwiązanie do wirtualizacji serwerów <a href="https://www.vmware.com/" target="_blank">(Link)</a>.
- **Hyper-V** – Wirtualizacja Microsoft <a href="https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/" target="_blank">(Link)</a>.

##### Hiperwizor typu 2
- **VirtualBox** – Wirtualizacja na systemie operacyjnym <a href="https://www.virtualbox.org/" target="_blank">(Link)</a>.

##### NAS, Chmura, Synchronizacja
- **TrueNAS** – Oprogramowanie NAS <a href="https://www.truenas.com/" target="_blank">(Link)</a>.
- **TrueNAS Scale** – NAS z obsługą kontenerów <a href="https://www.truenas.com/truenas-scale/" target="_blank">(Link)</a>.
- **UNAS Pro** – Rozwiązanie NAS dla profesjonalistów <a href="https://www.unas.com/" target="_blank">(Link)</a>.
- **Nextcloud** – Chmura osobista <a href="https://nextcloud.com/" target="_blank">(Link)</a>.
- **docker-dropbox-app** – Self-hosted Dropbox API w Dockerze <a href="https://github.com/rbonghi/docker-dropbox-app" target="_blank">(Link)</a>.
- **Syncthing** – Zdecentralizowana synchronizacja plików P2P z szyfrowaniem end-to-end i wersjonowaniem <a href="https://syncthing.net/" target="_blank">(Link)</a>.
- **CasaOS** – System zarządzania aplikacjami domowymi <a href="https://casaos.io/" target="_blank">(Link)</a>.
- **File Browser** – Menedżer plików przez przeglądarkę <a href="https://filebrowser.org/" target="_blank">(Link)</a>.
- **HexOS** – System operacyjny dla środowiska NAS.
- **OpenMediaVault** – Rozwiązanie NAS oparte na Debianie <a href="https://www.openmediavault.org/" target="_blank">(Link)</a>.
- **openmediavault-webdesk** – GUI dla OMV w Docker Compose <a href="https://github.com/TwanoO67/omv-web-desk" target="_blank">(Link)</a>
- **Unraid** – System operacyjny dla serwerów NAS z obsługą wirtualizacji i Docker <a href="https://unraid.net/" target="_blank">(Link)</a>.
- **Portainer + Nextcloud stack** – docker-compose do prostego wdrożenia portainer/nextcloud <a href="https://github.com/tv0ll/portainer-nextcloud" target="_blank">(Link)</a>

##### Zarządzanie Danymi i Backup
- **Proxmox Backup Server (PBS)** – Backup dla Proxmox <a href="https://www.proxmox.com/en/proxmox-backup-server" target="_blank">(Link)</a>.

##### ERP i Zarządzanie Firmą
- **ERPNext** – Oprogramowanie ERP oparte na Pythonie <a href="https://github.com/frappe/erpnext" target="_blank">(Link)</a>.

---

#### Aplikacje Multimedialne
- **Plex** – Strumieniowanie multimediów <a href="https://www.plex.tv/" target="_blank">(Link)</a>.
- **Sonarr** – Pobieranie seriali <a href="https://sonarr.tv/" target="_blank">(Link)</a>.
- **Radarr** – Pobieranie filmów <a href="https://radarr.video/" target="_blank">(Link)</a>.
- **Jellyfin** – Serwer multimedialny open-source <a href="https://jellyfin.org/" target="_blank">(Link)</a>.
- **PhotoPrism** – Zarządzanie zdjęciami <a href="https://github.com/photoprism/photoprism" target="_blank">(Link)</a>
- **PhotoPrism w Portainer / Docker Compose** – Oficjalna konfiguracja <a href="https://docs.photoprism.app/getting-started/portainer/" target="_blank">(Docs)</a> | <a href="https://docs.photoprism.app/getting-started/docker-compose/" target="_blank">(Compose)</a>
- **Immich** – Samohostowana platforma do zarządzania zdjęciami i wideo <a href="https://github.com/immich-app/immich" target="_blank">(Link)</a>
- **HandBrake** – Open-source narzędzie do transkodowania wideo <a href="https://github.com/HandBrake/HandBrake" target="_blank">(Link)</a>
- **SABnzbd** – Klient Usenet <a href="https://sabnzbd.org/" target="_blank">(Link)</a>.
- **Transmission** – Klient BitTorrent <a href="https://transmissionbt.com/" target="_blank">(Link)</a>.
- **qBittorrent** – Klient BitTorrent <a href="https://www.qbittorrent.org/" target="_blank">(Link)</a>.
- **Qui** – Webowy frontend do zarządzania autobrr i automatycznymi pobraniami <a href="https://github.com/autobrr/qui" target="_blank">(Link)</a>.
- **Whisparr** – Zarządzanie treściami <a href="https://github.com/Whisparr/Whisparr" target="_blank">(Link)</a>.
- **Bazarr** – Napisy do multimediów <a href="https://www.bazarr.media/" target="_blank">(Link)</a>.
- **Prowlarr** – Indeksatory do PVR <a href="https://prowlarr.com/" target="_blank">(Link)</a>.
- **Jellyseer** – Zarządzanie żądaniami Jellyfin <a href="https://github.com/Fallenbagel/jellyseerr" target="_blank">(Link)</a>.
- **Jitsi** – Open-source platforma wideokonferencyjna <a href="https://github.com/jitsi" target="_blank">(Link)</a>.
- **OpenBooks** – Biblioteka e-booków (brak linku)

---

#### Aplikacje i Narzędzia IT

##### Systemy
- **Home Assistant** – Automatyzacja domu <a href="https://www.home-assistant.io/" target="_blank">(Link)</a>
- **GetHomepage** – Strona główna aplikacji <a href="https://gethomepage.dev/" target="_blank">(Link)</a>
- **Heimdall** – Dashboard do aplikacji <a href="https://heimdall.site/" target="_blank">(Link)</a>
- **Dashy** – Konfigurowalny dashboard aplikacji <a href="https://dashy.to/" target="_blank">(Link)</a>
- **Homer** – Prostota w zarządzaniu interfejsem <a href="https://github.com/bastienwirtz/homer" target="_blank">(Link)</a>
- **Homie** – Lekka strona-startowa i dashboard linków dla self-hosted <a href="https://github.com/Brramble/homie" target="_blank">(Link)</a>

##### Zarządzanie
- **Vault / Bitwarden** – Menedżer haseł <a href="https://bitwarden.com/" target="_blank">(Link)</a>
- **Vaultwarden** – Alternatywa self-hosted dla Bitwarden <a href="https://github.com/dani-garcia/vaultwarden" target="_blank">(Link)</a>
- **Plane** – System do zarządzania projektami <a href="https://github.com/makeplane/plane" target="_blank">(Link)</a>
- **Taskcafe** – Tablicowy system zarządzania zadaniami <a href="https://github.com/JordanKnott/taskcafe" target="_blank">(Link)</a>
- **Planka** – Alternatywa Trello <a href="https://github.com/plankanban/planka" target="_blank">(Link)</a>
- **Asana** – SaaS do zarządzania projektami <a href="https://asana.com/pl" target="_blank">(Link)</a>

##### Komunikacja
- **Typebot** – Interaktywne chatboty <a href="https://github.com/baptisteArno/typebot.io" target="_blank">(Link)</a>
- **Formbricks** – Feedback i ankiety <a href="https://github.com/formbricks/formbricks" target="_blank">(Link)</a>
- **osTicket** – System zgłoszeniowy <a href="https://github.com/osTicket/osTicket" target="_blank">(Link)</a>
- **Helpy** – Helpdesk z bazą wiedzy <a href="https://github.com/helpyio/helpy" target="_blank">(Link)</a>
- **Zammad** – Helpdesk/ticketing <a href="https://github.com/zammad/zammad" target="_blank">(Link)</a>
- **Faveo Helpdesk** – Obsługa zgłoszeń z panelem klienta <a href="https://github.com/faveosuite/faveo-helpdesk" target="_blank">(Link)</a>
- **FreeScout** – Lekki helpdesk <a href="https://github.com/freescout-help-desk/freescout" target="_blank">(Link)</a>

##### Produktywność
- **AppFlowy** – Alternatywa dla Notion <a href="https://github.com/AppFlowy-IO/AppFlowy" target="_blank">(Link)</a>
- **LibreOffice Docker** – Pakiet biurowy <a href="https://hub.docker.com/r/linuxserver/libreoffice" target="_blank">(Link)</a>
- **ONLYOFFICE** – Pakiet biurowy do dokumentów, arkuszy i prezentacji <a href="https://github.com/ONLYOFFICE" target="_blank">(Link)</a>
- **NocoDB** – Baza danych jako usługa <a href="https://github.com/nocodb/nocodb" target="_blank">(Link)</a>
- **InstantDB** – Lekka baza danych <a href="https://github.com/instantdb/instant" target="_blank">(Link)</a>
- **Velld** – Prosty menedżer zadań i notatek w stylu Markdown <a href="https://github.com/dendianugerah/velld" target="_blank">(Link)</a>
- **IronCalc** – Arkusz kalkulacyjny online z obsługą formuł i importów <a href="https://github.com/ironcalc/IronCalc" target="_blank">(Link)</a>
- **Paperless-ngx** – System OCR i zarządzania dokumentami dla self-hosted <a href="https://github.com/paperless-ngx/paperless-ngx" target="_blank">(Link)</a>

##### Narzędzia
- **it-tools** – Narzędzia IT w przeglądarce <a href="https://it-tools.tech/" target="_blank">(Link)</a>
- **Dangerzone** – Konwersja dokumentów PDF <a href="https://github.com/freedomofpress/dangerzone" target="_blank">(Link)</a>
- **Stirling PDF** – Edycja i łączenie PDF <a href="https://github.com/sirting-pdf/stirling-pdf" target="_blank">(Link)</a>
- **ConvertX** – Konwerter plików <a href="https://github.com/svenstaro/convertx" target="_blank">(Link)</a>
- **Excalidraw** – Edytor diagramów <a href="https://github.com/excalidraw/excalidraw" target="_blank">(Link)</a>
- **Draw.io (self-host)** – Diagramy online <a href="https://github.com/jgraph/drawio" target="_blank">(Link)</a>

---

#### Linux – Aplikacje

##### System / Monitoring
- **Resources** – Monitor zasobów (CPU, RAM, sieć, procesy) w GTK <a href="https://github.com/nokyan/resources" target="_blank">(Link)</a>.
- **Mission Center** – Zaawansowany monitor systemu z rozbudowanym UI <a href="https://flathub.org/apps/io.missioncenter.MissionCenter" target="_blank">(Link)</a>.
- **Monitorets** – Minimalistyczny monitor zasobów z wykresami <a href="https://flathub.org/apps/io.github.jorchube.monitorets" target="_blank">(Link)</a>.
- **LACT** – Kontroler GPU AMD (taktowania, limity mocy, profile) <a href="https://flathub.org/apps/io.github.ilgarmehmetali.lact" target="_blank">(Link)</a>.
- **Gear Lever** – Narzędzie do montowania i zarządzania dyskami <a href="https://flathub.org/apps/it.mijorus.gearlever" target="_blank">(Link)</a>.
- **PiMan** – Dashboard do monitoringu Raspberry Pi (temperatura, CPU, RAM) <a href="https://github.com/GalwayCal/piman" target="_blank">(Link)</a>.
- **GPU Hot** – Monitor temperatur i użycia GPU <a href="https://github.com/psalias2006/gpu-hot" target="_blank">(Link)</a>.

##### Zarządzanie plikami i obrazami
- **Switcheroo** – Batch resize i konwersja obrazów <a href="https://flathub.org/apps/io.gitlab.adhami3310.Switcheroo" target="_blank">(Link)</a>.
- **Converseen** – Zaawansowana konwersja i kompresja obrazów <a href="https://flathub.org/apps/net.fasterland.converseen" target="_blank">(Link)</a>.
- **Pipeline** – Budowanie i uruchamianie pipeline'ów bez skryptów <a href="https://gitlab.com/schmiddi-on-mobile/pipeline" target="_blank">(Link)</a>.

##### Programistyczne i narzędzia
- **DevToolbox** – Zbiór narzędzi developerskich (JSON, hash, Base64) <a href="https://flathub.org/apps/me.iepure.devtoolbox" target="_blank">(Link)</a>.
- **Clapgrep** – GUI do szybkiego wyszukiwania w plikach <a href="https://flathub.org/apps/de.leopoldluley.Clapgrep" target="_blank">(Link)</a>.
- **Warehouse** – Menedżer Flatpaków do instalacji i uprawnień <a href="https://flathub.org/apps/io.github.flattool.Warehouse" target="_blank">(Link)</a>.

##### Notatki i organizacja
- **Speech Note** – Notatki głosowe z transkrypcją STT <a href="https://flathub.org/apps/net.mkiol.SpeechNote" target="_blank">(Link)</a>.
- **Errands** – Minimalistyczny menedżer zadań w stylu GNOME <a href="https://flathub.org/apps/io.github.mrvladus.List" target="_blank">(Link)</a>.
- **Planify** – Rozbudowany menedżer zadań z synchronizacją <a href="https://flathub.org/apps/io.github.alainm23.planify" target="_blank">(Link)</a>.
- **Klevernotes** – Notatki z obsługą Markdown i folderów <a href="https://flathub.org/apps/org.kde.klevernotes" target="_blank">(Link)</a>.
- **Iotas** – Minimalistyczna aplikacja do szybkich notatek (GNOME) <a href="https://flathub.org/apps/org.gnome.World.Iotas" target="_blank">(Link)</a>.

##### Terminale i emulatory
- **Alacritty** – Wydajny emulator terminala napisany w Rust <a href="https://github.com/alacritty/alacritty" target="_blank">(Link)</a>.
- **Black Box** – Nowoczesny emulator terminala dla GNOME <a href="https://gitlab.gnome.org/raggesilver/blackbox" target="_blank">(Link)</a>.
- **Contour** – Terminal z obsługą GPU i rozszerzonym renderingiem <a href="https://github.com/contour-terminal/contour" target="_blank">(Link)</a>.
- **Foot** – Lekki emulator Wayland <a href="https://codeberg.org/dnkl/foot" target="_blank">(Link)</a>.
- **GNOME Terminal** – Domyślny terminal środowiska GNOME <a href="https://gitlab.gnome.org/GNOME/gnome-terminal" target="_blank">(Link)</a>.
- **Guake** – Terminal typu dropdown inspirowany Quake <a href="https://github.com/Guake/guake" target="_blank">(Link)</a>.
- **Hyper** – Terminal oparty na technologiach webowych <a href="https://github.com/vercel/hyper" target="_blank">(Link)</a>.
- **iTerm2** – Rozbudowany terminal dla macOS <a href="https://iterm2.com" target="_blank">(Link)</a>.
- **Kitty** – Terminal z akceleracją GPU <a href="https://github.com/kovidgoyal/kitty" target="_blank">(Link)</a>.
- **Konsole** – Emulator terminala KDE <a href="https://invent.kde.org/utilities/konsole" target="_blank">(Link)</a>.
- **LXTerminal** – Lekki terminal środowiska LXDE <a href="https://github.com/lxde/lxterminal" target="_blank">(Link)</a>.
- **M-x term / ansi-term / vterm** – Terminale wewnątrz Emacsa <a href="https://www.gnu.org/software/emacs/" target="_blank">(Link)</a>.
- **st** – Minimalistyczny terminal suckless <a href="https://git.suckless.org/st" target="_blank">(Link)</a>.
- **Terminator** – Terminal z podziałem okien <a href="https://github.com/gnome-terminator/terminator" target="_blank">(Link)</a>.
- **Terminology** – Terminal środowiska Enlightenment <a href="https://github.com/Enlightenment/terminology" target="_blank">(Link)</a>.
- **Tilix** – Terminal kafelkowy z sesjami <a href="https://github.com/gnunn1/tilix" target="_blank">(Link)</a>.
- **urxvt** – Zaawansowany terminal RXVT-Unicode <a href="http://software.schmorp.de/pkg/rxvt-unicode.html" target="_blank">(Link)</a>.
- **Warp** – Terminal z funkcjami współpracy <a href="https://www.warp.dev" target="_blank">(Link)</a>.
- **WezTerm** – Terminal GPU z wbudowanym multiplexingiem <a href="https://github.com/wez/wezterm" target="_blank">(Link)</a>.
- **Xfce4 Terminal** – Terminal środowiska Xfce <a href="https://gitlab.xfce.org/apps/xfce4-terminal" target="_blank">(Link)</a>.
- **Xterm** – Klasyczny emulator terminala X11 <a href="https://invisible-island.net/xterm" target="_blank">(Link)</a>.

##### Edytory wideo
- **Olive** – Nieliniowy edytor wideo open-source <a href="https://github.com/olive-editor/olive" target="_blank">(Link)</a>.
- **DaVinci Resolve** – Profesjonalny pakiet montażowy <a href="https://www.blackmagicdesign.com/products/davinciresolve" target="_blank">(Link)</a>.
- **Blender** – Kompleksowe środowisko 3D z montażem wideo <a href="https://www.blender.org" target="_blank">(Link)</a>.
- **Reaper** – Zaawansowana stacja robocza audio-wideo <a href="https://www.reaper.fm" target="_blank">(Link)</a>.
- **OpenShot** – Prostota montażu open-source <a href="https://github.com/OpenShot/openshot-qt" target="_blank">(Link)</a>.
- **HandBrake** – Transkodowanie i konwersja materiałów wideo <a href="https://github.com/HandBrake/HandBrake" target="_blank">(Link)</a>.
- **Shotcut** – Cross-platformowy edytor oparty na MLT <a href="https://github.com/mltframework/shotcut" target="_blank">(Link)</a>.
- **FFmpeg** – Narzędzia CLI do obróbki audio/wideo <a href="https://github.com/FFmpeg/FFmpeg" target="_blank">(Link)</a>.
- **Lightworks** – Profesjonalny NLE <a href="https://lwks.com" target="_blank">(Link)</a>.
- **Pitivi** – Edytor wideo GNOME <a href="https://gitlab.gnome.org/GNOME/pitivi" target="_blank">(Link)</a>.
- **Kdenlive** – Zaawansowany edytor KDE <a href="https://invent.kde.org/multimedia/kdenlive" target="_blank">(Link)</a>.
- **OBS Studio** – Nagrywanie i streaming wideo <a href="https://github.com/obsproject/obs-studio" target="_blank">(Link)</a>.
- **LiVES** – Edytor i VJ tool <a href="https://lives-video.com" target="_blank">(Link)</a>.
- **Avidemux** – Edytor do szybkiej obróbki <a href="https://github.com/mean00/avidemux2" target="_blank">(Link)</a>.
- **Flowblade** – Edytor NLE dla Linuksa <a href="https://github.com/jliljebl/flowblade" target="_blank">(Link)</a>.
- **Cinelerra** – Profesjonalny montaż wideo <a href="https://cinelerra-gg.org" target="_blank">(Link)</a>.

##### Serwery plików self-hosted
- **TrueNAS** – Kompleksowy system NAS <a href="https://www.truenas.com" target="_blank">(Link)</a>.
- **ProFTPD** – Wydajny serwer FTP <a href="https://github.com/proftpd/proftpd" target="_blank">(Link)</a>.
- **MyDrive** – Prosty menedżer plików webowych <a href="https://github.com/Subarashii-kun/MyDrive" target="_blank">(Link)</a>.
- **Seafile** – Prywatna chmura z synchronizacją <a href="https://github.com/haiwen/seafile" target="_blank">(Link)</a>.
- **Nextcloud** – Kompletny pakiet współdzielenia plików <a href="https://github.com/nextcloud/server" target="_blank">(Link)</a>.
- **SeaweedFS** – Rozproszony system plików <a href="https://github.com/seaweedfs/seaweedfs" target="_blank">(Link)</a>.
- **GlusterFS** – Skalowalny system plików sieciowych <a href="https://github.com/gluster/glusterfs" target="_blank">(Link)</a>.
- **vsftpd / FTPd** – Bezpieczny serwer FTP <a href="https://security.appspot.com/vsftpd.html" target="_blank">(Link)</a>.
- **Pure-FTPd** – Lekki serwer FTP <a href="https://github.com/jedisct1/pure-ftpd" target="_blank">(Link)</a>.
- **Garage** – Obiektowy storage kompatybilny z S3 <a href="https://github.com/garagehq/garage" target="_blank">(Link)</a>.
- **sshfs** – Montowanie zasobów przez SSH <a href="https://github.com/libfuse/sshfs" target="_blank">(Link)</a>.
- **Zenko** – Warstwa zarządzania storage multi-cloud <a href="https://github.com/scality/zenko" target="_blank">(Link)</a>.
- **Pingvin Share** – Proste udostępnianie plików <a href="https://github.com/stonith404/pingvin-share" target="_blank">(Link)</a>.
- **Pydio Cells** – Bezpieczna chmura plików <a href="https://github.com/pydio/cells" target="_blank">(Link)</a>.
- **Sharry** – Wymiana plików z wygasaniem <a href="https://github.com/eikek/sharry" target="_blank">(Link)</a>.
- **Samba** – Udostępnianie SMB/CIFS <a href="https://www.samba.org" target="_blank">(Link)</a>.
- **Dufs** – Jednoplikiowy serwer plików HTTP <a href="https://github.com/sigoden/dufs" target="_blank">(Link)</a>.
- **SFTPgo** – Serwer SFTP/FTP/HTTP z GUI <a href="https://github.com/drakkan/sftpgo" target="_blank">(Link)</a>.
- **FileBrowser** – Menedżer plików w przeglądarce <a href="https://github.com/filebrowser/filebrowser" target="_blank">(Link)</a>.
- **Duplicati** – Backup w chmurze i lokalnie <a href="https://github.com/duplicati/duplicati" target="_blank">(Link)</a>.
- **Syncthing** – Synchronizacja P2P <a href="https://github.com/syncthing/syncthing" target="_blank">(Link)</a>.
- **Syncany** – Synchronizacja z szyfrowaniem <a href="https://github.com/syncany/syncany" target="_blank">(Link)</a>.
- **NFS** – Klasyczny protokół udostępniania plików <a href="https://kernel.org" target="_blank">(Link)</a>.
- **ProjectSend** – Portal do udostępniania plików klientom <a href="https://github.com/ignacionelson/ProjectSend" target="_blank">(Link)</a>.
- **CephFS** – Rozproszony system plików Ceph <a href="https://github.com/ceph/ceph" target="_blank">(Link)</a>.
- **OpenMediaVault** – System NAS dla serwerów domowych <a href="https://github.com/openmediavault/openmediavault" target="_blank">(Link)</a>.

##### Analiza malware i reverse engineering
- **Radare2** – Rama do analizy binariów <a href="https://github.com/radareorg/radare2" target="_blank">(Link)</a>.
- **Bytecode Viewer** – Analiza bytecode JVM <a href="https://github.com/Konloch/bytecode-viewer" target="_blank">(Link)</a>.
- **Hopper** – Komercyjny disassembler <a href="https://www.hopperapp.com" target="_blank">(Link)</a>.
- **Angr** – Silnik analizy symbolicznej <a href="https://github.com/angr/angr" target="_blank">(Link)</a>.
- **Ghidra** – Framework NSA do RE <a href="https://github.com/NationalSecurityAgency/ghidra" target="_blank">(Link)</a>.
- **Frida** – Instrumentacja dynamiczna <a href="https://github.com/frida/frida" target="_blank">(Link)</a>.
- **PyREBox** – Piaskownica do analizy malware <a href="https://github.com/Cisco-Talos/pyrebox" target="_blank">(Link)</a>.
- **JD-GUI** – Decompiler Java <a href="https://github.com/java-decompiler/jd-gui" target="_blank">(Link)</a>.
- **Volatility** – Analiza pamięci RAM <a href="https://github.com/volatilityfoundation/volatility" target="_blank">(Link)</a>.
- **YARA** – Reguły wykrywania malware <a href="https://github.com/VirusTotal/yara" target="_blank">(Link)</a>.
- **Wireshark** – Analiza ruchu sieciowego <a href="https://gitlab.com/wireshark/wireshark" target="_blank">(Link)</a>.
- **OllyDbg** – Debugger Windows <a href="http://www.ollydbg.de" target="_blank">(Link)</a>.
- **Apktool** – Inżynieria wsteczna aplikacji Android <a href="https://github.com/iBotPeaches/Apktool" target="_blank">(Link)</a>.
- **REMnux** – Dystrybucja do analizy malware <a href="https://remnux.org" target="_blank">(Link)</a>.
- **wxHexEditor** – Hex editor dla dużych plików <a href="https://github.com/EUA/wxHexEditor" target="_blank">(Link)</a>.
- **Capstone** – Silnik disassemblingu <a href="https://github.com/capstone-engine/capstone" target="_blank">(Link)</a>.

##### VPN self-hosted
- **OpenVPN** – Popularne rozwiązanie VPN <a href="https://github.com/OpenVPN/openvpn" target="_blank">(Link)</a>.
- **Pritunl** – Panel zarządzania OpenVPN/WireGuard <a href="https://github.com/pritunl/pritunl" target="_blank">(Link)</a>.
- **Tailscale** – VPN typu mesh na bazie WireGuard <a href="https://github.com/tailscale/tailscale" target="_blank">(Link)</a>.
- **PiVPN** – Skrypty do wdrożenia VPN na Raspberry Pi <a href="https://github.com/pivpn/pivpn" target="_blank">(Link)</a>.
- **Psiphon** – Sieć VPN i obfuskacja ruchu <a href="https://github.com/Psiphon-Labs/psiphon" target="_blank">(Link)</a>.
- **strongSwan** – IPsec VPN dla Linuksa <a href="https://github.com/strongswan/strongswan" target="_blank">(Link)</a>.
- **SoftEther** – Wieloprotokołowy serwer VPN <a href="https://github.com/SoftEtherVPN/SoftEtherVPN" target="_blank">(Link)</a>.
- **tinc** – VPN mesh z szyfrowaniem <a href="https://github.com/gsliepen/tinc" target="_blank">(Link)</a>.
- **ZeroTier** – Wirtualne sieci SD-WAN <a href="https://github.com/zerotier/ZeroTierOne" target="_blank">(Link)</a>.
- **Amnezia VPN** – Samohostowany klient/serwer VPN <a href="https://github.com/amnezia-vpn/amnezia-client" target="_blank">(Link)</a>.
- **OPNsense** – Firewall/VPN BSD <a href="https://opnsense.org" target="_blank">(Link)</a>.
- **Firezone** – VPN oparty na WireGuard z GUI <a href="https://github.com/firezone/firezone" target="_blank">(Link)</a>.
- **NetBird** – Alternatywa Tailscale <a href="https://github.com/netbirdio/netbird" target="_blank">(Link)</a>.
- **Libreswan** – Implementacja IPsec <a href="https://github.com/libreswan/libreswan" target="_blank">(Link)</a>.
- **WireGuard Easy** – Prosty interfejs do WireGuard <a href="https://github.com/wg-easy/wg-easy" target="_blank">(Link)</a>.
- **pfSense** – Firewall/VPN FreeBSD <a href="https://www.pfsense.org" target="_blank">(Link)</a>.

##### Menedżery plików
- **nnn** – Terminalowy menedżer plików <a href="https://github.com/jarun/nnn" target="_blank">(Link)</a>.
- **Nemo** – Menedżer środowiska Cinnamon <a href="https://github.com/linuxmint/nemo" target="_blank">(Link)</a>.
- **Joshuto** – Menedżer terminalowy z interfejsem TUI <a href="https://github.com/kamiyaa/joshuto" target="_blank">(Link)</a>.
- **Caja** – Menedżer MATE <a href="https://github.com/mate-desktop/caja" target="_blank">(Link)</a>.
- **Vifm** – Menedżer w stylu Vim <a href="https://github.com/vifm/vifm" target="_blank">(Link)</a>.
- **PCManFM** – Lekki menedżer LXDE/LXQt <a href="https://github.com/lxde/pcmanfm" target="_blank">(Link)</a>.
- **Thunar** – Menedżer środowiska Xfce <a href="https://gitlab.xfce.org/xfce/thunar" target="_blank">(Link)</a>.
- **Ranger** – Menedżer konsolowy z podglądem <a href="https://github.com/ranger/ranger" target="_blank">(Link)</a>.
- **Dolphin** – Rozbudowany menedżer KDE <a href="https://invent.kde.org/system/dolphin" target="_blank">(Link)</a>.
- **Midnight Commander** – Klasyczny menedżer tekstowy <a href="https://github.com/MidnightCommander/mc" target="_blank">(Link)</a>.
- **Double Commander** – Dwupanelowy menedżer multi-platformowy <a href="https://github.com/doublecmd/doublecmd" target="_blank">(Link)</a>.
- **Konqueror** – Przeglądarka i menedżer KDE <a href="https://invent.kde.org/network/konqueror" target="_blank">(Link)</a>.
- **Nautilus** – Menedżer GNOME <a href="https://gitlab.gnome.org/GNOME/nautilus" target="_blank">(Link)</a>.
- **Krusader** – Zaawansowany menedżer plików dla KDE <a href="https://invent.kde.org/utilities/krusader" target="_blank">(Link)</a>.
- **Sunflower** – Lekki menedżer z dwoma panelami <a href="https://github.com/MeanEYE/Sunflower" target="_blank">(Link)</a>.
- **Clifm** – Menedżer terminalowy typu "Command Line Interface File Manager" <a href="https://github.com/pascl/clifm" target="_blank">(Link)</a>.

##### Platformy IoT open-source
- **Home Assistant** – Automatyzacja domu <a href="https://github.com/home-assistant/core" target="_blank">(Link)</a>.
- **OpenHAB** – Platforma automatyki domowej <a href="https://github.com/openhab/openhab-core" target="_blank">(Link)</a>.
- **Mainflux** – Platforma IoT z microserwisami <a href="https://github.com/mainflux/mainflux" target="_blank">(Link)</a>.
- **DeviceHive** – Zestaw narzędzi i protokołów IoT <a href="https://github.com/devicehive/devicehive" target="_blank">(Link)</a>.
- **WaziGate** – Edge gateway IoT <a href="https://github.com/Waziup/wazigate-edge" target="_blank">(Link)</a>.
- **ChirpStack** – Stos sieci LoRaWAN <a href="https://github.com/chirpstack" target="_blank">(Link)</a>.
- **Domoticz** – Lekka platforma domowa <a href="https://github.com/domoticz/domoticz" target="_blank">(Link)</a>.
- **Eclipse Kura** – Middleware IoT w Javie <a href="https://github.com/eclipse/kura" target="_blank">(Link)</a>.
- **SensorBee** – Strumieniowe przetwarzanie danych IoT <a href="https://github.com/sensorbee/sensorbee" target="_blank">(Link)</a>.
- **Gladys Assistant** – Asystent domowy <a href="https://github.com/GladysAssistant/Gladys" target="_blank">(Link)</a>.
- **SiteWhere** – Platforma IoT na mikroserwisach <a href="https://github.com/sitewhere/sitewhere" target="_blank">(Link)</a>.
- **Zetta** – API-first middleware IoT <a href="https://github.com/zettajs/zetta" target="_blank">(Link)</a>.
- **IoTivity** – Standard komunikacji IoT <a href="https://github.com/iotivity/iotivity-lite" target="_blank">(Link)</a>.
- **MySensors** – Sieci czujników DIY <a href="https://github.com/mysensors/MySensors" target="_blank">(Link)</a>.
- **EdgeX Foundry** – Mikroserwisy IoT sterowane wydarzeniami <a href="https://github.com/edgexfoundry" target="_blank">(Link)</a>.
- **ThingsBoard** – Platforma IoT z dashboardami <a href="https://github.com/thingsboard/thingsboard" target="_blank">(Link)</a>.

##### Blokowanie reklam
**Przeglądarki z blokowaniem**
- **Brave** – Przeglądarka z wbudowanym Shield <a href="https://github.com/brave/brave-browser" target="_blank">(Link)</a>.
- **Vivaldi** – Przeglądarka z blokadą trackerów <a href="https://vivaldi.com" target="_blank">(Link)</a>.
- **Opera** – Wbudowany ad-blocker i VPN <a href="https://www.opera.com" target="_blank">(Link)</a>.
- **Epic Browser** – Prywatna przeglądarka <a href="https://epicbrowser.com" target="_blank">(Link)</a>.
- **DuckDuckGo Browser** – Mobilna przeglądarka z blokowaniem śledzenia <a href="https://duckduckgo.com/app" target="_blank">(Link)</a>.

**Rozszerzenia przeglądarkowe**
- **AdGuard** – Rozszerzenie blokujące reklamy i trackery <a href="https://github.com/AdguardTeam/AdguardBrowserExtension" target="_blank">(Link)</a>.
- **AdBlock** – Klasyczny blokad reklam <a href="https://getadblock.com" target="_blank">(Link)</a>.
- **uBlock Origin** – Lekki i skuteczny bloker <a href="https://github.com/gorhill/uBlock" target="_blank">(Link)</a>.
- **NoScript** – Blokowanie skryptów w przeglądarce <a href="https://github.com/hackademix/noscript" target="_blank">(Link)</a>.
- **Privacy Badger** – Blokowanie trackerów EFF <a href="https://github.com/EFForg/privacybadger" target="_blank">(Link)</a>.
- **Ghostery** – Ochrona prywatności i blokowanie śledzenia <a href="https://www.ghostery.com" target="_blank">(Link)</a>.
- **AdBlocker Ultimate** – Otwartoźródłowy bloker reklam <a href="https://github.com/adblockultimate/AdBlocker-Ultimate" target="_blank">(Link)</a>.

**Rozwiązania DNS**
- **StevenBlack Hosts** – Zbiorcze listy hostów <a href="https://github.com/StevenBlack/hosts" target="_blank">(Link)</a>.
- **DNS66** – Filtrowanie DNS na Androidzie <a href="https://github.com/julian-klode/dns66" target="_blank">(Link)</a>.
- **AdGuard DNS** – Prywatny DNS z blokowaniem reklam <a href="https://adguard-dns.io" target="_blank">(Link)</a>.
- **hBlock** – Skrypt generujący hostfile <a href="https://github.com/hectorm/hblock" target="_blank">(Link)</a>.
- **Pi-hole** – Sieciowy DNS sinkhole <a href="https://github.com/pi-hole/pi-hole" target="_blank">(Link)</a>.
- **Technitium DNS** – Serwer DNS z filtrowaniem <a href="https://github.com/TechnitiumSoftware/DnsServer" target="_blank">(Link)</a>.

**Zapory i firewalle**
- **OpenSnitch** – Firewall aplikacyjny <a href="https://github.com/evilsocket/opensnitch" target="_blank">(Link)</a>.
- **Lockdown** – Firewall i VPN prywatności <a href="https://lockdownprivacy.com" target="_blank">(Link)</a>.
- **pfBlockerNG** – Blokowanie DNS/IP w pfSense <a href="https://github.com/pfsense/FreeBSD-ports/tree/devel/net/pfblockerng" target="_blank">(Link)</a>.

**Serwery proxy**
- **Privoxy** – Filtrujący proxy HTTP <a href="https://www.privoxy.org" target="_blank">(Link)</a>.
- **Squid** – Popularny proxy z filtracją <a href="http://www.squid-cache.org" target="_blank">(Link)</a>.
- **Zen** – Reguły filtrujące dla proxy <a href="https://github.com/zenfilters/zen" target="_blank">(Link)</a>.

---

#### Edytory i Środowiska Programistyczne
- **Visual Studio Code (VSCode)** – Popularny edytor kodu <a href="https://code.visualstudio.com/" target="_blank">(Link)</a>.
- **VSCodium** – Wersja open-source Visual Studio Code pozbawiona telemetrii <a href="https://vscodium.com/" target="_blank">(Link)</a>.
- **GitHub** – Repozytorium kodu i współpracy <a href="https://github.com/" target="_blank">(Link)</a>.
- **Gedit** – Lekki edytor GNOME <a href="https://gitlab.gnome.org/GNOME/gedit" target="_blank">(Link)</a>.
- **Notepads** – Nowoczesny edytor UWP <a href="https://github.com/0x7c13/notepads" target="_blank">(Link)</a>.
- **Atom** – Rozszerzalny edytor od GitHub <a href="https://github.com/atom/atom" target="_blank">(Link)</a>.
- **JED** – Prosty edytor tekstowy dla terminala <a href="https://www.jedsoft.org" target="_blank">(Link)</a>.
- **Lapce** – Wydajny edytor w Rust <a href="https://github.com/lapce/lapce" target="_blank">(Link)</a>.
- **Mousepad** – Lekki edytor Xfce <a href="https://gitlab.xfce.org/apps/mousepad" target="_blank">(Link)</a>.
- **Pico** – Klasyczny edytor konsolowy <a href="https://www.nano-editor.org/dist/v2.1/nano.html#Pico" target="_blank">(Link)</a>.
- **Micro** – Terminalowy edytor z obsługą myszki <a href="https://github.com/zyedidia/micro" target="_blank">(Link)</a>.
- **Geany** – Lekki IDE z obsługą wielu języków <a href="https://github.com/geany/geany" target="_blank">(Link)</a>.
- **Notepadqq** – Alternatywa Notepad++ dla Linuksa <a href="https://github.com/notepadqq/notepadqq" target="_blank">(Link)</a>.
- **FeatherPad** – Edytor Qt z zakładkami <a href="https://github.com/tsujan/FeatherPad" target="_blank">(Link)</a>.
- **Kakoune** – Edytor modalny inspirowany Vim <a href="https://github.com/mawww/kakoune" target="_blank">(Link)</a>.
- **JOE** – Joe's Own Editor <a href="https://sourceforge.net/projects/joe-editor/" target="_blank">(Link)</a>.
- **Zee** – Terminalowy edytor w Rust <a href="https://github.com/zee-editor/zee" target="_blank">(Link)</a>.
- **Sublime Text** – Wydajny edytor z pluginami <a href="https://www.sublimetext.com" target="_blank">(Link)</a>.
- **SciTE** – Edytor bazujący na Scintilla <a href="https://github.com/scintillaorg/scite" target="_blank">(Link)</a>.
- **ash** – Minimalistyczny edytor tekstu <a href="https://github.com/ash-shell/ash" target="_blank">(Link)</a>.
- **Emacs** – Rozszerzalny edytor Lisp <a href="https://git.savannah.gnu.org/git/emacs.git" target="_blank">(Link)</a>.
- **Brackets** – Edytor webowy <a href="https://github.com/brackets-cont/brackets" target="_blank">(Link)</a>.
- **jEdit** – Edytor w Javie <a href="https://github.com/jedit/jedit" target="_blank">(Link)</a>.
- **Kate** – Rozbudowany edytor KDE <a href="https://invent.kde.org/utilities/kate" target="_blank">(Link)</a>.
- **Xed** – Edytor środowiska Cinnamon <a href="https://github.com/linuxmint/xed" target="_blank">(Link)</a>.
- **Neovim** – Nowoczesny fork Vima <a href="https://github.com/neovim/neovim" target="_blank">(Link)</a>.
- **Vim** – Klasyczny edytor modalny <a href="https://github.com/vim/vim" target="_blank">(Link)</a>.
- **Nano** – Przyjazny edytor terminalowy <a href="https://git.savannah.gnu.org/git/nano.git" target="_blank">(Link)</a>.
