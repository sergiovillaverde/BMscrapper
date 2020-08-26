from bs4 import BeautifulSoup
import requests, csv, os
import pandas as pd 
import pyinputplus as pyip 

path = r"C:\Users\svill\Documents\Programación\Proyectos cortos Python\Backmarket scrapper\BMscrapper\CSV"

def getPrice():
    url = {}
    loadBool = False
    loadNum = 0
    
    while True:
        # Ask the user to load the CSV with the info of the devices to create the dict
        if loadNum < 1:
            load = pyip.inputChoice(['yes','no'], prompt='Do you want to load the previous consult?\n')
            if load == 'yes':
                with open('phonesURL.csv', 'r') as infile:
                    reader = csv.reader(infile)
                    with open('csvtodict.csv', 'w') as outfile:
                        writer = csv.writer(outfile)
                        url = {rows[0]:rows[1] for rows in reader}
            
                os.remove('csvtodict.csv')
                loadBool = True
                break
            elif load == 'no':
                loadNum = 1
        
        # Ask the user for the name and URL of the device
        name = input('Which is the name of the phone?\n')
        phoneURL = input('Which is the URL of the phone?\n')
        #phoneName = name + phoneURL
        #url = dict(phoneName.split())
        url.update({name:phoneURL})
        more = pyip.inputChoice(['yes','no'], prompt='Do you want to track more phones?\n')
        if more == 'no':
            break
    
    # Ask the user to save the info of the chosen devices
    if loadBool == False:
        save = pyip.inputChoice(['yes','no'], prompt='Do you want to save the URL for the next time?\n')
        if save == 'yes':
            with open('phonesURL.csv', 'w') as f:
                for key in url.keys():
                    f.write("%s,%s\n"%(key,url[key]))
    
    for k, v in url.items():
        link = str(v)
        response = requests.get(link)
        content = BeautifulSoup(response.content, "html.parser")
        
        state = []
        price = []
        for i in content.find('div', attrs={"class":"_1OTebAgHAcWddAP7YhPlZr"}):
            state.append(i.find('div', attrs={"class":"_3tVEyw2WXK4Ne75JtF4vL4"}).text.strip('\n\xa0€'))
            price.append(i.find('div', attrs={"class":"_1KnTWVHWxp0RXYEjGmT44-"}).text.strip('\n\xa0€'))
            
        phonePrice = dict(zip(state,price))
        
        os.chdir(path)
        with open('test.csv', 'w') as f:
            for key in phonePrice.keys():
                f.write("%s,%s\n"%(key,phonePrice[key]))
                
        with open('test.csv', 'r') as file_in:
            with open(k + '.csv', 'w') as file_out:
                writer = csv.writer(file_out)
                for row in csv.reader(file_in):
                    writer.writerow(row[:-1])
                    
        os.remove('test.csv')
        
        print(k + ' price was tracked.')
        
getPrice()