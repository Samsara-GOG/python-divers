def cube(w):
    #print ("%s x %s x %s = %s" %(w, w, w, w**3))
    return w**3
#print(cube(9))

def volumeSphere(r):
    return 4 * 3.1416 * cube(r) / 3

r = input('Entrer la valeur du rayon : ')
print('Le volume de cette sphère vaut', volumeSphere(float(r)))

def table(base):
    resultat = [] # resultat est d’abord une liste vide
    n = 1
    while n < 11:
        b = n * base
        resultat.append(b) # ajout d’un terme à la liste
        n = n +1 # (voir explications ci-dessous)
    return resultat
"""
ta9 = table(9)
print(ta9[0])
print(ta9[3])
print(ta9[2:5])

print("\n")

print(table(9))
print(table(9)[3])
cube(9)
"""