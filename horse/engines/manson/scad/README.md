# Manson CAD model

> **Status:** illustrative · **Owns:** parametric piston sketch · **Up:** [Manson](../README.md) · **Lang:** EN · [FR](../../../2cheval/engines/manson/scad/README.md)

[`piston.scad`](piston.scad) is a parametric sketch, not a production drawing. It uses `inner_r = 70` mm and a geometric unit called `chink`; it is not scaled to the full-size engine.

## Configuration linked to env

Engine/material parameters are **env-driven**:

- [`../../../env/values/engine.json`](../../../env/values/engine.json) is the source of truth (efficiency, ΔT, frequency, air properties, fill ratio, density, can costing range, remelting).
- [`env.scad`](env.scad) is **generated** from env by `tools/calc.py` (`--sync`, `--update`, or default run).
- [`piston.scad`](piston.scad) includes `env.scad` and uses those values in its first-order power/mass report; sketch-specific geometry (`inner_r`, `chamber_l`, `pressure_ratio`) remains local to the sketch.

OpenSCAD prints the derived `V_c`, `V_a`, mass/power and env can assumptions in the console (`echo`).

## Files

- [`piston.scad`](piston.scad) — parametric sketch (env-configured).
- [`env.scad`](env.scad) — generated env configuration for OpenSCAD.
- [`manson.stl`](manson.stl) — exported mesh.

## Run

```bash
python3 tools/calc.py --sync   # regenerate env.scad (and compat params)
openscad engines/manson/scad/piston.scad
```

## See also

- [Sizing](../sizing.md)
- [Optimisation](../optimisation.md)
- [Recycled material / can scenarios](../../../business/recycled-material.md)
- [Soft-coded model](../../../model/README.md)
- [Manson hub](../README.md)
