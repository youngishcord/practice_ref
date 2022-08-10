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
def main(id, res, dell):
    '''
    anon
    '''

    id_list = requests.get(f'http://localhost:8042/{res}').content.decode('utf-8')
    id_list = json.loads(id_list)
    print(f'id list from {res}')
    print(id_list)

    if id == None:
        id = input('input resource id: ')

    if id not in id_list:
        print('wrong id')
        return

    url = f'http://localhost:8042/{res}/{id}/anonymize'
    requests.post(url, data=json.dumps({}))

    if dell:
        requests.delete(f'http://localhost:8042/{res}/{id}')

if __name__ == "__main__":
    main()