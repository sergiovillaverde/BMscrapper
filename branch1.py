from bs4 import BeautifulSoup
import requests

url = 'https://www.backmarket.es/iphone-x-64-gb-gris-espacial-libre-segunda-mano/36833.html#?l=0'
response = requests.get(url)
content = BeautifulSoup(response.content, "html.parser")

precio = content.find('div', attrs={"class":"_1OTebAgHAcWddAP7YhPlZr"})
print(precio.text)