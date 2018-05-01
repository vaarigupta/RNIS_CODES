import urllib.request
import json

import pprint
#key = 'GHK67945Ki8I9I9J9'
from sys import argv
print(argv)
url = 'http://samples.openweathermap.org/data/2.5/weather?q='+argv[1]+'&appid=b6907d289e10d714a6e88b30761fae22'

req = urllib.request.urlopen(url)
data = req.read()

parseddata = json.loads(data)
#pprint.pprint(parseddata)
#json.dumps()
#pprint.pprint(parseddata)
#weather1 = parseddata['main'][argv[1]]
#weather2 = parseddata['main'][argv[1]]
weather3 = parseddata['main'][argv[2]]
weather4 = parseddata['main'][argv[3]]

#pprint.pprint(weather1)
#pprint.pprint(weather2)
pprint.pprint(weather3)
pprint.pprint(weather4) 

