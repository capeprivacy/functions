import os
import pathlib

import numpy as np
from pycape import Cape
from pycape import FunctionRef

import numpy_serde as serde

if __name__ == "__main__":
    url = os.environ.get("CAPE_HOST", "wss://enclave.capeprivacy.com")
    token_file = os.environ.get("TOKEN_FILE", "numpy_token.json")
    token_file = pathlib.Path(__file__).parent.absolute() / token_file

    f = FunctionRef.from_json(token_file)
    cape = Cape(url=url)
    x = np.array([1, 2, 3, 4])
    result = cape.run(f, x, serde_hooks=(serde.encoder, serde.decoder), use_serdio=True)

    print(f"The result is: {result}")
