"""
Une légende de l’Inde ancienne raconte que le jeu d’échecs a été inventé par un vieux sage,
que son roi voulut remercier en lui affirmant qu’il lui accorderait n’importe quel cadeau en
récompense. Le vieux sage demanda qu’on lui fournisse simplement un peu de riz pour ses
vieux jours, et plus précisément un nombre de grains de riz suffisant pour que l’on puisse en
déposer 1 seul sur la première case du jeu qu’il venait d’inventer, deux sur la suivante, quatre
sur la troisième, et ainsi de suite jusqu’à la 64 e case.
Écrivez un programme Python qui affiche le nombre de grains à déposer sur chacune des 64
cases du jeu. Calculez ce nombre de deux manières :
• le nombre exact de grains (nombre entier) ;
• le nombre de grains en notation scientifique (nombre réel).
"""

numSquare = 1       # numéro de la case
quantityCorn = 1    # nombre de grains à y déposer
# Pour la variante, il suffit de définir quantityCorn comme <float>
# en remplaçant la ligne ci-dessus par :  quantityCorn = 1.

while numSquare < 65:
    print(numSquare, quantityCorn)
    numSquare, quantityCorn = numSquare+1, quantityCorn*2


    