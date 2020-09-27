import json
json_data = open('newmap_HS.json').read()
data = json.loads(json_data)
new = []
cleanmap = []
for each in data:
    if isinstance(each[0], str):
        cleanmap.append(new)
        new = each
    else:
        new.append(each[0])
def writer(target,tbw):
    with open(target,'w') as outfile:
        json.dump(tbw,outfile)
writer('cleanmap_HS.json',cleanmap)