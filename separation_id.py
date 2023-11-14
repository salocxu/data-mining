import pandas as pd

#Charger le fichier CSV contenant toutes les données
file_path = 'data_tab.xlsx'
all_data = pd.read_excel(file_path)

#Grouper les données par identifiant de train (mapped_veh_id)
grouped_data = all_data.groupby('mapped_veh_id')

#Enregistrer les données de chaque train dans un fichier CSV séparé
for train_id, train_data in grouped_data:
    train_filename = f'train{train_id}.csv'
    train_data.to_csv(train_filename, index=False, sep=',')