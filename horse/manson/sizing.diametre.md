On reprend [les volumes par cycle calculés](sizing.volumes.md) pour un moteur de Manson à **2 cycles/s**, **5 % de rendement**, **ΔT = 300 °C** :

* 3 kW → **83 L/cycle**
* 6 kW → **166 L/cycle**
* 9 kW → **249 L/cycle**

La longueur du cylindre est calculée par :

genui{"shapes_measurement_learning_block":{"type_id":"CYLINDER_VOLUME","locale_override":"fr-FR"}}

[
L=\frac{V}{\pi r^2}
]

avec :

* (V) = volume déplacé par cycle
* (r) = rayon du piston

---

## Cylindre rayon 25 cm

Rayon :

[
r=0,25,m
]

Surface :

[
S=\pi \times 0,25^2=0,196,m^2
]

| Puissance | Volume/cycle | Course nécessaire |
| --------- | -----------: | ----------------: |
| 3 kW      |         83 L |         **42 cm** |
| 6 kW      |        166 L |         **85 cm** |
| 9 kW      |        249 L |        **1,27 m** |

---

## Cylindre rayon 45 cm

Rayon :

[
r=0,45,m
]

Surface :

[
S=\pi \times0,45^2=0,636,m^2
]

| Puissance | Volume/cycle | Course nécessaire |
| --------- | -----------: | ----------------: |
| 3 kW      |         83 L |         **13 cm** |
| 6 kW      |        166 L |         **26 cm** |
| 9 kW      |        249 L |         **39 cm** |

---

## Cylindre rayon 70 cm

Rayon :

[
r=0,70,m
]

Surface :

[
S=\pi \times0,70^2=1,54,m^2
]

| Puissance | Volume/cycle | Course nécessaire |
| --------- | -----------: | ----------------: |
| 3 kW      |         83 L |        **5,4 cm** |
| 6 kW      |        166 L |       **10,8 cm** |
| 9 kW      |        249 L |       **16,2 cm** |

---

## Tableau résumé

| Rayon piston |   3 kW |    6 kW |    9 kW |
| -----------: | -----: | ------: | ------: |
|        25 cm |  42 cm |   85 cm |  127 cm |
|        45 cm |  13 cm |   26 cm |   39 cm |
|        70 cm | 5,4 cm | 10,8 cm | 16,2 cm |

On voit que pour un moteur de Manson lent à grande section, un rayon de **45 cm** donne des dimensions mécaniques assez réalistes : un moteur de **9 kW** demanderait environ **40 cm de course** avec un piston de **90 cm de diamètre**.
