import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Assuming your dataset is stored in a DataFrame df
data = {
    'studyid': ['1-2-0011-01', '1-2-0011-01', '1-2-0011-01', '1-2-0013-01', '1-2-0013-01', '1-2-0013-01', '1-2-0013-01', '1-2-0017-01',
                '1-2-0027-01', '1-2-0027-01', '1-2-0029-01', '1-2-0029-01', '1-2-0029-01', '1-2-0031-01', '1-2-0031-01', '1-2-0034-01',
                '1-2-0038-01', '1-2-0038-01', '1-2-0060-01', '1-2-0060-01', '1-2-0061-01', '1-2-0064-01', '1-2-0064-01', '1-2-0070-01',
                '1-2-0074-01', '1-2-0074-01', '1-2-0074-01', '1-2-0086-01', '1-2-0088-01', '1-2-0088-01', '1-2-0095-01', '1-2-0097-01',
                '1-2-0097-01', '1-2-0100-01', '1-2-0100-01', '1-2-0102-01', '1-2-0103-01', '1-2-0107-01', '1-2-0107-01', '1-2-0116-01',
                '1-2-0119-01', '1-2-0128-01', '1-2-0135-01', '1-2-0136-01', '1-2-0138-01', '1-2-0138-01', '1-2-0139-01', '1-2-0139-01',
                '1-2-0139-01', '1-2-0139-01', '1-2-0139-01', '1-2-0140-01', '1-2-0140-01', '1-2-0148-01', '1-2-0149-01', '1-2-0152-01',
                '1-2-0154-01', '1-2-0154-01', '1-2-0163-01', '1-2-0163-01', '1-2-0163-01', '1-2-0164-01', '1-2-0164-01', '1-2-0164-01',
                '2-1-1055-01', '2-1-1055-01', '2-1-1055-01', '2-2-1004-01', '2-2-1033-01', '2-2-1071-01', '2-2-1096-01', '2-2-1108-01',
                '2-2-1108-01', '2-2-1108-01', '2-2-1112-01', '2-2-1121-01', '2-2-1129-01', '2-2-1134-01', '2-2-1149-01', '2-2-1149-01',
                '2-2-1155-01', '2-2-1155-01', '2-2-1156-01', '2-2-1157-01', '2-2-1157-01', '2-2-1158-01', '2-2-1158-01', '2-2-1160-01',
                '2-2-1171-01', '2-2-1174-01', '2-2-1174-01', '2-2-1184-01', '2-2-1185-01', '2-2-1185-01', '2-2-1186-01', '2-2-1187-01',
                '2-2-1188-01', '2-2-1191-01', '2-2-1192-01', '3-2-3007-01', '3-2-3009-01'],
    'placetype': ['Bar', 'Bar', 'Church', 'Bar', 'Bar', 'Bar', 'Bar', 'Bar', 'Bar', 'Bar', 'Bar', 'Bar', 'Church', 'Church', 'Bar',
                  'Bar', 'Church', 'Bar', 'Bar', 'Church', 'Church', 'Bar', 'Bar', 'Bar', 'Church', 'Bar', 'Bar', 'Bar', 'Church',
                  'Church', 'Church', 'Bar', 'Church', 'Bar', 'Church', 'Bar', 'Bar', 'Bar', 'Bar', 'Church', 'Bar', 'Bar', 'Bar',
                  'Bar', 'Church', 'Bar', 'Bar', 'Bar', 'Bar', 'Bar', 'Bar', 'Church', 'Bar', 'Bar', 'Bar', 'Bar', 'Bar', 'Church',
                  'Bar', 'Bar', 'Bar', 'Bar', 'Bar', 'Church', 'Bar', 'Bar', 'Bar', 'Church', 'Church', 'Bar', 'Bar', 'Church', 'Bar',
                  'Bar', 'Bar', 'Church', 'Church', 'Bar', 'Bar', 'Bar', 'Bar', 'Bar', 'Bar', 'Bar', 'Church', 'Church', 'Bar', 'Bar',
                  'Bar', 'Bar', 'Bar', 'Bar', 'Bar', 'Church', 'Bar', 'Bar', 'Bar', 'Bar', 'Church', 'Bar', 'Bar'],
    'placename': ['Bar17', 'Bar21', 'Church8', 'Bar25', 'Bar26', 'Bar30', 'Bar30', 'Bar27', 'Bar16', 'Bar19', 'Bar55', 'Bar56', 'Church26',
                  'Church14', 'Church7', 'Bar18', 'Bar31', 'Church19', 'Church10', 'Church11', 'Bar35', 'Bar52', 'Bar54', 'Church12',
                  'Bar29', 'Bar29',  'Church17', 'Church6', 'Bar60', 'Church28', 'Church15', 'Bar20', 'Church13', 'Bar22', 'Bar23', 'Church9', 'Church1',
                  'Bar50', 'Bar54', 'Bar63', 'Church16', 'Bar61', 'Bar37', 'Bar62', 'Bar57', 'Church27', 'Bar47', 'Bar48', 'Bar49',
                  'Bar49', 'Church29', 'Bar58', 'Bar59', 'Bar15', 'Bar2', 'Bar28', 'Bar1', 'Bar3', 'Bar32', 'Bar33', 'Church18',
                  'Bar51', 'Bar52', 'Bar54', 'Bar38', 'Bar44', 'Church23', 'Church22', 'Bar46', 'Church24', 'Church3', 'Bar39', 'Bar40',
                  'Church20', 'Bar38', 'Bar8', 'Church5', 'Bar12', 'Bar34', 'Bar36', 'Bar9', 'Church2', 'Bar53', 'Bar44', 'Bar45',
                  'Bar42', 'Bar43', 'Church21', 'Church4', 'Bar10', 'Bar11', 'Bar41', 'Bar5', 'Bar6', 'Church3', 'Bar14', 'Bar13',
                  'Bar7', 'Church25', 'Bar4', 'Bar24']
}

df = pd.DataFrame(data)

# Create a multigraph
G = nx.MultiGraph()

# Add nodes and edges to the graph
for index, row in df.iterrows():
    G.add_edge(row['studyid'], row['placename'], placetype=row['placetype'])

# Prepare a color map for nodes based on placetype
node_colors = {'Bar': 'blue', 'Church': 'green'}
colors = [node_colors.get(G.nodes[node].get('placetype', ''), 'skyblue') for node in G.nodes]

# Draw the graph with color-coded nodes
pos = nx.spring_layout(G, k=0.50, iterations=50)  # You can use different layouts as per your preference
nx.draw(G, pos, with_labels=True, edge_color='gray', node_color=colors, font_size=8, font_color='black', font_weight='bold', node_size=300)

# Display the graph
plt.show()
