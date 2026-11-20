# Puissance à partir du volume d'air

> **Status:** reference · **Owns:** relations puissance/volume d'air et limites · **Up:** [M Manson](README.md) · **Lang:** FR · [EN](../../../engines/manson/power-from-air.md)

Pourquoi le Manson atmosphérique a besoin d'un grand volume et d'une basse fréquence. Les formules classiques (PME, débit d'air) et leur comparaison complète sont dans la [page anglaise](../../../engines/manson/power-from-air.md).

## Formules classiques, en bref

$$P = \frac{p_{me} \times V_d \times N}{2 \times 60} \qquad \dot m_{air} = \frac{V_d \times N \times \rho \times \eta_v}{2 \times 60}$$

- `p_me` : pression moyenne effective ; essence atmosphérique 8–12 bar, diesel 7–10 bar, suralimenté 15–30 bar.
- `V_d` : cylindrée ; `N` : régime ; le facteur 2 correspond au quatre-temps.
- `η_v` : rendement volumétrique (0,8–0,95 en atmosphérique).

La relation clé est `P ∝ V_d × N × p_me` : la puissance augmente avec la cylindrée, le régime et la pression moyenne. Ce sont les leviers d'un moteur automobile.

## Pourquoi le Manson est différent

Le projet est **atmosphérique** (pas de suralimentation), à **combustion externe** (l'air de travail ne se mélange pas au carburant), avec un **piston déplaceur** (`V_a = V_c / 2`) et une fréquence de **2 Hz**. La formule PME ou la formule de débit d'air ne décrivent pas directement ce moteur ; elles servent à comparer.

**Contrôle d'ordre de grandeur.** Pour 2 ch, `V_c` = 135,5 L. À 2 Hz (120 tr/min), produire 1,47 kW via la formule PME implique `p_me` ≈ **0,11 bar**, soit environ 1 % des 8–12 bar d'un moteur essence. Le Manson n'utilise pas un cycle haute pression : il extrait le travail d'un faible `ΔT`, d'où le grand volume.

## Formule du projet

$$P = \eta \cdot \rho \cdot f \cdot V_a \cdot C_p \cdot \Delta T$$

À la base (η = 5 %, ρ = 1,2 kg/m³, f = 2 Hz, Cp = 1 005 J/(kg·K), ΔT = 180 K) : `P ≈ 21 708 × V_a` (W, `V_a` en m³).

| Cible | `V_a` | `V_c` | `D` (D = L) |
|---:|---:|---:|---:|
| 2 ch | 67,76 L | 135,53 L | 55,67 cm |
| 6 ch | 203,3 L | 406,6 L | 80,3 cm |
| 20 ch | 677,63 L | 1 355,26 L | 119,94 cm |

## Limite carburant

**30 kg / 20 min** à 12 MJ/kg donnent 300 kW thermiques, donc **15 kW ≈ 20,4 ch à 5 %**. La ligne 20 ch consomme 29,4 kg par 20 min. À 15 %, la même alimentation laisse 45 kW. La puissance retenue est `min(P_air, P_fuel)` ; voir [dimensionnement](sizing.md#limite-carburant), [carburant](fuel.md) et [levier rendement](../../leviers/rendement.md).

## Voir aussi

- [Dimensionnement](sizing.md) · [Thermodynamique](thermodynamics.md)
- [État stationnaire](../../thermodynamic-steady.md)
- [Glossaire](../../GLOSSARY.md) · [Version anglaise](../../../engines/manson/power-from-air.md)
