import pandas as pd

# Given data
data = {
    'studyid': ['1-2-0011-01', '1-2-0011-01', '1-2-0013-01', '1-2-0013-01', '1-2-0013-01', '1-2-0013-01', '1-2-0017-01', '1-2-0027-01', '1-2-0027-01', '1-2-0029-01', '1-2-0029-01', '1-2-0034-01', '1-2-0038-01', '1-2-0061-01', '1-2-0064-01', '1-2-0064-01', '1-2-0074-01', '1-2-0074-01', '1-2-0088-01', '1-2-0097-01', '1-2-0100-01', '1-2-0100-01', '1-2-0107-01', '1-2-0107-01', '1-2-0116-01', '1-2-0128-01', '1-2-0135-01', '1-2-0136-01', '1-2-0138-01', '1-2-0139-01', '1-2-0139-01', '1-2-0139-01', '1-2-0139-01', '1-2-0140-01', '1-2-0140-01', '1-2-0148-01', '1-2-0149-01', '1-2-0152-01', '1-2-0154-01', '1-2-0154-01', '1-2-0163-01', '1-2-0163-01', '1-2-0164-01', '1-2-0164-01', '1-2-0164-01', '2-1-1055-01', '2-1-1055-01', '2-2-1033-01', '2-2-1108-01', '2-2-1108-01', '2-2-1112-01', '2-2-1121-01', '2-2-1134-01', '2-2-1149-01', '2-2-1149-01', '2-2-1155-01', '2-2-1156-01', '2-2-1157-01', '2-2-1157-01', '2-2-1158-01', '2-2-1158-01', '2-2-1174-01', '2-2-1174-01', '2-2-1184-01', '2-2-1185-01', '2-2-1185-01', '2-2-1187-01', '2-2-1188-01', '2-2-1191-01', '3-2-3007-01', '3-2-3009-01'],
    'bar': ['Bar17', 'Bar21', 'Bar25', 'Bar26', 'Bar30', 'Bar30', 'Bar27', 'Bar16', 'Bar19', 'Bar55', 'Bar56', 'Bar18', 'Bar31', 'Bar35', 'Bar52', 'Bar54', 'Bar29', 'Bar29', 'Bar60', 'Bar20', 'Bar22', 'Bar23', 'Bar50', 'Bar54', 'Bar63', 'Bar61', 'Bar37', 'Bar62', 'Bar57', 'Bar47', 'Bar48', 'Bar49', 'Bar49', 'Bar58', 'Bar59', 'Bar15', 'Bar2', 'Bar28', 'Bar1', 'Bar3', 'Bar32', 'Bar33', 'Bar51', 'Bar52', 'Bar54', 'Bar38', 'Bar44', 'Bar46', 'Bar39', 'Bar40', 'Bar38', 'Bar8', 'Bar12', 'Bar34', 'Bar36', 'Bar9', 'Bar53', 'Bar44', 'Bar45', 'Bar42', 'Bar43', 'Bar10', 'Bar11', 'Bar41', 'Bar5', 'Bar6', 'Bar14', 'Bar13', 'Bar7', 'Bar4', 'Bar24']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Sort the DataFrame by 'bar' and 'studyid'
df.sort_values(['bar', 'studyid'], inplace=True)

# Create a dictionary to store the edge list
edge_list = {'Node 1': [], 'Node 2': [], 'Node 3': [], 'Bar': [], 'Edge': []}

# Iterate through unique bars
for bar in df['bar'].unique():
    # Get the Study IDs for the current bar
    study_ids = df[df['bar'] == bar]['studyid'].tolist()

    # Create all possible pairs of Study IDs for the current bar
    pairs = [(study_ids[i], study_ids[j]) for i in range(len(study_ids)) for j in range(i + 1, len(study_ids))]

    # Add data to the edge list
    for pair in pairs:
        edge_list['Node 1'].append(pair[0])
        edge_list['Node 2'].append(pair[1])
        edge_list['Node 3'].append(None)  # Placeholder for Node 3
        edge_list['Bar'].append(bar)
        edge_list['Edge'].append(None)  # Placeholder for Edge

# Assign unique numbers to the 'Node 3' and 'Edge' columns
edge_list_df = pd.DataFrame(edge_list)
edge_list_df['Node 3'] = edge_list_df.groupby(['Node 1', 'Bar'])['Node 3'].transform(lambda x: x.rank())
edge_list_df['Edge'] = edge_list_df.groupby(['Bar'])['Edge'].transform(lambda x: x.rank())

# Reorder columns
edge_list_df = edge_list_df[['Node 1', 'Node 2', 'Node 3', 'Bar', 'Edge']]

# Display the resulting DataFrame
print(edge_list_df)