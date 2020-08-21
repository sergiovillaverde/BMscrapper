import os
from time import sleep

os.chdir(r"C:\Users\svill\Documents\Programación\Proyectos cortos Python\Backmarket scrapper\BMscrapper\Models")

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

try:
    print('El programa se ha iniciado.')
    sleep(2)
    print('Recopilando precios de iPhone X')
    iphoneXnegro()
    iphoneXplata()

    print('Recopilando precios de iPhone XR.')
    iphoneXRnegro()
    iphoneXRrojo()
    iphoneXRazul()
    iphoneXRcoral()
    iphoneXRamarillo()
    iphoneXRblanco()

    print('Recopilando precios de iPhone XS.')
    iphoneXSnegro()
    iphoneXSplata()
    iphoneXSdorado()

    print('Los archivos CSV están listos, el programa ha terminado.')
    sleep(5)
    
except:
    print('Ha surgido un error, el programa se ha detenido.')