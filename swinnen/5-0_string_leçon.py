#concatenation string
a = 'Petit poisson '
b = 'deviendra grand'
c = a + b
print(c)

#fonction length d'un string len()
ch = 'Georges'
print("Longueur de ", ch, ":", len(ch))

ch2 ='René'
print("Longueur de", ch2, ":", len(ch2))

#Convertir en nombre véritable une chaîne de caractères qui représente un nombre. Exemple :
ch3 = '8647'
#print(ch3 + 45) #erreur: on ne peut pas additionner une chaîne et un nombre

#converti la chaine en nombre entier avec int()
n = int(ch3)
print(n + 65)

#converti la chaine en nombre réel avec float()
z = '1000'
y = float(z)
print(y + 2.5)
