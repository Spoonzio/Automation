from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json, os, requests

# Initiate header
header = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}

# Function to insert header in url
def make_soup(url):
    req_link = Request(url, headers = header)
    return req_link

# Get input from user
term = str(input("What to search on Google images:\n"))

# Get input from user, include error catching
count = 0
while True:
    try:
        count = int(input("How many images to download? (Max 50)\n"))
    except (ValueError):
        print("Sorry, I didn't understand that.")
        continue

    if count <= 0 or count > 50:
        print("Please enter a positive nunber below 50")
    else:
        break
    
# Search on Google images, create soup
search_link = "https://www.google.com/search?q="+ term.replace(" ", "+") +"&source=lnms&tbm=isch"
print("Searching on Google images ("+ search_link+")...")
page = urlopen(make_soup(search_link))
soup = BeautifulSoup(page,"html.parser")

# Make directory if not exist
if not os.path.exists("Images"):
    os.mkdir("Images")

os.chdir("Images")

# Find meta data from page
flag = 0
for meta in soup.find_all("div", {"class" : "rg_meta"}):
    # Get img url, extension, name
    try: 
        img_link = json.loads(meta.text)["ou"]
        img_ext =  json.loads(meta.text)["ity"]
        img_name = ""
        for char in json.loads(meta.text)["pt"]:
            if char.isalnum() == False:
                img_name += "-"
            else:
                img_name += char

        if img_ext:
            img_name += ("." + img_ext)
            print("Saving "+ img_name +"...")
            
            r = requests.get(img_link)
            with open(img_name, "wb") as imgfile:
                imgfile.write(r.content)

            flag += 1
    except Exception:
        pass

    if flag == count:
        print("Saved " + str(flag) +" images of " + str(term))
        break