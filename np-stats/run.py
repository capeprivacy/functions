import os

import numpy as np
from pycape import Cape


import numpy_serde as serde

if __name__ == "__main__":
    function_id_env = os.environ.get("FUNCTION_ID")
    token_env = os.environ.get("TOKEN")

    cape = Cape()
    f = cape.function(function_id_env)
    t = cape.token(token_env)

    x = np.array([1, 2, 3, 4])
    result = cape.run(f, t, x, serde_hooks=(serde.encoder, serde.decoder), use_serdio=True)

    print(f"The result is: {result}")
