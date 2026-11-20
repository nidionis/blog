# Manson CAD model

> **Status:** illustrative · **Owns:** parametric piston sketch · **Up:** [M Reloaded](README.md) · **Lang:** EN · [FR](../../../2cheval/engines/manson/scad/README.md)

[`piston.scad`](piston.scad) is a parametric sketch, not a production drawing. It uses `inner_r = 70` mm and a geometric unit called `chink`; it is not scaled to the full-size engine.

## Soft-coded parameters

The top of the file exposes the geometry and the first-order power model:

- `inner_r`, `chamber_l` — chamber radius and height in mm.
- `eta`, `delta_t_k`, `frequency_hz` — baseline efficiency, `ΔT` and cycle rate.
- `pressure_ratio` — 1 for the atmospheric baseline; >1 for a sealed variant.
- `rho_air`, `cp_air` — air properties.

OpenSCAD prints the derived `V_c`, `V_a`, chamber mass and power in the console (`echo`). The formulas match [`model/levers.py`](../../../model/levers.py). Change a number, re-render, and the sketch and the console report follow.

- [`piston.scad`](piston.scad) — parametric sketch.
- [`manson.stl`](manson.stl) — exported mesh.

Full-size volumes and diameters are in [sizing](../sizing.md); the sensitivity drawings are in [levers](../../../levers/README.md).

## Run

```bash
openscad engines/manson/scad/piston.scad
```

## See also

- [Sizing](../sizing.md)
- [Optimisation](../optimisation.md)
- [Soft-coded model](../../../model/README.md)
- [Manson hub](../README.md)
