import urllib
import json
KEY = "kljubTcPNjsXE2jJ2DGuM"
PKEY = "SSEr2T9ZbIUGgQENcK96G7wlNElwKFztaP0Xw4nB"
def api(location):
    import urllib.request
    import json.decoder
    KEY = "kljubTcPNjsXE2jJ2DGuM"
    PKEY = "SSEr2T9ZbIUGgQENcK96G7wlNElwKFztaP0Xw4nB"       
    request = urllib.request.urlopen("https://api.aerisapi.com/conditions/" + location + "?format=json&plimit=1&filter=1min&client_id="+KEY+"&client_secret="+PKEY)
    response = request.read()
    json = json.loads(response)
    if json['success']:
        return json
    else:
        print("An error occurred: %s" % (json['error']['description']))
        request.close()
        
def image_api():
    import imageio
    import urllib.request
    import cv2
    url = "https://radar.weather.gov/ridge/standard/KFWS_0.gif"
    fname = "tmp.gif"
    imdata = urllib.request.urlopen(url).read()
    open(fname,"wb+").write(imdata)
    gif = imageio.mimread(fname)
    return 'tmp.gif'

def run(location):
    data = api(location)
    jsondump = json.dumps(data, sort_keys= True)
    jsonloads = json.loads(jsondump)
    data_return = jsonloads['response'][0]['periods'][0]
    return data_return

def forcast_api(location):
    import urllib.request
    import json.decoder
    KEY = "kljubTcPNjsXE2jJ2DGuM"
    PKEY = "SSEr2T9ZbIUGgQENcK96G7wlNElwKFztaP0Xw4nB"       
    request = urllib.request.urlopen("https://api.aerisapi.com/forecasts/" + location + "?format=json&filter=day&limit=7&client_id=" + KEY + "&client_secret=" + PKEY)
    response = request.read()
    json = json.loads(response)
    if json['success']:
        return json
    else:
        print("An error occurred: %s" % (json['error']['description']))
        request.close()
    
def forecast_run(location):
    data = forcast_api(location)
    jsondump = json.dumps(data, sort_keys= True)
    jsonloads = json.loads(jsondump)
    data_return = jsonloads['response'][0]['periods']
    maxTemps = []
    lowTemps = []
    maxHum = []
    pre = []
    for i in data_return:
        maxTemps.append(str(i['maxTempF']) + 'F')
        lowTemps.append(str(i['minTempF']) + 'F')
        maxHum.append(str(i['humidity']) + '%')
        pre.append(str(i['precipIN']) + "IN")
    day = []
    for i in range(len(maxTemps)):
        day.append([maxTemps[i], lowTemps[i], maxHum[i], pre[i]])
    return day

    
    
    