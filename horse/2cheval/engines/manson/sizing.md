# Dimensionnement du moteur Manson

> **Status:** canonical · **Owns:** volume, diamètre et puissance · **Up:** [M Manson](README.md) · **Lang:** FR · [EN](../../../engines/manson/sizing.md)

Cette page donne les volumes et diamètres à la **base de 5 %**. La dérivation complète et les autres paliers de rendement sont dans la [page anglaise](../../../engines/manson/sizing.md) et dans le [levier rendement](../../leviers/rendement.md).

## Hypothèses

- Rendement global **η = 5 %**.
- Écart de température **ΔT = 180 K** (`T_chaud = 200 °C`, `T_ambiant = 20 °C`).
- Fréquence **f = 2 Hz**.
- **Cp = 1 005 J/(kg·K)**, **ρ = 1,2 kg/m³**.
- Géométrie cylindrique avec **D = L** (convention de tableau).

## Formules

$$P_{th} = \frac{P_m}{\eta} \qquad \dot m = \frac{P_{th}}{C_p \cdot \Delta T} \qquad V_a = \frac{\dot m / \rho}{f}$$

$$V_c = 2 V_a = \frac{\pi D^2}{4} \cdot D \quad\Rightarrow\quad D = \left(\frac{4 V_c}{\pi}\right)^{1/3}$$

Le facteur 2 est la règle du déplaceur : l'air de travail occupe la moitié de la chambre géométrique. Voir [état stationnaire](../../thermodynamic-steady.md).

## Résultats à 5 %

<!-- calc:sizing:fr -->
| Puissance mécanique | Thermique | Débit | `V_a` | `V_c` | `D` |
|---:|---:|---:|---:|---:|---:|
| **1,47 kW** (2 ch) | 29,4 kW | 0,1626 kg/s | 67,76 L | 135,53 L | **55,67 cm** |
| **2,94 kW** (4 ch) | 58,8 kW | 0,3253 kg/s | 135,53 L | 271,05 L | **70,14 cm** |
| **4,41 kW** (6 ch) | 88,3 kW | 0,4879 kg/s | 203,29 L | 406,58 L | **80,29 cm** |
| **5,88 kW** (8 ch) | 117,7 kW | 0,6505 kg/s | 271,05 L | 542,10 L | **88,38 cm** |
| **8,83 kW** (12 ch) | 176,5 kW | 0,9758 kg/s | 406,58 L | 813,16 L | **101,16 cm** |
| **14,71 kW** (20 ch) | 294,2 kW | 1,6263 kg/s | 677,63 L | 1 355,26 L | **119,94 cm** |
<!-- /calc:sizing:fr -->

Un meilleur rendement réduit le volume en `1/η` : à 15 %, la chambre 2 ch fait environ 45 L au lieu de 135,5 L. Le diamètre ne baisse que comme la racine cubique. Voir [leviers](../../leviers/README.md).

## Limite carburant

La source de chaleur ajoute un second plafond : **30 kg de biomasse en 20 min** = 90 kg/h à **12 MJ/kg** :

$$P_{th,max} = 90 \times \frac{12\,000}{3\,600} = 300\ \text{kW} \qquad P_{m,max} = 0,05 \times 300 = 15\ \text{kW} \approx 20,4\ \text{ch}$$

La ligne 20 ch consomme **29,4 kg par 20 min**, exactement à la limite **à 5 %**. À 15 %, la même alimentation laisse 45 kW, mais la chambre et les matériaux doivent suivre. La puissance retenue est `min(P_air, P_fuel)`. Voir [carburant](fuel.md) et [levier rendement](../../leviers/rendement.md).

## Géométrie

`D = L` n'est qu'une convention. À `D = 135 cm`, 70 mm de hauteur donnent ≈ 1,5 ch, 118–142 mm donnent 2–3 ch, et 947 mm donnent 20 ch. Voir [volume et poids](../../leviers/volume-poids.md) et le [premier prototype](../../production/prototype.md).

## Voir aussi

- [Thermodynamique](thermodynamics.md)
- [État stationnaire](../../thermodynamic-steady.md)
- [CAO](scad/README.md)
- [Version anglaise](../../../engines/manson/sizing.md)
