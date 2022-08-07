from concurrent.futures import thread
from email.policy import default
import click
import requests
from requests.auth import HTTPBasicAuth

@click.command()
@click.option('--fpath', default='./data/data_to_upl/')
@click.option('--fname', default=None, 
                help='''enter file-name with .zip or smt if\n
                file actually in current directory. Else you need add fpath''')#prompt='enter file-name'
@click.option('--login', prompt='login', help='enter login')
@click.option('--passw', prompt='password', help='enter password')
def main(login, passw, fpath, fname):
    '''
    upload DICOM files from .zip archive
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
    

    pass


if __name__ == "__main__":
    main()