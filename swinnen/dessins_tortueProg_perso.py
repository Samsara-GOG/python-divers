#! C:/Users/Jay/Desktop/Python/Python38
# -*- coding:Utf8 -*-
from dessins_tortue_perso import *

"""
7.6 (suite)
Testez votre module à l’aide d’un programme qui fera appel à ces fonctions à plusieurs
reprises, avec des arguments variés pour dessiner une série de carrés et de triangles :
"""
"""
# dessiner cinq carrés rouges, alignés :
i = 0

def fivecarre(i) :
    while i < 5 :
        down() # abaisser le crayon
        carre(25+10*i, 'red', 0) # tracer un carré
        up() # relever le crayon
        forward(65+20*i) # avancer + loin
        i += 1

j = 0
   
def fivetriangle(j) :
    while j < 5 :
        down()
        triangle(30+7*j, 'blue', 0) # tracer un carré
        up()
        forward(77+21*j)
        j += 1

def ninestars(k) :
    while k < 5 :
        down()
        etoile5(55+10*k, 'green', 144)
        up()
        goto(-150, 60)
        k += 1

    while k > 0 :
        down()
        etoile5(55-10*k, 'green', 144)
        up()
        backward(150)
        k -= 1
    b = input()

    
up() # relever le crayon
goto(-200, 50) # reculer en haut à gauche
fivecarre(0)

up()
goto(-170, 50)
fivetriangle(0)

up()
goto(-170, 100)
ninestars(0)

up() # relever le crayon
goto(-250, 50)
    
etoile5(45, 'green', 0)
forward(56)
etoile5(65, 'green', 0)
forward(77)
etoile5(85, 'green', 0)
forward(98)
etoile5(105, 'green', 0)
forward(118)
etoile5(85, 'green', 0)
forward(98)
etoile5(65, 'green', 0)
forward(77)
etoile5(45, 'green', 0)
a = input()
"""

up()                        # relever le crayon
goto(-20, 120)              # positionner le point de départ
tracer(0)                   # ne pas traînasser

# dessiner une série de formes de + en + petites :
i, t = 0, 40
while i < 9:
    carre(t, 'red', 0)      # tracer un carré
    forward(t + 5)          # avancer + loin
    etoile6(t, 'blue', 0)
    forward(t +5)           # avancer + loin
    triangle(t, 'red', 0)
    forward(t +5)           # avancer + loin
    etoile5(t, 'blue', 144)
    forward(t +5)           # avancer + loin

    t -= 3                  # diminuer la taille
    i = i +1

a = input()                 # attendre

