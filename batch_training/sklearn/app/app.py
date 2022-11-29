# import necessary packages
import sklearn
from sklearn.linear_model import SGDClassifier
import pandas as pd
import pickle

def cape_handler(batch):
    # accept batch input training data
    batch = batch.decode()
    data = pd.read_json(batch)

    # load model
    with open("model.pickle", "rb") as f:
        clf = pickle.load(f)

    # prep batch data
    X = data.drop(['Class'], axis=1)
    Y = data["Class"]
    X_data = X.values
    Y_data = Y.values

    # train
    clf.partial_fit(X, Y, classes=[0,1])
    
    # save model
    with open("model", "wb") as f:
        pickle.dump(clf, f)

    # return model
    s = pickle.dumps(clf)
    return s