import csv, os
from clase import url

with open('phonesURL.csv', 'r') as infile:
    reader = csv.reader(infile)
    with open('csvtodict.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        url = {rows[0]:rows[1] for rows in reader}
        
os.remove('csvtodict.csv')

print(url)