# Synthèse : Puissance du Moteur Manson

Détail des puissances mécaniques obtenues selon le rendement global.

## Modèles et Capacités

Le moteur est décliné en trois modèles principaux, définis par leur puissance nominale :

1. **Coursier** : 1 cheval-vapeur (740 W)
2. **Familial** : 3 chevaux-vapeur (2220 W)
3. **Utilitaire** : 8 chevaux-vapeur (5920 W)

## Influence du Volume du Foyer

Comme détaillé dans les [calculs thermiques](../rocket_stove/yield.md), la puissance mécanique dépend du volume du foyer et du rendement réel.

| Volume Foyer | Puissance thermique | Puissance mécanique (10 %) | Chevaux |
| :----------- | :------------------ | :------------------------- | :------ |
| **3 L**      | 8 kW                | 0,8 kW                     | ≈ 1 ch  |
| **25 L**     | 60 kW               | 6 kW                       | ≈ 8 ch  |
| **50 L**     | 120 kW              | 12 kW                      | ≈ 16 ch |

## Autonomie par Modèle (Recharge paille)

| Modèle | Puissance | Volume Recharge | Autonomie (à 8%) |
|:-------|----------:|----------------:|-----------------:|
| **Coursier** | 1 CV | 3 L | ~12 min |
| **Familial** | 3 CV | 9 L | ~12 min |
| **Utilitaire** | 8 CV | 27 L | ~14 min |

*Note : Les volumes de 3L, 9L et 27L de paille sont optimisés pour une fréquence de recharge régulière.*

---
Voir aussi :
- [Détail du rendement](yield.md)
- [Côté combustible](../rocket_stove/power.md)
