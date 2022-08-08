from email.policy import default
from requests.auth import HTTPBasicAuth
import requests
import re
import click
import json
import os


@click.command()
@click.option('--pid', default=None, help='patientID to which attach')
@click.option('--attid', default=None, help='id of the attached resource')
@click.option('--name', default=None, help='you can rename patient')
@click.option('--login', prompt='login', help='enter login')
@click.option('--passw', prompt='password', help='enter password', hide_input=True)
def main(login, passw, pid, attid, name):
    pass


if __name__ == "__main__":
    main()