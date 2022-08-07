from requests.auth import HTTPBasicAuth
import click
import requests
import json

@click.command()
@click.option('--res', default='patients', help='choose one of [patients, studies, series, instances]')
@click.option('--login', prompt='login: ', help='enter login')
@click.option('--passw', prompt='password: ', help='enter password')
def main(res, login, passw):
    '''
    to choose from [patients, studies, series, instances]
    '''
    if res not in ['patients', 'studies', 'series', 'instances']:
        print('wrong request')
        return

    url = f'http://localhost:8042/{res}'
    basic = HTTPBasicAuth(login, passw)
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