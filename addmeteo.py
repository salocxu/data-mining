import pandas as pd

# Charger les fichiers Excel dans des DataFrames
df1 = pd.read_excel('data_tab.xlsx')
df2 = pd.read_excel('Donnees_meteo_dayavg.xlsx')

# Convertir la colonne 'timestamps_UTC' de df1 en format datetime
df1['timestamps_UTC'] = pd.to_datetime(df1['timestamps_UTC'])

# Convertir la colonne 'DATE' de df2 en format datetime
df2['DATE'] = pd.to_datetime(df2['DATE'])


# Joindre les DataFrames en fonction des dates
df_merged = pd.merge(df1, df2, left_on='timestamps_UTC', right_on='DATE', how='inner')

# Supprimer la colonne redondante après la jointure
df_merged.drop('DATE', axis=1, inplace=True)

# Enregistrer le DataFrame résultant dans un nouveau fichier Excel
df_merged.to_excel('resultat_jointure.xlsx', index=False)