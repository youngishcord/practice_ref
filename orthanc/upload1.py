import os
import click
import requests
from requests.auth import HTTPBasicAuth

@click.command()
@click.option('--fpath', default='./', help='enter folder with .zip or files')
@click.option('--fname', default=None,
                help='''enter file-name with .zip or smt if
                file actually in current directory. Else you need add fpath.''')#prompt='enter file-name'
def main(fpath, fname):
    '''
    Upload DICOM files from .zip archive or folder.
    If you have space in fname or fpath use ` or ^
    '''
    url = 'http://localhost:8042/instances'

    
    if fname == None:
        if fpath[-4:] in ['.zip']:
            with open(fpath, 'rb') as f:
                requests.post(url, data=f.read())
        
        else:
            fname = os.listdir(fpath)

            for i in fname:
                with open(fpath+i, 'rb') as f:
                    requests.post(url, data=f.read())

    else:
        with open(fpath+fname, 'rb') as f:
            requests.post(url,data=f.read())


if __name__ == "__main__":
    main()