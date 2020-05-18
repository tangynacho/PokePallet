import json
import os.path

filename = 'pokemon.json'
data = {}
if os.path.isfile(filename):
    with open(filename) as json_file:
        try:
            data = json.load(json_file)
            print('json file loaded')
        except:
            print('invalid json file!')
else:
    print('{} does not exist'.format(filename))

boolean_keys = ['mega', 'ultra', 'alolan', 'starter', 'legendary', 'mythical', 'pseudo', 'baby', 'regional_bird', 'regional_rodent', 'regional_bug', 'fossil']

pid = ""
while not pid in data.keys() or pid == "n":
    pid = input("Enter the ID of the regional form you wish to add (n to quit):")

if not pid == "n":
    origin = data[pid]
    region = ""
    while not region in ["A", "G"]:
        region = input("Enter A for Alolan or G for Galarian:").upper()
    pid = pid + region
    if region == "A":
        name = "Alolan " + origin.name
        img = origin.img[:-4] + "-alolan.jpg"
        gen = 7
    elif region == "G":
        name = "Galarian " + origin.name
        img = origin.img[:-4] + "-galarian.jpg"
        gen = 8
    

with open(filename, 'w') as json_out:
    try:
        json.dump(data, json_out, indent=4)
        print('saved')
    except:
        print('error saving to file')