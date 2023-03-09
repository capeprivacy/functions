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


def filter_by_identifier(vault, key, value):
    ret = []
    for i in vault:
        if i[key] == value:
            ret.append(i)
    return ret


def cape_handler(arg):
    # Try to see if secret exists, if it does, process user input as string an non-json.
    secret = open_secret()
    if secret == None:
        try:
            user_input = json.loads(arg)
            # Cache the secret in enclave storage
            store_secret(user_input)

        except TypeError:
            raise TypeError(
                "expected secrets vault to passed in first in json format [{name, tag, username, password}]"
            )

    else:
        if type(arg) is not str:
            raise TypeError(f"expected input to be string, got {type(arg)}")

        if arg == "all":
            return json.dumps(secret, indent=4)

        # Try to split the string to get key, value.
        identifier = arg.split(":")
        if len(identifier) != 2:
            raise ValueError(
                f"expected input of the form `name:<identifier>`, or `tag:<identifier>`, got: {arg}"
            )
        cmd = identifier[0].strip()

        if cmd == "name":
            # iterage over secret and find a name match
            return json.dumps(
                filter_by_identifier(secret, "name", identifier[1].strip()), indent=4
            )

        elif cmd == "tag":
            return json.dumps(
                filter_by_identifier(secret, "tag", identifier[1].strip()), indent=4
            )

        else:
            return ValueError(
                f"unknown command: {identifier[0]}, please use `all`, `name:<identifier>`, or `tag:<identifier>`"
            )


if __name__ == "__main__":
    vault = [
        {"name": "aws", "tag": "grocery", "username": "bob", "password": "B013Pass"},
        {"name": "shop", "tag": "grocery", "username": "bob", "password": "B013Pass"},
    ]
    serialized = json.dumps(vault)

    # print(cape_handler(serialized))
    print(cape_handler("all"))

    print(cape_handler("name: aws"))
    print(cape_handler("tag: grocery"))
