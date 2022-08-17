from pprint import pprint
import requests
import json

def main() -> None:

    url = f'http://localhost:8042/changes'
    
    id_list = json.loads(requests.get(url).content.decode('utf-8'))
    a = id_list['Changes']
    print(a)
    for i in a:
        #print(i)
        if i['ChangeType'] == 'NewPatient':
            pprint(i)
            pprint


if __name__ == '__main__':
    main()