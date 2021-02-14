"""
7.10 
Définissez une fonction indexMax(liste) qui renvoie l’index de l’élément ayant la valeur la
plus élevée dans la liste transmise en argument. Exemple d’utilisation :
serie = [5, 8, 2, 1, 9, 3, 6, 7]
print(indexMax(serie))
4
"""


def indexMax(nums):
    "renvoie l'indice du plus grand élément de la liste nums"
    i, max = 0, 0
    while i < len(nums):
        if nums[i] > max :
            max, imax = nums[i], i
        i += 1    
    return ("L’index de l’élément ayant la valeur la plus élevée dans la liste transmise est : index %d pour valeur %d " %(imax, nums[imax]))
    
serie = [5, 8, 2, 1, 9, 3, 6, 7]        
print(indexMax(serie))
