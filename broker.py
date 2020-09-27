import json
json_data = open('pricelist.json').read()
data = json.loads(json_data)
price = 0
sum2 = 0
sums = []

for each in data:
    price = min(data[each])
    sum2 = price + sum2
    sums.append(price/1000000)

sums = sorted(sums,reverse = True)
print(sum2/1000000)
print(sums)
print(sums[68:])
print(sum(sums[68:]))