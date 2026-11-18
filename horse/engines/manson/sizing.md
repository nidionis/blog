# Dimensionnement du moteur Manson / Manson sizing

> **Status:** canonical · **Owns:** volume, diameter and power table · **Up:** [Manson](README.md)

**FR** — Cette page calcule le volume balayé et le diamètre à partir de la puissance, du rendement, du ΔT et de la fréquence. Toutes les valeurs partagent les mêmes hypothèses.  
**EN** — This page derives swept volume and diameter from power, efficiency, ΔT and frequency. All values share the same assumptions.

## Hypothèses / Assumptions

Voir le [glossaire](../../GLOSSARY.md) pour les valeurs de référence / See the [glossary](../../GLOSSARY.md) for baseline values :

- Rendement global / overall efficiency : **η = 5 %**
- Écart de température / temperature difference : **ΔT = 300 K**
- Fréquence / frequency : **f = 2 Hz**
- Capacité thermique de l'air / air heat capacity : **Cp = 1 005 J/(kg·K)**
- Masse volumique de l'air / air density : **ρ = 1.2 kg/m³**
- Géométrie / geometry : cylindre avec **D = L**

## Formules / Formulas

$$P_{th} = \frac{P_m}{\eta}$$

$$\dot m = \frac{P_{th}}{C_p \cdot \Delta T}$$

$$V_{cycle} = \frac{\dot m / \rho}{f}$$

Pour un cylindre de diamètre `D` et de longueur `L = D` / For a cylinder with diameter `D` and length `L = D` :

$$V = \frac{\pi D^2}{4} \cdot D \quad\Rightarrow\quad D = \left(\frac{4V}{\pi}\right)^{1/3}$$

## Résultats / Results

| Puissance mécanique / Mechanical power | Équivalent / Equivalent | Puissance thermique / Thermal power | Débit massique / Mass flow | Volume par cycle / Volume per cycle | Diamètre / Diameter (D = L) |
|---:|---:|---:|---:|---:|---:|
| **1.47 kW** | 2 ch | 29.4 kW | 0.0976 kg/s | **40.7 L** | **37.3 cm** |
| **2.94 kW** | 4 ch | 58.8 kW | 0.1952 kg/s | **81.3 L** | **47.0 cm** |
| **5.88 kW** | 8 ch | 117.7 kW | 0.3903 kg/s | **162.6 L** | **59.2 cm** |
| **8.83 kW** | 12 ch | 176.5 kW | 0.5855 kg/s | **244.0 L** | **67.7 cm** |

Les valeurs de puissance correspondent aux deux produits (Etalon 2 ch, Swagger 4 ch) et à deux tailles supérieures.  
The power rows cover the two products (Etalon 2 ch, Swagger 4 ch) and two larger sizes.

## Notes

- Le diamètre dépend de l'hypothèse `D = L`. Un cylindre plus plat (plus grand diamètre, course plus courte) est possible ; dans ce cas, seule la relation `V = πD²L/4` change.  
  Diameter depends on `D = L`. A flatter cylinder is possible; only the volume relation changes.
- L'ancienne table `sizing.diametre.md` annonçait 126 mm pour 180 L ; elle mélangeait les unités et est archivée dans [archive/deprecated/sizing.diametre.md](../../archive/deprecated/sizing.diametre.md).
- Le débit de carburant correspondant est dans [fuel](fuel.md) / The matching fuel flow is in [fuel](fuel.md).

## Voir aussi / See also

- [Thermodynamics / Thermodynamique](thermodynamics.md)
- [Fuel / Carburant](fuel.md)
- [SCAD model / Modèle CAO](scad/README.md)
- [Nuclear variant / Variante nucléaire](../../energy/nuclear/README.md)
