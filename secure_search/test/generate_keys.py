import json
import hybrid_pke


def generate_keypair():
    hpke = hybrid_pke.default()
    secret_key_r, public_key_r = hpke.generate_key_pair()  # receiver keys, pre-generated

    # include this with your function, and use it to encrypt responses
    with open('private_keyset.bin', 'wb') as f:
        f.write(secret_key_r)

    # keep this safe; it's used to decrypt
    with open('public_keyset.bin', 'wb') as f:
        f.write(public_key_r)

generate_keypair()