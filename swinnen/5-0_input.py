firstName = input("Entrez votre prénom : ")
print("Bonjour,", firstName)

print("Veuillez entrer un nombre positif quelconque pour un calcul : ", end=" ")
numberPositive = input()            # renvoit tjrs une chaîne de caractère (string)
numberCleaned = int(numberPositive) # conversion de la chaîne en un nombre entier, possibilité float()
print("Le carré de", numberCleaned, "vaut", numberCleaned**2)


a = input("Entrez une donnée numérique: ")
print(type(a))
print("Conversion du string en nombre réel")
b = float(a) # conversion de la chaîne en un nombre réel
print(a, "est désormais de type:", type(b))
