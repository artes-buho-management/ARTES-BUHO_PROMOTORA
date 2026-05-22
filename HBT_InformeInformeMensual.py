#INFORME MENSUAL
import PyPDF2
import os

#RUTA CARPETA (DONDE ESTA EL ARCHIVO UBICADO)
current_path = os.path.dirname(os.path.abspath(__file__))
print(current_path)

contenido = os.listdir(current_path)

#PORTADA
Portada_File = open('Portadas.pdf', 'rb')
Portada_Reader = PyPDF2.PdfFileReader(Portada_File)

pdfWriter = PyPDF2.PdfFileWriter()

#-------------------------------------------------

#PORTADA PRINCIPAL
pageObj = Portada_Reader.getPage(0)
pdfWriter.addPage(pageObj)

#PORTADA SEV
pageObj = Portada_Reader.getPage(1)
pdfWriter.addPage(pageObj)
#CONTENIDO SEV
SEV = []
for fichero in contenido:
    if 'HBT_SEV' in fichero:  
        SEV.append(fichero)
for fichero in SEV:
    SEV_File = open(fichero, 'rb')
    SEV_Reader = PyPDF2.PdfFileReader(SEV_File)
    for pageNum in range(SEV_Reader.numPages):
        pageObj = SEV_Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#PORTADA VAL
pageObj = Portada_Reader.getPage(2)
pdfWriter.addPage(pageObj)
#CONTENIDO VAL
SEV = []
for fichero in contenido:
    if 'HBT_VAL' in fichero:  
        SEV.append(fichero)
for fichero in SEV:
    SEV_File = open(fichero, 'rb')
    SEV_Reader = PyPDF2.PdfFileReader(SEV_File)
    for pageNum in range(SEV_Reader.numPages):
        pageObj = SEV_Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#PORTADA CC
pageObj = Portada_Reader.getPage(3)
pdfWriter.addPage(pageObj)
#CONTENIDO CC
SEV = []
for fichero in contenido:
    if 'HBT_CC' in fichero:  
        SEV.append(fichero)
for fichero in SEV:
    SEV_File = open(fichero, 'rb')
    SEV_Reader = PyPDF2.PdfFileReader(SEV_File)
    for pageNum in range(SEV_Reader.numPages):
        pageObj = SEV_Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#PORTADA CAT
pageObj = Portada_Reader.getPage(4)
pdfWriter.addPage(pageObj)
#CONTENIDO CAT
SEV = []
for fichero in contenido:
    if 'HBT_CAT' in fichero:  
        SEV.append(fichero)
for fichero in SEV:
    SEV_File = open(fichero, 'rb')
    SEV_Reader = PyPDF2.PdfFileReader(SEV_File)
    for pageNum in range(SEV_Reader.numPages):
        pageObj = SEV_Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)



#PORTADA MAD
pageObj = Portada_Reader.getPage(5)
pdfWriter.addPage(pageObj)
#CONTENIDO MAD
SEV = []
for fichero in contenido:
    if 'HBT_MAD' in fichero:  
        SEV.append(fichero)
for fichero in SEV:
    SEV_File = open(fichero, 'rb')
    SEV_Reader = PyPDF2.PdfFileReader(SEV_File)
    for pageNum in range(SEV_Reader.numPages):
        pageObj = SEV_Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#PORTADA N
pageObj = Portada_Reader.getPage(6)
pdfWriter.addPage(pageObj)
#CONTENIDO N
SEV = []
for fichero in contenido:
    if 'HBT_N' in fichero:  
        SEV.append(fichero)
for fichero in SEV:
    SEV_File = open(fichero, 'rb')
    SEV_Reader = PyPDF2.PdfFileReader(SEV_File)
    for pageNum in range(SEV_Reader.numPages):
        pageObj = SEV_Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#PORTADA MAL
pageObj = Portada_Reader.getPage(7)
pdfWriter.addPage(pageObj)
#CONTENIDO MAL
SEV = []
for fichero in contenido:
    if 'HBT_MAL' in fichero:  
        SEV.append(fichero)
for fichero in SEV:
    SEV_File = open(fichero, 'rb')
    SEV_Reader = PyPDF2.PdfFileReader(SEV_File)
    for pageNum in range(SEV_Reader.numPages):
        pageObj = SEV_Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutputFile = open('InformeMensual_ResumenEjecutivo_r04.pdf', 'wb')
pdfWriter.write(pdfOutputFile)