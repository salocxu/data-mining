import pandas as pd
import folium
import os
import os


count = 0
for file in os.listdir('.'):
    if file.endswith('.csv'):
        count += 1

print(count)


#nombre de fichier csv dans le dossier 

    
# Spécifiez le chemin vers votre fichier Excel
chemin_fichier_excel = 'data_tab.xlsx'

# Chargez le fichier Excel dans un DataFrame
data = pd.read_excel(chemin_fichier_excel)


carte = folium.Map(location=[data['lat'].mean(), data['lon'].mean()], zoom_start=4)

# Ajouter des marqueurs pour chaque lieu sur la carte
for index, row in data.iterrows():
    folium.Marker([row['lat'], row['lon']], popup=row['']).add_to(carte)

# Sauvegarder la carte au format HTML
carte.save('carte_geographique.html')