# Fuel consumption

> **Status:** canonical · **Owns:** fuel consumption per mechanical power · **Up:** [M Reloaded](README.md)

This page gives fuel flow for a given mechanical power at 5 % efficiency. Straw properties are in [straw](../../energy/rocket-stove/straw.md).

## Assumptions

- Mechanical power: **1 ch = 735.5 W**
- Overall efficiency: **5 %**
- Continuous full-load operation
- LHV: straw **15 MJ/kg**, charcoal **30 MJ/kg**, oil **43 MJ/kg**
- Densities: straw **100 kg/m³** (loose) or **250 kg/m³** (densified), charcoal **800 kg/m³**, oil **850 kg/m³**

## Fuel requirement

| Power | Mechanical | Thermal | Straw kg/h | Straw L/h (loose) | Straw L/h (densified) | Charcoal kg/h | Oil kg/h |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 ch | 0.74 kW | 14.7 kW | 3.53 | 35.3 | 14.1 | 1.77 | 1.23 |
| 2 ch | 1.47 kW | 29.4 kW | 7.06 | 70.6 | 28.2 | 3.53 | 2.46 |
| 3 ch | 2.21 kW | 44.1 kW | 10.59 | 105.9 | 42.4 | 5.30 | 3.70 |
| 4 ch | 2.94 kW | 58.8 kW | 14.12 | 141.2 | 56.5 | 7.06 | 4.93 |
| 6 ch | 4.41 kW | 88.3 kW | 21.18 | 211.8 | 84.7 | 10.59 | 7.39 |
| 8 ch | 5.88 kW | 117.7 kW | 28.24 | 282.4 | 113.0 | 14.12 | 9.85 |
| 12 ch | 8.83 kW | 176.5 kW | 42.36 | 423.6 | 169.5 | 21.18 | 14.78 |

The "densified" column is compressed straw; the "loose" column is uncompressed straw.

For a 10 min run at 2 ch: 7.06 kg/h × 1/6 h ≈ **1.18 kg of straw**.

## See also

- [Straw properties](../../energy/rocket-stove/straw.md)
- [Thermodynamics](thermodynamics.md)
- [Sizing](sizing.md)
- [Customer use case](../../business/customers.md)
