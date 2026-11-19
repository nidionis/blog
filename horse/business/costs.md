# Costs, production and sales by priority

> **Status:** canonical roll-up · **Owns:** cost summary · **Up:** [Business](README.md)

This table is a roll-up: some rows are capex, some are prototype builds, and some are sale prices. The entry prototype is 25 000 €; the full workshop can reach about 307 000 €. The series engine is estimated at ≈ **16,650 €** and the retained sale price is **19,999 €** (see [lathe machining](../engines/manson/costs/lathe-machining.md)).

All amounts are estimates in euros. Some rows are **tooling/capex**, some are **prototype builds**, and some are **sale prices**. They are not alternatives for the same item.

| Equipment / production | Scope | Production cost | Sale price | Source |
|---|---|---:|---:|---|
| [Small binder jetting](https://www.iro3d.com/) | capex | 30 000 | — | external |
| [XXL binder jetting](../production/binder-jetting/cost.md) | capex (BOM) | 46 000 – 78 000 | — | detailed BOM; ~100 000 all-in with R&D |
| XLarge PLA printer DIY | capex | 20 000 | 30 000 | — |
| Supplement Tour | capex | 5 000 | 35 000 | — |
| Prototype(s) | prototype | 15 000 | — | — |
| Prototype gearing | prototype | 10 000 | — | — |
| Complete pellet extruder (Titan type) | capex | 15 000 | — | — |
| Nitrogen generator | capex | 30 000 | — | — |
| Welding station | capex | 2 000 | — | — |
| Sheet roller | capex | 50 000 | — | — |
| Aluminium shredder (recycling) | capex | 30 000 | — | — |
| **Entry prototype (prototype + gearing)** | prototype | **25 000** | — | sum of the two prototype rows |
| **Full workshop (if every row is bought)** | capex + prototypes | **~253 000 – 285 000** (BOM) · **~307 000** (all-in) | — | capex + prototype rows; the entry-prototype row is a subtotal |
| [2 m lathe](../engines/manson/costs/lathe-machining.md) | capex | 600 000 | — | 3-year life |
| [Lathe amortization (1 year)](../engines/manson/costs/lathe-machining.md) | capex | 200 000 | — | €600,000 / 3 |
| [First engine — full lathe charge](../engines/manson/costs/lathe-machining.md) | prototype | 215 250 | — | excluding piston; ≈ 216 450 with piston |
| [2 chambers tool wear](../engines/manson/costs/lathe-machining.md) | production | 3 000 | — | per engine (upper bound) |
| [2 cylinders casting/printing](../engines/manson/costs/lathe-machining.md) | production | 12 000 | — | per engine (upper bound) |
| [Raw aluminum (2 cylinders, 66 %)](../engines/manson/costs/lathe-machining.md) | production | 252 | — | €0.02/kg |
| [Piston + rod + cylinder](../engines/manson/costs/lathe-machining.md) | production | 1 200 | — | 3 high-end bearings |
| [Production cost per engine (1,000/year)](../engines/manson/costs/lathe-machining.md) | production | 16 652 | — | lathe shared over 1,000 engines |
| [Retained sale price (resilience)](../engines/manson/costs/lathe-machining.md) | sale | — | 19 999 | margin ≈ 3,347 (2,000 salary + 1,347 buffer) |

## How to read this

- The business README's "from 25 000 €" is the **entry prototype**: 15 000 € prototype + 10 000 € gearing.
- The ~307 000 € figure is the **full equipment list**, not the price of a first engine.
- The **first engine** row charges the whole annual lathe amortization to one engine; it is a prototype cost, not the series cost.
- The **series engine** row spreads the lathe over 1,000 engines/year: ≈ 16,650 € cost, 19,999 € price, ≈ 3,350 € gross margin.
- The equipment/prototype rows above the **Full workshop** subtotal are capex; the engine production rows below it are **per-engine costs** and are not part of that subtotal.
- The XXL binder-jetting BOM is 46 000 – 78 000 €; the 100 000 € figure includes R&D and integration. See [details](../production/binder-jetting/cost.md).
- Raw-material costs for a massive motor are in [recycled material](recycled-material.md).

## See also

- [Manson material costs](../engines/manson/costs/README.md)
- [Lathe machining — production cost and resale price](../engines/manson/costs/lathe-machining.md)
- [Binder-jetting BOM](../production/binder-jetting/cost.md)
- [Business model](business-model.md)
