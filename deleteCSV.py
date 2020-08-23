import os, glob, shutil
from time import sleep
import pyinputplus as pyip 

CSVfiles = r"C:\Users\svill\Documents\Programación\Proyectos cortos Python\Backmarket scrapper\BMscrapper\CSV"
os.chdir(CSVfiles)

shutil.rmtree(CSVfiles)