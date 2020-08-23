import os, glob, shutil
from time import sleep
import pyinputplus as pyip 

def deleteCSV():
    CSVfiles = r"C:\Users\svill\Documents\Programación\Proyectos cortos Python\Backmarket scrapper\BMscrapper\CSV"
    os.chdir(CSVfiles)

    borrar = pyip.inputChoice(['si','no'], prompt='¿Quieres eliminar los archivos CSV?\n')
    while True:
        if borrar == 'si':
            try:
                shutil.rmtree(CSVfiles)
                sleep(1)
                print('Los archivos CSV han sido eliminados.')
                break
            except:
                print('Ha surgido un error, no se han podido eliminar los archivos.')
                
        elif borrar == 'no':
            break