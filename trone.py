from tkinter import*
import tkinter as tk
# procédure générale de déplacement :
def avance(gd, hb):
     global x1, y1
     x1, y1 = x1 +gd, y1 +hb
     can1.coords(oval1, x1,y1, x1+30,y1+30)
# gestionnaires d'événements :
def depl_gauche(event):
     avance(-10, 0)
def depl_droite(event):
     avance(10, 0)
def depl_haut(event):
     avance(0, -10)
def depl_bas(event):
     avance(0, 10)
#------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
x1, y1 = 10, 10 # coordonnées initiales
# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")
# création des widgets "esclaves" :
app = tk.Tk()
can1 = Canvas(fen1,bg='dark grey',height=300,width=300)
oval1 = can1.create_oval(x1,y1,x1+30,y1+30,width=2,fill='red')
can1.pack(side=LEFT)
Button(fen1,text='Quitter',command=fen1.quit).pack(side=BOTTOM)
app.bind("<KeyPress-d>",depl_gauche)
app.bind("<KeyPress-s>",depl_droite)
app.bind("<KeyPress-z>",depl_haut)
app.bind("<KeyPress-x>",depl_bas)
# démarrage du réceptionnaire d’évènements (boucle principale) :
fen1.mainloop()
