# Consommation de carburant / Fuel consumption

> **Status:** canonical · **Owns:** fuel consumption per mechanical power · **Up:** [Manson](README.md)

**FR** — Cette page donne le débit de carburant pour une puissance mécanique donnée, à 5 % de rendement. Les propriétés de la paille sont dans [straw](../../energy/rocket-stove/straw.md).  
**EN** — This page gives fuel flow for a given mechanical power at 5 % efficiency. Straw properties are in [straw](../../energy/rocket-stove/straw.md).

## Hypothèses / Assumptions

- Puissance mécanique / mechanical power : **1 ch = 735.5 W**
- Rendement global / overall efficiency : **5 %**
- Fonctionnement continu à pleine charge / continuous full-load operation
- PCI / LHV : paille **15 MJ/kg**, charbon **30 MJ/kg**, pétrole **43 MJ/kg**
- Densités / densities : paille **100 kg/m³** (vrac / loose) ou **250 kg/m³** (densifiée / densified), charbon **800 kg/m³**, pétrole **850 kg/m³**

## Besoin en carburant / Fuel requirement

| Puissance / Power | Mécanique / Mechanical | Thermique / Thermal | Paille kg/h / Straw | Paille L/h (vrac) / loose | Paille L/h (densifiée) / densified | Charbon kg/h / Charcoal | Pétrole kg/h / Oil |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 ch | 0.74 kW | 14.7 kW | 3.53 | 35.3 | 14.1 | 1.77 | 1.23 |
| 2 ch | 1.47 kW | 29.4 kW | 7.06 | 70.6 | 28.2 | 3.53 | 2.46 |
| 3 ch | 2.21 kW | 44.1 kW | 10.59 | 105.9 | 42.4 | 5.30 | 3.70 |
| 4 ch | 2.94 kW | 58.8 kW | 14.12 | 141.2 | 56.5 | 7.06 | 4.93 |
| 6 ch | 4.41 kW | 88.3 kW | 21.18 | 211.8 | 84.7 | 10.59 | 7.39 |
| 8 ch | 5.88 kW | 117.7 kW | 28.24 | 282.4 | 113.0 | 14.12 | 9.85 |
| 12 ch | 8.83 kW | 176.5 kW | 42.36 | 423.6 | 169.5 | 21.18 | 14.78 |

La colonne « paille L/h (densifiée) » correspond à de la paille compressée ; la colonne « vrac » correspond à de la paille non densifiée.  
The “densified” column is compressed straw; the “loose” column is uncompressed straw.

Pour un essai de 10 min à 2 ch / For a 10 min run at 2 ch : 7.06 kg/h × 1/6 h ≈ **1.18 kg de paille / straw**.

## Voir aussi / See also

- [Straw properties / Propriétés de la paille](../../energy/rocket-stove/straw.md)
- [Thermodynamics / Thermodynamique](thermodynamics.md)
- [Sizing / Dimensionnement](sizing.md)
- [Customer use case / Cas client](../../business/customers.md)
