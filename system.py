import socket
import os
import requests
from time import sleepr
name = socket.gethostname()
IP = socket.gethostbyname(name)
token = '' # your bot token
ID = '' # your telegram ID
web = f'https://pastebin.com/raw/MfKc94Pu'
tele_api = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=new user : {IP} '
print('''
     [1] log in
     [2] send ip 
''')
check = input('Enter a number : ')
if check == '1':
    req = requests.get(web).text
    if f'{IP}' in req:
        print('Logged in')
    else:
        print('Error')
        exit()
if check == '2':
    tele = requests.get(tele_api).status_code
    sleep(1)
    print('Your ip was sent to the developer ')
else:
    print('Thanks for using me ! , goodbye ')
    input(' ')
    exit()
