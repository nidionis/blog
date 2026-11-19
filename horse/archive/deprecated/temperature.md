# Thermodynamic Cycle Analysis: Delta T Calculation

> **Status:** deprecated · **Superseded by:** [manson/thermodynamics.md](../../engines/manson/thermodynamics.md)

This note treats work as heat and m³ as kg. It is kept for history only.

## 1. Objective

Determine the required temperature difference ($\Delta T$) per cycle to generate a specific mechanical power output, given a simplified geometric model and target horsepower.

## 2. Parameters & Constants

| Parameter | Symbol | Value | Unit | Notes |
| :--- | :---: | :---: | :--- | :--- |
| **Target Power** | $P$ | $2$ | hp | Total output |
| **Frequency** | $f$ | $2$ | Hz | Cycles per second |
| **Work per Cycle** | $W_{cycle}$ | $1$ | hp/cycle | Derived: $2 \text{ hp} / 2 \text{ Hz}$ |
| **Work (SI)** | $W_{SI}$ | $\approx 735$ | J | $1 \text{ hp} \approx 735.5 \text{ W}$ |
| **Radius** | $r$ | $64$ | cm | $0.64 \text{ m}$ |
| **Specific Heat** | $C$ | $1.0$ | — | Normalized coefficient (assumed) |
| **Mass Factor** | $m$ | — | — | Derived from Volume geometry |

## 3. Geometric Model

The system volume is approximated based on the radius ($r$) using a spherical model:

$$ V \approx r^3 \cdot \pi $$

*   **Radius:** $0.64 \text{ m}$
*   **Calculation:**
    $$ V \approx (0.64)^3 \cdot \pi \approx 0.823 \text{ m}^3 $$

> **Note:** The formula divides this volume by 2, implying an effective mass or working volume of $V/2$.

## 4. Thermodynamic Calculation

The heat energy required to achieve the temperature change is $Q = m \cdot C \cdot \Delta T$, where $Q$ corresponds to the work energy required per cycle ($735 \text{ J}$).

Solving for $\Delta T$:

$$ \Delta T = \frac{E_{cycle}}{m \cdot C} $$

with effective mass $m \propto \frac{V}{2}$:

$$ \Delta T = \frac{735}{\frac{0.64^3 \cdot \pi}{2}} $$

Step by step:

1.  **Numerator (energy):** $735 \text{ J}$
2.  **Denominator (geometric factor):** $0.64^3 \approx 0.262$; $\times \pi \approx 0.8235$; $\div 2 \approx 0.4118$
3.  **Final division:** $\Delta T = 735 / 0.4118$

## 5. Result

$$ \Delta T \approx 1,785 \text{ K} $$

### Conclusion

To generate **1 horsepower per cycle** at **2 Hz** with a system radius of **64 cm**, a temperature differential of approximately **1,785°C** is required.

Note: 60 Hz estimated at 30 °C using euria.

---

*Generated based on user-defined geometric constraints. Real-world applications require specific gas constants, pressure data, and efficiency corrections.*
