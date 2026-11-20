# Electric storage — the weak link

> **Status:** reference · **Owns:** battery sizing and cost caveats · **Up:** [2Cheval](../README.md) · **Lang:** EN · [FR](../2cheval/electric/README.md)

The project is heat-first, not battery-first. A battery is useful for starting, control and short bursts; it is a poor way to store a day of engine output. This page keeps the battery numbers honest.

## The trap

The [sodium-ion note](batteries/poid.cout.euria.md) lists a “cost at 100 €/kWh” column. That is the **capital cost of cells**, not the price of electricity. Multiplying it by the energy consumed gives the cost of buying the battery, not the cost of running it. The note is kept as a sizing source, not as an operating-cost model.

## Order of magnitude for 2 hp

| Use | Mechanical energy | Cells at 140 Wh/kg | Cell capex at €100/kWh | At €50/kWh |
|---|---:|---:|---:|---:|
| 10 min | 0.245 kWh | 1.8 kg | €25 | €12 |
| 1 h | 1.47 kWh | 10.5 kg | €147 | €74 |
| 24 h | 35.3 kWh | 252 kg | €3,530 | €1,765 |

Add 15–20 % for the battery management system, housing and cables. A 10-minute run is easy; a 24-hour run is a 250 kg battery, which is why the reference design uses straw or heat storage instead. See [resilience](../business/resilience.md).

## What a battery is good for

- Starting and control of the engine.
- Bridging a short outage or a peak.
- Storing electricity from a generator, not heat for the engine.

For heat, a hot-water or biomass store is far cheaper per kWh. For shaft work, a flywheel or the [kinetic horse](../drivetrain/design.md) is the low-tech option.

## See also

- [Sodium-ion sizing note](batteries/poid.cout.euria.md) — source table and caveats
- [Resilience](../business/resilience.md) — why storage is the weak link
- [Drivetrain](../drivetrain/design.md) — kinetic storage
- [Energy](../energy/README.md) — heat sources
