from inicio import *

'''
 La funcion ventana2 comprueba mediante un Try, si el frame1 esta cargado, y de ser asi lo quita.
 Queda pendiente diseñar el modo de tener mas de 2 frames
'''

def ventana1(self):

    try:
        self.frame2.pack_forget()
        CreaVentana1(self)
    except AttributeError:
        CreaVentana1(self)

def CreaVentana1(self):
    self.frame1 = Frame(self.root, width=800, height=600)
    self.label1 = Label(self.frame1, text="VENTANA 1")
    self.label1.place(relx=0.5, rely=0.5, anchor=S)
    self.frame1.pack()