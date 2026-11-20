# Costs — central roll-up

> **Status:** canonical roll-up · **Owns:** cost summary · **Up:** [Business](README.md) · **Lang:** EN · [FR](../2cheval/business/costs.md)

All amounts are **pessimistic estimates in euros**, at the 5 % baseline. Costs move with scale, yield and iteration: see [investment valorisation](investment-valorisation.md). This page owns the summary; derivations are linked.

## 1. Workshop and equipment

Detailed equipment, indicative **DIY vs purchased** ranges and reference links are in the [workshop equipment](workshop/equipment.md) folder. The [XXL binder-jetting BOM](../production/binder-jetting/cost.md) remains the component reference.

| Scope | Indicative range | Note |
|---|---:|---|
| Entry workshop / prototyping equipment (selected items) | ~25,000 € and up | see [equipment ranges](workshop/equipment.md); prototypes and gearing depend on route |
| Full workshop (BOM, indicative) | ~253,000–285,000 € | ~307,000 € all-in with integration/R&D; **not** the price of one engine |
| 2 m lathe (series capex) | ~600,000 € over 3 years | separate from workshop; low volume is a [failing scenario](../archive/scenarios/lathe-low-volume.md) |

## 2. First engine prototype

| Item | Value | Note |
|---|---:|---|
| **Prototype** | **€15,000** | expect **€30,000** if the connecting rod and support are ordered |
| Prototype gearing (if needed) | €10,000 | separate item; see [equipment ranges](workshop/equipment.md) |
| Material ceiling (2 full cylinders, 66 %, reference) | ~€27,842 | 899,730 cans + remelting at baseline can assumptions; stress test, not product material |
| Optimized 2 hp product material | ~€534 | 241.5 kg, 17,251 cans + remelting |

The first engine is an **unoptimized re-try**. Cost is dominated by **iteration and waste** (overpour, scrap, rework), not by perfect material. Route: **PLA print (1.5 m³) → sand mold (10 m³) → casting (~3 m³ crucible) → lathe finishing (~1.40 m)**. Detail: [first prototype](../engines/manson/costs/prototype.md), [recycled material](recycled-material.md), [can cost scenarios](recycled-material.md#can-cost-scenarios).

## 3. Series engine

| Item | 1,000 engines/year | 3,000 engines/year | 5,000 engines/year |
|---|---:|---:|---:|
| Lathe share (€200,000 / N) | 200 | 67 | 40 |
| 2 chambers tool wear | 3,000 | 3,000 | 3,000 |
| 2 cylinders casting/printing (pessimistic) | 12,000 | 12,000 | 12,000 |
| Recycled aluminium, cans (2 hp total `V_c`) | 534 | 534 | 534 |
| Piston + rod + cylinder | 1,200 | 1,200 | 1,200 |
| **Production cost** | **16,934** | **16,801** | **16,774** |
| Retained sale price | 19,999 | 19,999 | 19,999 |
| **Gross margin** | **3,065** | **3,198** | **3,225** |

By comparison, the standalone prototype is **€15,000** (expect **€30,000** if the connecting rod and support are ordered); the **€19,999** series price includes amortized tooling and margin. Assumptions and component breakdown: [lathe model](../engines/manson/costs/lathe-machining.md). At 12 engines/year the lathe share alone is €16,667 and the cost rises to ≈ €33,420 — see the [failing scenario](../archive/scenarios/lathe-low-volume.md).

## 4. What the engine replaces (price positioning)

| Replaced item | Typical cost | Note |
|---|---:|---|
| Air-water heat pump, 15–30 kW | €15,000–35,000 | heat only, COP 2–4 |
| Compact tractor, 20–40 hp | €25,000–60,000 | mechanical work |
| **2Cheval engine** | **€19,999** | ~1.5 kW shaft + ~29 kW heat at 5 % |

5 % mechanical efficiency is **not** a heat-pump COP: this is price positioning for heat plus shaft work, not thermodynamic equivalence. See [resilience](resilience.md).

## How to read this

- The **prototype** is **€15,000** (expect **€30,000** if the connecting rod and support are ordered); workshop/equipment capex is separate.
- “~€307,000” refers to the indicative **full equipment list** (all-in), not the first engine.
- The **series price** is **€19,999**.
- Raw material per engine is in [recycled material](recycled-material.md); can assumptions are env-configured (baseline 3 c/can, 14 g/can, down to 1 c and 8 g scenarios).

## See also

- [Workshop equipment](workshop/equipment.md)
- [Resilience](resilience.md) — why the price is defensible
- [Investment valorisation](investment-valorisation.md) — capex, waste factor, learning
- [First prototype](../engines/manson/costs/prototype.md) · [Large-piston estimate](../engines/manson/costs/large-piston-estimate.md)
- [Lathe model](../engines/manson/costs/lathe-machining.md) · [Recycled material](recycled-material.md)
- [Binder-jetting BOM](../production/binder-jetting/cost.md) · [Manson material costs](../engines/manson/costs/README.md)
