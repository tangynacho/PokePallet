from bs4 import BeautifulSoup
import requests
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

domain = "https://pokemondb.net"
page_link = domain+"/pokedex/bulbasaur"
run = True
bulba = True

while run:
    pokemon = {}

    page_response = requests.get(page_link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")

    main = page_content.main
    name = main.find("h1").text
    gen = int(main.find_all("div")[0].find_all("div")[0].find_all("p")[0].abbr.text[-1])

    tabset = main.find_all("div", attrs={"class": "tabset-basics tabs-wrapper tabs-onetab"})
    if not tabset:
        tabset = main.find("div", attrs={"class": "tabset-basics tabs-wrapper"})
    else:
        tabset = tabset[0]
    tab = tabset.find_all("div")[1].find_all("div")[0]
    panels = tab.find_all("div", attrs={"class": "grid-row"})[0].find_all("div")
    img_holder = panels[0].find_all("p")[0].a
    img = None
    if img_holder:
        img = img_holder["href"]
    else:
        img = panels[0].find_all("p")[0].img["src"]
    table = panels[1].table.tbody.find_all("tr")
    idnum = table[0].td.strong.text
    types = [x.text for x in table[1].td.find_all("a")]

    line = idnum
    evo_info = main.find("div", attrs={"class": "infocard-list-evo"})
    if evo_info:
        line_members = evo_info.find_all("div", attrs={"class": "infocard"})
        line = line_members[0].find("span", attrs={"class": "infocard-lg-data text-muted"}).find_all("small")[0].text[1:]
    
    pokemon["name"] = name
    pokemon["img"] = img
    pokemon["gen"] = gen
    pokemon["types"] = types
    pokemon["line"] = line
    for boo in boolean_keys:
        pokemon[boo] = False

    data[idnum] = pokemon
    with open(filename, 'w') as json_out:
        try:
            json.dump(data, json_out, indent=4)
            print(name)
        except:
            print('error saving to file')

    nav = main.nav
    links = nav.find_all("a")
    if len(links) > 1:
        page_link = domain + links[1]["href"]
    elif bulba:
        page_link = domain + links[0]["href"]
        bulba = False
    else:
        run = False
    
    # run = False