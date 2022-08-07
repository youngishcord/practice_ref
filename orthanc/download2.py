from requests.auth import HTTPBasicAuth
import requests
import re
import click
import json
import os

#############################################################################################
#############################################################################################
#############################################################################################

#допилить создание папки со скачанными архивами если ее нет

#############################################################################################
#############################################################################################
#############################################################################################

#url = 'http://localhost:8042/studies/0ed1244f-bf3f53d5-368bdb86-3f685643-b9744043/archive'

@click.command()
@click.option('--res', default='patients', help='choose one of [patients, studies, series]')
########################### убрать /\ вот это на '' #########################################
@click.option('--id', default=None, help='you can write resurces id in call')
@click.option('--login', prompt='login', help='enter login')
@click.option('--passw', prompt='password', help='enter password')
def main(res, id, login, passw):
    '''
    download DICOM files as zip archive
    can download patient, studies or series archive
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
        id = input('input resurce id : ')
    
    if id not in id_list:
        print('wrong id')
        return 
    
    url = f'http://localhost:8042/{res}/{id}/archive'
    r = requests.get(url, auth=basic)

    filename = r.headers.get("Content-Disposition")
    filename = re.findall('filename=(.+)', filename)[0].replace('"', '')
    try:
        os.makedirs('./data/data_downloaded')
    except:
        pass
    f = open(f"./data/data_downloaded/{filename}", 'wb')
    f.write(r.content)
    f.close()


if __name__ == "__main__":
    main()