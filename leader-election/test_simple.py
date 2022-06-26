import json

from pycape import Cape, FunctionRef

data = {"node_list": [5001, 5002, 5003]}
user_data = bytes(json.dumps(data), "utf8")
client = Cape(url="wss://hackathon.capeprivacy.com")
result = client.run(
    function_ref=FunctionRef(
        function_id="HDnKiSskQhYjNXyHFfoRVX",
        function_hash="bbd51f211e9683a79cbb4e413bc438f489bc08d82ca692073d64286017894c53",
    ),
    input=user_data,
)
print(result)
