# M Reloaded (Manson engine)

> **Status:** canonical hub · **Owns:** engine choice · **Up:** [Engines](../README.md) · **Lang:** EN · [FR](../../2cheval/engines/manson/README.md)

**M Reloaded** is the project name for the [Manson engine](https://moteurstirling.com/mace/manson/principes.php): open cycle, atmospheric pressure, piston displacer, chosen for simple construction and robustness. It is the only engine used by the 2 hp product.

## How it works

The engine converts heat into work by expanding air. The [efficiency](thermodynamics.md) is driven by the temperature difference between the hot source and ambient. The [combustion volume](../../energy/rocket-stove/combustion.md) affects available [power](fuel.md) but not directly the thermodynamic efficiency.

- **Sizing baseline** — 5 % overall efficiency, `ΔT` = 180 K, 2 Hz.
- **Target** — 15 % with [optimisation](optimisation.md).
- **Lab ceiling** — 20 %; not a customer promise.
- **Pressure** — atmospheric. Higher pressure is a separate sealed variant, not a tuning knob; see [pressure lever](../../levers/pressure.md).

## At a glance

| Mode | Mechanical | Thermal at 5 % | `V_c` | `D` (`D = L`) |
|---|---:|---:|---:|---:|
| Product | 2 ch ≈ 1.47 kW | 29.4 kW | 135.5 L | 55.7 cm |
| Stretch | 4 ch ≈ 2.94 kW | 58.8 kW | 271.1 L | 70.1 cm |
| Lab | 6 ch ≈ 4.41 kW | 88.3 kW | 406.6 L | 80.3 cm |
| Extreme | 20 ch ≈ 14.71 kW | 294.2 kW | 1 355.3 L | 119.9 cm |

The 20 ch extreme is exactly at the 30 kg / 20 min feed limit **at 5 %**. At 15 % the same feed allows 45 kW; the chamber and materials become the constraint. See [fuel](fuel.md) and [levers](../../levers/README.md).

## Pages

- [Sizing](sizing.md) — volumes, diameters, power table.
- [Thermodynamics](thermodynamics.md) — Carnot ceiling, efficiency tiers, `ΔT`.
- [Steady state](thermodynamic-steady.md) — check against the CAD sketch and the `D = 135 cm` geometry.
- [Fuel](fuel.md) — consumption and the 30 kg / 20 min cap.
- [Power from air](power-from-air.md) — standard MEP/airflow formulas and why the Manson is different.
- [Optimisation](optimisation.md) — port timing and displacer porosity.
- [CAD model](scad/README.md) — parametric `piston.scad`.
- [Costs](costs/README.md) — material, prototype and series.

## Studied alternative

The [Stirling Beta](../stirling/README.md) is a closed-cycle, pressurised alternative documented separately. Do not mix its assumptions with the Manson's.

## See also

- [Rocket stove](../../energy/rocket-stove/README.md)
- [Resilience](../../business/resilience.md)
- [Glossary](../../GLOSSARY.md)
- [Project map](../../README.md)
