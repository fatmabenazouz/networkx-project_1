import networkx as nx
import matplotlib.pyplot as plt

# Your Excel data
data = [
    {"placetype_mod": "Prison", "location": 1},
    {"placetype_mod": "Overlap", "location": 7},
    {"placetype_mod": "Overlap", "location": 11},
    {"placetype_mod": "Overlap", "location": 13},
    {"placetype_mod": "Clinic", "location": 14},
    {"placetype_mod": "Overlap", "location": 15},
    {"placetype_mod": "Overlap", "location": 17},
    {"placetype_mod": "Bar", "location": 18},
    {"placetype_mod": "Overlap", "location": 19},
    {"placetype_mod": "Overlap", "location": 20},
    {"placetype_mod": "Overlap", "location": 21},
    {"placetype_mod": "Church", "location": 22},
    {"placetype_mod": "Overlap", "location": 22},
    {"placetype_mod": "Church", "location": 23},
    {"placetype_mod": "Hospital", "location": 24},
    {"placetype_mod": "Overlap", "location": 26},
    {"placetype_mod": "Bar", "location": 27},
    {"placetype_mod": "Overlap", "location": 28},
    {"placetype_mod": "Overlap", "location": 29},
    {"placetype_mod": "Overlap", "location": 30},
    {"placetype_mod": "Overlap", "location": 31},
    {"placetype_mod": "Overlap", "location": 32},
    {"placetype_mod": "Overlap", "location": 33},
    {"placetype_mod": "Shop", "location": 34},
    {"placetype_mod": "Overlap", "location": 35},
    {"placetype_mod": "Work", "location": 36},
    {"placetype_mod": "Overlap", "location": 38},
    {"placetype_mod": "Overlap", "location": 39},
    {"placetype_mod": "Other", "location": 40},
    {"placetype_mod": "Overlap", "location": 40},
    {"placetype_mod": "Other", "location": 41},
    {"placetype_mod": "Overlap", "location": 42},
    {"placetype_mod": "Clinic", "location": 45},
    {"placetype_mod": "Other", "location": 57},
    {"placetype_mod": "Other", "location": 58},
    {"placetype_mod": "Overlap", "location": 59},
    {"placetype_mod": "Overlap", "location": 61},
    {"placetype_mod": "Overlap", "location": 62},
    {"placetype_mod": "Bar", "location": 63},
    {"placetype_mod": "Bar", "location": 64},
    {"placetype_mod": "Overlap", "location": 65},
    {"placetype_mod": "Work", "location": 66},
]

# Create a directed graph
G = nx.DiGraph()

# Add nodes with color attributes based on location type
for entry in data:
    location = entry["location"]
    placetype_mod = entry["placetype_mod"]
    G.add_node(location, placetype_mod=placetype_mod)

# Create a color map based on location types
color_map = {
    "Prison": "red",
    "Overlap": "blue",
    "Clinic": "green",
    "Bar": "purple",
    "Church": "yellow",
    "Hospital": "orange",
    "Shop": "cyan",
    "Work": "brown",
    "Other": "gray",
}

# Extract colors from the color map based on the placetype_mod attribute
node_colors = [color_map[G.nodes[node]["placetype_mod"]] for node in G.nodes]

# Draw the graph with color-coded nodes
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=800, font_size=8, font_color="white")

# Show the plot
plt.show()