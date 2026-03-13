""" Description: 
    - Contient epreuve devinette
    - Contient epreuve cle

"""
from tkinter import *
from main import * 

#creation de la fenetre, nom, taille, logo, couleur
salle2= Frame (grande_fenetre, bg= "#617e9d", bd=4,relief=SUNKEN)
                                                                
salle2.grid_columnconfigure((0,1,2), minsize=20 ,weight= 1)
salle2.grid_rowconfigure((0,1,2),minsize=20, weight=1 )
#================================================================ EPREUVE DEVINETTE=====================================================

#bouton Epreuve devinette  
button = Button (salle2,text = "devine")
button.grid(row=6, column=6)








#================================================================ EPREUVE CLE =====================================================


#bouton Epreuve cle 
button = Button (salle2,text = "trouve")
button.grid(row=5, column=5)

cadre = Frame (salle2, bg= "#617e9d", bd=4,relief=SUNKEN)








#Boucle principale 
salle2.mainloop()