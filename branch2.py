from bs4 import BeautifulSoup
from datetime import date
import requests, csv, openpyxl
import pandas as pd 

today = date.today().strftime('%d-%m-%Y')

def char_range(c1, c2):
    # Generamos los caracteres que le pasemos a c1 hasta c2
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

url = 'https://www.backmarket.es/iphone-x-64-gb-gris-espacial-libre-segunda-mano/36833.html#?l=0'
response = requests.get(url)
content = BeautifulSoup(response.content, "html.parser")

eXnegro = []
pXnegro = []
for precio in content.find('div', attrs={"class":"_1OTebAgHAcWddAP7YhPlZr"}):
    #eXnegro.append("Estado")
    eXnegro.append(precio.find('div', attrs={"class":"_3tVEyw2WXK4Ne75JtF4vL4"}).text.strip('\n\xa0€'))
    #pXnegro.append("Precio")
    pXnegro.append(precio.find('div', attrs={"class":"_1KnTWVHWxp0RXYEjGmT44-"}).text.strip('\n\xa0€'))
    
precioXnegro = dict(zip(eXnegro,pXnegro))
    
print(precioXnegro)

# Esto borra lo que tenga el CSV y escribe el diccionario
with open('precios.csv', 'w') as f:
        for key in precioXnegro.keys():
            f.write("%s,%s\n"%(key,precioXnegro[key]))
            
# Código para escribir en la hoja de cálculo
# TODO encontrar la casilla correspondiente al día y la columna en la que está

wb = openpyxl.load_workbook('Libro.xlsx')
book = wb['Hoja1']

for c in char_range('B', 'Z'):
    for n in range(2, 7):
        casilla = c + str(n)
        if book[casilla] is None:
            for v in precioXnegro.values():
                book[casilla] = v
                wb.save('Libro.xlsx')

'''
for columnNum in range(1, book.max_column):
    fecha = book.cell(row=1,column=columnNum).value
    if fecha == today:
        for i in range(5):
            book.cell(row=(i+1),column=columnNum).value = precioXnegro[]'''