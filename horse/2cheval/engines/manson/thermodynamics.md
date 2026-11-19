# Thermodynamique du moteur Manson — Version française (sous-projet 2Cheval)

> **Status:** canonical · **Owns:** efficiency, Carnot limit and ΔT · **Up:** [README](README.md)

Le moteur Manson convertit la chaleur en travail par expansion d'air. Le rendement théorique est borné par Carnot ; les paliers réalistes vont de 5 % à 20 %.

## Rendement de Carnot

Le **rendement théorique** dépend essentiellement de l'écart de température (ΔT). Le volume du foyer n'intervient pas directement dans le rendement.

Pour une ambiance à **20 °C (293 K)** :

| Température chaude | ΔT | Rendement de Carnot |
|---:|---:|---:|
| 200 °C | 180 °C | 38 % |
| 400 °C | 380 °C | 56 % |
| 600 °C | 580 °C | 66 % |
| 800 °C | 780 °C | 73 % |
| 1 000 °C | 980 °C | 77 % |

C'est une borne supérieure. Le cycle ouvert réel est loin de Carnot.

## Rendements réalistes

Nous considérons quatre paliers de performance globale (incluant la chaudière) :

- **5 %** : objectif initial, construction artisanale.
- **8 – 12 %** : conception avancée, matériaux haute performance mais usure.
- **15 %** : neuf en conditions optimales.
- **20 %** : neuf en surchauffe laboratoire.

## ΔT requis par cycle

À partir de la puissance mécanique `P_m`, de la fréquence `f` et du rendement `η` :

$$W_{cycle} = \frac{P_m}{f}$$

$$Q_{in} = \frac{W_{cycle}}{\eta}$$

$$m_{air} = \rho \cdot V_{cycle}$$

$$\Delta T = \frac{Q_{in}}{m_{air} \cdot C_p}$$

Exemple avec les hypothèses de référence (2 ch, 2 Hz, 67,76 L/cycle, η = 5 %, ρ = 1.2 kg/m³, Cp = 1 005 J/(kg·K)) :

- `W_cycle` ≈ 735 J
- `Q_in` ≈ 14.7 kJ
- `m_air` ≈ 0.0813 kg
- **ΔT ≈ 180 K**

Voir aussi : [Sizing](sizing.md), [État stationnaire FR](../../thermodynamic-steady.md), [Fuel](fuel.md), [Rocket stove](../../../energy/rocket-stove/README.md), [Glossaire](../../../GLOSSARY.md).
