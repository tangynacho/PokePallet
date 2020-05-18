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

boolean_keys = ['mega', 'ultra', 'starter', 'legendary', 'mythical', 'pseudo', 'baby', 'regional_bird', 'regional_rodent', 'regional_bug', 'fossil']
types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

pid = ""
while True:
    while not pid in data.keys() and not pid == "n":
        pid = input("Enter the ID of the regional form you wish to add (n to quit): ")

    if not pid == "n":
        origin = data[pid]
        print("Adding regional form for " + origin["name"])
        alolan = False
        galarian = False
        region = ""
        while not region in ["A", "G"]:
            region = input("Enter A for Alolan or G for Galarian: ").upper()
        pid = pid + region
        if region == "A":
            name = "Alolan " + origin["name"]
            img = origin["img"][:-4] + "-alolan.jpg"
            gen = 7
            alolan = True
        elif region == "G":
            name = "Galarian " + origin["name"]
            img = origin["img"][:-4] + "-galarian.jpg"
            gen = 8
            galarian = True
        type1 = ""
        while not type1 in types:
            type1 = input("Enter the first type of the new form: ")
        type2 = ""
        while (not type2 in types) and (not type2 == "n"):
            type2 = input("Enter the second type of the new form (n if none): ")
        if type2 == "n":
            ptypes = [type1]
        else:
            ptypes = [type1, type2]
        line = input("Enter the ID number of the first member of this pokemon's line: ")
        newbie = {
            "name": name,
            "img": img,
            "gen": gen,
            "types": ptypes,
            "line": line,
            "alolan": alolan,
            "galarian": galarian,
            "rating": 0
        }
        for bk in boolean_keys:
            newbie[bk] = False

        data[pid] = newbie

        with open(filename, 'w') as json_out:
            try:
                json.dump(data, json_out, indent=4)
                print('saved')
            except:
                print('error saving to file')
print("bye now")