"""
6.15 

Écrire une boucle de programme qui demande à l’utilisateur d’entrer des notes d’élèves. La
boucle se terminera seulement si l’utilisateur entre une valeur négative. Avec les notes ainsi
entrées, construire progressivement une liste. Après chaque entrée d’une nouvelle note (et
donc à chaque itération de la boucle), afficher le nombre de notes entrées, la note la plus
élevée, la note la plus basse, la moyenne de toutes les notes."""

from statistics import mean

note = 0

print("Rappel : Le programme s'arrêtera automatiquement si vous entrez une note négative.")
notes = []

while note >= 0:
    print("Veuillez entrer une note d'un élève")
    note = float(input())
    if note < 0:
        print("OK. Arrêt du programme.")
    else:
        notes.append(note)
        quantityNotes = len(notes)
        maxNote = max(notes)
        minNote = min(notes)
        averageNote = mean(notes)
        print("Nombre de notes entrée(s) :", quantityNotes)
        print("Note la plus élevée : %.2f" %maxNote)
        print("Note la plus faible : %.2f" %minNote)
        print("Moyenne de toutes les notes : %.2f" %averageNote)
    
