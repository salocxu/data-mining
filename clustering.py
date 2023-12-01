#importer les packages
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#importer les packages kmeans
from sklearn.cluster  import KMeans
from sklearn.preprocessing import StandardScaler

df=pd.read_csv('resultat_avec_colonnes.csv')
dfa=df[['lat',"lon"]]


#standardiser les données
scdfa=StandardScaler()
dfa_std=scdfa.fit_transform(dfa.astype(float))

#On part sur 3 clusters
kmeans=KMeans(n_clusters=3).fit(dfa_std)

#affecter les cluster à la varialb e labels
labels=kmeans.labels_

anomalie=df['maintenance']

#créer un dataset qui contient les valeurs de dfa_std
new_dfa=pd.DataFrame(data=dfa_std,columns=['lat','lon'])

#rajouter les labels à mon dataset dfa_std
new_dfa['labels_kmeans']=labels
new_dfa['anomalie_bin']=anomalie

#visualiser les cluster en 2dimesions
fig,ax=plt.subplots(figsize=[10,7])
plt.scatter(new_dfa['lat'][new_dfa['labels_kmeans']==0][new_dfa['anomalie_bin']==0],
            new_dfa['lon'][new_dfa['labels_kmeans']==0][new_dfa['anomalie_bin']==0],
            color='blue',s=20,linestyle='--')
plt.scatter(new_dfa['lat'][new_dfa['labels_kmeans']==1][new_dfa['anomalie_bin']==0],
            new_dfa['lon'][new_dfa['labels_kmeans']==1][new_dfa['anomalie_bin']==0],
            color='green',s=20,linestyle='--')
plt.scatter(new_dfa['lat'][new_dfa['labels_kmeans']==2][new_dfa['anomalie_bin']==0],
            new_dfa['lon'][new_dfa['labels_kmeans']==2][new_dfa['anomalie_bin']==0],
            color='yellow',s=20,linestyle='--')
plt.scatter(new_dfa['lat'][new_dfa['labels_kmeans']==0][new_dfa['anomalie_bin']==1],
            new_dfa['lon'][new_dfa['labels_kmeans']==0][new_dfa['anomalie_bin']==1],
            color='red',s=20,linestyle='--')
plt.scatter(new_dfa['lat'][new_dfa['labels_kmeans']==1][new_dfa['anomalie_bin']==1],
            new_dfa['lon'][new_dfa['labels_kmeans']==1][new_dfa['anomalie_bin']==1],
            color='red',s=20,linestyle='--')
plt.scatter(new_dfa['lat'][new_dfa['labels_kmeans']==2][new_dfa['anomalie_bin']==1],
            new_dfa['lon'][new_dfa['labels_kmeans']==2][new_dfa['anomalie_bin']==1],
            color='red',s=20,linestyle='--')


plt.show()