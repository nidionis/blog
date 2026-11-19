# Linear alternator for the Stirling study

> **Status:** exploratory summary · **Owns:** linear-alternator ranges · **Up:** [Stirling](README.md)

This applies to a free-piston Stirling with a linear alternator, not to the Manson.

## Magnets and mover

- NdFeB **N42–N52**; use SH/UH/EH grades or SmCo if the magnets exceed ~80 °C.
- Magnet outer diameter **40–150 mm**, thickness **5–20 mm** for the 1–2 kW class.
- Air gap **0.5–1.5 mm**; this is the tightest mechanical constraint.
- Mover mass **5–20 kg**; it participates in the resonant mass.
- Stroke **100–200 mm** for the 1–2 kW class.
- Halbach arrangement can gain ~20–30 % flux but complicates assembly.

## Coils

- Generator: **500–5 000 turns per phase** typical; **3 000–6 000+** for >100 V at 2 Hz.
- Conductor **0.5–4 mm²** (≈ AWG 20–12); Litz is not mandatory at 2–10 Hz.
- Coreless stator avoids cogging, at the cost of weaker coupling; a laminated iron core needs careful slot design.
- Displacer coil: **200–600 turns**, 10–50 N target force, driven with a phase lead around 90°.

## Control

At 2 Hz and 1–2 kW, the induced voltage is low and the current is high, so Joule losses matter. Wind several independent sections along the stroke and connect them in series; use active load control as a virtual gearbox to keep the oscillation stable.

## See also

- [Beta sizing](beta-sizing.md)
- [Raw coil estimation](notes/coil-estimation.md)
- [Vibration references](notes/vibrating.md)
- [Stirling hub](README.md)
