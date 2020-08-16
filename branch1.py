from bs4 import BeautifulSoup
import requests

url = 'https://www.backmarket.es/iphone-x-64-gb-gris-espacial-libre-segunda-mano/36833.html#?l=0'
response = requests.get(url)
content = BeautifulSoup(response.content, "html.parser")

for precio in content.find('div', attrs={"class":"_1OTebAgHAcWddAP7YhPlZr"}):
    precioXnegro= {
        "Estado": precio.find('div', attrs={"class":"_3tVEyw2WXK4Ne75JtF4vL4"}).text.strip('\n\xa0€'),
        "Precio": precio.find('div', attrs={"class":"_1KnTWVHWxp0RXYEjGmT44-"}).text.strip('\n\xa0€')
    }
    print(precioXnegro)