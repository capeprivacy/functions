from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key_bytes = key.export_key('PEM')
public_key_bytes = key.publickey().exportKey('PEM')


with open("private.pem", "wb") as f:
    f.write(private_key_bytes)
with open("public.pem", "wb") as f:
    f.write(public_key_bytes)
