from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

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

        menubar.add_command(label = "Ventana 1", command = self.ventana1)

        # pestaña2

        menubar.add_command(label="Ventana 2", command=self.ventana2)

        #asignamos el menu
        self.root.config(menu = menubar)


        #diseño de ventana1


        # diseño de ventana2


        self.root.mainloop()

    def ventana1(self):
        try:
            self.frame2.pack_forget()
            self.frame1 = Frame(self.root, width=800, height=600)
            self.label1 = Label(self.frame1, text="VENTANA 1")
            self.label1.place(relx=0.5, rely=0.5, anchor=S)
            self.frame1.pack()
        except AttributeError:
            self.frame1 = Frame(self.root,width = 800, height = 600)
            self.label1 = Label(self.frame1, text = "VENTANA 1")
            self.label1.place(relx=0.5, rely=0.5, anchor = S)
            self.frame1.pack()

    def ventana2(self):
        try:
            self.frame1.pack_forget()
            self.frame2 = Frame(self.root, width=800, height=600)
            self.label2 = Label(self.frame2, text="VENTANA 2")
            self.label2.place(relx=0.5, rely=0.5, anchor=S)
            self.frame2.pack()
        except AttributeError:
            self.frame2 = Frame(self.root, width=800, height=600)
            self.label2 = Label(self.frame2, text="VENTANA 2")
            self.label2.place(relx=0.5, rely=0.5, anchor=S)
            self.frame2.pack()



    def salir(self):
       self.root.quit()


def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()