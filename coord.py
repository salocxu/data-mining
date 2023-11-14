import pandas as pd
import folium
import os
import seaborn as sns
# extraire nombre d'un string en exp reguliere
import re 
trains = []
for file in os.listdir('.'):
    if file.endswith('.csv'):
        trains.append(file)



colors = ['darkblue', 'blue', 'beige', 'green', 'orange', 'cadetblue', 'pink', 'lightred', 'purple', 'lightgray', 'red', 'gray', 'white', 'black', 'lightgreen', 'lightblue', 'darkpurple', 'darkred', 'darkgreen']

#initialiser la carte

data0 = pd.read_csv(trains[0], delimiter=',')
number = re.search(r'\d+', trains[0]).group()

carte = folium.Map(location=[data0['lat'].mean(), data0['lon'].mean()], zoom_start=8)

for index, row in data0.iterrows(): 
    
    folium.Marker([row['lat'], row['lon']], icon=folium.Icon(color=colors[0]), popup= f'Train {number}').add_to(carte)

for elem, color in zip(trains[1:], colors[1:]):
# Spécifiez le chemin vers votre fichier Excel
    number = re.search(r'\d+', elem).group()

# Chargez le fichier Excel dans un DataFrame
    data = pd.read_csv(elem, delimiter=',')

# Ajouter des marqueurs pour chaque lieu sur la carte

    for index, row in data.iterrows():
    
        folium.Marker([row['lat'], row['lon']], icon=folium.Icon(color=color), popup= f'Train {number}').add_to(carte)

# Sauvegarder la carte au format HTML
carte.save('carte_geographique.html')