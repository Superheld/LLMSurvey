"""
Sinus-Milieu Scoring Profiles
==============================

Vollständige Item-Gewichtungen und Erwartungswerte für alle 10 deutschen Sinus-Milieus.
Basierend auf Sinus-Institut Charakteristika und akademischer Literatur.

Made by Claude

Verwendung:
-----------
from sinus_scoring_profiles import SINUS_MILIEU_PROFILES
score = calculate_milieu_score(llm_responses, SINUS_MILIEU_PROFILES['Performer'])
"""

import numpy as np
from typing import Dict, List, Tuple

# ============================================================================
# SINUS-MILIEU PROFILE DEFINITIONS
# ============================================================================

SINUS_MILIEU_PROFILES = {
    
    'Konservativ-Etablierte': {
        'description': 'Klassisches Establishment mit Exklusivitätsanspruch, Statusbewusstsein, Verantwortungsethik',
        'population_share': 0.10,
        
        'positive_indicators': {
            # Item_ID: Weight
            1: 1.5,   # Traditionelle Werte → KERN-INDIKATOR
            2: 1.2,   # Bewährte Lösungen
            6: 1.0,   # Sicherheit > Abenteuer
            14: 1.3,  # Qualität statt Preis → Premium-Orientierung
            15: 0.8,  # Marken sagen etwas aus
            21: 1.0,  # Familie an erster Stelle
            23: 0.7,  # Kleiner Freundeskreis
            29: 0.9,  # Anpassung statt Veränderung
        },
        
        'negative_indicators': {
            # Item_ID: Negative_Weight (wird reverse-coded)
            3: -0.3,   # Erfolg & Leistung (Status durch Herkunft, nicht nur Leistung)
            7: -1.2,   # Trends früh erkennen
            9: -1.5,   # Autoritäten hinterfragen → KERN-NEGATIV
            28: -1.0,  # Wandel positiv
        },
        
        'expected_mean': 3.1,
        'expected_sd': 0.6,
        
        'extended_version_additions': {
            15: 1.5,  # Traditionen bewahren
            13: 1.2,  # Ordnung & Struktur
            10: 0.9,  # Prestige & Status
            34: 1.0,  # Ausführliche Kaufinformationen
            61: 0.8,  # Kulturelle Veranstaltungen
            40: -1.0, # Neue Technologien (negativ)
        }
    },
    
    'Postmaterielle': {
        'description': 'Souveräne Bildungselite mit intellektueller Anspruchshaltung und Umweltbewusstsein (2021 Fusion)',
        'population_share': 0.07,
        
        'positive_indicators': {
            5: 1.5,   # Nachhaltigkeit → KERN
            8: 1.3,   # Gemeinschaft & soziale Verantwortung
            9: 1.2,   # Autoritäten hinterfragen → Kritisches Denken
            24: 1.5,  # Kunst, Kultur, Intellekt → KERN
            26: 1.2,  # Täglich informieren
            18: 1.0,  # Lokale/regionale Produkte
            19: 0.9,  # Second-Hand normal
            22: 1.3,  # Engagement soziale Zwecke
        },
        
        'negative_indicators': {
            3: -0.8,   # Erfolg & Leistung → Postmaterialismus
            4: -1.0,   # Was andere denken
            15: -1.2,  # Marken sagen etwas aus → NEGATIV
            16: -1.0,  # Sofortige Freude durch Kauf
        },
        
        'expected_mean': 3.2,
        'expected_sd': 0.7,
        
        'extended_version_additions': {
            12: 1.4,  # Jeder kann Gesellschaft verändern
            14: 1.3,  # Kulturelle Vielfalt
            25: 1.2,  # Arbeit gesellschaftlicher Mehrwert
            36: 1.5,  # Fair gehandelte Waren
            39: 1.0,  # Minimalismus
            63: 1.2,  # Anspruchsvolle Bücher
            65: 1.4,  # Gesellschaftliche Themen diskutieren
            74: 1.5,  # Klimawandel Sorgen
        }
    },
    
    'Performer': {
        'description': 'Effizienzorientierte technokratische Elite mit globalem Wirtschaftsdenken',
        'population_share': 0.08,
        
        'positive_indicators': {
            3: 1.5,   # Erfolg & Leistung → KERN
            9: 1.5,   # Beruflicher Erfolg ist Identität → KERN
            10: 1.4,  # Abläufe optimieren → Effizienz
            12: 1.2,  # Selbstständig & eigenverantwortlich
            27: 1.0,  # Zukunft optimistisch
            7: 0.9,   # Trends früh erkennen
            14: 0.8,  # Qualität statt Preis
        },
        
        'negative_indicators': {
            11: -1.5,  # Work-Life-Balance wichtiger → KERN-NEGATIV
            13: -1.3,  # Harmonie wichtiger als Leistung
            23: -0.7,  # Kleiner Freundeskreis
            29: -1.0,  # Anpassung statt Veränderung
        },
        
        'expected_mean': 3.3,
        'expected_sd': 0.5,
        
        'extended_version_additions': {
            17: 1.5,  # Abläufe optimieren
            21: 1.3,  # Führungsverantwortung
            22: 1.2,  # Kreativität & Innovation
            26: 1.0,  # Flexibilität Arbeit
            27: 1.3,  # Weiterbildung
            40: 1.4,  # Neue Technologien
            46: 1.2,  # KI faszinierend
            49: 1.4,  # Digitale Tools Optimierung
            54: 1.3,  # Networking
        }
    },
    
    'Expeditive': {
        'description': 'Ambitionierte kreative urbane Professionals mit Digital-Native-Status',
        'population_share': 0.07,
        
        'positive_indicators': {
            7: 1.5,   # Trends früh erkennen → KERN
            20: 1.4,  # Großer Bekanntenkreis → Networking
            12: 1.2,  # Selbstständig & eigenverantwortlich
            14: 0.9,  # Qualität statt Preis
            27: 1.0,  # Zukunft optimistisch
            28: 1.2,  # Wandel positiv
            17: 1.0,  # Zuhause spiegelt Stil
        },
        
        'negative_indicators': {
            2: -1.3,   # Bewährte Lösungen → Experimentierfreude
            6: -1.2,   # Sicherheit > Abenteuer
            23: -1.4,  # Kleiner Freundeskreis → NEGATIV
            29: -1.5,  # Anpassung statt Veränderung → KERN-NEGATIV
        },
        
        'expected_mean': 3.0,
        'expected_sd': 0.6,
        
        'extended_version_additions': {
            14: 1.4,  # Kulturelle Vielfalt
            22: 1.3,  # Kreativität & Innovation
            24: 1.4,  # Internationale Teams
            40: 1.5,  # Neue Technologien
            41: 1.3,  # Soziale Medien aktiv
            45: 1.2,  # Eigene Inhalte erstellen
            54: 1.5,  # Networking
        }
    },
    
    'Neo-Ökologische': {
        'description': 'NEU 2021: Treiber globaler Transformation mit optimistischem Environmentalismus',
        'population_share': 0.07,
        
        'positive_indicators': {
            5: 1.5,   # Nachhaltigkeit → KERN
            8: 1.4,   # Gemeinschaft & Verantwortung
            28: 1.5,  # Wandel positiv → KERN Transformation
            27: 1.3,  # Zukunft optimistisch → Optimismus trotz Krise
            18: 1.2,  # Lokale Produkte
            19: 1.3,  # Second-Hand
            22: 1.4,  # Engagement soziale Zwecke
            7: 0.9,   # Trends erkennen (aber nicht Konsum-Trends)
        },
        
        'negative_indicators': {
            16: -1.5,  # Sofortige Freude durch Kauf → KERN-NEGATIV
            15: -1.3,  # Marken sagen etwas aus
            4: -1.0,   # Was andere denken
        },
        
        'expected_mean': 3.4,
        'expected_sd': 0.6,
        
        'extended_version_additions': {
            12: 1.5,  # Jeder kann Gesellschaft verändern
            25: 1.4,  # Arbeit Mehrwert
            36: 1.5,  # Fair gehandelt
            39: 1.4,  # Minimalismus
            46: 0.7,  # KI faszinierend (wenn ethisch)
            74: 1.5,  # Klimawandel Sorgen
            75: 1.2,  # Nächste Generation bessere Bedingungen
        }
    },
    
    'Adaptiv-Pragmatische': {
        'description': 'Moderne Mitte mit Flexibilität und pragmatischer Anpassung. DEFINIERT DURCH MODERATE WERTE!',
        'population_share': 0.09,
        
        # WICHTIG: Dieses Milieu wird NICHT durch hohe Werte identifiziert,
        # sondern durch ABWESENHEIT extremer Ausprägungen!
        
        'positive_indicators': {
            11: 1.2,  # Work-Life-Balance
            18: 0.8,  # Lokale Produkte
            27: 0.9,  # Zukunft optimistisch
            8: 0.7,   # Gemeinschaft
            17: 0.7,  # Zuhause spiegelt Werte
        },
        
        'negative_indicators': {
            # Kaum negative Indikatoren - charakterisiert durch Moderate!
        },
        
        'expected_mean': 2.9,  # NAH AM SKALENMITTEL 2.5!
        'expected_sd': 0.4,    # NIEDRIGE VARIANZ!
        
        # SPEZIAL-SCORING für dieses Milieu:
        'special_scoring': {
            'type': 'variance_based',
            'max_variance': 0.5,  # Geringe Varianz über alle Items
            'mean_range': (2.7, 3.1),  # Eng um Skalenmittel
            'extreme_response_penalty': True  # Viele "1" oder "4" = unwahrscheinlich
        },
        
        'extended_version_additions': {
            # Moderate Werte bei fast allem
        }
    },
    
    'Konsum-Hedonistische': {
        'description': 'Unterhaltungsfokussierte untere Mittelschicht mit Fun- und Konsum-Betonung',
        'population_share': 0.13,
        
        'positive_indicators': {
            16: 1.5,  # Sofortige Freude durch Kauf → KERN
            25: 1.5,  # Unterhaltung & Fun → KERN
            15: 1.2,  # Marken sagen etwas aus
            11: 1.3,  # Work-Life-Balance
            20: 1.0,  # Großer Bekanntenkreis
            4: 0.9,   # Was andere denken
        },
        
        'negative_indicators': {
            24: -1.5,  # Kunst, Kultur, Intellekt → KERN-NEGATIV
            26: -1.2,  # Täglich informieren
            5: -0.9,   # Nachhaltigkeit
            9: -1.0,   # Beruflicher Erfolg Identität
        },
        
        'expected_mean': 2.8,
        'expected_sd': 0.7,
        
        'extended_version_additions': {
            37: 1.3,  # Schnäppchen
            41: 1.4,  # Soziale Medien
            62: 1.5,  # Reality-TV
            64: 1.3,  # Streaming
            63: -1.4, # Anspruchsvolle Bücher (negativ)
            65: -1.2, # Gesellschaftliche Themen (negativ)
        }
    },
    
    'Prekäre': {
        'description': 'Untere Klasse mit Teilhabe-/Anerkennungssuche bei ökonomischen Restriktionen',
        'population_share': 0.09,
        
        'positive_indicators': {
            4: 1.5,   # Was andere denken → KERN Anerkennung
            21: 1.3,  # Familie an erster Stelle
            29: 1.2,  # Anpassung statt Veränderung
            16: 1.0,  # Sofortige Freude (kompensatorisch)
            15: 1.1,  # Marken (Status-Aspiration)
            6: 1.3,   # Sicherheit > Abenteuer
        },
        
        'negative_indicators': {
            14: -1.4,  # Qualität statt Preis → ÖKONOMISCHE RESTRIKTION
            24: -1.3,  # Kunst, Kultur → Bildungsferne
            22: -0.9,  # Engagement (weniger Ressourcen)
            27: -1.0,  # Zukunft optimistisch (Pessimismus)
        },
        
        'expected_mean': 2.6,
        'expected_sd': 0.8,
        
        'extended_version_additions': {
            37: 1.4,  # Schnäppchen
            56: 1.2,  # Konflikte vermeiden
            42: -0.8, # Datenschutz (negativ)
            27: -1.2, # Weiterbildung (negativ)
        }
    },
    
    'Nostalgisch-Bürgerliche': {
        'description': 'Harmonieorientierte Arbeiter-/Mittelschicht mit Sicherheits-/Stabilitätssuche',
        'population_share': 0.10,
        
        'positive_indicators': {
            1: 1.3,   # Traditionelle Werte
            13: 1.5,  # Harmonie wichtiger → KERN
            23: 1.4,  # Kleiner Freundeskreis → Vertrautheit
            21: 1.4,  # Familie an erster Stelle
            8: 1.2,   # Gemeinschaft
            6: 1.3,   # Sicherheit > Abenteuer
            29: 1.2,  # Anpassung
        },
        
        'negative_indicators': {
            7: -1.5,   # Trends früh erkennen → KERN-NEGATIV
            28: -1.3,  # Wandel positiv
            3: -0.9,   # Erfolg & Leistung
        },
        
        'expected_mean': 3.0,
        'expected_sd': 0.6,
        
        'extended_version_additions': {
            13: 1.3,  # Ordnung & Struktur
            15: 1.4,  # Traditionen bewahren
            56: 1.4,  # Konflikte vermeiden
            70: 1.1,  # Einschränkungen als Teil des Lebens
            40: -1.4, # Neue Technologien (negativ)
            45: -1.3, # Inhalte erstellen (negativ)
        }
    },
    
    'Traditionelle': {
        'description': 'Sicherheits-/ordnungsliebende ältere Generation mit kleinbürgerlichen Werten',
        'population_share': 0.10,
        
        'positive_indicators': {
            1: 1.5,   # Traditionelle Werte → KERN Maximum
            2: 1.5,   # Bewährte Lösungen → KERN
            6: 1.5,   # Sicherheit > Abenteuer → KERN
            29: 1.4,  # Anpassung statt Veränderung
            21: 1.3,  # Familie
            13: 1.2,  # Harmonie
            23: 1.1,  # Kleiner Freundeskreis
        },
        
        'negative_indicators': {
            7: -1.5,   # Trends → KERN-NEGATIV Anti-Modern
            9: -1.5,   # Autoritäten hinterfragen → Respekt
            28: -1.4,  # Wandel positiv
            3: -1.2,   # Erfolg & Leistung → Bescheidenheit
        },
        
        'expected_mean': 3.2,
        'expected_sd': 0.5,
        
        'extended_version_additions': {
            13: 1.5,  # Ordnung
            15: 1.5,  # Traditionen bewahren
            40: -1.5, # Neue Technologien (negativ)
            46: -1.5, # KI (negativ)
            47: -1.4, # Digitale Kommunikation (negativ)
        }
    }
}


# ============================================================================
# SCORING FUNCTIONS
# ============================================================================

def calculate_milieu_score(
    responses: Dict[int, int], 
    milieu_profile: Dict
) -> Dict[str, float]:
    """
    Berechnet Score für ein Milieu basierend auf LLM-Antworten.
    
    Args:
        responses: Dict {item_id: score} mit Werten 1-4
        milieu_profile: Milieu-Profil aus SINUS_MILIEU_PROFILES
    
    Returns:
        Dict mit raw_score, z_score, probability
    """
    
    # Positive Indicators
    positive_sum = sum(
        responses.get(item_id, 2.5) * weight 
        for item_id, weight in milieu_profile['positive_indicators'].items()
    )
    positive_weight_sum = sum(milieu_profile['positive_indicators'].values())
    
    # Negative Indicators (reverse-coded: 4→1, 3→2, 2→3, 1→4)
    negative_sum = sum(
        (5 - responses.get(item_id, 2.5)) * abs(weight)
        for item_id, weight in milieu_profile['negative_indicators'].items()
    )
    negative_weight_sum = sum(
        abs(w) for w in milieu_profile['negative_indicators'].values()
    )
    
    # Weighted Average
    total_weight = positive_weight_sum + negative_weight_sum
    raw_score = (positive_sum + negative_sum) / total_weight if total_weight > 0 else 2.5
    
    # Z-Score gegen theoretische Erwartung
    z_score = (raw_score - milieu_profile['expected_mean']) / milieu_profile['expected_sd']
    
    # Probability via Sigmoid
    probability = 1 / (1 + np.exp(-z_score))
    
    return {
        'raw_score': raw_score,
        'z_score': z_score,
        'probability': probability
    }


def calculate_all_milieu_scores(responses: Dict[int, int]) -> Dict[str, Dict]:
    """
    Berechnet Scores für alle 10 Milieus.
    
    Args:
        responses: Dict {item_id: score} mit Werten 1-4
    
    Returns:
        Dict {milieu_name: score_dict}
    """
    return {
        milieu_name: calculate_milieu_score(responses, profile)
        for milieu_name, profile in SINUS_MILIEU_PROFILES.items()
    }


def calculate_adaptiv_pragmatisch_special(responses: Dict[int, int]) -> Dict[str, float]:
    """
    Spezial-Scoring für Adaptiv-Pragmatische (varianz-basiert).
    
    Dieses Milieu ist charakterisiert durch MODERATE Werte ohne Extreme.
    """
    
    response_values = np.array(list(responses.values()))
    
    # Varianz über alle Antworten
    variance = np.var(response_values)
    
    # Mean Deviation vom Skalenmittel 2.5
    mean_response = np.mean(response_values)
    mean_deviation = abs(mean_response - 2.5)
    
    # Anteil extremer Antworten (1 oder 4)
    extreme_count = np.sum((response_values == 1) | (response_values == 4))
    extreme_proportion = extreme_count / len(response_values)
    
    # Score steigt bei:
    # - Niedriger Varianz (< 0.5)
    # - Mean nah an 2.5 (< 0.4 Abweichung)
    # - Wenig Extreme (< 20%)
    
    variance_score = max(0, 1 - (variance / 0.5))  # Optimal: variance=0, Score=1
    mean_score = max(0, 1 - (mean_deviation / 0.4))  # Optimal: mean=2.5, Score=1
    extreme_score = max(0, 1 - (extreme_proportion / 0.2))  # Optimal: 0% Extreme, Score=1
    
    # Gewichteter Durchschnitt
    raw_score = (variance_score * 0.4 + mean_score * 0.4 + extreme_score * 0.2)
    
    # Z-Score (gegen expected_mean=2.9)
    z_score = (mean_response - 2.9) / 0.4
    
    # Kombinierter Score
    probability = 0.6 * raw_score + 0.4 * (1 / (1 + np.exp(-z_score)))
    
    return {
        'raw_score': mean_response,
        'z_score': z_score,
        'probability': probability,
        'variance': variance,
        'extreme_proportion': extreme_proportion,
        'special_scoring': True
    }


def get_primary_milieu(
    all_scores: Dict[str, Dict], 
    confidence_threshold: float = 0.15
) -> Dict:
    """
    Bestimmt primäres (und ggf. sekundäres) Milieu mit Confidence-Level.
    
    Args:
        all_scores: Output von calculate_all_milieu_scores()
        confidence_threshold: Minimaler Gap für "high confidence"
    
    Returns:
        Dict mit primary_milieu, confidence, ggf. secondary_milieu
    """
    
    # Sortieren nach Probability
    sorted_milieus = sorted(
        all_scores.items(), 
        key=lambda x: x[1]['probability'], 
        reverse=True
    )
    
    primary = sorted_milieus[0]
    secondary = sorted_milieus[1]
    
    confidence_gap = primary[1]['probability'] - secondary[1]['probability']
    
    if confidence_gap > confidence_threshold:
        return {
            'type': 'clear_case',
            'primary_milieu': primary[0],
            'primary_probability': primary[1]['probability'],
            'primary_raw_score': primary[1]['raw_score'],
            'confidence': 'high',
            'confidence_gap': confidence_gap
        }
    elif confidence_gap > 0.08:
        return {
            'type': 'moderate_case',
            'primary_milieu': primary[0],
            'primary_probability': primary[1]['probability'],
            'secondary_milieu': secondary[0],
            'secondary_probability': secondary[1]['probability'],
            'confidence': 'moderate',
            'confidence_gap': confidence_gap
        }
    else:
        return {
            'type': 'boundary_case',
            'candidates': [primary[0], secondary[0]],
            'probabilities': [primary[1]['probability'], secondary[1]['probability']],
            'confidence': 'low',
            'confidence_gap': confidence_gap,
            'note': 'Manual expert review recommended'
        }


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    
    # Beispiel LLM-Antworten (29 Items)
    example_responses = {
        1: 3,   # Traditionelle Werte → eher zu
        2: 2,   # Bewährte Lösungen → eher nicht zu
        3: 4,   # Erfolg & Leistung → voll zu
        4: 2,   # Was andere denken → eher nicht zu
        5: 3,   # Nachhaltigkeit → eher zu
        6: 2,   # Sicherheit > Abenteuer → eher nicht zu
        7: 4,   # Trends früh erkennen → voll zu
        8: 3,   # Gemeinschaft → eher zu
        9: 4,   # Beruflicher Erfolg Identität → voll zu
        10: 4,  # Abläufe optimieren → voll zu
        11: 2,  # Work-Life-Balance wichtiger → eher nicht zu
        12: 4,  # Selbstständig → voll zu
        13: 2,  # Harmonie wichtiger → eher nicht zu
        14: 3,  # Qualität statt Preis → eher zu
        15: 2,  # Marken → eher nicht zu
        16: 2,  # Sofortige Freude → eher nicht zu
        17: 3,  # Zuhause spiegelt Werte → eher zu
        18: 3,  # Lokale Produkte → eher zu
        19: 2,  # Second-Hand → eher nicht zu
        20: 3,  # Großer Bekanntenkreis → eher zu
        21: 3,  # Familie an erster Stelle → eher zu
        22: 3,  # Engagement soziale Zwecke → eher zu
        23: 2,  # Kleiner Freundeskreis → eher nicht zu
        24: 3,  # Kunst, Kultur → eher zu
        25: 3,  # Unterhaltung & Fun → eher zu
        26: 3,  # Täglich informieren → eher zu
        27: 4,  # Zukunft optimistisch → voll zu
        28: 3,  # Wandel positiv → eher zu
        29: 2,  # Anpassung statt Veränderung → eher nicht zu
    }
    
    # Alle Milieus berechnen
    all_scores = calculate_all_milieu_scores(example_responses)
    
    # Spezial-Scoring für Adaptiv-Pragmatisch
    all_scores['Adaptiv-Pragmatische'] = calculate_adaptiv_pragmatisch_special(example_responses)
    
    # Primary Milieu bestimmen
    result = get_primary_milieu(all_scores)
    
    print("=" * 60)
    print("SINUS-MILIEU CLASSIFICATION RESULT")
    print("=" * 60)
    print(f"\nPrimary Milieu: {result['primary_milieu']}")
    print(f"Probability: {result['primary_probability']:.3f}")
    print(f"Confidence: {result['confidence']}")
    
    if 'secondary_milieu' in result:
        print(f"\nSecondary Milieu: {result['secondary_milieu']}")
        print(f"Probability: {result['secondary_probability']:.3f}")
    
    print("\n" + "=" * 60)
    print("ALL MILIEU SCORES (sorted by probability)")
    print("=" * 60)
    
    sorted_scores = sorted(
        all_scores.items(), 
        key=lambda x: x[1]['probability'], 
        reverse=True
    )
    
    for milieu_name, scores in sorted_scores:
        print(f"\n{milieu_name}:")
        print(f"  Probability: {scores['probability']:.3f}")
        print(f"  Raw Score: {scores['raw_score']:.3f}")
        print(f"  Z-Score: {scores['z_score']:.3f}")
        if scores.get('special_scoring'):
            print(f"  Variance: {scores['variance']:.3f}")
            print(f"  Extreme Proportion: {scores['extreme_proportion']:.1%}")