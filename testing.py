import networkx as nx
from networkx import *
import yaml
import pandas as pd
import json
map = read_yaml('lowsec.yaml')
data = pd.read_csv('seedable.csv')
seeds = data.seed.tolist()

def writer(target,tbw):
    with open(target,'w') as outfile:
        json.dump(tbw,outfile)


for seed in seeds:
    if seed not in list(map.nodes):
        print('popped')
        seeds.remove(seed)

print(seeds)
print(len(seeds))
writer('seedable_losec.json',seeds)
