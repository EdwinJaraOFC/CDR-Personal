class VPC:
    """
    Podemos simular la creación de VPCs y subredes usando clases en 
    Python para representar estos elementos.
    """
    def __init__(self, cidr):
        self.cidr = cidr
        self.subnets = []

    def add_subnet(self, cidr):
        subnet = Subnet(cidr)
        self.subnets.append(subnet)

class Subnet:
    def __init__(self, cidr):
        self.cidr = cidr

# Crear una VPC
vpc = VPC('10.0.0.0/16')

# Añadir subredes
vpc.add_subnet('10.0.1.0/24')
vpc.add_subnet('10.0.2.0/24')

# Mostrar la configuración de la VPC
print(f"VPC CIDR: {vpc.cidr}")
for subnet in vpc.subnets:
    print(f"Subred CIDR: {subnet.cidr}")