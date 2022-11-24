import os
import pathlib
import json

from pycape import Cape
from pycape import FunctionRef

function_json = os.environ.get("FUNCTION_JSON", "seek.json")
function_json = pathlib.Path(__file__).parent.absolute() / function_json
function_ref = FunctionRef.from_json(function_json)

data1 = {"latitude":"43.795315","longitude":"-79.3240118"}
user_data1 = bytes(json.dumps(data1), "utf8")
data2 = {"latitude":"43.7939503","longitude":"-79.3224387"}
user_data2 = bytes(json.dumps(data2), "utf8")
cape = Cape()
cape.connect(function_ref)

result = cape.invoke(user_data1)
print(result)
result = cape.invoke(user_data2)
print(result)
cape.close()
