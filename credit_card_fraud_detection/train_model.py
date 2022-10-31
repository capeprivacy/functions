import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump, load

data = pd.read_csv("creditcard.csv")
X = data.drop(['Class'], axis=1)
Y = data["Class"]
X_data = X.values
Y_data = Y.values
X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size = 0.2, random_state = 42)


model = RandomForestClassifier()
model.fit(X_train, Y_train)

y_pred = model.predict(X_test)
print(accuracy_score(Y_test, y_pred))

# save model
dump(model, 'model.joblib') 
