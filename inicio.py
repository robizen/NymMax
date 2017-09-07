from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import Ventana1
import Ventana2

class Aplicacion():
    def __init__(self):
        #diseño de la ventana
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.resizable(0,0)
        self.root.title("NymMax 0.1 Home Edition")

        ####################
        #   MENU PRINCIPAL #
        ####################

        menubar = Menu(self.root)
        # pestaña archivo
        archivomenu = Menu(menubar, tearoff = 0)
        archivomenu.add_command(label = "salir", command=self.salir)
        menubar.add_cascade(label = "Archivo", menu = archivomenu)

        # pestaña1

        menubar.add_command(label = "Ventana 1", command=self.ventauno)

        # pestaña2

        menubar.add_command(label="Ventana 2", command=self.ventados)

        # pestaña3

        menubar.add_command(label="Ventana 3", command=self.ventatres)

        #asignamos el menu
        self.root.config(menu = menubar)


        self.root.mainloop()

    def ventauno(self):
        Ventana1.ventana1(self)

    def ventados(self):
        Ventana2.ventana2(self)

    def ventatres(self):
        try:
            self.root.pack_slaves()[0].destroy()
            self.frame3 = Frame(self.root, width=800, height=600)
            self.label3 = Label(self.frame3, text="FUNCIONA")
            self.label3.place(relx=0.5, rely=0.5, anchor=S)
            self.frame3.pack()
        except IndexError:
            self.frame3 = Frame(self.root, width=800, height=600)
            self.label3 = Label(self.frame3, text="FUNCIONA")
            self.label3.place(relx=0.5, rely=0.5, anchor=S)
            self.frame3.pack()


    def salir(self):
       self.root.quit()


def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()