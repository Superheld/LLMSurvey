# LLM-Survey: Sinus-Milieu Befragung mit Large Language Models

## Projektziel

Dieses Projekt ist ein **Lernexperiment**, das untersucht wie sich das Antwortverhalten verschiedener Large Language Models (LLMs) verändert, wenn sie unterschiedlich geframed werden.

**Die zentrale Frage:** Zeigen LLMs "soziale Erwünschtheit" oder Behavior Shifts, wenn man ihnen explizit mitteilt, dass sie an einem Test teilnehmen?

- **"Wie ist es"** (ohne Meta-Kontext): Natürliches Antwortverhalten basierend auf Trainingsdaten

- **"Wie möchte es sein"** (Test-Framing): Verändert sich das Verhalten wenn das Model weiß "Das ist ein Test"?

Das Sinus-Milieu-Framework dient dabei als strukturiertes Messinstrument, um Shifts im Antwortverhalten sichtbar zu machen – nicht um echte Milieus zu identifizieren.

**Wichtig:** Dieses Projekt dient dem Lernen und Experimentieren. Die Ergebnisse sind nicht repräsentativ oder wissenschaftlich valide bezüglich echter Sinus-Milieus, können aber interessante Muster im Model-Verhalten aufzeigen. 

**Hinweis:** Das Projekt wurde mit Hilfe von Claude Code erstellt. In der Regel habe ich den Code geschrieben und Claude war mein "Forum". Beim Setup hat er weite Teile geschrieben. In der Regel ist es an den Kommentaren (englisch vs. deutsch) erkennbar ;-)

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
- `questions`: 29 Survey-Fragen mit Metadaten
- `strategies`: 3 Prompt-Strategien mit System- und Conversation-Prompts
- `responses`: Einzelne LLM-Antworten mit Zuordnung zu Strategie und Frage

## Status

**Aktuell:** MVP in Entwicklung
- ✅ Fragebogen validiert und dokumentiert
- ✅ Datenbank-Schema erstellt
- ✅ LiteLLM-Integration getestet
- ⏳ Survey-Runner in Entwicklung
- ⏳ Scoring-Logik
- ⏳ Streamlit-Dashboard

## Lizenz & Nutzung

Dieses Projekt ist ein persönliches Lernprojekt und steht unter der [WTFPL](http://www.wtfpl.net/) (Do What The Fuck You Want To Public License).

**Kurz gesagt:** Nimm den Code, mach was du willst und sei einfach keine Spaßbremse.

Wer den Code nutzt, sollte sich aber bewusst sein: Dies ist **kein Production-Code** und **keine wissenschaftliche Referenz**. Es ist ein Spielplatz zum Lernen und Experimentieren.

## Kontakt

Bei Fragen, Anregungen oder Interesse am Projekt: Feel free to reach out!

---

**Letzte Aktualisierung:** 2025-12-30
