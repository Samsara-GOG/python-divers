from turtle import *

"""
reset()             On efface tout et on recommence
goto(x, y)          Aller à l’endroit de coordonnées x, y
forward(distance)   Avancer d’une distance donnée
backward(distance)  Reculer
up()                Relever le crayon (pour pouvoir avancer sans dessiner)
down()              Abaisser le crayon (pour recommencer à dessiner)
color(couleur)      couleur peut être une chaîne prédéfinie (’red’, ’blue’, etc.)
left(angle)         Tourner à gauche d’un angle donné (exprimé en degrés)
right(angle)        Tourner à droite
width(épaisseur)    Choisir l’épaisseur du tracé
fill(1)             Remplir un contour fermé à l’aide de la couleur sélectionnée
write(texte)        Texte doit être une chaîne de caractères
"""

def forme(n, a, taille, couleur, angle):
    "forme de base, avec n = nombre de côtés, a = angle des sommets"
    down()              # abaisser le crayon
    right(angle)        # choisir une orientation de départ
    color(couleur)      # ainsi qu'une couleur de tracé
    # tracer la forme graphique proprement dite :
    c =0
    while c < n:
        forward(taille)
        right(a)
        c = c +1
    up()
    
def etoile6(taille, couleur, angle):
    # dessiner un premier triangle équilatéral :
    forme(3, 120, taille, couleur, angle)
    # repositionner le crayon :
    left(30)
    forward(taille/1.732)       # 1.732 = 2 * cos(30°)
    # dessiner le second triangle, après rotation :
    right(90)
    forme(3, 120, taille, couleur, angle)
    # si l'on veut retrouver l'orientation initiale :
    #left(60)
    
"""
etoile6(50, ('red'), 120)
etoile6(50, ('blue'), 120)
etoile6(50, ('green'), 120)
"""

# Etoile
"""
a = 0
while a < 12:
    a += 1
    forward(150)
    left(150)
"""
    
# Un carré  
"""  
a = 0        
while a < 4:
    a += 1
    forward(50)
    left(90)
"""
    
# Un rectangle
"""
a = 0        
while a < 2:
    a += 1
    left(90)
    forward(25)
    left(90)
    forward(50)
"""
   
# Un triangle
"""
a = 0
while a < 3:
    color('red')
    forward(50)
    left(120)
    a += 1 
"""
 
# Un losange
"""
a = 0        
while a < 2:
    a += 1
    right(120)   
    forward(50)
    
while a < 4:
    a += 1
    right(60)
    forward(50)
    right(60)
"""
# Un cercle

# Un hexagone
"""
a = 0        
while a < 6:
    a += 1
    forward(50)
    left(60)
"""

