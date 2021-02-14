"""
6.13 
Convertir une note scolaire N quelconque, entrée par l’utilisateur sous forme de points (par
exemple 27 sur 85), en une note standardisée suivant le code ci-après :
    Note            Appréciation
    N >= 80 %           A
    80 % > N >= 60 %    B
    60 % > N >= 50 %    C
    50 % > N >= 40 %    D
    N < 40 %            E
"""
max = 85

print("Veuillez entrer la note sur 85 à convertir :")
note = eval(input())

def convert_note(note):
    if (note >= 0.8*max) :
        return "A"
    elif (note >= 0.6*max):
        return "B"
    elif (note >= 0.5*max):
        return "C"
    elif (note >= 0.4*max):
        return "D"
    else:
        return "E"
noteConvertie = convert_note(note)
print("La note convertie est", noteConvertie)