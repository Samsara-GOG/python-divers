"""
Vous pouvez remplacer le séparateur par défaut (l’espace) par un autre caractère quelconque (ou
même par aucun caractère), grâce à l’argument sep . Exemple :
"""

print("Bonjour", "à", "tous", sep ="*") # Bonjour*à*tous
print("Bonjour", "à", "tous", sep ="") #Bonjouràtous

# De même, vous pouvez remplacer le saut à la ligne par l’argument end :
n = 0
while n < 6:
    print("zut", end ="") # zutzutzutzutzut
    n += 1
