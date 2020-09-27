#Sorry Regus!
import json
import networkx as nx
import requests
from networkx import *
json_data = open('price.json').read()
data = json.loads(json_data)
print(len(data))
output = {}
name = ''

def writer(target,tbw):
    with open(target,'w') as outfile:
        json.dump(tbw,outfile)

for station in data:
    request = requests.get('https://esi.evetech.net/latest/universe/stations/' + str(station[1]) + '/?datasource=tranquility')
    stat = request.json()
    print(stat)
    name = stat['name'].split(' ', 1)[0]
    if name in list(output.keys()):
        output[name].append(stat['office_rental_cost'])
    else:
        output.update({name:[stat['office_rental_cost']]})


writer('pricelist.json',output)