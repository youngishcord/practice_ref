from requests.auth import HTTPBasicAuth
import click
import requests
import json

@click.command()
@click.option('--res', default='patients', show_default=True,
                help='choose one of [patients, studies, series, instances]')
@click.option('--login', prompt='login', help='enter login')
@click.option('--passw', prompt='password', help='enter password', hide_input=True)
def main(res, login, passw):
    '''
    can read data from patients, studies, series, instances
    return json form
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

    url = f'http://localhost:8042/{res}'
    
    id_list = requests.get(url, auth=basic).content.decode('utf-8')
    print(f'list of {res}:')
    print(id_list)
    id_list = json.loads(id_list)

    for id in id_list:
        url = f'http://localhost:8042/{res}/{id}'
        print(requests.get(url, auth=basic).content.decode('utf-8'), end='\n\n')
        print('-----------------------------------------------------------', end='\n\n')


if __name__ == "__main__":
    main()