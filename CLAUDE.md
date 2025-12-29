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
- ⚠️ **Lerne gerade:** Typen-Systeme (type hints)
- ⚠️ **Lerne gerade:** Schemas (Pydantic, JSON Schema, etc.)
- ⚠️ **Lerne gerade:** Ein/Ausgaben verschiedener Libraries verstehen
- ⚠️ **Lerne gerade:** Streamlit
- ❌ **Kann ich nicht:** Models trainieren (weder Hardware noch Erfahrung)
- ❌ **Neu für mich:** LiteLLM

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

### Was ich schon habe
- ✅ 29-Item Fragebogen (validiert) in `fragen_v1.1.md`
- ✅ Item-Mapping Matrix in `item_mapping.md`
- ✅ Scoring-Code (Python) in `scoring.md`
- ✅ PRD (vereinfachte MVP-Version)

### Was ich bauen will (MVP)
1. **Survey-Runner:** LLMs mit 29 Fragen befragen
2. **3 Prompt-Strategien:** One-Shot, Conversation, Step-by-Step
3. **Multi-Provider:** Viele verschiedene LLMs testen
4. **Datenbank:** SQLite (2 Tabellen: runs + responses)
5. **Scoring:** Milieu-Zuordnung berechnen
6. **Dashboard:** Streamlit-UI für Visualisierung

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
- [ ] **Technisch:** 5+ LLMs erfolgreich befragen
- [ ] **Technisch:** 3 Prompt-Strategien implementiert
- [ ] **Technisch:** Daten in SQLite gespeichert
- [ ] **Technisch:** Streamlit Dashboard läuft
- [ ] **Lernen:** LiteLLM verstanden & kann es nutzen
- [ ] **Lernen:** Streamlit Basics verstanden
- [ ] **Lernen:** Prompt Engineering praktisch erprobt
- [ ] **Lernen:** SQLite & Datenmanagement verinnerlicht

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

**Letzte Aktualisierung:** 2025-12-28
**Projekt-Phase:** Planning → Ready to start coding
**Nächster Schritt:** Step 1 - Setup & Erste Befragung
