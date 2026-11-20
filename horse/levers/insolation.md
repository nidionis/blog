# Insolation — the solar lever

> **Status:** exploratory lever · **Owns:** solar heat and insolation sensitivity · **Up:** [Levers](README.md) · **Lang:** EN · [FR](../2cheval/leviers/ensoleillement.md)

The engine does not care where the heat comes from. Straw is the reference because it is storable and dense, but solar heat can replace it whenever the sun is available. The lever is not the engine: it is the collector area and the storage.

## Definitions

- **Irradiance `G`** — instantaneous power per area, W/m². Clear-sky noon is about **1 000 W/m²**; a pessimistic average is **250–500 W/m²**.
- **Insolation `H`** — energy per area per day, kWh/m²/day. Temperate sunny sites: **2–6 kWh/m²/day**, with winter at the low end.
- **Collector efficiency `η_solar`** — useful heat divided by incident solar energy. Pessimistic **50 %** for a simple solar-thermal collector; concentrated systems can be higher but need tracking.

$$P_{th} = G \cdot A \cdot \eta_{solar} \qquad A = \frac{P_{th}}{G \cdot \eta_{solar}}$$

## Instantaneous aperture for 2 hp

| Engine efficiency | Thermal need | At 250 W/m² useful | At 400 W/m² | At 600 W/m² |
|---:|---:|---:|---:|---:|
| 5 % (baseline) | 29.4 kW | 118 m² | 74 m² | 49 m² |
| 15 % (target) | 9.8 kW | 39 m² | 25 m² | 16 m² |

These are **noon** areas. A 2 hp engine at 5 % needs a collector roughly the size of a small house roof; at 15 % it needs a large garage roof.

## Daily aperture and storage

| Use | Thermal energy | At 2 kWh/m²/day | At 4 kWh/m²/day |
|---|---:|---:|---:|
| 10 min at 2 hp, 5 % | 4.9 kWh | 2.5 m² | 1.2 m² |
| 10 min at 2 hp, 15 % | 1.6 kWh | 0.8 m² | 0.4 m² |
| 24 h at 2 hp, 5 % | 706 kWh | 353 m² | 176 m² |
| 24 h at 2 hp, 15 % | 235 kWh | 118 m² | 59 m² |

A short daily run is easy: a few square metres of collector can fuel a 10-minute demonstration. Continuous operation is a different project: it needs hundreds of square metres or a very large thermal store. At 5 %, storing 706 kWh in water over a 50 K swing takes about **12 m³**; at 15 % about **4 m³**. This is why the reference design keeps straw as the baseline and treats solar as a hybrid input.

## What it costs

- **Area** — the collector is the expensive part, not the engine.
- **Intermittency** — night, clouds and winter. A battery is a poor substitute for heat storage; a biomass stove is a cheap backup.
- **Temperature** — a flat-plate collector delivers 60–100 °C, not 200–800 °C. Concentrating collectors are needed for the high-`ΔT` lever. See [temperature](temperature.md).
- **Maintenance** — mirrors, tracking, dust and hail.

## Why it is a resilience lever

Solar and straw are complementary: sun in summer, stored straw in winter; solar for a short daily run, straw for continuous power. The [solar furnace](../engines/manson/costs/prototype.md) already appears in the prototype route for casting, so the project has a reason to develop solar concentration independently of the engine.

## See also

- [Solar heat](../energy/solar/README.md) — the heat-source variant
- [Temperature](temperature.md) — why concentration is needed for high `ΔT`
- [Resilience](../business/resilience.md) — hybrid source strategy
- [Model parameters](../model/params.json) — solar assumptions
