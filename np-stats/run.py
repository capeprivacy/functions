import os

import numpy as np
from pycape import Cape
from pycape import FunctionRef

import numpy_serde as serde

if __name__ == "__main__":
    token = os.environ.get("CAPE_TOKEN", None)
    url = os.environ.get("CAPE_HOST", "wss://enclave.capeprivacy.com")
    function_id = os.environ.get("CAPE_FUNCTION_ID", "bQyv2fbtyJukqx6fUhxMpW")
    function_hash = os.environ.get(
        "CAPE_FUNCTION_HASH",
        "d66591e203325d3fec3dc9d6f5936a419adf3a373014f99cd65ec56bbfe4da4a",
    )

    if function_hash is None:
        function_ref = function_id
    else:
        function_ref = FunctionRef(function_id, function_hash)

    cape = Cape(url=url, access_token=token)
    x = np.array([1, 2, 3, 4])
    f = FunctionRef(function_id, function_hash)
    result = cape.run(f, x, serde_hooks=(serde.encoder, serde.decoder), use_serdio=True)

    print(f"The result is: {result}")
