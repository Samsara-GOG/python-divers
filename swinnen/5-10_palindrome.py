#5.10   En partant de l’exercice précédent, écrivez un script qui détermine si une chaîne de caractères
#       donnée est un palindrome (c’est-à-dire une chaîne qui peut se lire indifféremment dans les
#       deux sens), comme par exemple « radar » ou « s.o.s ».

word = "radar"    # mot de base a utiliser pour la modification
word2 = "fournir"   # autre mot à tester
wordInverted = ""   # nouveau mot a créer
wordInverted2 = ""   # nouveau mot a créer
i = len(word)-1     # positionnement à la fin du mot

while i >= 0:
    wordInverted += word[i]
    wordInverted2 += word2[i]
    i -= 1 #decrement i
    
if word == wordInverted:
    print("\nLe mot", word, "est un palindrome.")
else:
    print("Le mot", word, "n'est pas un palindrome.")
    
print(word, "devient", wordInverted)
    
if word2 == wordInverted2:
    print("Le mot", word2, "est aussi un palindrome.") 
else:
    print("Le mot", word2, "n'est pas un palindrome.")
    
print(word2, "devient", wordInverted2)