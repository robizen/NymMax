from inicio import *


def ventana1(self):
    # Para cambiar de ventana, es necesario que primero intente eliminar el frame anterior.
    # Con este Try, se comprueba si existe el frame creado y si es asi, primero lo olvida y luego
    # crea el nuevo.
    ## TO-DO: Buscar un metodo mas eficiente y limpio de hacer esto. Por ahora, tendrá que servir
    try:
        self.frame2.pack_forget()
        self.frame1 = Frame(self.root, width=800, height=600)
        self.label1 = Label(self.frame1, text="VENTANA 1")
        self.label1.place(relx=0.5, rely=0.5, anchor=S)
        self.frame1.pack()
    except AttributeError:
        self.frame1 = Frame(self.root, width=800, height=600)
        self.label1 = Label(self.frame1, text="VENTANA 1")
        self.label1.place(relx=0.5, rely=0.5, anchor=S)
        self.frame1.pack()