from sklearn.metrics import accuracy_score
from joblib import load
import pandas as pd


def cape_handler(input_data):
    csv = input_data.decode("utf-8")
    csv = csv.replace("\\t", ",").replace("\\n", "\n")
    f = open("data.csv", "w")
    f.write(csv)
    f.close()

    data = pd.read_csv("data.csv")
    clf = load('model.joblib')
    y_pred = clf.predict(data)
    if y_pred == 0:
        return "This credit card transaction is legitimate"
    else:
        return "This credit card transaction is fraudulent"