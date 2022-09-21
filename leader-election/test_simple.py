import json

from pycape import Cape, FunctionRef

data = {"node_list": [5001, 5002, 5003]}
user_data = bytes(json.dumps(data), "utf8")
client = Cape()
# result = client.run(
#     FunctionRef(
#         id="YSuZwnotrM66hAiC3GhcJK",
#         checksum="80a3a1db46da61450f9b7493214d3b4c6a0a4504a1283c9ad1516b381f3698ba",
#     ),
#     user_data,
# )
# print(result)
key = """-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAnV8eokFPI6Nx+MJ+4iBG
+5Ms1W2qadbuKf8pFL3s8aEsLp4MSH7809b8nsLhgxtbs+nBh1CNaoOxkxY2bhhH
Kv8gmnkP0kuH0dRKz9Egf0R3CV+vA+lnRnZThoz8GeouXCmRoYT/crfIjNq4FnKb
6MMsGOdT1aS/UUYO5kvtz7/gTXE79RfQURWSt6oI3hBJQg/629ju1YVplXIIKQVy
ZqwSaihY6htW9HS4P9LPEsFOIPFvt0+ogwcYfub6+nBlBO8/Ud1TJCl1o9MgkMf5
YVjAEnY8IjxuJjGI6f53foLSd/Suou8BO+fCke1p82Bv7fjpBlwz3lvDmqzzcmF5
6L8Ru/nXD6vxBp34MkOwNIKrZWTxnLbgGKpk1k0T+2Gp2vahDeqHn/BGmtBREzbc
Db2oNpnikBf0eVJAEGM8J/pwQXUt2afRpSJ+PDT7Nh3m199NghUSHbEzzAvoib9B
VrlYJvrvIldBUMpboXFFn0HOku4OcdpCDuyauklCMFnK0YnqOUzXBokXQlkRqO5H
GxSN8obYmBWRDOLkNx3wAhhDkrR+sxFpqk+rMFPjYx3khBRW1FuMDDsKTYbUrRHW
I0oRt17NpJgBlRQWEJfS0rYTRpj5IAK6pBJR8WR08WpoOTW03cutEz5SfIonJAFA
Phnoqp6wsB5/7JTzciA+qAMCAwEAAQ==
-----END PUBLIC KEY-----"""

key = str.encode(key)


encrypted  = client.encrypt(str.encode("what is this"))
print(encrypted)

