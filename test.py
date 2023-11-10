import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:/Users/fdixi/Desktop/H423-Data mining/Project/ar41_for_ulb.csv'
all_data = pd.read_csv(file_path, delimiter=';', nrows=10000, usecols=lambda x: x != 'Unnamed: 0')
grouped_data = all_data.groupby('mapped_veh_id')





temperature_column = 'RS_E_InAirTemp_PC1'

plt.figure(figsize=(10, 6))
plt.scatter(all_data[temperature_column], range(len(all_data)), color='skyblue', edgecolor='black', alpha=0.6)
plt.title(f'Nuage de points de la Température ({temperature_column}) pour le Train 181')
plt.xlabel('Échantillons')
plt.ylabel('Température')
plt.show()
