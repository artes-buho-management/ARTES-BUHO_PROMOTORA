#CAMBIAR NOMBRE RESUMEN EJECUTIVO

import os

ruta = "C:\\Users\\rubenjimenez\\Desktop\\DescargasTP\\InformeMensual"
criterioArchivo = 'InformeMensual.pdf'
archivos =os.listdir(ruta)
print (archivos)
salida = []
for a in archivos:
        campos=a.split("_")
        if campos[4] != criterioArchivo:
            nuevoNombre = ruta + '\\' + campos[0] + '_' + campos[1] + '_' + campos[2] + '_' + campos[3] + '_' + criterioArchivo
            os.rename(ruta + '\\' + a, nuevoNombre)
        else:
            pass
