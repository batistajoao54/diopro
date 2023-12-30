from threading import Thread
from time import sleep

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        print(f'Carro: {piloto} {trajeto}')
        trajeto += velocidade
        sleep(0.5)

t_carro1 = Thread(target=carro, args=[10,"João"])
t_carro2 = Thread(target=carro, args=[5,'Batista'])

t_carro1.start()
t_carro2.start()

#precisamos estudar mais sobre essa biblioteca no futuro