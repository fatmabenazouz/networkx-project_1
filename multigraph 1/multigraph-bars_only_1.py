import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os

# Data
data_path = os.path.expanduser("~/Downloads/edgelist_bars_only_29Jan2024.xls")

# Step 2: Create a DataFrame from the Excel file
df = pd.read_excel("~/Downloads/edgelist_bars_only_29Jan2024.xls")

# Step 3: Create a NetworkX graph
G = nx.Graph()

# Step 4: Add nodes and edges to the graph
for _, row in df.iterrows():
    G.add_edge(row['studyid'], row['bar'])

# Step 5: Visualize the graph
pos = nx.spring_layout(G, k=0.50, iterations=50)  # You can use different layout algorithms
nx.draw(G, pos, with_labels=True, font_size=8, node_size=300, node_color="skyblue", font_color="black", font_weight="bold")
plt.show()

