import os
import json
from vardxg import Center
import requests
import time

os.system('cls')

def logo():
    vardxg = ("""
    Instander Last Update Infos V1
    """)
    print(Center.XCenter(vardxg))


def main():

    logo()

    while True:
        for i in range(1):
            url = "https://thedise.me/instander/ota.json"
            response = requests.get(url)
            data = json.loads(response.text)
            version = data['version']
            changelog = data['changelog']
            link = data['link']
            print("\n Version: ", version)
            print("\n Changelog: ", changelog)
            print("\n Link: ", link)
            time.sleep(4)
            os.system('cls')
            main()

main()

# -> Made by @vardxg on Telegram!
