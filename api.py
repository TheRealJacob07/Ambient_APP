import urllib
import json
import os
import ast
KEY = "kljubTcPNjsXE2jJ2DGuM"
PKEY = "SSEr2T9ZbIUGgQENcK96G7wlNElwKFztaP0Xw4nB"
def api():
    import urllib.request
    import json.decoder
    KEY = "kljubTcPNjsXE2jJ2DGuM"
    PKEY = "SSEr2T9ZbIUGgQENcK96G7wlNElwKFztaP0Xw4nB"       
    request = urllib.request.urlopen("https://api.aerisapi.com/conditions/pws_aledo?format=json&plimit=1&filter=1min&client_id="+KEY+"&client_secret="+PKEY)
    response = request.read()
    json = json.loads(response)
    if json['success']:
        return json
    else:
        print("An error occurred: %s" % (json['error']['description']))
        request.close()

def run():
    data = api()
    jsondump = json.dumps(data, sort_keys= True)
    jsonloads = json.loads(jsondump)
    data_return = jsonloads['response'][0]['periods'][0]
    return data_return


    
    
    