import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Read the Excel file into a DataFrame
df = pd.read_excel('~/Downloads/snmetric_matrix_NW_group2.xls')

# Set "studyid" as the index and convert the index to strings
df.set_index("studyid", inplace=True)
df.index = df.index.astype(str)

# Create a directed graph from the DataFrame
G = nx.from_pandas_adjacency(df, create_using=nx.DiGraph)

# Plot the graph
pos = nx.spring_layout(G)  # You can use other layout algorithms as well
nx.draw(G, pos, with_labels=True, node_size=700, font_size=8, font_color="black", font_weight="bold", node_color="skyblue", edge_color="gray", linewidths=0.5)

# Show the plot
plt.show()