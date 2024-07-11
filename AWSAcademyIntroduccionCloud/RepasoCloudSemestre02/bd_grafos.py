import networkx as nx
import matplotlib.pyplot as plt

class SimuladorNeptune:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node, **kwargs):
        self.graph.add_node(node, **kwargs)
        print(f"Añadido nodo: {node}")

    def add_edge(self, node1, node2, **kwargs):
        self.graph.add_edge(node1, node2, **kwargs)
        print(f"Añadida arista entre {node1} y {node2}")

    def get_node_attributes(self, node):
        attrs = self.graph.nodes[node]
        print(f"Atributos de nodo {node}: {attrs}")

    def get_edge_attributes(self, node1, node2):
        attrs = self.graph.edges[node1, node2]
        print(f"Atributos de arista entre {node1} y {node2}: {attrs}")

    def list_nodes(self):
        nodes = list(self.graph.nodes)
        print("Nodos:", nodes)

    def list_edges(self):
        edges = list(self.graph.edges)
        print("Aristas:", edges)

    def plot_graph(self):
        pos = nx.spring_layout(self.graph)  # Layout para posicionar los nodos
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='grey', font_size=10, font_weight='bold')
        plt.title("Simulación de Amazon Neptune")
        plt.show()

# Creación del simulador y operaciones en el grafo
simulador = SimuladorNeptune()

# Añadir nodos
simulador.add_node("Alice", role="Person", age=30)
simulador.add_node("Bob", role="Person", age=28)
simulador.add_node("Charlie", role="Person", age=35)
simulador.add_node("Eve", role="Person", age=25)

# Añadir aristas
simulador.add_edge("Alice", "Bob", relation="Friend")
simulador.add_edge("Bob", "Charlie", relation="Colleague")
simulador.add_edge("Charlie", "Eve", relation="Friend")
simulador.add_edge("Eve", "Alice", relation="Family")

# Consultas en el grafo
simulador.list_nodes()
simulador.list_edges()
simulador.get_node_attributes("Alice")
simulador.get_edge_attributes("Alice", "Bob")

# Graficar el grafo
simulador.plot_graph()
