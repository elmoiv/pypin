from downloader import download
from tools import *

__import__('warnings').filterwarnings("ignore")

TYPES = [
    ('Video', 'mp4'),
    ('Image', 'jpg'),
    ('GIF',   'gif')
    ]

ID, HTML = getHtml(input('URL: '))
JSON = getJson(HTML)
_type, mediaUrl = decideType(JSON)

if _type == None:
    print('Nothing Found!')
    exit(0)

file_name = f'{ID}.{TYPES[_type][1]}'

print(f'Downloading {TYPES[_type][0]}: {file_name}')
download(mediaUrl, file_name)