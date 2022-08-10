from requests.auth import HTTPBasicAuth
import click
import requests
import json

@click.command()
@click.option('--res', default='patients', show_default=True,
                help='choose one of [patients, studies, series, instances]')
def main(res):
    '''
    can read data from patients, studies, series, instances
    return json form
    '''
    

    if res not in ['patients', 'studies', 'series', 'instances']:
        print('wrong request')
        return

    url = f'http://localhost:8042/{res}'
    
    id_list = requests.get(url).content.decode('utf-8')
    print(f'list of {res}:')
    print(id_list)
    id_list = json.loads(id_list)

    for id in id_list:
        url = f'http://localhost:8042/{res}/{id}'
        print(requests.get(url).content.decode('utf-8'), end='\n\n')
        print('-----------------------------------------------------------', end='\n\n')


if __name__ == "__main__":
    main()