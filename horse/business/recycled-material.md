# Recycled material cost per engine

> **Status:** canonical · **Owns:** recycled-aluminium raw-material estimate · **Up:** [Business](README.md)

Raw-material estimate for cast aluminium made from used cans. The can price is hardened to **€0.03 per can** (the expected figure was €0.02), and remelting is charged **separately**. This is material only: machining, binder, labour and the rest of the production chain are excluded.

## 1. Assumptions

| Parameter | Value | Note |
|---|---:|---|
| Compacted aluminium density | **2,700 kg/m³** | solid-equivalent |
| Can mass | **13.5 g** | 74 cans/kg; 200,000 cans/m³ compacted |
| Chamber fill | **66 %** | pessimistic casting yield |
| Can price | **€0.03/can** | hardened from the expected €0.02 |
| Melting energy, theoretical | **0.27 kWh/kg** | heating + latent heat |
| Furnace efficiency | **80 %** | melting only |
| Remelting energy | **0.3375 kWh/kg** | 0.27 / 0.80 |
| Self-consumed solar electricity | **€0.20/kWh** | project assumption |
| Remelting cost | **€0.0675/kg** | 0.3375 × 0.20 |

The theoretical melting energy is `0.9 kJ/(kg·K) × 640 K + 397 kJ/kg ≈ 973 kJ/kg ≈ 0.27 kWh/kg` (aluminium heated from 20 °C to 660 °C, then melted).

## 2. Formula

For an engine with total chamber volume `V_c` (2 chambers of `V_c/2`):

$$m_{Al} = 0.66 \times V_c \times 2\,700\ \text{kg/m}^3$$

$$N_{cans} = \frac{m_{Al}}{0.0135\ \text{kg}}$$

$$\text{can cost} = N_{cans} \times €0.03$$

$$\text{remelting cost} = m_{Al} \times 0.3375\ \text{kWh/kg} \times €0.20/\text{kWh}$$

## 3. Material per engine

<!-- calc:material:en -->
| Engine | Total `V_c` | Aluminium | Cans | Can cost | Remelting | **Material total** |
|---|---:|---:|---:|---:|---:|---:|
| **2 hp** | 135.53 L | 241.5 kg | 17,889 | €536.67 | €16.30 | **€552.97** |
| **6 hp** | 406.58 L | 724.5 kg | 53,668 | €1,610.04 | €48.91 | **€1,658.95** |
| **20 hp** | 1,355.26 L | 2415.1 kg | 178,894 | €5,366.82 | €163.02 | **€5,529.84** |
| **2 full cylinders (stress test)** | 2 × 3.534 m³ | 12,596.2 kg | 933,053 | €27,991.59 | €850.24 | **€28,841.83** |
<!-- /calc:material:en -->

The first three rows are **product-sized engines**: total chamber volume `V_c` per engine (2 chambers of `V_c/2`), filled at 66 %. The last row is the old pessimistic billet case, **2 full cylinders** of `d = 1.5 m`, `L = 2 m` — the upper bound for remelting, kept separate from the product cost. Filling at 66 % keeps the remelting estimate below the 2-full-cylinder maximum.

## 4. Reading the result

- The **2 hp** engine material is ≈ **€553**: €537 of cans plus €16 of remelting.
- The **20 hp** fuel-limit engine material is ≈ **€5,530**.
- The **2-full-cylinder stress test** is ≈ **€28,842**, rounded to **€30,000** as the maximal unoptimized first-retry value. This sets the ceiling for the **€15,000–30,000** [first-prototyping investment assurance](../engines/manson/costs/prototype.md). It is not a per-engine product material cost.
- At €0.03/can, cans dominate: the can cost is ≈ 97 % of the material total, remelting ≈ 3 %.
- Using this charge through low-volume lathe production is a [failing scenario](../archive/scenarios/lathe-low-volume.md): sell or rent the production machine instead of amortizing a few items per unit.

## 5. What is excluded

Machining, tool wear, casting/printing, binder, labour, transport and the solar furnace capex. The full production cost is in [costs](costs.md); the series build-up is in [lathe machining](../engines/manson/costs/lathe-machining.md).

## See also

- [Costs](costs.md)
- [Manson material costs](../engines/manson/costs/README.md)
- [Manson sizing](../engines/manson/sizing.md)
- [Lathe machining — series cost](../engines/manson/costs/lathe-machining.md)
