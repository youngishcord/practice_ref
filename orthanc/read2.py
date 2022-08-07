import click
import requests

@click.command()
@click.option('--res', default='', help='choose one of [patients, studies, series, instances]')
@click.option('--data', default=None, help='ID for find DICOM data')
def main(res, data):
    '''
    to choose from [patients, studies, series, instances]
    '''
    if res not in ['patients', 'studies', 'series', 'instances']:
        print('wrong request')
        return

    url = f'http://localhost:8042/{res}'

    if data:
        url += f'/{data}'

    r = requests.get(url)
    print(f'list of {res}:')
    print(r.content.decode('utf-8'))


if __name__ == "__main__":
    main()