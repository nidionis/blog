# Pressure — the density lever

> **Status:** exploratory lever · **Owns:** working-gas pressure sensitivity · **Up:** [Levers](README.md) · **Lang:** EN · [FR](../2cheval/leviers/pression.md)

The baseline [Manson](../engines/manson/README.md) is **atmospheric and open-cycle**. Pressure is therefore not a tuning knob on the baseline engine: it is a different, sealed architecture. This page only quantifies what that architecture would buy.

## Law

For an ideal gas at constant temperature, density is proportional to pressure:

$$\rho = \frac{p}{R T} \qquad P \propto \rho \propto r_p \qquad D \propto r_p^{-1/3}$$

where `r_p = p / p_atm`. At the same power, doubling the working pressure halves the required air mass and reduces the chamber diameter by `2^(1/3) ≈ 1.26`.

## 2 hp chamber, ideal and pessimistic

The pessimistic column keeps only **60 % of the ideal gain** for leakage, seal friction, non-ideal filling and parasitic losses.

| Working pressure | Ideal `D` | Pessimistic `D` | Pessimistic `V_c` |
|---:|---:|---:|---:|
| 1 bar (baseline) | 55.7 cm | 55.7 cm | 135.5 L |
| 2 bar | 44.2 cm | 47.6 cm | 84.7 L |
| 4 bar | 35.1 cm | 39.5 cm | 48.4 L |
| 8 bar | 27.8 cm | 32.1 cm | 26.0 L |

These are **one-lever** figures: efficiency, temperature and frequency stay at the 5 %, 180 K, 2 Hz baseline.

## What it costs

- **Sealing** — a closed crankcase, piston rings or a rolling diaphragm, and a gas-tight displacer. Leakage destroys the gain.
- **Structure** — wall thickness and flange mass grow with pressure; the pressure vessel may weigh more than the volume it saves.
- **Friction and heat** — higher density increases heat transfer and parasitic losses; the 60 % derating is a warning, not a measurement.
- **Safety and code** — a pressurised hot-air engine is a pressure vessel. It needs relief, inspection and a real safety case.
- **Architecture** — the open Manson cannot simply be boosted. The studied pressurised alternative is the [Stirling Beta](../engines/stirling/README.md), not a modified Manson.

**Do not confuse the two pressures.** Forced draft in the [rocket stove](../energy/rocket-stove/README.md) raises combustion power; it does not raise the working-gas density in the engine. Only the second one is the lever above.

## Pessimistic reading

Treat pressure as an **optional compactness path**, not as a promised performance gain. The atmospheric baseline already delivers 2 hp; pressure is for a future variant when floor space or mass matters more than simplicity. It is also a resilience lever: if a site cannot handle a 1.36 m³ chamber, pressure and frequency are the two ways to shrink it.

## See also

- [Power from displaced air](../engines/manson/power-from-air.md) — why the atmospheric engine has a low mean effective pressure
- [Stirling Beta](../engines/stirling/README.md) — the studied closed, pressurised alternative
- [Volume and weight](volume-weight.md) — what pressure buys in mass
- [Model parameters](../model/params.json) — `pressure_derate`
