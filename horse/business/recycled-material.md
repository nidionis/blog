# Recycled material — can cost and aluminium

> **Status:** canonical · **Owns:** recycled-aluminium raw-material estimate · **Up:** [Business](README.md) · **Lang:** EN · [FR](../2cheval/business/recycled-material.md)

Raw-material estimate for cast aluminium made from used cans. The can costing is **env-configured** (soft-coded): baseline **€0.03/can** (down to **€0.01/can**) for a median can mass **14 g** (down to **8 g**), with remelting charged separately. This is material only: machining, binder, labour and the rest of the production chain are excluded.

## 1. Assumptions (baseline)

| Parameter | Value | Note |
|---|---:|---|
| Compacted aluminium density | **2,700 kg/m³** | solid-equivalent |
| Can mass (baseline / light) | **14 g / 8 g** | env-configured (`env/values/engine.json`) |
| Chamber fill | **66 %** | pessimistic casting yield |
| Can price (baseline / low) | **€0.03 / €0.01 per can** | env-configured scenario range |
| Melting energy, theoretical | **0.27 kWh/kg** | heating + latent heat |
| Furnace efficiency | **80 %** | melting only |
| Remelting energy | **0.3375 kWh/kg** | 0.27 / 0.80 |
| Self-consumed solar electricity | **€0.20/kWh** | project assumption |
| Remelting cost | **€0.0675/kg** | 0.3375 × 0.20 |

The theoretical melting energy is `0.9 kJ/(kg·K) × 640 K + 397 kJ/kg ≈ 973 kJ/kg ≈ 0.27 kWh/kg` (aluminium heated from 20 °C to 660 °C, then melted).

## 2. Function and formula

Cost calculation is implemented in [`tools/calc.py`](../tools/calc.py) (`can_cost(...)`, `table_can(...)`) and driven by `env/values/engine.json`.

For an engine with total chamber volume `V_c` (2 chambers of `V_c/2`):

$$m_{Al} = 0.66 \times V_c \times 2\,700\ \text{kg/m}^3$$

$$N_{cans} = \left\lceil \frac{m_{Al}}{m_{can}} \right\rceil,\qquad C_{cans} = N_{cans} \times p_{can}$$

$$C_{remelt} = m_{Al} \times 0.3375\ \text{kWh/kg} \times 0.20\ \text{€/kWh},\qquad C_{mat} = C_{cans} + C_{remelt}$$

## 3. Material per engine (baseline)

<!-- calc:material:en -->
| Engine | Total `V_c` | Aluminium | Cans | Can cost | Remelting | **Material total** |
|---|---:|---:|---:|---:|---:|---:|
| **2 hp** | 135.53 L | 241.5 kg | 17,251 | €517.53 | €16.30 | **€533.83** |
| **6 hp** | 406.58 L | 724.5 kg | 51,752 | €1,552.56 | €48.91 | **€1,601.47** |
| **20 hp** | 1,355.26 L | 2415.1 kg | 172,506 | €5,175.18 | €163.02 | **€5,338.20** |
| **2 full cylinders (stress test)** | 2 × 3.534 m³ | 12,596.2 kg | 899,730 | €26,991.90 | €850.24 | **€27,842.14** |
<!-- /calc:material:en -->

The first three rows are **product-sized engines** (total chamber volume `V_c`, 66 % fill). The last row is the pessimistic **2-full-cylinder** stress test — an upper bound kept separate from product cost.

## 4. Can cost scenarios

<!-- calc:can:en -->
| Can mass | Can price | €/kg (cans) | 2 hp cans | 2 hp can cost | 2 hp material | Stress-test material |
|---:|---:|---:|---:|---:|---:|---:|
| 14 g/can | 3 c/can | 2.14 | 17,251 | €517.53 | **€533.83** | **€27,842.14** |
| 14 g/can | 2 c/can | 1.43 | 17,251 | €345.02 | **€361.32** | **€18,844.84** |
| 14 g/can | 1 c/can | 0.71 | 17,251 | €172.51 | **€188.81** | **€9,847.54** |
| 8 g/can | 3 c/can | 3.75 | 30,189 | €905.67 | **€921.97** | **€48,086.05** |
| 8 g/can | 2 c/can | 2.50 | 30,189 | €603.78 | **€620.08** | **€32,340.78** |
| 8 g/can | 1 c/can | 1.25 | 30,189 | €301.89 | **€318.19** | **€16,595.51** |
<!-- /calc:can:en -->

## 5. Reading the result

- At the baseline (14 g, 3 c), the **2 hp** engine material is ≈ **€534** and the stress test is ≈ **€27,842**.
- Cans dominate the material total; lower can price or efficient collection/sourcing reduces cost directly, while lighter cans increase count for the same aluminium mass.
- The stress test remains a ceiling/reference, not a per-engine product material cost.
- Using this charge through low-volume lathe production is a [failing scenario](../archive/scenarios/lathe-low-volume.md): sell or rent the production machine instead of amortizing a few items per unit.

## 6. What is excluded

Machining, tool wear, casting/printing, binder, labour, transport and the solar furnace capex. The full production cost is in [costs](costs.md); the series build-up is in [lathe machining](../engines/manson/costs/lathe-machining.md); workshop equipment ranges are in [workshop equipment](workshop/equipment.md).

## See also

- [Costs](costs.md)
- [Workshop equipment](workshop/equipment.md)
- [Manson material costs](../engines/manson/costs/README.md)
- [Manson sizing](../engines/manson/sizing.md)
- [Lathe machining — series cost](../engines/manson/costs/lathe-machining.md)
- [env configuration](../env/README.md)
