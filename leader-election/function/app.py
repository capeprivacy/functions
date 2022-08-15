import json
from unicodedata import name

from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


# Function needs to check if the coordinates match the one that was provided.
def cape_handler(arg):
    user_input = json.loads(arg)

    if "node_list" not in user_input:
        raise Exception("node list is missing")

    nodes = user_input.get("node_list")

    nodes.sort()

    message = str(nodes[-1])
    digest = SHA256.new()
    digest.update(message.encode("utf-8"))
    print("digest", digest)

    private_key = RSA.importKey(open("private.pem").read())
    signer = PKCS1_v1_5.new(private_key)
    sig = signer.sign(digest)
    return_val = {}
    return_val["message"] = message
    return_val["signature"] = sig.hex()
    print("digest in hex", sig.hex())
    return json.dumps(return_val)


if __name__ == "__main__":
    public_key = RSA.importKey(open("public.pem").read())
    verifier = PKCS1_v1_5.new(public_key)
    # verified = verifier.verify(digest, sig)
    data = {"node_list": [5001, 5002, 5003]}
    user_data = bytes(json.dumps(data), "utf8")
    output = cape_handler(user_data)
    leader = json.loads(output)
    message = leader["message"].encode("utf-8")
    signature = bytes.fromhex(leader["signature"])
    # bytes.fromhex
    print("signature", signature)
    digest = SHA256.new()
    digest.update(message)
    verify = verifier.verify(digest, signature)
    if verify:
        print("Successfully verified message")
    else:
        print("FAILED")
