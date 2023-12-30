import ipaddress

ip = "192.168.0.1"

endereco = ipaddress.ip_address(ip)

print(endereco)


ip_rede = "192.168.0.0/24"

rede = ipaddress.ip_network(ip_rede, strict=False)

print(rede)

#imprimindo as redes

for ip in rede:
    print(ip)