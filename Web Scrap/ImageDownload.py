from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import time

# Initiate browser
path = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
browser = webdriver.Chrome(path)

# Get input from user
term = str(input("What to search on Google images:\n"))

# Get input from user, include error catching
try:
    count = int(input("How many images to download?\n"))
except(TypeError):
    print("Please enter an integer")

# Search on Google
search_link = "https://www.google.com/search?q=" + term.replace(" ", "+")
browser.get(search_link)
links = browser.find_elements_by_css_selector("a.q.qs")

# Select the Image tab
for link in links:
    link_text = link.text
    if link_text == "Images":
        link.click()
        break

# Select all images
img_links = browser.find_elements_by_css_selector(".rg_ic.rg_i")

# browser.full

# Click, get image and name, save
for img_link in img_links[:count]:
    img_link.click()

    image = browser.find_element_by_css_selector("img.irc_mi")
    img_url = image.get_attribute("src")

    img_name_link = browser.find_element_by_css_selector("a.irc_pt.irc_tas.irc-cms.i3598.irc_lth")
    img_name = img_name_link.text + ".jpeg"
    print(str(img_url) + " # " + str(img_name))
    urllib.request.urlretrieve(img_url, img_name)
    print("Saved "+ img_name)
    
# Close Browser
browser.close()