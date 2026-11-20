# Fuel consumption

> **Status:** canonical · **Owns:** fuel consumption and feed limit · **Up:** [M Reloaded](README.md) · **Lang:** EN · [FR](../../2cheval/engines/manson/fuel.md)

This page gives fuel flow for a given mechanical power at 5 % efficiency, and the **30 kg / 20 min** feed limit. Straw properties are in [straw](../../energy/rocket-stove/straw.md); the full biomass table is in [biomass calorific capacity](../../energy/rocket-stove/biomass-calorific.md).

## Assumptions

- Mechanical power: **1 ch = 735.5 W**.
- Overall efficiency: **5 %** (baseline; other tiers below).
- Continuous full-load operation.
- LHV: straw **12 MJ/kg**, charcoal **30 MJ/kg**, oil **43 MJ/kg**.
- Densities: straw **100 kg/m³** (loose) or **250 kg/m³** (densified), charcoal **800 kg/m³**, oil **850 kg/m³**.

## Fuel requirement at 5 %

<!-- calc:fuel:en -->
| Power | Mechanical | Thermal | Straw kg/h | Straw L/h (loose) | Straw L/h (densified) | Charcoal kg/h | Oil kg/h |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 ch | 0.74 kW | 14.7 kW | 4.41 | 44.1 | 17.7 | 1.77 | 1.23 |
| 2 ch | 1.47 kW | 29.4 kW | 8.83 | 88.3 | 35.3 | 3.53 | 2.46 |
| 3 ch | 2.21 kW | 44.1 kW | 13.24 | 132.4 | 53.0 | 5.30 | 3.69 |
| 4 ch | 2.94 kW | 58.8 kW | 17.65 | 176.5 | 70.6 | 7.06 | 4.93 |
| 6 ch | 4.41 kW | 88.3 kW | 26.48 | 264.8 | 105.9 | 10.59 | 7.39 |
| 8 ch | 5.88 kW | 117.7 kW | 35.30 | 353.0 | 141.2 | 14.12 | 9.85 |
| 12 ch | 8.83 kW | 176.5 kW | 52.96 | 529.6 | 211.8 | 21.18 | 14.78 |
| 20 ch | 14.71 kW | 294.2 kW | 88.26 | 882.6 | 353.0 | 35.30 | 24.63 |
<!-- /calc:fuel:en -->

For a 10 min run at 2 ch: 8.83 kg/h × 1/6 h ≈ **1.47 kg of straw**.

## Feed limit: 30 kg in 20 min

$$\dot m_{max} = \frac{30\ \text{kg}}{20\ \text{min}} = 90\ \text{kg/h}$$

At **12 MJ/kg**, the thermal limit is:

$$P_{th,max} = 90 \times \frac{12\,000}{3\,600} = 300\ \text{kW}$$

At **5 % efficiency**, the mechanical limit is:

$$P_{m,max} = 0.05 \times 300 = 15\ \text{kW} \approx 20.4\ \text{ch}$$

The **20 ch** row consumes **29.4 kg per 20 min**, exactly at the feed limit at 5 %. The 2 ch row consumes **2.94 kg per 20 min**.

## The cap depends on efficiency

<!-- calc:fuel-cap:en -->
| Efficiency | Mechanical cap | 2 ch straw (kg/h) | 20 ch straw (kg/h) |
|---:|---:|---:|---:|
| 5 % | 15 kW ≈ 20.4 ch | 8.83 kg/h | 88.3 kg/h |
| 10 % | 30 kW ≈ 40.8 ch | 4.41 kg/h | 44.1 kg/h |
| 15 % | 45 kW ≈ 61.2 ch | 2.94 kg/h | 29.4 kg/h |
| 20 % | 60 kW ≈ 81.6 ch | 2.21 kg/h | 22.1 kg/h |
<!-- /calc:fuel-cap:en -->

**15 kW is not an absolute engine limit.** It is the 5 % baseline cap. At 15 % the same feed allows 45 kW, but the chamber, materials and stove must support it. The retained power is `min(P_air, P_fuel)`; see [sizing](sizing.md#fuel-limit) and [efficiency](../../levers/efficiency.md).

The feed limit is a **stove and feeding assumption**, not a thermodynamic law: densified straw, a better auger or multiple stoves can raise it. The [insolation lever](../../levers/insolation.md) removes the fuel feed entirely when the sun is available.

## See also

- [Straw properties](../../energy/rocket-stove/straw.md)
- [Biomass calorific capacity](../../energy/rocket-stove/biomass-calorific.md)
- [Thermodynamics](thermodynamics.md)
- [Sizing](sizing.md)
- [Power from displaced air](power-from-air.md)
- [Customer use case](../../business/customers.md)
