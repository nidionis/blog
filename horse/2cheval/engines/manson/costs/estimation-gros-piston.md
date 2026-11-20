# Estimation gros piston — exemple aligné

> **Status:** worked example · **Owns:** alignement d'une estimation concurrente / grande pièce · **Up:** [Coûts matière Manson](README.md) · **Lang:** FR · [EN](../../../../engines/manson/costs/large-piston-estimate.md)

Cette page aligne une estimation externe pour un **grand composant piston** (Ø1,50 m × course 1,30 m) sur les hypothèses configurées dans l'env. Ce n'est **pas** le moteur produit de 2 ch : c'est un exemple d'échelle montrant comment matière, facteur de gaspillage, procédé et amortissement pilotent le coût. La base produit 2 ch est [135,5 L de chambre totale, ~241,5 kg d'alu coulé, ~534 € de matière (14 g / 0,03 €)](../../../business/recycled-material.md).

## 1. Géométrie et matière (recalculé)

| Élément | Valeur | Note |
|---|---:|---|
| Cylindre | `V_cyl = π × 0,75² × 1,30 = 2,297 m³` | Ø1,50 m, course 1,30 m |
| Matière effective (hypothèse) | `1,15 m³` | déplaceur + chambre/bielle/roue |
| Densité aluminium | `2 700 kg/m³` | [glossaire](../../../GLOSSARY.md) |
| Masse effective | `1,15 × 2 700 = 3 105 kg` |  |
| Prix canette (base / bas) | `0,03 € / 0,01 €` | configuré dans env |
| Masse canette (base / légère) | `14 g / 8 g` | configuré dans env |
| Refonte | `0,3375 kWh/kg × 0,20 €/kWh = 0,0675 €/kg` | four 80 %, solaire autoconsommé |

| Base matière | Canettes | Coût canettes | Refonte | **Matière parfaite** |
|---|---:|---:|---:|---:|
| 14 g, 0,03 € (base) | 221 786 | 6 654 € | 210 € | **6 863 €** |
| 14 g, 0,01 € | 221 786 | 2 218 € | 210 € | **2 427 €** |
| 8 g, 0,03 € | 388 125 | 11 644 € | 210 € | **11 853 €** |

La « matière parfaite » suppose la masse effective sans surcoulée, sans rebut et sans réessai. Les fabrications réelles paient un **facteur de gaspillage/itération**.

## 2. Facteur de gaspillage et scénarios

Le facteur de gaspillage regroupe rendement de coulée, surcoulée, défauts, pertes à la refonte et réessais. C'est le principal levier de [valorisation](../../../business/valorisation-investissement.md).

| Scénario | Facteur sur matière parfaite | Équivalent matière (14 g, 0,03 €) | Procédé fonte/moulage | **Coût unitaire indicatif** |
|---|---:|---:|---:|---:|
| Série optimiste | ×2 | ~13 730 € | ~2 500–4 000 € | **~16 000–18 000 €** |
| Réaliste | ×3 | ~20 590 € | ~2 500–4 000 € | **~23 000–25 000 €** |
| Prototype isolé pessimiste | ×4 | ~27 450 € | ~2 500–4 000 € | **~30 000–32 000 €** |

## 3. Investissement atelier (chemin scalable)

| Équipement | Coût | Rôle de valorisation |
|---|---:|---|
| Rails + moteurs (CNC DIY) | 2 000–4 000 € | mise en forme reproductible |
| Projet buse extrusion PLA→alu | 1 000–3 000 € | option procédé, actif R&D |
| Porte-outil couple élevé | 1 000–2 500 € | capacité d'usinage |
| Tour + impression rotative (slicer radial) | 2 000–5 000 € | finition et vitesse d'itération |
| **Total (chemin DIY indicatif)** | **6 000–10 000 €** | amortissable sur série |

Voir [équipement d'atelier](../../../business/atelier/equipement.md) pour les fourchettes indicatives. Acheter une machine lourde pour quelques unités est le [scénario d'échec](../../../archive/scenarios/lathe-low-volume.md).

## 4. Prototypage PLA + sable

- Motif PLA pour une grande pièce : ordre de **~5 000 €** de filament à cette échelle (moins si recyclé).
- Moule sable + usinage partenaire : typiquement **2 000–5 000 € par itération** selon l'accès labo/fonderie.
- Valeur : valider la géométrie avant une coulée métal risquée — une forme directe de [valorisation](../../../business/valorisation-investissement.md).

## 5. Alignement avec les bases du projet

| Référence | Échelle | Signal matière / coût | Usage |
|---|---|---|---|
| Moteur produit 2 ch | `V_c` 135,5 L, 241,5 kg Al | ~534 € matière (base) ; série **19 999 €** | produit marché canonique |
| Moteur 20 ch (limite 5 %) | `V_c` 1 355 L, 2 415 kg Al | ~5 338 € matière (base) | extrême à la limite d'alimentation |
| Cet exemple | 1,15 m³ effectif, 3 105 kg | ~6,9 k€ matière parfaite (base) ; ~16–32 k€ selon scénario | grande pièce / démonstrateur de coûts |
| Test 2 cylindres pleins | 12 596 kg Al | ~27 842 € matière plafond (base) | plafond matière / référence |

Pour le moteur 2 ch, le projet garde sa base documentée : **prototype 15 000 €** (prévoir **30 000 €** sur commande pour bielle et support) et **prix de série 19 999 €**. Voir [coûts](../../../business/costs.md) et [matière recyclée](../../../business/recycled-material.md).

## Voir aussi

- [Valorisation de l'investissement](../../../business/valorisation-investissement.md)
- [Matière recyclée / scénarios canette](../../../business/recycled-material.md)
- [Équipement d'atelier](../../../business/atelier/equipement.md)
- [Premier prototype](../../../production/prototype.md)
- [Usinage tour](../../../production/usinage-tour.md)
- [Version anglaise](../../../../engines/manson/costs/large-piston-estimate.md)
