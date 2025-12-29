# Product Requirements Document (PRD)
# Sinus-Milieu LLM Survey System - MVP

**Version:** 1.0 MVP (Minimal Viable Product)
**Datum:** 2025-12-28
**Autor:** Bruce
**Status:** Planning

---

## 1. Executive Summary

### Vision
LLMs mit einem 29-Item-Fragebogen befragen, Antworten speichern und in einem Streamlit-Dashboard visualisieren.

### Kernziele (MVP)
1. **Lernen:** LiteLLM, Streamlit, grundlegendes Datenhandling
2. **Experimentieren:** Verschiedene LLMs + 3 Prompt-Strategien testen
3. **Visualisieren:** Ergebnisse in einfachem Dashboard ansehen

### Success Metrics (MVP)
- ✅ 5+ verschiedene LLM-Modelle befragen
- ✅ 3 Prompt-Strategien implementiert (Frage-für-Frage, Konversation, One-Shot)
- ✅ Alle Antworten in SQLite gespeichert
- ✅ Streamlit Dashboard zeigt Ergebnisse
- ✅ Basis-Scoring für alle 10 Milieus funktioniert

---

## 2. Technical Stack (Minimal!)

### Absolutes Minimum
```txt
# LLM Integration
litellm                     # Multi-provider LLM API (das wichtigste!)

# UI
streamlit                   # Dashboard (einfacher als du denkst!)

# Data
pandas                      # CSV-Handling, Datenanalyse
# sqlite3 ist built-in Python, keine Installation nötig

# Visualization (kommt mit Streamlit)
plotly                      # Für schöne Charts in Streamlit

# Utils
python-dotenv               # API Keys sicher speichern
```

**Das ist alles!** Keine 20 Dependencies, nur 5.

### Später hinzufügen (wenn du willst)
```txt
# Phase 2 (nach MVP):
numpy                       # Für Scoring-Berechnungen
pyyaml                      # Wenn Config komplexer wird

# Phase 3 (Validierung):
scipy                       # Statistische Tests
pingouin                    # Cronbach's Alpha, ICC

# Niemals (für dieses Projekt):
mlflow                      # Zu komplex für Anfang
langchain                   # Separates Lernprojekt
```

---

## 3. Projektstruktur (Super Einfach!)

```
llm-survey/
├── .env                       # API Keys (geheim!)
├── requirements.txt           # Die 5 Dependencies
├── README.md
│
├── data/
│   └── survey.db             # SQLite - eine einzige Datei!
│
├── questions.txt             # Die 29 Fragen (plain text)
│
├── survey_runner.py          # HAUPTFILE: Surveys ausführen
├── scoring.py                # Dein bestehender Code aus scoring.md
│
└── streamlit_app.py          # Dashboard (kommt später)
```

**Das wars!** Nur 3 Python-Dateien zum Start.

### Später erweitern (optional):
```
llm-survey/
├── ... (wie oben)
│
└── data/
    └── exports/              # CSV Exports
```

**Keine** komplexen Ordner-Hierarchien, **keine** 20 Module.
Erst wenn es zu unübersichtlich wird, aufteilen.

### Datenfluss (Simpel!)

```
1. Du startest: python survey_runner.py

2. survey_runner.py:
   ├─> Liest questions.txt
   ├─> Schickt Fragen an LLM (via LiteLLM)
   ├─> Parst Antworten (1-4)
   └─> Speichert in survey.db

3. scoring.py:
   ├─> Liest Antworten aus survey.db
   ├─> Berechnet Milieu-Scores
   └─> Speichert Scores zurück in survey.db

4. streamlit_app.py:
   ├─> Liest Daten aus survey.db
   └─> Zeigt Charts & Tabellen
```

**So einfach!** Keine komplexen Pipelines.

---

## 4. Database Schema (Mini-Version!)

**Nur 2 Tabellen!** Mehr brauchst du nicht für den Anfang.

```sql
-- ============================================================================
-- TABLE 1: runs
-- Ein Survey-Run = 1 LLM befragt
-- ============================================================================
CREATE TABLE runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- Welches Modell?
    model_name TEXT NOT NULL,           -- "gpt-4o", "claude-sonnet-4", etc.

    -- Welche Strategie?
    prompt_strategy TEXT NOT NULL,      -- "one_shot", "conversation", "step_by_step"

    -- Parameter
    temperature REAL DEFAULT 0.7,

    -- Wann?
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Wie lange?
    duration_seconds REAL,

    -- Notizen
    notes TEXT
);

-- ============================================================================
-- TABLE 2: responses
-- Die 29 Antworten pro Run (1-4)
-- ============================================================================
CREATE TABLE responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id INTEGER NOT NULL,

    item_number INTEGER NOT NULL,       -- 1 bis 29
    response INTEGER NOT NULL,          -- 1, 2, 3 oder 4

    FOREIGN KEY (run_id) REFERENCES runs(id),
    UNIQUE(run_id, item_number)
);
```

**Das wars!** Scores berechnest du on-the-fly beim Anzeigen.
Wenn es später zu langsam wird, kannst du eine `scores`-Tabelle hinzufügen.

---

## 5. Features (MVP)

### Was das Programm können muss:

**1. LLMs befragen (3 Strategien)**
- ✅ **One-Shot:** Alle 29 Fragen auf einmal → 1 LLM-Call
- ✅ **Konversation:** 29 Fragen nacheinander im Chat → 29 Calls
- ✅ **Step-by-Step:** Jede Frage einzeln, neuer Chat → 29 Calls

**2. Antworten speichern**
- ✅ SQLite Datenbank (runs + responses)
- ✅ Welches Modell, welche Strategie, wann

**3. Scores berechnen**
- ✅ Dein bestehender Code aus `scoring.md`
- ✅ Alle 10 Milieus
- ✅ Primary Milieu mit Confidence

**4. Visualisieren (Streamlit)**
- ✅ Tabelle: Alle Runs anzeigen
- ✅ Radar Chart: Milieu-Profil eines Runs
- ✅ Vergleich: 2 Modelle nebeneinander

**Das wars!** Keine fancy Features, einfach funktional.

---

## 6. Implementation Plan (3 Steps!)

### Step 1: Setup & Erste Befragung (2-3 Stunden)

**Ziel:** Ein LLM befragen funktioniert

- [ ] Projektstruktur anlegen (Ordner + Dateien)
- [ ] `requirements.txt` erstellen & installieren
- [ ] `.env` mit API Keys erstellen
- [ ] `questions.txt` mit den 29 Fragen erstellen
- [ ] `survey.db` erstellen (2 Tabellen)
- [ ] `survey_runner.py`: One-Shot Strategy implementieren
- [ ] Test: GPT-4o befragen

**Fertig wenn:** Du 29 Antworten in der DB hast!

---

### Step 2: Scoring & Mehr Modelle (2-3 Stunden)

**Ziel:** Verschiedene LLMs testen & Scores berechnen

- [ ] `scoring.py` aus `scoring.md` portieren
- [ ] Funktion: Scores aus DB-Responses berechnen
- [ ] `survey_runner.py`: Conversation Strategy hinzufügen
- [ ] `survey_runner.py`: Step-by-Step Strategy hinzufügen
- [ ] Test: Claude, Mistral, Gemini befragen

**Fertig wenn:** Du 5+ Runs mit Scores hast!

---

### Step 3: Streamlit Dashboard (2-3 Stunden)

**Ziel:** Ergebnisse visualisieren

- [ ] `streamlit_app.py` erstellen
- [ ] Tabelle: Alle Runs anzeigen
- [ ] Radar Chart: Milieu-Profil zeigen
- [ ] Filter: Nach Modell/Strategie filtern
- [ ] Vergleich: 2 Runs nebeneinander

**Fertig wenn:** `streamlit run streamlit_app.py` läuft!

---

**Gesamt:** ~6-9 Stunden für MVP
**Nach jedem Step hast du was Funktionierendes!**

---

## 7. Configuration (Simpel!)

### `.env` (API Keys)

```bash
# ============================================================================
# API KEYS (kopiere zu .env und füge deine Keys ein)
# ============================================================================

# OpenAI
OPENAI_API_KEY=sk-...

# Anthropic
ANTHROPIC_API_KEY=sk-ant-...

# Google (Gemini)
GOOGLE_API_KEY=...

# Mistral
MISTRAL_API_KEY=...

# Groq
GROQ_API_KEY=gsk_...

# DeepSeek
DEEPSEEK_API_KEY=...

# Cohere
COHERE_API_KEY=...

```

### `questions.txt` (Die 29 Fragen)

Einfach die 29 Items aus `fragen_v1.1.md` rauskopierten, eine pro Zeile.

```txt
Bewährte Traditionen und Werte geben meinem Leben wichtige Orientierung.
Ich bevorzuge erprobte Lösungen gegenüber neuen, ungetesteten Ansätzen.
Persönlicher Erfolg und berufliche Leistung sind zentrale Bausteine meiner Identität.
...
(alle 29 Fragen)
```

---

## 8. Was du lernen wirst

**Step 1: LiteLLM**
- Multi-Provider LLM Integration
- Eine API für viele LLMs
- Error Handling

**Step 2: SQLite**
- Datenbank-Design (2 Tabellen reichen!)
- SQL Basics (CREATE, INSERT, SELECT)
- Daten persistent speichern

**Step 3: Streamlit**
- Web-UI ohne HTML/CSS/JavaScript
- Interaktive Dashboards
- Plotly Charts einbetten

**Step 4: Prompt Engineering**
- 3 verschiedene Strategien testen
- Was funktioniert besser?
- Strukturierte Outputs parsen

**Step 5: Datenanalyse**
- pandas für Survey-Daten
- Scores berechnen
- Vergleiche ziehen

---

## 9. Next Steps (JETZT!)

1. **Review dieses PRD** - Macht das Sinn für dich?
2. **Fragen klären** - Noch unklar was?
3. **Los geht's:** Ich kann dir helfen mit:
   - Projektstruktur anlegen
   - `requirements.txt` erstellen
   - Erste Version von `survey_runner.py` schreiben

**Bist du ready?** Was möchtest du zuerst machen?

---

**Letztes Update:** 2025-12-28 - MVP Version
