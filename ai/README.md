# 🤖 AI & Kreatywność Hub
Kompendium narzędzi, modeli i raportów o sztucznej inteligencji. Hub obejmuje zarówno praktyczne zastosowania (chatboty, IDE z AI, generatory obrazów), jak i eksperymentalne projekty badawcze.

## 🧭 Spis treści
- [Raport: Ocena najpopularniejszych systemów AI — listopad 2025](#raport-ocena-najpopularniejszych-systemów-ai--listopad-2025)
  - [Top 10 ogólnie](#top-10-ogólnie)
  - [Najważniejsze wnioski 2025](#najważniejsze-wnioski-2025)
- [Katalog narzędzi i modeli](#katalog-narzędzi-i-modeli)
  - [Chatboty i asystenci AI](#chatboty-i-asystenci-ai)
  - [Narzędzia programistyczne AI](#narzędzia-programistyczne-ai)
  - [Narzędzia do prototypowania](#narzędzia-do-prototypowania)
  - [Generowanie obrazów AI](#generowanie-obrazów-ai)
  - [Modele open source](#modele-open-source)
  - [Modele specjalistyczne](#modele-specjalistyczne)
  - [Eksperymentalne interfejsy i wyszukiwarki](#eksperymentalne-interfejsy-i-wyszukiwarki)

---

## Raport: Ocena najpopularniejszych systemów AI — listopad 2025
Pełne zestawienie metodologii, ocen i komentarzy znajduje się w raporcie [OCENA_NAJPOPULARNIEJSZYCH_SYSTEMÓW_AI_LISTOPAD_2025.md](./OCENA_NAJPOPULARNIEJSZYCH_SYSTEMÓW_AI_LISTOPAD_2025.md).

### Top 10 ogólnie
1. **ChatGPT (OpenAI)** — 9.25/10. Lider uniwersalnych zastosowań z niskim wskaźnikiem halucynacji GPT-4o (1.5%).
2. **Midjourney** — 9.125/10. Złoty standard generowania obrazów i preferencji estetycznych.
3. **Gemini (Google)** — 8.875/10. Model o najniższej liczbie halucynacji (0.7% dla Gemini-2.0-Flash).
4. **DALL·E 3 (OpenAI)** — 8.875/10. Największa dokładność interpretacji promptów (94%).
5. **OpenAI Codex (GPT-5-Codex)** — 8.875/10. Specjalista od kodu, 77.2% na SWE-bench Verified.
6. **GitHub Copilot** — 8.5/10. Najpopularniejszy asystent programistyczny (+56% szans na przejście testów).
7. **Cursor** — 8.5/10. Najszybciej rosnące IDE z AI, Composer do edycji wielu plików naraz.
8. **Canva AI** — 8.5/10. Drugi najpopularniejszy serwis designerski (996M wizyt miesięcznie).
9. **DeepSeek R1** — 8.375/10. Świetny reasoning (97% w MATH-500) bez kosztu modeli OpenAI.
10. **Bolt.new (StackBlitz)** — 8.375/10. Fenomenalny wzrost (0 → $40M ARR w 6 miesięcy).

### Najważniejsze wnioski 2025
- **Halucynacje**: Gemini 2.0 Flash prowadzi z 0.7%, podczas gdy modele reasoning OpenAI (o3/o4) osiągają nawet 33% w PersonQA.
- **Trendy technologiczne**: Konteksty rozmów rosną do 1–10M tokenów, a multimodalność (tekst+audio+wideo) staje się standardem.
- **Open source**: Modele takie jak LLaMA 4 i Mixtral zbliżają się jakością do rozwiązań proprietary, oferując długie okna kontekstu.
- **Narzędzia dla devów**: Bolt.new i Lovable notują rekordowy wzrost (od 0 do odpowiednio $40M i $17M ARR).
- **Niespodzianki**: Większe modele (Claude Opus 4.1, o3/o4) potrafią mieć więcej błędów niż mniejsze odpowiedniki (Sonnet 4, GPT-4o).

---

## Katalog narzędzi i modeli
Poniższe tabele łączą ocenę średnią (uśrednienie czterech kryteriów: użyteczność, błędy/halucynacje, popularność, poprawność) oraz najważniejsze wyróżniki.

### Chatboty i asystenci AI
| System | Średnia | Mocne strony | Błędy/Halucynacje |
| --- | --- | --- | --- |
| **ChatGPT (OpenAI)** | 9.25/10 | GPT-4o i GPT-5-mini obejmują szeroki zakres zastosowań, modele reasoning (o3/o4) dostępne dla zadań specjalnych. | GPT-4o: 1.5% halucynacji; GPT-5-mini: 4.9%; o3/o4: nawet 33% (PersonQA). |
| **Gemini (Google)** | 8.875/10 | Gemini-2.0-Flash-001 i Gemini 2.5 Pro z 1M tokenów kontekstu, wysoka integracja z ekosystemem Google Workspace. | 0.7% halucynacji — najlepszy wynik w 2025 r. |
| **Claude (Anthropic)** | 8.125/10 | Konserwatywne odpowiedzi, preferuje odmowę zamiast błędów; okno 200K–1M tokenów. | Sonnet 4: 4.4%; Opus 4.1: 10.1%; wysoki wskaźnik odmów (nawet 70%). |
| **DeepSeek** | 8.25/10 | 671B parametrów, świetny stosunek ceny do jakości, zbliżona wydajność do OpenAI o1. | DeepSeek-R1: 97% dokładności na MATH-500. |
| **Perplexity** | 7.875/10 | Łączy wyszukiwanie internetowe w czasie rzeczywistym z kilkoma LLM, idealny do badań. | Stabilne 8/10 pod względem błędów dzięki weryfikacji źródeł. |
| **Grok (xAI)** | 7.25/10 | Integracja z X (Twitter), dostęp do real-time danych platformy. | 7/10 — wciąż nadrabia dokładność względem liderów. |

### Narzędzia programistyczne AI
| System | Średnia | Wyróżniki | Dane jakości |
| --- | --- | --- | --- |
| **GitHub Copilot** | 8.5/10 | +56% szans na przejście testów, +13.6% linii bez błędów; nowy model embeddings poprawia wyszukiwanie. | Kontrowersje wokół wpływu na utrzymywalność kodu. |
| **OpenAI Codex (GPT-5-Codex)** | 8.875/10 | Autonomiczna praca przez 7+ godzin, 77.2% na SWE-bench Verified; dostępny w Copilocie od 13 XI 2025. | 9/10 błędy — 51.3% skuteczności w refaktoryzacji vs 33.9% GPT-5. |
| **Cursor** | 8.5/10 | IDE bazujące na VS Code z Composerem do wielu plików; $20/mies. Pro. | 8/10 błędy — stabilny partner pair-programmingu. |
| **Windsurf (Codeium)** | 8/10 | Agent Cascade z pamięcią sesji; $15/mies. start. | 8/10 błędy. |
| **Replit** | 7.75/10 | IDE w chmurze, Replit Agent generuje pełne aplikacje; świetne do nauki. | 7.5/10 błędy — mniejsza dojrzałość niż Cursor/Windsurf. |

### Narzędzia do prototypowania
| System | Średnia | Wyróżniki | Popularność |
| --- | --- | --- | --- |
| **Bolt.new (StackBlitz)** | 8.375/10 | WebContainer w przeglądarce, błyskawiczne prototypowanie front-endów. | $40M ARR w 6 miesięcy. |
| **Lovable** | 7.875/10 | Budowa aplikacji webowych na wzór Bolt.new, plan Pro $25/mies. | $17M ARR w 3 miesiące; 5 wiadomości/dzień w planie darmowym. |
| **v0 (Vercel)** | 8.25/10 | Konwersja Figma → kod React/Next.js, skupienie na komponentach UI. | Popularność 8/10 dzięki ekosystemowi Vercel. |

### Generowanie obrazów AI
| System | Średnia | Wyróżniki | Uwagi |
| --- | --- | --- | --- |
| **Midjourney** | 9.125/10 | Wersja V7 (04.2025) zapewnia najwyższą jakość artystyczną, 72% preferencji w testach. | Słabość: tekst w obrazach, interfejs przez Discorda. |
| **DALL·E 3 (OpenAI)** | 8.875/10 | 94% dokładności w interpretacji promptów, doskonała integracja z ChatGPT. | Preferowane do komercyjnych wizualizacji wymagających precyzji. |
| **Stable Diffusion** | 8/10 | Open source, najlepsza kontrola i customizacja, idealne do spójności postaci. | Wymaga wiedzy technicznej, jakość zależna od wybranego modelu. |
| **Canva AI** | 8.5/10 | Najłatwiejsze wejście w generowanie obrazów dla nie-designerów, szeroka biblioteka szablonów. | 996M wizyt miesięcznie — #2 w kategorii projektowania. |

### Modele open source
| System | Średnia | Wyróżniki | Halucynacje |
| --- | --- | --- | --- |
| **LLaMA 4 (Meta)** | 8.125/10 | Scout oferuje 10M tokenów kontekstu (~7 500 stron); Maverick i Scout dominują w zastosowaniach on-premise. | 4.6–4.7% |
| **Mixtral (Mistral AI)** | 7.75/10 | Architektura mixture-of-experts; Medium 3 oferuje frontier performance za $0.40/M tokenów. | 8/10 błędy. |
| **Qwen (Alibaba)** | 7.125/10 | Qwen 3 4B obsługuje 100+ języków, mocny w ekosystemie chińskim. | 7/10 błędy. |
| **GPT-OSS-120B (OpenAI)** | 7/10 | Pierwszy open-weight OpenAI od czasów GPT-2; 117B parametrów, 5.1B aktywnych. | 7.5/10 błędy. |

### Modele specjalistyczne
| System | Średnia | Wyróżniki | Błędy |
| --- | --- | --- | --- |
| **o3 / o4 (OpenAI)** | 7/10 | Modele reasoning z lepszym kodowaniem i matematyką, potrafią planować autonomiczne kroki. | 33% halucynacji w PersonQA — wymagają ręcznej weryfikacji. |
| **DeepSeek R1** | 8.375/10 | 97% dokładności w MATH-500, dorównuje o1 przy niższym koszcie. | 9/10 błędy — dużo bardziej stabilny niż o3/o4. |

### Eksperymentalne interfejsy i wyszukiwarki
- **GitHub Spark** — eksperymentalny interfejs do współpracy z repozytoriami w formie czatu, prezentowany w ramach [GitHub Next](https://githubnext.com/projects/github-spark).
- **DeepSeek.com** — wyszukiwarka wykorzystująca AI do grupowania wyników wątpliwych, łączy wątki tematyczne.
- **Perplexity** — opisany wyżej jako chatbot; kluczowy element to wyszukiwarka ze śledzeniem źródeł w czasie rzeczywistym.

---
