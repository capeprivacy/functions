import json
import hybrid_pke


def encrypt(input):
    hpke = hybrid_pke.default()
    with open('public_keyset.bin', 'rb') as key_bytes:
        key = key_bytes.read()
        info = b""
        aad = b""
        encap, ciphertext = hpke.seal(key, info, aad, input)

    return encap + ciphertext

def decrypt(ciphertext):
    # 32 bytes (KEM-derived public key) + 45 bytes (ciphertext of ptxt) = 77 bytes
    encap = ciphertext[0:32]
    ciphertext = ciphertext[32:]
    hpke = hybrid_pke.default()
    with open('private_keyset.bin', 'rb') as key_bytes:
        key = key_bytes.read()
        info = b""
        aad = b""
        plaintext = hpke.open(encap, key, info, aad, ciphertext)

    return plaintext

data = b'Hello World!'
ciphertext = encrypt(data)
print(f'\nCiphertext:')
print(ciphertext)

plaintext = decrypt(ciphertext)
print(f'\nDecrypted data:')
print(plaintext)