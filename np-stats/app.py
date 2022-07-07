import json
import numpy as np

from pycape.io_lifter import io_serialize
from pycape.serialize import deserialize
from pycape.serialize import serialize

@io_serialize
def cape_handler(x):
    ones  =  np.array([1, 1, 1 , 1])
    res = x + ones
    return res


if __name__  == "__main__":
    x = np.array([1, 2, 3, 4])
    x_ser = serialize(x)
    out = cape_handler(x_ser)
    out = deserialize(out)
    print("Res", out)
    
