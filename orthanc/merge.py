from email.policy import default
from requests.auth import HTTPBasicAuth
import requests
import re
import click
import json
import os


@click.command()
@click.option('--pid', default=None, help='patientID to which attach')
@click.option('--attid', default=None, help='id of the attached resource')
@click.option('--name', default=None, help='you can rename patient')
@click.option('--login', prompt='login', help='enter login')
@click.option('--passw', prompt='password', help='enter password', hide_input=True)
def main(login, passw, pid, attid, name):
    '''
    comment
    '''

    basic = HTTPBasicAuth(login, passw)
    try:
        q = requests.get('http://localhost:8042/system', auth=basic).content.decode('utf-8')
        if q == '':
            print('wrong login or password 1')
            return
    except:
        print('wrong login or password 2')
        return 

    id_list = requests.get(f'http://localhost:8042/patients', auth=basic).content.decode('utf-8')
    print(f'id list from patients')
    print(id_list)
    id_list = json.loads(id_list)
    
    patientids = [json.loads(requests.get(f'http://localhost:8042/patients/{id}', auth=basic).content.decode('utf-8'))['MainDicomTags']['PatientID'] for id in id_list]
    #for id in id_list:
    #    url = f'http://localhost:8042/patients/{id}'
    #    js = json.loads(requests.get(url, auth=basic).content.decode('utf-8'))
    #    patientids.append(js['MainDicomTags']['PatientID'])

    if attid == None:
        attid = input('input id of the attached resource: ') #можно переписать сценарий через echo click
    
    if attid not in id_list:
        print('wrong attached id')
        return

    if pid == None:
        pid = input('input patientID to which attach: ')
    
    if pid not in patientids:
        print('wrong patientid')
        return 
    
    if name == None:
        js = {"Replace":{"PatientID":pid},"Force":True}
    else:
        js = {"Replace":{"PatientID":pid,"PatientName":name},"Force":True}

    url = f'http://localhost:8042/patients/{attid}/modify'
    requests.post(url, auth=basic, data=json.dumps(js))

    requests.delete(f'http://localhost:8042/patients/{attid}', auth=basic)

if __name__ == "__main__":
    main()