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

# Ejemplo de uso
server1 = Server("Servidor 1")
server2 = Server("Servidor 2")
load_balancer = LoadBalancer()
load_balancer.add_server(server1)
load_balancer.add_server(server2)

# Distribuyendo solicitudes HTTP
load_balancer.distribute_http_requests(["Solicitud HTTP 1", "Solicitud HTTP 2", "Solicitud HTTP 3"])

# Distribuyendo solicitudes TCP
load_balancer.distribute_tcp_requests(["Solicitud TCP 1", "Solicitud TCP 2"])
