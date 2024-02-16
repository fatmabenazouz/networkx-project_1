import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# reading the new excel file
df = pd.read_excel('~/Downloads/NW-edge_list_output.xlsx')

G = nx.Graph()

# nodes
G.add_nodes_from(df['Node 1'])
G.add_nodes_from(df['Node 2'])

# defining colours for different locations
location_colors = {
    'Church': 'blue',
    'Current Home': 'green',
    'Friend': 'orange',
    'Family': 'purple',
    'Other': 'red',
    'Work': 'yellow',
    'Bar': 'gray',
    'Barber': 'brown',
    'Hostel': 'cyan',
    'Previous Home': 'magenta'
}

# edges with colour attribute
for _, row in df.iterrows():
    if pd.notnull(row['Node 2']):
        location1 = row['Location'].split()[0]  # location from string (e.g., 'Church46' -> 'Church')
        location2 = row['Location'].split()[0] if row['Node 2'] != '' else None
        color = 'black'  # default colour if location not found
        for location, col in location_colors.items():
            if location in location1 or (location2 and location in location2):
                color = col
                break
        G.add_edge(row['Node 1'], row['Node 2'], color=color)

# plotting the graph
pos = nx.spring_layout(G, k=0.50, iterations=50, seed=42)  # positions for all nodes
node_colors = ['skyblue'] * len(G.nodes())
node_size = 250
edge_colors = [G[u][v]['color'] for u, v in G.edges()]
nx.draw(G, pos, with_labels=False, node_color=node_colors, node_size=node_size, edge_color=edge_colors)

plt.show()