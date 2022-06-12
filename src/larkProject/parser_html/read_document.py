from urllib import response
import requests
from lark import Lark

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
        row : IP_1 + _WHITESPACE + IP_2 + MAP + _NL
        NAME : /[\u4e00-\u9fa5]/
        WORD: NAME*/\w/*NAME*/\w/*/\./*/\w/*/\./*/\(/*NAME*/\)/*NAME*/\w/*NAME*
        LOCATION: _WHITESPACE + WORD
        MAP : LOCATION+
        IP_1 : /([0-9]{1,3}\.*){4}/
        IP_2 : /([0-9]{1,3}\.*){4}/
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
        
        """
        return lark_text

    def transformDoc(self):
        pass

    def parseDoc(self):
        docText = self.readDoc()
        print(docText)
        lark_doc = self.larkText()
        parser = Lark(lark_doc, start = "value")
        print("Start parsing ... ")
        result = parser.parse(docText)
        print(result)
        print("Start transforming ... ")

        transformer = self.transformDoc()
        finalText = transformer.transform(result)

        print(finalText)

if __name__ == '__main__':
    par = ParseDoc()
    par.parseDoc()
