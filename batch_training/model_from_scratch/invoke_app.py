import os
import pathlib
from tqdm.notebook import tqdm
import pandas as pd

from pycape import Cape
from pycape import FunctionRef

if __name__ == "__main__":
    url = os.environ.get("CAPE_HOST", "https://app.capeprivacy.com")
    function_json = os.environ.get("FUNCTION_JSON", "app_token.json")
    function_json = pathlib.Path(__file__).parent.absolute() / function_json
    function_ref = FunctionRef.from_json(function_json)
    cape = Cape(url=url)
    cape.connect(function_ref)

    batch_size = 500
    for batch_df in tqdm(pd.read_csv("train_data.csv", chunksize=batch_size, iterator=True)):
        df_byte = batch_df.to_json().encode()
        clf = cape.invoke(df_byte)
    
    # trained model
    print(clf.decode())
    cape.close()