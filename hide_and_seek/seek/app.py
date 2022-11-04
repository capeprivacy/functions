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
    with open(path, 'w', encoding='utf-8') as f:
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
        user_loco = (float(user_input['latitude']), float(user_input['longitude']))
        secret_loco = (float(secret['latitude']), float(secret['longitude'] ))
        distance = GD(secret_loco,user_loco).m
        if distance < 10:
            ret = f"Congrats you found the treasure!"
        elif distance < 10000:
            ret = f"Getting closer! still {distance} meters away"
        else:
            ret = f"Not even close!"
        return ret

if __name__ == '__main__':
    # from geopy.distance import geodesic as GD
    # For the specified locations, load their latitude and longitude data.
    Abuja =(9.072264 , 7.491302)
    Dakar =(14.716677 , -17.467686)
    #Finally, print the distance between the two sites in kilometers.
    # print("The distance between Abuja and Dakar is: ", GD(Abuja,Dakar).km)
    user_data = '{"latitude":"44.646461","longitude":"-63.593312"}'
    # first = json.loads(user_data)
    print(cape_handler(user_data))
    print(cape_handler(user_data))


