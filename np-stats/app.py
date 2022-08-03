import numpy as np

import serdio

import numpy_serde


@serdio.lift_io(
    hook_bundle=(numpy_serde.encoder, numpy_serde.decoder),
    as_handler=True,
)
def cape_handler(x: np.ndarray) -> np.ndarray:
    return x + np.ones(4)
