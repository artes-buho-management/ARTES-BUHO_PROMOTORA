#DESCARGA RVT proyecto basico
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



def EsperarCierreVentanas():
    while len(driver.window_handles)!=1:
        print(len(driver.window_handles))
        time.sleep(1)
        print("esperando")


driver_path = 'C:\\Users\\rubenjimenez\\Downloads\\chromedriver.exe'

usuario = "ruben.jimenez"
contraseña = "rj@19268-D"


buscar = "2106_HBT"
pulsador = "8"



# Opciones de navegación
#nota:Cambiamos carpeta por obra
rutaDescarga = "C:\\Users\\rubenjimenez\\Desktop\\DescargasTP\\CosteControl\\" #IMPORTANTE, ruta de descarga

#creamos carpeta si no existe
if os.path.exists(rutaDescarga):
    pass
else: 
    os.makedirs(rutaDescarga)

options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_experimental_option("prefs", {
"download.default_directory" : rutaDescarga, "download.prompt_for_download": False, "plugins.always_open_pdf_externally": True})
driver = webdriver.Chrome(driver_path, chrome_options=options)

# Iniciarla en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()
#time.sleep(1)

# Inicializamos el navegador
driver.get('https://www20.thinkproject.com/tp20/oidc?jc=HBT-Informes')


#PONER USUARIO
WebDriverWait(driver, 120)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/input')))
mBox = driver.find_element_by_xpath('/html/body/div/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/input')
mBox.send_keys(usuario)
#PONER CONTRASEÑA
mBox = driver.find_element_by_xpath('/html/body/div/div/div/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/input')
mBox.send_keys(contraseña)
#CLICK PARA ACCEDER
boton=driver.find_element_by_xpath('/html/body/div/div/div/form/div/div/div/button')
boton.click()
#SELECCIONAMOS PROYECTO
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT,'06.06.03 Coste Control')))
boton=driver.find_element_by_link_text('06.06.03 Coste Control')

print ("buscado proyecto")
boton.click()

WebDriverWait(driver, 20)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[2]/div[3]/form/div/div[3]/div[3]/table[2]/tbody/tr[1]'))) #ESPERAR HASTA QUE APAREZCA UN ELEMENTO DE lA TABLA
NumTotal = int(driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div').text) #numero de archivos que hay en esa carpeta          
print(NumTotal)

#BUSCAR OBRA
WebDriverWait(driver, 20)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[2]/div[3]/form/div/div[3]/div[3]/table[1]/thead/tr/th[8]/div/div[1]/div[2]/div/div/input')))
mBox = driver.find_element_by_xpath('/html/body/div[2]/div[3]/form/div/div[3]/div[3]/table[1]/thead/tr/th[8]/div/div[1]/div[2]/div/div/input')

mBox.clear() #limpiamos contenido anterior
WebDriverWait(driver, 20)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                    '/html/body/div[2]/div[3]/form/div/div[3]/div[3]/table[2]/tbody/tr[1]'))) #esperar hasta que sea clikable un elemento de la tabla
mBox.send_keys(buscar) #enviamos texto para realizar la busqueda                         
boton=driver.find_element_by_xpath('/html/body/div[2]/div[3]/form/div/div[3]/div[3]/table[1]/thead/tr/th[7]/div[2]')
boton.click() #hacemos click
print ("buscada la obra")


#NUMERO DE ARCHIVOS TOTALES
while NumTotal == int(driver.find_element_by_class_name('total-records').text): #esperara mientras nº de archivos sea el mismo que el total de la carpeta, quiere decir que aun no ha cargado la busqueda
    time.sleep(1)
    print("esperando")

WebDriverWait(driver, 10)\
.until(EC.element_to_be_clickable((By.CLASS_NAME,
                                '/html/body/div[2]/div[3]/form/div/div[3]/div[3]/table[2]/tbody/tr[1]'))) #esperamos hasta que aparezca un elemento de descarga                         
NumArchivos = driver.find_element_by_class_name('total-records')              
NumArchivos = int(NumArchivos.text)
print(NumArchivos)

if NumArchivos != 0:  #Si numero de archivos es diferente de 0 descargamos, si no pasamos a siguiente 
    #NUMERO DE FILAS
    WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[2]/div[3]/form/div/div[3]/div[3]/table[2]/tbody/tr')))
    filas = len(driver.find_elements_by_class_name('msg-read'))
    filas = filas
    print(filas)

    if NumArchivos > 50:   #si numero de archivos es mayor que 50 tendremos que psar de pagina para descargar
        PagTotal=math.ceil(NumArchivos/50)
        print(PagTotal)    
        PagActual=0
        lista=[]
        for j in range(1,PagTotal+1): #bucle para pasar de pagina para descargar todos los archivos
            #FILAS
            
            WebDriverWait(driver, 120)\
                .until(EC.element_to_be_clickable((By.XPATH,
                                                '/html/body/div[2]/div[3]/form/div/div[3]/div[3]/table[2]/tbody/tr')))
            filas = len(driver.find_elements_by_class_name('msg-read'))
            filas = filas
            print(filas)
            
            #DESCARGA
            for i in range(1,filas+1):  #descargamos todos los archivos de una pagina
                WebDriverWait(driver, 10)\
                .until(EC.element_to_be_clickable((By.XPATH,
                                                '/html/body/div[2]/div[3]/form/div/div[3]/div[3]/table[2]/tbody/tr[' + str(i) + ']/td[12]/a')))
                element = driver.find_element_by_xpath('/html/body/div[2]/div[3]/form/div/div[3]/div[3]/table[2]/tbody/tr[' + str(i) + ']/td[12]/a')
                nombreArchivo=element.text
                if not nombreArchivo in lista:
                    element.click()
                    lista.append(nombreArchivo)
                    time.sleep(0.5)
                print(lista)

            EsperarCierreVentanas()  #esperamos que se ejecuten url

            #PASAR DE PAGINA
            PagActual=PagActual+1
            print(PagActual)
            if PagActual!=PagTotal: #si no estamos en la ultima pagina, pasamos pagina
                WebDriverWait(driver, 120)\
                    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                    'A.rightArrow')))\
                    .click()
                time.sleep(5)

            print('Tenemos varias paginas, vuelta de bucle, pasamos de pagina')

    else:  #Si solo tenemos 1 pagina de archivos, no hace falta que pasemos de pagina
        #DESCARGAR
        lista=[]
        for i in range(1,filas+1):
            WebDriverWait(driver, 10)\
                .until(EC.element_to_be_clickable((By.XPATH,
                                                '/html/body/div[2]/div[3]/form/div/div[3]/div[3]/table[2]/tbody/tr[' + str(i) + ']/td[12]/a')))
            element = driver.find_element_by_xpath('/html/body/div[2]/div[3]/form/div/div[3]/div[3]/table[2]/tbody/tr[' + str(i) + ']/td[12]/a')
            nombreArchivo=element.text
            if not nombreArchivo in lista:
                element.click()
                lista.append(nombreArchivo)
                time.sleep(0.5)       

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



