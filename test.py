import json
import networkx as nx
from networkx import *
import pandas as pd
import csv
kspace = read_yaml('kspace.yaml')
json_data = open('output.json').read()
data = json.loads(json_data)
def writer(target,tbw):
    with open(target,'w') as outfile:
        json.dump(tbw,outfile)

row0 = []
row1 = []
row2 = []
row3 = []
row4 = []

for each in data:
    row0.append(each[0])
    row1.append(each[1])
    row2.append(each[2])
    row3.append(each[3])
    row4.append(each[4])

with open('output.csv', mode='w+') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(row0)
    employee_writer.writerow(row1)
    employee_writer.writerow(row2)
    employee_writer.writerow(row3)
    employee_writer.writerow(row4)