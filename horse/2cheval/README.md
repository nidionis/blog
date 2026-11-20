# 2Cheval — un cheval qui mange de la paille

**Un moteur thermique avec un concept : un cheval qui mange de la paille.**

**FR** · [English](../README.md)

La paille brûle dans un [rocket stove](energy/rocket-stove/README.md) ; la chaleur entraîne un [M Reloaded (Manson)](engines/manson/README.md) atmosphérique ; l'arbre délivre **2 ch** et le reste de l'énergie sort en chaleur utile. Le moteur est volontairement simple, lourd et lent. Son avantage n'est pas le rendement : c'est la **résilience**.

## Le produit en un tableau

| Mode | Mécanique | Thermique à 5 % | Rôle |
|---|---:|---:|---|
| **Produit** | **2 ch ≈ 1,47 kW** | ~29,4 kW | ce dont le marché a besoin |
| Extension | 4 ch ≈ 2,94 kW | ~58,8 kW | version optionnelle |
| Laboratoire | 6 ch ≈ 4,41 kW | ~88,3 kW | besoin d'essai |
| Extrême | 20 ch ≈ 14,71 kW | ~294 kW | à la limite 30 kg / 20 min, 5 % |

Ces chiffres sont à la **base de 5 %**. Un meilleur rendement, une température, une pression ou une fréquence plus élevées rendent la même puissance plus petite ; aucun n'est nécessaire à la promesse de 2 ch. Voir [leviers](leviers/README.md).

## Pourquoi c'est résilient

- **Multi-combustible** — combustion externe : paille, bois, granulés, charbon de bois, pétrole, chaleur solaire ou nucléaire. Le moteur ne voit que de la chaleur.
- **Cœur basse technologie** — cycle ouvert, pression atmosphérique, 2 Hz, pièces coulées simples, [transmission hackable](drivetrain/README.md).
- **Charges multiples** — arbre, chaleur, électricité, tracteur, pompe à chaleur ; une charge qui échoue ne bloque pas le moteur.
- **Plancher pessimiste** — 5 % de rendement, 12 MJ/kg de paille, 66 % de remplissage de coulée. L'optimiste est un bonus, pas le plan.
- **Dégradation gracieuse** — si le rendement reste à 5 %, on construit une chambre plus grande ; si la masse gêne, on monte pression, fréquence ou température.

L'argument complet est dans [résilience](business/resilience.md). Les six chemins sont [pression](leviers/pression.md), [température](leviers/temperature.md), [fréquence](leviers/frequence.md), [volume et poids](leviers/volume-poids.md), [rendement](leviers/rendement.md) et [ensoleillement](leviers/ensoleillement.md).

## Par où commencer

1. [Résilience](business/resilience.md) — pourquoi un moteur pessimiste est flexible.
2. [Leviers](leviers/README.md) — ce que chaque amélioration apporte et coûte.
3. [Dimensionnement](engines/manson/sizing.md) — volumes et diamètres.
4. [Carburant](engines/manson/fuel.md) — consommation et limite 30 kg / 20 min.
5. [Production](production/README.md) — impression PLA → moule sable → coulée → tour.

## Carte du projet

- **Demande** — [business](business/README.md) · [clients](business/customers.md)
- **Énergie** — [paille](energy/rocket-stove/straw.md) → [rocket stove](energy/rocket-stove/README.md) · [solaire](energy/solaire/README.md) · [nucléaire](energy/nuclear/README.md)
- **Conversion** — [M Reloaded](engines/manson/README.md) (choisi) · [Stirling Beta](engines/stirling/README.md) (étudié)
- **Transmission** — [transmission](drivetrain/README.md) · [engrenage et cheval cinétique](drivetrain/design.md)
- **Production** — [stratégie](production/strategy.md) · [premier prototype](production/prototype.md) · [polar slicer](production/polar-slicer/README.md) · [binder jetting](production/binder-jetting/README.md)
- **Modèle** — [modèle soft-coded](modele/README.md) · [glossaire](GLOSSARY.md)

## Coût, en une ligne

[Prototype d'entrée à partir de 25 000 €](business/costs.md) (prototype + engrenage, pas l'atelier complet) ; [assurance premier moteur 15 000–30 000 €](production/prototype.md) ; [moteur de série 19 999 €](business/costs.md#3-moteur-de-série). Le prix de série laisse environ 3 050 € de marge brute à 1 000 moteurs/an.

## Statut

Projet de prototype documenté, pas un produit certifié. Le premier moteur physique est un **réessai non optimisé** ; le rendement de 15 % et les variantes pressurisées sont des études. Voir [archive](archive/README.md) pour les hypothèses dépassées et le [glossaire](GLOSSARY.md) pour le vocabulaire de statut.
