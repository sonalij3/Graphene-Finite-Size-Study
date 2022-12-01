#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def extract_properties_from_data(log_file_path):
    data = []
    header = ['molecule-tag','atom-type','q','x','y','z','nx','ny','nz']
    searchToken_1 = 'xlo'
    searchToken_2 = 'ylo'
    box_x = []
    box_y = []

    with open(log_file_path, 'r') as f:
        for line in f:
            if searchToken_1 in line:
                box_x = np.asarray(line.split())[0:2].astype(float)
            if searchToken_2 in line:
                box_y = np.asarray(line.split())[0:2].astype(float)
            try:
                properties = list(map(float, line.split()))
                data.append(properties)
            except:
                continue

    # There is some [] at the end of the data for some reason so I'm removing it
    while [] in data:
        del data[data.index([])]

    # Dropna because if we got some other numeric row we need to eliminate it.
    df = pd.DataFrame(data, columns=header).dropna(axis=0)
    return df, box_x,box_y




file = "graphene_single_layer_x-45_y_45_795_C.data"
df,box_x,box_y = extract_properties_from_data(file)
plt.figure()
plt.scatter(df['x'],df['y'])
x_holder = np.ones(len(df['x']))
y_holder = np.ones(len(df['y']))
plt.plot(x_holder*box_x[0],np.linspace(box_y[0],box_y[1],len(df['x'])),color='k')
plt.plot(x_holder*box_x[1],np.linspace(box_y[0],box_y[1],len(df['x'])),color='k')
plt.plot(np.linspace(box_x[0],box_x[1],len(df['y'])),y_holder*box_y[0],color='k')
plt.plot(np.linspace(box_x[0],box_x[1],len(df['y'])),y_holder*box_y[1],color='k')
plt.ylabel('y (Angstrom meters)')
plt.xlabel('x (Angstrom meters)')

# %%
