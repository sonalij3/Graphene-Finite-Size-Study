import pandas as pd

def extract_properties_from_log(log_file_path):
    data = []
    search_token = 'TotEng'
    df_head = None
    with open(log_file_path, 'r') as f:
        for line in f:
            if search_token in line:
                df_head = line.split()
            try:
                properties = list(map(float, line.split()))
                data.append(properties)
            except:
                continue

    # There is some [] at the end of the data for some reason so I'm removing it
    while [] in data:
        del data[data.index([])]

    # Dropna because if we got some other numeric row we need to eliminate it.
    df = pd.DataFrame(data, columns=df_head).dropna(axis=0)
    return df

# Usage example
common_path = 'C:/Users/Vitor/Desktop/test_lammps.txt' # path of the lammps log file
data = extract_properties_from_log(common_path)
print(data.head())
