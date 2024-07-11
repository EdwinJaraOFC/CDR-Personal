import random

class Node:
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print(f"Nodo {self.name} recibió el mensaje: {message}")

class Network:
    def __init__(self):
        self.nodes = []
        self.groups = {}

    def add_node(self, node):
        self.nodes.append(node)
        print(f"Nodo {node.name} añadido a la red")

    def create_group(self, group_name, members):
        self.groups[group_name] = members
        member_names = ", ".join(member.name for member in members)
        print(f"Grupo {group_name} creado con los miembros: {member_names}")

    def unicast(self, sender, receiver, message):
        print(f"Unicast desde {sender.name} a {receiver.name}: {message}")
        receiver.receive(message)

    def broadcast(self, sender, message):
        print(f"Broadcast desde {sender.name}: {message}")
        for node in self.nodes:
            if node != sender:
                node.receive(message)

    def multicast(self, sender, group_name, message):
        if group_name in self.groups:
            print(f"Multicast desde {sender.name} al grupo {group_name}: {message}")
            for node in self.groups[group_name]:
                node.receive(message)
        else:
            print(f"Grupo {group_name} no existe")

    def anycast(self, sender, message):
        receiver = random.choice(self.nodes)
        print(f"Anycast desde {sender.name} a {receiver.name}: {message}")
        receiver.receive(message)

# Ejemplo de uso
network = Network()

# Crear nodos
node1 = Node("Nodo 1")
node2 = Node("Nodo 2")
node3 = Node("Nodo 3")
node4 = Node("Nodo 4")

# Añadir nodos a la red
network.add_node(node1)
network.add_node(node2)
network.add_node(node3)
network.add_node(node4)

# Crear grupo de multicast
network.create_group("Grupo 1", [node2, node3])

# Enviar mensajes utilizando diferentes tipos de comunicación
network.unicast(node1, node2, "Hola Nodo 2")
print("-" * 40)
network.broadcast(node1, "Hola a todos")
print("-" * 40)
network.multicast(node1, "Grupo 1", "Hola Grupo 1")
print("-" * 40)
network.anycast(node1, "Hola nodo cualquiera")
