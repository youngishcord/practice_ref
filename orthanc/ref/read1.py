import click
import requests

@click.command()
@click.argument('data')
def main(data):
    '''
    to choose from [patients, studies, series, instances]
    '''
    if data not in ['patients', 'studies', 'series', 'instances']:
        print('wrong request')
        return
    url = f'http://localhost:8042/{data}'

    r = requests.get(url)
    print(f'list of {data}:')
    print(r.content.decode('utf-8'))


if __name__ == "__main__":
    main()