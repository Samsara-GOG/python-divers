# -*- coding: utf-8 -*-
"""
7.13 Définissez une fonction compteMots(ph) qui renvoie le nombre de mots contenus dans la
phrase ph. On considère comme mots les ensembles de caractères inclus entre des espaces.
"""
def compteMots(ph):
    "Renvoit le nombre de mots contenus dans la phrase ph"
    i, sum = 0, 0
    while i < len(ph):
        if ph[i] != " " :
            sum += 1
        i += 1
    return ("Le nombre de mots contenus dans la phrase s'élève à : %d." %sum)
               
print(compteMots("Momo Mamie"))
        