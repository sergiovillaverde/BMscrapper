from bs4 import BeautifulSoup
import requests, csv, os

# PRECIO IPHONE X PLATA 64GB
def iphoneXRnegro():
    url = 'https://www.backmarket.es/iphone-xr-64-gb-negro-libre-segunda-mano/161659.html#?l=0'
    response = requests.get(url)
    content = BeautifulSoup(response.content, "html.parser")

    eXRnegro = []
    pXRnegro = []
    for precio in content.find('div', attrs={"class":"_1OTebAgHAcWddAP7YhPlZr"}):
        #eXnegro.append("Estado")
        eXRnegro.append(precio.find('div', attrs={"class":"_3tVEyw2WXK4Ne75JtF4vL4"}).text.strip('\n\xa0€'))
        #pXnegro.append("Precio")
        pXRnegro.append(precio.find('div', attrs={"class":"_1KnTWVHWxp0RXYEjGmT44-"}).text.strip('\n\xa0€'))
        
    precioXRnegro= dict(zip(eXRnegro,pXRnegro))
        
    print(precioXRnegro)

    # Esto borra lo que tenga el CSV y escribe el diccionario
    # Cambiamos de directorio para guardar el CSV
    os.chdir(r"C:\Users\svill\Documents\Programación\Proyectos cortos Python\Backmarket scrapper\BMscrapper\CSV")
    with open('XRnegro.csv', 'w') as f:
            for key in precioXRnegro.keys():
                f.write("%s,%s\n"%(key,precioXRnegro[key]))
                
    with open('XRnegro.csv', 'r') as file_in:
        with open('iPhoneXRnegro.csv', 'w') as file_out:
            writer = csv.writer(file_out)
            for row in csv.reader(file_in):
                writer.writerow(row[:-1])
                
    os.remove('XRnegro.csv')