from urllib import response
import requests
from lark import Lark, Transformer

class ParseDoc:
    def __init__(self) -> None:
        pass
    def readDoc(self):
        s = requests.Session()
        response = s.get('https://image.pdflibr.com/crawler/blog/tencent_cloud_ip_range.txt')
        # response => print status: 200 OK
        # response.text => print text (Binary Response content)
        # Display current encoding mathod
        print(response.encoding)
        response.encoding = 'utf-8'
        docText = response.text
        return docText

    def larkText(self):
        lark_text = r"""
        start : value
        value : _NL? row+ seperator summary
                |ip_1
                |ip_2
                |map

        row : ip_1 + _WHITESPACE + ip_2 + map + _NL
        NAME : /[\u4e00-\u9fa5]/
        WORD: NAME*/\w/*NAME*/\w/*/\./*/\w/*/\./*/\(/*NAME*/\)/*NAME*/\w/*NAME*
        LOCATION: _WHITESPACE + WORD
        map : LOCATION+
        ip_1 : /([0-9]{1,3}\.*){4}/
        ip_2 : /([0-9]{1,3}\.*){4}/
        HYPER : /\-/+

        seperator : HYPER + _NL

        summary : SUM +  _WHITESPACE + MATCH + _NL
        SUM_NAME : NAME+ 
        SUM_NUM : /\d/+
        SEP: /\：//\s/*
        SUM : SUM_NAME + SEP + _WHITESPACE + SUM_NUM
        MATCH_NAME : NAME+
        MATCH_NUM : /\d/+
        MATCH : MATCH_NAME + SEP + _WHITESPACE + MATCH_NUM 
        
         

        %import common.NEWLINE -> _NL
        %import common.WS_INLINE -> _WHITESPACE
        %import common.WS

        %ignore WS
        %ignore _WHITESPACE
        
        """
        return lark_text

    
    def parseDoc(self):
        docText = self.readDoc()
        print(docText)
        lark_doc = self.larkText()
        parser = Lark(lark_doc, start = "value")
        print("Start parsing ... ")
        result = parser.parse(docText)
        print(result.pretty())
        print("Start transforming ... ")

        transformer = TransformTree().transform(result)
        # finalText = transformer.transform(result)

        print(transformer)

class TransformTree(Transformer):
    def row(self,rows):
        # [row1 : dict{IP_1:_ip1, IP_2:_ip2, Map: _map}, row2, ...]
        l2 = list(rows)
        
        return {"ip1" : l2[0], "ip2": l2[1], "loc": l2[2]}
        
    

if __name__ == '__main__':
    par = ParseDoc()
    par.parseDoc()
