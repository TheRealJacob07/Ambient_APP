import api
import json
file = api.run()
data = json.dumps(file,sort_keys= True)
data2=json.loads(data)
print(data2['response'][0]['periods'][0]['tempF'])
print()