import csv
from clase import url

with open('phonesURL.csv', 'w') as f:
    for key in url.keys():
        f.write("%s,%s\n"%(key,url[key]))