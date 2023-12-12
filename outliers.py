import pandas as pd
from scipy.stats import zscore
import numpy as np
import variables

from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score


def detect_outliers(excel_file, limit_air, limit_oil, limit_water, z_score_threshold):
    # Load the CSV file containing all the data
    all_data = pd.read_excel(excel_file)

    air_columns = ['RS_E_InAirTemp_PC1', 'RS_E_InAirTemp_PC2']
    oil_columns = ['RS_T_OilTemp_PC1', 'RS_T_OilTemp_PC2']
    water_columns = ['RS_E_WatTemp_PC1', 'RS_E_WatTemp_PC2']

    # Combine all temperature columns
    all_temperature_columns = air_columns + oil_columns + water_columns

    # Calculate Z-scores for temperature columns
    z_scores = np.abs(zscore(all_data[all_temperature_columns]))

    # Identify outliers based on Z-scores
    z_score_outliers = (z_scores > z_score_threshold).any(axis=1)

    # Identify outliers based on specified limits
    limit_outliers = (
        (all_data[air_columns] > limit_air) |
        (all_data[oil_columns] > limit_oil) |
        (all_data[water_columns] > limit_water)
    ).any(axis=1)

    # Combine Z-score outliers and limit outliers
    all_data['outlier'] = (z_score_outliers | limit_outliers).astype(int)

    return all_data

# Example usage
file_path = 'resultat_jointure2.xlsx'  # Replace with the actual file path
result_with_outliers = detect_outliers(file_path, limit_air=variables.limit_air, limit_oil=variables.limit_oil, limit_water=variables.limit_water, z_score_threshold=3)

result_with_outliers.to_excel('result_with_outliers.xlsx', index=False)

# Assuming 'outlier' is the ground truth and 'outlier_prediction' is the predicted outliers
y_true = result_with_outliers['maintenance']
y_pred = result_with_outliers['outlier']

# Confusion matrix
conf_matrix = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:\n", conf_matrix)

# Precision, Recall, and F1-Score
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print("Precision:", precision)
print("Recall:", recall)
print("F1-Score:", f1)