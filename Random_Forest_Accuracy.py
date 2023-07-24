import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score


data = pd.read_excel('/home/jarvis/Downloads/FirstTest-AutomaticSelection.xlsx')
X = data.drop('sgc22', axis=1)
y = data['sgc22']

# label encoding on the string column
label_encoder = LabelEncoder()
X['Items'] = label_encoder.fit_transform(X['Items'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy sgc22:", accuracy)
