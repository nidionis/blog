# Fréquence — le levier de vitesse

> **Status:** canonical · **Owns:** sensibilité à la fréquence de cycle · **Up:** [Leviers](README.md) · **Lang:** FR · [EN](../../levers/frequency.md)

La base tourne à **2 Hz**, un cycle toutes les demi-secondes. C'est lent volontairement : piston, déplaceur et lumières sont simples, et l'arbre peut entraîner une machine lente sans réducteur. La fréquence est le levier le plus facile à écrire et l'un des plus difficiles à rendre fiable.

## Loi

$$P \propto f \qquad D \propto f^{-1/3}$$

À remplissage et couple constants, doubler la fréquence double la puissance. Pour les mêmes 2 ch, la chambre se réduit comme la racine cubique de la fréquence :

| Fréquence | Cycles/min | `V_c` à 2 ch | `D` à 2 ch |
|---:|---:|---:|---:|
| 1 Hz | 60 | 271,1 L | 70,1 cm |
| 2 Hz (base) | 120 | 135,5 L | 55,7 cm |
| 4 Hz | 240 | 67,8 L | 44,2 cm |
| 8 Hz | 480 | 33,9 L | 35,1 cm |

Même 8 Hz ne fait que 480 cycles par minute, très loin d'un moteur automobile. Le moteur reste une machine lente.

## Ce que cela coûte

- **Distribution** — admission et échappement doivent remplir et vider la chambre en moins de temps. C'est le travail décrit dans [optimisation](../engines/manson/optimisation.md).
- **Pertes de charge** — la perte de pression croît à peu près comme le carré de la vitesse ; la loi `P ∝ f` suppose que la chambre se remplit encore.
- **Usure et bruit** — roulements, joints et déplaceur voient plus de cycles par heure. À 8 Hz, quatre fois plus qu'à la base.
- **Dynamique** — un piston léger et rapide est plus difficile à guider ; vibration et équilibrage deviennent dimensionnants.
- **Alternateur** — un alternateur linéaire à basse fréquence demande beaucoup de spires ; plus de fréquence aide l'électricité. Voir [alternateur linéaire](../engines/stirling/linear-alternator.md).

## Lecture pessimiste

Dimensionner à 2 Hz. Traiter 4 Hz comme une amélioration réaliste et 8 Hz comme une cible de développement qui exige des mesures de remplissage, d'usure et de bruit. Si la distribution ne suit pas, le gain disparaît et les pertes restent.

## Pourquoi la basse fréquence est résiliente

Un moteur lent tolère une combustion imparfaite, un carburant sale et des roulements simples. Il peut entraîner directement une [transmission hackable](../drivetrain/design.md). La vitesse est un levier de compacité, pas une condition de la promesse de 2 ch.

## Voir aussi

- [Dimensionnement](../engines/manson/sizing.md) — la fréquence dans la relation de puissance
- [Optimisation](../engines/manson/optimisation.md) — distribution et porosité
- [Volume et poids](volume-poids.md) — ce qu'une chambre plus petite fait gagner
- [Version anglaise (dérivation)](../../levers/frequency.md)
