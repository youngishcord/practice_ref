from email.policy import default
from requests.auth import HTTPBasicAuth
import requests
import re
import click
import json
import os


@click.command()
@click.option('--res', default='patients', show_default=True, 
                help='choose one of [patients, studies, series]')
@click.option('--id', default=None, help='you can write resource id in call')
@click.option('--dell', is_flag=True, help='delete old data')
@click.option('--login', prompt='login', help='enter login')
@click.option('--passw', prompt='password', help='enter password', hide_input=True)
def main(login, passw, id, res, dell):
    '''
    anon
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

    if res not in ['patients', 'studies', 'series']:
        print('wrong request')
        return

    id_list = requests.get(f'http://localhost:8042/{res}', auth=basic).content.decode('utf-8')
    id_list = json.loads(id_list)
    print(f'id list from {res}')
    print(id_list)

    if id == None:
        id = input('input resource id: ')

    if id not in id_list:
        print('wrong id')
        return

    url = f'http://localhost:8042/{res}/{id}/anonymize'
    requests.post(url, auth=basic, data=json.dumps({}))

    if dell:
        requests.delete(f'http://localhost:8042/{res}/{id}', auth=basic)

if __name__ == "__main__":
    main()