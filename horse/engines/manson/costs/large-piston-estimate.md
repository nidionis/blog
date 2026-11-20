# Large-piston estimate — aligned worked example

> **Status:** worked example · **Owns:** competitor/large-component cost alignment · **Up:** [Manson costs](README.md) · **Lang:** EN · [FR](../../../2cheval/engines/manson/costs/estimation-gros-piston.md)

This page aligns an external estimate for a **large piston component** (Ø1.50 m × 1.30 m stroke) with the project’s hardened assumptions. It is **not** the 2 hp product engine: it is a scale/geometry example that shows how material, waste factor, process and amortization drive cost. The 2 hp product baseline is [135.5 L total chamber, ~242 kg cast Al, ~€553 material](../../../business/recycled-material.md).

## 1. Geometry and material (recalculated)

| Item | Value | Note |
|---|---:|---|
| Cylinder | `V_cyl = π × 0.75² × 1.30 = 2.297 m³` | Ø1.50 m, stroke 1.30 m |
| Effective material (assumed) | `1.15 m³` | design assumption: displacer + chamber/rod/wheel |
| Aluminium density | `2,700 kg/m³` | [glossary](../../../GLOSSARY.md) |
| Effective mass | `1.15 × 2,700 = 3,105 kg` |  |
| Can price | `€0.03/can` | hardened project assumption |
| Can mass | `13.5 g` baseline (`15 g` variant shown) | `€2.22/kg` at 13.5 g, `€2.00/kg` at 15 g |
| Remelting | `0.3375 kWh/kg × €0.20/kWh = €0.0675/kg` | 80 % furnace, self-consumed solar |

| Material basis | Can cost | Remelting | **Perfect material** |
|---|---:|---:|---:|
| 13.5 g cans (project baseline) | €6,900 | €210 | **€7,110** |
| 15 g cans (variant) | €6,210 | €210 | **€6,420** |

“Perfect material” assumes the effective mass with no overpour, no scrap and no failed iteration. Real builds pay a **waste/iteration factor**.

## 2. Waste factor and unit scenarios

The waste factor bundles casting yield, overpour, defects, re-melt loss and re-tries. It is the main [valorisation](../../../business/investment-valorisation.md) lever: iteration reduces it.

| Scenario | Factor on perfect material | Material equivalent (13.5 g basis) | Casting/molding process | **Indicative unit cost** |
|---|---:|---:|---:|---:|
| Optimistic series | ×2 | ~€14,220 | ~€2,500–4,000 | **~€15,000–18,000** |
| Realistic | ×3 | ~€21,330 | ~€2,500–4,000 | **~€24,000–25,000** |
| Pessimistic isolated prototype | ×4 | ~€28,440 | ~€2,500–4,000 | **~€31,000–33,000** |

Casting/molding process here means furnace/amort share, energy, sand mold, labor and handling for this scale of part (order €2.5k–4k per iteration in a low-capex setup). A high-capex industrial route changes the split but not the need to amortize.

## 3. Workshop investment (scalable path)

| Equipment | Cost | Valorisation role |
|---|---:|---|
| Rails + motors (DIY CNC) | €2,000–4,000 | repeatable shaping |
| PLA→metal extrusion/nozzle project | €1,000–3,000 | process option, R&D asset |
| High-torque tool holder | €1,000–2,500 | machining capability |
| Lathe + rotary/printing (radial slicer) | €2,000–5,000 | finishing and iteration speed |
| **Total (indicative DIY path)** | **€6,000–10,000** | amortizable over series |

This is a **low-capex valorisation path**, different from the project’s €600k series lathe assumption. Buying heavy tooling for a few units is the [failing scenario](../../../archive/scenarios/lathe-low-volume.md); renting, sharing or selling the machine preserves value.

## 4. PLA + sand prototyping

- PLA pattern for a large part: order **~€5,000** filament at this mass scale (less if recycled).
- Sand mold + partner machining: typically **€2,000–5,000 per iteration** depending on lab/foundry access.
- Value: validates geometry before committing to a risky metal pour — a direct form of [investment valorisation](../../../business/investment-valorisation.md).

## 5. Alignment with project baselines

| Reference | Scale | Material / cost signal | Use |
|---|---|---|---|
| 2 hp product engine | `V_c` 135.5 L, 241.5 kg Al | ~€553 material; series **€19,999** | canonical market product |
| 20 hp engine (5 % limit) | `V_c` 1,355 L, 2,415 kg Al | ~€5,530 material | extreme at feed limit |
| This worked example | 1.15 m³ effective, 3,105 kg | ~€7.1k perfect material; ~€15–33k by scenario | large component / cost driver demo |
| 2-full-cylinder stress test | 12,596 kg Al | ~€28,842 material ceiling | first-engine assurance **€15k–30k** |

The example supports a **first resale range ~€30,000–40,000** for a large, early, low-volume component with margin (≈20–30 % on a realistic build), and **~€15,000–20,000** in series if waste factor and amortization are valorised. For the 2 hp engine, the project keeps the separate, documented baseline: **€15k–30k first-engine assurance** and **€19,999 series price**. See [costs](../../../business/costs.md).

## See also

- [Investment valorisation](../../../business/investment-valorisation.md)
- [Recycled material](../../../business/recycled-material.md)
- [First prototype](prototype.md)
- [Lathe model](lathe-machining.md)
- [French version](../../../2cheval/engines/manson/costs/estimation-gros-piston.md)
