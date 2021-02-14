#5.9 Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l’inversant.
#    Ainsi par exemple, « zorglub » deviendra « bulgroz ».

word = "zorglub"    # mot de base a utiliser pour la modification
wordInverted = ""   # nouveau mot a créer
i = len(word)-1     # positionnement à la fin du mot

while i >= 0:
    wordInverted += word[i]
    i -= 1 #decrement i
print(word, "devient", wordInverted)