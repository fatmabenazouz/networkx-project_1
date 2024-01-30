import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load data into DataFrame (assuming it's stored in a CSV file)
df = pd.read_csv('/Users/fatmabenazouz/Downloads/snmetric_matrix_NW_group2 (1).csv', index_col='studyid')

# Create a graph
G = nx.Graph()

# Add edges to the graph based on DataFrame values
for index, row in df.iterrows():
    for col, value in row.iteritems():
        if value == 1:
            G.add_edge(index, col)

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw(G, with_labels=True)
plt.show()
