import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Provide the absolute or relative path to your Excel file
file_path = '/Users/fatmabenazouz/Downloads/snmetric_matrix_nw_group2_24jan2024.xls'
df = pd.read_excel(file_path)

# Create a graph
G = nx.Graph()

# Iterate through the rows of the DataFrame
for i, row in df.iterrows():
    # Check if the row contains 'net-' in the first cell
    if 'net-' in row.iloc[0]:
        # Add node to the graph
        G.add_node(row.iloc[0])

        # Iterate through the remaining cells to add edges
        for j in range(1, len(row)):
            # Check if the common cell contains 1
            if row.iloc[j] == 1:
                # Add an edge between the nodes
                G.add_edge(row.iloc[0], df.columns[j])

# Draw the graph
pos = nx.spring_layout(G)  # You can choose a different layout if needed
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1000, node_color='skyblue', font_size=8, font_color='black', edge_color='gray')

print("Nodes:", G.nodes())
print("Edges:", G.edges())

plt.show()