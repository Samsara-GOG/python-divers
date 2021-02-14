"""
7.9 Définissez une fonction compteCar(ca,ch) qui renvoie le nombre de fois que l’on rencontre le
caractère ca dans la chaîne de caractères ch. Par exemple, l’exécution de l’instruction :
print(compteCar(’e’, ’Cette phrase est un exemple’)) doit donner le résultat : 7
"""

def compteCar(ca, ch):
    "Renvoie le nombre de caractères ca trouvés dans la chaîne ch"
    sum = 0
    for i in ch:
        if i == ca:
            sum += 1
    return sum

print(compteCar("e", "Cette phrase est un exemple"))

"""
Solution:

#! /usr/bin/env python
# -*- coding:Utf8 -*-

def compteCar(ca, ch):
    "Renvoie le nombre de caractères ca trouvés dans la chaîne ch"
    i, tot = 0, 0
    while i < len(ch):
        if ch[i] == ca:
            tot = tot + 1
        i = i + 1
    return tot    
        
# test :
print(compteCar("e","Cette chaîne est un exemple"))
"""