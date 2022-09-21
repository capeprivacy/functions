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
edges = {}
edges["uuid"] = str(5001)
edges["generation"] =1
edges["node_list"] = [5001, 5002]
edge_info = json.dumps(edges)
edge_info = bytes(edge_info, "utf8")
# string_encoded_encrypted_edge_info = encrypted.decode('utf-8')
# print(f"encrypted value: {string_encoded_encrypted_edge_info}")

encrypted  = client.encrypt(edge_info)
print(encrypted)

