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

valid_keys = ['name', 'img', 'gen', 'types', 'line', 'stage', 'stages']
types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
gens = [1, 2, 3, 4, 5, 6, 7, 8]

while True:
    pid = ""
    while not pid in data.keys() and not pid == "n":
        pid = input("Enter the ID of the pokemon whose keys you wish to edit (n to quit): ")
    if not pid == "n":    
        while True:
            print("Editing keys for " + data[pid]["name"])
            key = ""
            while not key in valid_keys and not key == "n":
                key = input("Enter the key you wish to edit (n to quit): ")
            if not key == "n":
                print("Current value is: " + data[pid][key])
                val = None
                if key == "types":
                    t1 = ""
                    while not t1 in types:
                        t1 = input("Enter first new type: ")
                    t2 = ""
                    while not t2 in types and not t2 == "n":
                        t2 = input("Enter second new type (n if none): ")
                    val = [t1]
                    if not t2 == "n":
                        val.append(t2)
                elif key == "gen":
                    while not val in gens:
                        val = input("Enter the new gen: ")
                else:
                    val = input("Enter the new value: ")
                data[pid][key] = [val]
                with open(filename, 'w') as json_out:
                    try:
                        json.dump(data, json_out, indent=4)
                        print('saved')
                    except:
                        print('error saving to file')
            else:
                break
    else:
        break
print("bye now")
        
