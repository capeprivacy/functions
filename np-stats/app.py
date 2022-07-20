import numpy as np

import pycape

import numpy_serde


@pycape.lift_io(
    hook_bundle=(numpy_serde.encoder, numpy_serde.decoder),
)
def add_ones(x: np.ndarray) -> np.ndarray:
    return x + np.ones(4)


cape_handler = add_ones.as_cape_handler()
