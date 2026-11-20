# Volume et poids — le levier de taille

> **Status:** canonical · **Owns:** volume, géométrie et mise à l'échelle de la masse · **Up:** [Leviers](README.md) · **Lang:** FR · [EN](../../levers/volume-weight.md)

Le moteur est une machine grande, lente et à basse pression. Le volume est la variable principale : la puissance est proportionnelle au volume d'air de travail, et la matière coulée au volume de chambre. C'est le levier que la base utilise déjà.

## Définitions

- `V_c` — volume géométrique total de la chambre (les deux chambres).
- `V_a` — volume d'air de travail, `V_a = V_c / 2` (règle du déplaceur).
- `D = L` — **convention** des tableaux, pas une règle de fabrication. Une chambre plate ou haute peut contenir le même volume.

## Puissance, volume et masse à la base

| Cible | `V_a` | `V_c` | `D` (`D = L`) | Alu coulé à 66 % | Puissance spécifique |
|---:|---:|---:|---:|---:|---:|
| 2 ch | 67,8 L | 135,5 L | 55,7 cm | 242 kg | 6,1 W/kg |
| 4 ch | 135,5 L | 271,1 L | 70,1 cm | 483 kg | 6,1 W/kg |
| 6 ch | 203,3 L | 406,6 L | 80,3 cm | 725 kg | 6,1 W/kg |
| 20 ch | 677,6 L | 1 355,3 L | 119,9 cm | 2 415 kg | 6,1 W/kg |

À technologie constante, **puissance et masse de chambre croissent ensemble**. Quatre fois la puissance demande quatre fois l'aluminium, mais seulement `4^(1/3) ≈ 1,59` fois le diamètre. C'est la loi de la racine cubique : les gros moteurs ne sont pas proportionnellement plus larges, ils sont plus lourds.

La masse est celle de la chambre coulée seule, à 66 % de remplissage. Elle exclut parois, piston, bielle, isolation, stove et alternateur : c'est une borne basse.

## Plat ou haut : le même volume

À `D = 135 cm`, la section est de 1,431 m² ; c'est la hauteur de chambre qui règle la puissance :

| Hauteur de chambre | `V_c` | Puissance à 5 % | Équivalent |
|---:|---:|---:|---:|
| 70 mm | 0,100 m³ | 1,09 kW | 1,5 ch |
| 118 mm | 0,169 m³ | 1,84 kW | 2,5 ch |
| 142 mm | 0,203 m³ | 2,21 kW | 3 ch |
| 947 mm | 1,355 m³ | 14,71 kW | 20 ch |

L'**enveloppe PLA de 1,5 m³** est une enveloppe d'impression, pas une chambre de 1,5 m³. Le premier prototype de 2–3 ch n'utilise que 118–142 mm de hauteur dans cette enveloppe ; le même diamètre peut accueillir 20 ch avec une chambre plus haute. Voir [premier prototype](../production/prototype.md).

## Le levier

- **Volume** — linéaire en puissance : facile à augmenter, coûteux en matière.
- **Masse** — linéaire en volume : la puissance spécifique reste près de 6 W/kg mécanique tant que pression, fréquence ou température ne changent pas.
- **Pression, fréquence, température** — réduisent la chambre à puissance égale, mais ajoutent joints, vitesse ou matériaux. L'optimum de masse n'est pas l'optimum de volume.

## Lecture pessimiste

Utiliser la ligne 2 ch. C'est le plus petit moteur qui tient la promesse commerciale, et ses 242 kg d'aluminium coulé sont déjà un problème de manutention à deux. Ne pas supposer un moteur léger : le projet échange de la masse contre de la simplicité.

## Voir aussi

- [Dimensionnement](../engines/manson/sizing.md) — le tableau canonique
- [Matière recyclée](../business/recycled-material.md) — masse d'aluminium et nombre de canettes
- [Pression](pression.md) · [Fréquence](frequence.md) · [Température](temperature.md) — les leviers de compacité
- [Version anglaise (dérivation)](../../levers/volume-weight.md)
