#! /usr/bin/env python
# -*- coding:Utf8 -*-

"""
7.5 Définissez une fonction maximum(n1,n2,n3) qui renvoie le plus grand de 3 nombres n1, n2,
n3 fournis en arguments. Par exemple, l’exécution de l’instruction :
print(maximum(2,5,4)) doit donner le résultat : 5.
"""

def maximum(n1, n2, n3) :
    "Nombre maximum entre 3 nombres"
    if n1 > n2 and n1 > n3 :
        return n1
    elif n2 > n1 and n2 > n3 :
        return n2
    else :
        return n3
        
# test :
print(maximum(2,5,4))
print(maximum(4.5, 5.7, 3.9))
print(maximum(8.2, 2.1, 6.7))
print(maximum(1.3, 4.8, 7.6))