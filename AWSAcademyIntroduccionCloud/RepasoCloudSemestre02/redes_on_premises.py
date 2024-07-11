"""
Introducción a las Redes On-Premises y Corporativas Básicas

Simula la topología de una red y la comunicación entre dispositivos utilizando 
Python y librerías como networkx para modelar y visualizar las redes.
"""

import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo vacío
G = nx.Graph()

# Añadir nodos (dispositivos)
G.add_node("Router")
G.add_node("Switch 1")
G.add_node("Switch 2")
G.add_node("PC 1")
G.add_node("PC 2")
G.add_node("PC 3")
G.add_node("PC 4")

# Añadir enlaces (conexiones)
G.add_edges_from([("Router", "Switch 1"), ("Router", "Switch 2"), ("Switch 1", "PC 1"), ("Switch 1", "PC 2"),  ("Switch 2", "PC 3"), ("Switch 2", "PC 4")])

# Dibujar el grafo
nx.draw(G, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_color='black')
plt.show()