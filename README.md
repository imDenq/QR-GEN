# Projet QR Code - Paul-André, Théo, Soren


## Introduction à GitHub

GitHub est une plateforme de développement collaboratif offrant un espace centralisé où les équipes peuvent partager, collaborer et contribuer à des projets.


## Les commandes a connaitre pour débuter sur Git

Voici une liste de commandes Git utiles pour débuter votre projet
Apprenez les bien et tester les pour vous entrainez et les prendres en main.

### Les commmandes ayant un impact direct sur votre projet
- Initialiser un dépôt Git :`git init`  
Initialise un nouveau dépôt Git dans le répertoire courant.

- Ajouter un fichier au suivi :`git add "fichier"`  
Ajoute un fichier spécifié au suivi, préparant les modifications pour le prochain commit.

- Effectuer un commit :`git commit`  
Enregistre les modifications ajoutées au suivi, créant un nouveau commit dans l'historique.

- Restaurer un fichier précédent :`git restore "fichier"`  
Annule les modifications apportées à un fichier, le restaurant à sa version précédente.

- Supprimer les fichiers non suivis :`git clean . -f`  
Supprime les fichiers non suivis dans le répertoire de travail de manière forcée.

- Modifier le dernier commit :`git commit --amend`  
Permet de modifier le dernier commit en ajoutant des modifications supplémentaires ou en modifiant le message de commit.

### Les commandes "view" ou "verif"
- Vérifier l'état du dépôt :`git status`  
Affiche l'état des fichiers dans le dépôt, montrant les modifications non enregistrées et les fichiers prêts à être validés.

- Voir l'historique des commits :`git log`  
Affiche l'historique des commits avec des détails tels que l'auteur, la date et le message de commit.

- Voir les modifications non validées :`git diff`  
Montre les modifications entre le répertoire de travail et la dernière version enregistrée.

- Afficher les détails d'un commit :`git show "hash"`  
Affiche les détails d'un commit spécifique en utilisant son identifiant unique (hash).

- Afficher la liste des branches :`git branch`  
Affiche la liste des branches locales et met en évidence la branche actuelle.

### Les deux commandes permettant de communiquer avec GitHub
- Pousser les modifications vers le dépôt distant :`git push`  
Envoie les commits locaux vers le dépôt distant, mettant à jour l'historique.

- Récupérer les modifications depuis le dépôt distant :`git pull`  
Récupère les modifications du dépôt distant et les fusionne avec la branche locale actuelle.


## Les Branches sur GitHub

Sur GitHub, les branches sont utilisées pour développer des fonctionnalités de manière isolée, expérimenter de nouvelles idées, corriger des erreurs ou effectuer d'autres modifications sans affecter directement la branche principale du projet, généralement appelée `main`. Les branches permettent une gestion flexible du flux de travail et facilitent la collaboration entre plusieurs contributeurs.

Voici quelques concepts clés liés aux branches sur GitHub :

- Création d'une nouvelle branche principale :
    `git branch main`
    `git checkout main`

- Création d'une nouvelle branche :
    `git branch nom_de_la_branche`
    `git checkout nom_de_la_branche`

- Fusion classique d'une branche vers la principal :
    `git checkout main`
    `git merge nom_de_la_branche`

En résumé, les branches Git sont utilisées pour développer des fonctionnalités de manière isolée. Voici les commandes associées : créer une nouvelle branche, effectuer des modifications, valider les modifications, pousser la branche vers le référentiel distant et créer une pull request pour la fusion. Ensuite, vous pouvez utiliser différentes stratégies de fusion pour intégrer les changements dans la branche principale.


# Conclusion
En résumé, GitHub s'impose comme un outil incontournable pour les développeurs, tant pour la gestion collaborative des projets que pour l'établissement d'une présence professionnelle en ligne. Sa popularité croissante souligne son importance dans le domaine de la programmation et son impact positif sur la productivité et l'efficacité des équipes de développement.