import random, string

tamanho = int(input("Tamanho da senha: "))

chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-_=+,.:;'

rnd = random.SystemRandom()
caracter : list = []

for i in range(tamanho):
    senha = rnd.choice(chars)
    caracter.append(senha)

resultado = "".join(caracter)
print(resultado)

#outro metodo de fazer o mesmo que os comando acima
#print(''.join(rnd.choice(chars) for i in range(tamanho)))
#essa unica linha faz o mesmo que as 5 linhas acima