import math
import string
from unicodedata import name
import json
import geopy
from geopy.distance import geodesic as GD


FILE_PATH = "./secret.json"


def open_secret(path=FILE_PATH):
    with open(path) as f:
        try:
            data = json.load(f)
        except Exception:
            return None
    return data


def store_secret(data, path=FILE_PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# Function needs to check if the coordinates match the one that was provided.
def cape_handler(arg):
    user_input = json.loads(arg)

    # use file cache instead
    secret = open_secret()
    if secret == None:
        # Store the current input as secret
        store_secret(user_input)
    else:
        # Calculate the difference between the user secret and the current input.
        user_loco = (float(user_input["latitude"]), float(user_input["longitude"]))
        secret_loco = (float(secret["latitude"]), float(secret["longitude"]))
        distance = GD(secret_loco, user_loco).m
        if distance < 100:
            ret = f"Congrats you found the treasure!"
        elif distance < 10000:
            ret = f"Getting closer! still {distance} meters away"
        else:
            ret = f"Not even close! still {distance} meters away"
        return ret
