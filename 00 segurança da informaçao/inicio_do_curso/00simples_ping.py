import os

ip_ou_host = input("Digite o IP ou Host: ")

os.system(f'ping -n 3 {ip_ou_host}')