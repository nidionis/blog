# Protection de Propriété Intellectuelle par Preuve Cryptographique

Ce document définit le cadre de protection de l'idée et du projet associés, en utilisant la technologie de clé privée comme preuve irréfutable de détention et d'antériorité.

## 1. Principe de la Preuve de Détention

L'idée, les concepts et les travaux décrits dans ce dépôt (notamment le système **iDeal** et les optimisations du **Moteur Manson**) sont protégés par une signature cryptographique.

*   **Identité** : Le détenteur légitime est celui qui possède la clé privée correspondant à l'empreinte (hash) de la clé publique spécifiée dans les métadonnées du projet ou du bloc de genèse.
*   **Intégrité** : Toute modification ou extension du concept doit être signée par cette clé pour être considérée comme "officielle".
*   **Antériorité** : L'inscription du hash de ce document sur une blockchain publique (Proof of Existence) fait foi de date certaine.

## 2. Déclaration de Propriété (Preuve par Clé Privée)

Je, soussigné, détenteur de la clé privée associée à l'adresse/identité cryptographique suivante :

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEldi9P+JGQUL6y2s0IwCykCqhaBJe0XfDESsicEZefI pain@fedora
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPsf+ZlJZ9NnOEzufzuSoFECSeCYiozud9ux31famxN3 painpain@fedora
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKuXZWtHSzB8Pj2otWi5IgGJNQVQXYGzhX8rMhi6aI8Q dell@device-65.home

Déclare être l'auteur et le propriétaire des concepts originaux décrits dans ce projet. La capacité à signer ce message avec ladite clé privée constitue la preuve juridique et technique de ma propriété sur l'idée.

## 3. Licence d'Utilisation : "Private Key Evidence License" (PKEL)

L'usage des idées contenues dans ce projet est régi par les conditions suivantes :

1.  **Reconnaissance de Source** : Toute utilisation, citation ou implémentation doit mentionner l'adresse cryptographique d'origine comme source de l'invention.
2.  **Droit d'Exploitation** : Le droit d'exploitation commerciale est réservé au détenteur de la clé privée de genèse, sauf accord explicite signé cryptographiquement par ce dernier.
3.  **Preuve de Consentement** : Une autorisation n'est valide que si elle est accompagnée d'un message signé par la clé privée du propriétaire, incluant le hash de l'accord et l'identité du bénéficiaire.
4.  **Non-Répudiation** : En utilisant ces travaux, vous acceptez que la preuve cryptographique soit supérieure à toute autre forme de témoignage humain ou document papier non signé numériquement.

## 4. Procédure de Vérification

Pour vérifier la légitimité d'une revendication sur cette idée :
1. Générer un message aléatoire (nonce).
2. Demander au revendicateur de signer ce message avec la clé privée associée au projet.
3. Vérifier la signature avec la clé publique de référence.
Si la vérification réussit, la détention est prouvée.

---
*Fait par preuve cryptographique, le 26 juillet 2026.*
