# Investment valorisation

> **Status:** concept · **Owns:** capex, iteration and learning as asset value · **Up:** [Business](README.md) · **Lang:** EN · [FR](../2cheval/business/valorisation-investissement.md)

**Investment valorisation** is the process by which spending on tools, molds, iterations and measurements becomes project value: lower unit cost, lower risk, reproducible geometry and know-how. In a pessimistic first build, money buys uncertainty; in later builds, the same investment buys margin.

## What is valorised

| Investment | Asset created | Effect on unit cost |
|---|---|---|
| Workshop / tooling (lathe, printer, furnace, CNC rails) | production capacity | amortized over `N` units; low volume is the [failing scenario](../archive/scenarios/lathe-low-volume.md) |
| Molds, patterns, PLA prints | reusable geometry | fewer re-tries, faster iteration |
| Casting and machining iterations | measured tolerances, scrap reduction | waste factor falls (e.g. ×4 → ×2) |
| Tests and instrumentation | validated `η`, `f`, `ΔT`, sealing | smaller engine for same power via [levers](../levers/README.md) |
| Documentation and model | [soft-coded parameters](../model/README.md) | consistent decisions, transferable build |

## Pessimistic path

| Stage | Typical waste / risk | Valorisation action |
|---|---|---|
| First re-try | high scrap, unknown geometry, ×3–4 material equivalent | cap the risk: **€15,000–30,000** assurance for the first engine |
| Validated prototype | geometry known, process repeatable | freeze pattern, measure efficiency, reduce rework |
| Small series | tooling amortized, stable yield | spread fixed costs, keep pessimistic charges |
| Series | learning curve, lower waste | target lower unit cost without changing the 2 hp promise |

The [large-piston worked example](../engines/manson/costs/large-piston-estimate.md) shows the same logic on a single large component: perfect material is cheap, but the first isolated build pays for waste, process and margin.

## Link to resilience

Valorisation is economic resilience: if the first build is expensive, the project still owns tools, molds and data. If one lever fails technically, another can compensate; if one unit is costly, the next can be cheaper because the investment is already made. See [resilience](resilience.md) and [costs](costs.md).

## See also

- [Costs](costs.md) — central roll-up
- [First prototype](../engines/manson/costs/prototype.md)
- [Large-piston estimate](../engines/manson/costs/large-piston-estimate.md)
- [Lathe model](../engines/manson/costs/lathe-machining.md)
- [Production strategy](../production/strategy.md)
- [French version](../2cheval/business/valorisation-investissement.md)
