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

for d in data:
    pok = data[d]
    print(pok["name"])
    pok["stage"] = input("Enter stage: ")
    pok["stages"] = input("Enter stages: ")
    with open(filename, 'w') as json_out:
        try:
            json.dump(data, json_out, indent=4)
            print('saved')
        except:
            print('error saving to file')