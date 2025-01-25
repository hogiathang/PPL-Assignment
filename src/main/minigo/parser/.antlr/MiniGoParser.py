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
        4,1,62,441,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        1,0,4,0,82,8,0,11,0,12,0,83,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,3,3,
        94,8,3,1,4,1,4,1,4,1,4,1,4,3,4,101,8,4,1,5,1,5,1,5,1,5,5,5,107,8,
        5,10,5,12,5,110,9,5,1,5,3,5,113,8,5,1,5,1,5,3,5,117,8,5,1,5,1,5,
        3,5,121,8,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,129,8,6,1,6,1,6,3,6,133,
        8,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,158,8,9,1,9,1,9,1,9,1,10,1,10,
        3,10,165,8,10,1,11,1,11,1,11,5,11,170,8,11,10,11,12,11,173,9,11,
        1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,14,1,14,1,14,1,14,5,14,192,8,14,10,14,12,14,195,9,14,1,14,1,14,
        1,15,1,15,1,15,5,15,202,8,15,10,15,12,15,205,9,15,1,16,1,16,1,16,
        3,16,210,8,16,1,16,1,16,1,17,1,17,1,17,5,17,217,8,17,10,17,12,17,
        220,9,17,1,18,1,18,1,18,1,19,1,19,1,19,1,19,3,19,229,8,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,5,19,246,8,19,10,19,12,19,249,9,19,1,20,1,20,1,20,1,20,3,20,255,
        8,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,264,8,20,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,276,8,21,1,22,1,22,
        1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,5,23,288,8,23,10,23,12,23,
        291,9,23,1,23,1,23,1,23,1,23,1,23,1,23,5,23,299,8,23,10,23,12,23,
        302,9,23,1,23,1,23,3,23,306,8,23,1,24,1,24,1,24,1,24,1,24,1,24,3,
        24,314,8,24,5,24,316,8,24,10,24,12,24,319,9,24,1,24,1,24,1,25,1,
        25,1,25,1,25,3,25,327,8,25,1,25,1,25,1,25,3,25,332,8,25,1,25,1,25,
        1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,5,27,350,8,27,10,27,12,27,353,9,27,1,27,1,27,3,27,357,8,27,
        1,27,1,27,1,28,1,28,1,28,3,28,364,8,28,1,28,1,28,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,3,29,375,8,29,1,30,1,30,1,30,1,30,1,31,1,31,
        1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,
        1,34,1,35,1,35,1,35,1,36,1,36,1,36,3,36,403,8,36,1,36,1,36,1,36,
        1,36,5,36,409,8,36,10,36,12,36,412,9,36,3,36,414,8,36,1,36,1,36,
        1,36,1,37,1,37,3,37,421,8,37,1,37,1,37,1,38,1,38,5,38,427,8,38,10,
        38,12,38,430,9,38,1,38,1,38,1,39,1,39,1,39,4,39,437,8,39,11,39,12,
        39,438,1,39,0,1,38,40,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,
        76,78,0,9,2,0,9,9,12,14,2,1,52,52,56,56,2,0,22,22,34,34,1,0,26,31,
        1,0,21,22,1,0,23,25,2,0,8,9,13,14,1,0,36,41,2,0,20,20,44,44,458,
        0,81,1,0,0,0,2,87,1,0,0,0,4,89,1,0,0,0,6,93,1,0,0,0,8,100,1,0,0,
        0,10,102,1,0,0,0,12,124,1,0,0,0,14,137,1,0,0,0,16,141,1,0,0,0,18,
        147,1,0,0,0,20,164,1,0,0,0,22,166,1,0,0,0,24,177,1,0,0,0,26,181,
        1,0,0,0,28,187,1,0,0,0,30,198,1,0,0,0,32,206,1,0,0,0,34,213,1,0,
        0,0,36,221,1,0,0,0,38,228,1,0,0,0,40,263,1,0,0,0,42,275,1,0,0,0,
        44,277,1,0,0,0,46,305,1,0,0,0,48,307,1,0,0,0,50,322,1,0,0,0,52,335,
        1,0,0,0,54,337,1,0,0,0,56,360,1,0,0,0,58,374,1,0,0,0,60,376,1,0,
        0,0,62,380,1,0,0,0,64,382,1,0,0,0,66,386,1,0,0,0,68,393,1,0,0,0,
        70,396,1,0,0,0,72,399,1,0,0,0,74,418,1,0,0,0,76,424,1,0,0,0,78,436,
        1,0,0,0,80,82,3,6,3,0,81,80,1,0,0,0,82,83,1,0,0,0,83,81,1,0,0,0,
        83,84,1,0,0,0,84,85,1,0,0,0,85,86,5,0,0,1,86,1,1,0,0,0,87,88,7,0,
        0,0,88,3,1,0,0,0,89,90,7,1,0,0,90,5,1,0,0,0,91,94,3,8,4,0,92,94,
        3,42,21,0,93,91,1,0,0,0,93,92,1,0,0,0,94,7,1,0,0,0,95,101,3,10,5,
        0,96,101,3,12,6,0,97,101,3,14,7,0,98,101,3,16,8,0,99,101,3,18,9,
        0,100,95,1,0,0,0,100,96,1,0,0,0,100,97,1,0,0,0,100,98,1,0,0,0,100,
        99,1,0,0,0,101,9,1,0,0,0,102,103,5,11,0,0,103,108,5,20,0,0,104,105,
        5,51,0,0,105,107,5,20,0,0,106,104,1,0,0,0,107,110,1,0,0,0,108,106,
        1,0,0,0,108,109,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,111,113,
        3,78,39,0,112,111,1,0,0,0,112,113,1,0,0,0,113,120,1,0,0,0,114,121,
        3,2,1,0,115,117,3,2,1,0,116,115,1,0,0,0,116,117,1,0,0,0,117,118,
        1,0,0,0,118,119,5,35,0,0,119,121,3,38,19,0,120,114,1,0,0,0,120,116,
        1,0,0,0,121,122,1,0,0,0,122,123,3,4,2,0,123,11,1,0,0,0,124,125,5,
        5,0,0,125,126,5,20,0,0,126,128,5,45,0,0,127,129,3,34,17,0,128,127,
        1,0,0,0,128,129,1,0,0,0,129,130,1,0,0,0,130,132,5,46,0,0,131,133,
        3,2,1,0,132,131,1,0,0,0,132,133,1,0,0,0,133,134,1,0,0,0,134,135,
        3,76,38,0,135,136,3,4,2,0,136,13,1,0,0,0,137,138,5,6,0,0,138,139,
        5,20,0,0,139,140,3,20,10,0,140,15,1,0,0,0,141,142,5,10,0,0,142,143,
        5,20,0,0,143,144,5,35,0,0,144,145,3,38,19,0,145,146,3,4,2,0,146,
        17,1,0,0,0,147,148,5,5,0,0,148,149,5,45,0,0,149,150,5,20,0,0,150,
        151,5,20,0,0,151,152,5,46,0,0,152,153,5,20,0,0,153,154,5,45,0,0,
        154,155,3,34,17,0,155,157,5,46,0,0,156,158,3,2,1,0,157,156,1,0,0,
        0,157,158,1,0,0,0,158,159,1,0,0,0,159,160,3,76,38,0,160,161,3,4,
        2,0,161,19,1,0,0,0,162,165,3,22,11,0,163,165,3,26,13,0,164,162,1,
        0,0,0,164,163,1,0,0,0,165,21,1,0,0,0,166,167,5,7,0,0,167,171,5,47,
        0,0,168,170,3,24,12,0,169,168,1,0,0,0,170,173,1,0,0,0,171,169,1,
        0,0,0,171,172,1,0,0,0,172,174,1,0,0,0,173,171,1,0,0,0,174,175,5,
        48,0,0,175,176,3,4,2,0,176,23,1,0,0,0,177,178,5,20,0,0,178,179,3,
        2,1,0,179,180,3,4,2,0,180,25,1,0,0,0,181,182,5,8,0,0,182,183,5,47,
        0,0,183,184,3,32,16,0,184,185,5,48,0,0,185,186,3,4,2,0,186,27,1,
        0,0,0,187,193,5,45,0,0,188,189,3,30,15,0,189,190,3,2,1,0,190,192,
        1,0,0,0,191,188,1,0,0,0,192,195,1,0,0,0,193,191,1,0,0,0,193,194,
        1,0,0,0,194,196,1,0,0,0,195,193,1,0,0,0,196,197,5,46,0,0,197,29,
        1,0,0,0,198,203,5,20,0,0,199,200,5,51,0,0,200,202,5,20,0,0,201,199,
        1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,31,1,
        0,0,0,205,203,1,0,0,0,206,207,5,20,0,0,207,209,3,28,14,0,208,210,
        3,2,1,0,209,208,1,0,0,0,209,210,1,0,0,0,210,211,1,0,0,0,211,212,
        3,4,2,0,212,33,1,0,0,0,213,218,3,36,18,0,214,215,5,51,0,0,215,217,
        3,36,18,0,216,214,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,
        1,0,0,0,219,35,1,0,0,0,220,218,1,0,0,0,221,222,5,20,0,0,222,223,
        3,2,1,0,223,37,1,0,0,0,224,225,6,19,-1,0,225,226,7,2,0,0,226,229,
        3,40,20,0,227,229,3,40,20,0,228,224,1,0,0,0,228,227,1,0,0,0,229,
        247,1,0,0,0,230,231,10,7,0,0,231,232,5,33,0,0,232,246,3,40,20,0,
        233,234,10,6,0,0,234,235,5,32,0,0,235,246,3,40,20,0,236,237,10,5,
        0,0,237,238,7,3,0,0,238,246,3,40,20,0,239,240,10,4,0,0,240,241,7,
        4,0,0,241,246,3,40,20,0,242,243,10,3,0,0,243,244,7,5,0,0,244,246,
        3,40,20,0,245,230,1,0,0,0,245,233,1,0,0,0,245,236,1,0,0,0,245,239,
        1,0,0,0,245,242,1,0,0,0,246,249,1,0,0,0,247,245,1,0,0,0,247,248,
        1,0,0,0,248,39,1,0,0,0,249,247,1,0,0,0,250,254,5,20,0,0,251,255,
        3,78,39,0,252,253,5,42,0,0,253,255,5,20,0,0,254,251,1,0,0,0,254,
        252,1,0,0,0,254,255,1,0,0,0,255,264,1,0,0,0,256,264,5,53,0,0,257,
        264,5,54,0,0,258,264,5,55,0,0,259,260,5,45,0,0,260,261,3,38,19,0,
        261,262,5,46,0,0,262,264,1,0,0,0,263,250,1,0,0,0,263,256,1,0,0,0,
        263,257,1,0,0,0,263,258,1,0,0,0,263,259,1,0,0,0,264,41,1,0,0,0,265,
        276,3,50,25,0,266,276,3,54,27,0,267,276,3,56,28,0,268,276,3,68,34,
        0,269,276,3,70,35,0,270,276,3,72,36,0,271,276,3,74,37,0,272,276,
        3,44,22,0,273,276,3,10,5,0,274,276,3,16,8,0,275,265,1,0,0,0,275,
        266,1,0,0,0,275,267,1,0,0,0,275,268,1,0,0,0,275,269,1,0,0,0,275,
        270,1,0,0,0,275,271,1,0,0,0,275,272,1,0,0,0,275,273,1,0,0,0,275,
        274,1,0,0,0,276,43,1,0,0,0,277,278,5,20,0,0,278,279,5,36,0,0,279,
        280,3,78,39,0,280,281,7,6,0,0,281,282,3,46,23,0,282,45,1,0,0,0,283,
        284,5,47,0,0,284,289,3,46,23,0,285,286,5,51,0,0,286,288,3,46,23,
        0,287,285,1,0,0,0,288,291,1,0,0,0,289,287,1,0,0,0,289,290,1,0,0,
        0,290,292,1,0,0,0,291,289,1,0,0,0,292,293,5,48,0,0,293,306,1,0,0,
        0,294,295,5,47,0,0,295,300,3,38,19,0,296,297,5,51,0,0,297,299,3,
        38,19,0,298,296,1,0,0,0,299,302,1,0,0,0,300,298,1,0,0,0,300,301,
        1,0,0,0,301,303,1,0,0,0,302,300,1,0,0,0,303,304,5,48,0,0,304,306,
        1,0,0,0,305,283,1,0,0,0,305,294,1,0,0,0,306,47,1,0,0,0,307,308,5,
        20,0,0,308,317,5,47,0,0,309,310,5,20,0,0,310,311,5,43,0,0,311,313,
        3,38,19,0,312,314,5,51,0,0,313,312,1,0,0,0,313,314,1,0,0,0,314,316,
        1,0,0,0,315,309,1,0,0,0,316,319,1,0,0,0,317,315,1,0,0,0,317,318,
        1,0,0,0,318,320,1,0,0,0,319,317,1,0,0,0,320,321,5,48,0,0,321,49,
        1,0,0,0,322,326,5,20,0,0,323,327,3,78,39,0,324,325,5,42,0,0,325,
        327,5,20,0,0,326,323,1,0,0,0,326,324,1,0,0,0,326,327,1,0,0,0,327,
        328,1,0,0,0,328,331,3,52,26,0,329,332,3,38,19,0,330,332,3,48,24,
        0,331,329,1,0,0,0,331,330,1,0,0,0,332,333,1,0,0,0,333,334,3,4,2,
        0,334,51,1,0,0,0,335,336,7,7,0,0,336,53,1,0,0,0,337,338,5,1,0,0,
        338,339,5,45,0,0,339,340,3,38,19,0,340,341,5,46,0,0,341,351,3,76,
        38,0,342,343,5,2,0,0,343,344,5,1,0,0,344,345,5,45,0,0,345,346,3,
        38,19,0,346,347,5,46,0,0,347,348,3,76,38,0,348,350,1,0,0,0,349,342,
        1,0,0,0,350,353,1,0,0,0,351,349,1,0,0,0,351,352,1,0,0,0,352,356,
        1,0,0,0,353,351,1,0,0,0,354,355,5,2,0,0,355,357,3,76,38,0,356,354,
        1,0,0,0,356,357,1,0,0,0,357,358,1,0,0,0,358,359,3,4,2,0,359,55,1,
        0,0,0,360,363,5,3,0,0,361,364,3,58,29,0,362,364,3,66,33,0,363,361,
        1,0,0,0,363,362,1,0,0,0,364,365,1,0,0,0,365,366,3,76,38,0,366,57,
        1,0,0,0,367,375,3,62,31,0,368,369,3,60,30,0,369,370,5,52,0,0,370,
        371,3,62,31,0,371,372,5,52,0,0,372,373,3,64,32,0,373,375,1,0,0,0,
        374,367,1,0,0,0,374,368,1,0,0,0,375,59,1,0,0,0,376,377,5,20,0,0,
        377,378,5,36,0,0,378,379,3,38,19,0,379,61,1,0,0,0,380,381,3,38,19,
        0,381,63,1,0,0,0,382,383,5,20,0,0,383,384,3,52,26,0,384,385,3,38,
        19,0,385,65,1,0,0,0,386,387,7,8,0,0,387,388,5,51,0,0,388,389,5,20,
        0,0,389,390,5,36,0,0,390,391,5,17,0,0,391,392,5,20,0,0,392,67,1,
        0,0,0,393,394,5,16,0,0,394,395,3,4,2,0,395,69,1,0,0,0,396,397,5,
        15,0,0,397,398,3,4,2,0,398,71,1,0,0,0,399,402,5,20,0,0,400,401,5,
        42,0,0,401,403,5,20,0,0,402,400,1,0,0,0,402,403,1,0,0,0,403,404,
        1,0,0,0,404,413,5,45,0,0,405,410,3,38,19,0,406,407,5,51,0,0,407,
        409,3,38,19,0,408,406,1,0,0,0,409,412,1,0,0,0,410,408,1,0,0,0,410,
        411,1,0,0,0,411,414,1,0,0,0,412,410,1,0,0,0,413,405,1,0,0,0,413,
        414,1,0,0,0,414,415,1,0,0,0,415,416,5,46,0,0,416,417,3,4,2,0,417,
        73,1,0,0,0,418,420,5,4,0,0,419,421,3,38,19,0,420,419,1,0,0,0,420,
        421,1,0,0,0,421,422,1,0,0,0,422,423,3,4,2,0,423,75,1,0,0,0,424,428,
        5,47,0,0,425,427,3,42,21,0,426,425,1,0,0,0,427,430,1,0,0,0,428,426,
        1,0,0,0,428,429,1,0,0,0,429,431,1,0,0,0,430,428,1,0,0,0,431,432,
        5,48,0,0,432,77,1,0,0,0,433,434,5,49,0,0,434,435,5,53,0,0,435,437,
        5,50,0,0,436,433,1,0,0,0,437,438,1,0,0,0,438,436,1,0,0,0,438,439,
        1,0,0,0,439,79,1,0,0,0,39,83,93,100,108,112,116,120,128,132,157,
        164,171,193,203,209,218,228,245,247,254,263,275,289,300,305,313,
        317,326,331,351,356,363,374,402,410,413,420,428,438
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'boolean'", 
                     "'const'", "'var'", "'int'", "'float'", "'string'", 
                     "'continue'", "'break'", "'range'", "<INVALID>", "'nil'", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "':='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "':'", "'_'", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "','", "';'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "BOOLEAN", "CONST", 
                      "VAR", "INTERGER", "FLOAT", "STRING", "CONTINUE", 
                      "BREAK", "RANGE", "BOOLEANLIT", "NILLIT", "IDENTIFIER", 
                      "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "EQUALOP", 
                      "NOTEQUALOP", "LESSOP", "LESSEQUALOP", "GREATEROP", 
                      "GREATEREQUALOP", "ANDOP", "OROP", "NOTOP", "ASSIGNOP", 
                      "SHORTASSIGNOP", "INCASSIGNOP", "DECASSIGNOP", "MULASSIGNOP", 
                      "DIVASSIGNOP", "MODASSIGNOP", "DOT", "COLON", "BLANK", 
                      "LP", "RP", "LB", "RB", "LSB", "RSB", "COMMA", "SEMI", 
                      "INTLIT", "FLOATLIT", "STRINGLIT", "NL", "WS", "COMMENT", 
                      "MULTI_COMMENT", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_tYPE = 1
    RULE_endOfStatement = 2
    RULE_parserRuleSpec = 3
    RULE_decl = 4
    RULE_varDecl = 5
    RULE_funcDecl = 6
    RULE_typeDecl = 7
    RULE_constDecl = 8
    RULE_methodDecl = 9
    RULE_typeDefinition = 10
    RULE_structDefinition = 11
    RULE_structFields = 12
    RULE_interfaceDefinition = 13
    RULE_listParams = 14
    RULE_listIdentifier = 15
    RULE_interfaceFields = 16
    RULE_funcParams = 17
    RULE_funcParam = 18
    RULE_expression = 19
    RULE_term = 20
    RULE_statement = 21
    RULE_arrayLiteral = 22
    RULE_arraysBlock = 23
    RULE_structExpression = 24
    RULE_assignStatement = 25
    RULE_assignmentOperator = 26
    RULE_ifStatement = 27
    RULE_forStatement = 28
    RULE_forLoop = 29
    RULE_initilization = 30
    RULE_forCondition = 31
    RULE_forUpdate = 32
    RULE_forIteration = 33
    RULE_breakStatement = 34
    RULE_continueStatement = 35
    RULE_callStatement = 36
    RULE_returnStatement = 37
    RULE_block = 38
    RULE_arrayDims = 39

    ruleNames =  [ "program", "tYPE", "endOfStatement", "parserRuleSpec", 
                   "decl", "varDecl", "funcDecl", "typeDecl", "constDecl", 
                   "methodDecl", "typeDefinition", "structDefinition", "structFields", 
                   "interfaceDefinition", "listParams", "listIdentifier", 
                   "interfaceFields", "funcParams", "funcParam", "expression", 
                   "term", "statement", "arrayLiteral", "arraysBlock", "structExpression", 
                   "assignStatement", "assignmentOperator", "ifStatement", 
                   "forStatement", "forLoop", "initilization", "forCondition", 
                   "forUpdate", "forIteration", "breakStatement", "continueStatement", 
                   "callStatement", "returnStatement", "block", "arrayDims" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    BOOLEAN=9
    CONST=10
    VAR=11
    INTERGER=12
    FLOAT=13
    STRING=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    BOOLEANLIT=18
    NILLIT=19
    IDENTIFIER=20
    ADDOP=21
    SUBOP=22
    MULOP=23
    DIVOP=24
    MODOP=25
    EQUALOP=26
    NOTEQUALOP=27
    LESSOP=28
    LESSEQUALOP=29
    GREATEROP=30
    GREATEREQUALOP=31
    ANDOP=32
    OROP=33
    NOTOP=34
    ASSIGNOP=35
    SHORTASSIGNOP=36
    INCASSIGNOP=37
    DECASSIGNOP=38
    MULASSIGNOP=39
    DIVASSIGNOP=40
    MODASSIGNOP=41
    DOT=42
    COLON=43
    BLANK=44
    LP=45
    RP=46
    LB=47
    RB=48
    LSB=49
    RSB=50
    COMMA=51
    SEMI=52
    INTLIT=53
    FLOATLIT=54
    STRINGLIT=55
    NL=56
    WS=57
    COMMENT=58
    MULTI_COMMENT=59
    ERROR_CHAR=60
    ILLEGAL_ESCAPE=61
    UNCLOSE_STRING=62

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

        def parserRuleSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParserRuleSpecContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParserRuleSpecContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 80
                self.parserRuleSpec()
                self.state = 83 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1150074) != 0)):
                    break

            self.state = 85
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TYPEContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERGER(self):
            return self.getToken(MiniGoParser.INTERGER, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_tYPE




    def tYPE(self):

        localctx = MiniGoParser.TYPEContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tYPE)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29184) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndOfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_endOfStatement




    def endOfStatement(self):

        localctx = MiniGoParser.EndOfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_endOfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not(((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & 153122387330596865) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParserRuleSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parserRuleSpec




    def parserRuleSpec(self):

        localctx = MiniGoParser.ParserRuleSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parserRuleSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 91
                self.decl()
                pass

            elif la_ == 2:
                self.state = 92
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncDeclContext,0)


        def typeDecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypeDeclContext,0)


        def constDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_decl)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.funcDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.typeDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.constDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 99
                self.methodDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def tYPE(self):
            return self.getTypedRuleContext(MiniGoParser.TYPEContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def ASSIGNOP(self):
            return self.getToken(MiniGoParser.ASSIGNOP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDecl




    def varDecl(self):

        localctx = MiniGoParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(MiniGoParser.VAR)

            self.state = 103
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 104
                self.match(MiniGoParser.COMMA)
                self.state = 105
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 111
                self.arrayDims()


            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 114
                self.tYPE()
                pass

            elif la_ == 2:
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 29184) != 0):
                    self.state = 115
                    self.tYPE()


                self.state = 118
                self.match(MiniGoParser.ASSIGNOP)
                self.state = 119
                self.expression(0)
                pass


            self.state = 122
            self.endOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def funcParams(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamsContext,0)


        def tYPE(self):
            return self.getTypedRuleContext(MiniGoParser.TYPEContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcDecl




    def funcDecl(self):

        localctx = MiniGoParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(MiniGoParser.FUNC)
            self.state = 125
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 126
            self.match(MiniGoParser.LP)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 127
                self.funcParams()


            self.state = 130
            self.match(MiniGoParser.RP)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 29184) != 0):
                self.state = 131
                self.tYPE()


            self.state = 134
            self.block()
            self.state = 135
            self.endOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def typeDefinition(self):
            return self.getTypedRuleContext(MiniGoParser.TypeDefinitionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typeDecl




    def typeDecl(self):

        localctx = MiniGoParser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(MiniGoParser.TYPE)
            self.state = 138
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 139
            self.typeDefinition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def ASSIGNOP(self):
            return self.getToken(MiniGoParser.ASSIGNOP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constDecl




    def constDecl(self):

        localctx = MiniGoParser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(MiniGoParser.CONST)
            self.state = 142
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 143
            self.match(MiniGoParser.ASSIGNOP)
            self.state = 144
            self.expression(0)
            self.state = 145
            self.endOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LP)
            else:
                return self.getToken(MiniGoParser.LP, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RP)
            else:
                return self.getToken(MiniGoParser.RP, i)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def funcParams(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamsContext,0)


        def tYPE(self):
            return self.getTypedRuleContext(MiniGoParser.TYPEContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodDecl




    def methodDecl(self):

        localctx = MiniGoParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(MiniGoParser.FUNC)
            self.state = 148
            self.match(MiniGoParser.LP)
            self.state = 149
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 150
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 151
            self.match(MiniGoParser.RP)
            self.state = 152
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 153
            self.match(MiniGoParser.LP)

            self.state = 154
            self.funcParams()
            self.state = 155
            self.match(MiniGoParser.RP)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 29184) != 0):
                self.state = 156
                self.tYPE()


            self.state = 159
            self.block()
            self.state = 160
            self.endOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structDefinition(self):
            return self.getTypedRuleContext(MiniGoParser.StructDefinitionContext,0)


        def interfaceDefinition(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceDefinitionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typeDefinition




    def typeDefinition(self):

        localctx = MiniGoParser.TypeDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typeDefinition)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.structDefinition()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.interfaceDefinition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def structFields(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StructFieldsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StructFieldsContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structDefinition




    def structDefinition(self):

        localctx = MiniGoParser.StructDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_structDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(MiniGoParser.STRUCT)
            self.state = 167
            self.match(MiniGoParser.LB)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 168
                self.structFields()
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 174
            self.match(MiniGoParser.RB)
            self.state = 175
            self.endOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructFieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def tYPE(self):
            return self.getTypedRuleContext(MiniGoParser.TYPEContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structFields




    def structFields(self):

        localctx = MiniGoParser.StructFieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_structFields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 178
            self.tYPE()
            self.state = 179
            self.endOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def interfaceFields(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceFieldsContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceDefinition




    def interfaceDefinition(self):

        localctx = MiniGoParser.InterfaceDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_interfaceDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(MiniGoParser.INTERFACE)
            self.state = 182
            self.match(MiniGoParser.LB)
            self.state = 183
            self.interfaceFields()
            self.state = 184
            self.match(MiniGoParser.RB)
            self.state = 185
            self.endOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def listIdentifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ListIdentifierContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ListIdentifierContext,i)


        def tYPE(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.TYPEContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.TYPEContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_listParams




    def listParams(self):

        localctx = MiniGoParser.ListParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(MiniGoParser.LP)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 188
                self.listIdentifier()
                self.state = 189
                self.tYPE()
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 196
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_listIdentifier




    def listIdentifier(self):

        localctx = MiniGoParser.ListIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_listIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 199
                self.match(MiniGoParser.COMMA)
                self.state = 200
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceFieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def listParams(self):
            return self.getTypedRuleContext(MiniGoParser.ListParamsContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def tYPE(self):
            return self.getTypedRuleContext(MiniGoParser.TYPEContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceFields




    def interfaceFields(self):

        localctx = MiniGoParser.InterfaceFieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_interfaceFields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 207
            self.listParams()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 29184) != 0):
                self.state = 208
                self.tYPE()


            self.state = 211
            self.endOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcParam(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FuncParamContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FuncParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcParams




    def funcParams(self):

        localctx = MiniGoParser.FuncParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_funcParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.funcParam()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 214
                self.match(MiniGoParser.COMMA)
                self.state = 215
                self.funcParam()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def tYPE(self):
            return self.getTypedRuleContext(MiniGoParser.TYPEContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcParam




    def funcParam(self):

        localctx = MiniGoParser.FuncParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_funcParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 222
            self.tYPE()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(MiniGoParser.TermContext,0)


        def NOTOP(self):
            return self.getToken(MiniGoParser.NOTOP, 0)

        def SUBOP(self):
            return self.getToken(MiniGoParser.SUBOP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OROP(self):
            return self.getToken(MiniGoParser.OROP, 0)

        def ANDOP(self):
            return self.getToken(MiniGoParser.ANDOP, 0)

        def EQUALOP(self):
            return self.getToken(MiniGoParser.EQUALOP, 0)

        def NOTEQUALOP(self):
            return self.getToken(MiniGoParser.NOTEQUALOP, 0)

        def LESSOP(self):
            return self.getToken(MiniGoParser.LESSOP, 0)

        def LESSEQUALOP(self):
            return self.getToken(MiniGoParser.LESSEQUALOP, 0)

        def GREATEROP(self):
            return self.getToken(MiniGoParser.GREATEROP, 0)

        def GREATEREQUALOP(self):
            return self.getToken(MiniGoParser.GREATEREQUALOP, 0)

        def ADDOP(self):
            return self.getToken(MiniGoParser.ADDOP, 0)

        def MULOP(self):
            return self.getToken(MiniGoParser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(MiniGoParser.DIVOP, 0)

        def MODOP(self):
            return self.getToken(MiniGoParser.MODOP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 34]:
                self.state = 225
                _la = self._input.LA(1)
                if not(_la==22 or _la==34):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 226
                self.term()
                pass
            elif token in [20, 45, 53, 54, 55]:
                self.state = 227
                self.term()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 245
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 230
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 231
                        self.match(MiniGoParser.OROP)
                        self.state = 232
                        self.term()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 233
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 234
                        self.match(MiniGoParser.ANDOP)
                        self.state = 235
                        self.term()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 236
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 237
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4227858432) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 238
                        self.term()
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 239
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 240
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 241
                        self.term()
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 242
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 243
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 244
                        self.term()
                        pass

             
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MiniGoParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MiniGoParser.STRINGLIT, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_term




    def term(self):

        localctx = MiniGoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_term)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 254
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 251
                    self.arrayDims()

                elif la_ == 2:
                    self.state = 252
                    self.match(MiniGoParser.DOT)
                    self.state = 253
                    self.match(MiniGoParser.IDENTIFIER)


                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(MiniGoParser.INTLIT)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.match(MiniGoParser.FLOATLIT)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 4)
                self.state = 258
                self.match(MiniGoParser.STRINGLIT)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 5)
                self.state = 259
                self.match(MiniGoParser.LP)
                self.state = 260
                self.expression(0)
                self.state = 261
                self.match(MiniGoParser.RP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStatement(self):
            return self.getTypedRuleContext(MiniGoParser.AssignStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniGoParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ForStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(MiniGoParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ContinueStatementContext,0)


        def callStatement(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnStatementContext,0)


        def arrayLiteral(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLiteralContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def constDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 265
                self.assignStatement()
                pass

            elif la_ == 2:
                self.state = 266
                self.ifStatement()
                pass

            elif la_ == 3:
                self.state = 267
                self.forStatement()
                pass

            elif la_ == 4:
                self.state = 268
                self.breakStatement()
                pass

            elif la_ == 5:
                self.state = 269
                self.continueStatement()
                pass

            elif la_ == 6:
                self.state = 270
                self.callStatement()
                pass

            elif la_ == 7:
                self.state = 271
                self.returnStatement()
                pass

            elif la_ == 8:
                self.state = 272
                self.arrayLiteral()
                pass

            elif la_ == 9:
                self.state = 273
                self.varDecl()
                pass

            elif la_ == 10:
                self.state = 274
                self.constDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def SHORTASSIGNOP(self):
            return self.getToken(MiniGoParser.SHORTASSIGNOP, 0)

        def arraysBlock(self):
            return self.getTypedRuleContext(MiniGoParser.ArraysBlockContext,0)


        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLiteral




    def arrayLiteral(self):

        localctx = MiniGoParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 278
            self.match(MiniGoParser.SHORTASSIGNOP)

            self.state = 279
            self.arrayDims()
            self.state = 280
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 25344) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 281
            self.arraysBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraysBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def arraysBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ArraysBlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ArraysBlockContext,i)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arraysBlock




    def arraysBlock(self):

        localctx = MiniGoParser.ArraysBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arraysBlock)
        self._la = 0 # Token type
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.match(MiniGoParser.LB)
                self.state = 284
                self.arraysBlock()
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==51:
                    self.state = 285
                    self.match(MiniGoParser.COMMA)
                    self.state = 286
                    self.arraysBlock()
                    self.state = 291
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 292
                self.match(MiniGoParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.match(MiniGoParser.LB)
                self.state = 295
                self.expression(0)
                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==51:
                    self.state = 296
                    self.match(MiniGoParser.COMMA)
                    self.state = 297
                    self.expression(0)
                    self.state = 302
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 303
                self.match(MiniGoParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COLON)
            else:
                return self.getToken(MiniGoParser.COLON, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structExpression




    def structExpression(self):

        localctx = MiniGoParser.StructExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_structExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 308
            self.match(MiniGoParser.LB)
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 309
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 310
                self.match(MiniGoParser.COLON)
                self.state = 311
                self.expression(0)
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==51:
                    self.state = 312
                    self.match(MiniGoParser.COMMA)


                self.state = 319
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 320
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def assignmentOperator(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentOperatorContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def structExpression(self):
            return self.getTypedRuleContext(MiniGoParser.StructExpressionContext,0)


        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignStatement




    def assignStatement(self):

        localctx = MiniGoParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.state = 323
                self.arrayDims()
                pass
            elif token in [42]:
                self.state = 324
                self.match(MiniGoParser.DOT)
                self.state = 325
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [36, 37, 38, 39, 40, 41]:
                pass
            else:
                pass
            self.state = 328
            self.assignmentOperator()
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 329
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 330
                self.structExpression()
                pass


            self.state = 333
            self.endOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHORTASSIGNOP(self):
            return self.getToken(MiniGoParser.SHORTASSIGNOP, 0)

        def INCASSIGNOP(self):
            return self.getToken(MiniGoParser.INCASSIGNOP, 0)

        def DECASSIGNOP(self):
            return self.getToken(MiniGoParser.DECASSIGNOP, 0)

        def MULASSIGNOP(self):
            return self.getToken(MiniGoParser.MULASSIGNOP, 0)

        def DIVASSIGNOP(self):
            return self.getToken(MiniGoParser.DIVASSIGNOP, 0)

        def MODASSIGNOP(self):
            return self.getToken(MiniGoParser.MODASSIGNOP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignmentOperator




    def assignmentOperator(self):

        localctx = MiniGoParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4329327034368) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IF)
            else:
                return self.getToken(MiniGoParser.IF, i)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LP)
            else:
                return self.getToken(MiniGoParser.LP, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RP)
            else:
                return self.getToken(MiniGoParser.RP, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ELSE)
            else:
                return self.getToken(MiniGoParser.ELSE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ifStatement




    def ifStatement(self):

        localctx = MiniGoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(MiniGoParser.IF)
            self.state = 338
            self.match(MiniGoParser.LP)
            self.state = 339
            self.expression(0)
            self.state = 340
            self.match(MiniGoParser.RP)
            self.state = 341
            self.block()
            self.state = 351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 342
                    self.match(MiniGoParser.ELSE)
                    self.state = 343
                    self.match(MiniGoParser.IF)
                    self.state = 344
                    self.match(MiniGoParser.LP)
                    self.state = 345
                    self.expression(0)
                    self.state = 346
                    self.match(MiniGoParser.RP)
                    self.state = 347
                    self.block() 
                self.state = 353
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

            self.state = 356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 354
                self.match(MiniGoParser.ELSE)
                self.state = 355
                self.block()


            self.state = 358
            self.endOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(MiniGoParser.ForLoopContext,0)


        def forIteration(self):
            return self.getTypedRuleContext(MiniGoParser.ForIterationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forStatement




    def forStatement(self):

        localctx = MiniGoParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(MiniGoParser.FOR)
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 361
                self.forLoop()
                pass

            elif la_ == 2:
                self.state = 362
                self.forIteration()
                pass


            self.state = 365
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forCondition(self):
            return self.getTypedRuleContext(MiniGoParser.ForConditionContext,0)


        def initilization(self):
            return self.getTypedRuleContext(MiniGoParser.InitilizationContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def forUpdate(self):
            return self.getTypedRuleContext(MiniGoParser.ForUpdateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forLoop




    def forLoop(self):

        localctx = MiniGoParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_forLoop)
        try:
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.forCondition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.initilization()
                self.state = 369
                self.match(MiniGoParser.SEMI)
                self.state = 370
                self.forCondition()
                self.state = 371
                self.match(MiniGoParser.SEMI)
                self.state = 372
                self.forUpdate()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitilizationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def SHORTASSIGNOP(self):
            return self.getToken(MiniGoParser.SHORTASSIGNOP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_initilization




    def initilization(self):

        localctx = MiniGoParser.InitilizationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_initilization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 377
            self.match(MiniGoParser.SHORTASSIGNOP)
            self.state = 378
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forCondition




    def forCondition(self):

        localctx = MiniGoParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def assignmentOperator(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentOperatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forUpdate




    def forUpdate(self):

        localctx = MiniGoParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 383
            self.assignmentOperator()
            self.state = 384
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForIterationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def SHORTASSIGNOP(self):
            return self.getToken(MiniGoParser.SHORTASSIGNOP, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def BLANK(self):
            return self.getToken(MiniGoParser.BLANK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_forIteration




    def forIteration(self):

        localctx = MiniGoParser.ForIterationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_forIteration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            _la = self._input.LA(1)
            if not(_la==20 or _la==44):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 387
            self.match(MiniGoParser.COMMA)
            self.state = 388
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 389
            self.match(MiniGoParser.SHORTASSIGNOP)
            self.state = 390
            self.match(MiniGoParser.RANGE)
            self.state = 391
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_breakStatement




    def breakStatement(self):

        localctx = MiniGoParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(MiniGoParser.BREAK)
            self.state = 394
            self.endOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continueStatement




    def continueStatement(self):

        localctx = MiniGoParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(MiniGoParser.CONTINUE)
            self.state = 397
            self.endOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_callStatement




    def callStatement(self):

        localctx = MiniGoParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_callStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 400
                self.match(MiniGoParser.DOT)
                self.state = 401
                self.match(MiniGoParser.IDENTIFIER)


            self.state = 404
            self.match(MiniGoParser.LP)
            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 63085596340387840) != 0):
                self.state = 405
                self.expression(0)
                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==51:
                    self.state = 406
                    self.match(MiniGoParser.COMMA)
                    self.state = 407
                    self.expression(0)
                    self.state = 412
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 415
            self.match(MiniGoParser.RP)
            self.state = 416
            self.endOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStatement




    def returnStatement(self):

        localctx = MiniGoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(MiniGoParser.RETURN)
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 63085596340387840) != 0):
                self.state = 419
                self.expression(0)


            self.state = 422
            self.endOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(MiniGoParser.LB)
            self.state = 428
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1149978) != 0):
                self.state = 425
                self.statement()
                self.state = 430
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 431
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDimsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LSB)
            else:
                return self.getToken(MiniGoParser.LSB, i)

        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INTLIT)
            else:
                return self.getToken(MiniGoParser.INTLIT, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RSB)
            else:
                return self.getToken(MiniGoParser.RSB, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayDims




    def arrayDims(self):

        localctx = MiniGoParser.ArrayDimsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_arrayDims)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 433
                    self.match(MiniGoParser.LSB)
                    self.state = 434
                    self.match(MiniGoParser.INTLIT)
                    self.state = 435
                    self.match(MiniGoParser.RSB)

                else:
                    raise NoViableAltException(self)
                self.state = 438 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[19] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




