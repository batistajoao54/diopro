#servido para o cliente UDP

import socket
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("servidor socket criado com sucessso")
sleep(3)

host = "localhost"
porta = 5432

s.bind((host,porta))

mensagem = "\nServidor: Olá Cleinte"
sleep(3)

while True:
    dados,end = s.recvfrom(4096)

    if dados:
        print("servidor enviando mensagem...")
        sleep(3)
        s.sendto(dados + mensagem.encode(),end) #aparentimente tem um erro nessa parte?


