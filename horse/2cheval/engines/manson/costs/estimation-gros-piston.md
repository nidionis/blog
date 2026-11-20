# Estimation gros piston — exemple aligné

> **Status:** worked example · **Owns:** alignement d'une estimation concurrente / grande pièce · **Up:** [Coûts matière Manson](README.md) · **Lang:** FR · [EN](../../../../engines/manson/costs/large-piston-estimate.md)

Cette page aligne une estimation externe pour un **grand composant piston** (Ø1,50 m × course 1,30 m) sur les hypothèses durcies du projet. Ce n'est **pas** le moteur produit de 2 ch : c'est un exemple d'échelle qui montre comment matière, facteur de gaspillage, procédé et amortissement pilotent le coût. La base produit 2 ch est [135,5 L de chambre totale, ~242 kg d'alu coulé, ~553 € de matière](../../../business/recycled-material.md).

## 1. Géométrie et matière (recalculé)

| Élément | Valeur | Note |
|---|---:|---|
| Cylindre | `V_cyl = π × 0,75² × 1,30 = 2,297 m³` | Ø1,50 m, course 1,30 m |
| Matière effective (hypothèse) | `1,15 m³` | déplaceur + chambre/bielle/roue |
| Densité aluminium | `2 700 kg/m³` | [glossaire](../../../GLOSSARY.md) |
| Masse effective | `1,15 × 2 700 = 3 105 kg` |  |
| Prix canette | `0,03 €/canette` | hypothèse durcie du projet |
| Masse canette | `13,5 g` base (`15 g` variante) | `2,22 €/kg` à 13,5 g, `2,00 €/kg` à 15 g |
| Refonte | `0,3375 kWh/kg × 0,20 €/kWh = 0,0675 €/kg` | four 80 %, solaire autoconsommé |

| Base matière | Canettes | Refonte | **Matière parfaite** |
|---|---:|---:|---:|
| Canettes 13,5 g (base projet) | 6 900 € | 210 € | **7 110 €** |
| Canettes 15 g (variante) | 6 210 € | 210 € | **6 420 €** |

La « matière parfaite » suppose la masse effective sans surcoulée, sans rebut et sans réessai. Les fabrications réelles paient un **facteur de gaspillage/itération**.

## 2. Facteur de gaspillage et scénarios

Le facteur de gaspillage regroupe rendement de coulée, surcoulée, défauts, pertes à la refonte et réessais. C'est le principal levier de [valorisation](../../../business/valorisation-investissement.md) : l'itération le réduit.

| Scénario | Facteur sur matière parfaite | Équivalent matière (base 13,5 g) | Procédé fonte/moulage | **Coût unitaire indicatif** |
|---|---:|---:|---:|---:|
| Série optimiste | ×2 | ~14 220 € | ~2 500–4 000 € | **~15 000–18 000 €** |
| Réaliste | ×3 | ~21 330 € | ~2 500–4 000 € | **~24 000–25 000 €** |
| Prototype isolé pessimiste | ×4 | ~28 440 € | ~2 500–4 000 € | **~31 000–33 000 €** |

Le procédé fonte/moulage couvre ici four/amortissement, énergie, moule sable, main-d'œuvre et manutention pour une pièce de cette taille (ordre de 2,5–4 k€ par itération en faible capex). Une route industrielle plus lourde change la répartition, pas le besoin d'amortir.

## 3. Investissement atelier (chemin scalable)

| Équipement | Coût | Rôle de valorisation |
|---|---:|---|
| Rails + moteurs (CNC DIY) | 2 000–4 000 € | mise en forme reproductible |
| Projet buse extrusion PLA→alu | 1 000–3 000 € | option procédé, actif R&D |
| Porte-outil couple élevé | 1 000–2 500 € | capacité d'usinage |
| Tour + impression rotative (slicer radial) | 2 000–5 000 € | finition et vitesse d'itération |
| **Total (chemin DIY indicatif)** | **6 000–10 000 €** | amortissable sur série |

C'est un **chemin de valorisation à faible capex**, différent de l'hypothèse tour de série à 600 k€. Acheter une machine lourde pour quelques unités est le [scénario d'échec](../../../archive/scenarios/lathe-low-volume.md) ; louer, partager ou vendre la machine préserve la valeur.

## 4. Prototypage PLA + sable

- Motif PLA pour une grande pièce : ordre de **~5 000 €** de filament à cette échelle (moins si recyclé).
- Moule sable + usinage partenaire : typiquement **2 000–5 000 € par itération** selon l'accès labo/fonderie.
- Valeur : valider la géométrie avant une coulée métal risquée — une forme directe de [valorisation](../../../business/valorisation-investissement.md).

## 5. Alignement avec les bases du projet

| Référence | Échelle | Signal matière / coût | Usage |
|---|---|---|---|
| Moteur produit 2 ch | `V_c` 135,5 L, 241,5 kg Al | ~553 € matière ; série **19 999 €** | produit marché canonique |
| Moteur 20 ch (limite 5 %) | `V_c` 1 355 L, 2 415 kg Al | ~5 530 € matière | extrême à la limite d'alimentation |
| Cet exemple | 1,15 m³ effectif, 3 105 kg | ~7,1 k€ matière parfaite ; ~15–33 k€ selon scénario | grande pièce / démonstrateur de coûts |
| Test 2 cylindres pleins | 12 596 kg Al | ~28 842 € matière plafond | assurance premier moteur **15–30 k€** |

L'exemple soutient un **premier prix de revente ~30 000–40 000 €** pour une grande pièce précoce et faible volume avec marge (≈20–30 % sur un build réaliste), et **~15 000–20 000 €** en série si le gaspillage et l'amortissement sont valorisés. Pour le moteur 2 ch, le projet garde sa base documentée : **assurance premier moteur 15–30 k€** et **prix de série 19 999 €**. Voir [coûts](../../../business/costs.md).

## Voir aussi

- [Valorisation de l'investissement](../../../business/valorisation-investissement.md)
- [Matière recyclée](../../../business/recycled-material.md)
- [Premier prototype](../../../production/prototype.md)
- [Usinage tour](../../../production/usinage-tour.md)
- [Version anglaise](../../../../engines/manson/costs/large-piston-estimate.md)
