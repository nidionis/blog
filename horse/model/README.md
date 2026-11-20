# Soft-coded model

> **Status:** canonical calculation source · **Owns:** baseline constants and lever sensitivity · **Up:** [2Cheval](../README.md) · **Lang:** EN · [FR](../2cheval/modele/README.md)

This folder is the single input for the numbers used in the [lever articles](../levers/README.md). It is deliberately small: no simulation, no third-party dependency, only the first-order relations the project uses for sizing and sensitivity.

## Files

- [`params.json`](params.json) — baseline constants and lever ranges. **Edit this file, not the tables.**
- [`levers.py`](levers.py) — computes the tables, checks the baseline and writes the two SVG drawings.
- `../levers/sensitivity.svg` — 2 hp chamber diameter for each lever.
- `../levers/fuel-limit.svg` — mechanical power cap versus efficiency.

## Run

```bash
python3 model/levers.py          # print the tables and regenerate the SVGs
python3 model/levers.py --check  # only verify the baseline numbers
```

The sanity checks assert the project baseline: 2 hp → `V_a` = 67.76 L, `V_c` = 135.53 L, `D` = 55.67 cm, 15 kW at 5 % and 8.83 kg/h. If a constant changes, the check and the articles must change together.

## Relations

```
P        = η · ρ · f · V_a · Cp · ΔT          (first-order air power)
V_a      = V_c / 2                           (displacer rule)
D        = (4 · V_c / π)^(1/3)               (D = L convention)
P_fuel   = η · (30 kg / 20 min) · LHV        (feed cap at 12 MJ/kg)
m_Al     = 0.66 · V_c · 2700 kg/m³           (cast chamber mass, material only)
```

The model assumes constant ambient air density. Pressure is introduced as a density multiplier, `ρ_eff = ρ · r_p`, with a pessimistic `pressure_derate`; it is a **sealed-variant** lever, not a modification of the atmospheric Manson. Temperature is a `ΔT` multiplier at constant `η`; the Carnot table is a ceiling, not a prediction.

## What the model does not do

- It does not simulate a real cycle, port timing, leakage or heat exchange.
- It does not predict efficiency; `η` is an input tier.
- It does not size the stove, the alternator or the structure.
- It does not replace a test. It keeps the documents consistent until a measurement replaces an assumption.

## See also

- [Levers](../levers/README.md) — the articles built from this model
- [Glossary](../GLOSSARY.md) — symbols and units
- [Sizing](../engines/manson/sizing.md) — the canonical power table
