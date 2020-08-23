import os, glob
from time import sleep
import pyinputplus as pyip 

CSVfiles = r"C:\Users\svill\Documents\Programación\Proyectos cortos Python\Backmarket scrapper\BMscrapper\CSV"

# Evitar que el programa se cierre al terminar
while True:
    borrar = pyip.inputChoice(['si', 'no'], prompt='¿Quieres eliminar los archivos CSV?\n')
    if borrar == 'si':
        try:
            os.close(CSVfiles)
            files = glob.glob(CSVfiles)
            for f in files:
                os.remove(f)
            print('Archivos CSV eliminados.')
            sleep(3)
        except:
            print('No se han podido eliminar los archivos CSV.')
            
        try:
            os.mkdir(CSVfiles)
        except:
            print('No se ha podido crear de nuevo la carpeta CSV.')
            
        break
    
    elif borrar == 'no':
        print('El programa se va a cerrar.')
        break