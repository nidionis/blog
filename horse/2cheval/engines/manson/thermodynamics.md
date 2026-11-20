# Thermodynamique du moteur Manson

> **Status:** canonical · **Owns:** rendement, plafond de Carnot et `ΔT` · **Up:** [M Manson](README.md) · **Lang:** FR · [EN](../../../engines/manson/thermodynamics.md)

Le Manson convertit la chaleur en travail par expansion d'air. Le rendement théorique est borné par Carnot ; les paliers réalistes vont de 5 % à 20 %. La dérivation complète est dans la [page anglaise](../../../engines/manson/thermodynamics.md).

## Rendement de Carnot

Le rendement théorique dépend surtout de l'écart de température. Pour une ambiance à **20 °C (293 K)** :

| Température chaude | `ΔT` | Carnot |
|---:|---:|---:|
| 200 °C | 180 K | 38 % |
| 400 °C | 380 K | 56 % |
| 600 °C | 580 K | 66 % |
| 800 °C | 780 K | 73 % |
| 1 000 °C | 980 K | 77 % |

C'est une **borne supérieure** : le cycle ouvert réel en est loin. Voir [levier température](../../leviers/temperature.md).

## Rendements réalistes

Quatre paliers de performance globale, combusteur inclus :

- **5 %** — objectif initial, construction artisanale ; c'est la base de tous les chiffres.
- **8–12 %** — conception avancée, meilleurs matériaux, plus d'usure.
- **15 %** — cible après optimisation et essais.
- **20 %** — plafond de laboratoire en surchauffe.

Le rendement est le seul levier qui améliore à la fois puissance, consommation et taille. Voir [levier rendement](../../leviers/rendement.md).

## `ΔT` requis par cycle

$$W_{cycle} = \frac{P_m}{f} \qquad Q_{in} = \frac{W_{cycle}}{\eta} \qquad m_{air} = \rho V_{cycle} \qquad \Delta T = \frac{Q_{in}}{m_{air} C_p}$$

Exemple à la base (2 ch, 2 Hz, 67,76 L/cycle, η = 5 %, ρ = 1,2 kg/m³, Cp = 1 005 J/(kg·K)) : `W_cycle` ≈ 735 J, `Q_in` ≈ 14,7 kJ, `m_air` ≈ 0,0813 kg, **ΔT ≈ 180 K**.

## Voir aussi

- [Dimensionnement](sizing.md) · [Carburant](fuel.md)
- [État stationnaire](../../thermodynamic-steady.md)
- [Rocket stove](../../energy/rocket-stove/README.md)
- [Glossaire](../../GLOSSARY.md) · [Version anglaise](../../../engines/manson/thermodynamics.md)
