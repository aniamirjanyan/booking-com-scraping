import json
import csv

with open('C:/Users/aniam/PycharmProjects/WebScraping/output2.json') as jf:
    data = json.load(jf)

df = open('dfile.csv', 'w')
csv_writer = csv.writer(df)

data = data[0]

for apartment in data:

    csv_writer.writerow(apartment.values())

df.close()

