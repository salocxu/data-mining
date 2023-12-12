import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import variables

all_data = pd.read_excel('resultat_jointure2.xlsx')

# choisir en consequence
features = ['RS_E_InAirTemp_PC1', 'RS_E_InAirTemp_PC2', 'RS_T_OilTemp_PC1', 'RS_T_OilTemp_PC2', 'RS_E_WatTemp_PC1', 'RS_E_WatTemp_PC2', 'RS_E_OilPress_PC1', 'RS_E_OilPress_PC2', 'RS_E_RPM_PC1', 'RS_E_RPM_PC2']

# Standardize the features
scaler = StandardScaler()
all_data[features] = scaler.fit_transform(all_data[features])

# Initialize the Isolation Forest model
model = IsolationForest(contamination=variables.contamination)

nan_rows = all_data[all_data[features].isna().any(axis=1)]
nan_rows.to_excel('nan_rows.xlsx', index=False)


# Fit the model to the data
model.fit(all_data[features])

# Predict 
all_data['anomaly'] = model.predict(all_data[features])

# Map the predicted anomalies to 1 (outlier) and 0 (normal)
all_data['anomaly'] = all_data['anomaly'].map({1: 0, -1: 1})

# Display the results
print(all_data[['anomaly']])
