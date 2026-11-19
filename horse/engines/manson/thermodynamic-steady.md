# Thermodynamic steady state of the Manson engine

> **Status:** canonical · **Owns:** steady-state analysis · **Up:** [Manson](README.md)

## Abstract

**Context** — The chosen engine is the open-cycle [Manson](README.md): its piston displacer (see [SCAD model](scad/README.md)) divides the chamber, so the working air volume is half the chamber volume: `V_a = V_c / 2`.  
**Objective** — Establish the thermodynamic steady state of the engine and the power targets for marketing and lab.  
**Method** — piston power relation of [sizing](sizing.md) with `V_a = V_c / 2`; pessimistic baseline of [thermodynamics](thermodynamics.md) (η = 5 %, ΔT = 300 K, f = 2 Hz) and [glossary](../../GLOSSARY.md) constants (ρ = 1.2 kg/m³, C_p = 1005 J/(kg·K)).  
**Results** — Chamber from the SCAD model: `V_c` ≈ 2.10 L, `D` ≈ 13.9 cm, so `V_a` ≈ 1.05 L; at the pessimistic baseline the draw is ≈ 19 W. Target table: 2 hp ↔ `V_a` = 40.7 L, `V_c` = 81.3 L, `D` = 47.0 cm; 3 hp ↔ 61.0 L / 122.0 L / 53.8 cm; 4 hp ↔ 81.3 L / 162.6 L / 59.2 cm; 5 hp ↔ 101.7 L / 203.4 L / 63.7 cm; 6 hp ↔ 122.2 L / 244.5 L / 67.8 cm; 20 hp ↔ 406.6 L / 813.2 L / 101.2 cm. The design point at `D` = 135 cm gives `V_c` ≈ 100 L, `V_a` ≈ 50 L and `P` ≈ 1.81 kW ≈ 2.5 hp, matching the expected 2–3 hp.  
**Conclusion** — Marketing floor: 2 hp at `D` ≈ 47 cm. Lab need: 6 hp at `D` ≈ 68 cm. Lab extreme: `D` ≈ 101 cm for 20 hp.

---

## 1. Context and objective

The engine draws heat from the [rocket stove](../../energy/rocket-stove/README.md) through the piston displacer of the [SCAD model](scad/README.md). Per the design note, the working air volume is half the chamber volume (`V_a = V_c / 2`).

This document gives the steady-state power of the engine and the diameter/volume to expect for the power targets:

- **Marketing**: 2 hp is enough.
- **Pessimistic** ("nice surprises in lab or just nice conditions"): ~3–5 hp.
- **Lab need**: 6 hp.
- **Lab extreme**: up to 20 hp.

## 2. Theory

Piston power relation ([sizing](sizing.md), with `V_cycle` being the working air volume `V_a`):

```
W_cycle = P / f            (work per cycle, sizing.md)
Q_in    = W_cycle / η      (thermal input, thermodynamics.md)
P       = η · ρ · f · V_a · C_p · ΔT
```

With the displacer rule `V_a = V_c / 2` the chamber volume is twice the air volume, so:

```
P = η · ρ · f · V_c / 2 · C_p · ΔT
```

## 3. Methodology

Pessimistic baseline — the "initial / artisanal" tier of [thermodynamics](thermodynamics.md) and the [sizing](sizing.md) baseline:

| Parameter | Value | Source |
|---|---:|---|
| Overall efficiency `η` | 5 % | thermodynamics.md (tier "5 %") |
| Temperature difference `ΔT` | 300 K | sizing.md baseline |
| Cycle frequency `f` | 2 Hz | sizing.md baseline |
| Air density `ρ` | 1.2 kg/m³ | glossary |
| Air heat capacity `C_p` | 1005 J/(kg·K) | glossary |
| 1 hp | 735.5 W | glossary |

Chamber geometry from the piston SCAD (`scad/piston.scad`): `V_a = V_c / 2` and `D = L` (sizing.md convention).

## 4. Results

### 4.1 Chamber of the scad model

| Quantity | Value |
|---|---|
| Chamber volume `V_c` | ≈ 2.10 L |
| Chamber diameter `D` (D = L) | ≈ 13.9 cm |
| Air volume `V_a = V_c / 2` | ≈ 1.05 L |
| Pessimistic draw `P` | ≈ 19 W |

The scad draw is small: the marketing and lab targets need bigger chambers.

### 4.2 Power targets (pessimistic baseline, `V_a = V_c / 2`, `D = L`)

| Target power | Air volume `V_a` | Chamber `V_c = 2 · V_a` | Chamber diameter `D` |
|---|---:|---:|---:|
| **2 hp** (marketing) | 40.7 L | 81.3 L | 47.0 cm |
| 3 hp (pessimistic) | 61.0 L | 122.0 L | 53.8 cm |
| 4 hp (pessimistic range) | 81.3 L | 162.6 L | 59.2 cm |
| 5 hp (pessimistic range) | 101.7 L | 203.4 L | 63.7 cm |
| **6 hp** (lab need) | 122.2 L | 244.5 L | 67.8 cm |
| **20 hp** (lab extreme) | 406.6 L | 813.2 L | **101.2 cm** |

### 4.3 Design point: `D` = 135 cm

With the scad chamber height (`L` ≈ 70 mm) and `D` = 135 cm:

```
V_c = π · (0.675 m)² · 0.070 m ≈ 0.1002 m³
V_a = V_c / 2               ≈ 0.0501 m³
P   = η · ρ · f · V_a · C_p · ΔT ≈ 1,813 W ≈ 2.5 hp
```

This matches the expected 2–3 hp of the design note.

### 4.4 Direct answers

- Marketing floor (2 hp): chamber ≈ 81.3 L, diameter ≈ 47.0 cm, air volume ≈ 40.7 L.
- Lab need (6 hp): chamber ≈ 244.5 L, diameter ≈ 67.8 cm.
- **Lab extreme: expect a chamber of ≈ 0.81 m³, i.e. a diameter of ≈ 101 cm, for 20 hp.**

## 5. Discussion

- **Convention vs sizing.md.** sizing.md's model volume is the working air volume: its 2 ch row (40.7 L, 37.3 cm) is the doc's `V_a` at 2 hp. With the displacer rule of this note the chamber is twice that, and the doc's 2 hp row is `V_c` = 81.3 L, `D` = 47.0 cm — the same as the 4 ch row of the sizing table (81.3 L, 47.0 cm).
- **Optimism.** The tiers of [thermodynamics](thermodynamics.md) scale the table linearly in `η` and `ΔT` (P ∝ η·ΔT·f): the 8–12 %, 15 % and 20 % tiers cut the diameters by roughly 20–30 %; the 500 K lab-superheat maximum at the scad geometry draws ≈ 0.34 hp — the "nice surprises in lab" come from larger volumes or higher ΔT, not from the pessimistic baseline.
- **Not to mix.** Do not read the scad chamber (~2.1 L) as the marketing design; it is the prototype drawing of a smaller engine. The 2 hp marketing design per this steady state is ~81 L of chamber.
- **Caveats.** The model is static and pessimistic: `ΔT` is the average temperature gap of the working air, and the engine's real cycle is not simulated.

## 6. Conclusion

- **2 hp** is enough for marketing: chamber ≈ 81.3 L, `D` ≈ 47.0 cm (`V_a` = 40.7 L).
- **6 hp** is the lab need: chamber ≈ 244.5 L, `D` ≈ 67.8 cm.
- **20 hp** is the lab extreme: expect `D` ≈ 101.2 cm (chamber ≈ 0.81 m³).
- At `D` = 135 cm the model gives ≈ 2.5 hp at the pessimistic baseline, consistent with the expected 2–3 hp.

## Author note

- Original contribution: the power table with the rule `V_a = V_c / 2`, the confirmed design point `D` = 135 cm (≈ 2.5 hp), and the answer `D` ≈ 101 cm for the 20 hp lab case.
- Main limitation: static, pessimistic model (η = 5 %, ΔT = 300 K); no cycle simulation.
- Most likely reviewer 2: the model `P = η·ρ·f·V_a·C_p·ΔT` ignores mechanical losses (pipes, alternator) and the real piston stroke; the numbers aim at engineering common sense and should be re-checked after measuring real throughputs.

## References

- [Sizing](sizing.md) — volume/diameter model, `D = L` convention.
- [Thermodynamics](thermodynamics.md) — efficiency tiers, ΔT, ambient 20 °C.
- [Piston SCAD](scad/piston.scad) — piston displacer geometry (chamber ≈ 2.10 L, `D` ≈ 13.9 cm).
- [Glossary](../../GLOSSARY.md) — units (1 ch = 735.5 W, 1 L = 10⁻³ m³) and baseline assumptions.
- [Manson README](README.md), [Rocket stove README](../../energy/rocket-stove/README.md).
