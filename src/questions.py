"""
Sinus-Milieu Survey Fragen (V1.1)

29 Items über 6 thematische Blöcke.
Antwortskala: 1-4 (1=stimme überhaupt nicht zu, 4=stimme voll und ganz zu)
"""

from pydantic import BaseModel, Field
from typing import List


class SurveyQuestion(BaseModel):
    """Eine einzelne Survey-Frage mit Validation"""
    item_id: int = Field(ge=1, le=29, description="Item-Nummer 1-29")
    label: str = Field(min_length=1, description="Item-Label wie TRADITION_KERN")
    text: str = Field(min_length=10, description="Die eigentliche Frage")
    block: str = Field(description="Themenblock")

    class Config:
        frozen = True  # Unveränderlich


# Instruktionen für die Befragung
SURVEY_INSTRUCTION = """Bitte bewerten Sie jede Aussage nach Ihrem persönlichen Empfinden. Es gibt keine richtigen oder falschen Antworten.

Antwortskala:
1 = Stimme überhaupt nicht zu
2 = Stimme eher nicht zu
3 = Stimme eher zu
4 = Stimme voll und ganz zu"""


# Alle 29 Survey-Fragen
QUESTIONS: List[SurveyQuestion] = [
    # Block 1: Grundwerte und Lebensorientierung (8 Items)
    SurveyQuestion(
        item_id=1,
        label="TRADITION_KERN",
        text="Bewährte Traditionen und Werte geben meinem Leben wichtige Orientierung.",
        block="Grundwerte"
    ),
    SurveyQuestion(
        item_id=2,
        label="INNOVATION_VS_BEWAHRUNG",
        text="Ich bevorzuge erprobte Lösungen gegenüber neuen, ungetesteten Ansätzen.",
        block="Grundwerte"
    ),
    SurveyQuestion(
        item_id=3,
        label="LEISTUNG_IDENTITAET",
        text="Persönlicher Erfolg und berufliche Leistung sind zentrale Bausteine meiner Identität.",
        block="Grundwerte"
    ),
    SurveyQuestion(
        item_id=4,
        label="SOZIALE_ANERKENNUNG",
        text="Es ist mir wichtig, von anderen respektiert und anerkannt zu werden.",
        block="Grundwerte"
    ),
    SurveyQuestion(
        item_id=5,
        label="NACHHALTIGKEIT_VERHALTEN",
        text="Nachhaltigkeit und Umweltschutz beeinflussen konkret meine alltäglichen Entscheidungen.",
        block="Grundwerte"
    ),
    SurveyQuestion(
        item_id=6,
        label="SICHERHEIT_VS_RISIKO",
        text="Sicherheit und Stabilität haben für mich höhere Priorität als neue Erfahrungen und Risiken.",
        block="Grundwerte"
    ),
    SurveyQuestion(
        item_id=7,
        label="TRENDSETTING",
        text="Ich erkenne gesellschaftliche und kulturelle Trends früher als die meisten Menschen.",
        block="Grundwerte"
    ),
    SurveyQuestion(
        item_id=8,
        label="GEMEINWOHL_ORIENTIERUNG",
        text="Gemeinschaft und soziale Verantwortung sind wichtige Leitprinzipien für mich.",
        block="Grundwerte"
    ),

    # Block 2: Arbeit und Karriere (5 Items)
    SurveyQuestion(
        item_id=9,
        label="KARRIERE_IDENTITAET",
        text="Mein beruflicher Erfolg definiert maßgeblich, wer ich bin.",
        block="Arbeit"
    ),
    SurveyQuestion(
        item_id=10,
        label="OPTIMIERUNG_AFFINITAET",
        text="Ich optimiere gerne Abläufe, Prozesse und Systeme für bessere Effizienz.",
        block="Arbeit"
    ),
    SurveyQuestion(
        item_id=11,
        label="WORK_LIFE_BALANCE",
        text="Eine ausgeglichene Work-Life-Balance ist mir wichtiger als maximaler Karriereerfolg.",
        block="Arbeit"
    ),
    SurveyQuestion(
        item_id=12,
        label="AUTONOMIE_WUNSCH",
        text="Ich arbeite am liebsten selbstbestimmt und eigenverantwortlich.",
        block="Arbeit"
    ),
    SurveyQuestion(
        item_id=13,
        label="HARMONIE_VS_LEISTUNG",
        text="Ein harmonisches Arbeitsklima ist mir wichtiger als hoher Leistungsdruck.",
        block="Arbeit"
    ),

    # Block 3: Konsum und Lifestyle (6 Items)
    SurveyQuestion(
        item_id=14,
        label="QUALITAET_UEBER_PREIS",
        text="Bei Kaufentscheidungen achte ich primär auf Qualität, auch wenn das bedeutet, mehr zu zahlen.",
        block="Konsum"
    ),
    SurveyQuestion(
        item_id=15,
        label="MARKEN_IDENTITAET",
        text="Die Marken, die ich nutze, sagen etwas über meine Persönlichkeit und Werte aus.",
        block="Konsum"
    ),
    SurveyQuestion(
        item_id=16,
        label="IMPULSKONSUM",
        text="Ich kaufe gerne spontan Dinge, die mir in dem Moment Freude bereiten.",
        block="Konsum"
    ),
    SurveyQuestion(
        item_id=17,
        label="LIFESTYLE_EXPRESSION",
        text="Mein Zuhause und meine Einrichtung spiegeln bewusst meinen persönlichen Stil wider.",
        block="Konsum"
    ),
    SurveyQuestion(
        item_id=18,
        label="REGIONALITAET",
        text="Ich bevorzuge regionale und lokale Produkte gegenüber überregionalen Marken.",
        block="Konsum"
    ),
    SurveyQuestion(
        item_id=19,
        label="SECONDHAND_AKZEPTANZ",
        text="Second-Hand und Gebrauchtes zu kaufen ist für mich eine normale und positive Option.",
        block="Konsum"
    ),

    # Block 4: Soziales und Beziehungen (4 Items)
    SurveyQuestion(
        item_id=20,
        label="NETWORKING_ORIENTIERUNG",
        text="Ich pflege aktiv einen großen Bekanntenkreis und knüpfe gerne neue Kontakte.",
        block="Soziales"
    ),
    SurveyQuestion(
        item_id=21,
        label="FAMILIE_PRIORITAET",
        text="Familie hat für mich die höchste Priorität in meinem Leben.",
        block="Soziales"
    ),
    SurveyQuestion(
        item_id=22,
        label="SOZIALES_ENGAGEMENT",
        text="Ich engagiere mich regelmäßig für gesellschaftliche oder soziale Zwecke.",
        block="Soziales"
    ),
    SurveyQuestion(
        item_id=23,
        label="BEZIEHUNGSTIEFE",
        text="Ich bevorzuge wenige, aber dafür sehr enge Freundschaften.",
        block="Soziales"
    ),

    # Block 5: Kultur und Medien (3 Items)
    SurveyQuestion(
        item_id=24,
        label="HOCHKULTUR_INTERESSE",
        text="Ich interessiere mich intensiv für Kunst, Kultur und intellektuelle Auseinandersetzungen.",
        block="Kultur"
    ),
    SurveyQuestion(
        item_id=25,
        label="UNTERHALTUNGSORIENTIERUNG",
        text="Unterhaltung, Spaß und Ablenkung sind wichtige Bestandteile meines Alltags.",
        block="Kultur"
    ),
    SurveyQuestion(
        item_id=26,
        label="POLITISCHES_BEWUSSTSEIN",
        text="Ich informiere mich täglich über aktuelle politische und gesellschaftliche Entwicklungen.",
        block="Kultur"
    ),

    # Block 6: Zukunft und Veränderung (3 Items)
    SurveyQuestion(
        item_id=27,
        label="ZUKUNFTSOPTIMISMUS",
        text="Ich blicke grundsätzlich optimistisch und zuversichtlich in die Zukunft.",
        block="Zukunft"
    ),
    SurveyQuestion(
        item_id=28,
        label="WANDEL_BEJAHUNG",
        text="Gesellschaftlicher Wandel und Transformation sind grundsätzlich positiv und notwendig.",
        block="Zukunft"
    ),
    SurveyQuestion(
        item_id=29,
        label="ANPASSUNG_VS_GESTALTUNG",
        text="Ich passe mich lieber an gegebene Verhältnisse an, statt aktiv Veränderungen voranzutreiben.",
        block="Zukunft"
    ),
]


# Helper-Funktionen zum Zugriff
def get_question_by_id(item_id: int) -> SurveyQuestion:
    """Holt eine Frage anhand der Item-ID"""
    for q in QUESTIONS:
        if q.item_id == item_id:
            return q
    raise ValueError(f"Keine Frage mit item_id={item_id} gefunden")


def get_questions_by_block(block_name: str) -> List[SurveyQuestion]:
    """Holt alle Fragen eines bestimmten Blocks"""
    return [q for q in QUESTIONS if q.block == block_name]


def get_all_blocks() -> List[str]:
    """Gibt alle verfügbaren Blöcke zurück (in Reihenfolge)"""
    # Behalte Reihenfolge bei
    blocks = []
    for q in QUESTIONS:
        if q.block not in blocks:
            blocks.append(q.block)
    return blocks


# Wenn direkt ausgeführt, zeige alle Fragen
if __name__ == "__main__":
    print(f"📋 Sinus-Milieu Survey - {len(QUESTIONS)} Fragen\n")
    print(SURVEY_INSTRUCTION)
    print("\n" + "="*60 + "\n")

    for block in get_all_blocks():
        block_questions = get_questions_by_block(block)
        print(f"🔹 {block} ({len(block_questions)} Items)")
        for q in block_questions:
            print(f"  [{q.item_id:2d}] {q.label}")
            print(f"      {q.text}")
        print()
