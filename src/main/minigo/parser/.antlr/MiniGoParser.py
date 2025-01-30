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
        4,1,64,493,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,1,0,
        5,0,94,8,0,10,0,12,0,97,9,0,1,0,3,0,100,8,0,1,0,5,0,103,8,0,10,0,
        12,0,106,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,3,4,126,8,4,1,4,1,4,1,5,1,5,1,5,1,5,5,5,134,
        8,5,10,5,12,5,137,9,5,1,5,3,5,140,8,5,1,5,1,5,3,5,144,8,5,1,5,1,
        5,3,5,148,8,5,1,6,1,6,1,6,1,6,3,6,154,8,6,1,6,1,6,3,6,158,8,6,1,
        6,3,6,161,8,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,169,8,7,1,8,1,8,1,8,1,
        8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,184,8,9,1,9,1,9,3,9,188,
        8,9,1,9,1,9,1,10,1,10,1,10,5,10,195,8,10,10,10,12,10,198,9,10,1,
        10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,5,12,209,8,12,10,12,12,
        12,212,9,12,1,12,1,12,1,13,1,13,1,13,1,13,5,13,220,8,13,10,13,12,
        13,223,9,13,1,13,1,13,1,14,1,14,1,14,5,14,230,8,14,10,14,12,14,233,
        9,14,1,15,1,15,1,15,3,15,238,8,15,1,15,1,15,1,16,1,16,1,16,5,16,
        245,8,16,10,16,12,16,248,9,16,1,17,1,17,3,17,252,8,17,1,17,1,17,
        1,18,1,18,1,19,1,19,1,19,5,19,261,8,19,10,19,12,19,264,9,19,1,20,
        1,20,1,20,5,20,269,8,20,10,20,12,20,272,9,20,1,21,1,21,1,21,5,21,
        277,8,21,10,21,12,21,280,9,21,1,22,1,22,1,22,5,22,285,8,22,10,22,
        12,22,288,9,22,1,23,1,23,1,23,5,23,293,8,23,10,23,12,23,296,9,23,
        1,24,1,24,1,24,3,24,301,8,24,1,25,1,25,1,25,1,25,1,25,3,25,308,8,
        25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,320,8,
        26,1,26,3,26,323,8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,
        27,1,27,1,27,1,27,3,27,337,8,27,1,27,1,27,1,28,1,28,1,28,1,28,1,
        28,1,28,1,29,1,29,1,29,1,29,5,29,351,8,29,10,29,12,29,354,9,29,1,
        29,1,29,1,29,1,29,1,29,1,29,5,29,362,8,29,10,29,12,29,365,9,29,1,
        29,1,29,3,29,369,8,29,1,30,1,30,1,30,1,30,1,30,1,30,3,30,377,8,30,
        5,30,379,8,30,10,30,12,30,382,9,30,1,30,1,30,1,31,1,31,1,31,1,31,
        3,31,390,8,31,1,31,1,31,1,31,3,31,395,8,31,1,32,1,32,1,33,1,33,1,
        33,1,33,1,33,1,33,1,33,1,33,5,33,407,8,33,10,33,12,33,410,9,33,1,
        33,1,33,3,33,414,8,33,1,34,1,34,1,34,3,34,419,8,34,1,34,1,34,1,35,
        1,35,1,35,1,35,1,35,1,35,1,35,3,35,430,8,35,1,36,1,36,1,36,1,36,
        1,37,1,37,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,39,1,39,
        1,40,1,40,1,41,1,41,1,42,1,42,1,42,3,42,456,8,42,1,42,1,42,1,42,
        1,42,5,42,462,8,42,10,42,12,42,465,9,42,3,42,467,8,42,1,42,1,42,
        1,43,1,43,3,43,473,8,43,1,44,1,44,5,44,477,8,44,10,44,12,44,480,
        9,44,1,44,1,44,1,45,1,45,3,45,486,8,45,1,45,4,45,489,8,45,11,45,
        12,45,490,1,45,0,0,46,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,
        76,78,80,82,84,86,88,90,0,8,2,0,10,13,54,54,2,1,52,52,61,61,1,0,
        29,34,1,0,24,25,1,0,26,28,2,0,25,25,37,37,2,0,23,23,38,42,2,0,44,
        44,54,54,516,0,95,1,0,0,0,2,109,1,0,0,0,4,116,1,0,0,0,6,118,1,0,
        0,0,8,125,1,0,0,0,10,129,1,0,0,0,12,149,1,0,0,0,14,164,1,0,0,0,16,
        170,1,0,0,0,18,175,1,0,0,0,20,191,1,0,0,0,22,201,1,0,0,0,24,205,
        1,0,0,0,26,215,1,0,0,0,28,226,1,0,0,0,30,234,1,0,0,0,32,241,1,0,
        0,0,34,249,1,0,0,0,36,255,1,0,0,0,38,257,1,0,0,0,40,265,1,0,0,0,
        42,273,1,0,0,0,44,281,1,0,0,0,46,289,1,0,0,0,48,300,1,0,0,0,50,307,
        1,0,0,0,52,322,1,0,0,0,54,336,1,0,0,0,56,340,1,0,0,0,58,368,1,0,
        0,0,60,370,1,0,0,0,62,385,1,0,0,0,64,396,1,0,0,0,66,398,1,0,0,0,
        68,415,1,0,0,0,70,429,1,0,0,0,72,431,1,0,0,0,74,435,1,0,0,0,76,437,
        1,0,0,0,78,441,1,0,0,0,80,448,1,0,0,0,82,450,1,0,0,0,84,452,1,0,
        0,0,86,470,1,0,0,0,88,474,1,0,0,0,90,488,1,0,0,0,92,94,3,8,4,0,93,
        92,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,99,1,0,0,
        0,97,95,1,0,0,0,98,100,3,2,1,0,99,98,1,0,0,0,99,100,1,0,0,0,100,
        104,1,0,0,0,101,103,3,8,4,0,102,101,1,0,0,0,103,106,1,0,0,0,104,
        102,1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,106,104,1,0,0,0,107,
        108,5,0,0,1,108,1,1,0,0,0,109,110,5,6,0,0,110,111,5,1,0,0,111,112,
        5,45,0,0,112,113,5,46,0,0,113,114,3,88,44,0,114,115,3,6,3,0,115,
        3,1,0,0,0,116,117,7,0,0,0,117,5,1,0,0,0,118,119,7,1,0,0,119,7,1,
        0,0,0,120,126,3,10,5,0,121,126,3,12,6,0,122,126,3,14,7,0,123,126,
        3,16,8,0,124,126,3,18,9,0,125,120,1,0,0,0,125,121,1,0,0,0,125,122,
        1,0,0,0,125,123,1,0,0,0,125,124,1,0,0,0,126,127,1,0,0,0,127,128,
        3,6,3,0,128,9,1,0,0,0,129,130,5,18,0,0,130,135,5,54,0,0,131,132,
        5,51,0,0,132,134,5,54,0,0,133,131,1,0,0,0,134,137,1,0,0,0,135,133,
        1,0,0,0,135,136,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,138,140,
        3,90,45,0,139,138,1,0,0,0,139,140,1,0,0,0,140,147,1,0,0,0,141,148,
        3,4,2,0,142,144,3,4,2,0,143,142,1,0,0,0,143,144,1,0,0,0,144,145,
        1,0,0,0,145,146,5,22,0,0,146,148,3,36,18,0,147,141,1,0,0,0,147,143,
        1,0,0,0,148,11,1,0,0,0,149,150,5,6,0,0,150,151,5,54,0,0,151,153,
        5,45,0,0,152,154,3,32,16,0,153,152,1,0,0,0,153,154,1,0,0,0,154,155,
        1,0,0,0,155,160,5,46,0,0,156,158,3,90,45,0,157,156,1,0,0,0,157,158,
        1,0,0,0,158,159,1,0,0,0,159,161,3,4,2,0,160,157,1,0,0,0,160,161,
        1,0,0,0,161,162,1,0,0,0,162,163,3,88,44,0,163,13,1,0,0,0,164,165,
        5,7,0,0,165,168,5,54,0,0,166,169,3,20,10,0,167,169,3,24,12,0,168,
        166,1,0,0,0,168,167,1,0,0,0,169,15,1,0,0,0,170,171,5,17,0,0,171,
        172,5,54,0,0,172,173,5,22,0,0,173,174,3,36,18,0,174,17,1,0,0,0,175,
        176,5,6,0,0,176,177,5,45,0,0,177,178,5,54,0,0,178,179,5,54,0,0,179,
        180,5,46,0,0,180,181,5,54,0,0,181,183,5,45,0,0,182,184,3,32,16,0,
        183,182,1,0,0,0,183,184,1,0,0,0,184,185,1,0,0,0,185,187,5,46,0,0,
        186,188,3,4,2,0,187,186,1,0,0,0,187,188,1,0,0,0,188,189,1,0,0,0,
        189,190,3,88,44,0,190,19,1,0,0,0,191,192,5,8,0,0,192,196,5,47,0,
        0,193,195,3,22,11,0,194,193,1,0,0,0,195,198,1,0,0,0,196,194,1,0,
        0,0,196,197,1,0,0,0,197,199,1,0,0,0,198,196,1,0,0,0,199,200,5,48,
        0,0,200,21,1,0,0,0,201,202,5,54,0,0,202,203,3,4,2,0,203,204,3,6,
        3,0,204,23,1,0,0,0,205,206,5,9,0,0,206,210,5,47,0,0,207,209,3,30,
        15,0,208,207,1,0,0,0,209,212,1,0,0,0,210,208,1,0,0,0,210,211,1,0,
        0,0,211,213,1,0,0,0,212,210,1,0,0,0,213,214,5,48,0,0,214,25,1,0,
        0,0,215,221,5,45,0,0,216,217,3,28,14,0,217,218,3,4,2,0,218,220,1,
        0,0,0,219,216,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,222,1,
        0,0,0,222,224,1,0,0,0,223,221,1,0,0,0,224,225,5,46,0,0,225,27,1,
        0,0,0,226,231,5,54,0,0,227,228,5,51,0,0,228,230,5,54,0,0,229,227,
        1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,29,1,
        0,0,0,233,231,1,0,0,0,234,235,5,54,0,0,235,237,3,26,13,0,236,238,
        3,4,2,0,237,236,1,0,0,0,237,238,1,0,0,0,238,239,1,0,0,0,239,240,
        3,6,3,0,240,31,1,0,0,0,241,246,3,34,17,0,242,243,5,51,0,0,243,245,
        3,34,17,0,244,242,1,0,0,0,245,248,1,0,0,0,246,244,1,0,0,0,246,247,
        1,0,0,0,247,33,1,0,0,0,248,246,1,0,0,0,249,251,5,54,0,0,250,252,
        3,90,45,0,251,250,1,0,0,0,251,252,1,0,0,0,252,253,1,0,0,0,253,254,
        3,4,2,0,254,35,1,0,0,0,255,256,3,38,19,0,256,37,1,0,0,0,257,262,
        3,40,20,0,258,259,5,36,0,0,259,261,3,38,19,0,260,258,1,0,0,0,261,
        264,1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,39,1,0,0,0,264,262,
        1,0,0,0,265,270,3,42,21,0,266,267,5,35,0,0,267,269,3,40,20,0,268,
        266,1,0,0,0,269,272,1,0,0,0,270,268,1,0,0,0,270,271,1,0,0,0,271,
        41,1,0,0,0,272,270,1,0,0,0,273,278,3,44,22,0,274,275,7,2,0,0,275,
        277,3,44,22,0,276,274,1,0,0,0,277,280,1,0,0,0,278,276,1,0,0,0,278,
        279,1,0,0,0,279,43,1,0,0,0,280,278,1,0,0,0,281,286,3,46,23,0,282,
        283,7,3,0,0,283,285,3,46,23,0,284,282,1,0,0,0,285,288,1,0,0,0,286,
        284,1,0,0,0,286,287,1,0,0,0,287,45,1,0,0,0,288,286,1,0,0,0,289,294,
        3,48,24,0,290,291,7,4,0,0,291,293,3,48,24,0,292,290,1,0,0,0,293,
        296,1,0,0,0,294,292,1,0,0,0,294,295,1,0,0,0,295,47,1,0,0,0,296,294,
        1,0,0,0,297,298,7,5,0,0,298,301,3,48,24,0,299,301,3,50,25,0,300,
        297,1,0,0,0,300,299,1,0,0,0,301,49,1,0,0,0,302,308,3,52,26,0,303,
        304,5,45,0,0,304,305,3,36,18,0,305,306,5,46,0,0,306,308,1,0,0,0,
        307,302,1,0,0,0,307,303,1,0,0,0,308,51,1,0,0,0,309,323,5,55,0,0,
        310,323,5,56,0,0,311,323,5,57,0,0,312,323,5,14,0,0,313,323,5,15,
        0,0,314,323,5,16,0,0,315,319,5,54,0,0,316,320,3,90,45,0,317,318,
        5,43,0,0,318,320,5,54,0,0,319,316,1,0,0,0,319,317,1,0,0,0,319,320,
        1,0,0,0,320,323,1,0,0,0,321,323,3,84,42,0,322,309,1,0,0,0,322,310,
        1,0,0,0,322,311,1,0,0,0,322,312,1,0,0,0,322,313,1,0,0,0,322,314,
        1,0,0,0,322,315,1,0,0,0,322,321,1,0,0,0,323,53,1,0,0,0,324,337,3,
        62,31,0,325,337,3,66,33,0,326,337,3,68,34,0,327,337,3,80,40,0,328,
        337,3,82,41,0,329,337,3,84,42,0,330,337,3,86,43,0,331,337,3,56,28,
        0,332,337,3,10,5,0,333,337,3,14,7,0,334,337,3,18,9,0,335,337,3,16,
        8,0,336,324,1,0,0,0,336,325,1,0,0,0,336,326,1,0,0,0,336,327,1,0,
        0,0,336,328,1,0,0,0,336,329,1,0,0,0,336,330,1,0,0,0,336,331,1,0,
        0,0,336,332,1,0,0,0,336,333,1,0,0,0,336,334,1,0,0,0,336,335,1,0,
        0,0,337,338,1,0,0,0,338,339,3,6,3,0,339,55,1,0,0,0,340,341,5,54,
        0,0,341,342,5,23,0,0,342,343,3,90,45,0,343,344,3,4,2,0,344,345,3,
        58,29,0,345,57,1,0,0,0,346,347,5,47,0,0,347,352,3,58,29,0,348,349,
        5,51,0,0,349,351,3,58,29,0,350,348,1,0,0,0,351,354,1,0,0,0,352,350,
        1,0,0,0,352,353,1,0,0,0,353,355,1,0,0,0,354,352,1,0,0,0,355,356,
        5,48,0,0,356,369,1,0,0,0,357,358,5,47,0,0,358,363,3,36,18,0,359,
        360,5,51,0,0,360,362,3,36,18,0,361,359,1,0,0,0,362,365,1,0,0,0,363,
        361,1,0,0,0,363,364,1,0,0,0,364,366,1,0,0,0,365,363,1,0,0,0,366,
        367,5,48,0,0,367,369,1,0,0,0,368,346,1,0,0,0,368,357,1,0,0,0,369,
        59,1,0,0,0,370,371,5,54,0,0,371,380,5,47,0,0,372,373,5,54,0,0,373,
        374,5,53,0,0,374,376,3,36,18,0,375,377,5,51,0,0,376,375,1,0,0,0,
        376,377,1,0,0,0,377,379,1,0,0,0,378,372,1,0,0,0,379,382,1,0,0,0,
        380,378,1,0,0,0,380,381,1,0,0,0,381,383,1,0,0,0,382,380,1,0,0,0,
        383,384,5,48,0,0,384,61,1,0,0,0,385,389,5,54,0,0,386,390,3,90,45,
        0,387,388,5,43,0,0,388,390,5,54,0,0,389,386,1,0,0,0,389,387,1,0,
        0,0,389,390,1,0,0,0,390,391,1,0,0,0,391,394,3,64,32,0,392,395,3,
        36,18,0,393,395,3,60,30,0,394,392,1,0,0,0,394,393,1,0,0,0,395,63,
        1,0,0,0,396,397,7,6,0,0,397,65,1,0,0,0,398,399,5,2,0,0,399,400,3,
        36,18,0,400,408,3,88,44,0,401,402,5,3,0,0,402,403,5,2,0,0,403,404,
        3,36,18,0,404,405,3,88,44,0,405,407,1,0,0,0,406,401,1,0,0,0,407,
        410,1,0,0,0,408,406,1,0,0,0,408,409,1,0,0,0,409,413,1,0,0,0,410,
        408,1,0,0,0,411,412,5,3,0,0,412,414,3,88,44,0,413,411,1,0,0,0,413,
        414,1,0,0,0,414,67,1,0,0,0,415,418,5,4,0,0,416,419,3,70,35,0,417,
        419,3,78,39,0,418,416,1,0,0,0,418,417,1,0,0,0,419,420,1,0,0,0,420,
        421,3,88,44,0,421,69,1,0,0,0,422,430,3,74,37,0,423,424,3,72,36,0,
        424,425,5,52,0,0,425,426,3,74,37,0,426,427,5,52,0,0,427,428,3,76,
        38,0,428,430,1,0,0,0,429,422,1,0,0,0,429,423,1,0,0,0,430,71,1,0,
        0,0,431,432,5,54,0,0,432,433,5,23,0,0,433,434,3,36,18,0,434,73,1,
        0,0,0,435,436,3,36,18,0,436,75,1,0,0,0,437,438,5,54,0,0,438,439,
        3,64,32,0,439,440,3,36,18,0,440,77,1,0,0,0,441,442,7,7,0,0,442,443,
        5,51,0,0,443,444,5,54,0,0,444,445,5,23,0,0,445,446,5,21,0,0,446,
        447,5,54,0,0,447,79,1,0,0,0,448,449,5,20,0,0,449,81,1,0,0,0,450,
        451,5,19,0,0,451,83,1,0,0,0,452,455,5,54,0,0,453,454,5,43,0,0,454,
        456,5,54,0,0,455,453,1,0,0,0,455,456,1,0,0,0,456,457,1,0,0,0,457,
        466,5,45,0,0,458,463,3,36,18,0,459,460,5,51,0,0,460,462,3,36,18,
        0,461,459,1,0,0,0,462,465,1,0,0,0,463,461,1,0,0,0,463,464,1,0,0,
        0,464,467,1,0,0,0,465,463,1,0,0,0,466,458,1,0,0,0,466,467,1,0,0,
        0,467,468,1,0,0,0,468,469,5,46,0,0,469,85,1,0,0,0,470,472,5,5,0,
        0,471,473,3,36,18,0,472,471,1,0,0,0,472,473,1,0,0,0,473,87,1,0,0,
        0,474,478,5,47,0,0,475,477,3,54,27,0,476,475,1,0,0,0,477,480,1,0,
        0,0,478,476,1,0,0,0,478,479,1,0,0,0,479,481,1,0,0,0,480,478,1,0,
        0,0,481,482,5,48,0,0,482,89,1,0,0,0,483,485,5,49,0,0,484,486,3,36,
        18,0,485,484,1,0,0,0,485,486,1,0,0,0,486,487,1,0,0,0,487,489,5,50,
        0,0,488,483,1,0,0,0,489,490,1,0,0,0,490,488,1,0,0,0,490,491,1,0,
        0,0,491,91,1,0,0,0,49,95,99,104,125,135,139,143,147,153,157,160,
        168,183,187,196,210,221,231,237,246,251,262,270,278,286,294,300,
        307,319,322,336,352,363,368,376,380,389,394,408,413,418,429,455,
        463,466,472,478,485,490
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'true'", "'false'", 
                     "'nil'", "'const'", "'var'", "'continue'", "'break'", 
                     "'range'", "'='", "':='", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'&&'", "'||'", "'!'", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "'_'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "','", "';'", "':'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "IF", "ELSE", "FOR", "RETURN", 
                      "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                      "FLOAT", "BOOLEAN", "TRUE", "FALSE", "NIL", "CONST", 
                      "VAR", "CONTINUE", "BREAK", "RANGE", "ASSIGN", "DECLARE", 
                      "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQ", "NEQ", 
                      "LT", "LEQ", "GT", "GEQ", "AND", "OR", "NOT", "PLUS_ASSIGN", 
                      "MINUS_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "DOT", "BLANK", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACKET", "RBRACKET", "COMMA", "SEMI", "COLON", 
                      "IDENTIFIER", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "BLOCK_COMMENT", "LINE_COMMENT", "WS", "NEWLINE", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_mainFunction = 1
    RULE_baseType = 2
    RULE_endOfStatement = 3
    RULE_declaration = 4
    RULE_varDecl = 5
    RULE_funcDecl = 6
    RULE_typeDecl = 7
    RULE_constDecl = 8
    RULE_methodDecl = 9
    RULE_structDefinition = 10
    RULE_structFields = 11
    RULE_interfaceDefinition = 12
    RULE_listParams = 13
    RULE_listIdentifier = 14
    RULE_interfaceFields = 15
    RULE_funcParams = 16
    RULE_funcParam = 17
    RULE_expression = 18
    RULE_logicOrExp = 19
    RULE_logicAndExp = 20
    RULE_equalityExp = 21
    RULE_additiveExp = 22
    RULE_multiplicativeExp = 23
    RULE_unaryExp = 24
    RULE_primaryExp = 25
    RULE_term = 26
    RULE_statement = 27
    RULE_arrayLiteral = 28
    RULE_arraysBlock = 29
    RULE_structExpression = 30
    RULE_assignStatement = 31
    RULE_assignmentOperator = 32
    RULE_ifStatement = 33
    RULE_forStatement = 34
    RULE_forLoop = 35
    RULE_initilization = 36
    RULE_forCondition = 37
    RULE_forUpdate = 38
    RULE_forIteration = 39
    RULE_breakStatement = 40
    RULE_continueStatement = 41
    RULE_callStatement = 42
    RULE_returnStatement = 43
    RULE_block = 44
    RULE_arrayDims = 45

    ruleNames =  [ "program", "mainFunction", "baseType", "endOfStatement", 
                   "declaration", "varDecl", "funcDecl", "typeDecl", "constDecl", 
                   "methodDecl", "structDefinition", "structFields", "interfaceDefinition", 
                   "listParams", "listIdentifier", "interfaceFields", "funcParams", 
                   "funcParam", "expression", "logicOrExp", "logicAndExp", 
                   "equalityExp", "additiveExp", "multiplicativeExp", "unaryExp", 
                   "primaryExp", "term", "statement", "arrayLiteral", "arraysBlock", 
                   "structExpression", "assignStatement", "assignmentOperator", 
                   "ifStatement", "forStatement", "forLoop", "initilization", 
                   "forCondition", "forUpdate", "forIteration", "breakStatement", 
                   "continueStatement", "callStatement", "returnStatement", 
                   "block", "arrayDims" ]

    EOF = Token.EOF
    T__0=1
    IF=2
    ELSE=3
    FOR=4
    RETURN=5
    FUNC=6
    TYPE=7
    STRUCT=8
    INTERFACE=9
    STRING=10
    INT=11
    FLOAT=12
    BOOLEAN=13
    TRUE=14
    FALSE=15
    NIL=16
    CONST=17
    VAR=18
    CONTINUE=19
    BREAK=20
    RANGE=21
    ASSIGN=22
    DECLARE=23
    PLUS=24
    MINUS=25
    MUL=26
    DIV=27
    MOD=28
    EQ=29
    NEQ=30
    LT=31
    LEQ=32
    GT=33
    GEQ=34
    AND=35
    OR=36
    NOT=37
    PLUS_ASSIGN=38
    MINUS_ASSIGN=39
    MUL_ASSIGN=40
    DIV_ASSIGN=41
    MOD_ASSIGN=42
    DOT=43
    BLANK=44
    LPAREN=45
    RPAREN=46
    LBRACE=47
    RBRACE=48
    LBRACKET=49
    RBRACKET=50
    COMMA=51
    SEMI=52
    COLON=53
    IDENTIFIER=54
    INT_LIT=55
    FLOAT_LIT=56
    STRING_LIT=57
    BLOCK_COMMENT=58
    LINE_COMMENT=59
    WS=60
    NEWLINE=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    ERROR_CHAR=64

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

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclarationContext,i)


        def mainFunction(self):
            return self.getTypedRuleContext(MiniGoParser.MainFunctionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 92
                    self.declaration() 
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 98
                self.mainFunction()


            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 393408) != 0):
                self.state = 101
                self.declaration()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_mainFunction




    def mainFunction(self):

        localctx = MiniGoParser.MainFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mainFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(MiniGoParser.FUNC)
            self.state = 110
            self.match(MiniGoParser.T__0)
            self.state = 111
            self.match(MiniGoParser.LPAREN)
            self.state = 112
            self.match(MiniGoParser.RPAREN)
            self.state = 113
            self.block()
            self.state = 114
            self.endOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_baseType




    def baseType(self):

        localctx = MiniGoParser.BaseTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398509497344) != 0)):
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

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_endOfStatement




    def endOfStatement(self):

        localctx = MiniGoParser.EndOfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_endOfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not(((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & 4620693217682128897) != 0)):
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


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


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
            return MiniGoParser.RULE_declaration




    def declaration(self):

        localctx = MiniGoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 120
                self.varDecl()
                pass

            elif la_ == 2:
                self.state = 121
                self.funcDecl()
                pass

            elif la_ == 3:
                self.state = 122
                self.typeDecl()
                pass

            elif la_ == 4:
                self.state = 123
                self.constDecl()
                pass

            elif la_ == 5:
                self.state = 124
                self.methodDecl()
                pass


            self.state = 127
            self.endOfStatement()
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

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
            self.state = 129
            self.match(MiniGoParser.VAR)
            self.state = 130
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 131
                self.match(MiniGoParser.COMMA)
                self.state = 132
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 138
                self.arrayDims()


            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 141
                self.baseType()
                pass

            elif la_ == 2:
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398509497344) != 0):
                    self.state = 142
                    self.baseType()


                self.state = 145
                self.match(MiniGoParser.ASSIGN)
                self.state = 146
                self.expression()
                pass


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

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def funcParams(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamsContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcDecl




    def funcDecl(self):

        localctx = MiniGoParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(MiniGoParser.FUNC)
            self.state = 150
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 151
            self.match(MiniGoParser.LPAREN)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 152
                self.funcParams()


            self.state = 155
            self.match(MiniGoParser.RPAREN)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18577348462918656) != 0):
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 156
                    self.arrayDims()


                self.state = 159
                self.baseType()


            self.state = 162
            self.block()
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

        def structDefinition(self):
            return self.getTypedRuleContext(MiniGoParser.StructDefinitionContext,0)


        def interfaceDefinition(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceDefinitionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typeDecl




    def typeDecl(self):

        localctx = MiniGoParser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(MiniGoParser.TYPE)
            self.state = 165
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.state = 166
                self.structDefinition()
                pass
            elif token in [9]:
                self.state = 167
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


    class ConstDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constDecl




    def constDecl(self):

        localctx = MiniGoParser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(MiniGoParser.CONST)
            self.state = 171
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 172
            self.match(MiniGoParser.ASSIGN)
            self.state = 173
            self.expression()
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

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def funcParams(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamsContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodDecl




    def methodDecl(self):

        localctx = MiniGoParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(MiniGoParser.FUNC)
            self.state = 176
            self.match(MiniGoParser.LPAREN)
            self.state = 177
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 178
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 179
            self.match(MiniGoParser.RPAREN)
            self.state = 180
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 181
            self.match(MiniGoParser.LPAREN)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 182
                self.funcParams()


            self.state = 185
            self.match(MiniGoParser.RPAREN)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398509497344) != 0):
                self.state = 186
                self.baseType()


            self.state = 189
            self.block()
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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def structFields(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StructFieldsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StructFieldsContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structDefinition




    def structDefinition(self):

        localctx = MiniGoParser.StructDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_structDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(MiniGoParser.STRUCT)
            self.state = 192
            self.match(MiniGoParser.LBRACE)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==54:
                self.state = 193
                self.structFields()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199
            self.match(MiniGoParser.RBRACE)
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

        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structFields




    def structFields(self):

        localctx = MiniGoParser.StructFieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_structFields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 202
            self.baseType()
            self.state = 203
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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def interfaceFields(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.InterfaceFieldsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.InterfaceFieldsContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceDefinition




    def interfaceDefinition(self):

        localctx = MiniGoParser.InterfaceDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_interfaceDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(MiniGoParser.INTERFACE)
            self.state = 206
            self.match(MiniGoParser.LBRACE)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==54:
                self.state = 207
                self.interfaceFields()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 213
            self.match(MiniGoParser.RBRACE)
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

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def listIdentifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ListIdentifierContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ListIdentifierContext,i)


        def baseType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BaseTypeContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_listParams




    def listParams(self):

        localctx = MiniGoParser.ListParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_listParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(MiniGoParser.LPAREN)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==54:
                self.state = 216
                self.listIdentifier()
                self.state = 217
                self.baseType()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 224
            self.match(MiniGoParser.RPAREN)
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
        self.enterRule(localctx, 28, self.RULE_listIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 227
                self.match(MiniGoParser.COMMA)
                self.state = 228
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 233
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


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceFields




    def interfaceFields(self):

        localctx = MiniGoParser.InterfaceFieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_interfaceFields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 235
            self.listParams()
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398509497344) != 0):
                self.state = 236
                self.baseType()


            self.state = 239
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
        self.enterRule(localctx, 32, self.RULE_funcParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.funcParam()
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 242
                self.match(MiniGoParser.COMMA)
                self.state = 243
                self.funcParam()
                self.state = 248
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

        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcParam




    def funcParam(self):

        localctx = MiniGoParser.FuncParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_funcParam)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(MiniGoParser.IDENTIFIER)

            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 250
                self.arrayDims()


            self.state = 253
            self.baseType()
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

        def logicOrExp(self):
            return self.getTypedRuleContext(MiniGoParser.LogicOrExpContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression




    def expression(self):

        localctx = MiniGoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.logicOrExp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicOrExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicAndExp(self):
            return self.getTypedRuleContext(MiniGoParser.LogicAndExpContext,0)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.OR)
            else:
                return self.getToken(MiniGoParser.OR, i)

        def logicOrExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.LogicOrExpContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.LogicOrExpContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_logicOrExp




    def logicOrExp(self):

        localctx = MiniGoParser.LogicOrExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_logicOrExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.logicAndExp()
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 258
                    self.match(MiniGoParser.OR)
                    self.state = 259
                    self.logicOrExp() 
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicAndExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExp(self):
            return self.getTypedRuleContext(MiniGoParser.EqualityExpContext,0)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.AND)
            else:
                return self.getToken(MiniGoParser.AND, i)

        def logicAndExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.LogicAndExpContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.LogicAndExpContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_logicAndExp




    def logicAndExp(self):

        localctx = MiniGoParser.LogicAndExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_logicAndExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.equalityExp()
            self.state = 270
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 266
                    self.match(MiniGoParser.AND)
                    self.state = 267
                    self.logicAndExp() 
                self.state = 272
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.AdditiveExpContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.AdditiveExpContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.EQ)
            else:
                return self.getToken(MiniGoParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEQ)
            else:
                return self.getToken(MiniGoParser.NEQ, i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LT)
            else:
                return self.getToken(MiniGoParser.LT, i)

        def LEQ(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LEQ)
            else:
                return self.getToken(MiniGoParser.LEQ, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.GT)
            else:
                return self.getToken(MiniGoParser.GT, i)

        def GEQ(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.GEQ)
            else:
                return self.getToken(MiniGoParser.GEQ, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_equalityExp




    def equalityExp(self):

        localctx = MiniGoParser.EqualityExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_equalityExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.additiveExp()
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33822867456) != 0):
                self.state = 274
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33822867456) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 275
                self.additiveExp()
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.MultiplicativeExpContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.MultiplicativeExpContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.PLUS)
            else:
                return self.getToken(MiniGoParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.MINUS)
            else:
                return self.getToken(MiniGoParser.MINUS, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_additiveExp




    def additiveExp(self):

        localctx = MiniGoParser.AdditiveExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_additiveExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.multiplicativeExp()
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24 or _la==25:
                self.state = 282
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 283
                self.multiplicativeExp()
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.UnaryExpContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.UnaryExpContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.MUL)
            else:
                return self.getToken(MiniGoParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DIV)
            else:
                return self.getToken(MiniGoParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.MOD)
            else:
                return self.getToken(MiniGoParser.MOD, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_multiplicativeExp




    def multiplicativeExp(self):

        localctx = MiniGoParser.MultiplicativeExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_multiplicativeExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.unaryExp()
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0):
                self.state = 290
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 291
                self.unaryExp()
                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExp(self):
            return self.getTypedRuleContext(MiniGoParser.UnaryExpContext,0)


        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def primaryExp(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExpContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_unaryExp




    def unaryExp(self):

        localctx = MiniGoParser.UnaryExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_unaryExp)
        self._la = 0 # Token type
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                _la = self._input.LA(1)
                if not(_la==25 or _la==37):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 298
                self.unaryExp()
                pass
            elif token in [14, 15, 16, 45, 54, 55, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.primaryExp()
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


    class PrimaryExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(MiniGoParser.TermContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primaryExp




    def primaryExp(self):

        localctx = MiniGoParser.PrimaryExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_primaryExp)
        try:
            self.state = 307
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15, 16, 54, 55, 56, 57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.term()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.match(MiniGoParser.LPAREN)
                self.state = 304
                self.expression()
                self.state = 305
                self.match(MiniGoParser.RPAREN)
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


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def callStatement(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_term




    def term(self):

        localctx = MiniGoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_term)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 311
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 312
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 313
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 314
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 315
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 319
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [49]:
                    self.state = 316
                    self.arrayDims()
                    pass
                elif token in [43]:
                    self.state = 317
                    self.match(MiniGoParser.DOT)
                    self.state = 318
                    self.match(MiniGoParser.IDENTIFIER)
                    pass
                elif token in [-1, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 46, 47, 48, 50, 51, 52, 54, 61]:
                    pass
                else:
                    pass
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 321
                self.callStatement()
                pass


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

        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


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


        def typeDecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypeDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclContext,0)


        def constDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 324
                self.assignStatement()
                pass

            elif la_ == 2:
                self.state = 325
                self.ifStatement()
                pass

            elif la_ == 3:
                self.state = 326
                self.forStatement()
                pass

            elif la_ == 4:
                self.state = 327
                self.breakStatement()
                pass

            elif la_ == 5:
                self.state = 328
                self.continueStatement()
                pass

            elif la_ == 6:
                self.state = 329
                self.callStatement()
                pass

            elif la_ == 7:
                self.state = 330
                self.returnStatement()
                pass

            elif la_ == 8:
                self.state = 331
                self.arrayLiteral()
                pass

            elif la_ == 9:
                self.state = 332
                self.varDecl()
                pass

            elif la_ == 10:
                self.state = 333
                self.typeDecl()
                pass

            elif la_ == 11:
                self.state = 334
                self.methodDecl()
                pass

            elif la_ == 12:
                self.state = 335
                self.constDecl()
                pass


            self.state = 338
            self.endOfStatement()
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

        def DECLARE(self):
            return self.getToken(MiniGoParser.DECLARE, 0)

        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def arraysBlock(self):
            return self.getTypedRuleContext(MiniGoParser.ArraysBlockContext,0)


        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLiteral




    def arrayLiteral(self):

        localctx = MiniGoParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_arrayLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 341
            self.match(MiniGoParser.DECLARE)

            self.state = 342
            self.arrayDims()
            self.state = 343
            self.baseType()
            self.state = 344
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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def arraysBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ArraysBlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ArraysBlockContext,i)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

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
        self.enterRule(localctx, 58, self.RULE_arraysBlock)
        self._la = 0 # Token type
        try:
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.match(MiniGoParser.LBRACE)
                self.state = 347
                self.arraysBlock()
                self.state = 352
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==51:
                    self.state = 348
                    self.match(MiniGoParser.COMMA)
                    self.state = 349
                    self.arraysBlock()
                    self.state = 354
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 355
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.match(MiniGoParser.LBRACE)
                self.state = 358
                self.expression()
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==51:
                    self.state = 359
                    self.match(MiniGoParser.COMMA)
                    self.state = 360
                    self.expression()
                    self.state = 365
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 366
                self.match(MiniGoParser.RBRACE)
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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

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
        self.enterRule(localctx, 60, self.RULE_structExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 371
            self.match(MiniGoParser.LBRACE)
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==54:
                self.state = 372
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 373
                self.match(MiniGoParser.COLON)
                self.state = 374
                self.expression()
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==51:
                    self.state = 375
                    self.match(MiniGoParser.COMMA)


                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 383
            self.match(MiniGoParser.RBRACE)
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
        self.enterRule(localctx, 62, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.state = 386
                self.arrayDims()
                pass
            elif token in [43]:
                self.state = 387
                self.match(MiniGoParser.DOT)
                self.state = 388
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [23, 38, 39, 40, 41, 42]:
                pass
            else:
                pass
            self.state = 391
            self.assignmentOperator()
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 392
                self.expression()
                pass

            elif la_ == 2:
                self.state = 393
                self.structExpression()
                pass


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

        def DECLARE(self):
            return self.getToken(MiniGoParser.DECLARE, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(MiniGoParser.PLUS_ASSIGN, 0)

        def MINUS_ASSIGN(self):
            return self.getToken(MiniGoParser.MINUS_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignmentOperator




    def assignmentOperator(self):

        localctx = MiniGoParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8521223503872) != 0)):
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ELSE)
            else:
                return self.getToken(MiniGoParser.ELSE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ifStatement




    def ifStatement(self):

        localctx = MiniGoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(MiniGoParser.IF)
            self.state = 399
            self.expression()
            self.state = 400
            self.block()
            self.state = 408
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 401
                    self.match(MiniGoParser.ELSE)
                    self.state = 402
                    self.match(MiniGoParser.IF)
                    self.state = 403
                    self.expression()
                    self.state = 404
                    self.block() 
                self.state = 410
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 411
                self.match(MiniGoParser.ELSE)
                self.state = 412
                self.block()


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
        self.enterRule(localctx, 68, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(MiniGoParser.FOR)
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 416
                self.forLoop()
                pass

            elif la_ == 2:
                self.state = 417
                self.forIteration()
                pass


            self.state = 420
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
        self.enterRule(localctx, 70, self.RULE_forLoop)
        try:
            self.state = 429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.forCondition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.initilization()
                self.state = 424
                self.match(MiniGoParser.SEMI)
                self.state = 425
                self.forCondition()
                self.state = 426
                self.match(MiniGoParser.SEMI)
                self.state = 427
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

        def DECLARE(self):
            return self.getToken(MiniGoParser.DECLARE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_initilization




    def initilization(self):

        localctx = MiniGoParser.InitilizationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_initilization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 432
            self.match(MiniGoParser.DECLARE)
            self.state = 433
            self.expression()
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
        self.enterRule(localctx, 74, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.expression()
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
        self.enterRule(localctx, 76, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 438
            self.assignmentOperator()
            self.state = 439
            self.expression()
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

        def DECLARE(self):
            return self.getToken(MiniGoParser.DECLARE, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def BLANK(self):
            return self.getToken(MiniGoParser.BLANK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_forIteration




    def forIteration(self):

        localctx = MiniGoParser.ForIterationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_forIteration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            _la = self._input.LA(1)
            if not(_la==44 or _la==54):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 442
            self.match(MiniGoParser.COMMA)
            self.state = 443
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 444
            self.match(MiniGoParser.DECLARE)
            self.state = 445
            self.match(MiniGoParser.RANGE)
            self.state = 446
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

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakStatement




    def breakStatement(self):

        localctx = MiniGoParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(MiniGoParser.BREAK)
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

        def getRuleIndex(self):
            return MiniGoParser.RULE_continueStatement




    def continueStatement(self):

        localctx = MiniGoParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(MiniGoParser.CONTINUE)
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

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

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
        self.enterRule(localctx, 84, self.RULE_callStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 453
                self.match(MiniGoParser.DOT)
                self.state = 454
                self.match(MiniGoParser.IDENTIFIER)


            self.state = 457
            self.match(MiniGoParser.LPAREN)
            self.state = 466
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 270251299486941184) != 0):
                self.state = 458
                self.expression()
                self.state = 463
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==51:
                    self.state = 459
                    self.match(MiniGoParser.COMMA)
                    self.state = 460
                    self.expression()
                    self.state = 465
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 468
            self.match(MiniGoParser.RPAREN)
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

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStatement




    def returnStatement(self):

        localctx = MiniGoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(MiniGoParser.RETURN)
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 270251299486941184) != 0):
                self.state = 471
                self.expression()


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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(MiniGoParser.LBRACE)
            self.state = 478
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398511448308) != 0):
                self.state = 475
                self.statement()
                self.state = 480
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 481
            self.match(MiniGoParser.RBRACE)
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

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACKET)
            else:
                return self.getToken(MiniGoParser.LBRACKET, i)

        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACKET)
            else:
                return self.getToken(MiniGoParser.RBRACKET, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayDims




    def arrayDims(self):

        localctx = MiniGoParser.ArrayDimsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_arrayDims)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 483
                self.match(MiniGoParser.LBRACKET)
                self.state = 485
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 270251299486941184) != 0):
                    self.state = 484
                    self.expression()


                self.state = 487
                self.match(MiniGoParser.RBRACKET)
                self.state = 490 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==49):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





