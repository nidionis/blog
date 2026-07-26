# Moteur Manson : Conversion Thermomécanique

Le moteur Manson est un [moteur à air chaud](https://fr.wikipedia.org/wiki/Moteur_Manson) à cycle ouvert,   
choisi pour sa simplicité de construction et sa robustesse.  
Il transforme l'énergie thermique produite par la [chaudière](../rocket_stove/power.md).

## Principes de Fonctionnement

Le [rendement](yield.md) du moteur est intimement lié à l'écart de température entre la source chaude et l'ambiance.  
Contrairement à d'autres cycles, le [volume du foyer](../rocket_stove/yield.md) influence la [puissance](power.md) disponible mais pas directement l'efficacité thermodynamique.
Nous pensons atteindre au moins 15% avec quelques [optimisations](optimisation.md) dans les meilleures conditions.
Et attendons 5% de rendement pour des conditions moins bonnes (ex: une source chaude à 400 °C.
Pour un moteur de [diametre](diameter.md) ~50 cm et de [volume](sizing_volume.md) ~250 L.

### Rendement Théorique (Carnot)

Le tableau suivant montre le rendement maximal théorique selon la température de la source chaude (pour une ambiance à 20 °C) :

| Température (°C) | ΔT (K) | Rendement de Carnot |
| :--- | :--- | :--- |
| 200 °C | 180 K | 38 % |
| 400 °C | 380 K | 56 % |
| 600 °C | 580 K | 66 % |
| 800 °C | 780 K | 73 % |

s
## Documentation Technique

- **[Analyse du Rendement](yield.md)** : Détail des pertes et calculs d'efficacité.
- **[Synthèse des Puissances](power.md)** : Relation entre consommation de paille et chevaux-vapeur.
- **[Dimensionnement du Volume](sizing_volume.md)** : Calcul de la cylindrée nécessaire par cycle.
- **[Diamètre et Sizing](sizing.diametre.md)** : Spécifications géométriques des pistons.

---
*Ce projet s'inscrit dans une démarche de low-tech pour une autonomie énergétique durable.*
