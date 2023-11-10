import csv
import pandas as pd
import numpy as np
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

# faure en sorte de choper directmeent les colonnes qui nous interessent ou prendre sa position 
def supprimer_sous_lim(data : pd.DataFrame, limite : float, liste_colonnes : list ):
    index = 0
    brake = False
    while data.iloc[index+1,0] != None:
        for colonnes in range (data.shape[1]):
            for elem in liste_colonnes:
                if data.columns.values[colonnes] == elem:
                    if data.iloc[index, colonnes] <= limite:
                        print(index, colonnes)
                        data = data.drop(axis=0, index=index)
                        brake = True
                        break
                        # eviter de suprimer liste non existente
            if brake == True:
                brake = False
                break    
            
        index += 1    

    return data



copier = 'oui'

# On parcourt les lignes du CSV
n= 10000
# pas besoin de toujours le faire
    

#voir = data.duplicated(subset='timestamps_UTC', keep='first')
valeur0inutile = ['RS_E_InAirTemp_PC1','RS_E_InAirTemp_PC2', 'RS_E_OilPress_PC1','RS_E_OilPress_PC2','RS_E_RPM_PC1','RS_E_RPM_PC2','RS_E_WatTemp_PC1','RS_E_WatTemp_PC2','RS_T_OilTemp_PC1','RS_T_OilTemp_PC2' ]


if copier == 'oui':
    data = pd.read_csv('ar41_for_ulb.csv', sep=';', nrows=n)
    data = supprimer_sous_lim(data, 0, valeur0inutile )
    workbook = Workbook()
    sheet = workbook.active



    for index in range (len(data.columns)-1):
        sheet.cell(row=1, column=index + 1, value= data.columns[index+1])
    for lignes in range (data.shape[0]):
        for colonnes in range (len(data.columns)-1):
            # type dataframe en a besoin pour les index
            #regarder si deux oil temp
            sheet.cell(row=lignes + 2, column=colonnes + 1, value=data.iloc[lignes ,colonnes+1])

    workbook.save('data_tab.xlsx')
    workbook.close()
#travailler à partir du excel


data = pd.read_excel('data_tab.xlsx')
# je souhaite que tu me fasses une moyenne des donnees sur les colonnes 3 à fin

avg = data.iloc[:, 5:].mean(axis=0)
workbook = Workbook()
sheet = workbook.active

for index in range (len(avg)):
    sheet.cell(row=1, column=index + 1, value= data.columns[index + 5])
    sheet.cell(row=2, column=index + 1, value= avg[index])
    # modifier param cases
    column_letter = get_column_letter(index + 1)
    sheet.column_dimensions[column_letter].width = 20


workbook.save('data_avg.xlsx')
workbook.close()
