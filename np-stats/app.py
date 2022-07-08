import numpy as np

from pycape import io_serialize


@io_serialize
def cape_handler(x):
    return x + np.ones(4)