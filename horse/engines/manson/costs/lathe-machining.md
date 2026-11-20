# Lathe cost model — assumptions and margin

> **Status:** cost model · **Owns:** per-engine series cost assumptions · **Up:** [Manson costs](README.md) · **Lang:** EN · [FR](../../../2cheval/production/usinage-tour.md)

The 2 m lathe is for **finishing** and series production, not first shaping. The first prototype is **€15,000** (expect **€30,000** if the connecting rod and support are ordered): see [first prototype](prototype.md). This page owns the assumptions; the summary table is in [business costs](../../../business/costs.md#3-series-engine).

## 1. Assumptions (pessimistic, upper bound)

- **2 m lathe** — purchase ≈ **€600,000**, 3-year life → **€200,000/year**.
- **Production** — `N` engines/year; viable scenarios **1,000 / 3,000 / 5,000**.
- **Tool wear** for 2 chambers — **€3,000/engine**.
- **Casting/printing** of 2 cylinders `d = 1.5 m`, `L = 2 m` — **€12,000/engine**.
- **Recycled aluminium** — 2 hp total chamber volume 135.53 L × 66 % × 2,700 kg/m³ = **241.5 kg** → **17,251 cans** at baseline **€0.03/can** (14 g, env-configured) = **€517.53**, plus **€16.30** remelting → **~€534/engine**. Detail: [recycled material](../../../business/recycled-material.md).
- **Piston + connecting rod + cylinder** — **€1,200/engine**.

The tool-wear and casting lines remain oversized 2-cylinder charges, so the total stays conservative.

## 2. Cost formula

$$C(N) = \frac{200{,}000}{N} + 3{,}000 + 12{,}000 + 534 + 1{,}200$$

| `N` engines/year | Lathe share | Production cost | Margin at €19,999 |
|---:|---:|---:|---:|
| 1,000 | €200 | €16,934 | €3,065 |
| 3,000 | €67 | €16,801 | €3,198 |
| 5,000 | €40 | €16,774 | €3,225 |

By comparison, the standalone prototype is **€15,000** (expect **€30,000** if the connecting rod and support are ordered); series cost includes amortized tooling. The floor price “cost + €2,000” would be ≈ **€18,934** at 1,000 engines/year. The retained **€19,999** leaves margin for transport, warranty and administration. See the [central table](../../../business/costs.md#3-series-engine).

## 3. Max piston cost

No gears: a connecting rod with **3 high-end ball bearings** and one more cylinder.

| Component | Pessimistic estimate |
|---|---:|
| Metallized piston | ≈ €200 |
| Connecting rod (3 high-end bearings + rod + pins) | ≈ €900–1,000 |
| Chamber cylinder (aluminium + machining) | ≈ €50–60 |
| **Piston total** | **≈ €1,200** |

## 4. Prototype ceiling and failing scenario

The **2-full-cylinder stress test** (2 cylinders `d = 1.5 m`, `L = 2 m`, 66 % fill → 12,596 kg) gives ~**€27,842** of material at baseline can assumptions (899,730 cans, 14 g, €0.03), configurable down/up via [can scenarios](../../../business/recycled-material.md#4-can-cost-scenarios). It is a material ceiling/reference, not a per-engine cost.

Producing only a few items per lathe is the **worst deal**: at 12 engines/year the lathe share is ≈ €16,667/engine and the cost rises to ≈ €33,420, above €19,999. The action is to **sell or rent the production machine**. See [failing scenario](../../../archive/scenarios/lathe-low-volume.md).

## See also

- [Business costs — central table](../../../business/costs.md)
- [First prototype](prototype.md)
- [Recycled material](../../../business/recycled-material.md)
- [Workshop equipment](../../../business/workshop/equipment.md)
- [Material costs](README.md)
- [Resilience](../../../business/resilience.md)
