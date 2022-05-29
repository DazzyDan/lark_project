LARKJSON = r"""
start : value
value : dict
        |list
        | string

dict : "{" [ pair ("," pair)*] "}"  
list : "[" [value ("," value)*] "]"
pair : string ":" value
string : ESCAPED_STRING

%import common.ESCAPED_STRING
%import common.WS

%ignore WS
"""
