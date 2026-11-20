# Slow tractor and Kinetic Horse

> **Status:** exploratory · **Owns:** gear and kinetic-storage concepts · **Up:** [Drivetrain](README.md) · **Lang:** EN · [FR](../2cheval/drivetrain/design.md)

Ideas for a slow, hackable drivetrain: chainrings per axis, plus a kinetic-energy reference called **Kinetic Horse**.

## Chainrings

- One or more chainrings per axis.
- Simple interfaces, standard chains, no gearbox.
- The engine runs at 2 Hz; the drivetrain trades speed for torque.

## Kinetic Horse

A 500 kg mass at 10 m/s stores:

$$E_k = \frac{1}{2} m v^2 = \frac{1}{2} \times 500 \times 10^2 = 25\ \text{kJ}$$

That is about 17 seconds of 2 hp shaft work, or a short tractor push. It is a low-tech buffer, not a battery: no chemistry, no electronics, no rare materials.

## Why it matters

A slow, heavy drivetrain is resilient: it can be repaired in a workshop, it tolerates a stalled engine, and it can drive a [tractor](README.md)-like load directly. It is the mechanical counterpart of the [pessimistic baseline](../levers/README.md).

## See also

- [Drivetrain hub](README.md)
- [Resilience](../business/resilience.md)
- [Customer use case](../business/customers.md)
