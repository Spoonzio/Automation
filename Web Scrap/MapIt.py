import webbrowser, sys, pyperclip

address = pyperclip.paste()

while not address:
    address = str(input("Address: "))
    if not address:
        print("You did not enter any address.")

link = ('https://www.google.com/maps/place/'+ str(address)).replace(" ", "+")

try:
    print("Opening " + str(link) + " ...")
    webbrowser.open(link)

except Exception as e:
    print ("Webbrowser error: " % e)