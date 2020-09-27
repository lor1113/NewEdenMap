import yaml
import networkx as nx
from networkx import *
map = read_yaml('kspace.yaml')

nodes = list(map.nodes(data='security'))
for node in nodes:
    if node[1] < 0:
        map.remove_node(node[0])
        print(node[1])
    if node[1] > 0.45:
        print(node[1])
        map.remove_node(node[0])

print(list(map.nodes))
write_yaml(map,'lowsec.yaml')