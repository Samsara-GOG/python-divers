"""7.3 Définissez une fonction surfCercle(R). Cette fonction doit renvoyer la surface (l’aire) d’un
cercle dont on lui a fourni le rayon R en argument. Par exemple, l’exécution de l’instruction :
print(surfCercle(2.5)) doit donner le résultat : 19.63495..."""

from math import pi

def surfCercle(r) :
    "Calcul de la surface d'un Cercle avec son rayon"
    float(r)
    surface = pi * r**2
    return round(surface, 5)

print(surfCercle(2.5))