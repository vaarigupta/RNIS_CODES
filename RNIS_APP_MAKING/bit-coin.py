import urllib.request
import matplotlib.pyplot as plt
import json
#import pprint  #preety print

url ='https://blockchain.info/charts/market-price?timespan=60days&format=json'
req = urllib.request.urlopen(url)
data = req.read()

parsed = json.loads(data)
list1 = []
bit = parsed['values'] # it's pointing to a list
for i in range(len(bit)):
    list1.append(bit[i]['y'])
    
   
    
plt.plot(list1)     
plt.show()
