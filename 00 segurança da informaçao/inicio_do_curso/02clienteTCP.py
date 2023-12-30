import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    except socket.error as e:
        print("A conexão Falhou!")
        print(f'Erro: {e}')
        sys.exit()
    print("Socket criado com sucesso!")


    HostAlvo = input("Digite o host ou IP: ")
    PortaAlvo = int(input("Digite a porta: "))

    try:
        s.connect((HostAlvo, PortaAlvo))
        print("Cliente TCP conectado!")
        s.shutdown(2)
    except socket.error as e:
        print("A conexao falhou")
        print(f'Erro : {e}')
        sys.exit()

if __name__ == '__main__':
    main()