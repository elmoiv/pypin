import bs4, json, re, requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
}

def getJson(html):
    soup = bs4.BeautifulSoup(html, "html.parser")

    # Get json script
    scriptTag = soup.find(
                'script',
                {
                    'id': '__PWS_DATA__',
                    'type': 'application/json'
                }
            )

    # __import__('pyperclip').copy(re.findall(r'>(.*)<', str(scriptTag))[0])
    
    # Extract json inside script
    return json.loads(re.findall(r'>(.*)<', str(scriptTag))[0])

def getHtml(url):
    # Redirect to main pin if shortened
    if 'pin.it' in url:
        url = requests.get(url).url
    
    try:
        _id = re.findall(r'/pin/([^/]+)', url)[0]
        return _id, requests.get(url).text
    except:
        return None, None

def decideType(jsonData):
    response = jsonData['props']['initialReduxState']['pins']
    
    # Handle if 404
    if not bool(response):
        return None, None
    
    _id = [*response.keys()][0]
    data = response[_id]
    
    # Get Video
    if data['videos']:
        return 0, data['videos']['video_list']['V_720P']['url']
    
    # Get Gif
    if data['embed']:
        return 1, data['embed']['src']
    
    # Get Image
    return 2, data['images']['orig']['url']