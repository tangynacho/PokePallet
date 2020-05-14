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
    # change this based on the desired key to add
    data[d]["rating"] = 0

with open(filename, 'w') as json_out:
            try:
                json.dump(data, json_out, indent=4)
                print(pok["name"], k, "set to", pok[k])
            except:
                print('error saving to file')