import pandas as pd

# reading data from an excel file
file_path = '~/Desktop/Excel Files/SNMETRIC_NW_edgelist_7Feb2024.xls'
df = pd.read_excel(file_path)

# creating a dictionary to store the edge list
edge_list = {'Node 1': [], 'Node 2': [], 'Location': [], 'Edge': []}

# unique study IDs
for study_id in df['studyid'].unique():
    # unique locations for the current study ID
    locations = df[df['studyid'] == study_id]['location'].unique()

    for location in locations:
        # adding a row for the current location
        edge_list['Node 1'].append(study_id)
        edge_list['Node 2'].append(None)
        edge_list['Location'].append(location)
        edge_list['Edge'].append(None)  # Placeholder for Edge

        # pairs of study IDs for the current locations
        other_study_ids = df[(df['location'] == location) & (df['studyid'] != study_id)]['studyid'].unique()

        # adding data to the edge list
        for other_study_id in other_study_ids:
            edge_list['Node 1'].append(study_id)
            edge_list['Node 2'].append(other_study_id)
            edge_list['Location'].append(location)
            edge_list['Edge'].append(None)  # Placeholder for Edge

# assigning unique numbers to the edge column
edge_list_df = pd.DataFrame(edge_list)
edge_list_df['Edge'] = edge_list_df.groupby(['Location'])['Edge'].transform(lambda x: x.rank())

# reordering columns
edge_list_df = edge_list_df[['Node 1', 'Node 2', 'Location', 'Edge']]

pd.set_option('display.max_rows', None)

# displaying dataframe
print(edge_list_df)

# saving the dataframe to an Excel file
output_file_path = '~/Downloads/NW-edge_list_output.xlsx'
edge_list_df.to_excel(output_file_path, index=False)

print("Data has been successfully saved to", output_file_path)