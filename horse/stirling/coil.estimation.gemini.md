Voici une analyse approfondie et les plages de paramètres (ranges) recommandées pour la conception des bobines et des aimants de votre moteur/générateur Stirling de type Beta à piston libre.

L'enjeu majeur avec un alternateur linéaire couplé à un moteur Stirling (particulièrement s'il fonctionne à des fréquences aussi basses que 2 Hz) est de maximiser la densité de flux magnétique pour compenser la faible vitesse de déplacement du piston, tout en évitant de bloquer la mécanique par des forces magnétiques indésirables (cogging torque).

---

## 1. Conception du Circuit Magnétique (Aimants et Piston)

Le piston moteur est ici la pièce en mouvement (mover). Sa masse est critique car elle participe, avec la pression du gaz, à la fréquence de résonance du système.

* **Matériau Magnétique :**
* **Néodyme-Fer-Bore (NdFeB) :** Grades **N42 à N52**. C'est le standard pour maximiser le champ magnétique ($B_r$ de $1,3$ à $1,45\text{ T}$).
* *Note thermique :* Assurez-vous que l'alternateur est situé dans la zone froide du Stirling. Si la température au niveau des aimants dépasse 80°C, privilégiez des aimants haute température (grades finissant par SH, UH, EH) ou passez au **Samarium-Cobalt (SmCo)**, bien que ce dernier soit plus fragile et coûteux.


* **Dimensions des aimants cylindriques/annulaires :**
* **Diamètre extérieur :** **40 mm à 150 mm** (dépendant de l'alésage de votre cylindre de puissance).
* **Épaisseur par aimant :** **5 mm à 20 mm**. Des aimants plus épais évitent la désaimantation sous forte charge, mais augmentent drastiquement la masse mobile.


* **Topologie Magnétique :**
* **Empilement à pôles alternés (N-S / S-N) :** C'est l'approche classique. Les aimants sont séparés par des disques polaires en fer doux (épaisseur 3 à 10 mm) qui redirigent le flux radialement vers les bobines.
* **Réseau de Halbach cylindrique (Avancé) :** Oriente le champ magnétique presque exclusivement vers l'extérieur (vers les bobines), augmentant le flux de ~20 à 30% et permettant de se passer d'un noyau de fer central lourd.


* **Entrefer (Air gap) :**
* **0,5 mm à 1,5 mm.** C'est l'un des paramètres les plus stricts. Plus l'entrefer est grand, plus le champ magnétique s'effondre. Cela exige un guidage mécanique (paliers secs ou aérostatiques) extrêmement rigoureux.



---

## 2. Conception du Stator (Bobines Génératrices et Motrices)

Dans votre configuration, vous avez deux sous-systèmes électriques : une bobine génératrice (récupération d'énergie sur le piston) et une bobine motrice (pilotage du déplaceur).

### A. Bobine Génératrice (Piston Moteur)

Puisque la tension induite ($E$) dépend de la vitesse de variation du flux ($E = N \cdot \frac{d\Phi}{dt}$), une faible fréquence (ex. 2 Hz) force à compenser par un nombre de spires gigantesque et des aimants très puissants.

* **Section du conducteur :**
* **0,5 mm² à 4,0 mm²** (diamètre de fil de 0,8 mm à 2,2 mm, équivalent AWG 20 à AWG 12).
* *Type de fil :* Pour une fréquence de 2 à 10 Hz, un fil de cuivre émaillé standard (Grade 2, tenue à 200°C) est suffisant ; l'effet de peau est négligeable à ces basses fréquences, le fil de Litz n'est donc pas strictement obligatoire ici, bien qu'il facilite le bobinage des fortes sections.


* **Nombre de spires ($N$) :**
* **Plage typique : 500 à 5000 spires** par phase. Pour atteindre plus de 100V à très basse vitesse, vous serez dans la fourchette haute (3000-5000), ce qui augmentera l'inductance de la bobine et sa résistance interne ($R_{int}$).


* **Présence de Fer au Stator (Coreless vs. Iron Core) :**
* *Sans fer (Coreless / Air Core) :* La bobine est noyée dans de l'époxy. **Avantage majeur :** Zéro "force de détente" (cogging torque). Le piston ne subit pas d'attraction parasite, ce qui est vital pour ne pas bloquer un moteur Stirling à faible inertie. **Inconvénient :** Le couplage magnétique est faible, nécessitant encore plus d'aimants.
* *Avec fer (Ferromagnétique feuilleté) :* Le flux est maximisé, mais les aimants vont "cranter" face aux dents du stator. Cela nécessite un design d'encoches très spécifique (fractional slot) pour lisser la force de détente.



### B. Bobine Motrice (Déplaceur)

Le déplaceur ne fait que déplacer le gaz d'une zone à l'autre (pas de compression). La force requise est minime, seuls les frottements et l'inertie de la pièce sont à vaincre.

* **Force cible :** 10 N à 50 N.
* **Bobinage :** **200 à 600 spires** de fil fin (ex. 0,2 mm² à 0,5 mm²).
* **Alimentation :** Pilotage par pont en H ou onduleur, fournissant un signal déphasé (typiquement 90° d'avance sur le piston moteur, ajustable selon la thermodynamique) pour optimiser le cycle PV du moteur.

---

## 3. Matrice de Synthèse pour le Dimensionnement

| Paramètre | Plage "Micro-générateur" (10W - 50W) | Plage "Générateur Lourd" (~1kW - 2kW à 2Hz) |
| --- | --- | --- |
| **Diamètre ext. Aimants** | 20 mm - 40 mm | 80 mm - 150 mm |
| **Grade Aimants** | N42 | N52 (ou Halbach massif) |
| **Poids du Mover (Aimants + axe)** | 0,1 kg - 0,5 kg | 5 kg - 20 kg (Participe à la masse résonante) |
| **Course du piston (Stroke)** | 10 mm - 30 mm | 100 mm - 200 mm |
| **Entrefer (Air gap)** | 0,3 mm - 0,5 mm | 0,8 mm - 1,5 mm |
| **Densité de courant admise** | 4 à 6 A/mm² | 2 à 4 A/mm² (Refroidissement critique) |
| **Nombre de spires (Générateur)** | 300 - 800 spires | 3000 - 6000+ spires |
| **Diamètre du fil de cuivre** | 0,4 mm - 0,8 mm | 1,5 mm - 2,5 mm (ou multibrins) |
| **Type de Stator** | Sans fer (Coreless) | Ferromagnétique fortement recommandé |

### Recommandations finales pour l'intégration

À très basse fréquence (2 Hz) et forte puissance (1,5 kW), la tension générée naturellement sera faible et le courant extrêmement fort, générant beaucoup de chaleur (Pertes par effet Joule $P = R \cdot I^2$). Il est souvent stratégique de **bobiner plusieurs sections indépendantes** le long de la course du cylindre et de les relier en série.

De plus, un système de contrôle de charge électronique actif (Active Load Control) est indispensable : en modifiant le courant tiré dans la bobine en temps réel, on crée un amortissement magnétique piloté qui agit exactement comme une "boîte de vitesse" virtuelle, permettant de garder l'oscillation du Stirling parfaitement stable.
