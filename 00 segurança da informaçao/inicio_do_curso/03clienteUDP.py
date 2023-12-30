#precisa criar um servidor para esse cliente

import socket
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente Socket criado com sucesso!")
sleep(3)

host = "localhost"
porta = 5432

mensagem = "Olá Servidor"
sleep(3)

try:
    print(f"Cliente: {mensagem}")
    sleep(3)
    s.sendto(mensagem.encode(),(host,porta))

    dados,servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f'Cliente: {dados}')
    sleep(3)
finally:
    print("Cliente fechando a conexao!")
    sleep(3)
    s.close()

