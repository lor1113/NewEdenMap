import json
import networkx as nx
from networkx import *
import pandas as pd
kspace = read_yaml('kspace.yaml')
json_data = open('to_seed.json').read()
data = json.loads(json_data)
json_data2 = open('to_seed_id.json').read()
data2 = json.loads(json_data2)
to_seed = []
a = []
b = []
c = []
d = []
length = 0
names = list(kspace.nodes(data='name'))
print(names)
output = []
def writer(target,tbw):
    with open(target,'w') as outfile:
        json.dump(tbw,outfile)

for each in list(kspace.nodes(data = True)):
    if each[1]['name'] in data:
        a.append(each[1]['name'])
    for n in list(kspace.neighbors(each[0])):
        if kspace.nodes[n]['name'] in data:
            if kspace.nodes[n]['name'] not in a:
                b.append(kspace.nodes[n]['name'])
        for nn in list (kspace.neighbors(n)):
            if kspace.nodes[nn]['name'] in data:
                if kspace.nodes[nn]['name'] not in a:
                    if kspace.nodes[nn]['name'] not in b:
                        c.append(kspace.nodes[nn]['name'])
    if not a:
        if not b:
            if not c:
                for seed in data2:
                    if len(shortest_path(kspace,source=each[0],target=seed)) < length:
                        d = [kspace.node[seed]['name'],len(shortest_path(kspace,source=each[0],target=seed))-1]
                        length = len(shortest_path(kspace,source=each[0],target=seed))
    for cc in c:
        if cc in b:
            c.remove(cc)
    output.append([each[1]['name'],a,b,c,d])
    print([each[1]['name'],a,b,c,d])
    a = []
    b = []
    c = []
    d = []
    length = 100

writer('output.json',output)
