# Analyse Coût-Poids et Énergie (Batterie Sodium-Ion)

## 1. Tableau Poids-Coût pour Scénarios d'Utilisation
*Base : Consommation de 100 W continus. Densité : 140 Wh/kg.*

| Scénario | Durée | Énergie Requise (Wh) | Poids Estimé (kg) | Coût (100 €/kWh) | Coût (50 €/kWh - Industriel) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Usage Court** | 20 min | 33,3 Wh | ~0,24 kg | 3,33 € | 1,67 € |
| **Usage Moyen** | 2 heures | 200 Wh | ~1,43 kg | 20,00 € | 10,00 € |
| **Usage Long** | 24 heures | 2 400 Wh (2,4 kWh) | ~17,14 kg | 240,00 € | 120,00 € |
| **Usage Hebdo** | 7 jours | 16 800 Wh (16,8 kWh) | ~120,00 kg | 1 680,00 € | 840,00 € |

> **Note sur le poids :** Le poids indiqué concerne uniquement les cellules de batterie. Un système complet (BMS, boîtier, câbles) ajoute environ 15 à 20 % de masse supplémentaire.

---

## 2. Coût de l'Énergie : "Cheval-Vapeur" (ch)
*Base de conversion : 1 ch = 736 W. Calcul du coût pour faire tourner 1 cheval pendant la durée indiquée.*

| Unité de Temps | Énergie Consommée (kWh) | Coût à 100 €/kWh | Coût à 50 €/kWh |
| :--- | :--- | :--- | :--- |
| **1 Minute** | 0,0123 kWh | 1,23 € | 0,61 € |
| **1 Heure** | 0,736 kWh | 73,60 € | 36,80 € |
| **1 Jour (24h)** | 17,664 kWh | 1 766,40 € | 883,20 € |
| **1 Semaine** | 123,65 kWh | 12 364,80 € | 6 182,40 € |
| **1 Mois (28j)** | 494,59 kWh | 49 459,20 € | 24 729,60 € |
| **1 An (365j)** | 6 447,36 kWh | 644 736,00 € | 322 368,00 € |

### Analyse de rentabilité
À 100 W (soit environ **0,136 ch**), vos coûts réels seront environ **7,3 fois plus faibles** que la colonne "1 cheval" ci-dessus.
*   **Coût réel pour 100W pendant 24h :** ~24,00 € (Scénario 100€/kWh) ou ~12,00 € (Scénario 50€/kWh).
*   **Avantage Sodium :** Contrairement au Lithium, le coût du sodium reste stable (matière première abondante), ce qui rend le scénario à 50 €/kWh durable sur le long terme, contrairement au lithium sujet aux fluctuations boursières.
