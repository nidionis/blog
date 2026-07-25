# Synthèse – Projet de moteur de Manson à cycle ouvert
# Problematique : Assurer 2 chevaux

Voir aussi la [présentation générale du projet](../README.md) et le [détail du calcul de rendement](yield.gpt.md).

## Concept

Le projet concerne un **moteur de Manson à cycle ouvert**, constitué de seulement trois éléments principaux :

1. **Chaudière** (source chaude)
2. **Piston**
3. **Bielle** (conversion du mouvement alternatif en rotation)

Le fluide de travail est l'air atmosphérique :
- admission d'air,
- chauffage dans la chaudière,
- détente dans le cylindre,
- échappement à l'atmosphère.

Le moteur fonctionne donc **à cycle ouvert**, contrairement au moteur Stirling dont le gaz reste confiné.

---

# Rendement

## Limite théorique

Le rendement maximal est donné par le cycle de Carnot (voir le [détail du calcul de rendement](yield.gpt.md)) :

\[
\eta = 1-\frac{T_f}{T_c}
\]

Exemple :

- chaudière : **600 °C (873 K)**
- ambiance : **20 °C (293 K)**

Rendement maximal :

**66,4 %**

Cette valeur reste inaccessible en pratique.

---

## Rendements réalistes

| Niveau | Rendement |
|---------|----------:|
| Prototype historique | 5–10 % |
| Conception moderne | 10–15 % |
| Conception très optimisée | 15–20 % |

---

# Cas d'un moteur de 20 kW (soit 27,2 chevaux-vapeur)

| Rendement | Puissance thermique |
|-----------:|-------------------:|
| 10 % | 200 kW |
| 15 % | 133 kW |
| 20 % | 100 kW |

---

# Besoins en combustible

## Pour 200 kW thermiques

### Bois sec

- 40 à 50 kg/h

≈ 80 à 140 litres de bûches par heure.

# Chaudière Rocket Stove

Le moteur sera alimenté par une chaudière de type **[Rocket Stove](../../rocket_stove.euria.gpt.md)**, adaptée à plusieurs usages.

Trois tailles sont envisagées :

| Modèle | Volume approximatif de chaudière | Usage |
|---------|---------------------------------:|-------|
| **Coursier** | **3 L** | Petit véhicule léger | 1-2 chevaux
| **Familial** | **≈25 L** | Automobile ou petit utilitaire | soit probablement 2-6 chevaux
| **Poids lourd / Péniche terrestre** | **≈50 L** | Transport lourd, tracteur ou péniche terrestre | 6 chevaux continu
---
L'objectif est de disposer d'une même architecture de moteur, déclinée en plusieurs puissances simplement en faisant varier la taille de la chaudière Rocket Stove.  
Note: 1 cheval = ~40km/h  

# Philosophie du projet

Le projet privilégie :

- une mécanique extrêmement simple ;
- un faible nombre de pièces mobiles (3 simples, garantie a vie) ;
- une alimentation par biomasse locale (bois, foin, résidus agricoles) ;
- une maintenance minimale ;
- une fabrication accessible ;
- une architecture évolutive selon la puissance recherchée.

Le moteur est pensé comme une alternative robuste aux motorisations conventionnelles, capable d'utiliser des combustibles renouvelables tout en conservant une conception mécanique dépouillée.
```
