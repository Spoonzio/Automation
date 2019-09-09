import os

import requests
from PIL import Image

pixel = {0: " ", 1: ".", 2: ":", 3: "|", 4: "+", 5: "=", 6: "$", 7: "#", 8: "@"}

filepath = str(input("Full file location from drive to file extension, OR image URL:\n"))
imgfile = filepath
# try:
# if os.path.exists(filepath):
#     os.chdir(filepath)

#     for char in filepath:
#         path 
    
#     for char in reversed(filepath):
#         if char != "/" or char != "\\":
#             filename_rev += char 
#         else:
#             break

#     imgfile = filename_rev[::-1]

# except():
#     url = filepath.lower()
#     if not url.startswith("http"):
#         url = "HTTP://" + url

#     page = requests.get(filepath)
#     if 199 < page.status_code < 400:
#         imgfile = page.content

#     print("Not valid URL or valid path!")
#     exit

img = Image.open(imgfile)
width = img.size[0]
height = img.size[1]

img.convert(mode = "L")
loaded_img = img.load()

with open("ascii.txt", "w+") as txt_file:
    for i in range(0, height):
        line = ""
        for j in range(0,width):
            rgba = loaded_img[j,i]
            # print(str(brightness))
            # brightness = 250 - brightness[0]
            brightness = 0
            
            if len(rgba) == 4:
                brightness = rgba[3]
            else:
                brightness = sum(rgba)/3

            index = brightness//32
            if index > 7:
                index = 7
            char_pixel = pixel[index]
            line += char_pixel

        line += "\n"
        txt_file.write(line)



            
            
