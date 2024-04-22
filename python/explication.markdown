# Analyse code TennisGame6

Premièrement on commence le refacto de la fonction # score # parceque  c'est vraiment la fonction principale et il y a beaucoup de choses à améliorer 
Il y a une redondance significative dans la méthode score lorsque q'on attribue regularScore et tieScore. Les cas pour attribuer ces valeurs sont essentiellement les mêmes à plusieurs endroits.

1.Refacto de tie score 
Création de la fonction privée _tie_score qui renvoie le score name si le score de deux joueurs sont égaux  
2.Refacto de end game score
3.refacto regular_score

#Golden master
### Création de la méthode de test golden master avec une seule langue
- Création initiale de la méthode de test Golden Master.
- Utilisation de la langue française comme langue par défaut pour les scores.

### Refactorisation du chemin du répertoire de sauvegarde
- Refactorisation du chemin du répertoire de sauvegarde pour rendre le code plus claire et comprehensible.
- Utilisation de constantes pour définir le chemin du répertoire.

### Utilisation d'une constante pour la langue et ajout de la prise en charge de différents langages
- Ajout d'une constante pour la langue par défaut.
- Prise en charge de différents langages en ajoutant des paramètres à la méthode `play_game()` et à la méthode `make_file_name()`.

### Rajout de la méthode `makedirs` pour la création automatique du répertoire golden-master
- Ajout de la méthode `makedirs` pour créer automatiquement le répertoire `golden-master` s'il n'existe pas déjà.
- Ceci garantit que les fichiers de sauvegarde peuvent être créés sans nécessiter de préparation manuelle des répertoires.

### Ajout de commentaires pour la clarté du code
- Ajout de commentaires explicatifs pour décrire le but et le fonctionnement de chaque méthode.
- Amélioration de la lisibilité et de la compréhension du code pour les contributeurs futurs.

### Refactoring: Ajout de gestion de l'encodage pour la lecture et l'écriture des fichiers
- Ajout de gestion de l'encodage lors de la lecture et de l'écriture des fichiers pour éviter les problèmes potentiels avec les caractères spéciaux.
- Utilisation de l'encodage spécifié dans la variable `ENCODING` pour assurer la compatibilité avec les différentes plates-formes et configurations.

