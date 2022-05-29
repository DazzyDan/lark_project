from lark import Lark

text_parser = Lark(
    r"""
        ?start: value

        ?value: dict     
            | list
            | string
            | SIGNED_NUMBER     -> number
            | "true"            -> true
            | "false"           -> false
            | "null"            -> null

    dict : "{" [pair ("," pair)*] "}"
    list : "[" [value ("," value)*] "]"
    pair : string ":" value
    string: ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    
    %ignore WS
    """,
    start="value",
)

text = """
        {
            "empty_object" : {},
            "empty_array"  : [],
            "booleans"     : { "YES" : true, "NO" : false },
            "numbers"      : [ 0, 1, -2, 3.3, 4.4e5, 6.6e-7 ],
            "strings"      : [ "This", [ "And" , "That", "And a \\"b" ] ],
            "nothing"      : null
        }
        """
print("Start parsering ... ")
tree = text_parser.parse(text)
print(tree.pretty())
