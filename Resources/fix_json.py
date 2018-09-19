import json
from pprint import pprint

with open('candy_full.json') as f:
    data = json.load(f)



chunk = []
filenum = 1
for i in range(len(data)):
    chunk.append(data[i])
    if i+1 % 5000 == 0:
        fp = open("candy_full_formatted_"+str(filenum)+".json","w")
        filenum += 1
        fp.write(json.dumps(chunk,indent=4, separators=(',', ': ')))
        fp.close()
        chunk = []



fp = open("candy_full_formatted_"+str(filenum)+".json","w")
fp.write(json.dumps(chunk,indent=4, separators=(',', ': ')))
fp.close()
