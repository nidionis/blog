# Failing scenario — lathe low volume and machine sale

> **Status:** archived scenario · **Owns:** low-volume lathe amortization risk · **Up:** [Archive](../README.md)

This page archives the **worst-deal** production path: using a 2 m lathe as the production unit for only a few engines per year. It is kept as a **failing scenario** and a trigger to consider selling or renting out the production machine.

## Why this is the worst deal

- **2 m lathe**: purchase ≈ **€600,000**, 3-year life → **€200,000/year** amortization.
- The series cost model only works when the lathe produces **thousands of engines** over its life.
- At **12 engines/year** (one sale/month), the lathe share is `€200,000 / 12 ≈ €16,667` per engine.
- With the 2 hp product material and conservative casting/tooling charges, the production cost rises to ≈ **€33,420**.
- At the retained sale price of **€19,999**, this does not cover amortization.

## Material ceiling reference

The 2-full-cylinder stress test (2 cylinders `d = 1.5 m`, `L = 2 m`, filled at 66 % → 12,596 kg Al) is a **material ceiling/reference**, not a per-engine product path. At baseline env-configured can assumptions (14 g, €0.03/can) it is ~**€27,842** material; see [recycled material](../../business/recycled-material.md) and [can scenarios](../../business/recycled-material.md#4-can-cost-scenarios). The project now exposes the prototype as **€15,000** (expect **€30,000** if the connecting rod and support are ordered), separate from series pricing.

Forcing a 2-full-cylinder material charge through low-volume lathe production remains non-viable at €19,999.

## Failing-scenario actions

If production stays at a few units per lathe:

1. **Stop the per-unit amortization path** — it is not viable.
2. **Sell the production machine** (2 m lathe) to recover capital, or
3. **Rent/share the lathe** with other production to spread amortization, or
4. **Build for stock** only if demand and cash flow justify it, or
5. **Raise the price** to cover real amortization.

## Superseded assumptions

- Old “whole lathe on one engine” and outsourced first-prototype breakdowns are superseded by the current prototype pricing and env-driven cost model.
- The first prototype route remains **PLA print → sand mold → casting → lathe finishing**, bounded by process/iteration choices rather than by obsolete outsourced ranges.

## See also

- [First prototype](../../engines/manson/costs/prototype.md)
- [Recycled material](../../business/recycled-material.md)
- [Costs](../../business/costs.md)
- [Workshop equipment](../../business/workshop/equipment.md)
- [Series cost model](../../engines/manson/costs/lathe-machining.md)
- [French archive](../../2cheval/archive/scenarios/lathe-low-volume.md)
- [Archive](../README.md)
