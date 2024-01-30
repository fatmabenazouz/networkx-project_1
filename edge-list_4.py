import pandas as pd

# reading data from an excel file
file_path = '~/Downloads/edgelist_bars_only_29Jan2024.xls'
df = pd.read_excel(file_path)

# creating a dictionary to store the edge list
edge_list = {'Node 1': [], 'Node 2': [], 'Bar': [], 'Edge': []}

# unique Study IDs
for study_id in df['studyid'].unique():
    # Add a row for the current Study ID with a placeholder bar
    edge_list['Node 1'].append(study_id)
    edge_list['Node 2'].append(None)
    edge_list['Bar'].append(df[df['studyid'] == study_id]['bar'].iloc[0])
    edge_list['Edge'].append(None)

    # unique bars for the current Study ID
    bars = df[df['studyid'] == study_id]['bar'].unique()

    # pairs of Study IDs for the current bars
    for bar in bars:
        other_study_ids = df[(df['bar'] == bar) & (df['studyid'] != study_id)]['studyid'].tolist()

        # adding data to the edge list
        for other_study_id in other_study_ids:
            edge_list['Node 1'].append(study_id)
            edge_list['Node 2'].append(other_study_id)
            edge_list['Bar'].append(bar)
            edge_list['Edge'].append(None)  # Placeholder for Edge

# assigning unique numbers to the edge column
edge_list_df = pd.DataFrame(edge_list)
edge_list_df['Edge'] = edge_list_df.groupby(['Bar'])['Edge'].transform(lambda x: x.rank())

# reorder columns
edge_list_df = edge_list_df[['Node 1', 'Node 2', 'Bar', 'Edge']]

# display dataframe
print(edge_list_df)