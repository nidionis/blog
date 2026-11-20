# Costs — central roll-up

> **Status:** canonical roll-up · **Owns:** cost summary · **Up:** [Business](README.md) · **Lang:** EN · [FR](../2cheval/business/costs.md)

All amounts are **pessimistic estimates in euros**, at the 5 % baseline. Costs move with scale, yield and iteration: see [investment valorisation](investment-valorisation.md). This page owns the summary; derivations are linked.

## 1. Workshop and equipment

| Equipment / production | Scope | Production cost | Sale price | Note |
|---|---|---:|---:|---|
| [Small binder jetting](https://www.iro3d.com/) | capex | 30,000 | — | external |
| [XXL binder jetting](../production/binder-jetting/cost.md) | capex (BOM) | 46,000–78,000 | — | ~100,000 all-in with R&D |
| XLarge PLA printer DIY | capex | 20,000 | 30,000 | — |
| Lathe supplement | capex | 5,000 | 35,000 | — |
| Prototype(s) | prototype | 15,000 | — | — |
| Prototype gearing | prototype | 10,000 | — | — |
| Complete pellet extruder (Titan type) | capex | 15,000 | — | — |
| Nitrogen generator | capex | 30,000 | — | — |
| Welding station | capex | 2,000 | — | — |
| Sheet roller | capex | 50,000 | — | — |
| Aluminium shredder (recycling) | capex | 30,000 | — | — |
| **Entry prototype (prototype + gearing)** | prototype | **25,000** | — | subtotal |
| **Full workshop (every row)** | capex + prototypes | **~253,000–285,000** (BOM) · **~307,000** (all-in) | — | not the price of one engine |

The **2 m lathe** is a separate series capex: €600,000 over 3 years → €200,000/year. It is not in the workshop total because buying it for one prototype is the [failing scenario](../archive/scenarios/lathe-low-volume.md).

## 2. First engine prototype and waste factor

The first engine is an **unoptimized re-try**. Cost is dominated by **iteration and waste** (overpour, scrap, rework), not by perfect material. The [large-piston worked example](../engines/manson/costs/large-piston-estimate.md) shows the driver: a ×1 perfect-material case can become ×3–4 on an isolated prototype, then fall with learning.

| Item | Value | Note |
|---|---:|---|
| First prototyping assurance | **€15,000–30,000** | material, process, finishing, iteration risk |
| Material ceiling (2 full cylinders, 66 %) | €28,842 | 933,053 cans + remelting; stress test, not product material |
| Optimized 2 hp product material | €553 | 241.5 kg, 17,890 cans + remelting |

Route: **PLA print (1.5 m³) → sand mold (10 m³) → casting (~3 m³ crucible) → lathe finishing (~1.40 m)**. Each iteration is [valorised](investment-valorisation.md) as lower waste and validated geometry. Detail: [first prototype](../engines/manson/costs/prototype.md), [recycled material](recycled-material.md).

## 3. Series engine

| Item | 1,000 engines/year | 3,000 engines/year | 5,000 engines/year |
|---|---:|---:|---:|
| Lathe share (€200,000 / N) | 200 | 67 | 40 |
| 2 chambers tool wear | 3,000 | 3,000 | 3,000 |
| 2 cylinders casting/printing (pessimistic) | 12,000 | 12,000 | 12,000 |
| Recycled aluminium, cans (2 hp total `V_c`) | 553 | 553 | 553 |
| Piston + rod + cylinder | 1,200 | 1,200 | 1,200 |
| **Production cost** | **16,953** | **16,820** | **16,793** |
| Retained sale price | 19,999 | 19,999 | 19,999 |
| **Gross margin** | **3,046** | **3,179** | **3,206** |

The margin includes about **€2,000** for a salary (one sale/month) and €1,046–1,206 for transport, warranty and administration. Assumptions and component breakdown: [lathe model](../engines/manson/costs/lathe-machining.md). At 12 engines/year the lathe share alone is €16,667 and the cost rises to ≈ €33,420 — see the [failing scenario](../archive/scenarios/lathe-low-volume.md).

## 4. What the engine replaces (price positioning)

| Replaced item | Typical cost | Note |
|---|---:|---|
| Air-water heat pump, 15–30 kW | €15,000–35,000 | heat only, COP 2–4 |
| Compact tractor, 20–40 hp | €25,000–60,000 | mechanical work |
| **2Cheval engine** | **€19,999** | ~1.5 kW shaft + ~29 kW heat at 5 % |

5 % mechanical efficiency is **not** a heat-pump COP: this is price positioning for heat plus shaft work, not thermodynamic equivalence. See [resilience](resilience.md).

## How to read this

- “From €25,000” is the **entry prototype** (15,000 prototype + 10,000 gearing), not the engine price.
- “~€307,000” is the **full equipment list**, not the first engine.
- The **first engine assurance** is **€15,000–30,000**; the **series price** is **€19,999**.
- Raw material per engine is in [recycled material](recycled-material.md); can price €0.03, remelting separate.

## See also

- [Resilience](resilience.md) — why the price is defensible
- [Investment valorisation](investment-valorisation.md) — capex, waste factor, learning
- [First prototype](../engines/manson/costs/prototype.md) · [Large-piston estimate](../engines/manson/costs/large-piston-estimate.md)
- [Lathe model](../engines/manson/costs/lathe-machining.md) · [Recycled material](recycled-material.md)
- [Binder-jetting BOM](../production/binder-jetting/cost.md) · [Manson material costs](../engines/manson/costs/README.md)
