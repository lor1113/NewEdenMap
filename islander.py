import json
cleanedges = []
json_data = open('edges_HS.json').read()
data = json.loads(json_data)
islands = ['Actee','Aikantoh','Aivoli','Algasienan','Allebin','Amane','Anher','Antiainen','Arasare','Archavoinet','Artisine','Arveyil','Atai','Atgur','Avada','Bamiette','Bazadod','Boystin','Brellystier','Chibi','Chidah','Clarelam','Clorteler','Droselory','Eggheron','Elanoda','Eldulf','Endatoh','Endrulf','Erindur','Erkinen','Erzoh','Faktun','Fegomenko','Fera','Furskeshin','Gererique','Haimeh','Halenan','Hayumtom','Hodrold','Horaka','Hroduko','Iffrue','Imata','Ivorider','Jangar','Jotenen','Kattegaud','Keba','Kiskoken','Komaa','Kurmaru','Larryn','Lazer','Liukikka','Lour','Maire','Mili','Mishi','Moh','Mollin','Niballe','Nidebora','Octanneve','Odette','Odinesyn','Oerse','Oishami','Olide','Ommaerrer','Ondree','Orien','Osmallanais','Ossa','Otalieto','Otomainen','Otraren','Pahineh','Palpis','Perckhevin','Piri','Pochelympe','Postouvin','Rauntaka','Satalama','Sazilid','Semiki','Serad','Shenda','Shenela','Sooma','Stegette','Stoure','Uesuro','Uhtafal','Uktiad','Ulerah','Varigne','Vecodie','Vilinnon','Vivanier','Weraroix','Yvaeroure','Yvelet','Zaveral']
def writer(target,tbw):
    with open(target,'w') as outfile:
        json.dump(tbw,outfile)
def contains(a, b):
    a_set = set(a)
    b_set = set(b)
    if len(a_set.intersection(b_set)) > 0:
        return(True)
    return(False)

for edge in data:
    if contains(edge,islands):
        print('HS Island')
    else:
        cleanedges.append(edge)

writer('edges_HS.json',cleanedges)