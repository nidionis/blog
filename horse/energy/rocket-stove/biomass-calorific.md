# Biomass calorific capacity

> **Status:** reference · **Owns:** biomass LHV/PCS values · **Up:** [Rocket stove](README.md) · **Lang:** EN · [FR](../../2cheval/energy/rocket-stove/biomass-calorific.md)

Calorific values vary with fuel type and moisture. This page records the reference table and the value used for the engine sizing.

## Lower heating value (LHV) — dry basis

| Biomass | LHV (kWh/kg) | LHV (MJ/kg) |
|---|---:|---:|
| Wood (hardwood) | 4.0 – 4.4 | 14.5 – 16 |
| Wood (softwood) | 4.2 – 4.6 | 15 – 16.5 |
| Cereals (straw) | 3.5 – 4.0 | **12.5 – 14.5** |
| Miscanthus | 3.8 – 4.2 | 13.5 – 15 |
| Nuts / shells | 4.0 – 4.5 | 14.5 – 16 |
| Wood pellets | 4.6 – 5.0 | 16.5 – 18 |
| Biogas (pure methane) | ~10 | ~36 |

## Moisture impact

Moisture is the most critical factor:

- **Dry wood** (< 20 % moisture): LHV ≈ 4.0–4.4 kWh/kg.
- **Fresh wood** (~50 % moisture): LHV ≈ 1.5–2.0 kWh/kg.
- Each additional 10 % moisture reduces LHV by about 0.4–0.5 kWh/kg, because part of the heat evaporates water.

## Practical rule

For ordinary firewood (~20 % moisture):

> **1 stere of wood ≈ 1,500–2,000 kWh** (depending on species).

## Higher heating value (HHV)

HHV is about 7–10 % higher than LHV because it includes the latent heat of water vapour. Conventional boilers use LHV; condensing boilers can use HHV.

## Project baseline

The engine sizing uses **12 MJ/kg**, deliberately below the table's straw range. This is pessimistic:

- Straw table range: 12.5–14.5 MJ/kg.
- Retained baseline: **12 MJ/kg** (below the low end).
- The previous 15 MJ/kg value was optimistic; all fuel flows are recalculated with 12 MJ/kg.

At 5 % efficiency, 12 MJ/kg and a 30 kg / 20 min feed limit, the thermal input is 300 kW and the mechanical limit is 15 kW ≈ 20.4 hp. At 15 % the same feed allows 45 kW. See [fuel consumption](../../engines/manson/fuel.md), [sizing](../../engines/manson/sizing.md) and [efficiency](../../levers/efficiency.md).

## See also

- [Straw properties](straw.md)
- [Fuel consumption](../../engines/manson/fuel.md)
- [Sizing](../../engines/manson/sizing.md)
- [Thermodynamics](../../engines/manson/thermodynamics.md)
- [Combustion](combustion.md)
- [Rocket stove](README.md)
