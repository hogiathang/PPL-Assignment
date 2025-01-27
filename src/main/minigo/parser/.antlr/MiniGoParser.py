# Generated from d:/HK242/PPL/Assignment/B1/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,62,5,2,0,7,0,1,0,1,0,1,0,0,0,1,0,0,0,3,0,2,1,0,0,0,2,3,5,0,0,
        1,3,1,1,0,0,0,0
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'true'", "'false'", 
                     "'nil'", "'const'", "'var'", "'continue'", "'break'", 
                     "'range'", "'='", "':='", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'&&'", "'||'", "'!'", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "TRUE", "FALSE", "NIL", "CONST", "VAR", 
                      "CONTINUE", "BREAK", "RANGE", "ASSIGN", "DECLARE", 
                      "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQ", "NEQ", 
                      "LT", "LEQ", "GT", "GEQ", "AND", "OR", "NOT", "PLUS_ASSIGN", 
                      "MINUS_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "DOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
                      "RBRACKET", "COMMA", "SEMI", "COLON", "IDENTIFIER", 
                      "INT_LIT", "FLOAT_LIT", "STRING_LIT", "BOOL_LIT", 
                      "BLOCK_COMMENT", "LINE_COMMENT", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    TRUE=13
    FALSE=14
    NIL=15
    CONST=16
    VAR=17
    CONTINUE=18
    BREAK=19
    RANGE=20
    ASSIGN=21
    DECLARE=22
    PLUS=23
    MINUS=24
    MUL=25
    DIV=26
    MOD=27
    EQ=28
    NEQ=29
    LT=30
    LEQ=31
    GT=32
    GEQ=33
    AND=34
    OR=35
    NOT=36
    PLUS_ASSIGN=37
    MINUS_ASSIGN=38
    MUL_ASSIGN=39
    DIV_ASSIGN=40
    MOD_ASSIGN=41
    DOT=42
    LPAREN=43
    RPAREN=44
    LBRACE=45
    RBRACE=46
    LBRACKET=47
    RBRACKET=48
    COMMA=49
    SEMI=50
    COLON=51
    IDENTIFIER=52
    INT_LIT=53
    FLOAT_LIT=54
    STRING_LIT=55
    BOOL_LIT=56
    BLOCK_COMMENT=57
    LINE_COMMENT=58
    WS=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61
    ERROR_CHAR=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





