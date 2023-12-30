import hashlib

#precisamos de 2 arquivos para testar

arquivo1 = '05a.txt'
arquivo2 = '05b.txt'

hash1 = hashlib.new('ripemd160')
hash2 = hashlib.new('ripemd160')

hash1.update(open(arquivo1, 'rb').read())
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f"São diferentes! \n{hash1.hexdigest()}\n{hash2.hexdigest()}")
else:
    print(f"São iguais! \n{hash1.hexdigest()}\n{hash2.hexdigest()}")

#posso tbem pegar dados dos usuarios: mais irei pegar um caminho um pouco grande

senha = input("Digite sua senha: ")
arquivo_nome = "05ctestando.txt"

with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
    arquivo.write(senha)

hash3 = hashlib.new('ripemd160')
hash3.update(open(arquivo_nome, 'rb').read())

with open(arquivo_nome, 'a') as arquivo:
    arquivo.write(f'\n{hash3.hexdigest()}')

print(f'Arquivo Salvo: {hash3.hexdigest()}')

