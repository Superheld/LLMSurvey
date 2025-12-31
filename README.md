# LLM-Survey: Sinus-Milieu Befragung mit Large Language Models

## Projektziel

Dieses Projekt ist ein **Lernexperiment**, das untersucht wie sich das Antwortverhalten verschiedener Large Language Models (LLMs) verändert, wenn sie unterschiedlich geframed werden.

**Die zentrale Frage:** Zeigen LLMs "soziale Erwünschtheit" oder Behavior Shifts, wenn man ihnen explizit mitteilt, dass sie an einem Test teilnehmen?

- **"Wie ist es"** (ohne Meta-Kontext): Natürliches Antwortverhalten basierend auf Trainingsdaten

- **"Wie möchte es sein"** (Test-Framing): Verändert sich das Verhalten wenn das Model weiß "Das ist ein Test"?

Das Sinus-Milieu-Framework dient dabei als strukturiertes Messinstrument, um Shifts im Antwortverhalten sichtbar zu machen – nicht um echte Milieus zu identifizieren.

**Wichtig:** Dieses Projekt dient dem Lernen und Experimentieren. Die Ergebnisse sind nicht repräsentativ oder wissenschaftlich valide bezüglich echter Sinus-Milieus, können aber interessante Muster im Model-Verhalten aufzeigen. 

**Hinweis:** Das Projekt wurde mit Hilfe von Claude Code erstellt. In der Regel habe ich den Code geschrieben und Claude war mein "Forum". Beim Setup hat er weite Teile geschrieben. In der Regel ist es an den Kommentaren (englisch vs. deutsch) erkennbar ;-) **CLAUDE.md ist auf meine Ziele optimiert, am besten du initiierst das Projekt für dich neu!**

## Lernziele

Das Projekt verfolgt folgende technische Lernziele:

- **LiteLLM & Multi-Provider-Integration:** Praktischer Umgang mit verschiedenen LLM-APIs (OpenAI, Anthropic, Mistral, Groq, DeepSeek, etc.) über eine einheitliche Schnittstelle
- **Experimentelles Design:** Systematische Erfassung von Model-Behavior unter kontrollierten Bedingungen
- **Streamlit:** Aufbau interaktiver Dashboards zur Datenvisualisierung
- **Datenmanagement:** SQLite-Datenbankdesign und -verwaltung für experimentelle Daten
- **Systematisches Experimentieren:** Strukturierte Erfassung und Auswertung von Multi-Model-Experimenten

## Was dieses Projekt zeigen kann (und was nicht)

### Interessante Beobachtungen, die möglich sind:

- **Behavior Shifts durch Meta-Prompts:** Verschiebt sich die "Milieu-Zuordnung" eines Models, wenn man explizit sagt "Das ist ein Test"? Gibt es messbare Unterschiede zwischen "natürlichem" Verhalten (ohne Framing) und "performativem" Verhalten (Test-Framing)?

- **Model-spezifische Shifts:** Reagieren verschiedene Models unterschiedlich stark auf Meta-Prompts? Zeigen sich systematische Unterschiede zwischen Providern (z.B. OpenAI vs. Anthropic vs. Mistral)?

- **Framing-Sensitivität:** Wie stark ist der Einfluss des Framings verglichen mit dem Einfluss des Befragungs-Modus (One-Shot vs. Conversation vs. Question-by-Question)?

- **Konsistenz vs. Variabilität:** Ist der Shift reproduzierbar? Verhält sich ein Model konsistent über verschiedene Befragungs-Modi hinweg, oder ist das Verhalten instabil?

**Das könnte beweisen:** Dass LLMs unterschiedliches Verhalten zeigen abhängig vom Meta-Kontext – nicht dass sie echte soziale Milieus repräsentieren, sondern dass sie auf den Kontext "Test" vs. "kein Test" reagieren.

### Was dieses Projekt NICHT liefert:

1. **Keine echte Milieu-Validierung:** LLMs sind keine Menschen und haben keine echten soziokulturellen Verortungen. Die "Antworten" sind statistische Muster, keine authentischen Lebensrealitäten.

2. **Keine repräsentativen Daten:** Die Anzahl der befragten Modelle und Durchläufe ist für belastbare statistische Aussagen viel zu klein.

3. **Keine kontrollierte Studie:** Es gibt keine Kontrolle für systematische Verzerrungen, Training Bias oder Alignment-Artefakte.

4. **Kein validiertes Instrument:** Der Fragebogen ist eine vereinfachte, LLM generierte Adaption des Sinus-Milieu-Konzepts und kein wissenschaftlich validiertes Erhebungsinstrument. Die Originalfragen des Sinus Instituts sind nicht zugänglich.

**Kurz gesagt:** Dieses Projekt macht Spaß, ich lerne dabei eine Menge, und die Ergebnisse sind interessant zu beobachten – aber sie haben keine wissenschaftliche Aussagekraft über echte Sinus-Milieus. Sie zeigen höchstens Patterns im LLM-Antwortverhalten.

## Technischer Aufbau

### Fragebogen
- 29 validierte Items über 6 thematische Blöcke (Grundwerte, Arbeit, Konsum, Soziales, Kultur, Zukunft)
- 4-stufige Antwortskala (1 = stimme überhaupt nicht zu, 4 = stimme voll und ganz zu)
- Mapping auf 10 Sinus-Milieus über gewichtete Scoring-Matrix

### Experimentelles Design

**6 Strategien = 3 Befragungs-Modi × 2 Framings**

**Befragungs-Modi:**
1. **One-Shot:** Alle 29 Fragen auf einmal → JSON Array-Output
2. **Conversation:** Frage-für-Frage MIT Message-History
3. **Question-by-Question:** Frage-für-Frage OHNE History (isoliert)

**Framings:**
1. **None:** Kein Meta-Kontext, nur die Fragen → "Wie ist es"
2. **Test:** Explizit: "Du nimmst an einem Test teil" → "Wie möchte es sein"

**Kontrollierte Variablen:** Gleiche Fragen, gleiche Antwortskala, gleiche Reihenfolge
**Experimentelle Variablen:** Model, Framing, Befragungs-Modus

### Tech Stack
- **Python 3.13**
- **LiteLLM:** Multi-Provider LLM-Integration
- **SQLite:** Lokale Datenhaltung
- **Streamlit:** Dashboard und Visualisierung
- **Pydantic:** Datenvalidierung und Schemas
- **Pandas & Plotly:** Datenanalyse und Charts

### Datenbank-Schema
```
questions:   id, label, text, block
strategies:  id, name, system_path, message_path
models:      id, model_id, provider, name
runs:        id, model_id, strategy_id, prompt_tokens, completion_tokens, duration_time, timestamp
responses:   id, run_id, question_id, answer
```

**Beziehungen:**
- `runs.model_id` → `models.id`
- `runs.strategy_id` → `strategies.id`
- `responses.run_id` → `runs.id`
- `responses.question_id` → `questions.id`

## Setup & Installation

### Voraussetzungen
- Python 3.13+
- API Keys für gewünschte LLM-Provider (Mistral, OpenAI, Anthropic, Gemini, DeepSeek)

### Installation

1. **Repository klonen**
   ```bash
   git clone https://github.com/Superheld/LLMSurvey.git
   cd LLMSurvey
   ```

2. **Dependencies installieren**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment-Variablen setzen**

   Erstelle eine `.env` Datei im Projekt-Root mit deinen API Keys:
   ```bash
   MISTRAL_API_KEY=your_key_here
   OPENAI_API_KEY=your_key_here
   ANTHROPIC_API_KEY=your_key_here
   GEMINI_API_KEY=your_key_here
   DEEPSEEK_API_KEY=your_key_here
   ```

4. **Datenbank initialisieren**
   ```bash
   # Führe die Setup-Notebooks in setup/ der Reihe nach aus:
   # 1. sqlite_1-puretables.ipynb
   # 2. sqlite_2-questions.ipynb
   # 3. sqlite_3-models.ipynb
   # 4. sqlite_4-strategies.ipynb
   ```

### Verwendung

**Survey durchführen:**
```bash
# Öffne survey/oneshot.ipynb
# Wähle Models in der models_to_test Liste
# Führe alle Zellen aus
```

**Ergebnisse auswerten:**
```bash
# Öffne survey/evaluation.ipynb
# Führe alle Zellen aus für tabellarische Übersicht
```

## Status

**Aktuell:** MVP Core funktionsfähig ✅

### Implementiert
- ✅ Fragebogen validiert (29 Items über 6 thematische Blöcke)
- ✅ Datenbank-Schema mit 5 Tabellen (inkl. runs für Metriken-Tracking)
- ✅ Setup-Notebooks für Datenbankinitialisierung
- ✅ Response Format mit Pydantic für JSON Schema Enforcement
- ✅ **Oneshot-Modus komplett** - beide Strategien getestet (oneshot_none + oneshot_test)
- ✅ **Code-Refactoring** - Modularisierung in `survey/models.py` und `survey/response.py`
- ✅ **Notebooks-Struktur** - Separation: `notebooks/` für Experimente, `survey/` für Code
- ✅ **SQLite Row Factory** - Dictionary-like DB-Zugriff statt Tuples
- ✅ **Multi-Provider Support** mit provider-spezifischen Anpassungen (DeepSeek json_object)
- ✅ **Metriken-Tracking** (prompt_tokens, completion_tokens, duration_time, timestamp)
- ✅ **Scoring-Pipeline** funktional (10 Sinus-Milieus mit gewichteter Matrix)
- ✅ **Evaluation-Notebook** mit run-basierter Aggregation (AVG über multiple Runs)
- ✅ 10 Models getestet (Mistral, OpenAI, Anthropic, Gemini, DeepSeek - je 2)
- ✅ 6 Strategien definiert (3 Modi × 2 Framings)

### In Arbeit
- ⏳ Conversation-Modus implementieren
- ⏳ QuestionByQuestion-Modus implementieren
- ⏳ Sinus-Milieu Daten validieren (Namen + Prozentanteile)
- ⏳ Visualisierungen (Heatmaps, Radar Charts, Antwortmuster)
- ⏳ Streamlit Dashboard

### Erste Erkenntnisse (Oneshot-Strategien)

**10 Models getestet:** Mistral Small/Large, OpenAI GPT-5.2 Nano/5.2, Claude Haikaku/Opus, Gemini Flash/Pro, DeepSeek Chat/Reasoner

**Strategien getestet:** `oneshot_none` (ohne Test-Framing), `oneshot_test` (mit Test-Framing)

**Multiple Runs pro Model+Strategie**

**Stabilität:**
- Große Modelle (Large/Pro/Opus) ändern sich nur wenig zwischen Runs
- Kleine Modelle (Small/Flash/Nano/Haikaku) nähern sich den größeren Schwestern an

**Test-Framing Effekt:**
- Werte werden stabiler, **außer bei Claude** bei dem die Confidence sinkt.
- DeepSeek Reasoner möchte anders kategorisiert werden wenn es weiß dass es getestet wird
- Verhalten ändert sich zwischen `oneshot_none` und `oneshot_test`

**Secondary Milieu:**
- Starke Schwankungen über die Zeit

**Performance (Duration):**
- **Schnellste:** Gemini Flash (~2s), Claude Haikaku (~2s)
- **Mittelfeld:** Mistral Small (~4s), Mistral Large (~5s), Claude Opus (~6s), Gemini Pro (~8s)
- **Langsam:** DeepSeek Chat (~17s), GPT-5.2 Nano (~24s)
- **Sehr langsam:** DeepSeek Reasoner (~54s)

**Nächste Schritte:**
- Conversation- und QuestionByQuestion-Modi implementieren
- Visualisierungen erstellen

### Known Issues

- **Sinus-Milieu Benennungen und Prozentanteile:** Aktuell fehlerhafte Werte in `survey/scoring.py` - Summe der population_share = 90% statt 100%. Muss gegen Original-Sinus-Daten validiert werden.

## Lizenz & Nutzung

Dieses Projekt ist ein persönliches Lernprojekt und steht unter der [WTFPL](http://www.wtfpl.net/) (Do What The Fuck You Want To Public License).

**Kurz gesagt:** Nimm den Code, mach was du willst und sei einfach keine Spaßbremse.

Wer den Code nutzt, sollte sich aber bewusst sein: Dies ist **kein Production-Code** und **keine wissenschaftliche Referenz**. Es ist ein Spielplatz zum Lernen und Experimentieren.

## Kontakt

Bei Fragen, Anregungen oder Interesse am Projekt: Feel free to reach out!

---

**Letzte Aktualisierung:** 2025-12-31
