# Estimation du volume d'air pour un moteur de Manson à cycle ouvert (2 à 9 kW)

*Note technique synthétique*

## Résumé

Cet article présente l'estimation du débit d'air et du volume balayé nécessaires pour un moteur de Manson à cycle ouvert délivrant 2, 3, 6 et 9 kW.

Hypothèses retenues :

* Rendement global ($\eta$) : $0{,}05$ ($5\ \%$)
* Écart de température ($\Delta T$) : $300\ \text{K}$
* Fréquence de fonctionnement ($f$) : $2\ \text{Hz}$
* Capacité thermique de l'air ($C_p$) : $1005\ \text{J/(kg}\cdot\text{K)}$
* Masse volumique de l'air ($\rho$) : $1{,}2\ \text{kg/m}^3$

---

## 1. Formules utilisées

* **Puissance thermique** :

$$P_{th} = \frac{P_m}{\eta}$$


* **Débit massique** :

$$q_m = \frac{P_{th}}{C_p \cdot \Delta T}$$


* **Volume par cycle** :

$$V_{cycle} = \frac{q_m / \rho}{f}$$



---

## 2. Résultats Numériques

| Puissance Mécanique ($P_m$) | Puissance Thermique ($P_{th}$) | Débit Massique ($q_m$) | Volume par Cycle ($V_{cycle}$) |
| --- | --- | --- | --- |
| **2 kW** | $40\ \text{kW}$ | $0{,}43\ \text{kg/s}$ | **180 litres** |
| **3 kW** | $60\ \text{kW}$ | $0{,}65\ \text{kg/s}$ | **270 litres** |
| **6 kW** | $120\ \text{kW}$ | $1{,}30\ \text{kg/s}$ | **540 litres** |
| **9 kW** | $180\ \text{kW}$ | $1{,}95\ \text{kg/s}$ | **810 litres** |

---

## 3. Conclusion

Les résultats mettent en évidence des volumes par cycle très importants (allant de 180 à 810 litres), confirmant les contraintes dimensionnelles majeures des moteurs à air à cycle ouvert pour atteindre des puissances de l'ordre du kilowatt.
