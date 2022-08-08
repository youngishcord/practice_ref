import os
import click
import requests
from requests.auth import HTTPBasicAuth

@click.command()
@click.option('--fpath', default='./', help='enter folder with .zip or files')
@click.option('--fname', default=None,
                help='''enter file-name with .zip or smt if
                file actually in current directory. Else you need add fpath.''')#prompt='enter file-name'
@click.option('--login', prompt='login', help='enter login')
@click.option('--passw', prompt='password', help='enter password', hide_input=True)
def main(login, passw, fpath, fname):
    '''
    Upload DICOM files from .zip archive or folder.
    If you have space in fname or fpath use ` or ^
    '''
    url = 'http://localhost:8042/instances'
    basic = HTTPBasicAuth(login, passw)
    try:
        q = requests.get('http://localhost:8042/system', auth=basic).content.decode('utf-8')
        if q == '':
            print('wrong login or password 1')
            return
    except:
        print('wrong login or password 2')
        return 
    
    if fname == None:
        if fpath[-4:] in ['.zip']:
            with open(fpath, 'rb') as f:
                requests.post(url, auth=basic, data=f.read())
        
        else:
            fname = os.listdir(fpath)

            for i in fname:
                with open(fpath+i, 'rb') as f:
                    requests.post(url, auth=basic, data=f.read())

    else:
        with open(fpath+fname, 'rb') as f:
            requests.post(url, auth=basic, data=f.read())


if __name__ == "__main__":
    main()