"""
6.12 

Demander à l’utilisateur qu’il entre un nombre. Afficher ensuite : soit la racine carrée de ce
nombre, soit un message indiquant que la racine carrée de ce nombre ne peut être calculée.
"""

from math import sqrt

print("Veuillez entrer un nombre pour calculer sa racine carrée :")
racine = eval(input())

if racine > 0:
    racineCarre = sqrt(racine)
    print("La racine carrée de", racine, "est", racineCarre)
else:
    print("La racine carrée du nombre", racine, "n'est pas calculable")