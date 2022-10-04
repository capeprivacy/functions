import os
import pathlib

import numpy as np
from pycape import Cape
from pycape import FunctionRef

import numpy_serde as serde

if __name__ == "__main__":
    url = os.environ.get("CAPE_HOST", "wss://enclave.capeprivacy.com")
    function_json = os.environ.get("FUNCTION_JSON", "numpy_token.json")
    function_json = pathlib.Path(__file__).parent.absolute() / function_json

    f = FunctionRef.from_json(function_json)
    cape = Cape(url=url)
    x = np.array([1, 2, 3, 4])
    result = cape.run(f, x, serde_hooks=(serde.encoder, serde.decoder), use_serdio=True)

    print(f"The result is: {result}")
