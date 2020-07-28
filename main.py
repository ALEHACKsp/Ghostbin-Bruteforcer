import string
import random
import requests
import os
import threading
import ctypes
from threading import Thread
from colorama import Fore
lock = threading.Lock()
valid = 0
invalid = 0

os.system('cls')
if not os.path.exists('Ghostbin'): os.makedirs('Ghostbin')

def saveCapture(link, content):
    with open(f'Ghostbin/{link}.txt', 'w', encoding = 'UTF-8') as f:
        f.write(content + '\n')

def Main():
    global invalid
    global valid
    while True:
        Random = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(5))
        r = requests.get(f'https://ghostbin.co/paste/{Random}/raw')
        if r.status_code == 404:
            lock.acquire()
            print(f'{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}{r.url}')
            invalid += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f'[Ghostbin Bruteforcer] By Dropout | Valid: {valid} | Invalid: {invalid}')
            lock.release()
        else:
            lock.acquire()
            print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}{r.url}')
            valid += 1
            saveCapture(f'{Random}', f'{r.text}')
            ctypes.windll.kernel32.SetConsoleTitleW(f'[Ghostbin Bruteforcer] By Dropout | Valid: {valid} | Invalid: {invalid}')
            lock.release()

for i in range(0, 100):
    Thread(target=Main).start()
