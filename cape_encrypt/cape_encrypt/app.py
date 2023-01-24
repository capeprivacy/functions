from cape_encrypt.cape_encrypt import decrypt
import json

# expects a json array of cape encrypted data
def cape_handler(encrypted_data):
    encrypted_data = json.loads(encrypted_data)

    out = []
    for item in encrypted_data:
        out.append(decrypt(bytes(item, 'ascii')))

    return out
