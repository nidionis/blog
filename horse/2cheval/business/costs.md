# Coûts, production et ventes par priorité — 2Cheval

> **Status:** canonical roll-up · **Owns:** cost summary · **Up:** [Business](README.md)

Tableau récapitulatif : certaines lignes sont des investissements (capex), d'autres des prototypes, d'autres des coûts de production ou des prix de vente. Le point d'entrée prototype est de 25 000 € ; l'atelier complet peut atteindre environ 307 000 €. Le moteur de série est estimé à ≈ **16 650 €** et le prix de vente retenu est **19 999 €** (voir [usinage tour](../production/usinage-tour.md)).

| Équipement / production | Envergure | Coût production | Prix de vente | Source |
|---|---|---:|---:|---|
| [Petite imprimante binder jetting](https://www.iro3d.com/) | capex | 30 000 | — | externe |
| [Imprimante binder jetting XL](../production/binder-jetting/cost.md) | capex (BOM) | 46 000 – 78 000 | — | BOM détaillé ; ~100 000 tout-in avec R&D |
| Imprimante PLA DIY XLarge | capex | 20 000 | 30 000 | — |
| Supplement Tour | capex | 5 000 | 35 000 | — |
| Prototype(s) | prototype | 15 000 | — | — |
| Engrenage de prototype | prototype | 10 000 | — | — |
| Extrudeur pélleteur complet (type Titan) | capex | 15 000 | — | — |
| Générateur d'azote | capex | 30 000 | — | — |
| Poste de soudage | capex | 2 000 | — | — |
| Rouleuse de tôles | capex | 50 000 | — | — |
| Déchiqueteur aluminium (recyclage) | capex | 30 000 | — | — |
| **Prototype d'entrée (prototype + engrenage)** | prototype | **25 000** | — | somme des deux lignes prototypes |
| **Atelier complet (si toutes les lignes)** | capex + prototypes | **~253 000 – 285 000** (BOM) · **~307 000** (tout-in) | — | capex + lignes prototypes ; ligne prototype d'entrée est un sous-total |
| [Tour métaux 2 m](../production/machining-cost.md) | capex | 600 000 | — | achat, durée de vie 3 ans |
| [Amortissement tour (1 an)](../production/machining-cost.md) | capex | 200 000 | — | €600 000 / 3 ans |
| [Premier moteur — tour chargé à 100 %](../production/machining-cost.md) | prototype | 215 250 | — | hors piston ; avec piston ≈ 216 450 |
| [Usure 2 chambres](../production/usinage-tour.md) | production | 3 000 | — | par moteur (majorant) |
| [Refonte/impression 2 cylindres d=1,5 m](../production/usinage-tour.md) | production | 12 000 | — | par moteur (majorant) |
| [Brut aluminium 2 cylindres (66 %, 2 cents/kg)](../production/usinage-tour.md) | production | 252 | — | par moteur |
| [Piston + bielle + cylindre](../production/usinage-tour.md) | production | 1 200 | — | 3 roulements haut de gamme |
| [Coût de production par moteur (1 000/an)](../production/usinage-tour.md) | production | 16 652 | — | tour réparti sur 1 000 moteurs |
| [tour a metaux — estimations cout / recettes — Usinage tour](../production/usinage-tour.md) | vente | — | 19 999 | marge ≈ 3 347, dont 2 000 salaire |

Voir aussi : [Coefficients de lecture](#comment-lire) — Comment lire cette page (FR, méthode).

## Comment lire (FR)

- Le « à partir de 25 000 € » du README du business est le **prototype d'entrée** : 15 000 € de prototype + 10 000 € d'engrenage.
- Le chiffre d'environ 307 000 € est la **liste complète d'équipement**, pas le prix du premier moteur.
- Le BOM XXL est de 46 000 – 78 000 € ; le chiffre de 100 000 € inclut la R&D et l'intégration. Voir [details](../production/binder-jetting/cost.md).
- Les coûts de matière pour un moteur massif sont dans [matière recyclée](recycled-material.md).
- Les lignes « Usure 2 chambres », « Refonte/impression », « Brut aluminium », « Piston + bielle + cylindre » et « Coût de production par moteur » sont des **coûts par moteur**, pas des équipements de l'atelier.
- « Premier moteur — tour chargé à 100 % » est un coût de **prototype** (tout le tour sur un seul moteur), pas le coût de série.

## Voir aussi

- [Dictionnaire / Glossary](../GLOSSARY.md)
