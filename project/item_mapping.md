# Sinus-Milieu Item-Mapping-Matrix: Detaillierte Auswertungslogik

## Übersicht

Dieses Dokument definiert **exakt**, wie die 29 Standard-Items (und 75 erweiterten Items) zu den 10 Sinus-Milieus zugeordnet werden. Für jedes Milieu werden die indikatorischen Items mit Gewichtungen und theoretischer Begründung spezifiziert.

## Methodologische Grundlagen

### Scoring-Prinzipien

**1. Item-Gewichtungen:**
- **Kern-Indikatoren** (Gewicht 1.5): Items, die zentral für ein Milieu sind
- **Starke Indikatoren** (Gewicht 1.0): Items, die klar zum Milieu passen
- **Moderate Indikatoren** (Gewicht 0.7): Items, die teilweise indikativ sind
- **Negative Indikatoren** (Gewicht -1.0 bis -1.5): Items, die gegen ein Milieu sprechen (reverse-coded)

**2. Antwortskala:**
```
1 = Stimme überhaupt nicht zu
2 = Stimme eher nicht zu
3 = Stimme eher zu
4 = Stimme voll und ganz zu
```

**3. Score-Berechnung pro Milieu:**
```
Milieu_Score = Σ(Item_Response × Item_Weight) / Σ(|Item_Weight|)

Normalisierung: Z-Score gegen theoretische Erwartungswerte
Probability: Sigmoid(Z-Score) → [0,1]
```

---

## Milieu 1: Konservativ-Etablierte (10% der Bevölkerung)

### Charakteristik
Klassisches Establishment mit Exklusivitätsanspruch, Statusbewusstsein und Verantwortungsethik. Betonung von Tradition, Ordnung, Qualität und Distinktion.

### Item-Mapping (Standard-29)

| Item | Aussage | Gewicht | Erwarteter Wert | Begründung |
|------|---------|---------|-----------------|------------|
| **1** | Traditionelle Werte geben Leben Orientierung | **+1.5** | 3.5 | **KERN-INDIKATOR**: Tradition ist zentral für dieses Milieu |
| **2** | Bewährte Lösungen bevorzugt | **+1.2** | 3.3 | Konservatismus, Skepsis gegenüber Experimenten |
| **6** | Sicherheit > Abenteuer | **+1.0** | 3.2 | Risikoaversion, Stabilitätsorientierung |
| **14** | Qualität statt Preis | **+1.3** | 3.7 | **Premium-Orientierung**, Distinktionskonsum |
| **15** | Marken sagen etwas über Persönlichkeit | **+0.8** | 3.0 | Status-Signaling, aber nicht Hauptfokus |
| **21** | Familie an erster Stelle | **+1.0** | 3.5 | Traditionelle Familienwerte |
| **23** | Kleiner, enger Freundeskreis | **+0.7** | 3.0 | Exklusivität in sozialen Beziehungen |
| **29** | Anpassung statt Veränderung | **+0.9** | 3.0 | Erhalt bestehender Verhältnisse |
| **3** | Erfolg & Leistung zentral | **-0.3** | 2.5 | Eher Status durch Herkunft als durch Leistung |
| **7** | Trends früh erkennen | **-1.2** | 1.8 | **NEGATIV**: Trendsetting passt nicht zu Konservatismus |
| **9** | Autoritäten hinterfragen | **-1.5** | 1.5 | **KERN-NEGATIV**: Respekt vor Autorität ist zentral |
| **28** | Gesellschaftlicher Wandel positiv | **-1.0** | 2.0 | Skepsis gegenüber raschem Wandel |

**Theoretische Erwartungswerte:**
- Mean Score: **3.1** (überdurchschnittlich bei traditionellen Items)
- SD: **0.6**
- Typisches Profil: Hohe Zustimmung zu 1, 2, 6, 14, 21; Ablehnung von 7, 9, 28

### Zusätzliche Items (Erweiterte Version 75)

| Item | Aussage | Gewicht | Erwarteter Wert |
|------|---------|---------|-----------------|
| **15** | Bewährte Traditionen bewahren | +1.5 | 3.7 |
| **13** | Ordnung und Struktur wichtig | +1.2 | 3.5 |
| **10** | Prestige und Status motivieren | +0.9 | 3.2 |
| **34** | Ausführliche Kaufinformationen | +1.0 | 3.4 |
| **61** | Kulturelle Veranstaltungen besuchen | +0.8 | 3.1 |
| **40** | Neue Technologien früh ausprobieren | -1.0 | 2.0 |

---

## Milieu 2: Postmaterielle (7% der Bevölkerung)

### Charakteristik
Souveräne Bildungselite mit intellektueller Anspruchshaltung und Umweltbewusstsein. **2021 Fusion aus Liberal-Intellektuellen und Sozial-Ökologischen.** Betonung von Bildung, Kultur, Kritik, Nachhaltigkeit.

### Item-Mapping (Standard-29)

| Item | Aussage | Gewicht | Erwarteter Wert | Begründung |
|------|---------|---------|-----------------|------------|
| **5** | Nachhaltigkeit beeinflusst Entscheidungen | **+1.5** | 3.8 | **KERN**: Umweltbewusstsein zentral |
| **8** | Gemeinschaft & soziale Verantwortung | **+1.3** | 3.6 | Gesellschaftliche Verantwortung |
| **9** | Autoritäten hinterfragen | **+1.2** | 3.5 | **Kritisches Denken**, Reflexivität |
| **24** | Interesse an Kunst, Kultur, Intellekt | **+1.5** | 3.9 | **KERN**: Hochkultur-Orientierung |
| **26** | Täglich über Ereignisse informieren | **+1.2** | 3.7 | Politisches Bewusstsein |
| **18** | Lokale/regionale Produkte | **+1.0** | 3.4 | Nachhaltigkeitsaspekt |
| **19** | Second-Hand normal | **+0.9** | 3.2 | Anti-Konsum, Nachhaltigkeit |
| **22** | Engagement für soziale Zwecke | **+1.3** | 3.5 | Gesellschaftliches Engagement |
| **3** | Erfolg & Leistung zentral | **-0.8** | 2.2 | **Postmaterialismus**: Nicht erfolgsorientiert |
| **4** | Wichtig was andere denken | **-1.0** | 1.8 | Souveränität, nicht statusorientiert |
| **15** | Marken sagen etwas aus | **-1.2** | 1.7 | **NEGATIV**: Anti-Konsum, nicht markenfixiert |
| **16** | Sofortige Freude durch Kauf | **-1.0** | 1.9 | Kritik am Konsumismus |

**Theoretische Erwartungswerte:**
- Mean Score: **3.2**
- SD: **0.7**
- Typisches Profil: Maximale Zustimmung zu 5, 24, 26; starke Ablehnung von 4, 15, 16

### Zusätzliche Items (Erweiterte Version)

| Item | Aussage | Gewicht | Erwarteter Wert |
|------|---------|---------|-----------------|
| **12** | Jeder kann Gesellschaft positiv verändern | +1.4 | 3.7 |
| **14** | Kulturelle Vielfalt schätzen | +1.3 | 3.8 |
| **25** | Arbeit soll gesellschaftlichen Mehrwert haben | +1.2 | 3.6 |
| **36** | Fair gehandelte Waren | +1.5 | 3.8 |
| **39** | Minimalismus & Verzicht | +1.0 | 3.3 |
| **63** | Anspruchsvolle Bücher | +1.2 | 3.7 |
| **65** | Gesellschaftliche Themen diskutieren | +1.4 | 3.8 |
| **74** | Klimawandel bereitet Sorgen | +1.5 | 3.9 |

---

## Milieu 3: Performer (8% der Bevölkerung)

### Charakteristik
Effizienzorientierte, technokratische Elite mit globalem Wirtschaftsdenken, Technologieaffinität und Leistungsorientierung. Strategisches Karriere-Planning, Work-Life-Optimierung.

### Item-Mapping (Standard-29)

| Item | Aussage | Gewicht | Erwarteter Wert | Begründung |
|------|---------|---------|-----------------|------------|
| **3** | Erfolg & Leistung zentral | **+1.5** | 3.9 | **KERN**: Achievement-Orientierung |
| **9** | Beruflicher Erfolg ist Identität | **+1.5** | 3.8 | **KERN**: Karriere-Fokus |
| **10** | Abläufe & Prozesse optimieren | **+1.4** | 3.8 | **Effizienz**, systematisches Denken |
| **12** | Selbstständig & eigenverantwortlich | **+1.2** | 3.7 | Autonomie, Unternehmergeist |
| **27** | Zukunft optimistisch | **+1.0** | 3.5 | Positives Mindset, Machbarkeit |
| **7** | Trends früh erkennen | **+0.9** | 3.3 | Innovation, First-Mover |
| **14** | Qualität statt Preis | **+0.8** | 3.2 | Premium, aber funktional |
| **11** | Work-Life-Balance wichtiger als Karriere | **-1.5** | 1.7 | **KERN-NEGATIV**: Karriere hat Priorität |
| **13** | Harmonie wichtiger als Leistung | **-1.3** | 1.8 | **Performance** > Harmonie |
| **23** | Kleiner Freundeskreis | **-0.7** | 2.3 | Großes Netzwerk für Erfolg |
| **29** | Anpassung statt Veränderung | **-1.0** | 2.0 | Gestaltungswille, nicht Anpassung |

**Theoretische Erwartungswerte:**
- Mean Score: **3.3**
- SD: **0.5**
- Typisches Profil: Maximum bei 3, 9, 10, 12; Minimum bei 11, 13

### Zusätzliche Items (Erweiterte Version)

| Item | Aussage | Gewicht | Erwarteter Wert |
|------|---------|---------|-----------------|
| **17** | Abläufe optimieren | +1.5 | 3.9 |
| **21** | Führungsverantwortung übernehmen | +1.3 | 3.7 |
| **22** | Kreativität & Innovation wichtig | +1.2 | 3.6 |
| **26** | Flexibilität bei Arbeitszeit/-ort | +1.0 | 3.5 |
| **27** | Regelmäßige Weiterbildung | +1.3 | 3.8 |
| **40** | Neue Technologien früh ausprobieren | +1.4 | 3.7 |
| **46** | KI faszinierend | +1.2 | 3.6 |
| **49** | Digitale Tools zur Alltags-Optimierung | +1.4 | 3.8 |
| **54** | Networking wichtig | +1.3 | 3.7 |

---

## Milieu 4: Expeditive (7% der Bevölkerung)

### Charakteristik
Ambitionierte, kreative, urbane Professionals mit Digital-Native-Status, kosmopolitischer Ausrichtung. Networking-Expertise, kulturelle Mobilität, Trendsetting, pragmatischer Idealismus.

### Item-Mapping (Standard-29)

| Item | Aussage | Gewicht | Erwarteter Wert | Begründung |
|------|---------|---------|-----------------|------------|
| **7** | Trends früh erkennen | **+1.5** | 3.8 | **KERN**: Trendsetter, Early Adopter |
| **20** | Großer Bekanntenkreis, neue Kontakte | **+1.4** | 3.8 | **Networking-Intensität** |
| **12** | Selbstständig & eigenverantwortlich | **+1.2** | 3.6 | Autonomie, Flexibilität |
| **14** | Qualität statt Preis | **+0.9** | 3.3 | Lifestyle-Konsum, aber nicht elitär |
| **27** | Zukunft optimistisch | **+1.0** | 3.5 | Aufbruchsstimmung |
| **28** | Wandel positiv & notwendig | **+1.2** | 3.6 | Change-Affinität |
| **17** | Zuhause spiegelt Stil & Werte | **+1.0** | 3.4 | Lifestyle-Expression |
| **2** | Bewährte Lösungen bevorzugt | **-1.3** | 1.8 | **NEGATIV**: Experimentierfreude statt Konservatismus |
| **6** | Sicherheit > Abenteuer | **-1.2** | 1.9 | Risikobereitschaft |
| **23** | Kleiner Freundeskreis | **-1.4** | 1.6 | **KERN-NEGATIV**: Breites Netzwerk |
| **29** | Anpassung statt Veränderung | **-1.5** | 1.5 | Gestalter, nicht Anpasser |

**Theoretische Erwartungswerte:**
- Mean Score: **3.0**
- SD: **0.6**
- Typisches Profil: Hoch bei 7, 20, 28; sehr niedrig bei 23, 29

### Zusätzliche Items (Erweiterte Version)

| Item | Aussage | Gewicht | Erwarteter Wert |
|------|---------|---------|-----------------|
| **14** | Kulturelle Vielfalt schätzen | +1.4 | 3.7 |
| **22** | Kreativität & Innovation | +1.3 | 3.7 |
| **24** | Internationale/multikulturelle Teams | +1.4 | 3.8 |
| **40** | Neue Technologien früh ausprobieren | +1.5 | 3.9 |
| **41** | Soziale Medien aktiv nutzen | +1.3 | 3.7 |
| **45** | Eigene Inhalte online erstellen | +1.2 | 3.5 |
| **54** | Networking wichtig | +1.5 | 3.8 |

---

## Milieu 5: Neo-Ökologische (7% der Bevölkerung)

### Charakteristik
**NEU 2021**: Treiber globaler Gesellschaftstransformation. Optimistischer Environmentalismus, Post-Wachstums-Ökonomie, soziale Gerechtigkeit, Glaube an systemischen Wandel.

### Item-Mapping (Standard-29)

| Item | Aussage | Gewicht | Erwarteter Wert | Begründung |
|------|---------|---------|-----------------|------------|
| **5** | Nachhaltigkeit beeinflusst Entscheidungen | **+1.5** | 3.9 | **KERN**: Klima & Umwelt zentral |
| **8** | Gemeinschaft & soziale Verantwortung | **+1.4** | 3.7 | Transformative Gemeinschaft |
| **28** | Wandel positiv & notwendig | **+1.5** | 3.9 | **KERN**: Systemtransformation |
| **27** | Zukunft optimistisch | **+1.3** | 3.8 | **Optimismus** trotz Krise |
| **18** | Lokale/regionale Produkte | **+1.2** | 3.7 | Nachhaltiger Konsum |
| **19** | Second-Hand normal | **+1.3** | 3.6 | Kreislaufwirtschaft |
| **22** | Engagement für soziale Zwecke | **+1.4** | 3.8 | Aktivismus |
| **7** | Trends früh erkennen | **+0.9** | 3.3 | Innovation, aber nicht Konsum-Trends |
| **16** | Sofortige Freude durch Kauf | **-1.5** | 1.5 | **KERN-NEGATIV**: Anti-Konsumismus |
| **15** | Marken sagen etwas aus | **-1.3** | 1.6 | Ablehnung von Status-Konsum |
| **4** | Wichtig was andere denken | **-1.0** | 2.0 | Authentizität > Status |

**Theoretische Erwartungswerte:**
- Mean Score: **3.4**
- SD: **0.6**
- Typisches Profil: Maximum bei 5, 28, 27; Minimum bei 16, 15

### Zusätzliche Items (Erweiterte Version)

| Item | Aussage | Gewicht | Erwarteter Wert |
|------|---------|---------|-----------------|
| **12** | Jeder kann Gesellschaft verändern | +1.5 | 3.9 |
| **25** | Arbeit soll Mehrwert haben | +1.4 | 3.8 |
| **36** | Fair gehandelte Waren | +1.5 | 3.9 |
| **39** | Minimalismus & Verzicht | +1.4 | 3.7 |
| **46** | KI faszinierend (wenn ethisch) | +0.7 | 3.0 |
| **74** | Klimawandel bereitet Sorgen | +1.5 | 3.9 |
| **75** | Nächste Generation bessere Bedingungen | +1.2 | 3.5 |

---

## Milieu 6: Adaptiv-Pragmatische (9% der Bevölkerung)

### Charakteristik
Moderne Mitte mit Flexibilitätsbetonung, Zugehörigkeitsbedürfnissen, pragmatischer Anpassungsfähigkeit. Sicherheitssuche balanciert mit Veränderungsakzeptanz, Mainstream-Konsum, moderate politische Positionen.

### Item-Mapping (Standard-29)

| Item | Aussage | Gewicht | Erwarteter Wert | Begründung |
|------|---------|---------|-----------------|------------|
| **11** | Work-Life-Balance wichtiger | **+1.2** | 3.5 | Balance-Orientierung |
| **18** | Lokale/regionale Produkte | **+0.8** | 3.1 | Pragmatischer Konsum |
| **27** | Zukunft optimistisch | **+0.9** | 3.2 | Moderat positiv |
| **8** | Gemeinschaft & Verantwortung | **+0.7** | 3.0 | Zugehörigkeit wichtig |
| **17** | Zuhause spiegelt Werte | **+0.7** | 3.0 | Lifestyle-Expression moderat |
| **ALLE Items** | Durchschnittlich moderate Werte | **Â±0.5** | 2.8-3.2 | **KERN**: Keine extremen Ausprägungen! |

**WICHTIG**: Dieses Milieu ist **nicht durch hohe Werte definiert**, sondern durch **Abwesenheit extremer Ausprägungen**. 

**Scoring-Logik:**
```python
# Adaptiv-Pragmatisch identifiziert durch:
variance = np.var(all_item_responses)
mean_deviation = np.mean(np.abs(all_item_responses - 2.5))

# Score steigt, wenn:
# - Niedrige Varianz (alle Items nah am Mittelwert)
# - Keine starken Zustimmungen (4) oder Ablehnungen (1)
```

**Theoretische Erwartungswerte:**
- Mean Score: **2.9** (nah am Skalenmittel 2.5)
- SD: **0.4** (niedrig!)
- Typisches Profil: Viele "3" (eher zu), wenige "1" oder "4"

---

## Milieu 7: Konsum-Hedonistische (13% der Bevölkerung)

### Charakteristik
Unterhaltungsfokussierte untere Mittelschicht mit Fun-, Konsum- und Sofortbefriedigungs-Betonung. Markenbewusstsein, Entertainment-Medien, Social Media, Work-Life-Balance > Karriere.

### Item-Mapping (Standard-29)

| Item | Aussage | Gewicht | Erwarteter Wert | Begründung |
|------|---------|---------|-----------------|------------|
| **16** | Sofortige Freude durch Kauf | **+1.5** | 3.7 | **KERN**: Hedonistischer Konsum |
| **25** | Unterhaltung & Fun wichtig | **+1.5** | 3.8 | **KERN**: Entertainment-Orientierung |
| **15** | Marken sagen etwas aus | **+1.2** | 3.5 | Markenbewusstsein |
| **11** | Work-Life-Balance wichtiger | **+1.3** | 3.6 | Leben > Karriere |
| **20** | Großer Bekanntenkreis | **+1.0** | 3.3 | Soziale Aktivität |
| **4** | Wichtig was andere denken | **+0.9** | 3.2 | Gruppenzugehörigkeit |
| **24** | Kunst, Kultur, Intellekt | **-1.5** | 1.6 | **KERN-NEGATIV**: Nicht hochkultur-orientiert |
| **26** | Täglich über Ereignisse informieren | **-1.2** | 1.9 | Weniger politisches Interesse |
| **5** | Nachhaltigkeit beeinflusst | **-0.9** | 2.2 | Weniger Umweltbewusstsein |
| **9** | Beruflicher Erfolg Identität | **-1.0** | 2.1 | Karriere nicht zentral |

**Theoretische Erwartungswerte:**
- Mean Score: **2.8**
- SD: **0.7**
- Typisches Profil: Hoch bei 16, 25, 15; niedrig bei 24, 26

### Zusätzliche Items (Erweiterte Version)

| Item | Aussage | Gewicht | Erwarteter Wert |
|------|---------|---------|-----------------|
| **37** | Schnäppchen & Sonderangebote | +1.3 | 3.6 |
| **41** | Soziale Medien aktiv | +1.4 | 3.7 |
| **62** | Reality-TV & Prominenten-News | +1.5 | 3.7 |
| **64** | Streaming & On-Demand | +1.3 | 3.6 |
| **63** | Anspruchsvolle Bücher | -1.4 | 1.7 |
| **65** | Gesellschaftliche Themen diskutieren | -1.2 | 1.9 |

---

## Milieu 8: Prekäre (9% der Bevölkerung)

### Charakteristik
Untere Klasse mit Teilhabe- und Anerkennungssuche bei ökonomischen Restriktionen. Aspiration nach Mainstream-Konsum, Sensibilität für soziale Exklusion, traditionelle Familienwerte, Statussorgen.

### Item-Mapping (Standard-29)

| Item | Aussage | Gewicht | Erwarteter Wert | Begründung |
|------|---------|---------|-----------------|------------|
| **4** | Wichtig was andere denken | **+1.5** | 3.7 | **KERN**: Anerkennung essentiell |
| **21** | Familie an erster Stelle | **+1.3** | 3.6 | Traditionelle Familienwerte |
| **29** | Anpassung statt Veränderung | **+1.2** | 3.4 | Vermeidung von Risiken |
| **16** | Sofortige Freude durch Kauf | **+1.0** | 3.3 | Kompensatorischer Konsum |
| **15** | Marken sagen etwas aus | **+1.1** | 3.4 | Status-Aspiration |
| **6** | Sicherheit > Abenteuer | **+1.3** | 3.5 | Existenzielle Sicherheit |
| **14** | Qualität statt Preis | **-1.4** | 1.7 | **ÖKONOMISCHE RESTRIKTION** |
| **24** | Kunst, Kultur, Intellekt | **-1.3** | 1.8 | Bildungsferne |
| **22** | Engagement soziale Zwecke | **-0.9** | 2.2 | Weniger Ressourcen für Engagement |
| **27** | Zukunft optimistisch | **-1.0** | 2.1 | Pessimismus aufgrund Lage |

**Theoretische Erwartungswerte:**
- Mean Score: **2.6**
- SD: **0.8**
- Typisches Profil: Hoch bei 4, 21, 6; niedrig bei 14, 24, 27

### Zusätzliche Items (Erweiterte Version)

| Item | Aussage | Gewicht | Erwarteter Wert |
|------|---------|---------|-----------------|
| **37** | Schnäppchen motivieren | +1.4 | 3.7 |
| **56** | Konflikte vermeiden | +1.2 | 3.5 |
| **42** | Datenschutz sehr wichtig | -0.8 | 2.3 |
| **27** | Weiterbildung investieren | -1.2 | 1.9 |

---

## Milieu 9: Nostalgisch-Bürgerliche (10% der Bevölkerung)

### Charakteristik
Harmonieorientierte Arbeiter-/Mittelschicht mit Sicherheits- und Stabilitätssuche. Gemeinschaftsorientierung, traditionelle Beziehungsmodelle, Skepsis gegenüber raschem Wandel, Präferenz für vertraute soziale Umgebungen.

### Item-Mapping (Standard-29)

| Item | Aussage | Gewicht | Erwarteter Wert | Begründung |
|------|---------|---------|-----------------|------------|
| **1** | Traditionelle Werte Orientierung | **+1.3** | 3.5 | Tradition wichtig |
| **13** | Harmonie wichtiger als Leistung | **+1.5** | 3.7 | **KERN**: Harmonie-Fokus |
| **23** | Kleiner, enger Freundeskreis | **+1.4** | 3.6 | Vertrautheit > Netzwerk |
| **21** | Familie an erster Stelle | **+1.4** | 3.7 | Familienzentrum |
| **8** | Gemeinschaft & Verantwortung | **+1.2** | 3.5 | Lokale Gemeinschaft |
| **6** | Sicherheit > Abenteuer | **+1.3** | 3.6 | Sicherheitsbedürfnis |
| **29** | Anpassung statt Veränderung | **+1.2** | 3.4 | Stabilität bewahren |
| **7** | Trends früh erkennen | **-1.5** | 1.5 | **KERN-NEGATIV**: Nicht trendsetting |
| **28** | Wandel positiv | **-1.3** | 1.7 | Skepsis gegenüber Wandel |
| **3** | Erfolg & Leistung zentral | **-0.9** | 2.2 | Nicht leistungsorientiert |

**Theoretische Erwartungswerte:**
- Mean Score: **3.0**
- SD: **0.6**
- Typisches Profil: Hoch bei 13, 21, 23; niedrig bei 7, 28

### Zusätzliche Items (Erweiterte Version)

| Item | Aussage | Gewicht | Erwarteter Wert |
|------|---------|---------|-----------------|
| **13** | Ordnung & Struktur wichtig | +1.3 | 3.6 |
| **15** | Traditionen bewahren | +1.4 | 3.7 |
| **56** | Konflikte vermeiden | +1.4 | 3.7 |
| **70** | Einschränkungen als Teil des Lebens | +1.1 | 3.4 |
| **40** | Neue Technologien ausprobieren | -1.4 | 1.7 |
| **45** | Inhalte online erstellen | -1.3 | 1.6 |

---

## Milieu 10: Traditionelle (10% der Bevölkerung)

### Charakteristik
Sicherheits- und ordnungsliebende ältere Generation mit kleinbürgerlichen Werten. Etablierte Routinen, Autoritätsrespekt, konventionelle Lebensstilmuster, Anpassung bei Bewahrung von Kernwerten.

### Item-Mapping (Standard-29)

| Item | Aussage | Gewicht | Erwarteter Wert | Begründung |
|------|---------|---------|-----------------|------------|
| **1** | Traditionelle Werte Orientierung | **+1.5** | 3.8 | **KERN**: Maximum Tradition |
| **2** | Bewährte Lösungen bevorzugt | **+1.5** | 3.8 | **KERN**: Konservatismus |
| **6** | Sicherheit > Abenteuer | **+1.5** | 3.9 | **KERN**: Sicherheitsorientierung |
| **29** | Anpassung statt Veränderung | **+1.4** | 3.7 | Erhalt Status Quo |
| **21** | Familie an erster Stelle | **+1.3** | 3.6 | Traditionelle Familie |
| **13** | Harmonie wichtiger als Leistung | **+1.2** | 3.5 | Kein Leistungsdruck |
| **23** | Kleiner Freundeskreis | **+1.1** | 3.4 | Vertraute Kreise |
| **7** | Trends früh erkennen | **-1.5** | 1.3 | **KERN-NEGATIV**: Anti-Modern |
| **9** | Autoritäten hinterfragen | **-1.5** | 1.4 | Autoritätsrespekt |
| **28** | Wandel positiv | **-1.4** | 1.5 | Wandel-Skepsis |
| **3** | Erfolg & Leistung zentral | **-1.2** | 1.8 | Bescheidenheit |

**Theoretische Erwartungswerte:**
- Mean Score: **3.2**
- SD: **0.5**
- Typisches Profil: Maximum bei 1, 2, 6, 29; Minimum bei 7, 9, 28

### Zusätzliche Items (Erweiterte Version)

| Item | Aussage | Gewicht | Erwarteter Wert |
|------|---------|---------|-----------------|
| **13** | Ordnung & Struktur | +1.5 | 3.9 |
| **15** | Traditionen bewahren | +1.5 | 3.9 |
| **40** | Neue Technologien | -1.5 | 1.3 |
| **46** | KI faszinierend | -1.5 | 1.4 |
| **47** | Digitale Kommunikation bevorzugen | -1.4 | 1.5 |

---

## Scoring-Algorithmus: Schritt-für-Schritt

### Schritt 1: Item-Response-Matrix einlesen

```python
# Beispiel LLM-Antworten (29 Items)
llm_responses = {
    1: 3,  # "Traditionelle Werte" → Stimme eher zu
    2: 2,  # "Bewährte Lösungen" → Stimme eher nicht zu
    3: 4,  # "Erfolg & Leistung" → Stimme voll zu
    # ... 26 weitere Items
}
```

### Schritt 2: Gewichtete Scores pro Milieu berechnen

```python
def calculate_milieu_score(responses, milieu_profile):
    """
    Args:
        responses: dict {item_id: score}
        milieu_profile: dict {
            'positive_indicators': {item_id: weight},
            'negative_indicators': {item_id: weight},
            'expected_mean': float,
            'expected_sd': float
        }
    
    Returns:
        dict with raw_score, z_score, probability
    """
    
    # Positive Indicators
    positive_sum = sum(
        responses[item_id] * weight 
        for item_id, weight in milieu_profile['positive_indicators'].items()
    )
    positive_weight_sum = sum(milieu_profile['positive_indicators'].values())
    
    # Negative Indicators (reverse-coded)
    negative_sum = sum(
        (5 - responses[item_id]) * abs(weight)  # Reverse: 4→1, 3→2, 2→3, 1→4
        for item_id, weight in milieu_profile['negative_indicators'].items()
    )
    negative_weight_sum = sum(abs(w) for w in milieu_profile['negative_indicators'].values())
    
    # Weighted Average
    raw_score = (positive_sum + negative_sum) / (positive_weight_sum + negative_weight_sum)
    
    # Z-Score gegen theoretische Erwartung
    z_score = (raw_score - milieu_profile['expected_mean']) / milieu_profile['expected_sd']
    
    # Probability via Sigmoid
    probability = 1 / (1 + np.exp(-z_score))
    
    return {
        'raw_score': raw_score,
        'z_score': z_score,
        'probability': probability
    }
```

### Schritt 3: Alle 10 Milieus berechnen

```python
all_milieu_scores = {}

for milieu_name, profile in SINUS_MILIEU_PROFILES.items():
    all_milieu_scores[milieu_name] = calculate_milieu_score(
        llm_responses, 
        profile
    )

# Sortieren nach Wahrscheinlichkeit
sorted_milieus = sorted(
    all_milieu_scores.items(), 
    key=lambda x: x[1]['probability'], 
    reverse=True
)
```

### Schritt 4: Primäre Zuordnung mit Confidence

```python
primary = sorted_milieus[0]
secondary = sorted_milieus[1]

confidence_gap = primary[1]['probability'] - secondary[1]['probability']

if confidence_gap > 0.15:
    classification = {
        'type': 'clear_case',
        'primary_milieu': primary[0],
        'primary_probability': primary[1]['probability'],
        'confidence': 'high'
    }
elif confidence_gap > 0.08:
    classification = {
        'type': 'moderate_case',
        'primary_milieu': primary[0],
        'primary_probability': primary[1]['probability'],
        'secondary_milieu': secondary[0],
        'secondary_probability': secondary[1]['probability'],
        'confidence': 'moderate'
    }
else:
    classification = {
        'type': 'boundary_case',
        'candidates': [primary[0], secondary[0]],
        'probabilities': [primary[1]['probability'], secondary[1]['probability']],
        'confidence': 'low',
        'note': 'Manuelle Experten-Review empfohlen'
    }
```

---

## Validierung & Quality Checks

### 1. Interne Konsistenz (Cronbach's Alpha)

```python
# Pro Milieu: Nur Items mit Gewicht > 0.8 verwenden
def check_internal_consistency(responses, milieu_profile):
    from pingouin import cronbach_alpha
    
    relevant_items = [
        item_id for item_id, weight in milieu_profile['positive_indicators'].items()
        if weight >= 0.8
    ]
    
    item_responses = [responses[i] for i in relevant_items]
    
    alpha = cronbach_alpha(item_responses)
    
    return {
        'cronbachs_alpha': alpha,
        'interpretation': 'good' if alpha > 0.70 else 'questionable',
        'item_count': len(relevant_items)
    }
```

### 2. Test-Retest Reliability (ICC)

```python
# Über multiple Runs
def calculate_test_retest(run1_scores, run2_scores, run3_scores):
    from pingouin import intraclass_corr
    
    # Reshape: runs × milieus
    data = pd.DataFrame({
        'run1': run1_scores,
        'run2': run2_scores,
        'run3': run3_scores
    })
    
    icc_result = intraclass_corr(
        data=data,
        targets='milieus',
        raters='runs',
        ratings='probability'
    )
    
    return icc_result['ICC'][0]
```

### 3. Face Validity Check

```python
# Plausibilität der Top-3-Zuordnungen
def validate_face_validity(top_3_milieus):
    """
    Checks ob Top-3 theoretisch kompatibel sind
    
    Beispiel: Konservativ-Etabliert + Traditionell = OK (benachbart)
    Konservativ-Etabliert + Neo-Ökologisch = WARNUNG (konträr)
    """
    
    # Kompatibilitäts-Matrix (aus Sinus-Literatur)
    COMPATIBILITY_MATRIX = {
        'Konservativ-Etablierte': ['Postmaterielle', 'Performer', 'Traditionelle'],
        'Postmaterielle': ['Konservativ-Etablierte', 'Neo-Ökologische', 'Performer'],
        'Performer': ['Konservativ-Etablierte', 'Expeditive', 'Postmaterielle'],
        # ... weitere
    }
    
    primary = top_3_milieus[0]
    compatible_milieus = COMPATIBILITY_MATRIX[primary]
    
    warnings = []
    for milieu in top_3_milieus[1:]:
        if milieu not in compatible_milieus:
            warnings.append(f"WARNUNG: {primary} und {milieu} sind theoretisch konträr!")
    
    return warnings
```

---

## Visualisierung der Scores

### Radar Chart

```python
import plotly.graph_objects as go

def create_milieu_radar(milieu_scores):
    categories = list(milieu_scores.keys())
    values = [scores['probability'] for scores in milieu_scores.values()]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='LLM Milieu-Profil'
    ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        title='Sinus-Milieu Probability Scores'
    )
    
    return fig
```

### Heatmap für LLM-Vergleich

```python
import seaborn as sns
import matplotlib.pyplot as plt

def create_llm_comparison_heatmap(llm_scores_dict):
    """
    llm_scores_dict: {
        'GPT-4': {milieu: probability, ...},
        'Claude': {milieu: probability, ...},
        ...
    }
    """
    
    df = pd.DataFrame(llm_scores_dict).T
    
    plt.figure(figsize=(14, 8))
    sns.heatmap(
        df,
        annot=True,
        fmt='.2f',
        cmap='RdYlGn',
        center=0.5,
        cbar_kws={'label': 'Probability'}
    )
    
    plt.title('LLM Milieu-Scores Comparison', fontsize=16)
    plt.xlabel('Sinus-Milieus', fontsize=12)
    plt.ylabel('LLMs', fontsize=12)
    plt.tight_layout()
    
    return plt.gcf()
```

---

## Zusammenfassung: Was macht gute Zuordnung aus?

### Starke Zuordnung (Confidence: High)

✅ **Hoher Primary Score** (Probability > 0.65)
✅ **Große Differenz zu Secondary** (Gap > 0.15)
✅ **Theoretisch plausibel** (Keine konträren Top-3)
✅ **Konsistent über Runs** (ICC > 0.70)
✅ **Klare Item-Patterns** (Erwartete Items haben erwartete Werte)

### Schwache Zuordnung (Confidence: Low)

âŒ Alle Scores im Mittelfeld (0.45 - 0.55)
âŒ Minimale Differenz zwischen Top-3 (<0.08)
âŒ Widersprüchliche Item-Patterns
âŒ Hohe Varianz über Runs (ICC < 0.50)
âŒ Theoretisch inkonsistent

---

## Nächste Schritte für Implementierung

1. **SINUS_MILIEU_PROFILES Dictionary erstellen** mit allen Gewichtungen aus diesem Dokument
2. **Scoring-Funktionen implementieren** wie oben beschrieben
3. **Validierungs-Pipeline aufsetzen** (Cronbach's Alpha, ICC, Face Validity)
4. **Pilot-Test** mit 1 LLM, 3 Runs → Debuggen
5. **Full Data Collection** mit allen LLMs und Bedingungen

**Diese Matrix ist jetzt die wissenschaftliche Grundlage für euer gesamtes Scoring-System!** 🎯