# Coûts — synthèse commerciale

> **Status:** canonical roll-up · **Owns:** synthèse des coûts · **Up:** [Business](README.md) · **Lang:** FR · [EN](../../business/costs.md)

Montants **pessimistes en euros**, à la base 5 %. Le coût évolue avec l'échelle, le rendement de coulée et les itérations : voir [valorisation de l'investissement](valorisation-investissement.md). Cette page est la synthèse ; les dérivations sont liées.

## 1. Atelier et équipement

Le détail des équipements, les fourchettes indicatives **DIY vs acheté** et les liens de référence sont dans le dossier [équipement d'atelier](atelier/equipement.md). La [BOM binder jetting XXL](../production/binder-jetting/cost.md) reste la référence composants.

| Périmètre | Fourchette indicative | Note |
|---|---:|---|
| Atelier / prototypage d'entrée (sélection) | ~25 000 € et plus | voir [équipement](atelier/equipement.md) ; prototypes et engrenage selon la route |
| Atelier complet (BOM, indicatif) | ~253 000–285 000 € | ~307 000 € tout compris avec intégration/R&D ; pas le prix d'un moteur |
| Tour 2 m (capex série) | ~600 000 € sur 3 ans | séparé de l'atelier ; faible volume = [scénario d'échec](../archive/scenarios/lathe-low-volume.md) |

## 2. Premier prototype et facteur de gaspillage

| Poste | Valeur | Note |
|---|---:|---|
| **Prototype** | **15 000 €** | prévoir **30 000 €** sur commande pour bielle et support |
| Engrenage prototype (si nécessaire) | 10 000 € | poste séparé ; voir [équipement](atelier/equipement.md) |
| Plafond matière (2 cylindres pleins, 66 %, référence) | ~27 842 € | 899 730 canettes + refonte aux hypothèses de base ; test, pas matière produit |
| Matière produit 2 ch (`V_c` total) | ~534 € | 241,5 kg, 17 251 canettes + refonte |

Le premier moteur est un **réessai non optimisé**. Le coût vient surtout des itérations et du rebut (surcoulée, défauts, reprises), pas de la matière parfaite. Route : **impression PLA (1,5 m³) → moule sable (10 m³) → coulée (creuset ~3 m³) → finition tour (~1,40 m)**. Détail : [premier prototype](../production/prototype.md), [matière recyclée](recycled-material.md), [scénarios de coût canette](recycled-material.md#scénarios-de-coût-canette).

## 3. Moteur de série

Tour amorti sur des milliers de moteurs. Détail : [page anglaise](../../business/costs.md#3-series-engine), [usinage tour](../production/usinage-tour.md).

| | 1 000/an | 3 000/an | 5 000/an |
|---|---:|---:|---:|
| **Coût de production** | **16 934 €** | **16 801 €** | **16 774 €** |
| Prix de vente | 19 999 € | 19 999 € | 19 999 € |
| **Marge brute** | **3 065 €** | **3 198 €** | **3 225 €** |

En comparaison, le prototype seul est à **15 000 €** (prévoir **30 000 €** sur commande pour bielle et support) ; le prix de série **19 999 €** inclut l'amortissement outillage et la marge. Marge ≈ **2 000 €** salaire (1 vente/mois) + réserve (transport, garantie, administration). Plancher « coût + 2 000 € » ≈ 18 934 € à 1 000/an.

## 4. Remplacement (positionnement de prix)

| Objet remplacé | Coût typique | Note |
|---|---:|---|
| PAC air-eau 15–30 kW | 15 000–35 000 € | chaleur seule, COP 2–4 |
| Tracteur compact 20–40 ch | 25 000–60 000 € | travail mécanique |
| **Moteur 2Cheval** | **19 999 €** | ~1,5 kW mécanique + ~29 kW thermique à 5 % |

5 % de rendement mécanique n'est pas un COP de PAC : positionnement de prix (chaleur + arbre), pas équivalence thermodynamique. Voir [résilience](resilience.md).

## Voir aussi

- [Équipement d'atelier](atelier/equipement.md)
- [Valorisation de l'investissement](valorisation-investissement.md)
- [Premier prototype](../production/prototype.md) · [Estimation gros piston](../engines/manson/costs/estimation-gros-piston.md)
- [Matière recyclée](recycled-material.md) · [Usinage tour](../production/usinage-tour.md)
- [Scénario d'échec : faible volume tour](../archive/scenarios/lathe-low-volume.md)
- [Glossaire](../GLOSSARY.md) · [Version anglaise](../../business/costs.md)
