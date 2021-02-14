"""
6.2 Écrivez un programme qui calcule le périmètre et l’aire d’un triangle quelconque dont l’utilisa-
teur fournit les 3 côtés.
(Rappel : l’aire d’un triangle quelconque se calcule à l’aide de la formule :
s=sqrt(d*(d-a)*(d-b)*(d-c))
dans laquelle d désigne la longueur du demi-périmètre, et a, b, c celles des trois côtés.)
"""
from math import sqrt

print("Calcul du périmètre et de la surface d'un triangle quelconque")
print("Veuillez fournir les mesures des 3 côtés du triangle:")
print("Premier côté du triangle:")
aRaw = input()
a = float(aRaw)
print("Deuxième côté du triangle:")
bRaw = input()
b = float(bRaw)
print("Troisième côté du triangle:")
cRaw = input()
c = float(cRaw)

# périmètre: a + b + c
p = a + b + c
# demipérimètre: périmètre/2
d = p/2

#Calcul Aire s=sqrt(d*(d-a)*(d-b)*(d-c))
s = sqrt(d*(d-a)*(d-b)*(d-c))
                     
print("Le périmètre de ce triangle est de %.2f" %p, end = " ") 
print ("et sa surface est de %.2f." %s)