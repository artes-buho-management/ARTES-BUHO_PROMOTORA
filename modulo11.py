def imprimir ():
    #print(desplegableTk)
    desplegableTk= desplegableCaja.get()
    print(desplegableTk)

from tkinter import *
import tkinter as tk
from tkinter import ttk

OptionList= ["Coste Control", 'Informe Semanal']


ventana = Tk()
buscarTk= StringVar()
fechaTk= StringVar()
desplegableTk= StringVar()


buscarTk.set("2106_HBT")
fechaTk.set("05/05/2021")
#desplegableTk.set(OptionList[0])

ventana.title ("Habitat Inmobiliaria")
ventana.geometry("400x400")
#ventana.configure(background='White')


etiqueta1=Label(ventana,text="Escribe que quiere buscar: ").place(x=10,y=10)
BuscarCaja=Entry(ventana,textvariable=buscarTk).place(x=170,y=10)

etiqueta2=Label(ventana,text="Fecha mínima del archivo: ").place(x=10,y=40)
FechaCaja=Entry(ventana,textvariable=fechaTk).place(x=170,y=40)


etiqueta3=Label(ventana,text="¿Qué quiere decargar? ").place(x=10,y=70)
desplegableCaja = ttk.Combobox(ventana, values=["Coste Control", "Informe Mensual"])
desplegableCaja.place(x=170,y=70)
desplegableCaja.current(1)




boton=Button(ventana,text="Ejecutar", command=imprimir).place(x=10, y=100)
ventana.mainloop()
