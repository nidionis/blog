> **Status:** canonical derivation · **Up:** [Polar grid](polar-grid.md)

Derivation of the minimum stopping radius so two beads of width `d` do not overlap near the centre.

In polar coordinates, when multiple radii converge towards the centre, the angular spacing tightens and the lines end up overlapping if they keep a constant bead width (pipe diameter $d$). To avoid over-extrusion and the nozzle crash at the centre, each radius must stop at a minimum distance from the centre (stop radius), forming triangular or trapezoidal "void" zones between them.

---

### 1. Stop radius for intermediate axes ($\pi/4, 3\pi/4$, etc.)

Let $d$ be the pipe diameter (the bead width). For the main axes, the angular spacing is $\Delta\theta = \pi/2$. The minimum stop radius so two adjacent lines do not overlap:

$$R_0 = \frac{d}{2}$$

Consider two adjacent radii separated by an angle $\alpha$ (e.g., between $0$ and $\pi/4$, $\Delta\theta = \pi/4$). The Euclidean distance $E(R)$ between two beads of width $d$ at distance $R$ from the centre is:

$$E(R) = 2R \sin\left(\frac{\Delta\theta}{2}\right)$$

To ensure the two beads of width $d$ do not overlap:

$$2R \sin\left(\frac{\Delta\theta}{2}\right) \ge d \implies R \ge \frac{d}{2 \sin\left(\frac{\Delta\theta}{2}\right)}$$

* **For the bisectrices ($\pi/4, 3\pi/4, \dots$) interleaved between the $\pi/2$ axes:** the angular gap is $\Delta\theta = \pi/4$ (45°), so:

$$R_{\pi/4} = \frac{d}{2 \sin(\pi/8)} = \frac{d}{2 \times 0{,}38268} \approx 1{,}306 \, d$$

* **For the sub-bisectrices ($\pi/8, 3\pi/8, \dots$):** the gap drops to $\Delta\theta = \pi/8$ (22.5°), so:

$$R_{\pi/8} = \frac{d}{2 \sin(\pi/16)} = \frac{d}{2 \times 0{,}19509} \approx 2{,}563 \, d$$

---

### 2. Geometric shape and mathematical sequence

This is a **geometric sequence (inverse harmonic) linked to the sine function**. Generally, if the angular step is halved at each generation $n$, the stop radius of the $n$-th series is:

$$R_n = \frac{d}{2 \sin\left(\frac{\theta_0}{2^n}\right)}$$

As $n$ increases, the stop radius increases in proportion to $1/\sin(1/2^n)$, pushing the radii further from the centre to let the geometry pass without collision.
