import networkx as nx
import matplotlib.pyplot as plt
import xlrd
import os

file = '/Users/fatmabenazouz/Downloads/snmetric_edgelist_group2_NW_labels.xls'

G = nx.Graph()
names = []

book = xlrd.open_workbook(file)
sheet = book.sheet_by_index(0)

for row in range(sheet.nrows):
    data = sheet.row_slice(row)
    placetype = data[0].value
    location = data[1].value
    names.append((placetype, location))

G.add_edges_from(names)

# Specify layout
pos = nx.kamada_kawai_layout(G)

# Adjust figure size
plt.figure(figsize=(10, 8))

# Draw the graph
nx.draw(G, pos, with_labels=True, font_size=8, node_size=100, node_color="skyblue", edge_color="gray", font_color="black")

plt.show()