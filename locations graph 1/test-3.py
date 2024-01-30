import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()