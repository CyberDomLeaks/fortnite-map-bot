import os
import PIL
import requests
import time
from PIL import Image
from colorama import *
init()
print("Starting..")
url = 'https://fortnite-api.com/images/map_en.png'
r = requests.get(url, allow_redirects=True)
open('map.png', 'wb').write(r.content)
response = requests.get('https://benbotfn.tk/api/v1/status')
version = response.json()['currentFortniteVersionNumber']
print(Fore.BLUE+"Retrived The Map, Saving image..")
img=Image.open('map.png')
img=img.resize((1200,1200),PIL.Image.ANTIALIAS)
img.save('smallmap.png')
os.remove('map.png')
print(Fore.BLUE+"Saved map!")
print("Finished,losing in 2 seconds.")
time.sleep(2)
