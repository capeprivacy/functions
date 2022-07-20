import os

from pycape import Cape

import numpy as np

if __name__ == "__main__":
    token = os.environ.get("CAPE_TOKEN", None)
    url = os.environ.get("CAPE_HOST", "wss://hackathon.capeprivacy.com")
    function_id = os.environ.get(
        "CAPE_FUNCTION", "b65b77c4-5422-451b-8291-55d9f4b7a016"
    )

    cape = Cape(url=url, access_token=token)
    x = np.array([1, 2, 3, 4])
    result = cape.run(function_id, x, msgpack_serialize=True)

    print(f"The result is: {result}")
