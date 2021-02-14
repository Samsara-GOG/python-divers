# -*- coding: utf-8 -*-

# Petit exercice utilisant la bibliothèque graphique tkinter

from Lib.tkinter import *
from Lib.random import randrange

# --- définition des fonctions gestionnaires d'événements : ---
def drawline():
    "Tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul
    can1.create_line(x1, y1, x2, y2, width=2, fill=coul)
    
    # modification des coordonnées pour la ligne suivante :
    #y2, y1 = y2+10, y1-10
    y2, y1 = y2+10, y1+10 # parallèle
    
def drawline2():
    "Tracera deux lignes rouges en croix au centre du canevas"
    global x3, y3, x4, y4, x5, y5, x6, y6, coul2
    can1.create_line(x3, y3, x4, y4, width=2, fill=coul2) # ligne horizontale de la croix
    can1.create_line(x5, y5, x6, y6, width=2, fill=coul2) # ligne verticale de la croix

def changecolor():
    "Changement aléatoire de la couleur du tracé"
    global coul, coul2
    #pal=['purple','cyan','maroon','green','red','blue','orange','yellow'] # => génère un nombre aléatoire de 0 à 7
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c = randrange(1, 4) # => couleurs cyan, marron et green
    coul = pal[c]
    coul2 = pal[4] #couleur rouge pour la croix
    
#------ Programme principal -------

# les variables suivantes seront utilisées de manière globale :
#x1, y1, x2, y2 = 10, 190, 190, 10 # coordonnées de la ligne
#x1, y1, x2, y2 = 0, 0, 200, 0 # lignes tracées horizontales et parallèles 
x1, y1, x2, y2 = 0, 0, 650, 0 # extrémités se confondent avec les bords du canevas à 650
coul = 'dark green' # couleur de la ligne
x3, y3, x4, y4 = 0, 325, 650, 325 # coordonnées de la ligne Horizontale
x5, y5, x6, y6 = 250, 0, 250, 650 # coordonnées de la ligne Verticale
coul2 = 'red'

# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
#can1 = Canvas(fen1, bg='dark grey', height=200, width=200)
can1 = Canvas(fen1, bg='dark grey', height=650, width=500) #hauteur de 650 et largeur de 500
can1.pack(side=LEFT)
bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Tracer une ligne', command=drawline)
bou2.pack()
bou3 = Button(fen1, text='Autre couleur', command=changecolor)
bou3.pack()
bou4 = Button(fen1, text='Viseur', command=drawline2) # Ajout d'un bouton viseur
bou4.pack()

fen1.mainloop() # démarrage du réceptionnaire d’événements

fen1.destroy() # destruction (fermeture) de la fenêtre