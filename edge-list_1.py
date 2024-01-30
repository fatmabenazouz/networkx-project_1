import pandas as pd

# Sample data
data = [
    ["1-2-0011-01", "Bar17"],
    ["1-2-0011-01", "Bar21"],
    ["1-2-0013-01", "Bar25"],
    ["1-2-0013-01", "Bar26"],
    ["1-2-0013-01", "Bar30"],
    ["1-2-0013-01", "Bar30"],
    ["1-2-0017-01", "Bar27"],
    ["1-2-0027-01", "Bar16"],
    ["1-2-0027-01", "Bar19"],
    ["1-2-0029-01", "Bar55"],
    ["1-2-0029-01", "Bar56"],
    ["1-2-0034-01", "Bar18"],
    ["1-2-0038-01", "Bar31"],
    ["1-2-0061-01", "Bar35"],
    ["1-2-0064-01", "Bar52"],
    ["1-2-0064-01", "Bar54"],
    ["1-2-0074-01", "Bar29"],
    ["1-2-0074-01", "Bar29"],
    ["1-2-0088-01", "Bar60"],
    ["1-2-0097-01", "Bar20"],
    ["1-2-0100-01", "Bar22"],
    ["1-2-0100-01", "Bar23"],
    ["1-2-0107-01", "Bar50"],
    ["1-2-0107-01", "Bar54"],
    ["1-2-0116-01", "Bar63"],
    ["1-2-0128-01", "Bar61"],
    ["1-2-0135-01", "Bar37"],
    ["1-2-0136-01", "Bar62"],
    ["1-2-0138-01", "Bar57"],
    ["1-2-0139-01", "Bar47"],
    ["1-2-0139-01", "Bar48"],
    ["1-2-0139-01", "Bar49"],
    ["1-2-0139-01", "Bar49"],
    ["1-2-0140-01", "Bar58"],
    ["1-2-0140-01", "Bar59"],
    ["1-2-0148-01", "Bar15"],
    ["1-2-0149-01", "Bar2"],
    ["1-2-0152-01", "Bar28"],
    ["1-2-0154-01", "Bar1"],
    ["1-2-0154-01", "Bar3"],
    ["1-2-0163-01", "Bar32"],
    ["1-2-0163-01", "Bar33"],
    ["1-2-0164-01", "Bar51"],
    ["1-2-0164-01", "Bar52"],
    ["1-2-0164-01", "Bar54"],
    ["2-1-1055-01", "Bar38"],
    ["2-1-1055-01", "Bar44"],
    ["2-2-1033-01", "Bar46"],
    ["2-2-1108-01", "Bar39"],
    ["2-2-1108-01", "Bar40"],
    ["2-2-1112-01", "Bar38"],
    ["2-2-1121-01", "Bar8"],
    ["2-2-1134-01", "Bar12"],
    ["2-2-1149-01", "Bar34"],
    ["2-2-1149-01", "Bar36"],
    ["2-2-1155-01", "Bar9"],
    ["2-2-1156-01", "Bar53"],
    ["2-2-1157-01", "Bar44"],
    ["2-2-1157-01", "Bar45"],
    ["2-2-1158-01", "Bar42"],
    ["2-2-1158-01", "Bar43"],
    ["2-2-1174-01", "Bar10"],
    ["2-2-1174-01", "Bar11"],
    ["2-2-1184-01", "Bar41"],
    ["2-2-1185-01", "Bar5"],
    ["2-2-1185-01", "Bar6"],
    ["2-2-1187-01", "Bar14"],
    ["2-2-1188-01", "Bar13"],
    ["2-2-1191-01", "Bar7"],
    ["3-2-3007-01", "Bar4"],
    ["3-2-3009-01", "Bar24"]
]

# Creating a DataFrame from the sample data
df = pd.DataFrame(data, columns=["studyid", "bar"])

# Creating the edge list
edge_list = []

# Iterating over unique study IDs
for study_id in df["studyid"].unique():
    # Filtering data for each study ID
    study_data = df[df["studyid"] == study_id]
    
    # Creating edges for each unique combination of "bar"
    for i in range(len(study_data["bar"])):
        for j in range(i+1, len(study_data["bar"])):
            edge_list.append({
                "Node 1": study_id,
                "Node 2": "" if i == 0 else study_data["bar"].iloc[i-1],
                "Node 3": "" if j == 0 else study_data["bar"].iloc[j-1],
                "Bar": study_data["bar"].iloc[i],
                "Edge": len(edge_list) + 1
            })

# Creating a DataFrame from the edge list
edge_list_df = pd.DataFrame(edge_list, columns=["Node 1", "Node 2", "Node 3", "Bar", "Edge"])

# Displaying the edge list
print(edge_list_df)