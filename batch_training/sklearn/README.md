# Batch training

This readme describes how to perform batch training on an Sklearn model with pycape

## How to perform batch training with Cape on sklearn models

### Prepare sklearn model
Run:
```
python3 prep_sklearn_model.py
``` 
In this script you specify the sklearn model type and save it as a pickle. This untrained pickled model will be deployed into the enclave, where it will be trained.

E.g.:
```
# initialize model
clf = SGDClassifier(alpha=.0001, loss='log', penalty='l2', n_jobs=-1, shuffle=True)

# save model
with open("model.pickle", "wb") as f:
    pickle.dump(clf, f)
```
### Prepare app.py
The `cape_hander()` function in `app.py` will receive a batch of training data, load the pickled model, train it on that batch, save the model as a pickle, and return it.
E.g.:
```
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
```

### Prepare deployment folder with dependencies
Create a depoyment folder called `app`:
```
mkdir app
```
Save app.py into the folder:
```
cp app.py ./app
```
Save untrained model into the folder:
```
cp model.pickle ./app
```
Install necessary libraries listed in `requirements.txt`
```
sudo docker run -v `pwd`:/build -w /build --rm -it python:3.9-slim-bullseye pip install -r requirements.txt --target ./app/
```

### Login and deploy with Cape
```
cape login

Your CLI confirmation code is: GQDK-SNHL
Visit this URL to complete the login process: https://login.capeprivacy.com/activate?user_code=GQDK-SNHL
Congratulations, you're all set!
```

```
cape deploy ./app

Deploying function to Cape ...
Success! Deployed function to Cape.
Function ID ➜  NxnusuJ8caocbx9ckEg5tb
Function Checksum ➜  bf750d97b35fe9973e580949e4143ea5350df2d3ca607f85aecebbe016ac1eb1
```

### Generate token

```
cape token <FUNCTION_ID> --function-checksum <FUNCTION_CHECKSUM> -o json > app_token.json
```

The file `app_token.json` will be used to create a function reference `pycape.FunctionRef` for estabilishing a connection with the enclave.

### Invoke the deployed Cape function from PyCape
```
CAPE_DEV_DISABLE_SSL=True python3 invoke_app_sklearn.py
```
This script will invoke the Cape function repeatedly to train the model batch by batch. After training is completed, the model is saved as a pickle file.

E.g.:
```
import os
import pathlib
from tqdm.notebook import tqdm
import pandas as pd
import pickle

from pycape import Cape
from pycape import FunctionRef

if __name__ == "__main__":
    url = os.environ.get("CAPE_HOST", "https://k8s-cape-enclaver-750003af11-e3080498c852b366.elb.us-east-1.amazonaws.com")
    function_json = os.environ.get("FUNCTION_JSON", "sklearn_token.json")
    function_json = pathlib.Path(__file__).parent.absolute() / function_json
    function_ref = FunctionRef.from_json(function_json)
    cape = Cape(url=url)
    cape.connect(function_ref)

# set batch size
batch_size = 500

# train model in batches
for batch_df in tqdm(pd.read_csv("training_data.csv", chunksize=batch_size, iterator=True)):
    df_byte = batch_df.to_json().encode()
    clf = cape.invoke(df_byte)
    clf = pickle.loads(clf)

# save model
with open("trained_sklearn_model.pickle", "wb") as f:
    pickle.dump(clf, f)
```

### Test the trained model
```
python3 test_app_sklearn.py
```

E.g.:
```
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
```