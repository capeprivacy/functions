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

client = Cape(url="wss://enclave.capeprivacy.com")
function_id = "Jzv8Ksmqdf9n6za5s6qWiD"
function_hash = "a50e20e91434e66fe0aa576daf5f3366855bcb79fcb07419efe71c63ba995263"
f = FunctionRef(function_id, function_hash)

# false for 172.19.0.4; true for 1.2.3.4
resp_ciphertext = client.run(f, b'[{"protocol": "tcp", "hosts": "1.2.3.4:29092", "state": "ESTABLISHED"}]')

# false for both IPs
#resp_ciphertext = client.run(f, b'[{"protocol": "tcp", "hosts": "0.0.0.0:29092", "state": "ESTABLISHED"}]')

print(f'\nResponse from Cape (ciphertext):')
print(resp_ciphertext)

plaintext = decrypt(resp_ciphertext)
print(f'\nDecrypted response:')
print(plaintext)