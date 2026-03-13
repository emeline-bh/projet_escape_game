""" Description: 
    - Contient epreuves devniettes  
    - Contient epreuves devniettes

"""
from tkinter import *

#creation de la fenetre, nom, taille, logo, couleur
salle2= Tk()

salle2.title ("Escape game - Salle 2 ")

salle2.geometry("500x500")
salle2.minsize(300,200)
                                                                                  
#salle2.iconbitmap("logo.ico")

salle2.config(background="#c6a7da")
salle2.grid_columnconfigure((0,1,2), minsize=20 ,weight= 1)
salle2.grid_rowconfigure((0,1,2),minsize=20, weight=1 )
#================================================================ EPREUVE DEVINETTE=====================================================

#bouton Epreuve devinette  
button = Button (salle2,text = "devine")
button.grid(row=6, column=6)

cadre = Frame (salle2, bg= "#617e9d", bd=4,relief=SUNKEN)











#Boucle principale 
salle2.mainloop()