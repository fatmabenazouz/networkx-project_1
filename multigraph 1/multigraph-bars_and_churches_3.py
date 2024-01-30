import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Complete dataset
data = [
    ("1-2-0011-01", "Bar", "Bar17"),
    ("1-2-0011-01", "Bar", "Bar21"),
    ("1-2-0011-01", "Church", "Church8"),
    ("1-2-0013-01", "Bar", "Bar25"),
    ("1-2-0013-01", "Bar", "Bar26"),
    ("1-2-0013-01", "Bar", "Bar30"),
    ("1-2-0013-01", "Bar", "Bar30"),
    ("1-2-0017-01", "Bar", "Bar27"),
    ("1-2-0027-01", "Bar", "Bar16"),
    ("1-2-0027-01", "Bar", "Bar19"),
    ("1-2-0029-01", "Bar", "Bar55"),
    ("1-2-0029-01", "Bar", "Bar56"),
    ("1-2-0029-01", "Church", "Church26"),
    ("1-2-0031-01", "Church", "Church14"),
    ("1-2-0031-01", "Church", "Church7"),
    ("1-2-0034-01", "Bar", "Bar18"),
    ("1-2-0038-01", "Bar", "Bar31"),
    ("1-2-0038-01", "Church", "Church19"),
    ("1-2-0060-01", "Church", "Church10"),
    ("1-2-0060-01", "Church", "Church11"),
    ("1-2-0061-01", "Bar", "Bar35"),
    ("1-2-0064-01", "Bar", "Bar52"),
    ("1-2-0064-01", "Bar", "Bar54"),
    ("1-2-0070-01", "Church", "Church12"),
    ("1-2-0074-01", "Bar", "Bar29"),
    ("1-2-0074-01", "Bar", "Bar29"),
    ("1-2-0074-01", "Church", "Church17"),
    ("1-2-0086-01", "Church", "Church6"),
    ("1-2-0088-01", "Bar", "Bar60"),
    ("1-2-0088-01", "Church", "Church28"),
    ("1-2-0095-01", "Church", "Church15"),
    ("1-2-0097-01", "Bar", "Bar20"),
    ("1-2-0097-01", "Church", "Church13"),
    ("1-2-0100-01", "Bar", "Bar22"),
    ("1-2-0100-01", "Bar", "Bar23"),
    ("1-2-0102-01", "Church", "Church9"),
    ("1-2-0103-01", "Church", "Church1"),
    ("1-2-0107-01", "Bar", "Bar50"),
    ("1-2-0107-01", "Bar", "Bar54"),
    ("1-2-0116-01", "Bar", "Bar63"),
    ("1-2-0119-01", "Church", "Church16"),
    ("1-2-0128-01", "Bar", "Bar61"),
    ("1-2-0135-01", "Bar", "Bar37"),
    ("1-2-0136-01", "Bar", "Bar62"),
    ("1-2-0138-01", "Bar", "Bar57"),
    ("1-2-0138-01", "Church", "Church27"),
    ("1-2-0139-01", "Bar", "Bar47"),
    ("1-2-0139-01", "Bar", "Bar48"),
    ("1-2-0139-01", "Bar", "Bar49"),
    ("1-2-0139-01", "Bar", "Bar49"),
    ("1-2-0139-01", "Church", "Church29"),
    ("1-2-0140-01", "Bar", "Bar58"),
    ("1-2-0140-01", "Bar", "Bar59"),
    ("1-2-0148-01", "Bar", "Bar15"),
    ("1-2-0149-01", "Bar", "Bar2"),
    ("1-2-0152-01", "Bar", "Bar28"),
    ("1-2-0154-01", "Bar", "Bar1"),
    ("1-2-0154-01", "Bar", "Bar3"),
    ("1-2-0163-01", "Bar", "Bar32"),
    ("1-2-0163-01", "Bar", "Bar33"),
    ("1-2-0163-01", "Church", "Church18"),
    ("1-2-0164-01", "Bar", "Bar51"),
    ("1-2-0164-01", "Bar", "Bar52"),
    ("1-2-0164-01", "Bar", "Bar54"),
    ("2-1-1055-01", "Bar", "Bar38"),
    ("2-1-1055-01", "Bar", "Bar44"),
    ("2-1-1055-01", "Church", "Church23"),
    ("2-2-1004-01", "Church", "Church22"),
    ("2-2-1033-01", "Bar", "Bar46"),
    ("2-2-1071-01", "Church", "Church24"),
    ("2-2-1096-01", "Church", "Church3"),
    ("2-2-1108-01", "Bar", "Bar39"),
    ("2-2-1108-01", "Bar", "Bar40"),
    ("2-2-1108-01", "Church", "Church20"),
    ("2-2-1112-01", "Bar", "Bar38"),
    ("2-2-1121-01", "Bar", "Bar8"),
    ("2-2-1129-01", "Church", "Church5"),
    ("2-2-1134-01", "Bar", "Bar12"),
    ("2-2-1149-01", "Bar", "Bar34"),
    ("2-2-1149-01", "Bar", "Bar36"),
    ("2-2-1155-01", "Bar", "Bar9"),
    ("2-2-1155-01", "Church", "Church2"),
    ("2-2-1156-01", "Bar", "Bar53"),
    ("2-2-1157-01", "Bar", "Bar44"),
    ("2-2-1157-01", "Bar", "Bar45"),
    ("2-2-1158-01", "Bar", "Bar42"),
    ("2-2-1158-01", "Bar", "Bar43"),
    ("2-2-1160-01", "Church", "Church21"),
    ("2-2-1171-01", "Church", "Church4"),
    ("2-2-1174-01", "Bar", "Bar10"),
    ("2-2-1174-01", "Bar", "Bar11"),
    ("2-2-1184-01", "Bar", "Bar41"),
    ("2-2-1185-01", "Bar", "Bar5"),
    ("2-2-1185-01", "Bar", "Bar6"),
    ("2-2-1186-01", "Church", "Church3"),
    ("2-2-1187-01", "Bar", "Bar14"),
    ("2-2-1188-01", "Bar", "Bar13"),
    ("2-2-1191-01", "Bar", "Bar7"),
    ("2-2-1192-01", "Church", "Church25"),
    ("3-2-3007-01", "Bar", "Bar4"),
    ("3-2-3009-01", "Bar", "Bar24")
]

# Create a directed multigraph
G = nx.MultiDiGraph()

# Add nodes and edges
for studyid, placetype, placename in data:
    G.add_node(studyid)
    G.add_edge(studyid, placename, placetype=placetype)

# Create color mapping for edges based on Placetypes
placetype_color_mapping = {'Bar': 0, 'Church': 1}  # Assign a numerical value to each Placetype
edge_colors = [
    placetype_color_mapping.get(G[studyid][placename][0].get("placetype", ""), 0)
    if G[studyid][placename] else 0
    for studyid, placename in G.edges()
]

# Draw the graph
pos = nx.spring_layout(G, k=0.50, iterations=50)
nx.draw_networkx_nodes(G, pos, node_color="skyblue", node_size=200)
nx.draw_networkx_labels(G, pos, font_size='9')
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2, alpha=0.6, edge_cmap=plt.cm.Reds)

# Create a legend for edge colors
legend_labels = {0: "Bar", 1: "Church"}  # Update based on your Placetypes
plt.legend(legend_labels.values(), loc="best")

# Draw edge labels manually
for studyid, placename, placetype in G.edges(data="placetype"):
    if placetype:
        edge_label = f"{studyid}: {placetype[0]}"

plt.title("NetworkX Visualization")
plt.show()