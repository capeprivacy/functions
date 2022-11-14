import json

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


def cape_handler(arg):
    user_input = json.loads(arg)

    # use file cache instead if the target location has been provided
    secret = open_secret()
    if secret == None:
        # Store the current input as secret
        store_secret(user_input)
    else:
        # Execute password retrieval logic, secret already exists. 
        name = user_input["account"]
        tag = user_input["tag"]
        # If the user wants to return the entire secret, return it in JSON format.
        if tag == "all":
            ret = f"Congrats you found the treasure!"
        elif distance < 10000:
            ret = f"Getting closer! still {distance} meters away"
        else:
            ret = f"Not even close!"
        return ret


if __name__ == "__main__":
    user_data = '{"latitude":"44.646461","longitude":"-63.593312"}'
    print(cape_handler(user_data))
    print(cape_handler(user_data))
