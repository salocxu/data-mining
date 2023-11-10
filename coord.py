import pandas as pd
import folium


# Spécifiez le chemin vers votre fichier Excel
chemin_fichier_excel = 'data_tab.xlsx'

# Chargez le fichier Excel dans un DataFrame
data = pd.read_excel(chemin_fichier_excel)


carte = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=4)

# Ajouter des marqueurs pour chaque lieu sur la carte
for index, row in data.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Nom']).add_to(carte)

# Sauvegarder la carte au format HTML
carte.save('carte_geographique.html')