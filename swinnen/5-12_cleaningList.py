#5.12   Écrivez un programme qui affiche « proprement » tous les éléments d’une liste. 
#       Si on l’appliquait par exemple à la liste t2 de l’exercice ci-dessus, on devrait obtenir :
#       Janvier Février Mars Avril Mai Juin Juillet Août Septembre Octobre Novembre Décembre

t2 = [ ' Janvier ' , ' Février ' , ' Mars ' , ' Avril ' , ' Mai ' , ' Juin ' ,
' Juillet ' , ' Août ' , ' Septembre ' , 'Octobre ' , ' Novembre ' , ' Décembre ' ]

i = 0

print("Avant:", t2)
print("Après:", end = " ")

while i < len(t2):
    print(t2[i], end = " ")
    i += 1