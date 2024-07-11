"""
Direccionamiento IP y CIDR
Podemos escribir un script en Python que calcule y muestre 
rangos de direcciones IP basados en CIDR.
"""

from ipaddress import ip_network

# Rango CIDR
cidr = '192.168.1.0/24'

# Crear una red basada en el CIDR
network = ip_network(cidr)

# Mostrar todas las direcciones IP en la red
print(f"Rango de direcciones IP para {cidr}:")
for ip in network.hosts():
    print(ip)
