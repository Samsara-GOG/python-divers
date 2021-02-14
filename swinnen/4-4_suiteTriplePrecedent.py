"""
Écrivez un programme qui affiche une suite de 12 nombres dont chaque terme soit égal au
triple du terme précédent.
"""

count, numPrev, numNext, = 1, 1, 1

print("\nSuite de 12 nombres dont chaque terme soit égal au triple du terme précédent\n")
while count <= 12:
    print(numNext, end = " ")
    numPrev, numNext, count = numNext, numNext*3, count+1