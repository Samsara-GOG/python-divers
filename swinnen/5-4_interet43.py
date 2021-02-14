"""
Écrivez un programme qui calcule les intérêts accumulés chaque année pendant 20 ans, par
capitalisation d’une somme de 100 euros placée en banque au taux fixe de 4,3 %
"""

somme = 100
intAnnee = somme * (4.30/100) * (12/12)
print("\nPour la somme de", somme, "euros placée en banque au taux fixe de 4,3 %, l'intérêt par année est de", intAnnee, "euros par an.")
int20ans = intAnnee * 20
print("Et sur 20 ans, l'intérêt accumulé s'élève à", int20ans, "euros.")