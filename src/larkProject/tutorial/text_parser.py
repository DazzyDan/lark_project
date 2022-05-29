from lark import Lark
from json_transfomer import MyTransformer, TreeToJson

text_parser = Lark(
    r"""
?value: dict
          | list
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : string ":" value

    string : ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS
""",
    start="value",
)

text = '{"key": ["item0", "item1", 3.14]}'
tree = text_parser.parse(text)
print( text_parser.parse(text).pretty() )
print(MyTransformer().transform(tree))
print(TreeToJson().transform(tree))