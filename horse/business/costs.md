# Costs, production and sales — central roll-up — 2Cheval

> **Status:** canonical roll-up · **Owns:** cost summary · **Up:** [Business](README.md)

Central cost page: workshop, **first prototype**, **series engine** and **what the engine replaces**. All amounts are pessimistic estimates in euros.

## 1. Workshop and equipment

| Equipment / production | Scope | Production cost | Sale price | Source |
|---|---|---:|---:|---|
| [Small binder jetting](https://www.iro3d.com/) | capex | 30 000 | — | external |
| [XXL binder jetting](../production/binder-jetting/cost.md) | capex (BOM) | 46 000 – 78 000 | — | detailed BOM; ~100 000 all-in with R&D |
| XLarge PLA printer DIY | capex | 20 000 | 30 000 | — |
| Lathe supplement | capex | 5 000 | 35 000 | — |
| Prototype(s) | prototype | 15 000 | — | — |
| Prototype gearing | prototype | 10 000 | — | — |
| Complete pellet extruder (Titan type) | capex | 15 000 | — | — |
| Nitrogen generator | capex | 30 000 | — | — |
| Welding station | capex | 2 000 | — | — |
| Sheet roller | capex | 50 000 | — | — |
| Aluminium shredder (recycling) | capex | 30 000 | — | — |
| **Entry prototype (prototype + gearing)** | prototype | **25 000** | — | sum of the two prototype rows |
| **Full workshop (if every row is bought)** | capex + prototypes | **~253 000 – 285 000** (BOM) · **~307 000** (all-in) | — | capex + prototype rows; the entry-prototype row is a subtotal |
| [2 m lathe](../engines/manson/costs/lathe-machining.md) — series option | capex | 600 000 | — | 3-year life |
| [Lathe amortization (1 year)](../engines/manson/costs/lathe-machining.md) — series option | capex | 200 000 | — | €600,000 / 3 |

The 2 m lathe is a **series** capex, not a first-prototype cost: prototype finishing is subcontracted (see section 2).

## 2. First prototype — PLA, sand, casting, lathe

The first engine is not machined from solid: PLA print (1.5 m³) → sand mold (10 m³) → casting (~3 m³ crucible, solar furnace or foundry) → lathe finishing (~1.40 m). Detail: [prototype](../engines/manson/costs/prototype.md).

| Item | Low | Central | High |
|---|---:|---:|---:|
| PLA print 1.5 m³ | 20,000 | 45,000 | 75,000 |
| Fine sand 10 m³ | 3,000 | 5,000 | 8,000 |
| Contract casting | 10,000 | 20,000 | 30,000 |
| Lathe finishing 1.40 m | 3,000 | 10,000 | 20,000 |
| Piston + rod + cylinder | 1,200 | 2,000 | 3,000 |
| Engineering + assembly | 15,000 | 30,000 | 60,000 |
| **Outsourced prototype total** | **52,200** | **112,000** | **196,000** |
| Solar furnace + 3 m³ crucible + mirrors (capex) | 70,000 | 150,000 | 230,000 |
| **Total with furnace** | **122,200** | **262,000** | **426,000** |

The furnace and crucible are reusable: shared over 10 prototypes, their share falls to €7,000–23,000 per prototype. The first prototype itself therefore remains ≈ **€52,000–196,000**; the furnace is a workshop investment.

## 3. Series engine

| Item | 1,000 engines/year | 3,000 engines/year | 5,000 engines/year |
|---|---:|---:|---:|
| Lathe share (€200,000 / N) | 200 | 67 | 40 |
| 2 chambers tool wear | 3,000 | 3,000 | 3,000 |
| 2 cylinders casting/printing | 12,000 | 12,000 | 12,000 |
| Raw aluminum (2 cylinders, 66 %) | 252 | 252 | 252 |
| Piston + rod + cylinder | 1,200 | 1,200 | 1,200 |
| **Production cost** | **16,652** | **16,519** | **16,492** |
| Retained sale price | 19,999 | 19,999 | 19,999 |
| **Gross margin** | **3,347** | **3,480** | **3,507** |

Old comparison scenario: whole lathe charged to one engine = ≈ €215,250 excluding piston (see [lathe machining](../engines/manson/costs/lathe-machining.md)). It is no longer the first-build scenario.

## 4. What the engine replaces

| Replaced item | Typical cost | Note |
|---|---:|---|
| Air-water heat pump, 15–30 kW | 15,000 – 35,000 | heat only, COP 2–4 |
| Compact tractor, 20–40 hp | 25,000 – 60,000 | mechanical work |
| **2Cheval engine** | **19,999** | ~1.5 kW mechanical + ~29 kW thermal |

The 5 % mechanical efficiency is not a heat-pump COP. A heat pump moves 2–4 kWh of heat per kWh of electricity; the engine converts 5 % of the straw heat into shaft work and releases the rest as heat. The comparison is price positioning (heat + mechanical shaft), not thermodynamic equivalence: the engine sits in the heat-pump price range and below the price of a compact tractor, while delivering both heat and shaft power. The 20–40 hp tractor delivers much more power; the 2 hp engine is compared on price, not power.

## How to read this

- The business README's "from 25 000 €" is the **entry prototype**: 15 000 € prototype + 10 000 € gearing, not the engine prototype.
- The ~307 000 € figure is the **full equipment list**, not the price of a first engine.
- The XXL binder-jetting BOM is 46 000 – 78 000 €; the 100 000 € figure includes R&D and integration. See [details](../production/binder-jetting/cost.md).
- Raw-material costs for a massive motor are in [recycled material](recycled-material.md).
- The **first engine prototype** (section 2) is a prototyping cost, not the series cost.
- The **series engine** (section 3) spreads the lathe over thousands of units; the €19,999 price leaves ≈ €3,350 gross margin.

## See also

- [First prototype — PLA, sand, casting, lathe](../engines/manson/costs/prototype.md)
- [Lathe machining — series cost and resale price](../engines/manson/costs/lathe-machining.md)
- [Binder-jetting BOM](../production/binder-jetting/cost.md)
- [Business model](business-model.md)
- [Manson material costs](../engines/manson/costs/README.md)
