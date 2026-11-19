# Consommation de carburant — Version française (sous-projet 2Cheval)

> **Status:** canonical · **Owns:** fuel consumption per mechanical power · **Up:** [README](README.md)

Cette page donne le débit de carburant pour une puissance mécanique donnée, à 5 % de rendement. Les propriétés de la paille sont dans [straw](../../../energy/rocket-stove/straw.md).

## Hypothèses

- Puissance mécanique : **1 ch = 735.5 W**
- Rendement global : **5 %**
- Fonctionnement continu à pleine charge
- PCI : paille **15 MJ/kg**, charbon **30 MJ/kg**, pétrole **43 MJ/kg**
- Densités : paille **100 kg/m³** (vrac) ou **250 kg/m³** (densifiée), charbon **800 kg/m³**, pétrole **850 kg/m³**

## Besoin en carburant

| Puissance | Mécanique | Thermique | Paille kg/h | Paille L/h (vrac) | Paille L/h (densifiée) | Charbon kg/h | Pétrole kg/h |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 ch | 0.74 kW | 14.7 kW | 3.53 | 35.3 | 14.1 | 1.77 | 1.23 |
| 2 ch | 1.47 kW | 29.4 kW | 7.06 | 70.6 | 28.2 | 3.53 | 2.46 |
| 3 ch | 2.21 kW | 44.1 kW | 10.59 | 105.9 | 42.4 | 5.30 | 3.70 |
| 4 ch | 2.94 kW | 58.8 kW | 14.12 | 141.2 | 56.5 | 7.06 | 4.93 |
| 6 ch | 4.41 kW | 88.3 kW | 21.18 | 211.8 | 84.7 | 10.59 | 7.39 |
| 8 ch | 5.88 kW | 117.7 kW | 28.24 | 282.4 | 113.0 | 14.12 | 9.85 |
| 12 ch | 8.83 kW | 176.5 kW | 42.36 | 423.6 | 169.5 | 21.18 | 14.78 |

La colonne « paille L/h (densifiée) » correspond à de la paille compressée ; la colonne « vrac » correspond à de la paille non densifiée.

Pour un essai de 10 min à 2 ch : 7.06 kg/h × 1/6 h ≈ **1.18 kg de paille**.

## Voir aussi
- [Dictionnaire / Glossary](../../GLOSSARY.md)

- [Straw properties](../../../energy/rocket-stove/straw.md)
- [Thermodynamics](thermodynamics.md)
- [Sizing](sizing.md)
- [Customer use case](../../../business/customers.md)
