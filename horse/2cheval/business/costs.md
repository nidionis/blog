# Coûts, production et ventes — page centrale — 2Cheval

> **Status:** canonical roll-up · **Owns:** cost summary · **Up:** [Business](README.md)

Page centrale des coûts : atelier, **premier prototype**, **moteur de série** et **coût de ce que le moteur remplace**. Tous les montants sont des estimations pessimistes en euros.

## 1. Atelier et équipement

| Équipement / production | Envergure | Coût production | Prix de vente | Source |
|---|---|---:|---:|---|
| [Petite imprimante binder jetting](https://www.iro3d.com/) | capex | 30 000 | — | externe |
| [Imprimante binder jetting XL](../production/binder-jetting/cost.md) | capex (BOM) | 46 000 – 78 000 | — | BOM détaillé ; ~100 000 tout-in avec R&D |
| Imprimante PLA DIY XLarge | capex | 20 000 | 30 000 | — |
| Supplément tour | capex | 5 000 | 35 000 | — |
| Prototype(s) | prototype | 15 000 | — | — |
| Engrenage de prototype | prototype | 10 000 | — | — |
| Extrudeur de pellets complet (type Titan) | capex | 15 000 | — | — |
| Générateur d'azote | capex | 30 000 | — | — |
| Poste de soudage | capex | 2 000 | — | — |
| Rouleuse de tôles | capex | 50 000 | — | — |
| Déchiqueteur aluminium (recyclage) | capex | 30 000 | — | — |
| **Prototype d'entrée (prototype + engrenage)** | prototype | **25 000** | — | somme des deux lignes prototypes |
| **Atelier complet (si toutes les lignes)** | capex + prototypes | **~253 000 – 285 000** (BOM) · **~307 000** (tout-in) | — | capex + lignes prototypes ; ligne prototype d'entrée est un sous-total |
| [Tour métaux 2 m](../production/machining-cost.md) — option série | capex | 600 000 | — | achat, durée de vie 3 ans |
| [Amortissement tour (1 an)](../production/machining-cost.md) — option série | capex | 200 000 | — | €600 000 / 3 ans |

Le tour 2 m est un capex de **série**, pas du premier prototype : la finition du prototype est sous-traitée (voir section 2).

## 2. Premier prototype — PLA, sable, coulée, tour

Le premier moteur n'est pas usiné dans la masse : impression PLA (1,5 m³) → moule sable (10 m³) → coulée (creuset ~3 m³, four solaire ou fonderie) → finition tour (~1,40 m). Détail : [prototype](../production/prototype.md).

| Poste | Bas | Central | Haut |
|---|---:|---:|---:|
| Impression PLA 1,5 m³ | 20 000 | 45 000 | 75 000 |
| Sable fin 10 m³ | 3 000 | 5 000 | 8 000 |
| Coulée sous-traitée | 10 000 | 20 000 | 30 000 |
| Finition tour 1,40 m | 3 000 | 10 000 | 20 000 |
| Piston + bielle + cylindre | 1 200 | 2 000 | 3 000 |
| Ingénierie + assemblage | 15 000 | 30 000 | 60 000 |
| **Total prototype sous-traité** | **52 200** | **112 000** | **196 000** |
| Four solaire + creuset 3 m³ + miroirs (capex) | 70 000 | 150 000 | 230 000 |
| **Total prototype avec four** | **122 200** | **262 000** | **426 000** |

Le four et le creuset sont réutilisables : partagés sur 10 prototypes, leur part tombe à €7 000–23 000 par prototype. Le premier prototype seul reste donc à ≈ **€52 000–196 000** ; le four est un investissement d'atelier.

## 3. Moteur de série

| Poste | 1 000 moteurs/an | 3 000 moteurs/an | 5 000 moteurs/an |
|---|---:|---:|---:|
| Part du tour (€200 000 / N) | 200 | 67 | 40 |
| Usure 2 chambres | 3 000 | 3 000 | 3 000 |
| Refonte/impression 2 cylindres | 12 000 | 12 000 | 12 000 |
| Brut aluminium (2 cylindres, 66 %) | 252 | 252 | 252 |
| Piston + bielle + cylindre | 1 200 | 1 200 | 1 200 |
| **Coût de production** | **16 652** | **16 519** | **16 492** |
| Prix de vente retenu | 19 999 | 19 999 | 19 999 |
| **Marge brute** | **3 347** | **3 480** | **3 507** |

Ancien scénario de comparaison : tour chargé à 100 % sur un seul moteur = ≈ €215 250 hors piston (voir [machining-cost](../production/machining-cost.md)). Ce n'est plus le scénario de première fabrication.

## 4. Coût de ce que le moteur remplace

| Objet remplacé | Coût typique | Note |
|---|---:|---|
| PAC air-eau 15–30 kW | 15 000 – 35 000 | chaleur seule, COP 2–4 |
| Tracteur compact 20–40 ch | 25 000 – 60 000 | travail mécanique |
| **Moteur 2Cheval** | **19 999** | ~1,5 kW mécanique + ~29 kW thermique |

Le rendement mécanique de 5 % n'est pas un COP de PAC. Une PAC déplace 2–4 kWh de chaleur par kWh d'électricité ; le moteur convertit 5 % de la chaleur de la paille en travail mécanique et restitue le reste en chaleur. La comparaison est un positionnement de prix (chaleur + arbre mécanique), pas une équivalence thermodynamique. Le tracteur de 20–40 ch fournit beaucoup plus de puissance : le moteur 2 ch se compare au prix, pas à la puissance. Voir [résilience](resilience.md).

## Comment lire

- Le « à partir de 25 000 € » du README du business est le **prototype d'entrée** : 15 000 € de prototype + 10 000 € d'engrenage, pas le prototype moteur.
- Le chiffre d'environ 307 000 € est la **liste complète d'équipement**, pas le prix du premier moteur.
- Le BOM XXL est de 46 000 – 78 000 € ; le chiffre de 100 000 € inclut la R&D et l'intégration. Voir [details](../production/binder-jetting/cost.md).
- Les coûts de matière pour un moteur massif sont dans [matière recyclée](recycled-material.md).
- Le **premier prototype moteur** (section 2) est un coût de prototypage, pas le coût de série.
- Le **moteur de série** (section 3) répartit le tour sur des milliers d'unités ; le prix de €19 999 laisse ≈ €3 350 de marge.

## Voir aussi

- [Premier prototype — PLA, sable, coulée, tour](../production/prototype.md)
- [Usinage tour — coût de série et prix de revente](../production/usinage-tour.md)
- [Coût de production : usine tour et cylindres](../production/machining-cost.md)
- [Résilience — moteur résilient à € 19 999](resilience.md)
- [Dictionnaire / Glossary](../GLOSSARY.md)
