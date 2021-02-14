# -*- coding: utf-8 -*-

"""
7.12 
Définissez une fonction inverse(ch) qui permette d’inverser les l’ordre des caractères d’une
chaîne quelconque. La chaîne inversée sera renvoyée au programme appelant.
"""
def inverse(ch):
    "Inverse l’ordre des caractères d’une chaîne quelconque"
    ch2 = ""  #chaîne inversée
    i = len(ch)-1     # positionnement à la fin du mot
    
    while i >= 0:
        ch2 += ch[i]
        i -= 1 #decrement i
    return(ch, "devient", ch2)

liste = "Ziza" #chaîne à inverser
print(inverse(liste))

"""
#Autre façon
def inverse(ch):
    "Inverse l’ordre des caractères d’une chaîne quelconque"
    ch2 = ""  #chaîne inversée
    i = len(word)-1     # positionnement à la fin du mot
    
    for lettre in reversed(ch):
        ch2 += lettre
    return ch2
"""