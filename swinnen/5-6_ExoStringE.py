#5.6 Écrivez un script qui détermine si une chaîne contient ou non le caractère « e »
"""
# Première méthode
word = "élève"
for letter in word:
    if letter == "e":
        print("Le mot", word, "contient le caractère", letter)
"""
# Autre méthode
word = "eleve"   # Mot à parcourir
letter = "e"       # Lettre à trouver dans le mot
position = 0       # Détermination de la position des lettres
flag = 0           # Signal si lettre découverte

while position < len(word):
    if (word[position] == letter):
        flag += 1    
    position += 1
print("\nLe mot", word, end = " ")       
        
if (flag > 0):
    print("contient la lettre", letter)
else:
    print("ne contient pas la lettre", letter)