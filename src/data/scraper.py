from bs4 import BeautifulSoup
import requests

domain = "https://pokemondb.net"
page_link = domain+"/pokedex/phantump"
run = True
bulba = True

while run:
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

    evo_info = main.find("div", attrs={"class": "infocard-list-evo"})
    if evo_info:
        line_members = evo_info.find_all("div", attrs={"class": "infocard"})
        line = line_members[0].find("span", attrs={"class": "infocard-lg-data text-muted"}).find_all("small")[0].text[1:]
        members = len(line_members)
    
    # print("#"+idnum)
    print(name)
    # print(img)
    # print(gen)
    # print(types)
    # print(line)
    # print(members)

    nav = main.nav
    links = nav.find_all("a")
    if len(links) > 1:
        page_link = domain + links[1]["href"]
    elif bulba:
        page_link = domain + links[0]["href"]
        bulba = False
    else:
        run = False