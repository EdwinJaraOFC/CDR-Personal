import networkx as nx
import matplotlib.pyplot as plt
import random

class Network:
    def __init__(self):
        self.graph = nx.Graph()
        self.groups = {}

    def add_node(self, node):
        self.graph.add_node(node)
        print(f"Nodo {node} añadido a la red")

    def add_edge(self, node1, node2):
        self.graph.add_edge(node1, node2)
        print(f"Conexión añadida entre {node1} y {node2}")

    def create_group(self, group_name, members):
        self.groups[group_name] = members
        member_names = ", ".join(members)
        print(f"Grupo {group_name} creado con los miembros: {member_names}")

    def unicast(self, sender, receiver, message):
        if receiver in self.graph:
            print(f"Unicast desde {sender} a {receiver}: {message}")
        else:
            print(f"El nodo {receiver} no existe en la red")

    def broadcast(self, sender, message):
        print(f"Broadcast desde {sender}: {message}")
        for node in self.graph.nodes:
            if node != sender:
                print(f"Nodo {node} recibió el mensaje: {message}")

    def multicast(self, sender, group_name, message):
        if group_name in self.groups:
            print(f"Multicast desde {sender} al grupo {group_name}: {message}")
            for node in self.groups[group_name]:
                print(f"Nodo {node} recibió el mensaje: {message}")
        else:
            print(f"Grupo {group_name} no existe")

    def anycast(self, sender, message):
        receiver = random.choice(list(self.graph.nodes))
        print(f"Anycast desde {sender} a {receiver}: {message}")
        print(f"Nodo {receiver} recibió el mensaje: {message}")

    def draw_graph(self):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_weight='bold', edge_color='black', linewidths=1, arrows=True)
        nx.draw_networkx_edge_labels(self.graph, pos)
        plt.title("Diagrama de Red")
        plt.show()

# Ejemplo de uso
network = Network()

# Crear nodos
network.add_node("Nodo 1")
network.add_node("Nodo 2")
network.add_node("Nodo 3")
network.add_node("Nodo 4")

# Crear conexiones entre nodos
network.add_edge("Nodo 1", "Nodo 2")
network.add_edge("Nodo 1", "Nodo 3")
network.add_edge("Nodo 2", "Nodo 3")
network.add_edge("Nodo 3", "Nodo 4")

# Crear grupo de multicast
network.create_group("Grupo 1", ["Nodo 2", "Nodo 3"])

# Enviar mensajes utilizando diferentes tipos de comunicación
network.unicast("Nodo 1", "Nodo 2", "Hola Nodo 2")
print("-" * 40)
network.broadcast("Nodo 1", "Hola a todos")
print("-" * 40)
network.multicast("Nodo 1", "Grupo 1", "Hola Grupo 1")
print("-" * 40)
network.anycast("Nodo 1", "Hola nodo cualquiera")

# Dibujar el grafo de la red
network.draw_graph()
