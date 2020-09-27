import requests
import json
systems = []
system_info = []
response = requests.get('https://esi.evetech.net/latest/universe/systems/?datasource=tranquility')
systems = response.json()
def writer(target,tbw):
    with open(target,'w') as outfile:
        json.dump(tbw,outfile)
for each in systems:
    if each < 31000000:
        print(each)
        try:
            response = requests.get('https://esi.evetech.net/latest/universe/systems/'+ str(each) +'/?datasource=tranquility&language=en-us')
            system_info.append(response.json())
        except:
            response = requests.get('https://esi.evetech.net/latest/universe/systems/'+ str(each) +'/?datasource=tranquility&language=en-us')
            system_info.append(response.json())
print(system_info)
writer('system_data.json',system_info)
