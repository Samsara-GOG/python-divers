"""
5.15 Écrivez un programme qui analyse un par un tous les éléments d’une liste de mots (par
exemple : [ ' Jean ' , ' Maximilien ' , ' Brigitte ' , ' Sonia ' , ' Jean-Pierre ' , ' Sandra ' ] ) pour
générer deux nouvelles listes. L’une contiendra les mots comportant moins de 6 caractères,
l’autre les mots comportant 6 caractères ou davantage.
"""

names = ['Jean' , 'Maximilien' , 'Brigitte' , 'Sonia' , 'Jean-Pierre' , 'Sandra']
i = 0
namesMoreSixChr = []
nameslessSixChr = []

while i < len(names):
    if (len(names[i]) < 6):
        nameslessSixChr.append(names[i])
    elif (len(names[i]) >= 6):
        namesMoreSixChr.append(names[i])
    i += 1
    
print("Noms avec plus de 6 lettres:", namesMoreSixChr)
print("Noms avec moins de 6 lettres:", nameslessSixChr)