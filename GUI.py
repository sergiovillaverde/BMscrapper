import tkinter
import os
from mainFunctions import manualInput, save

window = tkinter.Tk()
window.geometry("300x100")
nameInput = tkinter.Entry(window)
urlInput = tkinter.Entry(window)

### FUNCIONES ###
# Función al pulsar manual
def manualPressed():
    manualButton.pack_forget()
    nameInput.pack()
    urlInput.pack()
    add = tkinter.Button(window, text='Add', command=inputData)
    add.pack()
    
def inputData():
    name = str(nameInput.get())
    url = str(urlInput.get())
    manualInput(name,url)    
    label = tkinter.Label(window, text='Do you want to track more devices?')
    label.pack()
    yes = tkinter.Button(window, text='Yes', command=inputData)
    yes.pack()
    no = tkinter.Button(window, text='No', command=save)
    no.pack()
    
# Ventana inicial con dos botones
manualButton = tkinter.Button(window, text='Manual Input', command=manualPressed)
manualButton.pack()

CSVexist = os.path.isfile('./phonesURL.csv')
if CSVexist == True:
    loadButton = tkinter.Button(window, text='Load')
    loadButton.pack()
    

    
    
    
window.mainloop()