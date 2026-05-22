#CREAR INFORMES
import PyPDF2
import os

def pdfReader(ruta,codigo):
    """esta funcion....."""
    cont = os.listdir(ruta)
    for fichero in cont:
        if codigo in fichero:
            break
    File = open(ruta+"\\"+fichero, 'rb')
    if File:
        Reader = PyPDF2.PdfFileReader(File)
        return  Reader  
    else:
        return File  

def add_Page(pdf,index,Reader,Portada):
    """esta función....."""
    pageObj = Portada.getPage(index)
    pdf.addPage(pageObj)
    #CONTENIDO
    for pageNum in range(Reader.numPages):
        pageObj = Reader.getPage(pageNum)
        pdf.addPage(pageObj)

#RUTA CARPETA (DONDE ESTA EL ARCHIVO UBICADO)
current_path = os.path.dirname(os.path.abspath(__file__))
print(current_path)
"""crear listado de indices y readers por cada territorial para añadir
las paginas mediante un bucle"""

#PORTADA
Portada_File = open('Portadas.pdf', 'rb')
Portada_Reader = PyPDF2.PdfFileReader(Portada_File)

pdfWriter = PyPDF2.PdfFileWriter()

#PORTADA PRINCIPAL
pageObj = Portada_Reader.getPage(0)
pdfWriter.addPage(pageObj)

#CUADRO RESUMEN
pageObj = Portada_Reader.getPage(8)
pdfWriter.addPage(pageObj)
#--------------------------------------------------------------------
contenidos = os.listdir(current_path)
territoriales = ["HBT_" + x.split("_")[2] for x in contenidos if "_HBT_" in x ]

indices = {'HBT_SEV':1,'HBT_VAL':2, 'HBT_CC':3, 'HBT_CAT':4, 'HBT_N':5, 'HBT_MAL':6,'HBT_MAD':7}

for t in territoriales:
    index = indices[t]
    _reader = pdfReader(current_path, t)
    add_Page(pdfWriter, index,_reader, Portada_Reader)

pdfOutputFile = open('CosteControl_COMPLETO.pdf', 'wb')
pdfWriter.write(pdfOutputFile)