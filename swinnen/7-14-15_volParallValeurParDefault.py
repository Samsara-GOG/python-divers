# -*- coding: utf-8 -*-

"""7.4 Définissez une fonction volBoite(x1,x2,x3) qui renvoie le volume d’une boîte
parallélépipédique dont on fournit les trois dimensions x1, x2, x3 en arguments.
Par exemple, l’exécution de l’instruction :
print(volBoite(5.2, 7.7, 3.3)) doit donner le résultat : 132.132.

7.14 Modifiez la fonction volBoite(x1,x2,x3) que vous avez définie dans un exercice précédent, de manière à ce qu’elle puisse être appelée avec trois, deux, un seul, ou même aucun argument.
Utilisez pour ceux ci des valeurs par défaut égales à 10.

Par exemple :
print(volBoite()) doit donner le résultat : 1000
print(volBoite(5.2)) doit donner le résultat : 520.0
print(volBoite(5.2, 3)) doit donner le résultat : 156.0

7.15 Modifiez la fonction volBoite(x1,x2,x3) ci-dessus de manière à ce qu’elle puisse être appelée avec un, deux, ou trois arguments. Si un seul est utilisé, la boîte est considérée comme cubique (l’argument étant l’arête de ce cube). Si deux sont utilisés, la boîte est considérée comme un prisme à base carrée (auquel cas le premier argument est le côté du carré, et le second la hauteur du prisme). Si trois arguments sont utilisés, la boîte est considérée comme un parallélépipède. 

Par exemple :
print(volBoite()) doit donner le résultat : -1 (indication d’une erreur)
print(volBoite(5.2)) doit donner le résultat : 140.608
print(volBoite(5.2, 3)) doit donner le résultat : 81.12
print(volBoite(5.2, 3, 7.4)) doit donner le résultat : 115.44
"""

def volBoite(x1 =-1, x2 =-1, x3 =-1) :
    "Calcul du Volume d'une boîte cubique, prisme à base carrée et parallépipède"

    if x1 == -1 :
        return x1                     # aucun argument
    elif x2 == -1 :
        return round(x1**3, 3)        # un argument -> boite cubique
    elif x3 == -1 :
        return round(x1 * x1 * x2, 3) # deux arguments -> boîte prismatique
    else :
        return round(x1*x2*x3, 3)
        

#print(volBoite(5.2, 3, 7.4))
#print(volBoite())
#print(volBoite(5.2))
#print(volBoite(5.2, 3))

#print(volBoite())
#print(volBoite(5.2))
#print(volBoite(5.2, 3))
#print(volBoite(5.2, 3, 7.4))