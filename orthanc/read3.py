from requests.auth import HTTPBasicAuth
import click
import requests
import json

@click.command()
@click.option('--res', default='patients', help='choose one of [patients, studies, series, instances]')
########################### убрать /\ вод это на ''
@click.option('--login', prompt='login: ', help='enter login')
@click.option('--passw', prompt='password: ', help='enter password')
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
    r = requests.get(url, auth=basic)
    
    list_data = r.content.decode('utf-8')
    print(f'list of {res}:')
    print(list_data)
    list_data = json.loads(list_data)

    for i in list_data:
        url = f'http://localhost:8042/{res}/{i}'
        print(requests.get(url, auth=basic).content.decode('utf-8'), end='\n\n')
        print('-----------------------------------------------------------', end='\n\n')


if __name__ == "__main__":
    main()