"""
print("Veuillez entrer le chiffre désiré pour l'affichage de sa table de multiplication :\n")
number = int(input())

def multiplUniv(table):
    print("Fragment de la table de multiplication de", table)
    i = 1
    while i < 11:
        number = i*table
        print("%s x %s" %(i, table), "=", number)
        i += 1
        
multiplUniv(number)
"""

"""
#Utilisation d’une variable comme argument

a = 1
while a<30 :
    multiplUniv(a)
    a += 1
"""


#Corrigé

def table(base):
    n = 1
    while n <11 :
        print(n * base, end =' ')
        n += 1
  
"""  
a = 1
while a <20:
    table(a)
    a += 1
"""

def tableMulti(base, debut, fin):
    print('Fragment de la table de multiplication par', base, ':')
    n = debut
    while n <= fin :
        print(n, 'x', base, '=', n * base)
        n += 1 
"""        
#tableMulti(5, 10, 20)
"""

t, d, f = 11, 5, 10
while t<21:
    tableMulti(t,d,f)
    t, d, f = t +1, d +3, f +5
