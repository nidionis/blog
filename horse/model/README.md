# Soft-coded model

> **Status:** canonical calculation source · **Owns:** model docs and compatibility params · **Up:** [2Cheval](../README.md) · **Lang:** EN · [FR](../2cheval/modele/README.md)

Configuration is centralized in **[`env/`](../env/README.md)** (values, i18n/translations, concept mappings). [`params.json`](params.json) in this folder is a **derived compatibility file** synchronized from `env/` by `tools/calc.py`. Calculation scripts are consolidated in [`tools/calc.py`](../tools/calc.py).

## Source of truth

- **Values:** `env/values/*.json` (units/constants, engine baseline, fuels, targets, levers, checks, SVG config)
- **Names/translations:** `env/i18n/en.json`, `env/i18n/fr.json`
- **Concept mappings:** `env/concepts/concepts.json`
- **Derived compat:** `model/params.json` (synced automatically)

## Run

```bash
python3 tools/calc.py                 # sync compat, print baseline, write SVGs
python3 tools/calc.py --check         # verify baseline (from env/values/checks.json)
python3 tools/calc.py --tables all    # print generated markdown tables
python3 tools/calc.py --update        # sync + rewrite marked <!-- calc:... --> blocks + {{env:...}} refs
python3 tools/calc.py --sync          # sync derived compat files only

# compatibility
python3 model/levers.py
python3 model/levers.py --check
```

## Generated/configured outputs

- Table blocks: `sizing:en`, `sizing:fr`, `fuel:en`, `fuel:fr`, `fuel-cap:en`, `fuel-cap:fr`, `material:en`, `material:fr`
- Inline substitutions outside code: `{{env:values.engine.baseline.eta}}`, `{{i18n:fr:...}}` (resolved on `--update`)
- SVGs and `model/params.json` are regenerated from env.

## Relations

```
P        = η · ρ · f · V_a · Cp · ΔT          (first-order air power)
V_a      = V_c / 2                           (displacer rule)
D        = (4 · V_c / π)^(1/3)               (D = L convention)
P_fuel   = η · (30 kg / 20 min) · LHV        (feed cap at 12 MJ/kg)
m_Al     = 0.66 · V_c · 2700 kg/m³           (cast chamber mass, material only)
```

If a parameter, name, or translation changes, edit `env/`, run `--update`/`--check`, and review affected prose.

## See also

- [env/ configuration](../env/README.md)
- [Levers](../levers/README.md)
- [Sizing](../engines/manson/sizing.md) · [Fuel](../engines/manson/fuel.md) · [Recycled material](../business/recycled-material.md)
- [Glossary](../GLOSSARY.md)
