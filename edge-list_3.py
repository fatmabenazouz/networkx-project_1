import pandas as pd

# Read data from an Excel file
file_path = '~/Downloads/edgelist_bars_only_29Jan2024.xls'  # Replace with the actual file path
df = pd.read_excel(file_path)

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