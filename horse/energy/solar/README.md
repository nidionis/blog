# Solar heat variant

> **Status:** exploratory · **Owns:** solar heat source · **Up:** [Energy](../README.md) · **Lang:** EN · [FR](../../2cheval/energy/solaire/README.md)

Solar heat can replace straw whenever the sun is available. It does not change the engine; it changes the heat source and adds a collector and a store. The reference design keeps straw as the baseline because straw is storable and dense.

## Two temperature routes

| Route | Typical temperature | Use |
|---|---:|---|
| Flat-plate or evacuated-tube collector | 60–100 °C | preheat, domestic heat, very low `ΔT` |
| Concentrating collector (mirrors, Fresnel) | 200–800 °C | engine hot side, higher `ΔT` |
| [Solar furnace](../../engines/manson/costs/prototype.md) | > 1 000 °C | casting, materials, not continuous engine heat |

The engine's hot side is limited by its materials, not by the sun. A flat-plate collector cannot reach a useful `ΔT` for a compact engine; concentration is required for the [temperature lever](../../levers/temperature.md).

## Sizing

$$P_{th} = G \cdot A \cdot \eta_{solar}$$

At a pessimistic **250 W/m² useful** (500 W/m² irradiance × 50 % collector), a 2 hp engine at 5 % needs **118 m²** at noon. At 15 % it needs **39 m²**. A 10-minute daily run needs only a few square metres; continuous 24 h operation needs hundreds. The full table is in [insolation](../../levers/insolation.md).

## Storage and hybrid operation

- **Short run** — a few m² of collector and a small hot-water store can fuel a demonstration.
- **Continuous** — hundreds of m², or a large thermal store, or a biomass backup. At 5 %, 24 h of 2 hp is about 706 kWh thermal, roughly 12 m³ of water over a 50 K swing.
- **Hybrid** — solar preheats the stove air or the working air; straw supplies the top-up at night. The engine does not need to choose.

## Limits

Solar is intermittent, diffuse in winter, and land-hungry. It is a resilience input, not a fuel replacement for every site. The [solar furnace](../../engines/manson/costs/prototype.md) already in the prototype route is a separate, high-temperature tool.

## See also

- [Insolation lever](../../levers/insolation.md) — areas and storage numbers
- [Temperature lever](../../levers/temperature.md) — why concentration matters
- [Resilience](../../business/resilience.md) — hybrid source strategy
- [Energy hub](../README.md)
