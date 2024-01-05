import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import SpectralClustering

G = nx.Graph()

with open('./adventOfCode2023/25/input.txt', 'r') as apparatus:
    for line in apparatus:
        node, connections = line.split(': ')
        connections = connections.rstrip().split(' ')

        G.add_edges_from([(node, connection) for connection in connections])


nx.draw(G, with_labels=True)
plt.show()

ev = nx.linalg.algebraicconnectivity.fiedler_vector(G)
labels = [0 if v < 0 else 1 for v in ev] # using threshold 0

nx.draw(G, pos=nx.drawing.layout.spring_layout(G),
           with_labels=True, node_color=labels)
plt.show()

print(f'Total nodes: {len(G.nodes())}, nodes in Cluster A: {sum(labels)}, nodes in cluster B: {len(G.nodes()) - sum(labels)}')

