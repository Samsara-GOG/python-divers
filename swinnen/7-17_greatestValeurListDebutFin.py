# -*- coding: utf-8 -*-
"""
7.17 
Définissez une fonction eleMax(liste,debut,fin) qui renvoie l’élément ayant la plus grande valeur dans la liste transmise. Les deux arguments debut et fin indiqueront les indices entre lesquels doit s’exercer la recherche, et chacun d’eux pourra être omis (comme dans l’exercice précédent). 

Exemples de la fonctionnalité attendue :
>>> serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
>>> print(eleMax(serie)) #9
>>> print(eleMax(serie, 2, 5)) #7
>>> print(eleMax(serie, 2)) #8
>>> print(eleMax(serie, fin =3, debut =1)) #6
"""
def eleMax(lst, debut =0, fin =-1):
    "renvoie le plus grand élément de la liste lst"
    if fin == -1:
        fin = len(lst)
    max, i = 0, 0
    while i < len(lst):
        if (i >= debut and i <= fin and lst[i] > max):
            max = lst[i]
        i += 1
    return max
          
serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]

#print(eleMax(serie)) #9
#print(eleMax(serie, 2, 5)) #7
#print(eleMax(serie, 2)) #8
#print(eleMax(serie, fin =3, debut =1)) #6