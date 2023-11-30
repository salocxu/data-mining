import pandas as pd

# mettre en binaires les valeurs des colonnes qui nous interessent
def prepare_logistic_reg(excel_file, limite_air, limite_oil, limite_water):
   
    all_data = pd.read_excel(excel_file)
    air_columns = ['RS_E_InAirTemp_PC1', 'RS_E_InAirTemp_PC2']
    oil_columns = ['RS_T_OilTemp_PC1', 'RS_T_OilTemp_PC2']
    water_columns = ['RS_E_WatTemp_PC1', 'RS_E_WatTemp_PC2']

    all_data[air_columns] = (all_data[air_columns] > limite_air).astype(int)
    all_data[oil_columns] = (all_data[oil_columns] > limite_oil).astype(int)
    all_data[water_columns] = (all_data[water_columns] > limite_water).astype(int)

    return all_data

def add_maintenance(data: pd.DataFrame):
    air_columns = ['RS_E_InAirTemp_PC1', 'RS_E_InAirTemp_PC2']
    oil_columns = ['RS_T_OilTemp_PC1', 'RS_T_OilTemp_PC2']
    water_columns = ['RS_E_WatTemp_PC1', 'RS_E_WatTemp_PC2']

    data['maintenance'] = 0
    all = data[air_columns + oil_columns + water_columns]
    
    data.loc[all.any(axis=1) !=0, 'maintenance'] = 1

#histoire de 
    maintenance_frequency = data['maintenance'].sum()
    print(f"Frequency of Maintenance Events: {maintenance_frequency}")

    return data

#Charger le fichier CSV contenant toutes les données
file_path = 'data_tab.xlsx'

result_interm = prepare_logistic_reg(file_path, 65, 115, 100)
result = add_maintenance(result_interm)

#all_data = pd.read_excel(file_path)

#Grouper les données par identifiant de train (mapped_veh_id)
grouped_data = result.groupby('mapped_veh_id')

#Enregistrer les données de chaque train dans un fichier CSV séparé
for train_id, train_data in grouped_data:
    train_filename = f'trains/train{train_id}.csv'
    train_data.to_csv(train_filename, index=False, sep=',')