# Coûts — synthèse commerciale

> **Status:** canonical roll-up · **Owns:** synthèse des coûts · **Up:** [Business](README.md) · **Lang:** FR · [EN](../../business/costs.md)

Montants **pessimistes en euros**, à la base 5 %. Le coût évolue avec l'échelle, le rendement de coulée et les itérations : voir [valorisation de l'investissement](valorisation-investissement.md). Cette page est la synthèse ; les dérivations sont liées.

## 1. Atelier et équipement

- **Prototype d'entrée** (prototype + engrenage) : **25 000 €**.
- **Atelier complet** (toutes lignes) : **~253 000–285 000 €** (BOM) · **~307 000 €** tout compris — pas le prix d'un moteur.
- **Tour 2 m** (série) : ≈ **600 000 €**, 3 ans → **200 000 €/an**. Quelques unités par tour = [scénario d'échec](../archive/scenarios/lathe-low-volume.md).

## 2. Premier prototype et facteur de gaspillage

Le premier moteur est un **réessai non optimisé**. Le coût vient surtout des itérations et du rebut (surcoulée, défauts, reprises), pas de la matière parfaite. L'[estimation gros piston](../engines/manson/costs/estimation-gros-piston.md) montre le mécanisme : un cas parfait ×1 peut devenir ×3–4 en prototype isolé, puis baisser avec l'apprentissage.

| Poste | Valeur | Note |
|---|---:|---|
| **Assurance premier prototypage** | **15 000–30 000 €** | matière, procédé, finition, risque d'itération |
| Plafond matière (2 cylindres pleins, 66 %) | 28 842 € | 933 053 canettes + refonte ; test, pas matière produit |
| Matière produit 2 ch (`V_c` total) | 553 € | 241,5 kg, 17 890 canettes + refonte |

Route : **impression PLA (1,5 m³) → moule sable (10 m³) → coulée (creuset ~3 m³) → finition tour (~1,40 m)**. Chaque itération est [valorisée](valorisation-investissement.md). Détail : [premier prototype](../production/prototype.md), [matière recyclée](recycled-material.md).

## 3. Moteur de série

Tour amorti sur des milliers de moteurs. Détail : [page anglaise](../../business/costs.md#3-series-engine), [usinage tour](../production/usinage-tour.md).

| | 1 000/an | 3 000/an | 5 000/an |
|---|---:|---:|---:|
| **Coût de production** | **16 953 €** | **16 820 €** | **16 793 €** |
| Prix de vente | 19 999 € | 19 999 € | 19 999 € |
| **Marge brute** | **3 046 €** | **3 179 €** | **3 206 €** |

Marge ≈ **2 000 €** salaire (1 vente/mois) + ~**1 050 €** réserve (transport, garantie, administration). Plancher « coût + 2 000 € » ≈ 18 953 € à 1 000/an.

## 4. Remplacement (positionnement de prix)

| Objet remplacé | Coût typique | Note |
|---|---:|---|
| PAC air-eau 15–30 kW | 15 000–35 000 € | chaleur seule, COP 2–4 |
| Tracteur compact 20–40 ch | 25 000–60 000 € | travail mécanique |
| **Moteur 2Cheval** | **19 999 €** | ~1,5 kW mécanique + ~29 kW thermique à 5 % |

5 % de rendement mécanique n'est pas un COP de PAC : positionnement de prix (chaleur + arbre), pas équivalence thermodynamique. Voir [résilience](resilience.md).

## Voir aussi

- [Valorisation de l'investissement](valorisation-investissement.md)
- [Premier prototype](../production/prototype.md) · [Estimation gros piston](../engines/manson/costs/estimation-gros-piston.md)
- [Matière recyclée](recycled-material.md) · [Usinage tour](../production/usinage-tour.md)
- [Scénario d'échec : faible volume tour](../archive/scenarios/lathe-low-volume.md)
- [Glossaire](../GLOSSARY.md) · [Version anglaise](../../business/costs.md)
