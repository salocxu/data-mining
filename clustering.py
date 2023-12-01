#importer les packages
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#importer les packages kmeans
from sklearn.cluster  import KMeans
from sklearn.preprocessing import StandardScaler

df=pd.read_excel('resultat_jointure.xlsx')
dfa=df[['lat',"lon"]]


#standardiser les données
scdfa=StandardScaler()
dfa_std=scdfa.fit_transform(dfa.astype(float))

#On part sur 3 clusters
kmeans=KMeans(n_clusters=3).fit(dfa_std)

#affecter les cluster à la varialb e labels
labels=kmeans.labels_

#créer un dataset qui contient les valeurs de dfa_std
new_dfa=pd.DataFrame(data=dfa_std,columns=['lat','lon'])

#rajouter les labels à mon dataset dfa_std
new_dfa['labels_kmeans']=labels

#visualiser les cluster en 2dimesions
fig,ax=plt.subplots(figsize=[10,7])
plt.scatter(new_dfa['lat'][new_dfa['labels_kmeans']==0],new_dfa['lon'][new_dfa['labels_kmeans']==0],
            color='blue',s=100,linestyle='--')
plt.scatter(new_dfa['lat'][new_dfa['labels_kmeans']==1],new_dfa['lon'][new_dfa['labels_kmeans']==1],
            color='red',s=100,linestyle='--')
plt.scatter(new_dfa['lat'][new_dfa['labels_kmeans']==2],new_dfa['lon'][new_dfa['labels_kmeans']==2],
            color='green',s=100,linestyle='--')

plt.show()