import json
import networkx as nx
from statistics import mean
from networkx import *
from numpy import mean
import operator
banned = ["UUA-F4","A821-A","J7HZ-F","A-R00001","A-R00002","A-R00003","B-R00004","B-R00005","B-R00006","B-R00007","B-R00008","C-R00009","C-R00010","C-R00011","C-R00012","C-R00013","C-R00014","C-R00015","D-R00016","D-R00017","D-R00018","D-R00019","D-R00020","D-R00021","D-R00022","D-R00023","E-R00024","E-R00025","E-R00026","E-R00027","E-R00028","E-R00029","F-R00030","G-R00031","H-R00032"]
json_data = open('universe.json').read()
data = json.loads(json_data)
map = read_yaml('kspace.yaml')
map2 = read_yaml('kspace.yaml')

def namer(toname):
    named = []
    for name in toname:
        named.append(map.nodes[name]['name'])
    return named

for node in map.nodes:
    system = map.nodes[node]
    if system['security'] > 0.45:
        map2.remove_node(node)
    if system['security'] < 0:
        map2.remove_node(node)

write_yaml(map2,'lowsec.yaml')