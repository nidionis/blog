# Dimensionnement d'un Moteur Stirling de Type Beta : Analyse Paramétrique pour 2 Chevaux à Basse Fréquence

Le dimensionnement d'un moteur Stirling de type Beta pour une puissance utile cible de **2 chevaux (environ 1471 Watts)** nécessite de concilier des contraintes thermodynamiques et mécaniques strictes. À basse fréquence ($1 \text{ à } 5\text{ Hz}$), l'extraction d'une telle puissance impose des volumes de travail conséquents et une gestion rigoureuse de la pression de charge et du gradient thermique ($\Delta T$).

---

## 1. Fondements Théoriques et Équations de Dimensionnement

### A. La Puissance et le Nombre de Beale

En ingénierie préliminaire des moteurs Stirling, la corrélation de Beale relie la puissance utile $P$ (en Watts) à la pression moyenne de travail $P_m$ (en Pascals), au volume balayé par le piston $V_{sw}$ (en $\text{m}^3$), et à la fréquence de cycle $f$ (en Hertz) :

$$P = \mathbf{B} \cdot P_m \cdot V_{sw} \cdot f$$

Où $\mathbf{B}$ est le nombre de Beale, généralement compris entre $0{,}11$ et $0{,}15$ pour un moteur bien optimisé. Le travail net par cycle dépend directement de l'écart de température $\Delta T = T_h - T_c$ et du rapport de compression volumétrique.

### B. Influence des Paramètres Clés

* **La Fréquence ($f$) :** De basses fréquences ($1 \text{ à } 3\text{ Hz}$) réduisent les pertes par frottement et les pertes de charge aérodynamiques dans les échangeurs, mais exigent des volumes balayés ($V_{sw}$) plus importants pour maintenir la puissance.
* **Le Gradient Thermique ($\Delta T$) :** Variant de $150^\circ\text{C}$ à $500^\circ\text{C}$ ($423\text{ K}$ à $773\text{ K}$), il détermine le rendement de Carnot théorique et la capacité du gaz de travail (azote) à se détendre avec force.
* **La Pression de Charge ($P_m$) :** Compense la faible réactivité des basses fréquences. Plus la pression est élevée, plus la densité moléculaire du gaz augmente, élevant le travail net par cycle pour un même volume.

---

## 2. Tableaux Paramétriques de Dimensionnement

Les tableaux ci-dessous présentent les configurations nécessaires pour obtenir **1471 Watts (2 ch)** en fonction des volumes totaux du cylindre ($80\text{ L} \text{ à } 400\text{ L}$), des fréquences ($1\text{ Hz} \text{ à } 5\text{ Hz}$), des deltas de température ($150^\circ\text{C} \text{ à } 500^\circ\text{C}$) et de la pression moyenne d'azote requise.

### Tableau 1 : Pression moyenne requise en fonction du Volume et de la Fréquence

*(Conditions moyennes : $\Delta T = 350^\circ\text{C}$, coefficient de Beale $\mathbf{B} = 0{,}13$)*

| Volume Total ($V_{tot}$) | Fréquence ($1\text{ Hz}$) | Fréquence ($2\text{ Hz}$) | Fréquence ($3\text{ Hz}$) | Fréquence ($5\text{ Hz}$) |
| --- | --- | --- | --- | --- |
| **80 Litres** | $7{,}1\text{ MPa}$ ($71\text{ bars}$) | $3{,}6\text{ MPa}$ ($36\text{ bars}$) | $2{,}4\text{ MPa}$ ($24\text{ bars}$) | $1{,}4\text{ MPa}$ ($14\text{ bars}$) |
| **150 Litres** | $3{,}8\text{ MPa}$ ($38\text{ bars}$) | $1{,}9\text{ MPa}$ ($19\text{ bars}$) | $1{,}3\text{ MPa}$ ($13\text{ bars}$) | $0{,}76\text{ MPa}$ ($7{,}6\text{ bars}$) |
| **200 Litres** | $2{,}8\text{ MPa}$ ($28\text{ bars}$) | $1{,}4\text{ MPa}$ ($14\text{ bars}$) | $0{,}95\text{ MPa}$ ($9{,}5\text{ bars}$) | $0{,}57\text{ MPa}$ ($5{,}7\text{ bars}$) |
| **400 Litres** | $1{,}4\text{ MPa}$ ($14\text{ bars}$) | $0{,}7\text{ MPa}$ ($7\text{ bars}$) | $0{,}48\text{ MPa}$ ($4{,}8\text{ bars}$) | $0{,}29\text{ MPa}$ ($2{,}9\text{ bars}$) |

---

### Tableau 2 : Impact du Delta de Température ($\Delta T$) sur la Pression Requise

*(Pour un volume fixe de $200\text{ L}$ à une fréquence de $3\text{ Hz}$)*

| Delta de Température ($\Delta T$) | Température Chaude estimée ($T_h$) | Pression Moyenne Nécessaire ($P_m$) |
| --- | --- | --- |
| **$150^\circ\text{C}$** ($423\text{ K}$) | $270^\circ\text{C}$ | $2{,}1\text{ MPa}$ ($21\text{ bars}$) |
| **$250^\circ\text{C}$** ($523\text{ K}$) | $370^\circ\text{C}$ | $1{,}3\text{ MPa}$ ($13\text{ bars}$) |
| **$350^\circ\text{C}$** ($623\text{ K}$) | $470^\circ\text{C}$ | $0{,}95\text{ MPa}$ ($9{,}5\text{ bars}$) |
| **$500^\circ\text{C}$** ($773\text{ K}$) | $620^\circ\text{C}$ | $0{,}67\text{ MPa}$ ($6{,}7\text{ bars}$) |

---

## 3. Synthèse et Recommandations pour l'Architecture Beta

1. **Compromis Volume / Pression :** Pour un moteur fonctionnant à basse fréquence ($2 \text{ à } 3\text{ Hz}$), viser un volume de **$150 \text{ à } 200\text{ Litres}$** permet de maintenir des pressions de service modérées (entre $1\text{ et } 2\text{ MPa}$, soit $10 \text{ à } 20\text{ bars}$), ce qui simplifie grandement l'étanchéité du carter et la résistance des structures mécaniques.
2. **Rôle de l'Azote ($N_2$) :** L'azote offre un bon compromis de masse molaire et de sécurité par rapport à l'hydrogène ou l'hélium, mais exige des coefficients d'échange thermique optimisés dans les zones de chauffe et de refroidissement pour éviter les pertes par inefficacité thermique, en particulier lorsque le $\Delta T$ se situe dans la frange basse ($150^\circ\text{C}$).
3. **Gestion des Volumes Morts :** Dans les grands volumes ($> 100\text{ L}$), la minimisation des espaces morts (canalisations, espaces sous le déplaceur) est critique. Un volume mort excessif réduit l'amplitude de la pression cyclique et annule le bénéfice d'une grande cylindrée.
