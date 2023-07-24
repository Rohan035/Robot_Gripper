import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load the data from the Excel file
df = pd.read_excel('/home/jarvis/Downloads/FirstTest-AutomaticSelectio.xlsx')
X = df.drop('sgc22', axis=1)
X_cleaned = X.dropna()
#df_nan = df[df.isna(X)]
#df_zerofill = df.fillna(0)
# Separate the features (X) and the target variable (y)
#X = data.drop('sgc22', axis=1)  # Remove the target variable column
#y = data['sgc22']  # Keep only the target variable column

# Perform label encoding on the string column
#label_encoder = LabelEncoder()
#X['Items'] = label_encoder.fit_transform(X['Items'])

# Create a Random Forest classifier
#rf = RandomForestClassifier(n_estimators=100)

# Train the model
#rf.fit(X, y)
