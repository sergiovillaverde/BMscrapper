import os
from time import sleep

CSVfiles = r"C:\Users\svill\Documents\Programación\Proyectos cortos Python\Backmarket scrapper\BMscrapper\CSV"
modelsFile = r"C:\Users\svill\Documents\Programación\Proyectos cortos Python\Backmarket scrapper\BMscrapper\Models"
os.chdir(modelsFile)

from Models.iphoneXnegro import iphoneXnegro
from Models.iphoneXplata import iphoneXplata
from Models.iphoneXRnegro import iphoneXRnegro
from Models.iphoneXRrojo import iphoneXRrojo
from Models.iphoneXRazul import iphoneXRazul
from Models.iphoneXRcoral import iphoneXRcoral
from Models.iphoneXRamarillo import iphoneXRamarillo
from Models.iphoneXRblanco import iphoneXRblanco
from Models.iphoneXSnegro import iphoneXSnegro
from Models.iphoneXSplata import iphoneXSplata
from Models.iphoneXSdorado import iphoneXSdorado
from deleteCSV import deleteCSV

try:
    print('El programa se ha iniciado.')
    sleep(2)
    print('Recopilando precios de iPhone X.')
    sleep(1)
    print('iPhone X negro:')
    iphoneXnegro()
    sleep(1)
    print('iPhone X plata:')
    iphoneXplata()
    sleep(1)

    print('Recopilando precios de iPhone XR.')
    sleep(1)
    print('iPhone XR negro:')
    iphoneXRnegro()
    sleep(1)
    print('iPhone XR rojo:')
    iphoneXRrojo()
    sleep(1)
    print('iPhone XR azul:')
    iphoneXRazul()
    sleep(1)
    print('iPhone XR coral:')
    iphoneXRcoral()
    sleep(1)
    print('iPhone XR amarillo:')
    iphoneXRamarillo()
    sleep(1)
    print('iPhone XR blanco:')
    iphoneXRblanco()
    sleep(1)

    print('Recopilando precios de iPhone XS.')
    sleep(1)
    print('iPhone XS negro:')
    iphoneXSnegro()
    sleep(1)
    print('iPhone XS plata:')
    iphoneXSplata()
    sleep(1)
    print('iPhone XS dorado:')
    iphoneXSdorado()
    sleep(1)

    print('Los archivos CSV están listos, el programa ha terminado.')
    
    # Abrimos la carpeta CSV para ahorrar tiempo
    #os.startfile(CSVfiles) # OJO! Sólo funciona en Windows
    sleep(7)     
    
    #deleteCSV()
    
except:
    print('Ha surgido un error, el programa se ha detenido.')