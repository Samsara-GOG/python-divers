"""
Premier essai de script Python
petit programme simple affichant une suite de Fibonacci, c.à.d une suite
de nombres dont chaque terme est égal à la somme des deux précédents.
"""

print("\nSuite de Fibonacci\n")

a, b, c = 1, 1, 1           # a & b servent au calcul des termes sucessifs
                            # c est simple compteur
while c < 11:               
    print(b, end = " ")     # nous afficherons 11 termes au total sur la même ligne
    a, b, c = b, a+b, c+1


