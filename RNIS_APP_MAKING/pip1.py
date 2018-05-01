import urllib.request
import json

import pprint
#key = 'GHK67945Ki8I9I9J9'
from sys import argv
url = 'http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22'

req = urllib.request.urlopen(url)
data = req.read()
pprint.pprint(data)
#print(type(data))
#print(type(req))

parseddata = json.loads(data)
print(type(parseddata))
pprint.pprint(parseddata)
#json.dumps()
#pprint.pprint(parseddata)
weather = parseddata['name']['london']
pprint.pprint(weather)                             
 
