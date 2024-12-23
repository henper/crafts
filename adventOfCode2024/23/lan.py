import networkx as nx
import matplotlib.pyplot as plt

computers = [
    ('kh','tc'),
	('qp','kh'),
	('de','cg'),
	('ka','co'),
	('yn','aq'),
	('qp','ub'),
	('cg','tb'),
	('vc','aq'),
	('tb','ka'),
	('wh','tc'),
	('yn','cg'),
	('kh','ub'),
	('ta','co'),
	('de','co'),
	('tc','td'),
	('tb','wq'),
	('wh','td'),
	('ta','ka'),
	('td','qp'),
	('aq','cg'),
	('wq','ub'),
	('ub','vc'),
	('de','ta'),
	('wq','aq'),
	('wq','vc'),
	('wh','yn'),
	('ka','de'),
	('kh','ta'),
	('co','tc'),
	('wh','qp'),
	('tb','vc'),
	('td','yn'),
]

#from input import computers

G = nx.Graph()

G.add_edges_from(computers)


options = {
    "font_size": 36,
    "node_size": 3000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
    "with_labels": True,
}

nx.draw_networkx(G, **options)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()


threes = []
for node in G.nodes:
    if node[0] != 't':
        continue

    neighbors = set(G.adj[node].keys())

    for neighbor in neighbors:
        once_removed = set(G.adj[neighbor].keys())

        triplets = neighbors.intersection(once_removed)

        for triplet in triplets:


            three = set((node, neighbor, triplet))
            if three not in threes:
                threes.append(three)

print(len(threes))

# 2226 Too high