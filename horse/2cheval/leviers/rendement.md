# Rendement — le levier multiplicateur

> **Status:** canonical · **Owns:** sensibilité au rendement global · **Up:** [Leviers](README.md) · **Lang:** FR · [EN](../../levers/efficiency.md)

Le rendement global `η` est la puissance mécanique divisée par la puissance thermique, **combusteur inclus**. C'est le seul levier qui améliore à la fois la puissance, la consommation et la taille du moteur — ce qui en fait aussi le plus difficile à obtenir.

## Loi

$$P \propto \eta \quad\text{à carburant constant} \qquad \dot m_{carburant} \propto \frac{1}{\eta} \quad\text{à puissance constante}$$

| `η` global | `D` à 2 ch | Paille à 2 ch | Plafond mécanique à 30 kg / 20 min |
|---:|---:|---:|---:|
| 5 % (base) | 55,7 cm | 8,83 kg/h | 15 kW ≈ 20,4 ch |
| 10 % | 44,2 cm | 4,41 kg/h | 30 kW ≈ 40,8 ch |
| 15 % (cible) | 38,6 cm | 2,94 kg/h | 45 kW ≈ 61,2 ch |
| 20 % (plafond labo) | 35,1 cm | 2,21 kg/h | 60 kW ≈ 81,6 ch |

La promesse client utilise **5–15 %** ; 20 % est un plafond de laboratoire, pas un argument de vente. Le palier intermédiaire 8–12 % est une version avancée, avec de meilleurs matériaux et plus d'usure.

## D'où vient le rendement

- **Combustion** — le [rocket stove](../energy/rocket-stove/README.md) doit brûler la paille complètement, avec peu d'excès d'air et peu d'imbûlés.
- **Échange thermique** — le gaz chaud doit réellement chauffer l'air de travail ; un `ΔT` sur le papier n'est pas un `ΔT` dans la chambre.
- **Distribution et remplissage** — voir [optimisation](../engines/manson/optimisation.md). Une chambre qui ne se remplit pas perd de la puissance avant la thermodynamique.
- **Étanchéité et frottement** — fuites et frottement du piston sont des pertes directes, aggravées par la pression et la vitesse.
- **Isolation** — chaque kelvin perdu avant la détente est un point de rendement perdu.

## Lecture pessimiste

Dimensionner et chiffrer à **5 %**. N'utiliser 15 % qu'après un essai mesuré, et ne jamais multiplier les meilleurs cas entre eux. Les gains sont multiplicatifs dans le modèle, mais pas indépendants dans la machine : température, pression et fréquence sollicitent les mêmes joints et matériaux.

## Pourquoi c'est un levier de résilience

Si la paille est chère ou si la limite d'alimentation bloque, le rendement libère de la marge. Si le moteur est trop lourd, le rendement réduit la chambre. Si une version n'atteint pas 15 %, la base à 5 % délivre encore les 2 ch avec une chambre plus grande. Le plancher pessimiste, c'est la résilience.

## Voir aussi

- [Thermodynamique](../engines/manson/thermodynamics.md) — Carnot et paliers
- [Carburant](../engines/manson/fuel.md) — consommation et limite d'alimentation
- [Dimensionnement](../engines/manson/sizing.md) — volume pour une puissance
- [Optimisation](../engines/manson/optimisation.md) — chemins de pertes pratiques
- [Version anglaise (dérivation)](../../levers/efficiency.md)
