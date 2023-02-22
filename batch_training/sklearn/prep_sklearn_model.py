"""
Prepare an sklearn model: (1) choose a model type, (2) save it as a pickle that will be deployed to enclave
"""

import pickle
from sklearn.linear_model import SGDClassifier

# initialize model
clf = SGDClassifier(alpha=.0001, loss='log', penalty='l2', n_jobs=-1, shuffle=True)
# save model
with open("model.pickle", "wb") as f:
    pickle.dump(clf, f)