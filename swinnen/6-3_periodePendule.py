"""
6.3 Écrivez un programme qui calcule la période d’un pendule simple de longueur donnée.
La formule qui permet de calculer la période d’un pendule simple est : T = 2*Pi*sqrt(l/g)
l représentant la longueur du pendule et g la valeur de l’accélération de la pesanteur au lieu
d’expérience.

g = 9,8
"""
from math import sqrt

pi = 3.14
g = 9.8
period = 0

print("Calcul de la période d'un pendule simple de longueur donnée")
print("Veuillez entrer la valeur de longueur du pendule en cm :")
lenghtPendulumRaw = input()
lenghtPendulumCm = float(lenghtPendulumRaw)
lenghtPendulumM = lenghtPendulumCm/100 

period = 2*pi*sqrt(lenghtPendulumM/g)
print("La périole de ce pendule de longueur de %.2fcm" %lenghtPendulumCm, "est de %.2fs." %period)


