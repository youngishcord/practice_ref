from pprint import pprint
from requests.auth import HTTPBasicAuth
import requests
import json

basic = HTTPBasicAuth('yura', 'yurapass')
url = f'http://localhost:8042/patients/0ed1244f-bf3f53d5-368bdb86-3f685643-b9744043'
js = json.loads(requests.get(url, auth=basic).content.decode('utf-8'))
pprint(js['MainDicomTags']['PatientID'])



id_list = requests.get(f'http://localhost:8042/patients', auth=basic).content.decode('utf-8')
id_list = json.loads(id_list)
print(f'id list from patients')
print(id_list)



patientids = [json.loads(requests.get(f'http://localhost:8042/patients/{id}', auth=basic).content.decode('utf-8'))['MainDicomTags']['PatientID'] for id in id_list]
