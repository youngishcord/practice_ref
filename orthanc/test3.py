import requests
from requests.auth import HTTPBasicAuth

path = './data/data_to_upl/Гаврилов SE1.zip'
url = 'http://localhost:8042/instances'
f = open(path, 'rb')
print(f)
content = f.read()
#print(content)
f.close()
basic = HTTPBasicAuth('yura', 'yurapass')
resp = requests.post(url, auth=basic, data=content)