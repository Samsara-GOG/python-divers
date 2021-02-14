jour = ['lundi', 'mardi', 'mercredi', 1800, 20.357, 'jeudi', 'vendredi']
print(jour) #['lundi', 'mardi', 'mercredi', 1800, 20.357, 'jeudi', 'vendredi']
print(jour[2]) #mercredi
print(jour[4]) #20.357

jour[3] = jour[3] +47
print(jour[3]) #1847
print(jour) #['lundi', 'mardi', 'mercredi', 1847, 20.357, 'jeudi', 'vendredi']
print(len(jour)) #7

del(jour[4])
print(jour) #['lundi', 'mardi', 'mercredi', 1847, 'jeudi', 'vendredi']

jour.append('samedi')
print(jour) # ['lundi', 'mardi', 'mercredi', 1847, 'jeudi', 'vendredi', 'samedi']

jour = ['dimanche','lundi','mardi','mercredi','jeudi','vendredi','samedi']
a, b = 0, 0
while a < 25:
    a = a + 1
    b = a % 7
    print(a, jour[b])