# Matière recyclée — coût canette et aluminium

> **Status:** canonical · **Owns:** estimation de matière première recyclée · **Up:** [Business](README.md) · **Lang:** FR · [EN](../../business/recycled-material.md)

Estimation de matière pour de l'aluminium coulé à partir de canettes. Le coût canette est **configuré dans `env/`** (soft-coded) : base **0,03 €/canette** (jusqu'à **0,01 €/canette**) pour une masse médiane **14 g** (jusqu'à **8 g**), la refonte étant comptée **séparément**. C'est uniquement la matière : usinage, liant, main-d'œuvre et reste de la chaîne sont exclus.

## Hypothèses (base)

| Paramètre | Valeur |
|---|---:|
| Densité de l'aluminium compacté | **2 700 kg/m³** |
| Masse d'une canette (base / légère) | **14 g / 8 g** (`env/values/engine.json`) |
| Remplissage de la chambre | **66 %** |
| Prix de la canette (base / bas) | **0,03 € / 0,01 €** (plage de scénarios) |
| Énergie de refonte | **0,3375 kWh/kg** (four à 80 %) |
| Électricité solaire autoconsommée | **0,20 €/kWh** |
| Coût de refonte | **0,0675 €/kg** |

## Fonction et formule

Le calcul est implémenté dans [`tools/calc.py`](../../tools/calc.py) (`can_cost(...)`, `table_can(...)`) et piloté par `env/values/engine.json`.

$$m_{Al} = 0.66 \times V_c \times 2\,700\ \text{kg/m}^3$$

$$N_{cans} = \left\lceil \frac{m_{Al}}{m_{canette}} \right\rceil,\qquad C_{canettes} = N_{cans} \times p_{canette}$$

$$C_{refonte} = m_{Al} \times 0.3375\ \text{kWh/kg} \times 0.20\ \text{€/kWh},\qquad C_{matière} = C_{canettes} + C_{refonte}$$

## Matière par moteur (base)

<!-- calc:material:fr -->
| Moteur | `V_c` total | Aluminium | Canettes | **Total matière** |
|---|---:|---:|---:|---:|
| **2 ch** | 135,53 L | 241,5 kg | 17 251 | **533,83 €** |
| **6 ch** | 406,58 L | 724,5 kg | 51 752 | **1 601,47 €** |
| **20 ch** | 1 355,26 L | 2415,1 kg | 172 506 | **5 338,20 €** |
| **2 cylindres pleins (test)** | 2 × 3,534 m³ | 12 596,2 kg | 899 730 | **27 842,14 €** |
<!-- /calc:material:fr -->

Les trois premières lignes sont des moteurs **taille produit** (volume total `V_c`, remplissage 66 %). La dernière ligne est le test pessimiste **2 cylindres pleins** — un plafond, pas un coût produit.

## Scénarios de coût canette

<!-- calc:can:fr -->
| Masse canette | Prix canette | €/kg (canettes) | Canettes 2 ch | Coût canettes 2 ch | Matière 2 ch | Matière test |
|---:|---:|---:|---:|---:|---:|---:|
| 14 g/canette | 3 c/canette | 2,14 | 17 251 | 517,53 € | **533,83 €** | **27 842,14 €** |
| 14 g/canette | 2 c/canette | 1,43 | 17 251 | 345,02 € | **361,32 €** | **18 844,84 €** |
| 14 g/canette | 1 c/canette | 0,71 | 17 251 | 172,51 € | **188,81 €** | **9 847,54 €** |
| 8 g/canette | 3 c/canette | 3,75 | 30 189 | 905,67 € | **921,97 €** | **48 086,05 €** |
| 8 g/canette | 2 c/canette | 2,50 | 30 189 | 603,78 € | **620,08 €** | **32 340,78 €** |
| 8 g/canette | 1 c/canette | 1,25 | 30 189 | 301,89 € | **318,19 €** | **16 595,51 €** |
<!-- /calc:can:fr -->

## Lecture

- À la base (14 g, 3 c), la matière du moteur **2 ch** est ≈ **534 €** et le test ≈ **27 842 €**.
- Les canettes dominent le total matière ; un prix plus bas réduit directement le coût, tandis que des canettes plus légères augmentent le nombre pour une même masse d'aluminium.
- Le test reste un plafond/référence, pas un coût matière produit par moteur.
- Amortir cette charge sur quelques unités est le [scénario d'échec](../archive/scenarios/lathe-low-volume.md) : vendre ou louer la machine.

## Voir aussi

- [Coûts](costs.md) · [Équipement d'atelier](atelier/equipement.md)
- [Usinage tour](../production/usinage-tour.md)
- [Dimensionnement Manson](../engines/manson/sizing.md)
- [Glossaire](../GLOSSARY.md)
- [Configuration env](../../env/README.md)
- [Version anglaise](../../business/recycled-material.md)
