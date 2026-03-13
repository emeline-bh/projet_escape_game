""" Description 
    - Local escape game (fentre principale + salle 1 + salle 2)
     
"""
from tkinter import * 
grande_fenetre= Tk()
grande_fenetre.title ("Escape game")

grande_fenetre.geometry("1500x1500")
grande_fenetre.minsize(300,200)
grande_fenetre.iconbitmap("logomaison.ico")
grande_fenetre.config(background="#000000")

grande_fenetre.grid_columnconfigure((0,1,2), minsize=20 ,weight= 1)
grande_fenetre.grid_rowconfigure((0,1,2),minsize=20, weight=1 )

# affichage du texte de bienvenue 
bienvenue = Label(
    grande_fenetre,
    text="Bienvenue dans notre escape game !!",
    font=("Calibri", 16),
    fg="white",
    bg= "#262020"
)

bienvenue.grid(row= 2, column=3)

        
grande_fenetre.mainloop()
