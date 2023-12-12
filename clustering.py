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

# Compter le nombre d'occurrences de 1 en fonction de la valeur de colonne2
ano_par_ligne = new_dfa.groupby(labels).sum()
records_par_ligne = new_dfa.groupby(labels).size()

ano_l1=(ano_par_ligne.iloc[0,3])
ano_l2=(ano_par_ligne.iloc[1,3])
ano_l3=(ano_par_ligne.iloc[2,3])
rec_l1=(records_par_ligne.iloc[0])
rec_l2=(records_par_ligne.iloc[1])
rec_l3=(records_par_ligne.iloc[2])

freq_ano_l1=(ano_l1/rec_l1)*100
freq_ano_l2=(ano_l2/rec_l2)*100
freq_ano_l3=(ano_l3/rec_l3)*100

freqtot_l1=(ano_l1/(ano_l1+ano_l2+ano_l3))*100
freqtot_l2=(ano_l2/(ano_l1+ano_l2+ano_l3))*100
freqtot_l3=(ano_l3/(ano_l1+ano_l2+ano_l3))*100

# Afficher les résultats
print('la fréquence danomalie sur la ligne 1 est de', freq_ano_l1)
print('la fréquence danomalie sur la ligne 2 est de', freq_ano_l2)
print('la fréquence danomalie sur la ligne 3 est de', freq_ano_l3)
print('la fréquence danomalie sur la ligne 1 par rapport à toutes les anomalies est de', freqtot_l1)
print('la fréquence danomalie sur la ligne 2 par rapport à toutes les anomalies est de', freqtot_l2)
print('la fréquence danomalie sur la ligne 3 par rapport à toutes les anomalies est de', freqtot_l3)


#ajout de la colonne labels au fichier csv principal
df['labels_kmeans']=labels

# Créer trois nouveaux DataFrames en fonction des labels
cluster_0 = df[df['labels_kmeans'] == 0]
cluster_1 = df[df['labels_kmeans'] == 1]
cluster_2 = df[df['labels_kmeans'] == 2]

# Enregistrer chaque DataFrame dans un fichier CSV
cluster_0.to_csv('ligne_1.csv', index=False)
cluster_1.to_csv('ligne_2.csv', index=False)
cluster_2.to_csv('ligne_3.csv', index=False)

plt.show()