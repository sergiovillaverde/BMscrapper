from bs4 import BeautifulSoup
import requests, csv, os
import pandas as pd 
import pyinputplus as pyip 

path = r"C:\Users\svill\Documents\Programación\Proyectos cortos Python\Backmarket scrapper\BMscrapper\CSV"

url = {}

def getPrice():
    while True:
        name = input('Which is the name of the phone?\n')
        phoneURL = input('Which is the URL of the phone?\n')
        #phoneName = name + phoneURL
        #url = dict(phoneName.split())
        url.update({name:phoneURL})
        more = pyip.inputChoice(['yes','no'], prompt='Do you want to track more phones?\n')
        if more == 'no':
            break
        
    # TODO las keys serán el nombre del móvil y los values serán las url
    
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
        
        print(phonePrice)
        
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
        
getPrice()