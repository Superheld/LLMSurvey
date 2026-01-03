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

**8 Strategien = 2 Befragungs-Modi × 4 System Prompts**

**Befragungs-Modi:**
1. **One-Shot:** Alle 29 Fragen auf einmal → JSON Array-Output
2. **Question-by-Question:** Frage-für-Frage OHNE History (isoliert)

**Conversation-Modus wurde bewusst weggelassen:**
- Bei 92.5% Convergence zu "Adaptiv-Pragmatische" ist kaum Unterschied im Endergebnis zu erwarten
- Drift tritt auch ohne Message-History auf
- Nicht unterscheidbar ob Drift durch Conversation-Effekt oder normales Model-Verhalten entsteht
- Kann bei Bedarf später für spezifische Drift-Analysen ergänzt werden

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

  **Hinweis:** Groq-Anmeldung hat nicht funktioniert und wurde daher nicht in die Tests einbezogen.

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
- ✅ **Oneshot-Modus komplett** - alle 4 System Prompt Varianten getestet
- ✅ **QuestionByQuestion-Modus komplett** - alle 4 System Prompt Varianten getestet
- ✅ **8 Strategien vollständig implementiert** (2 Modi × 4 System Prompts)
- ✅ **Code-Refactoring** - Modularisierung in `survey/models.py` und `survey/request.py`
- ✅ **Notebooks-Struktur** - Separation: `notebooks/` für Experimente, `survey/` für Code
- ✅ **SQLite Row Factory** - Dictionary-like DB-Zugriff statt Tuples
- ✅ **Multi-Provider Support** mit provider-spezifischen Anpassungen (DeepSeek json_object)
- ✅ **Metriken-Tracking** (prompt_tokens, completion_tokens, duration_time, timestamp)
- ✅ **Scoring-Pipeline** funktional (10 Sinus-Milieus mit gewichteter Matrix)
- ✅ **Evaluation-Notebook** mit run-basierter Aggregation (AVG über multiple Runs)
- ✅ 10 Models getestet (Mistral, OpenAI, Anthropic, Gemini, DeepSeek - je 2)
- ✅ **System Prompt Optimierung** - 4 Varianten für Bias-Reduktion (none, test, llm_opinion, llm_explicit)
- ✅ **Message Order Fix** - System Prompts werden korrekt VOR User Messages gesendet
- ✅ **Question ID Fix** - question_id wird aus Loop übernommen statt aus LLM Response (verhindert "alle Antworten als Frage 1" Bug)
- ✅ **Exception Handling** - Robustere Fehlerbehandlung in survey/request.py

### In Arbeit
- ⏳ Sinus-Milieu Daten validieren (Namen + Prozentanteile)
- ⏳ Visualisierungen (Heatmaps, Radar Charts, Antwortmuster)
- ⏳ Streamlit Dashboard
- ⏳ Analyse welche spezifischen Fragen zu `<UNKNOWN>` Responses führen (betrifft primär Mistral bei questionbyquestion)

### Erkenntnisse aus allen 8 Strategien

**10 Models getestet:** Mistral Small/Large, OpenAI GPT-5.2 Nano/5.2, Claude Haikaku/Opus, Gemini Flash/Pro, DeepSeek Chat/Reasoner

**8 Strategien vollständig getestet:** 2 Modi (oneshot, questionbyquestion) × 4 System Prompts (none, test, llm_opinion, llm_explicit)

#### 1. Strategieabhängige Varianz (wichtigster Finding!)

**Varianz ist stark strategieabhängig:**
- **oneshot_test:** 9/10 Models → Adaptiv-Pragmatische (90% Konvergenz, fast alle high confidence)
- **oneshot_none:** 9/10 Models → Adaptiv-Pragmatische (hohe Stabilität)
- **questionbyquestion_llm_opinion:** 10/10 Models → Adaptiv-Pragmatische (100% Konvergenz, teils 0.940 Probability!)
- **ABER oneshot_llm_opinion:** Deutliche Varianz! DeepSeek → Nostalgisch-Bürgerliche/Traditionelle (einziger systematischer Ausreißer)
- **ABER questionbyquestion_llm_explicit:** Viele unclear results, mehr Unsicherheit

**Interpretation:** System Prompts beeinflussen Antwortverhalten massiv - aber nicht alle in Richtung Varianz

#### 2. Test-Framing Paradox

**Erwartung:** Test-Framing sollte LLMs ermutigen die volle Skala (1-4) zu nutzen
**Realität:** Test-Framing verstärkt Konvergenz!

- **oneshot_test:** Höchste Konvergenzrate (90%), fast alle high confidence
- **questionbyquestion_test:** Ebenfalls sehr stabil (80%+)
- **Hypothese:** "Es gibt keine falschen Antworten" → LLMs fühlen sich SICHERER moderate Antworten zu geben
- **Paradox:** Explizite Permission für Extreme führt zu MEHR Konformität, nicht weniger

#### 3. DeepSeek llm_opinion = Einziger echter Ausreißer

**DeepSeek bei llm_opinion:**
- **oneshot:** Wechsel zu Nostalgisch-Bürgerliche/Traditionelle (EINZIGER non-Adaptiv-Pragmatische Milieu-Wechsel!)
- **questionbyquestion:** Adaptiv-Pragmatische mit 0.940 Probability (höchste im ganzen Experiment)
- **Interpretation:** "Reflektiere deine Trainingsdaten" triggert bei DeepSeek systematisch andere Patterns

**Dies ist das einzige Beispiel wo ein Model konsistent ein anderes Milieu zeigt!**

#### 4. Oneshot vs QuestionByQuestion: Kohärenz vs. Isolation

**Oneshot (alle 29 Fragen auf einmal):**
- Stabilere Milieu-Zuordnungen
- Weniger "unclear" Fälle
- Höhere Confidence-Werte
- Models entwickeln konsistente "Persona" über alle Fragen

**QuestionByQuestion (isolierte Einzelfragen):**
- Mehr "unclear" results (v.a. bei llm_explicit, llm_opinion)
- Niedrigere durchschnittliche Confidence
- Mistral gibt vereinzelt `<UNKNOWN>` zurück (verweigert Antwort)
- Fehlender Kontext führt zu inkonsistenteren Antworten

**Hypothese:** Kontextuelle Kohärenz hilft LLMs konsistente Antwortmuster zu generieren

#### 5. Model-spezifische Patterns

**Mistral (Large/Small):**
- Extrem konsistent über fast alle Strategien
- Vereinzelt `<UNKNOWN>` Responses bei questionbyquestion (~3 Fragen)
- Höchste Probabilities (oft 0.90+)

**Claude (Haiku/Opus):**
- Opus sehr stabil, kaum unclear results
- Haiku mehr Varianz, aber immer noch hohe Konvergenz

**DeepSeek (Chat/Reasoner):**
- Chat: Extrem hohe Probabilities (0.86-0.94) bei test/none Strategien
- Beide: Systematisch anders bei llm_opinion (Traditionelle/Nostalgisch-Bürgerliche)

**GPT-5.2 (Nano/5.2):**
- Nano extrem konsistent (fast immer Adaptiv-Pragmatische)
- 5.2 mehr unclear results

**Gemini (Flash/Pro):**
- Sehr ähnlich zu Mistral: Hohe Konsistenz, wenig Varianz

#### 6. Technische Erkenntnisse

**DeepSeek json_object Handling:**
- DeepSeek nutzt `json_object` statt `json_schema` (API-Limitation)
- Orientiert sich primär am System Prompt Beispiel
- **Bug gefunden:** qbq System Prompts zeigten `{"answers": [...]}` Array → DeepSeek gab Array zurück obwohl SINGLE Mode
- **Fix:** System Prompts auf `{"question": 1, "answer": 3}` angepasst (ohne Array)
- **Learning:** Bei json_object ist System Prompt Format KRITISCH

**Question ID Bug:**
- **Problem:** LLMs gaben immer `"question": 1` zurück (kopierten Beispiel aus System Prompt)
- Führte zu: Alle 29 Responses mit question_id=1 in DB → falsches Scoring
- **Fix:** question_id aus Loop übernehmen, LLM-Response ignorieren
- **Learning:** LLMs kopieren Beispiele literal wenn kein anderer Kontext

**`<UNKNOWN>` Responses:**
- Mistral (primär bei questionbyquestion) verweigert vereinzelt Antwort
- Betrifft ~3 von 29 Fragen
- Models sagen explizit `<UNKNOWN>` statt zu spekulieren
- **TODO:** Systematische Analyse welche Fragen betroffen sind

#### 7. Convergence zu "Adaptiv-Pragmatische"

**Über alle Strategien hinweg:**
- ~70-90% aller Runs landen bei "Adaptiv-Pragmatische" (strategieabhängig)
- Definition Sinus: "Moderne Mitte, flexibel, pragmatisch, moderate Werte OHNE Extreme"
- **Hypothese bestätigt:** LLMs sind trainiert auf Konsens, Ausgewogenheit, Vermeidung von Extrempositionen
- Test-Framing verstärkt dies paradoxerweise

**Einzige systematische Ausnahme:** DeepSeek bei llm_opinion

### Known Issues

- **Sinus-Milieu Benennungen und Prozentanteile:** Aktuell fehlerhafte Werte in `survey/scoring.py` - Summe der population_share = 90% statt 100%. Muss gegen Original-Sinus-Daten validiert werden.

## Lizenz & Nutzung

Dieses Projekt ist ein persönliches Lernprojekt und steht unter der [WTFPL](http://www.wtfpl.net/) (Do What The Fuck You Want To Public License).

**Kurz gesagt:** Nimm den Code, mach was du willst und sei einfach keine Spaßbremse.

Wer den Code nutzt, sollte sich aber bewusst sein: Dies ist **kein Production-Code** und **keine wissenschaftliche Referenz**. Es ist ein Spielplatz zum Lernen und Experimentieren.

## Kontakt

Bei Fragen, Anregungen oder Interesse am Projekt: Feel free to reach out!

---

**Letzte Aktualisierung:** 2026-01-03
