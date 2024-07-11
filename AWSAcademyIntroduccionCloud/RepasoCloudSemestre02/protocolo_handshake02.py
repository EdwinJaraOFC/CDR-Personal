import random
import time

# Definición de la clase Servidor
class Servidor:
    def __init__(self):
        self.estado = "LISTENING"

    def recibir_syn(self):
        if random.choice([True, False]):  # Simulación de pérdida de paquetes
            print("Servidor: Paquete SYN recibido.")
            self.estado = "SYN_RECEIVED"
            return True
        else:
            print("Servidor: Paquete SYN perdido.")
            return False

    def enviar_syn_ack(self):
        if random.choice([True, False]):  # Simulación de pérdida de paquetes
            print("Servidor: Enviando SYN-ACK.")
            return True
        else:
            print("Servidor: Paquete SYN-ACK perdido.")
            return False

    def recibir_ack(self):
        if random.choice([True, False]):  # Simulación de pérdida de paquetes
            print("Servidor: Paquete ACK recibido.")
            self.estado = "ESTABLISHED"
            return True
        else:
            print("Servidor: Paquete ACK perdido.")
            return False

# Definición de la clase Cliente
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = "CLOSED"

    def enviar_syn(self, servidor):
        print(f"{self.nombre}: Enviando SYN.")
        if servidor.recibir_syn():
            self.estado = "SYN_SENT"
            return True
        else:
            print(f"{self.nombre}: Reintentando enviar SYN.")
            return False

    def recibir_syn_ack(self, servidor):
        print(f"{self.nombre}: Esperando SYN-ACK.")
        if servidor.enviar_syn_ack():
            print(f"{self.nombre}: Paquete SYN-ACK recibido.")
            self.estado = "SYN_RECEIVED"
            return True
        else:
            print(f"{self.nombre}: SYN-ACK no recibido. Reintentando o esperando.")
            return False

    def enviar_ack(self, servidor):
        print(f"{self.nombre}: Enviando ACK.")
        if servidor.recibir_ack():
            self.estado = "ESTABLISHED"
            print(f"{self.nombre}: Conexión establecida.")
            return True
        else:
            print(f"{self.nombre}: Reintentando enviar ACK.")
            return False

# Función para simular el proceso de three-way handshake con múltiples clientes
def three_way_handshake_multi(clientes, servidor):
    for cliente in clientes:
        while not cliente.enviar_syn(servidor):
            time.sleep(1)

        while not cliente.recibir_syn_ack(servidor):
            time.sleep(1)

        while not cliente.enviar_ack(servidor):
            time.sleep(1)
        print()  # Separador entre clientes

# Crear instancias de Cliente y Servidor
num_clientes = 3
clientes = [Cliente(f"Cliente-{i+1}") for i in range(num_clientes)]
servidor = Servidor()

# Simular el three-way handshake con múltiples clientes
three_way_handshake_multi(clientes, servidor)
