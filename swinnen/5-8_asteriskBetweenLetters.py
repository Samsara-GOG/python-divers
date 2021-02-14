# 5.8 
# Écrivez un script qui recopie une chaîne (dans une nouvelle variable), en insérant des
# astérisques entre les caractères.
# Ainsi par exemple, « gaston » devra devenir « g*a*s*t*o*n »

"""
word = "gaston"
for letter in word:
    #print(letter, end = " ")
"""

word = "gaston"     # mot a modifier dans une nouvelle variable
wordAsterisk = ""   # variable pour le nouveau mot
i = 0               # compteur indice

while i < len(word):
    if i == 0:
        wordAsterisk += word[i]  
    else:  
        wordAsterisk += "*"+word[i]
    i += 1
print(word, "devient", wordAsterisk)
    
