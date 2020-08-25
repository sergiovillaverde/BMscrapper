from bs4 import BeautifulSoup
import requests, csv, os
import pandas as pd 

path = r"C:\Users\svill\Documents\Programación\Proyectos cortos Python\Backmarket scrapper\BMscrapper\CSV"

def getPrice():
    url = {}
    # TODO las keys serán el nombre del móvil y los values serán las url
    
    for k, v in url.items():
        url = str(v)
        response = requests.get(url)
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