# Glossary and concept index

> **Status:** canonical vocabulary · **Owns:** symbols, units, baseline constants, EN/FR map · **Up:** [2Cheval](README.md) · **Lang:** EN · [FR](2cheval/GLOSSARY.md)

This page owns **symbols, units and baseline constants**. Each technical term links to its short article; the article owns the explanation and the numbers. Do not redefine a term here.

## Units and symbols

| Term | Meaning |
|---|---|
| `ch`, `cv`, `hp` | cheval-vapeur / horsepower: **1 ch = 735.5 W** |
| `kW` | 1 000 W |
| `L` | litre; 1 000 L = 1 m³ |
| `ΔT` | hot-source minus ambient temperature, in K or °C |
| `η` | overall efficiency: mechanical output / thermal input, combustor included |
| `LHV` / `PCI` | lower heating value, in MJ/kg |
| `bar` | 100 000 Pa; 10 bar ≈ 1 MPa |
| `V_c` | total geometric chamber volume (both chambers) |
| `V_a` | working air volume; `V_a = V_c / 2` (displacer rule) |
| `D = L` | cylinder convention used in the tables, not a manufacturing rule |
| `f` | cycle frequency, in Hz |
| `r_p` | working-pressure ratio `p / p_atm`; 1 = atmospheric |
| `G` | solar irradiance, W/m² (instantaneous) |
| `H` | solar insolation, kWh/m²/day (daily energy) |

## Baseline constants

| Parameter | Baseline | Used by |
|---|---:|---|
| Mechanical reference | 1 ch = 735.5 W | [fuel](engines/manson/fuel.md), [sizing](engines/manson/sizing.md) |
| Overall efficiency `η` | **5 %** (15 % target, 20 % lab ceiling, 8–12 % intermediate) | [thermodynamics](engines/manson/thermodynamics.md) |
| Ambient temperature | 20 °C | [thermodynamics](engines/manson/thermodynamics.md) |
| Cycle frequency `f` | 2 Hz | [sizing](engines/manson/sizing.md) |
| Temperature difference `ΔT` | 180 K (200 °C hot, 20 °C ambient) | [sizing](engines/manson/sizing.md) |
| Air heat capacity `Cp` | 1 005 J/(kg·K) | [sizing](engines/manson/sizing.md) |
| Air density `ρ` | 1.2 kg/m³ | [sizing](engines/manson/sizing.md) |
| Straw LHV | **12 MJ/kg** (below the 12.5–14.5 table range) | [straw](energy/rocket-stove/straw.md) |
| Straw density, loose / densified | ~100 / ~250 kg/m³ | [straw](energy/rocket-stove/straw.md) |
| Feed limit | 30 kg / 20 min = 90 kg/h | [fuel](engines/manson/fuel.md) |
| Casting fill | 66 % | [recycled material](business/recycled-material.md) |
| Can price / mass (baseline) | €0.03/can, 14 g (env-configured; down to €0.01 and 8 g) | [recycled material](business/recycled-material.md) |
| Pressure derating | 60 % of ideal gain | [pressure lever](levers/pressure.md) |

## Terms

- **M Reloaded (Manson)** — project name for the chosen open-cycle, atmospheric hot-air engine. Hub: [engines/manson](engines/manson/README.md).
- **Rocket stove** — the straw combustor that supplies heat. Hub: [energy/rocket-stove](energy/rocket-stove/README.md).
- **Fuel limit** — 30 kg / 20 min at 12 MJ/kg → 300 kW thermal → **15 kW ≈ 20.4 hp at 5 %**. At 15 % the same feed allows 45 kW. See [fuel](engines/manson/fuel.md).
- **Efficiency tiers** — 5 % baseline, 8–12 % advanced, 15 % target, 20 % lab. The customer promise is 5–15 %. See [efficiency lever](levers/efficiency.md).
- **Densified straw** — compressed straw, about 250 kg/m³; loose straw is about 100 kg/m³. See [straw](energy/rocket-stove/straw.md).
- **Stirling Beta** — closed-cycle, pressurised alternative studied separately; not the chosen engine. Hub: [engines/stirling](engines/stirling/README.md).
- **Linear alternator** — magnet/coil generator for the free-piston Stirling study, not the Manson. See [linear alternator](engines/stirling/linear-alternator.md).
- **Polar slicer** — cylindrical/polar G-code prototype. Hub: [production/polar-slicer](production/polar-slicer/README.md).
- **Binder jetting** — sand-printing route towards aluminium parts. Hub: [production/binder-jetting](production/binder-jetting/README.md).
- **First prototype** — first physical engine; PLA print → sand mold → casting → lathe finishing. See [prototype](engines/manson/costs/prototype.md).
- **Kinetic Horse** — 500 kg at 10 m/s = **25 kJ**; a low-tech energy reference. See [drivetrain](drivetrain/design.md).
- **Heat pump / tractor** — replacement references for heat and mechanical work; €15,000–35,000 and €25,000–60,000. See [costs](business/costs.md#4-what-the-engine-replaces).
- **Investment valorisation** — capex and iteration becoming asset value (tooling, molds, measurements, lower waste factor). See [investment valorisation](business/investment-valorisation.md).
- **Waste / iteration factor** — multiplier on perfect material for overpour, scrap and rework; falls with learning. See [large-piston estimate](engines/manson/costs/large-piston-estimate.md).
- **Insolation** — daily solar energy per area; not the same as instantaneous irradiance. See [insolation lever](levers/insolation.md).
- **Canonical** — normative page; other pages link to it.
- **Source note** — raw derivation, AI output or transcript kept as evidence; not normative.
- **Exploratory** — concept under study, not a project decision.
- **Archive / deprecated** — kept for history; superseded by a canonical page.

## Concept index (EN ↔ FR)

The English tree is the technical source. The French tree holds the French marketing/strategy pages plus short French sheets that link back to the English article for derivations.

| Concept | English | Français |
|---|---|---|
| Engine hub | [M Reloaded](engines/manson/README.md) | [Moteur Manson](2cheval/engines/manson/README.md) |
| Sizing | [Sizing](engines/manson/sizing.md) | [Dimensionnement](2cheval/engines/manson/sizing.md) |
| Thermodynamics | [Thermodynamics](engines/manson/thermodynamics.md) | [Thermodynamique](2cheval/engines/manson/thermodynamics.md) |
| Steady state | [Steady state](engines/manson/thermodynamic-steady.md) | [État stationnaire](2cheval/thermodynamic-steady.md) |
| Fuel | [Fuel](engines/manson/fuel.md) | [Carburant](2cheval/engines/manson/fuel.md) |
| Power from air | [Power from air](engines/manson/power-from-air.md) | [Puissance air](2cheval/engines/manson/power-from-air.md) |
| Optimisation | [Optimisation](engines/manson/optimisation.md) | [Optimisation](2cheval/engines/manson/optimisation.md) |
| CAD sketch | [SCAD](engines/manson/scad/README.md) | [CAO](2cheval/engines/manson/scad/README.md) |
| First prototype | [Prototype](engines/manson/costs/prototype.md) | [Premier prototype](2cheval/production/prototype.md) |
| Lathe series cost | [Lathe](engines/manson/costs/lathe-machining.md) | [Usinage tour](2cheval/production/usinage-tour.md) |
| Recycled material | [Recycled material](business/recycled-material.md) | [Matière recyclée](2cheval/business/recycled-material.md) |
| Rocket stove | [Rocket stove](energy/rocket-stove/README.md) | [Rocket stove](2cheval/energy/rocket-stove/README.md) |
| Straw | [Straw](energy/rocket-stove/straw.md) | [Paille](2cheval/energy/rocket-stove/straw.md) |
| Biomass LHV | [Biomass](energy/rocket-stove/biomass-calorific.md) | [Biomasse](2cheval/energy/rocket-stove/biomass-calorific.md) |
| Solar heat | [Solar](energy/solar/README.md) | [Solaire](2cheval/energy/solaire/README.md) |
| Nuclear variant | [Nuclear](energy/nuclear/README.md) | [Nucléaire](2cheval/energy/nuclear/README.md) |
| Stirling | [Stirling](engines/stirling/README.md) | [Stirling](2cheval/engines/stirling/README.md) |
| Drivetrain | [Drivetrain](drivetrain/README.md) | [Transmission](2cheval/drivetrain/README.md) |
| Polar slicer | [Polar slicer](production/polar-slicer/README.md) | [Polar slicer](2cheval/production/polar-slicer/README.md) |
| Binder jetting | [Binder jetting](production/binder-jetting/README.md) | [Binder jetting](2cheval/production/binder-jetting/README.md) |
| Resilience | [Resilience](business/resilience.md) | [Résilience](2cheval/business/resilience.md) |
| Levers hub | [Levers](levers/README.md) | [Leviers](2cheval/leviers/README.md) |
| Pressure | [Pressure](levers/pressure.md) | [Pression](2cheval/leviers/pression.md) |
| Temperature | [Temperature](levers/temperature.md) | [Température](2cheval/leviers/temperature.md) |
| Frequency | [Frequency](levers/frequency.md) | [Fréquence](2cheval/leviers/frequence.md) |
| Volume and weight | [Volume and weight](levers/volume-weight.md) | [Volume et poids](2cheval/leviers/volume-poids.md) |
| Efficiency | [Efficiency](levers/efficiency.md) | [Rendement](2cheval/leviers/rendement.md) |
| Insolation | [Insolation](levers/insolation.md) | [Ensoleillement](2cheval/leviers/ensoleillement.md) |
| Soft-coded model | [Model](model/README.md) | [Modèle](2cheval/modele/README.md) |
| Electric storage | [Electric storage](electric/README.md) | [Stockage électrique](2cheval/electric/README.md) |
| Investment valorisation | [Investment valorisation](business/investment-valorisation.md) | [Valorisation de l'investissement](2cheval/business/valorisation-investissement.md) |
| Large-piston estimate | [Large-piston estimate](engines/manson/costs/large-piston-estimate.md) | [Estimation gros piston](2cheval/engines/manson/costs/estimation-gros-piston.md) |

## Languages

- The main tree is **English** and owns the derivations, tables and code.
- The `2cheval/` tree is **French**: marketing, strategy, investors, plus short French concept sheets.
- A French sheet translates the explanation and links to the English article for the full table. Do not maintain two full copies of the same table.
- Every new concept gets one English article and one short French sheet; both are listed above.

## See also

- [Project map](README.md)
- [French glossary](2cheval/GLOSSARY.md)
- [Levers](levers/README.md)
- [Resilience](business/resilience.md)
