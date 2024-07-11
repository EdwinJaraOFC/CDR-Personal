class LoadBalancer:
    def __init__(self):
        self.servers = []  # Lista de servidores gestionados por el balanceador de carga

    def add_server(self, server):
        self.servers.append(server)
        print(f"Servidor {server.name} añadido al balanceador de carga.")  # Confirmación de servidor añadido

    def distribute_http_requests(self, requests):
        print("Distribuyendo solicitudes HTTP...")
        for i, request in enumerate(requests):
            server = self.servers[i % len(self.servers)]
            server.handle_request(request)

    def distribute_tcp_requests(self, requests):
        print("Distribuyendo solicitudes TCP...")
        for i, request in enumerate(requests):
            server = self.servers[i % len(self.servers)]
            server.handle_request(request)

class Server:
    def __init__(self, name):
        self.name = name  # Nombre del servidor
        self.requests_handled = 0  # Contador de solicitudes manejadas por el servidor

    def handle_request(self, request):
        self.requests_handled += 1
        print(f"Servidor {self.name} manejando solicitud: {request}")
        print(f"Solicitudes manejadas por {self.name}: {self.requests_handled}")

class Region:
    def __init__(self, name):
        self.name = name  # Nombre de la región
        self.servers = []  # Lista de servidores en la región
        self.load_balancer = LoadBalancer()  # Balanceador de carga para la región

    def add_server(self, server):
        self.servers.append(server)
        self.load_balancer.add_server(server)
        print(f"Servidor {server.name} añadido a la región {self.name}.")  # Confirmación de servidor añadido a la región

    def handle_request(self, request):
        self.load_balancer.distribute_http_requests([request])
        print(f"Solicitud manejada por la región {self.name}.")  # Confirmación de solicitud manejada por la región

    def replicate_data_to(self, other_region):
        print(f"Replicando datos de la región {self.name} a la región {other_region.name}.")  # Simulación de replicación de datos
        # Implementación de replicación de datos simulada
        other_region.servers = self.servers.copy()
        print(f"Datos replicados de la región {self.name} a la región {other_region.name}.")

class MultiRegionHA:
    def __init__(self):
        self.regions = []  # Lista de regiones

    def add_region(self, region):
        self.regions.append(region)
        print(f"Región {region.name} añadida al sistema de alta disponibilidad.")  # Confirmación de región añadida

    def route_request(self, request):
        # Simulación de enrutamiento basado en disponibilidad y rendimiento
        primary_region = self.regions[0]
        secondary_region = self.regions[1]
        try:
            primary_region.handle_request(request)
        except Exception as e:
            print(f"Falla en la región primaria: {e}")
            secondary_region.handle_request(request)
            print(f"Solicitud redirigida a la región secundaria {secondary_region.name}.")

# Ejemplo de uso
server1 = Server("Servidor 1")
server2 = Server("Servidor 2")

region1 = Region("us-east-1")
region1.add_server(server1)

region2 = Region("us-west-1")
region2.add_server(server2)

ha_system = MultiRegionHA()
ha_system.add_region(region1)
ha_system.add_region(region2)

# Simulación de replicación de datos
region1.replicate_data_to(region2)

# Enrutamiento de solicitudes
ha_system.route_request("Solicitud 1")
ha_system.route_request("Solicitud 2")
