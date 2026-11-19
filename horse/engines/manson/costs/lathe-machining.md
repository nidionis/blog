# Lathe machining — Production cost and resale price — English main project

> **Status:** cost model · **Owns:** per-engine production cost and sale price · **Up:** [M Reloaded](README.md)

The 2 m lathe is the main capex. Charged to a single engine, it gives a prototype cost ≈ **€215,250**. In series, amortized over thousands of engines, it costs only a few hundred euros per unit. The pessimistic engine cost is ≈ **€16,650**; the retained sale price is **€19,999**, with ≈ **€3,350** gross margin, of which **€2,000** targets a salary (one sale per month) and ≈ **€1,350** is a commercial buffer.

## 1. Assumptions (pessimistic, upper bound)

- **2 m lathe**: purchase ≈ **€600,000**, 3-year life → **€200,000/year** amortization.
- **Production**: `N` engines/year; scenarios **1,000 / 3,000 / 5,000**.
- **Tool wear** for 2 chambers: **€3,000/engine**.
- **Casting/printing** of 2 cylinders `d = 1.5 m`, `L = 2 m`: **€12,000/engine**.
- **Raw aluminum**: 2 × 6,300 kg × **€0.02/kg** ≈ **€252/engine**.
- **Piston + connecting rod + cylinder**: **€1,200/engine** (piston ≈ €200, rod with 3 high-end bearings ≈ €900–1,000, cylinder ≈ €50–60).

Upper bound: 2 chambers and 2 cylinders are charged to **every** engine. If the cylinders are billets shared between several engines, the real cost per engine is lower. The small-chamber 2 hp engine is also cheaper; this upper bound covers the large-cylinder case.

## 2. Cost per engine

| Item | 1,000 engines/year | 3,000 engines/year | 5,000 engines/year |
|---|---:|---:|---:|
| Lathe share (`€200,000 / N`) | 200 | 67 | 40 |
| 2 chambers tool wear | 3,000 | 3,000 | 3,000 |
| 2 cylinders casting/printing | 12,000 | 12,000 | 12,000 |
| Raw aluminum (2 cylinders, 66 %) | 252 | 252 | 252 |
| Piston + rod + cylinder | 1,200 | 1,200 | 1,200 |
| **Production cost** | **16,652** | **16,519** | **16,492** |

## 3. Max piston cost

No gears: a connecting rod with **3 high-end ball bearings** and one more cylinder.

| Component | Pessimistic estimate |
|---|---:|
| Metallized piston | ≈ €200 |
| Connecting rod (3 high-end bearings + rod + pins) | ≈ €900–1,000 |
| Chamber cylinder (aluminum + machining) | ≈ €50–60 |
| **Piston total** | **≈ €1,200** |

## 4. Sale price and margin

| | 1,000 engines/year | 3,000 engines/year | 5,000 engines/year |
|---|---:|---:|---:|
| Production cost | 16,652 | 16,519 | 16,492 |
| Retained sale price | 19,999 | 19,999 | 19,999 |
| **Gross margin** | **3,347** | **3,480** | **3,507** |
| Of which salary (1 sale/month) | 2,000 | 2,000 | 2,000 |
| Commercial buffer | 1,347 | 1,480 | 1,507 |

The floor price “cost + €2,000” would be ≈ **€18,650** (at 1,000 engines/year). The retained **€19,999** price leaves ≈ **€1,350** more for transport, warranty and administration.

## 5. First engine (prototype)

If the whole lathe is charged to a single engine, excluding the piston: `€200,000 + €3,000 + €12,000 + €252 ≈ €215,250`. With the piston: ≈ **€216,450**. That is the prototype cost, not the series cost. See [the French cost detail](../../../2cheval/production/machining-cost.md).

## 6. Honest limit

The **€19,999** price holds if the lathe produces **thousands** of engines over its life (or is shared with other production). At 12 engines/year (one sale/month), the lathe share is `€200,000 / 12 ≈ €16,667` per engine: the cost rises to ≈ **€33,100** and €19,999 does not cover amortization. In that case: build for stock, rent/share the lathe, or raise the price.

## See also

- [M Reloaded](README.md)
- [Material costs](README.md)
- [Business costs](../../../business/costs.md)
- [Dictionary technical](../../../GLOSSARY.md)
- [French version (2Cheval)](../../../2cheval/production/usinage-tour.md)
- [French resilience argument](../../../2cheval/business/resilience.md)

Keywords: [lathe machine / tour a metaux](../../../2cheval/production/usinage-tour.md), [cost estimates / estimations cout / recettes](../../../business/costs.md).
