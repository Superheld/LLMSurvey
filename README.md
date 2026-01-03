# LLM-Survey: Strukturierte Daten von LLMs generieren und verarbeiten

## Projektziel

Technisches Lernprojekt zur Arbeit mit strukturierten LLM-Outputs. Large Language Models dienen als Daten-Generator für ein experimentelles Setup mit 29-Fragen-Survey.

**Technischer Fokus:**
- LiteLLM Multi-Provider-Integration
- Pydantic JSON Schema Enforcement für strukturierte Outputs
- SQLite Datenmanagement für experimentelle Daten
- Systematisches Experimentieren mit verschiedenen Prompt-Strategien
- Datenauswertung mit Pandas/Plotly (geplant: Streamlit Dashboard)

**Nicht-Ziel:** LLM-Bias-Analyse oder wissenschaftlich valide Aussagen über Sinus-Milieus. Die Models liefern lediglich Daten zum Üben von Datenverarbeitung und Visualisierung.

## Tech Stack

- **Python 3.13**
- **LiteLLM** - Einheitliche API für verschiedene LLM-Provider
- **Pydantic** - Datenvalidierung und JSON Schema Generation
- **SQLite** - Lokale Datenhaltung
- **Pandas & Plotly** - Datenanalyse und Visualisierung
- **Jupyter Notebooks** - Experimente und Evaluation

## Experimentelles Setup

**8 Strategien = 2 Modi × 4 System Prompts**

**Befragungs-Modi:**
- Oneshot: Alle 29 Fragen auf einmal → JSON Array
- QuestionByQuestion: Frage für Frage isoliert → einzelne JSON Objects

**System Prompt Varianten:**
- `none` - Kein System Prompt (Baseline)
- `test` - Test-Framing
- `llm_opinion` - Training-Reflektion
- `llm_explicit` - Depersonalisiert/statistisch

**Datenquellen:** 10 LLM Models (Mistral, OpenAI, Anthropic, Gemini, DeepSeek)

**Fragebogen:** 29 Items auf 4-Punkt-Skala, Mapping auf 10 Sinus-Milieus via Scoring-Matrix

## Datenbank-Schema

```
questions:   id, label, text, block
strategies:  id, name, system_path, message_path
models:      id, model_id, provider, name
runs:        id, model_id, strategy_id, prompt_tokens, completion_tokens, duration_time, timestamp
responses:   id, run_id, question_id, answer
```

## Setup & Installation

**Voraussetzungen:**
- Python 3.13+
- API Keys für: Mistral, OpenAI, Anthropic, Gemini, DeepSeek

**Installation:**
```bash
git clone https://github.com/Superheld/LLMSurvey.git
cd LLMSurvey
pip install -r requirements.txt

# .env erstellen mit API Keys
MISTRAL_API_KEY=your_key
OPENAI_API_KEY=your_key
ANTHROPIC_API_KEY=your_key
GEMINI_API_KEY=your_key
DEEPSEEK_API_KEY=your_key
```

**Datenbank initialisieren:**
```bash
# Setup-Notebooks in Reihenfolge ausführen:
# 1. setup/sqlite_1-puretables.ipynb
# 2. setup/sqlite_2-questions.ipynb
# 3. setup/sqlite_3-models.ipynb
# 4. setup/sqlite_4-strategies.ipynb
```

**Survey durchführen:**
```bash
# notebooks/survey_oneshot.ipynb
# notebooks/survey_questionbyquestion.ipynb
```

**Evaluation:**
```bash
# notebooks/evaluation.ipynb
```

## Implementiert

**Core Features:**
- ✅ 8 Strategien vollständig implementiert (2 Modi × 4 System Prompts)
- ✅ Multi-Provider Support (Mistral, OpenAI, Anthropic, Gemini, DeepSeek)
- ✅ Pydantic Schema Enforcement für JSON Outputs
- ✅ SQLite Datenhaltung mit Run-Tracking (Tokens, Duration, Timestamp)
- ✅ Evaluation Notebook mit Aggregation über multiple Runs
- ✅ Provider-spezifische Anpassungen (DeepSeek json_object vs. json_schema)

**Technische Fixes:**
- ✅ Question ID aus Loop statt LLM Response (verhindert alle Antworten = Frage 1)
- ✅ System Prompts VOR User Messages
- ✅ Separate Prompts für oneshot vs. questionbyquestion Modi
- ✅ Exception Handling für Schema-Violations

## Beobachtungen

**Datenqualität:**
- ~100% Konvergenz aller Models zu einem Milieu ("Adaptiv-Pragmatische") nach 3-4 Runs
- Wenig Varianz zwischen Models → limitierte Basis für differenzierte Visualisierungen
- Test-Framing führt zu höherer Konformität (nicht zu mehr Varianz wie erwartet)

**Technische Herausforderungen:**
- DeepSeek nutzt `json_object` statt `json_schema` → System Prompt Format kritisch
- Manche Models produzieren Schema-Violations (DeepSeek Reasoner, Claude Haiku)
- Averaging über Runs glättet Varianz weg

**Limitation für Auswertung:**
- Sinus-Milieu Framework zu "soft" (konsensorientiert) → Models vermeiden Extreme
- Für interessantere Datenvielfalt: Kontroversere Fragen oder andere Frameworks nötig

## Lizenz

[WTFPL](http://www.wtfpl.net/) - Do What The Fuck You Want To Public License

Dies ist ein Lernprojekt, kein Production-Code.

---

**Letzte Aktualisierung:** 2026-01-03
