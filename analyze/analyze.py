import pandas as pd
import numpy as np

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

def get_data(file, warmup=1501):

    common_path = file # path of the lammps log file
    LJ_data = extract_properties_from_log(common_path)

    var_u = np.var(LJ_data['PotEng'][warmup:]) # Variance of potential energy kcal/mol
    var_e = np.var(LJ_data['TotEng'][warmup:]) # Variance of total energy kcal/mol

    k_b = 3.29983031e-27 # kcal/K
    T = np.mean(LJ_data['Temp'][warmup:]) # K
    N_A = 6.022e23 # mol

    C_v_u = var_u/(N_A*k_b*T*T) # kcal^2*K
                                # -----------
                                # kcal*mol^2*K^2 
    C_v_e = var_e/(N_A*k_b*T*T) # kcal^2*K
                                # -----------
                                # kcal*mol^2*K^2 
    
    E = np.mean(LJ_data['TotEng'][warmup:])
    U = np.mean(LJ_data['PotEng'][warmup:])
    T = np.mean(LJ_data['Temp'][warmup:])

    tmp = {}
    tmp[f'var_u'] = var_u
    tmp[f'var_e'] = var_e
    tmp[f'C_v_u'] = C_v_u
    tmp[f'C_v_e'] = C_v_e
    tmp[f'E']     = E
    tmp[f'U']     = U
    tmp[f'T']     = T
    
    df = pd.DataFrame([tmp])

    df.to_csv(f"csv/T_{np.round(T, decimals=0)}.csv")

    return df

if __name__ == "__main__":

    file1  = "graphene_single_layer_LJ_795C_after_temp_10K_log.txt"
    file2  = "graphene_single_layer_LJ_795C_after_temp_50K_log.txt"
    file3  = "graphene_single_layer_LJ_795C_after_temp_60K_log.txt"
    file4  = "graphene_single_layer_LJ_795C_after_temp_70K_log.txt"
    file5  = "graphene_single_layer_LJ_795C_after_temp_100K_log.txt"
    file6  = "graphene_single_layer_LJ_795C_after_temp_200K_log.txt"
    file7  = "graphene_single_layer_LJ_795C_after_temp_300K_log.txt"
    file8  = "graphene_single_layer_LJ_795C_after_temp_400K_log.txt"
    file9  = "graphene_single_layer_LJ_795C_after_temp_500K_log.txt"
    file10 = "graphene_single_layer_LJ_795C_after_temp_600K_log.txt"
    file11 = "graphene_single_layer_LJ_795C_after_temp_700K_log.txt"
    file12 = "graphene_single_layer_LJ_795C_after_temp_800K_log.txt"
    file13 = "graphene_single_layer_LJ_795C_after_temp_900K_log.txt"
    file14 = "graphene_single_layer_LJ_795C_after_temp_1000K_log.txt"
    file15 = "graphene_single_layer_LJ_795C_after_temp_1100K_log.txt"
    file16 = "graphene_single_layer_LJ_795C_after_temp_1200K_log.txt"
    file17 = "graphene_single_layer_LJ_795C_after_temp_1300K_log.txt"
    file18 = "graphene_single_layer_LJ_795C_after_temp_1400K_log.txt"

    file_names = [file1,
                  file2,
                  file3,
                  file4,
                  file5,
                  file6,
                  file7,
                  file8,
                  file9,
                  file10,
                  file11,
                  file12,
                  file13,
                  file14,
                  file15,
                  file16,
                  file17,
                  file18]


    df = get_data(file1)

    for i in range(1,18):
        df = pd.concat([df, get_data(file_names[i])])

    df.to_csv(f"csv/alldata.csv")
