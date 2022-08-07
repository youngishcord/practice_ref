import requests
from requests.auth import HTTPBasicAuth
import os
import pydicom

path = './data/data_to_upl/SE4/'
url = 'http://localhost:8042/instances'
content = os.listdir(path)
#print(content)
#print(path+content[0])
'''with open("IM1", "rb", encoding="cp1251") as f:
    contents = f.read()'''
for i in content:
    print(f'start upload {i}')
    f = open(path+i, 'rb')
    q = f.read()
    f.close()
    basic = HTTPBasicAuth('yura', 'yurapass')
    resp = requests.post(url, auth=basic, data=q)
    print('end')