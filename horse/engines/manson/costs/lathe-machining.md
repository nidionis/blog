# Lathe cost model — assumptions and margin

> **Status:** cost model · **Owns:** per-engine series cost assumptions · **Up:** [M Reloaded](README.md) · **Lang:** EN · [FR](../../../2cheval/production/usinage-tour.md)

The 2 m lathe is for **finishing** and series production, not first shaping. The first prototype is a **€15,000–30,000** unoptimized re-try assurance: see [first prototype](prototype.md). This page owns the assumptions; the summary table is in [business costs](../../../business/costs.md#3-series-engine).

## 1. Assumptions (pessimistic, upper bound)

- **2 m lathe** — purchase ≈ **€600,000**, 3-year life → **€200,000/year**.
- **Production** — `N` engines/year; viable scenarios **1,000 / 3,000 / 5,000**.
- **Tool wear** for 2 chambers — **€3,000/engine**.
- **Casting/printing** of 2 cylinders `d = 1.5 m`, `L = 2 m` — **€12,000/engine**.
- **Recycled aluminium** — 2 hp total chamber volume 135.53 L × 66 % × 2,700 kg/m³ = **241.5 kg** → **17,890 cans** at €0.03 = **€536.70**, plus **€16.30** remelting → **€553/engine**. Detail: [recycled material](../../../business/recycled-material.md).
- **Piston + connecting rod + cylinder** — **€1,200/engine**.

The tool-wear and casting lines remain oversized 2-cylinder charges, so the total stays conservative.

## 2. Cost formula

$$C(N) = \frac{200{,}000}{N} + 3{,}000 + 12{,}000 + 553 + 1{,}200$$

| `N` engines/year | Lathe share | Production cost | Margin at €19,999 |
|---:|---:|---:|---:|
| 1,000 | €200 | €16,953 | €3,046 |
| 3,000 | €67 | €16,820 | €3,179 |
| 5,000 | €40 | €16,793 | €3,206 |

The floor price “cost + €2,000” would be ≈ **€18,953** at 1,000 engines/year. The retained **€19,999** leaves about **€1,046** for transport, warranty and administration. See the [central table](../../../business/costs.md#3-series-engine).

## 3. Max piston cost

No gears: a connecting rod with **3 high-end ball bearings** and one more cylinder.

| Component | Pessimistic estimate |
|---|---:|
| Metallized piston | ≈ €200 |
| Connecting rod (3 high-end bearings + rod + pins) | ≈ €900–1,000 |
| Chamber cylinder (aluminium + machining) | ≈ €50–60 |
| **Piston total** | **≈ €1,200** |

## 4. Prototype ceiling and failing scenario

The **2-full-cylinder stress test** (2 cylinders `d = 1.5 m`, `L = 2 m`, 66 % fill → 12,596 kg, 933,053 cans) gives **€28,842** of material, rounded to **€30,000** as the maximal unoptimized first-retry value: **€15,000–30,000**. It is not a per-engine cost. See [first prototype](prototype.md) and [recycled material](../../../business/recycled-material.md).

Producing only a few items per lathe is the **worst deal**: at 12 engines/year the lathe share is ≈ €16,667/engine and the cost rises to ≈ €33,420, above €19,999. The action is to **sell or rent the production machine**. See [failing scenario](../../../archive/scenarios/lathe-low-volume.md).

## See also

- [Business costs — central table](../../../business/costs.md)
- [First prototype](prototype.md)
- [Recycled material](../../../business/recycled-material.md)
- [Material costs](README.md)
- [Resilience](../../../business/resilience.md)
