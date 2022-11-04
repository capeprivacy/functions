import os
import pathlib
import json

from pycape import Cape
from pycape import FunctionRef

function_json = os.environ.get("FUNCTION_JSON", "seek.json")
function_json = pathlib.Path(__file__).parent.absolute() / function_json
function_ref = FunctionRef.from_json(function_json)

data = {"latitude":"44.646461","longitude":"-63.593312"}
user_data = bytes(json.dumps(data), "utf8")
cape = Cape()
cape.connect(function_ref)

result = cape.invoke(user_data)
print(result)
result = cape.invoke(user_data)
print(result)
cape.close()
