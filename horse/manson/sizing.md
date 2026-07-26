# Estimation du volume d'air nécessaire pour un moteur de Manson à cycle ouvert

## Résumé

Cet article présente une estimation du débit d'air et du volume balayé nécessaires pour un moteur de Manson à cycle ouvert délivrant **3 kW, 6 kW et 9 kW** de puissance mécanique.

Les hypothèses retenues sont :

- Fonctionnement à **pression atmosphérique** ;
- Rendement global de conversion énergétique de **5 %** ;
- Différence de température entre source chaude et source froide : **$\Delta T = 300$ °C** ;
- Fréquence de fonctionnement : **2 cycles par seconde**.

L'objectif est d'obtenir un ordre de grandeur du volume d'air déplacé par cycle afin de dimensionner la cylindrée du moteur.

---

## 1. Hypothèses physiques

| Paramètre | Symbole | Valeur |
| :--- | :---: | ---: |
| Fluide de travail | - | Air |
| Pression | $P$ | 1 atm |
| Température de référence | $T_{ref}$ | 20 °C |
| Écart de température | $\Delta T$ | 300 K |
| Chaleur spécifique de l'air | $C_p$ | 1005 J/(kg·K) |
| Masse volumique de l'air | $\rho$ | 1,2 kg/m³ |
| Rendement moteur | $\eta$ | 5 % |
| Fréquence | $f$ | 2 cycles/s |

---

## 2. Puissance thermique nécessaire

Le rendement est défini par :
$$ \eta = \frac{P_{méc}}{P_{th}} $$

Donc :
$$ P_{th} = \frac{P_{méc}}{\eta} $$

Avec un rendement de 5 % ($\eta = 0,05$) :
$$ P_{th} = \frac{P_{méc}}{0,05} $$

Cela signifie que pour produire 1 kW mécanique, il faut environ :
$$ 1 / 0,05 = 20 \text{ kW thermiques} $$

---

## 3. Débit massique d'air

L'énergie transportée par 1 kg d'air chauffé de 300 °C est :
$$ E_{kg} = C_p \times \Delta T $$

Soit :
$$ E_{kg} = 1005 \times 300 = 301\,500 \text{ J/kg} $$

Le débit massique nécessaire $\dot{m}$ est :
$$ \dot{m} = \frac{P_{th}}{C_p \times \Delta T} $$

---

## 4. Débit volumique

Le débit volumique $\dot{V}$ est obtenu avec :
$$ \dot{V} = \frac{\dot{m}}{\rho} $$

Avec $\rho = 1,2 \text{ kg/m³}$.

---

## 5. Volume d'air par cycle

Le moteur fonctionne à une fréquence $f = 2$ cycles par seconde. Le volume déplacé par cycle $V_{cycle}$ est donc :
$$ V_{cycle} = \frac{\dot{V}}{f} $$

---

## 6. Résultats numériques

| Puissance mécanique | Puissance thermique | Débit d'air | Volume par cycle |
| :---: | :---: | :---: | :---: |
| **3 kW** | 60 kW | 0,166 m³/s | 83 L |
| **6 kW** | 120 kW | 0,332 m³/s | 166 L |
| **9 kW** | 180 kW | 0,498 m³/s | 249 L |

---

## 7. Relation pratique

Dans ces conditions :

- 1 kW mécanique nécessite environ **20 kW thermiques** ;
- 1 kW mécanique demande environ **0,055 m³/s d'air** ;
- À 2 cycles/s, cela représente environ **28 litres par cycle**.

| Puissance | Volume déplacé par cycle |
| :--- | :--- |
| **3 kW** | 83 litres |
| **6 kW** | 166 litres |
| **9 kW** | 249 litres |

---

## 8. Discussion

Ces valeurs correspondent à un moteur de Manson à cycle ouvert sans récupération parfaite de chaleur. Dans un moteur réel, plusieurs phénomènes modifient ces résultats :

- Pertes thermiques vers l'environnement ;
- Pertes par frottement ;
- Pertes de charge dans les conduits ;
- Efficacité du transfert thermique ;
- Efficacité du régénérateur.

Un régénérateur performant peut réduire fortement le débit d'air nécessaire en réutilisant une partie de l'énergie thermique contenue dans l'air sortant.

---

## 9. Conclusion

Pour un moteur de Manson à cycle ouvert fonctionnant à pression atmosphérique avec $\eta = 5\,\%$, $\Delta T = 300$ °C et $f = 2$ cycles/s, le volume théorique d'air nécessaire est :

- **3 kW** : 83 litres par cycle
- **6 kW** : 166 litres par cycle
- **9 kW** : 249 litres par cycle

Ces résultats donnent une première estimation de la cylindrée nécessaire pour concevoir un moteur de Manson de faible ou moyenne puissance.
