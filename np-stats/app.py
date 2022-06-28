import json
from os import lseek
import numpy as np

def cape_handler(x):
    data  =  np.array([1, 2, 3 , 4])
    mean = np.mean(data)
    res_json  = json.dumps(mean.tolist()).encode()
    return res_json
