# Moteur de Manson à cycle ouvert

## Une autre vision de la mobilité

Le [moteur de Manson](https://en.wikipedia.org/wiki/Manson_engine) est un moteur à air chaud extrêmement simple.  
Il fonctionne grâce à une chaudière chauffant l'air atmosphérique, qui se détend ensuite dans un cylindre avant d'être rejeté à l'extérieur.

Voir aussi la [synthèse détaillée du projet](manson/power.md) et le [calcul de rendement](manson/yield.gpt.md).

Contrairement aux moteurs thermiques modernes, il privilégie :

- la simplicité ;
- la robustesse ;
- la réparabilité ;
- l'utilisation de combustibles renouvelables.

---

# Rouler à la paille

Le moteur est conçu pour fonctionner avec une chaudière de type **[Rocket Stove](rocket_stove.euria.gpt.md)**, capable de brûler de nombreux combustibles solides :

- résidus agricoles.
- bois
- Electricité
- Huile
- solaire

L'objectif est de permettre à un véhicule de **rouler avec des ressources locales**, souvent considérées comme des déchets agricoles.

---

# Consommation

L'objectif de conception est de garantir :

> **5 litres de paille compactée par heure et par cheval-vapeur.**  
ex: Une moto coursier de 3L pour des petit trajet,
 30 L pour la familiale

Exemples :

| Puissance | Consommation |
|-----------:|-------------:|
| 1 cheval | 5 L/h |
| 2 chevaux | 10 L/h |
| 4 chevaux | 20 L/h |
| **6 chevaux** | **30 L/h** |

Cette consommation dépend naturellement du [rendement](manson/yield.gpt.md) obtenu, de la qualité du combustible et des conditions d'utilisation.
Nous considerons un moteur sans surpression, a 10 % de [rendement](manson/yield.gpt.md).

Pour le dimensionnement de la chaudière selon la température visée, voir les [volumes et consommations du four à bois](rocket_stove.euria.gpt.md).

---

# Une gamme modulaire

Une même architecture peut être déclinée selon plusieurs puissances.

| Modèle | Puissance visée |
|---------|----------------:|
| Coursier | 1 à 2 chevaux |
| Familial | 2 à 6 chevaux |
| Utilitaire | jusqu'à 6 chevaux continus |

La puissance est principalement déterminée par la taille de la chaudière [Rocket Stove].rocket_stove.euria.gpt.md) (voir aussi la [synthèse du projet](manson/power.md)).

---

# Moteur garanti à vie

La philosophie du projet est de concevoir un moteur pratiquement inusable.

Grâce à une mécanique volontairement dépouillée :

- très peu de pièces mobiles ;
- faible usure ;
- maintenance réduite ;
- fabrication simple ;
- réparations accessibles.

L'objectif est de proposer un **moteur garanti à vie**, dont les seules opérations courantes concernent les éléments d'usure périphériques (joints, roulements, lubrification).

---

# Pourquoi ce moteur ?

Ce projet ne cherche pas à concurrencer les moteurs modernes par leur rendement, mais par leur coût d'usage et leur longévité.

Ses principaux avantages sont :

- combustible local et renouvelable ;
- indépendance énergétique ;
- mécanique simple ;
- faible coût d'entretien ;
- longue durée de vie ;
- fabrication locale possible.

Le moteur de Manson constitue ainsi une alternative pour les véhicules légers, les petits utilitaires, les machines agricoles et les groupes fixes, partout où la simplicité, la durabilité et l'autonomie énergétique sont prioritaires.
