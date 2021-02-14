"""
Écrivez un programme qui calcule les 50 premiers termes de la table de multiplication par 13,
mais n’affiche que ceux qui sont des multiples de 7.
"""

c = 1
# Les 50 premiers multiples
while (c < 51):
    # resultat de la multiplication par 13
    d = 13*c
    # si le résultat est un multiple de 7
    if (d % 7 == 0):
        # multiple de 3 affiché avec une *, sans saut de ligne
        print(d, "*", end=" ")
    else:
        # résultat affiché sans *, sans saut de ligne
        print(d, end=" ")
    c += 1
