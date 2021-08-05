from PyPDF2 import PdfFileWriter, PdfFileReader
import tkinter as tk
from tkinter import filedialog
import ntpath
#import os #si estás en windows descomenta esta línea
import webbrowser


output_pdf = PdfFileWriter()

# agarra la ubicacion del path que le diste
def path_leaf(path):
    head, tail = ntpath.split(path)
    return head

# seleccion grafica con el tkinter y toda la pavada
def grab_file_path():
    # te abre el coso de dialogo
    file_dialog_window = tk.Tk()
    file_dialog_window.withdraw()  # cierra la ventanita del tk.Tk()
    # usas el dialog para abrir el archivo
    grabbed_file_path = filedialog.askopenfilename()
    return grabbed_file_path

# archivo que va a revertir
filePath = grab_file_path()

# abre el archivo y lo lee
with open(filePath, 'rb') as readfile:
    input_pdf = PdfFileReader(readfile)

    # revierte el orden del pdf página por página
    for page in reversed(input_pdf.pages):
        output_pdf.addPage(page)

    # forma grafica de elegir donde lo va a guardar (y arranca en el directorio que arrancaste)
    dirOfFileToBeSaved = path_leaf(filePath)
    locationOfFileToBeSaved=filedialog.asksaveasfilename(initialdir=dirOfFileToBeSaved, initialfile='name of reversed file.pdf',title="Select or type file name and location", filetypes=[("pdf files", "*.pdf")])
    # escribe la ubicación del archivo
    with open(locationOfFileToBeSaved, "wb") as writefile:
        output_pdf.write(writefile)

# te abre la ubicación del archivo (funca en linux)
webbrowser.open(locationOfFileToBeSaved)

#si estas en windows comentá el 44 y descomentá este:
#os.startfile(locationOfFileToBeSaved)
