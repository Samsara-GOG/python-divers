"""
6.14 

Soit la liste suivante :
[ ' Jean-Michel ' , ' Marc ' , ' Vanessa ' , ' Anne ' , 'Maximilien ' ,
' Alexandre-Benoît ' , ' Louise ' ]
Écrivez un script qui affiche chacun de ces noms avec le nombre de caractères correspondant.
"""

names = ['Jean-Michel', 'Marc', 'Vanessa' , 'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise']

for name in names:
    sizeName = len(name)
    print("Le prénom", name, "est composé de", sizeName, "caractères.")