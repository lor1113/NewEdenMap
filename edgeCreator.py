import json
json_data = open('namedmap_HS.json').read()
data = json.loads(json_data)
edges = []
start = ''
def writer(target,tbw):
    with open(target,'w') as outfile:
        json.dump(tbw,outfile)

for each in data:
    start = each[0]
    for link in each[1:]:
        edges.append([start,link])

writer('edges_HS.json',edges)