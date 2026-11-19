# Limite angulaire — Dérivation (Version française, sous-projet 2Cheval)

> **Status:** canonical derivation · **Up:** [Grille polaire](polar-grid.md)

Dérivation du rayon d'arrêt minimal pour que deux traits de largeur `d` ne se chevauchent pas près du centre.

En coordonnées polaires, lorsque plusieurs rayons convergent vers le centre, l'espacement angulaire se resserre et les lignes finissent par se chevaucher si elles gardent une largeur de dépôt constante (diamètre de buse $d$). Pour éviter la sur-extrusion et le crash de la buse au centre, chaque rayon doit s'arrêter à une distance minimale du centre (rayon de butée), formant des « zones de vide » triangulaires ou trapézoïdales entre eux.

---

### 1. Rayon de butée pour les axes intermédiaires ($\pi/4, 3\pi/4$, etc.)

Soit $d$ le diamètre de la buse. Pour les axes principaux, l'espace angulaire est $\Delta\theta = \pi/2$. Le rayon de butée pour que deux lignes adjointes ne se chevauchent pas est :

$$R_0 = \frac{d}{2}$$

Considérons deux rayons adjacents séparés par un angle $\alpha$ (par exemple, entre $0$ et $\pi/4$, $\Delta\theta = \pi/4$). La distance euclidienne $E(R)$ entre deux traits de largeur $d$ à distance $R$ du centre est :

$$E(R) = 2R \sin\left(\frac{\Delta\theta}{2}\right)$$

Pour que les deux traits de largeur $d$ ne se chevauchent pas :

$$2R \sin\left(\frac{\Delta\theta}{2}\right) \ge d \implies R \ge \frac{d}{2 \sin\left(\frac{\Delta\theta}{2}\right)}$$

* **Pour les bissectrices ($\pi/4, 3\pi/4, \dots$) intercalées entre les axes à $\pi/2$ :** l'écart angulaire est $\Delta\theta = \pi/4$ (45°), donc :

$$R_{\pi/4} = \frac{d}{2 \sin(\pi/8)} = \frac{d}{2 \times 0{,}38268} \approx 1{,}306 \, d$$

* **Pour les sous-bissectrices ($\pi/8, 3\pi/8, \dots$) :** l'écart tombe à $\Delta\theta = \pi/8$ (22,5°), donc :

$$R_{\pi/8} = \frac{d}{2 \sin(\pi/16)} = \frac{d}{2 \times 0{,}19509} \approx 2{,}563 \, d$$

---

### 2. Forme géométrique et suite mathématique

Il s'agit d'une **suite géométrique liée à la fonction sinus**. De manière générale, si l'on densifie le maillage en divisant le pas angulaire par 2 à chaque génération $n$, le rayon de butée de la $n$-ième série est :

$$R_n = \frac{d}{2 \sin\left(\frac{\theta_0}{2^n}\right)}$$

Quand $n$ augmente, le rayon de butée augmente proportionnellement à $1/\sin(1/2^n)$, ce qui fait reculer les rayons de plus en plus loin du centre pour laisser « passer » la géométrie sans collision.

## Voir aussi

- [Dictionnaire / Glossary](../../GLOSSARY.md)
