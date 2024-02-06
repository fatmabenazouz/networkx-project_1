import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Read data from Excel file
excel_file = "~/Downloads/updated-church_edgelist_02feb2024.xlsx"
df = pd.read_excel(excel_file)

# replacing "nan" values in Node 2 column with an empty string
df['Node 2'] = df['Node 2'].fillna("")

# creating a graph
G = nx.Graph()

# adding nodes and edges to the graph with weights
for index, row in df.iterrows():
    node1 = row['Node 1']
    node2 = row['Node 2']
    church = row['Church']
    weight = row['Edge'] if not pd.isna(row['Edge']) else None  # setting weight to None if Edge is NaN

    G.add_node(node1)  # add the node even if it doesn't connect to any other node

    
    if node2:
        G.add_edge(node1, node2, weight=weight)

# layout for nodes 
pos = nx.spring_layout(G, k=0.50, iterations=10)

# drawing the graph
nx.draw(G, pos, with_labels=False, font_weight='bold', node_size=200, node_color='lightgreen', font_size=8)

plt.show()