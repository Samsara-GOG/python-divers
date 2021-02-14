"""
7.11 
Définissez une fonction nomMois(n) qui renvoie le nom du énième mois de l’année.
Par exemple, l’exécution de l’instruction :
print(nomMois(4)) doit donner le résultat : Avril.
"""

def nomMois(n):
    "renvoie le nom du n-ième mois de l'année"
    mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet',
            'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    return mois[n-1] # les indices sont numérotés à partir de zéro

print(nomMois(12))

