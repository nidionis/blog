# Température — le levier ΔT

> **Status:** canonical · **Owns:** sensibilité à la température de source chaude · **Up:** [Leviers](README.md) · **Lang:** FR · [EN](../../levers/temperature.md)

Le moteur fonctionne sur un écart de température. À rendement fixe, la puissance est linéaire en `ΔT` ; le plafond de Carnot monte plus lentement. La base garde un air de travail à **200 °C chaud / 20 °C ambiant**, d'où une chambre volumineuse.

## Loi

$$P \propto \Delta T \qquad \Delta T = T_{chaud} - T_{ambiant}$$

Le rendement de Carnot `1 - T_froid / T_chaud` (en kelvin) est une borne, pas une prédiction : le cycle ouvert réel en est loin.

| Source chaude | `ΔT` | Puissance à `η` constant | `D` à 2 ch | Carnot |
|---:|---:|---:|---:|---:|
| 200 °C | 180 K | 1,00× | 55,7 cm | 38 % |
| 400 °C | 380 K | 2,11× | 43,4 cm | 56 % |
| 600 °C | 580 K | 3,22× | 37,7 cm | 66 % |
| 800 °C | 780 K | 4,33× | 34,1 cm | 73 % |

Un seul levier à la fois : le rendement reste à 5 %. En réalité, une source plus chaude peut aussi élever `η` ; ce serait un gain supplémentaire non prouvé, à ne pas inscrire au budget.

## Ce que cela coûte

- **Matériaux** — l'aluminium tient vers 200–300 °C, pas à 800 °C. Il faut acier, inox ou céramique, avec fluage, oxydation et dilatation.
- **Échangeur** — un gaz chaud ne fait pas automatiquement un air de travail chaud. Surface, débit et isolation décident du `ΔT` réel.
- **Pertes** — rayonnement et fumées augmentent avec la température ; la loi linéaire les ignore.
- **Combustion** — le [rocket stove](../energy/rocket-stove/README.md) peut être plus chaud que le moteur, mais le côté chaud doit rester dans sa limite matériau.

**Ne pas confondre source et fluide de travail.** La flamme de paille dépasse 800 °C ; le piston et la chambre du Manson, non.

## Lecture pessimiste

Dimensionner à 200 °C. Considérer 400 °C comme une version améliorée et 600–800 °C comme un sujet de laboratoire ou de moteur céramique. Le levier est réel, mais il déplace le problème de la thermodynamique vers les matériaux.

## Voir aussi

- [Thermodynamique](../engines/manson/thermodynamics.md) — table de Carnot et paliers
- [Dimensionnement](../engines/manson/sizing.md) — volumes de base
- [Carburant](../engines/manson/fuel.md) — chaleur à fournir
- [Ensoleillement](ensoleillement.md) — la concentration solaire peut atteindre ces températures
- [Version anglaise (dérivation)](../../levers/temperature.md)
