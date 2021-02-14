"""5.11 Soient les listes suivantes :
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = [ ' Janvier ' , ' Février ' , ' Mars ' , ' Avril ' , ' Mai ' , ' Juin ' ,
' Juillet ' , ' Août ' , ' Septembre ' , 'Octobre ' , ' Novembre ' , ' Décembre ' ]
Écrivez un petit programme qui crée une nouvelle liste t3. Celle-ci devra contenir tous les
éléments des deux listes en les alternant, de telle manière que chaque nom de mois soit suivi
du nombre de jours correspondant :
[ ' Janvier ' ,31, ' Février ' ,28, ' Mars ' ,31, etc...].
"""

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = [ ' Janvier ' , ' Février ' , ' Mars ' , ' Avril ' , ' Mai ' , ' Juin ' ,
' Juillet ' , ' Août ' , ' Septembre ' , 'Octobre ' , ' Novembre ' , ' Décembre ' ]
monthsDays = [] # nouvelle liste à remplir en fusionnant les listes days et months
j = 0           #indice pour parcourir les listes

while j < len(days):
    monthsDays.append(months[j])
    monthsDays.append(days[j])
    j += 1
print(monthsDays)
    

