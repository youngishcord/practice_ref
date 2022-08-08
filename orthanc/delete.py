import click
import json
import requests
from requests.auth import HTTPBasicAuth


@click.command()
@click.option('--res', default='patients', help='choose one of [patients, studies, series, instances]')
########################### убрать /\ вот это на '' #########################################
@click.option('--id', default=None, help='you can write resource id in call')
@click.option('--login', prompt='login', help='enter login')
@click.option('--passw', prompt='password', help='enter password', hide_input=True)
def main(login, passw, res, id):
    '''
    can delete one resource
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

    if res not in ['patients', 'studies', 'series', 'instances']:
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

    url = f'http://localhost:8042/{res}/{id}'
    requests.delete(url, auth=basic)



if __name__ == "__main__":
    main()