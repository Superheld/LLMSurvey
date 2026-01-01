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

**12 Strategien = 3 Befragungs-Modi × 4 System Prompts**

**Befragungs-Modi:**
1. **One-Shot:** Alle 29 Fragen auf einmal → JSON Array-Output
2. **Conversation:** Frage-für-Frage MIT Message-History
3. **Question-by-Question:** Frage-für-Frage OHNE History (isoliert)

**System Prompts (4 Varianten zum Testen verschiedener Framings):**
1. **none:** Leer - Baseline-Verhalten ohne System Prompt
2. **test:** Test-Framing mit expliziter Permission für Extreme (1-4 Skala)
3. **llm_opinion:** Training-Reflektion - "Antworte basierend auf deinem Training, nicht sozial erwünscht"
4. **llm_explicit:** Depersonalisiert, statistisch - "Basierend auf Mustern in Trainingsdaten"

**Ziel der System Prompt Varianten:** Reduktion des LLM People-Pleasing Bias und Erhöhung der Antwort-Varianz über die gesamte Skala (1-4).

**Kontrollierte Variablen:** Gleiche Fragen, gleiche Antwortskala, gleiche Reihenfolge
**Experimentelle Variablen:** Model, System Prompt, Befragungs-Modus

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
- ✅ **12 Strategien definiert** (3 Modi × 4 System Prompts)
- ✅ **System Prompt Optimierung** - 4 Varianten für Bias-Reduktion (none, test, llm_opinion, llm_explicit)
- ✅ **Message Order Fix** - System Prompts werden korrekt VOR User Messages gesendet
- ✅ **Exception Handling** - Robustere Fehlerbehandlung in survey/response.py

### In Arbeit
- ⏳ Conversation-Modus implementieren
- ⏳ QuestionByQuestion-Modus implementieren
- ⏳ Sinus-Milieu Daten validieren (Namen + Prozentanteile)
- ⏳ Visualisierungen (Heatmaps, Radar Charts, Antwortmuster)
- ⏳ Streamlit Dashboard

### Erste Erkenntnisse (Oneshot-Strategien)

**10 Models getestet:** Mistral Small/Large, OpenAI GPT-5.2 Nano/5.2, Claude Haikaku/Opus, Gemini Flash/Pro, DeepSeek Chat/Reasoner

**4 Strategien getestet:** `oneshot_none` (Baseline), `oneshot_test` (Test-Framing), `oneshot_llm_opinion` (Training-Reflektion), `oneshot_llm_explicit` (Statistisch-Depersonalisiert)

**LLM People-Pleasing Bias (wichtigster Finding):**
- **Initiale Beobachtung:** Fast nur Antworten 3-4, selten 2, nie 1
- **Interpretation:** LLMs vermeiden Widerspruch und Extreme → People-Pleasing
- **Nach Prompt-Optimierung:** Erste 1er und deutlich mehr 2er sichtbar
- **Erkenntnis:** Explizite Permission für Extreme (1-4 gleichwertig) erhöht Antwort-Varianz signifikant

**System Prompt Effekte auf Milieu-Zuordnung:**

1. **oneshot_test (stabilste Strategie):**
   - ALLE 10 Models → "Adaptiv-Pragmatische" Milieu
   - ALLE moderate/high confidence
   - Keine "unclear" Fälle
   - **Interpretation:** Test-Framing führt zu konvergenten, moderaten Antworten

2. **oneshot_none (Baseline - ebenfalls stabil):**
   - 8/10 Models → "Adaptiv-Pragmatische" (high confidence)
   - Nur 2 unclear (GPT-5.2, Gemini Flash)
   - Hohe Confidence-Werte (0.721-0.940)

3. **oneshot_llm_opinion (mehr Varianz):**
   - DeepSeek Chat wechselt zu **"Traditionelle/Nostalgisch-Bürgerliche"** (einziges non-Adaptiv-Pragmatische Ergebnis!)
   - 4 unclear Fälle (GPT-5.2, Gemini Flash/Pro)
   - **Interpretation:** "Training reflektieren" triggert unterschiedliche Interpretationen

4. **oneshot_llm_explicit (maximale Unsicherheit):**
   - 3 unclear Models (GPT-5.2, Mistral Large/Small)
   - **Besonderheit:** Mistral Large produzierte hier Begründungen zu jeder Antwort (musste gefiltert werden)
   - DeepSeek Reasoner zeigt dennoch hohe Überzeugung (0.721)
   - **Interpretation:** "Statistische Muster" ist am mehrdeutigsten

**Convergence towards "Adaptiv-Pragmatische":**
- 37 von 40 Runs (92.5%) landen bei "Adaptiv-Pragmatische" Milieu
- Definition laut Sinus: "Moderne Mitte, flexibel, pragmatisch, moderate Werte **OHNE Extreme**"
- **Hypothese:** LLMs tendieren zur Mitte weil sie trainiert sind auf Ausgewogenheit und Konsens

**Technischer Breakthrough:**
- **Schema in System Prompt** statt User Message verhindert "kreative" Interpretationen
- Mistral's Begründungen zeigen interessante Meta-Reflektion, aber verletzen JSON-Schema
- DeepSeek's json_object mode funktioniert zuverlässig mit Schema-Instruktion im System Prompt

**Performance (Duration):**
- **Schnellste:** Gemini Flash (~2s), Claude Haikaku (~2s)
- **Mittelfeld:** Mistral Small (~4s), Mistral Large (~5s), Claude Opus (~6s), Gemini Pro (~8s)
- **Langsam:** DeepSeek Chat (~17s), GPT-5.2 Nano (~24s)
- **Sehr langsam:** DeepSeek Reasoner (~54s)

**Nächste Schritte:**
- Conversation- und QuestionByQuestion-Modi implementieren (testen ob sequentielle Befragung andere Patterns zeigt)
- Visualisierungen für Antwortverteilung erstellen (Heatmaps: Models × Questions × Strategies)
- Reasoning-Mode evaluieren (Mistral's Begründungen systematisch erfassen?)

### Known Issues

- **Sinus-Milieu Benennungen und Prozentanteile:** Aktuell fehlerhafte Werte in `survey/scoring.py` - Summe der population_share = 90% statt 100%. Muss gegen Original-Sinus-Daten validiert werden.

## Lizenz & Nutzung

Dieses Projekt ist ein persönliches Lernprojekt und steht unter der [WTFPL](http://www.wtfpl.net/) (Do What The Fuck You Want To Public License).

**Kurz gesagt:** Nimm den Code, mach was du willst und sei einfach keine Spaßbremse.

Wer den Code nutzt, sollte sich aber bewusst sein: Dies ist **kein Production-Code** und **keine wissenschaftliche Referenz**. Es ist ein Spielplatz zum Lernen und Experimentieren.

## Kontakt

Bei Fragen, Anregungen oder Interesse am Projekt: Feel free to reach out!

---

**Letzte Aktualisierung:** 2026-01-01
