# Resilience — a pessimistic engine, many ways out

> **Status:** canonical commercial argument · **Owns:** resilience and flexibility · **Up:** [Business](README.md) · **Lang:** EN · [FR](../2cheval/business/resilience.md)

The 2Cheval is not resilient because it is optimal. It is resilient because it is sized at the **pessimistic floor** and has several independent ways to improve, substitute or degrade gracefully. This page is the argument behind the €19,999 price; the numbers live in [levers](../levers/README.md) and [costs](costs.md).

## 1. Four kinds of resilience

| Kind | Question | Answer |
|---|---|---|
| **Source** | What if straw is unavailable? | Wood, pellets, charcoal, oil, solar heat, nuclear heat; the engine only needs heat. |
| **Load** | What if the load changes? | Shaft, heat, electricity, tractor, heat pump; a slow shaft is easy to redirect. |
| **Design** | What if a part or skill is missing? | Open cycle, atmospheric pressure, low frequency, simple castings, hackable drivetrain. |
| **Economic** | What if the optimistic case fails? | The 5 % baseline still delivers 2 hp; the price is anchored to what it replaces. |

## 2. Source resilience

The [Manson](../engines/manson/README.md) is an **external-combustion** engine: the working air never mixes with the fuel. The [rocket stove](../energy/rocket-stove/README.md) can burn anything that burns, and the engine does not care about ash, moisture or flame colour — only about the heat reaching its hot side.

| Source | State | Carrier | Constraint | Article |
|---|---|---|---|---|
| Straw | reference | 12 MJ/kg, 100–250 kg/m³ | feed limit, moisture | [straw](../energy/rocket-stove/straw.md) |
| Wood, pellets, miscanthus | substitute | 13.5–18 MJ/kg | ash, stove size | [biomass](../energy/rocket-stove/biomass-calorific.md) |
| Charcoal, oil | dense substitute | 30–43 MJ/kg | cost, storage, safety | [fuel](../engines/manson/fuel.md) |
| Solar heat | hybrid | 2–6 kWh/m²/day | area, night, winter | [solar](../energy/solar/README.md) |
| Nuclear heat | exploratory | 1–12 hp range | shielding, regulation | [nuclear](../energy/nuclear/README.md) |
| Electricity / heat pump | replacement | grid or battery | capex, grid dependence | [costs](costs.md#4-what-the-engine-replaces) |

A wet or low-quality fuel does not break the engine; it lowers the achievable power and raises the consumption. The pessimistic 12 MJ/kg baseline already accounts for a bad batch. The 30 kg / 20 min feed limit is a **stove and feeding** assumption, not a thermodynamic law: densified straw, a better auger or multiple stoves can raise it. See [fuel](../engines/manson/fuel.md).

## 3. Load resilience

- **Shaft** — the primary output; a slow, high-torque shaft can drive a [tractor](../drivetrain/design.md), a pump, a mill or a winch.
- **Heat** — most of the straw energy leaves as heat. A heat exchanger can recover it for space, water or process heat.
- **Electricity** — a [linear alternator](../engines/stirling/linear-alternator.md) is studied for the Stirling variant; the Manson can also drive a generator.
- **Storage** — a [battery](../electric/README.md) is convenient but expensive per kWh; a hot-water or biomass store is cheaper for heat. Kinetic storage is documented in the [drivetrain](../drivetrain/design.md).

The point is not that one load is best. The point is that the same heat source can serve several loads, so a failed market or a failed generator does not strand the engine.

## 4. Design resilience

- **Open cycle, atmospheric pressure** — no sealed crankcase, no high-pressure vessel, no turbocharger.
- **Low frequency** — 2 Hz tolerates simple bearings and imperfect combustion; speed is an optional lever, not a requirement.
- **Simple materials** — cast aluminium from cans, a lathe-finished chamber, a [hackable drivetrain](../drivetrain/README.md).
- **Local production** — [PLA print → sand mold → casting → lathe](../engines/manson/costs/prototype.md) can be done close to the customer.
- **Soft-coded model** — the [lever model](../model/README.md) makes the trade-offs explicit and editable.

## 5. Failure modes and responses

| Failure | Response | Lever |
|---|---|---|
| Efficiency stays at 5 % | Build the larger 2 hp chamber; keep the promise | [volume and weight](../levers/volume-weight.md) |
| Chamber too heavy or too large | Raise pressure, frequency or temperature | [pressure](../levers/pressure.md), [frequency](../levers/frequency.md), [temperature](../levers/temperature.md) |
| Straw too wet or too expensive | Dry, densify, mix wood/pellets, or raise efficiency | [efficiency](../levers/efficiency.md), [straw](../energy/rocket-stove/straw.md) |
| No sun | Burn straw; solar is a hybrid, not a dependency | [insolation](../levers/insolation.md) |
| No biomass | Solar heat or the nuclear study; otherwise use the engine as a heat pump replacement | [solar](../energy/solar/README.md), [nuclear](../energy/nuclear/README.md) |
| No grid | Direct shaft and heat; electricity is optional | [drivetrain](../drivetrain/README.md) |
| Low production volume | Do not amortize a lathe on a few units; sell or rent it | [failing scenario](../archive/scenarios/lathe-low-volume.md) |
| Can price rises | Use scrap, ore or a different casting route | [recycled material](recycled-material.md) |

## 6. The pessimistic baseline is the guarantee

All commercial numbers use the floor: **5 % efficiency, 12 MJ/kg straw, 66 % casting fill, 30 kg / 20 min, €0.03/can**. The 15 % target and the 20 % lab ceiling are upside, not the promise. If they arrive, the engine gets smaller, lighter and cheaper per kW; if they do not, the 2 hp product still works.

## 7. Price positioning

| Item | Typical cost | Note |
|---|---:|---|
| Air-water heat pump, 15–30 kW | €15,000–35,000 | heat only, COP 2–4 |
| Compact tractor, 20–40 hp | €25,000–60,000 | mechanical work |
| **2Cheval engine** | **€19,999** | ~1.5 kW shaft + ~29 kW heat at the 5 % baseline |

The 5 % mechanical efficiency is **not** a heat-pump COP. The comparison is price positioning for heat plus shaft work, not thermodynamic equivalence. See [costs](costs.md#4-what-the-engine-replaces) and [customers](customers.md).

## 8. Limits

This is not perpetual motion and not a universal replacement. The engine is heavy, its electrical efficiency is low, its feed is limited, solar is intermittent, and the nuclear variant is a study, not a safety case. Resilience means **graceful degradation**, not infinite capability.

## See also

- [Levers](../levers/README.md) — the six improvement paths
- [Customers](customers.md) — the reference use case
- [Costs](costs.md) — workshop, prototype, series and replacement
- [Energy](../energy/README.md) — heat sources
- [Electric storage](../electric/README.md) — why batteries are the weak link
- [French version](../2cheval/business/resilience.md)
