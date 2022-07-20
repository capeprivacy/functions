import msgpack
import numpy as np


def encoder(x):
    if isinstance(x, np.ndarray):
        return {"__type__": "ndarray", "ndarray_bytes": _ndarray_to_bytes(x)}
    elif np.issctype(type(x)):
        # pack scalar as ndarray
        return {
            "__type__": "npscalar",
            "npscalar_bytes": _ndarray_to_bytes(np.asarray(x)),
        }


def decoder(ddict):
    if "__type__" in ddict:
        if ddict["__type__"] == "ndarray":
            return _ndarray_from_bytes(ddict["ndarray_bytes"])
        elif ddict["__type__"] == "npscalar":
            arr = _ndarray_from_bytes(ddict["npscalar_bytes"])
            return arr[()]
    return ddict


def _ndarray_to_bytes(arr) -> bytes:
    """Save ndarray to simple msgpack encoding."""
    if arr.dtype.hasobject or arr.dtype.isalignedstruct:
        raise ValueError(
            "Object and structured dtypes not supported "
            "for serialization of ndarrays."
        )
    tpl = (arr.shape, arr.dtype.name, arr.tobytes("C"))
    return msgpack.packb(tpl, use_bin_type=True)


def _ndarray_from_bytes(data: bytes) -> np.ndarray:
    """Load ndarray from simple msgpack encoding."""
    shape, dtype_name, buffer = msgpack.unpackb(data, raw=True)
    return np.frombuffer(
        buffer, dtype=np.dtype(dtype_name), count=-1, offset=0
    ).reshape(shape, order="C")
