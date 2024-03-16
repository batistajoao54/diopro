from time import sleep

menu = """
<><><><><><><><><><><><><><><><><>

(d) - DEPOSITO
(s) - SAQUE
(e) - EXTRATO
(p) - SAIR

<><><><><><><><><><><><><><><><><>
""" 

#variaveis que usarei para o projeto
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3 #uma variavel toda em maiuscula é considerada uma constante



#iniciando a logica do sistema

while True:

    opcao = input(menu)

    #tratando do deposito
    if opcao == "d":
        valor = float(input("Informe o valor de deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'

        else:
            print("Operaçao falhou: Valor informado invalido.")
            sleep(2)

    #tratando do saque
    elif opcao == "s":
        valor = float(input("informe o valor de saque: "))

        #criando variaveis de logica para ajudar nas operacoes
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operaçao falhou: Você não tem saldo suficiente")
            sleep(2)    

        elif excedeu_limite:
            print("Operação falhou: O valor do saque excedeu seu limite.")
            sleep(2)
        
        elif excedeu_saque:
            print("Operação falhou: Numero maximo de saques excedido.")
            sleep(2)
        
        elif valor > 0:
            saldo += valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
        
        else:
            print("Operação Falhou: O valor informado invalido")
            sleep(2)
    
    #operaçao para o extrato
    elif opcao == "e":
        print("********************************")
        print("Não foram realizadas movimentações." if not extrato else extrato) #fazer uma revisao sobre esse assunto
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("********************************")
        sleep(2)

    

    #parar o sistema
    elif opcao == "p":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operaçao desejada")
        sleep(2)
