from pprint import pprint
from pydoc import cli
from requests.auth import HTTPBasicAuth
import requests
import json
import click
import sys


@click.command()
@click.option('--shout', is_flag=True)
def info(shout):
    rv = sys.platform
    if shout:
        rv = rv.upper() + '!!!!111'
    click.echo(rv)

if __name__ == '__main__':
    info()

'''basic = HTTPBasicAuth('yura', 'yurapass')
url = f'http://localhost:8042/patients/0ed1244f-bf3f53d5-368bdb86-3f685643-b9744043'
js = json.loads(requests.get(url, auth=basic).content.decode('utf-8'))
pprint(js['MainDicomTags']['PatientID'])



id_list = requests.get(f'http://localhost:8042/patients', auth=basic).content.decode('utf-8')
id_list = json.loads(id_list)
print(f'id list from patients')
print(id_list)



patientids = [json.loads(requests.get(f'http://localhost:8042/patients/{id}', auth=basic).content.decode('utf-8'))['MainDicomTags']['PatientID'] for id in id_list]
'''