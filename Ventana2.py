from inicio import *
from tkinter import messagebox

'''
 La funcion ventana2 comprueba mediante un Try, si el frame1 esta cargado, y de ser asi lo quita.
 Queda pendiente diseñar el modo de tener mas de 2 frames
'''

def ventana2(self):

    try:
        self.root.pack_slaves()[0].destroy()
        CreaVentana2(self)
    except IndexError:
        CreaVentana2(self)


def CreaVentana2(self):
    self.frame2 = Frame(self.root, width=800, height=600)
    self.label2 = Label(self.frame2, text="VENTANA 2")
    self.label2.place(relx=0.5, rely=0.5, anchor=S)
    self.frame2.pack()
