import os
import PIL
import requests
import time
from PIL import Image
from colorama import *
init()
print("Starting program...")
url = 'https://fortnite-api.com/images/map_en.png'
r = requests.get(url, allow_redirects=True)
open('map.png', 'wb').write(r.content)
response = requests.get('https://benbotfn.tk/api/v1/status')
version = response.json()['currentFortniteVersionNumber']
print(Fore.BLUE+"Retrived The Map, Saving..")
img=Image.open('map.png')
img=img.resize((1200,1200),PIL.Image.ANTIALIAS)
img.save('smallmap.png')
os.remove('map.png')
print(Fore.BLUE+"saved the map")
print("Finished program. Closing in 5 seconds.")
time.sleep(5)