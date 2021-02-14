"""
6.16 
Écrivez un script qui affiche la valeur de la force de gravitation s’exerçant entre deux masses
de 10 000 kg , pour des distances qui augmentent suivant une progression géométrique de
raison 2, à partir de 5 cm (0,05 mètre).

La force de gravitation est régie par la formule F = 6.67E-11 * m*m' / d*d

Exemple d’affichage :
    d = .05 m : la force vaut 2.668 N
    d = .1 m : la force vaut 0.667 N
    d = .2 m : la force vaut 0.167 N
    d = .4 m : la force vaut 0.0417 N
    etc.

"""
a = 10000
b = 10000
distance = .05

while distance < 20:
    force = 6.67E-11 * a*b / (distance*distance)
    print("d =", distance, "m : la force vaut %.4f" %force, "N.")
    distance *= 2
