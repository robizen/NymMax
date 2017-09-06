from inicio import *


# Para cambiar de ventana, es necesario que primero intente eliminar el frame anterior.
# Con este Try, se comprueba si existe el frame creado y si es asi, primero lo olvida y luego
# crea el nuevo.
## TO-DO: Buscar un metodo mas eficiente y limpio de hacer esto. Por ahora, tendrá que servir

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
