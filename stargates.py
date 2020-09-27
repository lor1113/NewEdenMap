import requests
import json
newmap = []
counter = 0
json_data = open('map_HS.json').read()
data =json.loads(json_data)
new = []
def writer(target,tbw):
    with open(target,'w') as outfile:
        json.dump(tbw,outfile)

for system in data:
    counter = counter + 1
    new.append(system[0])
    for stargate in system[1]:
        try:
            response = requests.get('https://esi.evetech.net/latest/universe/stargates/'+ str(stargate) +'/?datasource=tranquility')
            r = response.json()
        except:
            response = requests.get('https://esi.evetech.net/latest/universe/stargates/'+ str(stargate) +'/?datasource=tranquility')
            r = response.json()
        try:
            new.append(r['destination']['system_id'])
            newmap.append(new)
            new = []
        except:
            print('ESI FUCKED UP')
            print(r)
            new = 0
    print(counter)
writer('newmap_HS.json',newmap)

