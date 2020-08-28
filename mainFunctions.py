from bs4 import BeautifulSoup
import os, csv, requests
import pyinputplus as pyip
import pandas as pd 
#from pathlib import Path 

# Variables globales
url = dict
# Path va a dar problemas en otros PCs
path = r"C:\Users\svill\Documents\Programación\Proyectos cortos Python\Backmarket scrapper\BMscrapper\CSV"

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

def manualInput(name,phoneURL):
    # Variables globales
    global url
    
    while True:
        # función para meter los datos a mano
        name = str #input('Which is the name of the device?\n')
        phoneURL = str #input('Which is the URL of the device?\n')
        url.update({name:phoneURL})
        more = pyip.inputChoice(['yes','no'], prompt='Do you want to track more devices?\n')    
        if more == 'no':
            break

def save():
    save = pyip.inputChoice(['yes','no'], prompt='Do you want to save your selection?\n')
    if save == 'yes':
        with open('phonesURL.csv','w') as f:
            for key in url.keys():
                f.write("%s,%s\n"%(key,url[key]))

def getInfo():
    # Global variables
    global url, path
    
    # función del for para hacer el scrap y crear los CSV
    for k, v in url.items():
        link = str(v)
        response = requests.get(link)
        content = BeautifulSoup(response.content,"html.parser")
        
        quality = []
        price = []
        for i in content.find('div', attrs={"class":"_1OTebAgHAcWddAP7YhPlZr"}):
            quality.append(i.find('div', attrs={"class":"_3tVEyw2WXK4Ne75JtF4vL4"}).text.strip('\n\xa0€'))
            price.append(i.find('div', attrs={"class":"_1KnTWVHWxp0RXYEjGmT44-"}).text.strip('\n\xa0€'))
            
        phonePrice = dict(zip(quality,price))
        
        os.chdir(path)
        with open('test.csv','r') as f:
            for key in phonePrice.keys():
                f.write("%s,%s\n"%(key,phonePrice[key]))
                
        with open('test.csv','r') as file_in:
            with open(k + '.csv','w') as file_out:
                writer = csv.writer(file_out)
                for row in csv.reader(file_in):
                    writer.writerow(row[:-1])
                    
        os.remove('test.csv')
        print(k + ' price was tracked.')