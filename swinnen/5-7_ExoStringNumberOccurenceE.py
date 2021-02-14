#5.7 Écrivez un script qui compte le nombre d’occurrences du caractère « e » dans une chaîne.


# Première méthode
word = "finir"    # Mot à parcourir
countLetter = 0    # Nombre de même lettre trouvé

for letter in word:
    if letter == "e":
        countLetter += 1 
letter = "e"
print("\nLe mot", word, "contient", countLetter ,"fois le caractère", letter)

"""
# Autre méthode
word = "founir"     # Mot à parcourir
letter = "e"       # Lettre à trouver dans le mot
position = 0       # Détermination de la position des lettres
countLetter = 0    # Nombre de même lettre trouvé

while position < len(word):
    if (word[position] == letter):
        countLetter += 1    
    position += 1
    
print("\nLe mot", word, "contient", countLetter, "fois la lettre", letter, end = " ")       
"""   