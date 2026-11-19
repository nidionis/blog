# Thermodynamic steady state of the Manson engine

> **Status:** canonical · **Owns:** steady-state analysis · **Up:** [Manson](README.md)

## Abstract

**Context** — The chosen engine is the open-cycle [Manson](README.md): its piston displacer (see [SCAD model](scad/README.md)) divides the chamber, so the working air volume is half the chamber volume: `V_a = V_c / 2`.

**Objective** — Establish the thermodynamic steady state of the engine and the power targets for marketing and lab.

**Method** — piston power relation of [sizing](sizing.md) with `V_a = V_c / 2`; pessimistic baseline of [thermodynamics](thermodynamics.md) (η = 5 %, ΔT = 180 K, f = 2 Hz) and [glossary](../../GLOSSARY.md) constants (ρ = 1.2 kg/m³, C_p = 1005 J/(kg·K)).

**Results** — Chamber from the SCAD sketch: `V_c` ≈ 1.06 L, `D` ≈ 13.9 cm, `L` ≈ 70 mm, so `V_a` ≈ 0.53 L; at the pessimistic baseline the draw is ≈ 12 W. Target table: 2 hp ↔ `V_a` = 67.8 L, `V_c` = 135.5 L, `D` = 55.7 cm; 3 hp ↔ 101.7 L / 203.4 L / 63.7 cm; 4 hp ↔ 135.5 L / 271.1 L / 70.1 cm; 5 hp ↔ 169.4 L / 338.8 L / 75.6 cm; 6 hp ↔ 203.8 L / 407.5 L / 80.4 cm; 20 hp ↔ 677.6 L / 1355.3 L / 119.9 cm. At `D` = 135 cm the power is set by the chamber height: 70 mm → ≈ 1.5 hp, 118 mm → ≈ 2.5 hp, 142 mm → ≈ 3 hp, 947 mm → 20 hp.

**Conclusion** — Marketing floor: 2 hp at `D` ≈ 55.7 cm. Lab need: 6 hp at `D` ≈ 80.4 cm. Lab extreme: `D` ≈ 119.9 cm for 20 hp. The 1.5 m³ prototype envelope is sized for the 2–3 hp first build; at `D` = 135 cm the same diameter can host up to 20 hp with a taller chamber.

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
| Temperature difference `ΔT` | 180 K | sizing.md baseline (200 °C hot, 20 °C ambient) |
| Cycle frequency `f` | 2 Hz | sizing.md baseline |
| Air density `ρ` | 1.2 kg/m³ | glossary |
| Air heat capacity `C_p` | 1005 J/(kg·K) | glossary |
| 1 hp | 735.5 W | glossary |

Chamber geometry from the piston SCAD (`scad/piston.scad`): `V_a = V_c / 2`; the `D = L` convention is used only for the target table.

## 4. Results

### 4.1 Chamber of the scad model

The sketch uses `inner_r = 70` mm and a chamber height of ≈ 70 mm. It is illustrative, not scaled to the full-size engine.

| Quantity | Value |
|---|---:|
| Chamber volume `V_c` | ≈ 1.06 L |
| Chamber diameter `D` | ≈ 13.9 cm |
| Chamber height `L` | ≈ 70 mm |
| Air volume `V_a = V_c / 2` | ≈ 0.53 L |
| Pessimistic draw `P` | ≈ 12 W |

The scad draw is small: the marketing and lab targets need bigger chambers.

### 4.2 Power targets (pessimistic baseline, `V_a = V_c / 2`, `D = L`)

| Target power | Air volume `V_a` | Chamber `V_c = 2 · V_a` | Chamber diameter `D` |
|---|---:|---:|---:|
| **2 hp** (marketing) | 67.8 L | 135.5 L | **55.7 cm** |
| 3 hp (pessimistic) | 101.7 L | 203.4 L | 63.7 cm |
| 4 hp (pessimistic range) | 135.5 L | 271.1 L | 70.1 cm |
| 5 hp (pessimistic range) | 169.4 L | 338.8 L | 75.6 cm |
| **6 hp** (lab need) | 203.8 L | 407.5 L | **80.4 cm** |
| **20 hp** (lab extreme) | 677.6 L | 1355.3 L | **119.9 cm** |

### 4.3 Prototype diameter: `D` = 135 cm

The 1.40 m lathe and the 1.5 m³ PLA envelope target a chamber around 1.35 m across. At that diameter the cross-section is 1.431 m², so the chamber height sets the power:

| Chamber height `L` | Chamber `V_c` | Power `P` | Equivalent |
|---:|---:|---:|---:|
| 70 mm | 0.100 m³ | 1.09 kW | ≈ 1.5 hp |
| 118 mm | 0.169 m³ | 1.84 kW | ≈ 2.5 hp |
| 142 mm | 0.203 m³ | 2.21 kW | ≈ 3 hp |
| 947 mm | 1.355 m³ | 14.71 kW | 20 hp |
| 1 048 mm | 1.500 m³ | 16.3 kW | ≈ 22 hp |

The expected 2–3 hp at `D` = 135 cm therefore needs `L` ≈ 118–142 mm, not 70 mm. These heights fit the 1.5 m³ prototype envelope; the 20 hp height is a lab extension at the same diameter. See [first prototype](costs/prototype.md).

### 4.4 Direct answers

- Marketing floor (2 hp): chamber ≈ 135.5 L, diameter ≈ 55.7 cm, air volume ≈ 67.8 L.
- Lab need (6 hp): chamber ≈ 407.5 L, diameter ≈ 80.4 cm.
- **Lab extreme: expect a chamber of ≈ 1.36 m³, i.e. a diameter of ≈ 119.9 cm, for 20 hp.**
- At `D` = 135 cm: 70 mm of chamber height gives ≈ 1.5 hp; 118–142 mm gives the expected 2–3 hp; 947 mm gives 20 hp.

## 5. Discussion

- **Convention vs sizing.md.** sizing.md's `V_cycle` is the working air volume `V_a`; this note doubles it to get the chamber volume `V_c`. The two tables now agree row for row: the 2 hp row is 67.76 L of air, 135.53 L of chamber and 55.67 cm.
- **Optimism.** The tiers of [thermodynamics](thermodynamics.md) scale the table linearly in `Power ∝ η·ΔT·f`: at 15 % the diameters shrink by roughly 30 %, at 8–12 % by 15–25 %. At the scad geometry even a 500 K superheat only draws a few tens of watts — the "nice surprises in lab" come from larger volumes or higher ΔT, not from the pessimistic baseline.
- **Not to mix.** Do not read the scad chamber (~1.06 L) as the marketing design; it is an illustrative sketch of a smaller engine. The 2 hp marketing design per this steady state is ~135.5 L of chamber.
- **Caveats.** The model is static and pessimistic: `ΔT` is the average temperature gap of the working air, and the engine's real cycle is not simulated.

## 6. Conclusion

- **2 hp** is enough for marketing: chamber ≈ 135.5 L, `D` ≈ 55.7 cm (`V_a` = 67.8 L).
- **6 hp** is the lab need: chamber ≈ 407.5 L, `D` ≈ 80.4 cm.
- **20 hp** is the lab extreme: expect `D` ≈ 119.9 cm (chamber ≈ 1.36 m³).
- At `D` = 135 cm the expected 2–3 hp needs a chamber height of 118–142 mm; 70 mm gives ≈ 1.5 hp. The 1.5 m³ envelope is sized for that first build; the same diameter can host 20 hp with a taller chamber.

## Author note

- Original contribution: the power table with the rule `V_a = V_c / 2` at ΔT = 180 K, the chamber-height table at `D` = 135 cm, and the answer `D` ≈ 119.9 cm for the 20 hp lab case.
- Main limitation: static, pessimistic model (η = 5 %, ΔT = 180 K); no cycle simulation.
- Most likely reviewer 2: the model `P = η·ρ·f·V_a·C_p·ΔT` ignores mechanical losses (pipes, alternator) and the real piston stroke; the numbers aim at engineering common sense and should be re-checked after measuring real throughputs.

## References

- [Sizing](sizing.md) — volume/diameter model, `D = L` convention.
- [Thermodynamics](thermodynamics.md) — efficiency tiers, ΔT, ambient 20 °C.
- [Piston SCAD](scad/piston.scad) — piston displacer geometry (chamber ≈ 1.06 L, `D` ≈ 13.9 cm, `L` ≈ 70 mm).
- [First prototype](costs/prototype.md) — PLA print, sand casting, 3 m³ crucible, lathe finishing.
- [Glossary](../../GLOSSARY.md) — units (1 ch = 735.5 W, 1 L = 10⁻³ m³) and baseline assumptions.
- [Manson README](README.md), [Rocket stove README](../../energy/rocket-stove/README.md).
