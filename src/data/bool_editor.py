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

boolean_keys = ['mega', 'ultra', 'alolan', 'galarian', 'starter', 'legendary', 'mythical', 'pseudo', 'baby', 'regional_bird', 'regional_rodent', 'regional_bug', 'fossil']

for k in boolean_keys:
    inp = input("Change the value of *" + k + "* for some pokemon? (y/n): ")
    while not inp == "n":
        inp = input("id to change (n to stop): ")
        if inp == "n":
            continue
        pok = data[inp]
        if not pok:
            print("Invalid id, try again.")
            continue
        else:
            pok[k] = not pok[k]
        data[inp] = pok
        with open(filename, 'w') as json_out:
            try:
                json.dump(data, json_out, indent=4)
                print(pok["name"], k, "set to", pok[k])
            except:
                print('error saving to file')
