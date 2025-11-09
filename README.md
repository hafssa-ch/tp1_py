# TP 1 : Classes et Objets – Exercices Python

Ce TP a pour objectif de pratiquer la création et l’utilisation de classes et objets en Python, avec des notions de propriétés, méthodes de classe, méthodes statiques et gestion de contexte.

## Exercice 1 — Compteur de visites de pages

Objectif :
Distinguer attributs de classe et attributs d’instance.
Description :
Création de la classe CompteurPage avec un attribut de classe total_visites et un attribut d’instance url.
Incrémentation du compteur global à chaque création de page.
Extension : suivi des visites par page individuelle via la méthode enregistrer_lecture().
<img width="776" height="206" alt="image" src="https://github.com/user-attachments/assets/f95c6069-44c8-4546-91a5-411abbde1f81" />

## Exercice 2 — Gestion d’inventaire d’articles

Objectif : 
Encapsuler les données métier et effectuer des calculs.
Description :
Classe Article avec reference, designation, prix_ht et stock.
Méthode valeur_stock() pour calculer la valeur d’un article.
Extension : méthode approvisionner() pour augmenter le stock et journaliser l’opération dans un fichier mouvements.log.
<img width="733" height="293" alt="image" src="https://github.com/user-attachments/assets/33c9f37a-e203-4b10-864c-10a9a6b0571f" />

## Exercice 3 — Carnet d’adresses minimal

Objectif : 
Travailler avec listes d’objets et méthodes de recherche.
Description :
Classe Contact avec nom, telephone et email, et propriété initiale.
Classe Carnet avec liste privée _contacts, méthodes ajouter(), recherche() et afficher_tous().
Extension : propriété en lecture seule nombre_contacts.
<img width="645" height="286" alt="image" src="https://github.com/user-attachments/assets/6b5af88d-f756-435d-b5ff-fffb49fff18f" />

## Exercice 4 — Calculatrice géométrique pour cercles

Objectif : 
Sécuriser l’accès aux attributs avec des propriétés.
Description :
Classe Cercle avec attribut privé _rayon.
Propriétés rayon (avec contrôle de valeur), perimetre et surface.
Extension : méthode agrandir(pourcentage) pour augmenter le rayon d’un certain pourcentage.
<img width="692" height="238" alt="image" src="https://github.com/user-attachments/assets/ab86aafd-734d-4b70-bff3-ab4f141c3400" />

## Exercice 5 — Journal de tâches avec gestion de contexte

Objectif :
Exploiter le mot-clé with pour gérer automatiquement l’ouverture et la fermeture d’un fichier.
Description :
Classe JournalTaches avec méthodes __enter__() et __exit__() pour gérer le fichier journal.txt.
Méthode enregistrer() pour ajouter une tâche horodatée.
Extension : méthode lire() pour afficher l’historique dans l’ordre chronologique inverse.
<img width="698" height="250" alt="image" src="https://github.com/user-attachments/assets/8a062f57-2952-4d49-aeb5-41ef790ef72c" />

## Exercice 6 — Convertisseur de devises

Objectif : 
Illustrer l’usage de méthodes statiques et de classe.
Description :
Classe Convertisseur avec attribut de classe taux_eur_dh.
Méthodes statiques vers_dh() et vers_eur() pour les conversions.
Méthode de classe mettre_a_jour_taux() pour modifier le taux de conversion global.
<img width="652" height="108" alt="image" src="https://github.com/user-attachments/assets/a1d20d28-3ee5-4e07-8f41-34723dea885c" />
