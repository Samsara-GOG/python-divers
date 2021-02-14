"""
Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7, en
signalant au passage (à l’aide d’une astérisque) ceux qui sont des multiples de 3.
Exemple : 7 14 21 * 28 35 42 * 49 ...
"""

c = 1
# Les 20 premiers multiples
while (c < 21):
    # resultat de la multiplication par 7
    d = 7*c
    # si le résultat est un multiple de 3
    if (d % 3 == 0):
        # multiple de 3 affiché avec une *, sans saut de ligne
        print(d, "*", end=" ")
    else:
        # résultat affiché sans *, sans saut de ligne
        print(d, end=" ")
    c += 1
