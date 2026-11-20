# Stockage électrique — le maillon faible

> **Status:** reference · **Owns:** dimensionnement et coût des batteries · **Up:** [2Cheval](../README.md) · **Lang:** FR · [EN](../../electric/README.md)

Le projet est **chaleur d'abord**, pas batterie d'abord. Une batterie sert au démarrage, au contrôle et aux courtes pointes ; c'est un mauvais moyen de stocker une journée de production. Cette page garde les chiffres batterie honnêtes.

## Le piège

La [note sodium-ion](batteries/poid.cout.euria.md) affiche une colonne « coût à 100 €/kWh ». C'est le **coût d'investissement des cellules**, pas le prix de l'électricité. Le multiplier par l'énergie consommée donne le prix d'achat de la batterie, pas le coût de fonctionnement. La note reste une source de dimensionnement, pas un modèle de coût d'usage.

## Ordre de grandeur pour 2 ch

| Usage | Énergie mécanique | Cellules à 140 Wh/kg | Capex cellules à 100 €/kWh | À 50 €/kWh |
|---|---:|---:|---:|---:|
| 10 min | 0,245 kWh | 1,8 kg | 25 € | 12 € |
| 1 h | 1,47 kWh | 10,5 kg | 147 € | 74 € |
| 24 h | 35,3 kWh | 252 kg | 3 530 € | 1 765 € |

Ajouter 15–20 % pour le BMS, le boîtier et les câbles. Une course de 10 min est facile ; 24 h, c'est une batterie de 250 kg — d'où le choix de la paille ou du stock thermique dans la conception de référence. Voir [résilience](../business/resilience.md).

## À quoi sert une batterie

- Démarrage et contrôle du moteur.
- Pontage d'une coupure courte ou d'une pointe.
- Stockage de l'électricité d'un générateur, pas de la chaleur du moteur.

Pour la chaleur, un stock d'eau chaude ou de biomasse coûte bien moins cher au kWh. Pour le travail mécanique, un volant ou le [cheval cinétique](../drivetrain/design.md) est l'option basse technologie.

## Voir aussi

- [Note sodium-ion](batteries/poid.cout.euria.md) — table source et avertissements
- [Résilience](../business/resilience.md) — pourquoi le stockage est le maillon faible
- [Transmission](../drivetrain/design.md) — stockage cinétique
- [Énergie](../energy/README.md) — sources de chaleur
- [Version anglaise](../../electric/README.md)
