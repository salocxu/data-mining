import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import practical_tools as pt

# Load the data
result_interm = pd.read_csv('trains/train122.csv')


features = ['RS_E_InAirTemp_PC1', 'RS_E_InAirTemp_PC2','RS_T_OilTemp_PC1', 'RS_T_OilTemp_PC2','RS_E_WatTemp_PC1', 'RS_E_WatTemp_PC2']  # Replace with your actual feature names



# Separate features (X) and target variable (y)

X = result_interm[features+ ['air1', 'oil2', 'water2','oil1', 'water1']]
    

y = result_interm['air2']


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=80)

# Initialize the logistic regression model
model = LogisticRegression()

#print(f'{X_train} \n')
print(y_train)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Print results
print("Accuracy:", accuracy)
print("\nConfusion Matrix:\n", confusion_mat)
print("\nClassification Report:\n", classification_rep)

