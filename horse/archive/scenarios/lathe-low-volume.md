# Failing scenario — lathe low volume and machine sale

> **Status:** archived scenario · **Owns:** low-volume lathe amortization risk · **Up:** [Archive](../README.md)

This page archives the **worst-deal** production path: using a 2 m lathe as the production unit for only a few engines per year. It is kept as a **failing scenario** and a trigger to consider selling or renting out the production machine.

## Why this is the worst deal

- **2 m lathe**: purchase ≈ **€600,000**, 3-year life → **€200,000/year** amortization.
- The series cost model only works when the lathe produces **thousands of engines** over its life.
- At **12 engines/year** (one sale/month), the lathe share is `€200,000 / 12 ≈ €16,667` per engine.
- With the 2 hp product material and conservative casting/tooling charges, the production cost rises to ≈ **€33,420**.
- At the retained sale price of **€19,999**, this does not cover amortization.

## 2-full-cylinder stress test (material ceiling)

The material stress test uses 2 full cylinders `d = 1.5 m`, `L = 2 m`, filled at 66 % → 12,596 kg, 933,053 cans, **€28,842** material (cans €27,992 + remelting €850). This is treated as the **maximal value for an unoptimized first re-try** and rounded to **€30,000** as investment assurance for first prototyping: **€15,000–30,000**.

If the same 2-full-cylinder charge is forced through low-volume lathe production, the total becomes ≈ **€45,242** at 1,000 engines/year and still ≈ **€45,082** at 5,000 engines/year — a negative margin at €19,999. This confirms: do not use the 2-full-cylinder billet as a per-engine product path.

## Failing-scenario actions

If production stays at a few units per lathe:

1. **Stop the per-unit amortization path** — it is not viable.
2. **Sell the production machine** (2 m lathe) to recover capital, or
3. **Rent/share the lathe** with other production to spread amortization, or
4. **Build for stock** only if demand and cash flow justify it, or
5. **Raise the price** to cover real amortization.

## Superseded assumptions

- Old “whole lathe on one engine” comparison: ≈ €243,842 excluding piston (≈ €245,042 with piston) with hardened can/remelting assumptions. Not a first-build scenario.
- Old outsourced first-prototype range €52,000–196,000 and furnace capex €122,000–426,000 are superseded by the **€15,000–30,000** first-prototyping investment assurance anchored to the €30,000 unoptimized material ceiling.
- The first prototype route remains conceptually **PLA print → sand mold → casting → lathe finishing**, but its investment is bounded by the assurance range rather than by the old outsourced breakdown.

## See also

- [First prototype](../../engines/manson/costs/prototype.md)
- [Recycled material](../../business/recycled-material.md)
- [Costs](../../business/costs.md)
- [Series cost model](../../engines/manson/costs/lathe-machining.md)
- [French archive](../../2cheval/archive/scenarios/lathe-low-volume.md)
- [Archive](../README.md)
