import requests, webbrowser, random
from bs4 import BeautifulSoup

def collect():
    term = str(input("What gadget review would you like to read?\n"))
    link = "https://www.google.com/search?q=" + term.replace(" ", "+") + "+review"
    print("extracting from " + link)    
    searchpage = requests.get(link)
    searchpage.raise_for_status()
    parse(searchpage)

def parse(fpage):
    soup = BeautifulSoup(fpage.text, "html.parser")
    result = (soup.select('a[href^="/url?q="]'))
    random.shuffle(result)

    for link in result[:5]:
        temp = str(link)[16:]
        for c in range(len(temp)):
            keyword = temp[c:c+4]
            if keyword == "&amp":
                
                href = temp[0:c]
                break

        webbrowser.open_new(href)

collect()

