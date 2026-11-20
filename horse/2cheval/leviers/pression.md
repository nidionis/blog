# Pression — le levier de densité

> **Status:** exploratory · **Owns:** sensibilité à la pression du gaz de travail · **Up:** [Leviers](README.md) · **Lang:** FR · [EN](../../levers/pressure.md)

Le Manson de base est **atmosphérique et à cycle ouvert**. La pression n'est donc pas un réglage : c'est une **autre architecture**, fermée. Cette page chiffre seulement ce que cette architecture apporterait.

## Loi

$$\rho = \frac{p}{R T} \qquad P \propto \rho \propto r_p \qquad D \propto r_p^{-1/3}$$

avec `r_p = p / p_atm`. À puissance égale, doubler la pression double la masse d'air volumique et réduit le diamètre de `2^(1/3) ≈ 1,26`.

## Chambre de 2 ch, idéal et pessimiste

La colonne pessimiste ne garde que **60 % du gain idéal** (fuites, joints, remplissage, pertes).

| Pression | `D` idéal | `D` pessimiste | `V_c` pessimiste |
|---:|---:|---:|---:|
| 1 bar (base) | 55,7 cm | 55,7 cm | 135,5 L |
| 2 bar | 44,2 cm | 47,6 cm | 84,7 L |
| 4 bar | 35,1 cm | 39,5 cm | 48,4 L |
| 8 bar | 27,8 cm | 32,1 cm | 26,0 L |

Un seul levier à la fois : rendement, température et fréquence restent à 5 %, 180 K et 2 Hz.

## Ce que cela coûte

- **Étanchéité** — carter fermé, segments ou membrane, déplaceur étanche. Une fuite annule le gain.
- **Structure** — épaisseur et brides croissent avec la pression ; la chambre peut peser plus lourd que le volume gagné.
- **Frottement et chaleur** — densité plus élevée = plus d'échanges et de pertes.
- **Sécurité** — un moteur à air chaud sous pression est un appareil sous pression : soupape, inspection, dossier de sécurité.
- **Architecture** — le Manson ouvert ne se « booste » pas. L'alternative pressurisée étudiée est le [Stirling Beta](../engines/stirling/README.md).

**Ne pas confondre les deux pressions.** Le tirage forcé du [rocket stove](../energy/rocket-stove/README.md) augmente la puissance de combustion ; il ne change pas la densité du gaz de travail.

## Lecture pessimiste

Traiter la pression comme un **chemin de compacité optionnel**, pas comme un gain promis. La base atmosphérique délivre déjà 2 ch. La pression sert si le sol ou la masse disponible ne supportent pas une chambre de 1,36 m³.

## Voir aussi

- [Puissance à partir de l'air](../engines/manson/power-from-air.md) — pourquoi la pression moyenne effective est basse
- [Stirling Beta](../engines/stirling/README.md) — l'alternative fermée étudiée
- [Volume et poids](volume-poids.md) — ce que la pression fait gagner en masse
- [Version anglaise (dérivation)](../../levers/pressure.md)
