# Moteur Manson : Conversion Thermomécanique

Le moteur Manson est un [moteur à air chaud](https://fr.wikipedia.org/wiki/Moteur_Manson) à cycle ouvert, choisi pour sa simplicité de construction et sa robustesse. Il transforme l'énergie thermique produite par la [chaudière](../rocket_stove/power.md) en puissance mécanique.

## Principes de Fonctionnement

Le [rendement](yield.md) du moteur est intimement lié à l'écart de température entre la source chaude et l'ambiance. Contrairement à d'autres cycles, le [volume du foyer](../rocket_stove/yield.md) influence la [puissance](power.md) disponible mais pas directement l'efficacité thermodynamique.

### Rendement Théorique (Carnot)

Le tableau suivant montre le rendement maximal théorique selon la température de la source chaude (pour une ambiance à 20 °C) :

| Température (°C) | ΔT (K) | Rendement de Carnot |
| :--- | :--- | :--- |
| 200 °C | 180 K | 38 % |
| 400 °C | 380 K | 56 % |
| 600 °C | 580 K | 66 % |
| 800 °C | 780 K | 73 % |

## Gamme de Modèles

Nous avons défini trois architectures de référence basées sur les besoins de mobilité et de travail :

| Modèle | Puissance Cible | Usage Principal | Détails |
| :--- | :--- | :--- | :--- |
| **Coursier** | 1 CV (740 W) | Véhicules légers | [Voir Puissance](power.md) |
| **Familial** | 3 CV (2,2 kW) | Transport de personnes | [Voir Sizing](sizing_volume.md) |
| **Utilitaire** | 8 CV (5,9 kW) | Travaux agricoles | [Voir Optimisation](optimisation.md) |

## Documentation Technique

- **[Analyse du Rendement](yield.md)** : Détail des pertes et calculs d'efficacité.
- **[Synthèse des Puissances](power.md)** : Relation entre consommation de paille et chevaux-vapeur.
- **[Dimensionnement du Volume](sizing_volume.md)** : Calcul de la cylindrée nécessaire par cycle.
- **[Diamètre et Sizing](sizing.diametre.md)** : Spécifications géométriques des pistons.

---
*Ce projet s'inscrit dans une démarche de [low-tech](../concept_general.md) pour une autonomie énergétique durable.*
