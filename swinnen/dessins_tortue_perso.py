#! /usr/bin/env python
# -*- coding:Utf8 -*-

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

7.6 Complétez le module de fonctions graphiques dessins_tortue.py décrit à la page 71.
Commencez par ajouter un paramètre angle à la fonction carre(), de manière à ce que les
carrés puissent être tracés dans différentes orientations.
Définissez ensuite une fonction triangle(taille, couleur, angle) capable de dessiner un
triangle équilatéral d’une taille, d’une couleur et d’une orientation bien déterminées.
"""

from turtle import *

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

def carre(taille, couleur, angle):
    "Fonction qui dessine un carré de taille et de couleur déterminées"
    right(angle)
    color(couleur)
    d = 0
    while d < 4:
        forward(taille)
        right(90)
        d += 1
        
#carre(100, ('red'), 0)

def triangle(taille, couleur, angle):
    "Fonction qui dessine un triangle de taille et de couleur déterminées"
    right(angle)
    color(couleur)
    c = 0
    while c < 3:
        forward(taille)
        right(120)
        c += 1
    

#triangle(100, ('blue'), 0)    

def etoile5(taille, couleur, angle):
    forme(5, 144, taille, couleur, angle)
    # 144° = 180° - 360°/10
    
#etoile5(55, 'green', 144)
    
def etoile6(taille, couleur, angle):
    down()
    triangle(100, ('blue'), 0)  
    up()
    left(30)
    forward(taille/1.732)
    right(180)
    down()    
    triangle(100, ('blue'), 270)
    up()
   

"""       
def essai() :
    "Cette fonction est bien documentée mais ne fait presque rien."
    print("Rien à signaler")
    
essai()
print(essai.__doc__)
"""