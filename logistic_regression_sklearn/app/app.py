import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def cape_handler(input_data):
    csv = input_data.decode("utf-8")
    csv = csv.replace("\\t", ",").replace("\\n", "\n")
    f = open("data.csv", "w")
    f.write(csv)
    f.close()

    data = pd.read_csv("data.csv")
    # data = pd.read_csv('../breast_cancer_data.csv')
    data_size = data.shape[0]
    test_split = 0.33
    test_size = int(data_size * test_split)

    choices = np.arange(0, data_size)
    test = np.random.choice(choices, test_size, replace=False)
    train = np.delete(choices, test)

    test_set = data.iloc[test]
    train_set = data.iloc[train]

    column_names = list(data.columns.values)
    features = column_names[1 : len(column_names) - 1]

    y_train = train_set["target"]
    y_test = test_set["target"]
    X_train = train_set[features]
    X_test = test_set[features]

    lr = make_pipeline(StandardScaler(), LogisticRegression())
    lr.fit(X_train, y_train)
    pred = lr.predict(X_test)

    accuracy = sum(pred == y_test) / pred.shape[0]

    # trained model
    model = {
        "accuracy": accuracy,
        "weights": lr[1].coef_.tolist(),
        "bias": lr[1].intercept_.tolist(),
    }

    return model


print(cape_handler("dfdsf"))
