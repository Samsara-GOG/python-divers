"""
Écrivez un programme qui affiche la suite de symboles suivante :
*
**
***
****
*****
******
*******
"""
# initialisation du compteur
i = 1
# initialisation des variables e modifiable, et d fixe
e, d = "", "*"

# 7 tours au compteur
while (i < 8):
    # affichage de * plus précédent resultat
    print(d+e)
    i += 1
    # incrémentation de la variable * modifiable
    e += "*"
