# Frequency — the speed lever

> **Status:** canonical lever · **Owns:** cycle-frequency sensitivity · **Up:** [Levers](README.md) · **Lang:** EN · [FR](../2cheval/leviers/frequence.md)

The baseline runs at **2 Hz**, one cycle every half second. That is slow on purpose: the piston, displacer and ports are simple, and the engine can drive a slow shaft without a gearbox. Frequency is the easiest lever to write down and one of the hardest to make reliable.

## Law

$$P \propto f \qquad D \propto f^{-1/3}$$

At constant filling and torque, doubling the cycle rate doubles the power. For the same 2 hp, the chamber shrinks as the cube root of the frequency:

| Frequency | Cycles/min | 2 hp `V_c` | 2 hp `D` |
|---:|---:|---:|---:|
| 1 Hz | 60 | 271.1 L | 70.1 cm |
| 2 Hz (baseline) | 120 | 135.5 L | 55.7 cm |
| 4 Hz | 240 | 67.8 L | 44.2 cm |
| 8 Hz | 480 | 33.9 L | 35.1 cm |

Even 8 Hz is only 480 cycles per minute, far below a car engine. The engine stays a low-speed machine by automotive standards.

## What it costs

- **Port timing** — the intake and exhaust must fill and empty the chamber in a shorter window. This is the work described in [optimisation](../engines/manson/optimisation.md).
- **Flow losses** — pressure drop grows roughly with the square of speed; the simple `P ∝ f` law assumes the chamber still fills.
- **Wear and noise** — bearings, seals and the displacer see more cycles per hour. At 8 Hz the engine has four times the baseline's cycle count.
- **Dynamics** — a light, fast piston is harder to guide; vibration and balancing become design drivers.
- **Alternator** — a linear alternator at low frequency needs many turns; higher frequency helps the electrical side. See [linear alternator](../engines/stirling/linear-alternator.md).

## Pessimistic reading

Use 2 Hz for sizing. Treat 4 Hz as a realistic improvement and 8 Hz as a development target that needs measured filling, wear and noise. If the ports cannot keep up, the power gain disappears and the losses stay.

## Why low frequency is resilient

A slow engine tolerates imperfect combustion, dirty fuel and simple bearings. It can drive a [hackable drivetrain](../drivetrain/design.md) directly. Speed is a compactness lever, not a requirement for the 2 hp promise.

## See also

- [Sizing](../engines/manson/sizing.md) — frequency in the power relation
- [Optimisation](../engines/manson/optimisation.md) — port timing and displacer porosity
- [Volume and weight](volume-weight.md) — what a smaller chamber saves
