# Glossaire / Glossary

> **Status:** canonical · **Owns:** vocabulary, units, baseline assumptions · **Up:** [2Cheval](README.md)

This page is the single source for terms, units and baseline assumptions. Other pages link here instead of redefining them.  
Cette page est la source unique des termes, unités et hypothèses de référence. Les autres pages renvoient ici au lieu de redéfinir.

## Unités / Units

| Term | Meaning |
|---|---|
| `ch`, `cv`, `hp` | cheval-vapeur / horsepower: **1 ch = 735.5 W** |
| `kW` | 1 000 W |
| `L` | litre; 1 000 L = 1 m³ |
| `ΔT` | temperature difference between hot source and ambient, in K or °C |
| `η` | overall efficiency: mechanical output / thermal input |
| `LHV` / `PCI` | lower heating value / pouvoir calorifique inférieur, in MJ/kg |
| `bar` | 100 000 Pa; 10 bar ≈ 1 MPa |

## Termes / Terms

- **Moteur Manson** — open-cycle hot-air engine, chosen for simplicity and robustness. Hub: [engines/manson](engines/manson/README.md).
- **Rocket stove** — the straw combustor that supplies heat. Hub: [energy/rocket-stove](energy/rocket-stove/README.md).
- **Stirling Beta** — a closed-cycle alternative studied separately; not the chosen engine. Hub: [engines/stirling](engines/stirling/README.md).
- **Densified straw** — compressed straw, about 250 kg/m³; loose straw is about 100 kg/m³.
- **Polar slicer** — the cylindrical/polar slicing prototype. Hub: [production/polar-slicer](production/polar-slicer/README.md).
- **Binder jetting** — sand-printing route towards aluminium parts. Hub: [production/binder-jetting](production/binder-jetting/README.md).
- **Canonical** — normative page; other pages link to it.
- **Source note** — raw derivation, AI output or transcript kept for evidence; not normative.
- **Exploratory** — concept under study, not a project decision.
- **Deprecated** — kept only for history; superseded by a canonical page.

## Hypothèses de référence / Baseline assumptions

| Parameter | Baseline value | Used by |
|---|---:|---|
| Mechanical reference | 1 ch = 735.5 W | [fuel](engines/manson/fuel.md), [sizing](engines/manson/sizing.md) |
| Overall efficiency `η` | 5 % (15 % optimised, 20 % lab) | [thermodynamics](engines/manson/thermodynamics.md) |
| Ambient temperature | 20 °C | [thermodynamics](engines/manson/thermodynamics.md) |
| Cycle frequency `f` | 2 Hz | [sizing](engines/manson/sizing.md) |
| Temperature difference `ΔT` | 300 K | [sizing](engines/manson/sizing.md) |
| Air heat capacity `Cp` | 1 005 J/(kg·K) | [sizing](engines/manson/sizing.md) |
| Air density `ρ` | 1.2 kg/m³ | [sizing](engines/manson/sizing.md) |
| Straw LHV | 15 MJ/kg | [straw](energy/rocket-stove/straw.md) |
| Straw density, loose | ~100 kg/m³ | [straw](energy/rocket-stove/straw.md) |
| Straw density, densified | ~250 kg/m³ | [straw](energy/rocket-stove/straw.md) |

## Langues / Languages

- Canonical pages and hubs are bilingual: a French and an English summary, plus shared tables and formulas.
- Raw source notes stay in their original language; they carry a bilingual status banner and link to the bilingual canonical page.
- Les pages canoniques et les hubs sont bilingues : un résumé français et un résumé anglais, avec des tableaux et formules partagés.
- Les notes sources restent dans leur langue d'origine ; elles portent un bandeau bilingue et renvoient à la page canonique bilingue.

## Conventions

- Canonical pages are bilingual; tables and formulas are shared to avoid duplicated data.
- Use relative Markdown links, not `[[wiki links]]`.
- Link the first mention of a concept; do not copy its table.
- When a number appears outside its canonical page, treat it as a summary and link to the source.

## See also

- [Project map](README.md)
- [Manson engine](engines/manson/README.md)
- [Costs](business/costs.md)
