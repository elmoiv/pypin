import os
from downloader import download
from tools import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))
__import__('warnings').filterwarnings("ignore")

os.makedirs('Pypin', exist_ok=1)
os.chdir('Pypin')

TYPES = [
    'Video',
    'GIF',
    'Image',
    ]

ID, HTML           =      getHtml(input('URL: '))
if ID == None:
    print('[ERROR] Not a Valid Pinterest URL')
    exit(0)

JSON               =      getJson(HTML)
TYPE, MEDIA_URL    =      decideType(JSON, ID)

if TYPE == None:
    print('[404] Nothing Found!')
    exit(0)

file_name = f'{ID}.{MEDIA_URL.split(".")[-1]}'

print(f'Downloading {TYPES[TYPE]}: {file_name}')
download(MEDIA_URL, file_name)