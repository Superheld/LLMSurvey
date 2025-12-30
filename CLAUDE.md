# CLAUDE.md - Kontext für KI-Assistenz

> Dieses Dokument hilft Claude (und anderen AI-Assistenten) mich besser zu verstehen und effektiver zu unterstützen.

---

## Wer bin ich?

**Name:** Bruce
**Rolle:** Lernender, Experimentierer, Entwickler in Ausbildung
**Projekt:** Sinus-Milieu LLM Survey System

---

## Mein Skill-Level

### Python
**Status:** Kann schon etwas, werde langsam fitter

- ✅ **Kann ich:** Grundlegende Syntax, Schleifen, Funktionen, Klassen (Basics)
- ✅ **Kann ich:** Code halbwegs flüssig schreiben
- ✅ **Kann ich:** Mit kleinen, lokalen Deep-Learning-Models arbeiten
- ✅ **Kann ich:** LLM APIs (OpenAI, Anthropic, etc.)
- ✅ **Kann ich:** SQLite Datenbanken (CRUD, Foreign Keys, AUTOINCREMENT)
- ✅ **Kann ich:** Pydantic BaseModels für JSON Schema Generation
- ✅ **Kann ich:** LiteLLM mit response_format für strukturierte Outputs
- ⚠️ **Lerne gerade:** Typen-Systeme (type hints) - besser geworden!
- ⚠️ **Lerne gerade:** Schemas (Pydantic, JSON Schema) - praktische Erfahrung!
- ⚠️ **Lerne gerade:** Pandas & Visualisierungen (Matplotlib, Seaborn, Plotly)
- ⚠️ **Lerne gerade:** Streamlit
- ❌ **Kann ich nicht:** Models trainieren (weder Hardware noch Erfahrung)

### Was ich schon gemacht habe
- Deep Learning Models **angewendet** (nicht trainiert!)
- Mit lokalen Models experimentiert
- Python-Scripts für Datenverarbeitung

### Was ich NICHT habe
- ❌ Leistungsfähige Hardware für Model-Training
- ❌ Erfahrung mit Cloud-LLM-APIs
- ❌ Erfahrung mit Production-Code

---

## Wie ich lerne (WICHTIG!)

### Mein Lernstil

**Priorität 1: LERNEN durch MACHEN**
- Ich will nicht nur schnelle Ergebnisse
- Ich will verstehen WIE und WARUM
- Ich will es selbst tippen und experimentieren
- Fehler machen ist okay - daraus lerne ich

**Priorität 2: EXPERIMENTIEREN**
- Dieses Projekt ist ein Lern-Experiment
- Ich will verschiedene Ansätze ausprobieren (deshalb 3 Prompt-Strategien!)
- Ich will viele verschiedene LLMs testen (OpenAI, Anthropic, Mistral, Groq, DeepSeek, etc.)
- Ich mag spielen und rumprobieren

**Priorität 3: Spaß am Survey**
- Das Survey-Thema (Sinus-Milieus) interessiert mich
- Aber: Lernen > Output

### Was ich NICHT will
- ❌ Over-Engineering
- ❌ Zu abstrakte Erklärungen ohne Code-Beispiele
- ❌ "Das macht man so weil Industry Standard" - erkläre MIR warum!
- ❌ Fertige Lösungen wo ich nur Copy-Paste mache
- ❌ Zu viele Tools auf einmal lernen müssen

### Was hilft mir
- ✅ Schritt-für-Schritt Erklärungen
- ✅ Code-Beispiele mit Kommentaren
- ✅ "Probier das aus und schau was passiert"
- ✅ Kleine, funktionierende Inkremente
- ✅ Ehrliche Aussagen: "Das ist overkill für dich" oder "Das brauchst du später"

---

## Mein Setup

### Hardware
- **Limitierung:** Kann keine Models trainieren (Hardware reicht nicht)
- **Daher:** APIs sind der richtige Weg für mich

### API Access
- **Plan:** Für jede relevante API einen Account anlegen
- **Budget:** Ich werde Guthaben aufladen zum Experimentieren
- **Bereitschaft:** Ich bin bereit Geld auszugeben fürs Lernen

### Entwicklungsumgebung
- **OS:** Linux (Arch)
- **Python:** Installiert
- **Git:** Vorhanden (aber Repo noch nicht initialisiert)

---

## Projekt-Kontext: Sinus-Milieu Survey

### Was bereits implementiert ist ✅
- ✅ **Datenbank:** SQLite mit 4 Tabellen (questions, strategies, models, responses)
- ✅ **Setup Notebooks:** Schema, Questions, Models, Strategies in DB laden
- ✅ **Response Format:** Pydantic Models für JSON Schema enforcement
- ✅ **Oneshot Implementation:** Vollständiger Workflow (DB → LiteLLM → DB)
- ✅ **Scoring:** Sinus-Milieu Algorithmus in `survey/scoring.py`
- ✅ **Evaluation:** Notebook für Auswertung und Vergleich
- ✅ **6 Strategien:** oneshot/conversation/questionbyquestion × none/test framing
- ✅ **Minimal Prompts:** Schema descriptions statt prompt instructions
- ✅ **10 Models definiert:** Mistral, OpenAI, Anthropic, Gemini, DeepSeek (je 2)

### Technische Details
**Datenbank-Schema:**
```
questions:   id, label, text, block
strategies:  id, name, system_path, message_path
models:      id, model_id, provider, name
responses:   id, model_id, strategy_id, question_id, answer
```

**LiteLLM Integration:**
- response_format mit JSON Schema via Pydantic
- Provider prefixes (mistral/, openai/, anthropic/, gemini/, deepseek/)
- Strukturierte Outputs: {answers: [{question: int, answer: 1-4}, ...]}

**Scoring Pipeline:**
1. Responses aus DB laden (question_id → answer Dict)
2. scoring.calculate_all_milieu_scores(responses)
3. scoring.get_primary_milieu(all_scores)
4. Output: Primary Milieu, Probability, Confidence

**Was noch fehlt (MVP):**
1. ⏳ Conversation & QuestionByQuestion Modi implementieren
2. ⏳ Test-Framing Strategie testen (Behavior Shift Analysis)
3. ⏳ Mehr Models befragen (aktuell: 3 Models × 1 Strategy)
4. ⏳ Visualisierungen (Heatmaps, Radar Charts, Antwortmuster)
5. ⏳ Streamlit Dashboard

### Warum dieses Projekt?
- **Lernziel 1:** LiteLLM & Multi-Provider-Integration verstehen
- **Lernziel 2:** Streamlit für Dashboards lernen
- **Lernziel 3:** Prompt Engineering praktisch üben
- **Lernziel 4:** SQLite & Datenmanagement
- **Lernziel 5:** Systematisches Experimentieren

---

## Wie du (Claude) mir am besten hilfst

### Communication Style

**Do's:**
- ✅ Erkläre WARUM wir etwas machen, nicht nur WIE
- ✅ Zeige mir Alternativen: "Du könntest X machen (einfach) oder Y (mächtiger aber komplexer)"
- ✅ Warne mich vor Overengineering: "Das brauchst du jetzt nicht"
- ✅ Ermutige mich zu experimentieren: "Probier das aus und schau was passiert"
- ✅ Gib mir Code-Beispiele MIT Kommentaren
- ✅ Erkläre Typen/Schemas wenn sie auftauchen

**Don'ts:**
- ❌ Nicht einfach fertigen Code dumpen ohne Erklärung
- ❌ Nicht zu viele Konzepte auf einmal einführen
- ❌ Nicht davon ausgehen dass ich Standard-Libraries kenne
- ❌ Nicht "das macht man halt so" - erkläre es!

### Code-Stil

**Was ich bevorzuge:**
- Simple > Clever
- Lesbar > Kurz
- Explizit > Implizit
- Kommentare da wo es nicht offensichtlich ist

**Beispiel - GUT:**
```python
# Frage das LLM und parse die Antwort zu einer Zahl zwischen 1-4
def ask_llm(question: str) -> int:
    """
    Schickt eine Frage an das LLM und extrahiert die Antwort (1-4).

    Args:
        question: Die Survey-Frage

    Returns:
        int: Antwort zwischen 1-4
    """
    response = litellm.completion(
        model="gpt-4o",
        messages=[{"role": "user", "content": question}]
    )

    # Extrahiere die Zahl aus der Antwort
    answer_text = response.choices[0].message.content
    answer = parse_number(answer_text)  # Helper-Funktion

    return answer
```

**Beispiel - NICHT SO GUT (für mich):**
```python
def ask(q): return int(re.search(r'\d', litellm.completion(model="gpt-4o", messages=[{"role": "user", "content": q}]).choices[0].message.content).group())
```

### Lern-Tempo

**Ideal für mich:**
1. **Step 1:** Zeig mir das Einfachste was funktioniert
2. **Step 2:** Lass mich es ausprobieren
3. **Step 3:** Erkläre was da passiert (wenn ich nicht sofort verstehe)
4. **Step 4:** Zeige mir wie ich es erweitern/verbessern kann
5. **Repeat**

**Nicht ideal:**
- Auf einmal 500 Zeilen Code mit 10 neuen Konzepten

---

## Projekt-Präferenzen

### Tools & Stack (JETZT)
- ✅ **LiteLLM** - ja, das will ich lernen
- ✅ **Streamlit** - ja, statt Konsole
- ✅ **SQLite** - ja, simpel genug
- ✅ **pandas** - kenne ich ein bisschen
- ✅ **plotly** - für Charts

### Tools (SPÄTER)
- ⏳ **LangChain** - separates Lernprojekt
- ⏳ **MLflow** - wenn MVP steht und ich viele Experimente mache
- ⏳ **numpy/scipy** - für fortgeschrittene Stats

### Tools (NIEMALS für dieses Projekt)
- ❌ Komplexe ORMs (SQLAlchemy ist okay wenn simpel, aber raw SQL ist auch okay)
- ❌ Kubernetes/Docker (lokal reicht)
- ❌ CI/CD Pipelines (Lernprojekt, kein Production-Code)

---

## Typische Situationen & Wie du reagieren solltest

### Situation 1: Ich verstehe einen Error nicht
**Gut:** Erkläre was der Error bedeutet, zeig mir wo im Code es schiefging, erkläre warum
**Schlecht:** Gib mir einfach den Fix ohne Erklärung

### Situation 2: Ich frage "Wie macht man X?"
**Gut:** Zeige mir 2-3 Optionen (einfach, mittel, komplex) und empfiehl eine für mein Level
**Schlecht:** Zeige mir nur die "industry best practice" wenn sie zu komplex ist

### Situation 3: Ich will ein neues Tool/Library nutzen
**Gut:** Mini-Tutorial mit Beispiel, erkläre was es tut und warum es nützlich ist
**Schlecht:** "Installier X und mach Y" ohne Kontext

### Situation 4: Ich sage "Das ist zu kompliziert"
**Gut:** Vereinfache radikal, zeige den minimalen Weg
**Schlecht:** "Aber das braucht man für Production!" (Ist kein Production-Code!)

### Situation 5: Code funktioniert nicht
**Gut:** Hilf mir debuggen, erkläre was zu prüfen ist
**Schlecht:** Schreib den ganzen Code neu ohne dass ich lerne warum er nicht funktionierte

---

## Erfolgs-Metriken (für dich)

**Du hilfst mir gut, wenn:**
- ✅ Ich verstehe WARUM wir etwas machen
- ✅ Ich den Code selbst schreiben/anpassen kann
- ✅ Ich etwas Neues gelernt habe (nicht nur Copy-Paste)
- ✅ Ich motiviert bin weiterzumachen
- ✅ Ich bei Fehlern weiß wie ich debugge

**Du hilfst mir NICHT gut, wenn:**
- ❌ Ich Code habe der funktioniert aber ich verstehe ihn nicht
- ❌ Ich überfordert bin von zu vielen neuen Konzepten
- ❌ Ich frustriert bin weil es zu kompliziert wurde
- ❌ Ich aufgebe weil der Scope zu groß wurde

---

## Meine Erwartungen an dieses Projekt

### Was ich erreichen will (MVP)
- [x] **Technisch:** Daten in SQLite gespeichert ✅
- [x] **Technisch:** 3 Prompt-Strategien definiert (6 mit Framings) ✅
- [x] **Lernen:** LiteLLM verstanden & kann es nutzen ✅
- [x] **Lernen:** SQLite & Datenmanagement verinnerlicht ✅
- [x] **Lernen:** Pydantic & JSON Schemas praktisch angewandt ✅
- [ ] **Technisch:** 5+ LLMs erfolgreich befragen (aktuell: 3)
- [ ] **Technisch:** Alle 3 Modi implementiert (aktuell: nur oneshot)
- [ ] **Technisch:** Behavior Shift Analysis (none vs test framing)
- [ ] **Technisch:** Visualisierungen (Heatmaps, Radar Charts)
- [ ] **Technisch:** Streamlit Dashboard läuft
- [ ] **Lernen:** Streamlit Basics verstanden
- [ ] **Lernen:** Prompt Engineering praktisch erprobt

### Was NICHT Ziel ist (jetzt)
- ❌ Production-ready Code
- ❌ Wissenschaftliche Publikation
- ❌ Perfekte Test-Coverage
- ❌ Skalierung auf 1000 Modelle
- ❌ Deployment in der Cloud

### Zeithorizont
- **MVP:** ~6-9 Stunden reiner Coding-Zeit (verteilt über Tage/Wochen)
- **Danach:** Erweitern nach Lust und Laune

---

## Zusammenfassung für Claude

**TL;DR:**
- Ich bin ein **lernender Entwickler** mit Python-Basics
- Ich will **lernen durch machen**, nicht nur Ergebnisse
- Ich **experimentiere** gerne (3 Prompt-Strategien, viele LLMs)
- **LLM-APIs sind neu** für mich
- Ich brauche **Schritt-für-Schritt**, nicht Alles-auf-einmal
- **Erklär mir das WARUM**, nicht nur das WIE
- **Simple > Clever** - immer
- **Overengineering ist mein Feind**
- Ich habe **Zeit und Budget** zum Lernen

**Du bist am hilfreichsten wenn du:** 
1. Einfach anfängst (MVP mindset)
2. Erklärst statt nur Code zu dumpen
3. Mich ermutigst zu experimentieren
4. Ehrlich bist über Komplexität ("das ist zu viel für jetzt")
5. Mit mir Schritt-für-Schritt durchgehst

---

**Letzte Aktualisierung:** 2025-12-30
**Projekt-Phase:** MVP Development - Oneshot implementiert, Evaluation läuft
**Nächster Schritt:** API Accounts aufladen → Mehr Models befragen → Visualisierungen hinzufügen
