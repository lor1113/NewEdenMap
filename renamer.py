import json
import requests
json_data = open('cleanmap_HS.json').read()
data = json.loads(json_data)
namedmap = []
new = []
def writer(target,tbw):
    with open(target,'w') as outfile:
        json.dump(tbw,outfile)

for each in data:
    for system in each:
        if isinstance(system, str):
            new.append(system)
        else:
            try:
                response = requests.get('https://esi.evetech.net/latest/universe/systems/'+ str(system) +'/?datasource=tranquility&language=en-us')
                r = response.json()
                new.append(r['name'])
            except:
                response = requests.get('https://esi.evetech.net/latest/universe/systems/'+ str(system) +'/?datasource=tranquility&language=en-us')
                r = response.json()
                new.append(r['name'])
    namedmap.append(new)
    print(new)
    new = []

writer('namedmap_HS.json',namedmap)