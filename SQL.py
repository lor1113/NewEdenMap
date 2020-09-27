import sqlite3
import numpy as np
import networkx as nx
from networkx import *
import json
conn = sqlite3.connect('eve.db')
c = conn.cursor()
json_data = open('to_seed_id.json').read()
data = json.loads(json_data)
map2 = read_yaml('kspace.yaml')
ops = [4,5,6,12,13,14,17,20,24,32,37,38,39]
seedable = []
def writer(target,tbw):
    with open(target,'w') as outfile:
        json.dump(tbw,outfile)
def inter(lst1, lst2):
    return list(set(lst1) & set(lst2))
c.execute('SELECT * FROM stastations')
stations = c.fetchall()
for station in stations:
    if station[5] in ops:
        if station[8] in data:
            seedable.append([station[8],station[0]])

writer('price.json',seedable)