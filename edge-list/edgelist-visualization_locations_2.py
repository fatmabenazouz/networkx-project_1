import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# reading the excel file
df = pd.read_excel('~/Downloads/edge_list_output.xlsx')

G = nx.Graph()

# nodes
G.add_nodes_from(df['Node 1'])
G.add_nodes_from(df['Node 2'])

# edges with colour attribute
for _, row in df.iterrows():
    if pd.notnull(row['Node 2']):
        color = 'red' if 'Bar' in row['Location'] else 'green'
        G.add_edge(row['Node 1'], row['Node 2'], color=color)

# plotting the graph
pos = nx.spring_layout(G, k=0.50, iterations=50)  # positions for all nodes
node_colors = ['skyblue'] * len(G.nodes())
node_size = 250
edge_colors = [G[u][v]['color'] for u, v in G.edges()]
nx.draw(G, pos, with_labels=False, node_color=node_colors, node_size=node_size, edge_color=edge_colors)

plt.show()