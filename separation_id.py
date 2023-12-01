import pandas as pd

# mettre en binaires les valeurs des colonnes qui nous interessent
def prepare_logistic_reg(excel_file, limite_air, limite_oil, limite_water):
    all_data = pd.read_excel(excel_file)
    all_data['air1'] = 0
    all_data['air2'] = 0
    all_data['oil1'] = 0
    all_data['oil2'] = 0
    all_data['water1'] = 0
    all_data['water2'] = 0
   
    airr = ['air1', 'air2']
    oil = ['oil1', 'oil2']
    water = ['water1', 'water2']
    air_columns = ['RS_E_InAirTemp_PC1', 'RS_E_InAirTemp_PC2']
    oil_columns = ['RS_T_OilTemp_PC1', 'RS_T_OilTemp_PC2']
    water_columns = ['RS_E_WatTemp_PC1', 'RS_E_WatTemp_PC2']

    all_data[airr] = (all_data[air_columns] > limite_air).astype(int)
    all_data[oil] = (all_data[oil_columns] > limite_oil).astype(int)
    all_data[water] = (all_data[water_columns] > limite_water).astype(int)

    return all_data

def add_maintenance(data: pd.DataFrame):
    airr = ['air1', 'air2']
    oil = ['oil1', 'oil2']
    water = ['water1', 'water2']
    
    data['maintenance'] = 0
    all = data[airr + oil + water]
    
    data.loc[all.any(axis=1) !=0, 'maintenance'] = 1

#histoire de 
    maintenance_frequency = data['maintenance'].sum()
    print(f"Frequency of Maintenance Events: {maintenance_frequency}")

    return data


#Charger le fichier CSV contenant toutes les données
file_path = 'data_tab.xlsx'

result_interm = prepare_logistic_reg(file_path, 65, 115, 100)
result = add_maintenance(result_interm)

result.to_csv('resultat_avec_colonnes.csv', index=False, sep=',')

#Grouper les données par identifiant de train (mapped_veh_id)
grouped_data = result.groupby('mapped_veh_id')

#Enregistrer les données de chaque train dans un fichier CSV séparé
for train_id, train_data in grouped_data:
    train_filename = f'trains/train{train_id}.csv'
    train_data.to_csv(train_filename, index=False, sep=',')