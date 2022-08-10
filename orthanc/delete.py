import click
import json
import requests
from requests.auth import HTTPBasicAuth


@click.command()
@click.option('--res', default='patients', help='choose one of [patients, studies, series, instances]')
########################### убрать /\ вот это на '' #########################################
@click.option('--id', default=None, help='you can write resource id in call')
def main(res, id):
    '''
    can delete one resource
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

    url = f'http://localhost:8042/{res}/{id}'
    requests.delete(url)



if __name__ == "__main__":
    main()