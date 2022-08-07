import requests
import re
import click

#url = 'http://localhost:8042/studies/0ed1244f-bf3f53d5-368bdb86-3f685643-b9744043/archive'

@click.command()
@click.argument("patientid")
def main(patientid):
    patients_list = requests.get('http://localhost:8042/patients').content.decode('utf-8')
    print(patients_list)
    
    if patientid not in patients_list:
        print('wrong patientID')
        return None
    
    url = f'http://localhost:8042/studies/{patientid}/archive'
    r = requests.get(url)

    filename = r.headers.get("Content-Disposition")
    filename = re.findall('filename=(.+)', filename)[0].replace('"', '')
    f = open(f"./data/data_downloaded/{filename}", 'wb')
    f.write(r.content)
    f.close()


if __name__ == "__main__":
    main()