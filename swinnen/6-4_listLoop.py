"""6.4 

Écrivez un programme qui permette d’encoder des valeurs dans une liste. Ce programme
devrait fonctionner en boucle, l’utilisateur étant invité à entrer sans cesse de nouvelles
valeurs, jusqu’à ce qu’il décide de terminer en frappant <Enter> en guise d’entrée. Le
programme se terminerait alors par l’affichage de la liste. 
Exemple de fonctionnement :
    Veuillez entrer une valeur : 25
    Veuillez entrer une valeur : 18
    Veuillez entrer une valeur : 6284
    Veuillez entrer une valeur :
    [25, 18, 6284]
"""

numbers = []
start = "start"

print("\nProgramme pour entrer des valeurs numériques")
print("(Faire \"Entrée\" sans entrer de valeur pour visionner la liste ou pour simplement quitter le programme)\n")

while start != "":
    print("Veuillez entrer des valeurs pour remplir cette liste : ", end = " ")
    start = input()
    if start != "":
        numbers.append(float(start))
print(numbers)
    