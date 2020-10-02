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
JSON               =      getJson(HTML)
_type, mediaUrl    =      decideType(JSON)
EXT                =      mediaUrl.split('.')[-1]

if _type == None:
    print('Nothing Found!')
    exit(0)

file_name = f'{ID}.{EXT}'

print(f'Downloading {TYPES[_type]}: {file_name}')
download(mediaUrl, file_name)