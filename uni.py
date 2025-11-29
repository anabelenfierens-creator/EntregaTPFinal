import matplotlib.pyplot as plt
import networkx as nx

# Crear un grafo dirigido para el diagrama PERT
G = nx.DiGraph()

# Nodos con etiquetas
nodes = {
    "A": "A\nPlanificación\n(7 días)",
    "B": "B\nLugar del Evento\n(8 días)",
    "C": "C\nDecoración\n(15 días)",
    "D": "D\nCatering\n(15 días)",
    "Start": "Inicio",
    "End": "Fin"
}

# Agregar nodos
for node, label in nodes.items():
    G.add_node(node, label=label)

# Agregar relaciones (aristas)
edges = [
    ("Start", "A"),
    ("A", "B"),
    ("B", "C"),
    ("B", "D"),
    ("C", "End"),
    ("D", "End")
]
G.add_edges_from(edges)

# Posiciones manuales para mejor visualización
pos = {
    "Start": (0, 2),
    "A": (1, 2),
    "B": (2, 2),
    "C": (3, 3),
    "D": (3, 1),
    "End": (4, 2)
}

# Dibujar nodos
plt.figure(figsize=(10, 6))
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color="#AED6F1")
nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle='-|>', arrowsize=20, edge_color='gray')
nx.draw_networkx_labels(G, pos, labels=nx.get_node_attributes(G, 'label'), font_size=9)

plt.title("Diagrama PERT - Organización Fiesta de 15", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()
