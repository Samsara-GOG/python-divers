"""6.10 
Demander à l’utilisateur son nom et son sexe (M ou F). En fonction de ces données, afficher
« Cher Monsieur » ou « Chère Mademoiselle » suivi du nom de la personne."""

print("Détermination du sexe et phrase personnalisée")
print("Quel est votre nom ?")
name = input()
print("Quel est votre sexe ? (M ou F)")
gender = input()

if gender == "M":
    print("Cher Monsieur", end = " ")
elif gender == "F":
    print("Chère Mademoiselle", end = " ")
else:
    print("Veuillez entrer un type de sexe M ou F")
print(name)