# Energy cost and weight analysis (Sodium-ion battery)

> **Status:** source note · **Not normative** · **Correction:** the cost columns are **cell capital cost**, not electricity price. See [electric storage](../README.md) for the reading.

## 1. Weight-cost table for usage scenarios
*Base: 100 W continuous consumption. Density: 140 Wh/kg. Costs are cell capex at the stated €/kWh.*

| Scenario | Duration | Required energy (Wh) | Estimated weight (kg) | Cell capex (100 €/kWh) | Cell capex (50 €/kWh - industrial) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Short use** | 20 min | 33.3 Wh | ~0.24 kg | 3.33 € | 1.67 € |
| **Medium use** | 2 hours | 200 Wh | ~1.43 kg | 20.00 € | 10.00 € |
| **Long use** | 24 hours | 2 400 Wh (2.4 kWh) | ~17.14 kg | 240.00 € | 120.00 € |
| **Fortnightly use** | 7 days | 16 800 Wh (16.8 kWh) | ~120.00 kg | 1 680.00 € | 840.00 € |

> **Weight note:** The weight indicated concerns only the battery cells. A complete system (BMS, housing, cables) adds about 15–20 % of additional mass.

---

## 2. Cell capex for one "horsepower" (ch)
*Conversion base: 1 ch = 736 W. The amounts below are the cost of buying the cells, not the price of the energy they deliver.*

| Time unit | Energy consumed (kWh) | Cell capex at 100 €/kWh | Cell capex at 50 €/kWh |
| :--- | :--- | :--- | :--- |
| **1 minute** | 0.0123 kWh | 1.23 € | 0.61 € |
| **1 hour** | 0.736 kWh | 73.60 € | 36.80 € |
| **1 day (24h)** | 17.664 kWh | 1 766.40 € | 883.20 € |
| **1 week** | 123.65 kWh | 12 364.80 € | 6 182.40 € |
| **1 month (28j)** | 494.59 kWh | 49 459.20 € | 24 729.60 € |
| **1 year (365j)** | 6 447.36 kWh | 644 736.00 € | 322 368.00 € |

### Scale check
At 100 W (about **0.136 ch**), the cell capex is about **7.3 times lower** than the “1 horse” column: ~24 € for 24 h at 100 €/kWh, or ~12 € at 50 €/kWh. This is still capital cost, not operating cost.

* **Sodium advantage:** unlike lithium, sodium cost remains stable (abundant raw material), making the 50 €/kWh scenario durable over the long term. That does not make a battery cheaper than a straw store for heat.
