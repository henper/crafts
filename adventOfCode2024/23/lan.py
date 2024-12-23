import networkx as nx
from itertools import combinations

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

from input import computers

G = nx.Graph()

G.add_edges_from(computers)

lan_party = [1,2,3] # we know the largest lan party is longer than 3
for node in G.nodes:

    neighbors = set(G.adj[node].keys())

    neighbors_neighbors = [ [neighbor] + list(G.adj[neighbor].keys()) for neighbor in neighbors ]

    largest_lan = len(lan_party)
    for i in range(largest_lan, len(neighbors)+1):

        combos = combinations(neighbors_neighbors, i)

        for combo in combos:

            lan = set([node] + [nodes[0] for nodes in combo])

            is_lan_party = True
            for node_list in combo:

                if not lan.issubset(node_list):
                    is_lan_party = False
                    break
            
            if not is_lan_party:
                continue

            if len(lan) >= largest_lan:
                lan_party = lan

party = list(lan_party)
party.sort()

print(','.join(party))

# 2226 Too high