import networkx as nx
import matplotlib.pyplot as plt
import xlrd
import os

file = os.path.expanduser("~/Downloads/snmetric_matrix_NW_group2.xls")

G = nx.Graph()
names = []

book = xlrd.open_workbook(file)
sheet = book.sheet_by_index(0)

for row in range(sheet.nrows):
    data = sheet.row_slice(row)
    studyid = data[0].value
    node1 = data[1].value
    node3 = data[2].value
    names.append((studyid, node1))

G.add_edges_from(names)

# Specify layout
pos = nx.kamada_kawai_layout(G)

# Adjust figure size
plt.figure(figsize=(10, 8))

# Draw the graph
nx.draw(G, pos, with_labels=True, font_size=8, node_size=100, node_color="skyblue", edge_color="gray", font_color="black")

plt.show()