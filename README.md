# LLM-Survey: Sinus-Milieu Befragung mit Large Language Models

## Projektziel

Dieses Projekt ist ein **Lernexperiment**, das untersucht wie verschiedene Large Language Models (LLMs), mehrfach mit unterschiedlichen Promptstrategien angesprochen, auf einen standardisierten Fragebogen zur Sinus-Milieu-Zuordnung reagieren.

**Wichtig:** Dieses Projekt dient ausschließlich dem Lernen und Experimentieren. Die Ergebnisse sind in keiner Weise repräsentativ oder wissenschaftlich valide. Es geht nicht darum, belastbare Aussagen über LLMs oder Sinus-Milieus zu treffen, sondern darum, praktische Erfahrungen mit verschiedenen Technologien zu sammeln. 

**Hinweis:** Das Projekt wurde mit Hilfe von Claude Code erstellt. In der Regel habe ich den Code geschrieben und Claude war mein "Forum". Beim Setup hat er weite Teile geschrieben. In der Regel ist es an den Kommentaren (englisch vs. deutsch) erkennbar ;-)

## Lernziele

Das Projekt verfolgt folgende technische Lernziele:

- **LiteLLM & Multi-Provider-Integration:** Praktischer Umgang mit verschiedenen LLM-APIs (OpenAI, Anthropic, Mistral, Groq, DeepSeek, etc.) über eine einheitliche Schnittstelle
- **Prompt Engineering:** Systematisches Experimentieren mit verschiedenen Prompt-Strategien (One-Shot, Conversation, Step-by-Step)
- **Streamlit:** Aufbau interaktiver Dashboards zur Datenvisualisierung
- **Datenmanagement:** SQLite-Datenbankdesign und -verwaltung für experimentelle Daten
- **Systematisches Experimentieren:** Strukturierte Erfassung und Auswertung von Multi-Model-Experimenten

## Was dieses Projekt zeigen kann (und was nicht)

### Interessante Beobachtungen, die möglich sind:

- **Prompt-Sensitivität:** Wie reagiert dasselbe Model auf unterschiedliche Prompt-Strategien? Schwanken die "Milieu-Zuordnungen" stark oder bleiben sie konsistent? Diese Variabilität ist ein Hinweis auf das "Innenleben" des Models.

- **Model-Vergleiche:** Wie unterscheiden sich verschiedene Models bei identischen Prompts? Welche Patterns zeigen sich in Abhängigkeit von Trainingsdaten, Alignment-Strategien oder Modell-Architektur?

- **Systematisches LLM-Verhalten:** Gibt es konsistente Antworttendenzen über Models und Strategien hinweg? Zeigen sich Artefakte der Trainings- oder Alignment-Prozesse?

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

### Prompt-Strategien
Das Projekt testet drei verschiedene Befragungsansätze:

1. **One-Shot:** Alle 29 Fragen in einem einzigen Prompt
2. **Conversation:** Frage-für-Frage im interaktiven Dialog
3. **Step-by-Step:** Blockweise Befragung (6 thematische Blöcke)

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
