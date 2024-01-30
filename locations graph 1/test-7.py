import networkx as nx
import matplotlib.pyplot as plt

# Create a graph object
G = nx.Graph()

# Add nodes to the graph
nodes = ['net' + str(i) for i in range(1, 73)]
G.add_nodes_from(nodes)

# Add edges to the graph
edges = [('net1', 'net24'), ('net1', 'net27'), ('net1', 'net28'), ('net1', 'net30'), ('net1', 'net32'), ('net1', 'net34'), ('net1', 'net42'), ('net1', 'net56'), ('net2', 'net16'), ('net2', 'net17'), ('net2', 'net18'), ('net2', 'net19'), ('net2', 'net45'), ('net3', 'net26'), ('net3', 'net28'), ('net3', 'net31'), ('net3', 'net33'), ('net3', 'net34'), ('net3', 'net36'), ('net3', 'net37'), ('net3', 'net38'), ('net3', 'net39'), ('net3', 'net40'), ('net3', 'net41'), ('net3', 'net43'), ('net3', 'net44'), ('net4', 'net26'), ('net4', 'net28'), ('net4', 'net31'), ('net4', 'net33'), ('net4', 'net34'), ('net4', 'net36'), ('net4', 'net37'), ('net4', 'net38'), ('net4', 'net39'), ('net4', 'net40'), ('net4', 'net41'), ('net4', 'net43'), ('net4', 'net45'), ('net4', 'net47'), ('net4', 'net50'), ('net4', 'net52'), ('net4', 'net54'), ('net4', 'net57'), ('net5', 'net14'), ('net5', 'net15'), ('net5', 'net16'), ('net5', 'net17'), ('net5', 'net18'), ('net5', 'net19'), ('net5', 'net46'), ('net6', 'net23'), ('net6', 'net25'), ('net6', 'net43'), ('net6', 'net45'), ('net7', 'net15'), ('net7', 'net16'), ('net7', 'net17'), ('net7', 'net19'), ('net7', 'net46'), ('net8', 'net15'), ('net8', 'net16'), ('net8', 'net17'), ('net8', 'net19'), ('net8', 'net46'), ('net9', 'net26'), ('net9', 'net27'), ('net9', 'net30'), ('net9', 'net31'), ('net9', 'net33'), ('net9', 'net34'), ('net9', 'net36'), ('net9', 'net37'), ('net9', 'net38'), ('net9', 'net39'), ('net9', 'net40'), ('net9', 'net41'), ('net9', 'net43'), ('net9', 'net44'), ('net10', 'net17'), ('net10', 'net18'), ('net10', 'net19'), ('net10', 'net46')]

G.add_edges_from(edges)

# Draw the graph
pos = nx.spring_layout(G, k=0.50, iterations=50)
color_map = ['firebrick' for node in G.nodes()]
nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=340, font_color='black', font_size='9', font_weight='bold', edge_color='gray')

# Show the graph
plt.show()