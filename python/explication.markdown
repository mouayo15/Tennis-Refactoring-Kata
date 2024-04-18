# Analyse code TennisGame6

Premièrement on commence le refacto de la fonction # score # parceque  c'est vraiment la fonction principale et il y a beaucoup de choses à améliorer 
Il y a une redondance significative dans la méthode score lorsque q'on attribue regularScore et tieScore. Les cas pour attribuer ces valeurs sont essentiellement les mêmes à plusieurs endroits.

1.Refacto de tie score 
Création de la fonction privée _tie_score qui renvoie le score name si le score de deux joueurs sont égaux  
2.Refacto de end game score
3.refacto regular_score
# Golden master 
Création de la méthode de test golden master avec une seule langue français 
