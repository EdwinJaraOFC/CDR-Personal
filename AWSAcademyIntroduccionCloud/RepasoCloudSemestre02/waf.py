class WebApplicationFirewall:
    def __init__(self):
        self.rules = []  # Lista de reglas del firewall

    def add_rule(self, rule):
        self.rules.append(rule)  # Añade una nueva regla al firewall
        print(f"Regla añadida: {rule.__name__}")

    def apply_rules(self, request):
        for rule in self.rules:
            if not rule(request):
                print(f"Solicitud bloqueada por la regla: {rule.__name__}")  # Mensaje de bloqueo de solicitud
                return False
        print("Solicitud permitida por el WAF")  # Mensaje de permiso de solicitud
        return True

def block_ip_rule(request):
    blocked_ips = ["192.168.0.1"]
    return request["ip"] not in blocked_ips

def sql_injection_rule(request):
    if any(keyword in request["query"].lower() for keyword in ["select", "drop", "insert", "delete"]):
        return False
    return True

def xss_rule(request):
    if "<script>" in request["content"].lower():
        return False
    return True

class Server:
    def __init__(self, name):
        self.name = name  # Nombre del servidor

    def handle_request(self, request, waf):
        if waf.apply_rules(request):
            print(f"Servidor {self.name} manejando solicitud: {request}")  # Mensaje de manejo de solicitud
        else:
            print(f"Servidor {self.name} bloqueó la solicitud: {request}")  # Mensaje de solicitud bloqueada

class LoadBalancer:
    def __init__(self):
        self.servers = []  # Lista de servidores gestionados por el balanceador de carga

    def add_server(self, server):
        self.servers.append(server)  # Añade un servidor al balanceador de carga
        print(f"Servidor {server.name} añadido al balanceador de carga.")

    def distribute_requests(self, requests, waf):
        print("Distribuyendo solicitudes...")
        for i, request in enumerate(requests):
            server = self.servers[i % len(self.servers)]
            server.handle_request(request, waf)

# Ejemplo de uso
waf = WebApplicationFirewall()
waf.add_rule(block_ip_rule)
waf.add_rule(sql_injection_rule)
waf.add_rule(xss_rule)

server1 = Server("Servidor 1")
server2 = Server("Servidor 2")

load_balancer = LoadBalancer()
load_balancer.add_server(server1)
load_balancer.add_server(server2)

requests = [
    {"ip": "192.168.0.2", "query": "SELECT * FROM users", "content": "Hello World"},
    {"ip": "192.168.0.1", "query": "DROP TABLE users", "content": "Hello World"},
    {"ip": "192.168.0.3", "query": "INSERT INTO users VALUES ('admin', '123')", "content": "<script>alert('XSS')</script>"},
    {"ip": "192.168.0.4", "query": "UPDATE users SET password='1234'", "content": "Normal content"}
]

load_balancer.distribute_requests(requests, waf)
