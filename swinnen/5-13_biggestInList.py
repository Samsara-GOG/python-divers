"""
5.13 
Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée. Par
exemple, si on l’appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15] , ce programme devrait
afficher : le plus grand élément de cette liste a la valeur 75.
"""

liste = [32, 5, 12, 8, 3, 75, 2, 15]
i = 0
max = 0

while i < len(liste):
    if liste[i] > max:
        max = liste[i]
    i += 1
    
print("Le plus grand élement de cette liste a la valeur", max)