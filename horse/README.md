# 2Cheval

**A heat engine with a concept: a horse that eats straw.**

**EN** · [Français](2cheval/README.md)

Straw burns in a [rocket stove](energy/rocket-stove/README.md); the heat drives an atmospheric [M Reloaded (Manson)](engines/manson/README.md); the shaft delivers **2 hp** and most of the straw energy leaves as usable heat. The engine is deliberately simple, heavy and low-speed. Its advantage is not efficiency: it is **resilience**.

## The product in one table

| Mode | Mechanical | Thermal at 5 % | Role |
|---|---:|---:|---|
| **Product** | **2 ch ≈ 1.47 kW** | ~29.4 kW | what the market needs |
| Stretch | 4 ch ≈ 2.94 kW | ~58.8 kW | optional build |
| Lab | 6 ch ≈ 4.41 kW | ~88.3 kW | test need |
| Extreme | 20 ch ≈ 14.71 kW | ~294 kW | at the 30 kg / 20 min feed limit, 5 % |

These are **5 % baseline** figures. A better efficiency, higher temperature, pressure or frequency makes the same power smaller; none of them is required for the 2 hp promise. See [levers](levers/README.md).

## Why it is resilient

- **Multi-fuel** — external combustion: straw, wood, pellets, charcoal, oil, solar or nuclear heat. The engine only sees heat.
- **Low-tech core** — open cycle, atmospheric pressure, 2 Hz, simple castings, a [hackable drivetrain](drivetrain/README.md).
- **Multiple loads** — shaft, heat, electricity, tractor, heat pump; a failed load does not strand the engine.
- **Pessimistic floor** — 5 % efficiency, 12 MJ/kg straw, 66 % casting fill. The optimistic case is upside, not the plan.
- **Graceful degradation** — if efficiency stays low, build a larger chamber; if mass is too high, raise pressure, frequency or temperature.

The full argument is in [resilience](business/resilience.md). The six improvement paths are [pressure](levers/pressure.md), [temperature](levers/temperature.md), [frequency](levers/frequency.md), [volume and weight](levers/volume-weight.md), [efficiency](levers/efficiency.md) and [insolation](levers/insolation.md).

## Start here

1. [Resilience](business/resilience.md) — why a pessimistic engine is flexible.
2. [Levers](levers/README.md) — what each improvement buys and costs.
3. [Sizing](engines/manson/sizing.md) — volumes and diameters.
4. [Fuel](engines/manson/fuel.md) — consumption and the 30 kg / 20 min feed limit.
5. [Production](production/README.md) — PLA print → sand mold → casting → lathe.

## Project map

- **Demand** — [business model](business/README.md) · [customers](business/customers.md)
- **Energy** — [straw](energy/rocket-stove/straw.md) → [rocket stove](energy/rocket-stove/README.md) · [solar](energy/solar/README.md) · [nuclear](energy/nuclear/README.md)
- **Conversion** — [M Reloaded](engines/manson/README.md) (chosen) · [Stirling Beta](engines/stirling/README.md) (studied)
- **Transmission** — [drivetrain](drivetrain/README.md) · [gear and kinetic horse](drivetrain/design.md)
- **Production** — [strategy](production/strategy.md) · [first prototype](engines/manson/costs/prototype.md) · [polar slicer](production/polar-slicer/README.md) · [binder jetting](production/binder-jetting/README.md)
- **Model** — [soft-coded levers](model/README.md) · [glossary](GLOSSARY.md)

## Cost, in one line

[Entry prototype from €25,000](business/costs.md) (prototype + gear, not the full workshop); [first engine assurance €15,000–30,000](engines/manson/costs/prototype.md); [series engine €19,999](business/costs.md#3-series-engine). The series price leaves about €3,050 gross margin at 1,000 engines/year.

## Status

This is a documented prototype project, not a certified product. The first physical engine is an **unoptimized re-try**; the 15 % efficiency and the pressurised variants are studies. See [archive](archive/README.md) for superseded assumptions and [glossary](GLOSSARY.md) for the status vocabulary.
