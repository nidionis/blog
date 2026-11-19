# Glossary

> **Status:** canonical · **Owns:** vocabulary, units, baseline assumptions · **Up:** [2Cheval](README.md)

This page is the single source for terms, units and baseline assumptions. Other pages link here instead of redefining them.

## Units

| Term | Meaning |
|---|---|
| `ch`, `cv`, `hp` | cheval-vapeur / horsepower: **1 ch = 735.5 W** |
| `kW` | 1 000 W |
| `L` | litre; 1 000 L = 1 m³ |
| `ΔT` | temperature difference between hot source and ambient, in K or °C |
| `η` | overall efficiency: mechanical output / thermal input |
| `LHV` / `PCI` | lower heating value / pouvoir calorifique inférieur, in MJ/kg |
| `bar` | 100 000 Pa; 10 bar ≈ 1 MPa |

## Terms

- **M Reloaded** — open-cycle hot-air engine, chosen for simplicity and robustness. Hub: [engines/manson](engines/manson/README.md).
- **Rocket stove** — the straw combustor that supplies heat. Hub: [energy/rocket-stove](energy/rocket-stove/README.md).
- **Stirling Beta** — a closed-cycle alternative studied separately; not the chosen engine. Hub: [engines/stirling](engines/stirling/README.md).
- **Densified straw** — compressed straw, about 250 kg/m³; loose straw is about 100 kg/m³.
- **Polar slicer** — the cylindrical/polar slicing prototype. Hub: [production/polar-slicer](production/polar-slicer/README.md).
- **Binder jetting** — sand-printing route towards aluminium parts. Hub: [production/binder-jetting](production/binder-jetting/README.md).
- **First prototype** — first physical engine; PLA print → sand mold → casting → lathe finishing. See [prototype](engines/manson/costs/prototype.md).
- **PLA printing** — large-format 3D print of the lost or reusable pattern (1.5 m³). See [prototype](engines/manson/costs/prototype.md).
- **Sand casting** — fine-sand mold (10 m³) around the pattern. See [prototype](engines/manson/costs/prototype.md).
- **Crucible** — ~3 m³ refractory vessel for molten aluminum. See [prototype](engines/manson/costs/prototype.md).
- **Solar furnace** — solar-concentration furnace using mirror-polished stainless-steel plates. See [prototype](engines/manson/costs/prototype.md).
- **Lathe finishing** — final machining at ~1.40 m diameter. See [prototype](engines/manson/costs/prototype.md).
- **Heat pump** — possible replacement for heat; €15,000–35,000. See [costs](business/costs.md#4-what-the-engine-replaces).
- **Tractor** — possible replacement for mechanical work; €25,000–60,000. See [costs](business/costs.md#4-what-the-engine-replaces).
- **Replacement cost** — cost of the item the engine replaces; price argument. See [costs](business/costs.md#4-what-the-engine-replaces).
- **Lathe machining** — 2 m lathe; series capex, amortized over thousands of engines. See [lathe machining — production cost and resale price](engines/manson/costs/lathe-machining.md).
- **Canonical** — normative page; other pages link to it.
- **Source note** — raw derivation, AI output or transcript kept for evidence; not normative.
- **Exploratory** — concept under study, not a project decision.
- **Deprecated** — kept only for history; superseded by a canonical page.

## Baseline assumptions

| Parameter | Baseline value | Used by |
|---|---:|---|
| Mechanical reference | 1 ch = 735.5 W | [fuel](engines/manson/fuel.md), [sizing](engines/manson/sizing.md) |
| Overall efficiency `η` | 5 % (15 % optimised, 20 % lab) | [thermodynamics](engines/manson/thermodynamics.md) |
| Ambient temperature | 20 °C | [thermodynamics](engines/manson/thermodynamics.md) |
| Cycle frequency `f` | 2 Hz | [sizing](engines/manson/sizing.md) |
| Temperature difference `ΔT` | 180 K — Carnot cycle at 200°C (`T_hot = 200°C`, `T_cold = 20°C`) | [sizing](engines/manson/sizing.md) |
| Air heat capacity `Cp` | 1 005 J/(kg·K) | [sizing](engines/manson/sizing.md) |
| Air density `ρ` | 1.2 kg/m³ | [sizing](engines/manson/sizing.md) |
| Straw LHV | 15 MJ/kg | [straw](energy/rocket-stove/straw.md) |
| Straw density, loose | ~100 kg/m³ | [straw](energy/rocket-stove/straw.md) |
| Straw density, densified | ~250 kg/m³ | [straw](energy/rocket-stove/straw.md) |

## Languages / Langues

- The main project tree is English-only.
- The parallel French tree rooted at `2cheval/` holds the French marketing, strategy and investor content, with redirects to the English technical articles.

## See also

- [Project map](README.md)
- [French glossary (2Cheval)](2cheval/GLOSSARY.md)
- [M Reloaded](engines/manson/README.md)
- [Costs](business/costs.md)
