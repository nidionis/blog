# Large-piston estimate — aligned worked example

> **Status:** worked example · **Owns:** competitor/large-component cost alignment · **Up:** [Manson costs](README.md) · **Lang:** EN · [FR](../../../2cheval/engines/manson/costs/estimation-gros-piston.md)

This page aligns an external estimate for a **large piston component** (Ø1.50 m × 1.30 m stroke) with the project’s env-configured assumptions. It is **not** the 2 hp product engine: it is a scale/geometry example showing how material, waste factor, process and amortization drive cost. The 2 hp product baseline is [135.5 L total chamber, ~241.5 kg cast Al, ~€534 material at 14 g / €0.03](../../../business/recycled-material.md).

## 1. Geometry and material (recalculated)

| Item | Value | Note |
|---|---:|---|
| Cylinder | `V_cyl = π × 0.75² × 1.30 = 2.297 m³` | Ø1.50 m, stroke 1.30 m |
| Effective material (assumed) | `1.15 m³` | design assumption: displacer + chamber/rod/wheel |
| Aluminium density | `2,700 kg/m³` | [glossary](../../../GLOSSARY.md) |
| Effective mass | `1.15 × 2,700 = 3,105 kg` |  |
| Can price (baseline / low) | `€0.03 / €0.01 per can` | env-configured |
| Can mass (baseline / light) | `14 g / 8 g` | env-configured |
| Remelting | `0.3375 kWh/kg × €0.20/kWh = €0.0675/kg` | 80 % furnace, self-consumed solar |

| Material basis | Cans | Can cost | Remelting | **Perfect material** |
|---|---:|---:|---:|---:|
| 14 g cans, €0.03 (baseline) | 221,786 | €6,654 | €210 | **€6,863** |
| 14 g cans, €0.01 | 221,786 | €2,218 | €210 | **€2,427** |
| 8 g cans, €0.03 | 388,125 | €11,644 | €210 | **€11,853** |

“Perfect material” assumes the effective mass with no overpour, no scrap and no failed iteration. Real builds pay a **waste/iteration factor**.

## 2. Waste factor and unit scenarios

The waste factor bundles casting yield, overpour, defects, re-melt loss and re-tries. It is the main [valorisation](../../../business/investment-valorisation.md) lever: iteration reduces it.

| Scenario | Factor on perfect material | Material equivalent (14 g, €0.03 basis) | Casting/molding process | **Indicative unit cost** |
|---|---:|---:|---:|---:|
| Optimistic series | ×2 | ~€13,730 | ~€2,500–4,000 | **~€16,000–18,000** |
| Realistic | ×3 | ~€20,590 | ~€2,500–4,000 | **~€23,000–25,000** |
| Pessimistic isolated prototype | ×4 | ~€27,450 | ~€2,500–4,000 | **~€30,000–32,000** |

Casting/molding process here means furnace/amort share, energy, sand mold, labor and handling for this scale of part (order €2.5k–4k per iteration in a low-capex setup).

## 3. Workshop investment (scalable path)

| Equipment | Cost | Valorisation role |
|---|---:|---|
| Rails + motors (DIY CNC) | €2,000–4,000 | repeatable shaping |
| PLA→metal extrusion/nozzle project | €1,000–3,000 | process option, R&D asset |
| High-torque tool holder | €1,000–2,500 | machining capability |
| Lathe + rotary/printing (radial slicer) | €2,000–5,000 | finishing and iteration speed |
| **Total (indicative DIY path)** | **€6,000–10,000** | amortizable over series |

This is a **low-capex valorisation path**, different from the project’s €600k series lathe assumption. Buying heavy tooling for a few units is the [failing scenario](../../../archive/scenarios/lathe-low-volume.md); see [workshop equipment](../../../business/workshop/equipment.md) for indicative ranges.

## 4. PLA + sand prototyping

- PLA pattern for a large part: order **~€5,000** filament at this mass scale (less if recycled).
- Sand mold + partner machining: typically **€2,000–5,000 per iteration** depending on lab/foundry access.
- Value: validates geometry before committing to a risky metal pour — a direct form of [investment valorisation](../../../business/investment-valorisation.md).

## 5. Alignment with project baselines

| Reference | Scale | Material / cost signal | Use |
|---|---|---|---|
| 2 hp product engine | `V_c` 135.5 L, 241.5 kg Al | ~€534 material (baseline); series **€19,999** | canonical market product |
| 20 hp engine (5 % limit) | `V_c` 1,355 L, 2,415 kg Al | ~€5,338 material (baseline) | extreme at feed limit |
| This worked example | 1.15 m³ effective, 3,105 kg | ~€6.9k perfect material (baseline); ~€16–32k by scenario | large component / cost driver demo |
| 2-full-cylinder stress test | 12,596 kg Al | ~€27,842 material ceiling (baseline) | material ceiling / reference |

The example supports a **first resale range ~€30,000–40,000** for a large, early, low-volume component with margin, and lower unit cost in series if waste factor and amortization are valorised. For the 2 hp engine, the project keeps its documented baseline: **prototype €15,000** (expect **€30,000** if the connecting rod and support are ordered) and **€19,999 series price**. See [costs](../../../business/costs.md) and [recycled material](../../../business/recycled-material.md).

## See also

- [Investment valorisation](../../../business/investment-valorisation.md)
- [Recycled material / can scenarios](../../../business/recycled-material.md)
- [Workshop equipment](../../../business/workshop/equipment.md)
- [First prototype](prototype.md)
- [Lathe model](lathe-machining.md)
- [French version](../../../2cheval/engines/manson/costs/estimation-gros-piston.md)
