import os
import pathlib
from tqdm.notebook import tqdm
import pandas as pd
import pickle

from pycape import Cape
from pycape import FunctionRef

if __name__ == "__main__":
    url = os.environ.get("CAPE_HOST", "https://k8s-cape-enclaver-750003af11-e3080498c852b366.elb.us-east-1.amazonaws.com")
    function_json = os.environ.get("FUNCTION_JSON", "app_token.json")
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