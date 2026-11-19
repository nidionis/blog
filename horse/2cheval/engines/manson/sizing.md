# Dimensionnement du moteur Manson — Version française (sous-projet 2Cheval)

> **Status:** canonical · **Owns:** volume, diameter and power table · **Up:** [M Reloaded](README.md)

Cette page calcule le volume et le diamètre à partir de la puissance, du rendement, du ΔT et de la fréquence. Toutes les valeurs partagent les mêmes hypothèses.

## Hypothèses

Voir le [glossaire](../../../GLOSSARY.md) pour les valeurs de référence :

- Rendement global : **η = 5 %** (tier initial, voir [thermodynamics](thermodynamics.md)).
- Écart de température : **ΔT = 180 K** — cycle de Carnot à 200°C : `T_hot = 200°C`, `T_cold = 20°C` (ambiant, voir [thermodynamics](thermodynamics.md), tableau 200 °C → 180 °C, rendement de Carnot 38 %).
- Fréquence : **f = 2 Hz**
- Capacité thermique de l'air : **Cp = 1 005 J/(kg·K)**
- Masse volumique de l'air : **ρ = 1.2 kg/m³**
- Géométrie : cylindre avec **D = L**

## Formules

$$P_{th} = \frac{P_m}{\eta}$$

$$\dot m = \frac{P_{th}}{C_p \cdot \Delta T}$$

$$V_{cycle} = \frac{\dot m / \rho}{f}$$

Pour un cylindre de diamètre `D` et de longueur `L = D` :

$$V = \frac{\pi D^2}{4} \cdot D \quad\Rightarrow\quad D = \left(\frac{4V}{\pi}\right)^{1/3}$$

## Résultats

2 ch = marché, 6 ch = besoin en laboratoire, 20 ch = extrême en laboratoire.

| Puissance mécanique | Puissance thermique | Débit massique | Volume d'air V_cycle | Volume de la chambre V_c = 2·V_cycle | Diamètre (D = L) |
|---:|---:|---:|---:|---:|---:|
| **1.47 kW** | 2 ch | 29.4 kW | 0.1626 kg/s | 67.76 L | 135.53 L | **55.67 cm** |
| **2.94 kW** | 4 ch | 58.8 kW | 0.3253 kg/s | 135.53 L | 271.05 L | **70.14 cm** |
| **4.42 kW** | 6 ch | 88.5 kW | 0.4890 kg/s | 203.75 L | 407.50 L | **80.35 cm** |
| **5.88 kW** | 8 ch | 117.7 kW | 0.6506 kg/s | 271.10 L | 542.20 L | **88.38 cm** |
| **8.83 kW** | 12 ch | 176.6 kW | 0.9762 kg/s | 406.76 L | 813.52 L | **101.18 cm** |
| **14.71 kW** | 20 ch | 294.2 kW | 1.6263 kg/s | 677.63 L | 1355.26 L | **119.94 cm** |

Le volume d'air (`V_cycle`) est la moitié du volume de la chambre : règle du displaceur (voir [Thermodynamic steady state](../../thermodynamic-steady.md)).

## Voir aussi

- [Thermodynamics](thermodynamics.md)
- [Stray state FR](../../thermodynamic-steady.md)
- [Scad model](scad/README.md)
