import os, csv
import pyinputplus as pyip 

# Variables globales
url = dict

# Crear loadNum para sacar del loop esta función si fuera necesario
def load():
    # Variables globales
    global url
    
    # función de cargar el CSV con los datos
    CSVexist = os.path.isfile('./phonesURL.csv')
    if CSVexist == True:
        # Ask the user to load the info
        load = pyip.inputChoice(['yes','no'], prompt='Do you want to load the previous consult?\n')
        if load == 'yes':
            with open('phonesURL.csv','r') as infile:
                reader = csv.reader(infile)
                with open('csvtodict.csv','w') as outfile:
                    writer = csv.writer(outfile)
                    url = {rows[0]:rows[1] for rows in reader}
                    
            os.remove('csvtodict.csv')

def manualInput():
    # Variables globales
    global url
    
    while True:
        # función para meter los datos a mano
        name = input('Which is the name of the device?\n')
        phoneURL = input('Which is the URL of the device?\n')
        url.update({name:phoneURL})
        more = pyip.inputChoice(['yes','no'], prompt='Do you want to track more devices?\n')    
        if more == no:
            break
        
    save = pyip.inputChoice(['yes','no'], prompt='Do you want to save your selection?\n')
    if save == 'yes':
        with open('phonesURL.csv','w') as f:
            for key in url.keys():
                f.write("%s,%s\n"%(key,url[key]))

def getInfo():
    # función del for para hacer el scrap y crear los CSV
    pass

