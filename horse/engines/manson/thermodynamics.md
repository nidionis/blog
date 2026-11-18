# Thermodynamique du moteur Manson / Manson thermodynamics

> **Status:** canonical · **Owns:** efficiency, Carnot limit and ΔT · **Up:** [Manson](README.md)

**FR** — Le moteur Manson convertit la chaleur en travail par expansion d'air. Le rendement théorique est borné par Carnot ; les paliers réalistes vont de 5 % à 20 %.  
**EN** — The Manson engine converts heat into work by air expansion. Theoretical efficiency is bounded by Carnot; realistic tiers run from 5 % to 20 %.

## Rendement de Carnot / Carnot efficiency

Le **rendement théorique** dépend essentiellement de l'écart de température (ΔT). Le volume du foyer n'intervient pas directement dans le rendement.  
The **theoretical efficiency** depends mainly on the temperature difference (ΔT). Combustion volume does not directly affect efficiency.

Pour une ambiance à **20 °C (293 K)** / With an ambient at **20 °C (293 K)** :

| Température chaude / Hot temperature | ΔT | Rendement de Carnot / Carnot efficiency |
|---:|---:|---:|
| 200 °C | 180 °C | 38 % |
| 400 °C | 380 °C | 56 % |
| 600 °C | 580 °C | 66 % |
| 800 °C | 780 °C | 73 % |
| 1 000 °C | 980 °C | 77 % |

C'est une borne supérieure. Le cycle ouvert réel est loin de Carnot.  
This is an upper bound. The real open cycle is far from Carnot.

## Rendements réalistes / Real efficiencies

Nous considérons quatre paliers de performance globale (incluant la chaudière) / We use four overall performance tiers (including the combustor):

- **5 %** : objectif initial, construction artisanale / initial target, artisanal build.
- **8 – 12 %** : conception avancée, matériaux haute performance mais usure / advanced design, high-performance materials but wear.
- **15 %** : neuf en conditions optimales / new, optimal conditions.
- **20 %** : neuf en surchauffe laboratoire / new, laboratory superheat.

## ΔT requis par cycle / Required ΔT per cycle

À partir de la puissance mécanique `P_m`, de la fréquence `f` et du rendement `η` / From mechanical power `P_m`, frequency `f` and efficiency `η` :

$$W_{cycle} = \frac{P_m}{f}$$

$$Q_{in} = \frac{W_{cycle}}{\eta}$$

$$m_{air} = \rho \cdot V_{cycle}$$

$$\Delta T = \frac{Q_{in}}{m_{air} \cdot C_p}$$

Exemple avec les hypothèses de référence / Example with the baseline assumptions (2 ch, 2 Hz, 40.7 L/cycle, η = 5 %, ρ = 1.2 kg/m³, Cp = 1 005 J/(kg·K)) :

- `W_cycle` ≈ 735 J
- `Q_in` ≈ 14.7 kJ
- `m_air` ≈ 0.0488 kg
- **ΔT ≈ 300 K**

C'est cohérent avec le dimensionnement : voir [sizing](sizing.md). L'ancienne note qui annonçait ~1 785 K utilisait le travail à la place de la chaleur et traitait des m³ comme des kg ; elle est archivée dans [archive/deprecated/temperature.md](../../archive/deprecated/temperature.md).  
This matches the sizing model: see [sizing](sizing.md). The old note claiming ~1,785 K used work instead of heat and treated m³ as kg; it is archived.

## Voir aussi / See also

- [Sizing / Dimensionnement](sizing.md)
- [Fuel / Carburant](fuel.md)
- [Rocket stove combustion / Combustion](../../energy/rocket-stove/combustion.md)
- [Glossary / Glossaire](../../GLOSSARY.md)
