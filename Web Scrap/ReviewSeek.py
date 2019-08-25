# Import Request, bs4
import requests
import webbrowser
import random
from bs4 import BeautifulSoup

# Gather user's search term


def collect():
    term = str(input("What gadget review would you like to read?\n"))
    link = "https://www.google.com/search?q=" + \
        term.replace(" ", "+") + "+review"
    print("extracting from " + link)

    # Get a page with the search results
    searchpage = requests.get(link)
    searchpage.raise_for_status()

    # Pass the page
    parse(searchpage)

# Filter given page


def parse(fpage):
    soup = BeautifulSoup(fpage.text, "html.parser")

    # Find all tags with href
    result = (soup.select('a[href^="/url?q="]'))
    random.shuffle(result)

    # Extract 5 link from html script
    for link in result[:5]:
        temp = str(link)[16:]

        # Find the end of the link
        for c in range(len(temp)):
            keyword = temp[c:c+4]
            if keyword == "&amp":

                href = temp[0:c]
                break

        # Open link in browser
        webbrowser.open_new(href)


collect()