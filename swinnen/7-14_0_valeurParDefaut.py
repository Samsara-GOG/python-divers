# -*- coding: utf-8 -*-
#Prenez la peine d’essayer et de décortiquer cet exemple.

def question(annonce, essais =4, please ='Oui ou non, s.v.p.!'):
    while essais >0:
        reponse = input(annonce)
        if reponse in ('o', 'oui','O','Oui','OUI'):
            return 1
        if reponse in ('n','non','N','Non','NON'):
            return 0
        print(please)
        essais = essais-1

#1    
#rep = question( ' Voulez-vous vraiment terminer ? ' )

#2 
#rep = question( ' Faut-il effacer ce fichier ? ' , 3)

#3
rep = question( ' Avez-vous compris ? ' , 2, ' Répondez par oui ou par non ! ' )