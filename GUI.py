import tkinter

window = tkinter.Tk()
window.geometry("400x300")

# Con esta función a la que no le pasamos argumento, el botón se crea así para llamar a la función
def saludo():
    print('Hola, Mundo!')
    
button1 = tkinter.Button(window, text='Press', command=saludo)
button1.pack()

# Con esta función a la que le pasamos un argumento, el botón se crea así para llamar a la función
'''
def saludo(nombre):
    print('Hola '+ nombre)
    
button1 = tkinter.Button(window, text='Press', command= lambda: saludo('python'))
button1.pack()
'''
window.mainloop()