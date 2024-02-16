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
    color = 'red' if 'Bar' in row['Location'] else 'green'
    G.add_edge(row['Node 1'], row['Node 2'], color=color)

# plotting the graph
pos = nx.spring_layout(G)  # positions for all nodes
edge_colors = [G[u][v]['color'] for u, v in G.edges()]
nx.draw(G, pos, with_labels=False, edge_color=edge_colors)
edge_labels = nx.get_edge_attributes(G, 'color')

# Show the plot
plt.show()