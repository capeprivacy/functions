import json
import hybrid_pke

# "selectors" are the strings to search for (you can customize these)
selectors_a = "172.19.0.4"
selectors_b = "1.2.3.4"

# Expects a string representation of a list of json objects like:
# [{"protocol": "tcp", "hosts": "172.18.0.4:29092", "state": "ESTABLISHED"}, {...}]
# Each json object MUST have a "hosts" element.
# Uses a bundled public key to decrypt results (named public_keyset.json).
def cape_handler(input):
    as_str = input.decode('utf-8')
    req = json.loads(as_str)

    def encrypt(input):
        hpke = hybrid_pke.default()
        with open('public_keyset.bin', 'rb') as key_bytes:
            key = key_bytes.read()
            info = b""
            aad = b""
            encap, ciphertext = hpke.seal(key, info, aad, bytes(json.dumps(input), 'utf-8'))

        return encap + ciphertext

    def find(input):
        a = False
        b = False
        if selectors_a in input["hosts"]:
            a = True
        if selectors_b in input["hosts"]:
            b = True

        return { selectors_a: a, selectors_b: b }

    finds = list(map(find, req))

    # return results in plaintext
    # return finds

    # alternatively, use this to encrypt the results with the supplied public key
    return encrypt(finds)