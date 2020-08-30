from mainFunctions import load, manualInput, save, getInfo, url, path, tracked
import tkinter, os

window = tkinter.Tk()
window.geometry("300x100")

# Global variables
nameInput = tkinter.Entry(window)
urlInput = tkinter.Entry(window)

def pressed():    
    # Variables globales
    global nameInput, urlInput
    
    # Cajas de texto
    #nameInput = tkinter.Entry(window)
    nameInput.pack()

    #urlInput = tkinter.Entry(window)
    urlInput.pack()

    send = tkinter.Button(window, text='save', command=inputs)
    send.pack()
    
def inputs():
    # Global variables
    global nameInput, urlInput
    
    name = str(nameInput.get())
    url = str(urlInput.get())
    manualInput(name,url)
    save()
    getInfo()
    
# Etiqueta que pregunte si quiero hacer save
# Dos botones, si y no, si presiono si hace save si presiono no sale de ese bucle

# 1 - Ventana pequeña con los botones de load o manual
def initialWindow():
    CSVexist = os.path.isfile('./phonesURL.csv') # Check if file exist
    if CSVexist == True:    
        loadButton = tkinter.Button(window, text='Load', command=loadPressed)
        loadButton.pack()

    mInputButton = tkinter.Button(window, text='Manual input', command=pressed)
    mInputButton.pack()

# 2 - Si pulsamos load pasamos a la ventana con el progreso
def loadPressed():
    window.geometry("300x300")
    load()
    getInfo()
    done = tkinter.Label(window, text='Prices tracked.')
    done.pack()

# 3 - Si pulsamos manual input cambiamos ventana y aparecen cuadros de input
def manualPresses():
    # Global variables
    global nameInput, urlInput
    
    name = str(nameInput.get())
    url = str(urlInput.get())
    manualInput(name,url)






















'''
# Con esta función a la que no le pasamos argumento, el botón se crea así para llamar a la función
def saludo():
    print('Hola, Mundo!')
    
button1 = tkinter.Button(window, text='Press', command=saludo)
button1.pack()

# Con esta función a la que le pasamos un argumento, el botón se crea así para llamar a la función
def saludo(nombre):
    print('Hola '+ nombre)
    
button1 = tkinter.Button(window, text='Press', command= lambda: saludo('python'))
button1.pack()
'''
window.mainloop()