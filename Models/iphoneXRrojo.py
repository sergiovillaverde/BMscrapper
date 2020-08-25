from bs4 import BeautifulSoup
import requests, csv, os

# PRECIO IPHONE X PLATA 64GB
def iphoneXRrojo():
    url = 'https://www.backmarket.es/iphone-xr-64-gb-rojo-libre-segunda-mano/205401.html'
    response = requests.get(url)
    content = BeautifulSoup(response.content, "html.parser")

    eXRrojo = []
    pXRrojo = []
    for precio in content.find('div', attrs={"class":"_1OTebAgHAcWddAP7YhPlZr"}):
        #eXnegro.append("Estado")
        eXRrojo.append(precio.find('div', attrs={"class":"_3tVEyw2WXK4Ne75JtF4vL4"}).text.strip('\n\xa0€'))
        #pXnegro.append("Precio")
        pXRrojo.append(precio.find('div', attrs={"class":"_1KnTWVHWxp0RXYEjGmT44-"}).text.strip('\n\xa0€'))
        
    precioXRrojo= dict(zip(eXRrojo,pXRrojo))
        
    print(precioXRrojo)

    # Esto borra lo que tenga el CSV y escribe el diccionario
    # Cambiamos de directorio para guardar el CSV
    os.chdir(r"C:\Users\svill\Documents\Programación\Proyectos cortos Python\Backmarket scrapper\BMscrapper\CSV")
    with open('XRrojo.csv', 'w') as f:
            for key in precioXRrojo.keys():
                f.write("%s,%s\n"%(key,precioXRrojo[key]))
                
    with open('XRrojo.csv', 'r') as file_in:
        with open('iPhoneXRrojo.csv', 'w') as file_out:
            writer = csv.writer(file_out)
            for row in csv.reader(file_in):
                writer.writerow(row[:-1])
                
    os.remove('XRrojo.csv')