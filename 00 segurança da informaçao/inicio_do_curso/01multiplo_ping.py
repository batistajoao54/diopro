import os
from time import sleep

with open('01host.txt') as file:
    dump = file.read()
    dump = dump.splitlines() #foi preciso separar por linhas para nao ter conflitos no loop

for ip in dump:
    os.system(f'ping -n 6 {ip}')

