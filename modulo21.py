def descargaCosteControl():
    #DESCARGA Coste Control

    # Librerías
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    import time
    import os
    from os import remove
    import pandas as pd
    import math
    import glob
    from datetime import date
    from datetime import datetime
    from datetime import timedelta

    def EsperarCierreVentanas():
        while len(driver.window_handles)!=1:
            print(len(driver.window_handles))
            time.sleep(1)
            print("esperando")

    def Datos(i):
        WebDriverWait(driver, 120)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[2]/div[3]/div[2]/div[3]/div[3]/table[2]/tbody/tr[' + str(i) + ']/td[12]/a')))
        element = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div[3]/div[3]/table[2]/tbody/tr[' + str(i) + ']/td[12]/a')
        fechaArchivo=driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div[3]/div[3]/table[2]/tbody/tr[' + str(i) + ']/td[18]').text
        timeArchivo=fechaArchivo[-5:]
        time=timeArchivo.split(":")
        horaArchivo=int(time[0])
        minutoArchivo=int(time[1])
        if "hoy" in fechaArchivo:
            diaArchivo=day
            mesArchivo=month
            anoArchivo=year
        elif "ayer" in fechaArchivo:
            diaArchivo=dayAyer
            mesArchivo=monthAyer
            anoArchivo=yearAyer           
        else:
            fechaArchivo=fechaArchivo[4:-5]
            campos=fechaArchivo.split(".")
            diaArchivo=int(campos[0])
            mesArchivo=int(campos[1])
            anoArchivo=campos[2]
        return element, diaArchivo, mesArchivo, anoArchivo, horaArchivo, minutoArchivo

    def Descargar(nombreArchivo, lista):
        if not nombreArchivo in lista:
            element.click()
            time.sleep(0.5)
            return True
        else:
            return False

    driver_path = os.getcwd() + '\chromedriver.exe'

    usuario = "ruben.jimenez"
    contraseña = "rj@19268-D"

    #Fecha a buscar
    fecha=str(fechaTk.get())
    hora=horaTk.get()
    buscar = str(buscarTk.get())
    desplegableTk= desplegableCaja.get()
    desplegable= str(desplegableTk)

    if desplegable=="Coste Control":
        boton1="06.06.03 Coste Control"
    if desplegable=="Informe Mensual":
        boton1="06.03 Informe Mensual"
    print (boton1)

    tiempo=hora.split(":")
    horaBusqueda=int(tiempo[0])
    minutoBusqueda=int(tiempo[1])
    campos=fecha.split("/")
    diaBusqueda=int(campos[0])
    mesBusqueda=int(campos[1])
    anoBusqueda=int(campos[2])
    today=date.today()
    day=today.day
    month=today.month
    year=today.year
    ayer=today-timedelta(days=1)
    dayAyer=ayer.day
    monthAyer=ayer.month
    yearAyer=ayer.year

    # Opciones de navegación
    #nota:Cambiamos carpeta por obra
    rutaDescarga = "C:\\Users\\rubenjimenez\\Desktop\\DescargasTP\\CosteControl\\" #IMPORTANTE, ruta de descarga

    options =  webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_experimental_option("prefs", {
    "download.default_directory" : rutaDescarga, "download.prompt_for_download": False, "plugins.always_open_pdf_externally": True})
    driver = webdriver.Chrome(driver_path, chrome_options=options)

    # Iniciarla en la pantalla 2
    #driver.set_window_position(2000, 0)
    driver.maximize_window()
    #time.sleep(1)

    # Inicializamos el navegador
    driver.get('https://www20.thinkproject.com/tp20/oidc?jc=HBT-Informes')

    #PONER USUARIO
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.auth0-lock-submit')))
    mBox = driver.find_element_by_name('username')
    mBox.send_keys(usuario)
    #PONER CONTRASEÑA
    mBox = driver.find_element_by_name('password')
    mBox.send_keys(contraseña)
    #CLICK PARA ACCEDER
    boton=driver.find_element_by_name('submit')
    boton.click()
    #SELECCIONAMOS PROYECTO
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.LINK_TEXT,boton1)))
    boton=driver.find_element_by_link_text(boton1)
    boton.click()
    #ESPERAR HASTA QUE ELEMENTO DE LA TABLA SEA CLIKABLE
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div.tpcde-checkbox__indicator'))) 
    NumTotal = int(driver.find_element_by_css_selector('div.total-records').text) #numero de archivos que hay en esa carpeta          
    print(NumTotal)
    #REALIZAR BUSQUEDA
    WebDriverWait(driver, 120)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[2]/div[3]/div[2]/div[3]/div[3]/table[1]/thead/tr/th[8]/div/div[1]/div[2]/div/div/input')))
    mBox = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div[3]/div[3]/table[1]/thead/tr/th[8]/div/div[1]/div[2]/div/div/input')
                                        
    mBox.clear() #limpiamos contenido anterior
    WebDriverWait(driver, 120)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div.container-header-section.widget-column-search-icon'))) #esperar hasta que sea clikable un elemento de la tabla
    mBox.send_keys(buscar) #enviamos texto para realizar la busqueda                         
    boton=driver.find_element_by_css_selector('div.container-header-section.widget-column-search-icon')
    boton.click() #hacemos click
    print ("buscada la obra")
    #NUMERO DE ARCHIVOS TOTALES
    while NumTotal == int(driver.find_element_by_css_selector('div.total-records').text): #esperara mientras nº de archivos sea el mismo que el total de la carpeta, quiere decir que aun no ha cargado la busqueda
        time.sleep(1)
        print("esperando")

    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'tr.msg-read'))) #esperamos hasta que aparezca un elemento de descarga                         
    NumArchivos = driver.find_element_by_css_selector('div.total-records')    
    NumArchivos = int(NumArchivos.text)
    print(NumArchivos)

    if NumArchivos != 0:  #Si numero de archivos es diferente de 0 descargamos, si no pasamos a siguiente 
        #NUMERO DE FILAS
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'tr.msg-read')))
        filas = len(driver.find_elements_by_css_selector('tr.msg-read'))
        filas = filas
        print(filas)

        if NumArchivos > 50:   #si numero de archivos es mayor que 50 tendremos que psar de pagina para descargar
            PagTotal=math.ceil(NumArchivos/50)
            print(PagTotal)    
            PagActual=0
            lista=[]
            for j in range(1,PagTotal+1): #bucle para pasar de pagina para descargar todos los archivos
                #FILAS
                WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'tr.msg-read')))
                filas = int(len(driver.find_elements_by_css_selector('tr.msg-read')))
                print(filas)
                
                #DESCARGA
            for i in range(1,filas+1):
                element = Datos(i)[0]
                diaArchivo=Datos(i)[1]
                mesArchivo= Datos(i)[2]
                anoArchivo=Datos(i)[3]
                horaArchivo=Datos(i)[4]
                minutoArchivo=Datos(i)[5]
                nombreArchivo=element.text

                if anoArchivo ==" ":
                    anoArchivo=year
                if anoBusqueda<=anoArchivo:
                    if mesBusqueda<mesArchivo:
                        print('descargamos')
                        if Descargar(nombreArchivo, lista):
                            lista.append(nombreArchivo)
                            print (lista)
                    elif mesBusqueda==mesArchivo:
                        if diaBusqueda<diaArchivo:
                            print('descargamos')
                            if Descargar(nombreArchivo, lista):
                                lista.append(nombreArchivo)
                                print(lista)
                        elif diaBusqueda==diaArchivo:
                            print('descargamos')
                            if horaBusqueda<horaArchivo:
                                if Descargar(nombreArchivo, lista):
                                    lista.append(nombreArchivo)
                                    print(lista)
                            elif diaBusqueda==diaArchivo and mesBusqueda==mesArchivo and anoBusqueda==anoArchivo:
                                if minutoBusqueda<=minutoArchivo:
                                    if Descargar(nombreArchivo, lista):
                                        lista.append(nombreArchivo)
                                        print(lista)   

                EsperarCierreVentanas()  #esperamos que se ejecuten url
                #PASAR DE PAGINA
                PagActual=PagActual+1
                print(PagActual)
                if PagActual!=PagTotal: #si no estamos en la ultima pagina, pasamos pagina
                    comprobacion1=driver.find_element_by_css_selector('td.integer-cell.renderable.system-index').text
                    comprobacion2=comprobacion1
                    pasarPagina=driver.find_element_by_css_selector('A.rightArrow')
                    pasarPagina.click()
                    print(comprobacion1)
                    while comprobacion1==comprobacion2:
                        comprobacion2=driver.find_element_by_css_selector('td.integer-cell.renderable.system-index').text
                        time.sleep(1)
                        print("esperando")
                        print(comprobacion2)
                    #time.sleep(5)


                print('Tenemos varias paginas, vuelta de bucle, pasamos de pagina')

        else:  #Si solo tenemos 1 pagina de archivos, no hace falta que pasemos de pagina
            #DESCARGAR
            lista=[]
            print(filas)
            for i in range(1,filas+1):
                element = Datos(i)[0]
                diaArchivo=Datos(i)[1]
                mesArchivo= Datos(i)[2]
                anoArchivo=Datos(i)[3]
                horaArchivo=Datos(i)[4]
                minutoArchivo=Datos(i)[5]
                nombreArchivo=element.text

                if anoArchivo ==" ":
                    anoArchivo=int(year)
                    anoArchivo=int(anoArchivo)
                if int(anoBusqueda)<=int(anoArchivo):
                    if int(mesBusqueda)<int(mesArchivo):
                        print('descargamos')
                        if Descargar(nombreArchivo, lista):
                            lista.append(nombreArchivo)
                            print (lista)
                    elif mesBusqueda==mesArchivo:
                        if diaBusqueda<diaArchivo:
                            print('descargamos')
                            if Descargar(nombreArchivo, lista):
                                lista.append(nombreArchivo)
                                print(lista)
                        elif diaBusqueda==diaArchivo and mesBusqueda==mesArchivo and anoBusqueda==anoArchivo:
                            print('descargamos')
                            if horaBusqueda<horaArchivo:
                                if Descargar(nombreArchivo, lista):
                                    lista.append(nombreArchivo)
                                    print(lista)
                            elif horaBusqueda==horaArchivo:
                                if minutoBusqueda<=minutoArchivo:
                                    if Descargar(nombreArchivo, lista):
                                        lista.append(nombreArchivo)
                                        print(lista)                                  
                        

    EsperarCierreVentanas() #esperamos que se ejecuten url

    #ESPERAR HASTA COMPLETAR DESCARGAS
    #esperar hasta que desaparezcan los archivos con extension .crdownload
    archivosDescarga = 1
    while archivosDescarga != 0:
        time.sleep(1)
        archivosDescarga = len(glob.glob1(rutaDescarga,"*.crdownload"))
        print("esperando")
        print(archivosDescarga)
    print("Descargas completas al 100%")
    #CERRAR WEB
    driver.quit() #cerramos web para resetear todo

    print('HA TERMINADO EL PROGRAMA CON EXITO')



from tkinter import *
import tkinter as tk
from tkinter import ttk

OptionList= ["Coste Control", 'Informe Semanal']


ventana = Tk()
buscarTk= StringVar()
fechaTk= StringVar()
horaTk = StringVar()
desplegableTk= StringVar()


buscarTk.set("2107_HBT")
fechaTk.set("01/06/2021")
horaTk.set("09:00")
desplegableTk.set(OptionList[0])

ventana.title ("Habitat Inmobiliaria")
ventana.geometry("400x180")
#ventana.configure(background='White')


etiqueta1=Label(ventana,text="¿Qué quiere buscar? ").place(x=10,y=10)
BuscarCaja=Entry(ventana,textvariable=buscarTk).place(x=170,y=10)

etiqueta2=Label(ventana,text="Fecha inicio busqueda: ").place(x=10,y=40)
FechaCaja=Entry(ventana,textvariable=fechaTk).place(x=170,y=40)

etiqueta4=Label(ventana,text="Hora inicio busqueda: ").place(x=10,y=70)
HoraCaja=Entry(ventana,textvariable=horaTk).place(x=170,y=70)



etiqueta3=Label(ventana,text="¿Qué quiere decargar? ").place(x=10,y=100)
desplegableCaja = ttk.Combobox(ventana, values=["Coste Control", "Informe Mensual"])
desplegableCaja.place(x=170,y=100)
desplegableCaja.current(0)
desplegableTk= desplegableCaja.get()

boton=Button(ventana,text="Ejecutar", command=descargaCosteControl).place(x=10, y=130)
ventana.mainloop()

