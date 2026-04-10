# 🎵 Agentic Heardle - Project Blueprint

## 🎯 Cel Projektu
Budowa agentycznej wersji gry **Heardle**. System wybiera utwór do zgadnięcia na podstawie opisu (mood, tempo, lata) oraz historii słuchania użytkownika z **Last.fm**, a następnie serwuje fragmenty audio.

## 🛠 Stack Techniczny
* **Orkiestracja:** `langgraph` 🕸️
* **LLM:** DeepSeek 🧠 (rozumowanie i selekcja)
* **Dane:** API Last.fm (`pylast`) 📊
* **Audio:** YouTube Search API 🔊
* **Język:** Python 3.13 🐍

## 🏗 Architektura Systemu

### 1. Struktura Projektu
| Katalog / Plik | Opis |
| :--- | :--- |
| `src/graph.py` | Definicja węzłów i krawędzi grafu LangGraph. |
| `src/state.py` | `AgentState` (TypedDict) – stan przechowujący dane gry. |
| `src/nodes.py` | Logika biznesowa poszczególnych kroków Agenta. |
| `src/tools.py` | Integracja z zewnętrznymi API (Last.fm, YT). |

### 2. Definicja Stanu (`AgentState`)
Będziemy śledzić następujące informacje:
* `description`: Prompt użytkownika (np. "melancholijny rock z lat 90").
* `user_id`: Identyfikator konta Last.fm.
* `candidate_tracks`: Lista utworów do wstępnej analizy (artist, title, playcount).
* `selected_track`: Finalny wybór Agenta z metadanymi.
* `game_status`: Metryki sesji (liczba prób, wynik).

### 3. Logika Przepływu (Graph Flow)
0. **'user_input'**: User definiuje rodzaj utworu którego szuka.
1. **`fetch_library`** 📥: Pobranie 50 najczęstszych utworów użytkownika z ostatniego okresu.
2. **`enrich_and_select`** 🔍: Agent typuje 3-5 utworów i dociąga dla nich tagi.
3. **`final_decision`** 🏆: Wybór jednego utworu najlepiej pasującego do opisu.
4. **`setup_audio`** 🎸: Pozyskanie linku do YouTube i przygotowanie fragmentów.

## 🗓 Plan MVP (4 Dni)
* **Dzień 1:** Setup środowiska, `pylast` i bazowy graf (pobieranie danych).
* **Dzień 2:** Agentyczna selekcja i wzbogacanie danych (LLM Reasoning).
* **Dzień 3:** Integracja z YouTube i logika odtwarzania fragmentów.
* **Dzień 4:** Obsługa błędów i prosty interfejs (CLI/Streamlit).