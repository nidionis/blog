# env/ — project configuration (no hardcoded values/names/translations)

This folder is the **authoritative configuration** for the project: digital values, names, and French–English translations used by tools and derivations live here. Scripts and generated artifacts read from `env/`; do not hardcode these in code.

## Structure

```
env/
  values/                 # digital values (parameters, constants, ranges, UI metrics)
    units.json            # unit conversions and physical constants (HP_W, KELVIN, ratios, etc.)
    engine.json           # ambient conditions and baseline engine parameters
    fuels.json            # fuel properties (LHV, densities)
    targets.json          # target power rows, fuel rows, material rows, stress test
    levers.json           # lever ranges and derating factors
    checks.json           # baseline assertions/tolerances for validation
    svg.json              # SVG layout, colors, fonts, sizes
  i18n/                   # names and translations for generated outputs
    en.json               # English labels, table headers, SVG/report strings, locale
    fr.json               # French labels, table headers, SVG/report strings, locale
  concepts/               # EN↔FR concept/name mappings
    concepts.json         # glossary concept index data
```

## Source of truth and derived artifacts

- **Source of truth:** `env/values/*`, `env/i18n/*`, `env/concepts/*`
- **Derived/compat:** `model/params.json` is synchronized from env by `tools/calc.py` (`--sync`, default run, or `--update`) for compatibility with existing consumers.
- **Generated:** `levers/sensitivity.svg`, `levers/fuel-limit.svg`, and marked markdown table blocks.

## Tools

```bash
python3 tools/calc.py                 # sync compat, compute baseline, write SVGs
python3 tools/calc.py --check         # verify baseline against env/values/checks.json
python3 tools/calc.py --tables all    # print generated markdown tables
python3 tools/calc.py --update        # sync + rewrite marked blocks + substitute env refs
python3 tools/calc.py --sync          # sync derived compat files only
python3 model/levers.py --check       # compatibility wrapper
```

## Using configuration in documents

### Generated table blocks

Place markers in Markdown; `--update` recalculates the table from env values (code fences/inline code are not modified):

```md
<!-- calc:sizing:en -->
...generated table...
<!-- /calc:sizing:en -->
```

Available: `sizing:en`, `sizing:fr`, `fuel:en`, `fuel:fr`, `fuel-cap:en`, `fuel-cap:fr`, `material:en`, `material:fr`.

### Inline value/name substitutions

`--update` replaces configured references in Markdown outside code fences/inline code:

- `{{env:values.engine.baseline.eta}}` → value from env config tree
- `{{i18n:fr:tables.sizing.headers.0}}` → translated/name string from i18n

Use these for values, names, or translations that must stay synchronized with configuration.

## Editing rules

- Change numeric assumptions in `env/values/*.json`, not in scripts or hardcoded prose.
- Change labels/translations in `env/i18n/en.json` and `env/i18n/fr.json`.
- Change concept mappings in `env/concepts/concepts.json`.
- After changes: run `python3 tools/calc.py --update` and `--check`, then review affected text.

## See also

- [Model README](../model/README.md)
- [Tools: calc.py](../tools/calc.py)
- [Levers](../levers/README.md)
