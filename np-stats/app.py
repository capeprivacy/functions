import numpy as np

import pycape


@pycape.lift_io
def add_ones(x: np.ndarray) -> np.ndarray:
    return x + np.ones(4)

cape_handler = add_ones.as_cape_handler()
