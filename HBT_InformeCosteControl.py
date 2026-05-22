#CREAR INFORMES

import PyPDF2
import os

#RUTA CARPETA (DONDE ESTA EL ARCHIVO UBICADO)
current_path = os.path.dirname(os.path.abspath(__file__))
print(current_path)

#--------------------------------------------------------------------
#SEV
contenido = os.listdir(current_path)
for fichero in contenido:
    print(fichero)
    if 'HBT_SEV' in fichero:
        break
print(fichero)
SEV_File = open(fichero, 'rb')
SEV_Reader = PyPDF2.PdfFileReader(SEV_File)

#VAL
contenido = os.listdir(current_path)
for fichero in contenido:
    print(fichero)
    if 'HBT_VAL' in fichero:
        break
print(fichero)
VAL_File = open(fichero, 'rb')
VAL_Reader = PyPDF2.PdfFileReader(VAL_File)

#CC

contenido = os.listdir(current_path)
for fichero in contenido:
    print(fichero)
    if 'HBT_CC' in fichero:
        break
print(fichero)
CC_File = open(fichero, 'rb')
CC_Reader = PyPDF2.PdfFileReader(CC_File)


#CAT
contenido = os.listdir(current_path)
for fichero in contenido:
    print(fichero)
    if 'HBT_CAT' in fichero:
        break
print(fichero)
CAT_File = open(fichero, 'rb')
CAT_Reader = PyPDF2.PdfFileReader(CAT_File)

#N
contenido = os.listdir(current_path)
for fichero in contenido:
    print(fichero)
    if 'HBT_N' in fichero:
        break
print(fichero)
N_File = open(fichero, 'rb')
N_Reader = PyPDF2.PdfFileReader(N_File)

#MAL
contenido = os.listdir(current_path)
for fichero in contenido:
    print(fichero)
    if 'HBT_MAL' in fichero:
        break
print(fichero)
MAL_File = open(fichero, 'rb')
MAL_Reader = PyPDF2.PdfFileReader(MAL_File)

#MAD
contenido = os.listdir(current_path)
for fichero in contenido:
    print(fichero)
    if 'HBT_MAD' in fichero:
        break
print(fichero)
MAD_File = open(fichero, 'rb')
MAD_Reader = PyPDF2.PdfFileReader(MAD_File)

#PORTADA
Portada_File = open('Portadas.pdf', 'rb')
Portada_Reader = PyPDF2.PdfFileReader(Portada_File)

pdfWriter = PyPDF2.PdfFileWriter()
#--------------------------------------------------------------------
#PORTADA PRINCIPAL
pageObj = Portada_Reader.getPage(0)
pdfWriter.addPage(pageObj)

#CUADRO RESUMEN
pageObj = Portada_Reader.getPage(8)
pdfWriter.addPage(pageObj)


#PORTADA SEV
pageObj = Portada_Reader.getPage(1)
pdfWriter.addPage(pageObj)
#CONTENIDO SEV
for pageNum in range(SEV_Reader.numPages):
        pageObj = SEV_Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#PORTADA VAL
pageObj = Portada_Reader.getPage(2)
pdfWriter.addPage(pageObj)
#CONTENIDO VAL
for pageNum in range(VAL_Reader.numPages):
        pageObj = VAL_Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)


#PORTADA CC
pageObj = Portada_Reader.getPage(3)
pdfWriter.addPage(pageObj)
#CONTENIDO CC
for pageNum in range(CC_Reader.numPages):
        pageObj = CC_Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)


#PORTADA CAT
pageObj = Portada_Reader.getPage(4)
pdfWriter.addPage(pageObj)
#CONTENIDO CAT
for pageNum in range(CAT_Reader.numPages):
        pageObj = CAT_Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#PORTADA N
pageObj = Portada_Reader.getPage(5)
pdfWriter.addPage(pageObj)
#CONTENIDO N
for pageNum in range(N_Reader.numPages):
        pageObj = N_Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#PORTADA MAL
pageObj = Portada_Reader.getPage(6)
pdfWriter.addPage(pageObj)
#CONTENIDO MAL
for pageNum in range(MAL_Reader.numPages):
        pageObj = MAL_Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#PORTADA MAD
pageObj = Portada_Reader.getPage(7)
pdfWriter.addPage(pageObj)
#CONTENIDO MAD
for pageNum in range(MAD_Reader.numPages):
        pageObj = MAD_Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutputFile = open('CosteControl_COMPLETO.pdf', 'wb')
pdfWriter.write(pdfOutputFile)



#pdfOutputFile.close()
#AFile.close()
#BFile.close()