"""
6.11 
Demander à l’utilisateur d’entrer trois longueurs a, b, c. À l’aide de ces trois longueurs,
déterminer s’il est possible de construire un triangle. Déterminer ensuite si ce triangle est
rectangle, isocèle, équilatéral ou quelconque. Attention : un triangle rectangle peut être
isocèle.
"""
print("\nCréationd d'un triangle\n")
print("Veuillez entrer trois valeurs pour les longueurs du triangle sous forme a, b, c :")
a, b, c = eval(input())

# Il n'est possible de construire un triangle que si chaque côté 
# a une longueur inférieure à la somme des deux autres : 
if a < (b+c) and b < (a+c) and c < (a+b) : 
  print("Ces trois longueurs déterminent bien un triangle.") 
else: 
  print("Il est impossible de construire un tel triangle !") 
  exit()      # ainsi l'on n'ira pas plus loin.
  
f = 0
if a == b and b == c :
    print("Ce triangle est équilatéral.")
    f = 1
elif a == b or b == c or c == a :
    print("Ce triangle est isocèle.")
    f = 1
    
if a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b :
    print("Ce triangle est rectangle.")
    f = 1
if f == 0 :
    print("Ce triangle est quelconque.")
    
    
"""
#########  Variante ? (proposée par Alex Misbah) ######### :
print("* Variante ? (par Alex Misbah) *")
a=eval(input('entrer une longueur a:'))
b=eval(input('entrer une longueur b:'))
c=eval(input('entrer une longueur c:'))

ab_carre=(a*b)**2
pytha=(b*c)**2+(c*a)**2

if a<(b+c) and b<(a+c) and c <(a+b):
    print(" les longueurs définissent un triangle")
    if ab_carre == pytha:
        print(" c'est un triangle rectangle")
    elif a == b == c:
        print(" c'est un triangle équilatéral")
    elif a == b or b == c or c == a:
        print("c'est un triangle isocèle")
    else:
        print("c'est un triangle quelconque")
else:
    print("les longueurs a,b et c ne permettent pas de définir un triangle")
"""
    


