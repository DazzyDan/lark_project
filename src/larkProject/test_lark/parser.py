from lark import Lark
from lark_text import LARKJSON
from transfomer import TreeToJson
import json
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "text.json")
f = open(path)
json_text = json.load(f)
json_file = json.dumps(json_text)
parser = Lark(LARKJSON, start = "value")

result = parser.parse(json_file)

print(TreeToJson().transform(result))
