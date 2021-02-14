"""
Premier essai de script Python
petit programme simple affichant une suite de Fibonacci, c.à.d une suite
de nombres dont chaque terme est égal à la somme des deux précédents.
"""

print("\nSuite de Fibonacci\n")
# a & b servent au calcul des termes sucessifs
a, b, c = 0, 1, 1         # c est simple compteur       
print(a, end = " ")       # affichage du premier terme à la suite des autres sur la même ligne                   
while c <= 15:            # nous afficherons 15 termes au total  
    print(c, ": ", b)                     
    a, b, c = b, a+b, c+1
