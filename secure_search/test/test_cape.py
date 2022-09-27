from pycape import Cape
from pycape import FunctionRef
import json
import hybrid_pke

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

# Cape search function info
function_id = "ZRtuUk7zcijjVy5F7uE9r7"
function_checksum = "ec8dce345048468ad2697e79d2a44086b6cf499f322c3e00bd91ee5b5097ede9"
f = FunctionRef(function_id, function_checksum)

# connect to Cape function
client = Cape()
client.connect(function_id)

# TEST 1: false for 172.19.0.4; true for 1.2.3.4
resp_ciphertext = client.invoke(b'[{"protocol": "tcp", "hosts": "1.2.3.4", "state": "ESTABLISHED"}]')

# TEST 2: false for both IPs
#resp_ciphertext = client.invoke(b'[{"protocol": "tcp", "hosts": "0.0.0.0", "state": "ESTABLISHED"}]')

print(f'\nResponse from Cape (ciphertext):')
print(resp_ciphertext)

plaintext = decrypt(resp_ciphertext)
print(f'\nDecrypted response:')
print(plaintext)

client.close()