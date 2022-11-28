import pickle
import sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score

# load the model trained in enclave
with open("trained_sklearn_model.pickle", "rb") as f:
    model = pickle.load(f)

# prepare testing data
data = pd.read_csv("testing_data.csv")
X = data.drop(['Class'], axis=1)
Y = data["Class"]
X_data = X.values
Y_data = Y.values

# run prediction and compute accuracy
y_pred = model.predict(X_data)
print(accuracy_score(Y_data, y_pred))