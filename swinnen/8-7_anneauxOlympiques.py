"""
8.7 
a) Créez un court programme qui dessinera les 5 anneaux olympiques dans un rectangle de
fond blanc (white). Un bouton <Quitter> doit permettre de fermer la fenêtre.

b) Modifiez le programme ci-dessus en y ajoutant 5 boutons. Chacun de ces boutons
provoquera le tracé de chacun des 5 anneaux
"""
# -*- coding: utf-8 -*-

# Petit exercice utilisant la bibliothèque graphique tkinter

from Lib.tkinter import *

# --- définition des fonctions gestionnaires d'événements : ---
def drawredcircle():
    "Tracé d'un anneau rouge dans le canevas can1"
    global x1, y1, x2, y2
    can1.create_oval(x1, y1, x2, y2, width=8, fill='', outline='red')
    
def drawblackcircle():
    "Tracé d'un anneau noir dans le canevas can1"
    global x3, y3, x4, y4
    can1.create_oval(x3, y3, x4, y4, width=8, fill='', outline='black')
    
def drawbluecircle():
    "Tracé d'un anneau bleu dans le canevas can1"
    global x5, y5, x6, y6
    can1.create_oval(x5, y5, x6, y6, width=8, fill='', outline='blue')
    
def drawgreencircle():
    "Tracé d'un anneau vert dans le canevas can1"
    global x7, y7, x8, y8
    can1.create_oval(x7, y7, x8, y8, width=8, fill='', outline='green')
    
def drawyellowcircle():
    "Tracé d'un anneau jaune dans le canevas can1"
    global x9, y9, x10, y10
    can1.create_oval(x9, y9, x10, y10, width=8, fill='', outline='orange')
 
#------ Programme principal -------

# les variables suivantes seront utilisées de manière globale :
x1, y1, x2, y2 = 342, 58, 442, 158 # coordonnées de l'anneau rouge
x3, y3, x4, y4 = 225, 58, 325, 158 # coordonnées de l'anneau noir
x5, y5, x6, y6 = 108, 58, 208, 158 # coordonnées de l'anneau bleu
x7, y7, x8, y8 = 275, 110, 375, 210 # coordonnées de l'anneau vert
x9, y9, x10, y10 = 165, 110, 265, 210 # coordonnées de l'anneau jaune

# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1, bg='white', height=250, width=500) #hauteur de 250 et largeur de 500
can1.pack(side=LEFT)
bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Tracer un anneau rouge', command=drawredcircle)
bou2.pack()
bou3 = Button(fen1, text='Tracer un anneau noir', command=drawblackcircle)
bou3.pack()
bou4 = Button(fen1, text='Tracer un anneau bleu', command=drawbluecircle)
bou4.pack()
bou5 = Button(fen1, text='Tracer un anneau vert', command=drawgreencircle)
bou5.pack()
bou6 = Button(fen1, text='Tracer un anneau jaune', command=drawyellowcircle)
bou6.pack()

fen1.mainloop() # démarrage du réceptionnaire d’événements

fen1.destroy() # destruction (fermeture) de la fenêtre


"""
Correction :

#! /usr/bin/env python
# -*- coding:Utf8 -*-

# Anneaux olympiques - version compacte.

from Lib.tkinter import *

# Coordonnées X,Y des 5 anneaux :
coord = [[20,30], [120,30], [220, 30], [70,80], [170,80]]
# Couleurs des 5 anneaux :
coul = ["red", "yellow", "blue", "green", "black"]

base = Tk()
can = Canvas(base, width =335, height =200, bg ="white")
can.pack()
bou = Button(base, text ="Quitter", command =base.quit)
bou.pack(side = RIGHT)
# Dessin des 5 anneaux :
i = 0
while i < 5:
    x1, y1 = coord[i][0], coord[i][1]
    can.create_oval(x1, y1, x1+100, y1 +100, width =2, outline =coul[i])
    i = i +1
base.mainloop()

"""


"""
#! /usr/bin/env python
# -*- coding:Utf8 -*-

# Anneaux olympiques - Variante dessinant chaque anneau séparém.

from Lib.tkinter import *

# Fonctions pour dessiner les 5 anneaux :

def dessineCercle(i):
    x1, y1 = coord[i][0], coord[i][1]
    can.create_oval(x1, y1, x1+100, y1 +100, width =2, outline =coul[i])

def a1():
    dessineCercle(0)

def a2():
    dessineCercle(1)

def a3():
    dessineCercle(2)

def a4():
    dessineCercle(3)

def a5():
    dessineCercle(4)

##### Programme principal : ##########

# Coordonnées X,Y des 5 anneaux :
coord = [[20,30], [120,30], [220, 30], [70,80], [170,80]]
# Couleurs des 5 anneaux :
coul = ["red", "yellow", "blue", "green", "black"]

base = Tk()
can = Canvas(base, width =335, height =200, bg ="white")
can.pack()
bou = Button(base, text ="Quitter", command =base.quit)
bou.pack(side = RIGHT)

# Installation des 5 boutons :
Button(base, text='1', command = a1).pack(side =LEFT)
Button(base, text='2', command = a2).pack(side =LEFT)
Button(base, text='3', command = a3).pack(side =LEFT)
Button(base, text='4', command = a4).pack(side =LEFT)
Button(base, text='5', command = a5).pack(side =LEFT)
base.mainloop()
"""