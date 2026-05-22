from tkinter import *



raiz =Tk()
raiz.title("hola mundo")
raiz.iconbitmap("F:\eglog\Proyectos\Panama\Archivos py\Con-Exceptions\TKINTER\imagenes\images.ico")
raiz.geometry("1000x850")
raiz.config(bg ="gray")
raiz.config(bd="30")
raiz.config(relief="groove")
miframe = Frame(raiz,bg="white",width="1000", height="650")
miframe.pack(fill ="both",expand = "True")

nombrelable = Label(miframe,text ="Cuenta de Correo:",font =(16))
nombrelable.grid(row="1",column="0")
passlabel = Label(miframe,text ="Contraseña:",font =(16))
passlabel.grid(row="2",column="0")
agelabel = Label(miframe,text ="age:",font =(16))
agelabel.grid(row="3",column="0")
textocorreo= Entry(miframe,width="30")
textocorreo.grid(row="1",column="1")
textopass= Entry(miframe,width="30")
textopass.grid(row="2",column="1")
textoage= Entry(miframe,width="30")
textoage.grid(row="3",column="1")

cuentas = []
def send_data():
    datos = {
        "Cuenta de Correo": textocorreo.get(),
        "Contraseña": textopass.get(),
        "age": textoage.get()
    }
    cuentas.append(datos)

ingresarboton = Button(miframe, text="Ingresar", command=send_data)
ingresarboton.grid(row="11", column="1")
raiz.mainloop()