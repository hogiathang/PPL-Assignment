# Generated from d:/HK242/PPL/Assignment/B1/PPL-ASSIGNMENT1-V4/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
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
        4,1,63,600,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        1,0,1,0,4,0,109,8,0,11,0,12,0,110,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,134,8,
        3,1,4,1,4,1,4,1,4,5,4,140,8,4,10,4,12,4,143,9,4,1,4,3,4,146,8,4,
        1,4,1,4,3,4,150,8,4,1,4,1,4,3,4,154,8,4,1,5,1,5,1,5,1,5,3,5,160,
        8,5,1,5,1,5,3,5,164,8,5,1,5,3,5,167,8,5,1,5,1,5,5,5,171,8,5,10,5,
        12,5,174,9,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,182,8,6,1,7,1,7,1,7,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,197,8,8,1,8,1,8,3,8,201,
        8,8,1,8,1,8,1,9,1,9,1,9,5,9,208,8,9,10,9,12,9,211,9,9,1,9,1,9,1,
        10,1,10,3,10,217,8,10,1,10,1,10,3,10,221,8,10,1,10,1,10,1,11,1,11,
        1,11,5,11,228,8,11,10,11,12,11,231,9,11,1,11,1,11,1,12,1,12,3,12,
        237,8,12,1,12,1,12,1,13,1,13,1,13,5,13,244,8,13,10,13,12,13,247,
        9,13,1,14,1,14,1,14,5,14,252,8,14,10,14,12,14,255,9,14,1,14,1,14,
        1,15,1,15,1,15,3,15,262,8,15,1,15,1,15,1,16,1,16,1,16,5,16,269,8,
        16,10,16,12,16,272,9,16,1,17,1,17,3,17,276,8,17,1,17,1,17,1,18,1,
        18,1,19,1,19,1,19,5,19,285,8,19,10,19,12,19,288,9,19,1,20,1,20,1,
        20,5,20,293,8,20,10,20,12,20,296,9,20,1,21,1,21,1,21,5,21,301,8,
        21,10,21,12,21,304,9,21,1,22,1,22,1,22,5,22,309,8,22,10,22,12,22,
        312,9,22,1,23,1,23,1,23,5,23,317,8,23,10,23,12,23,320,9,23,1,24,
        5,24,323,8,24,10,24,12,24,326,9,24,1,24,1,24,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,344,8,25,
        1,25,5,25,347,8,25,10,25,12,25,350,9,25,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,3,26,359,8,26,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,3,28,399,8,28,1,29,1,29,1,29,1,29,1,30,1,30,
        1,30,1,30,5,30,409,8,30,10,30,12,30,412,9,30,1,30,1,30,1,30,1,30,
        1,30,1,30,5,30,420,8,30,10,30,12,30,423,9,30,1,30,1,30,3,30,427,
        8,30,1,31,1,31,1,31,1,31,1,31,5,31,434,8,31,10,31,12,31,437,9,31,
        1,31,3,31,440,8,31,3,31,442,8,31,1,31,1,31,1,32,1,32,1,32,3,32,449,
        8,32,1,33,1,33,1,33,1,33,1,34,1,34,1,34,5,34,458,8,34,10,34,12,34,
        461,9,34,1,34,1,34,1,34,1,34,5,34,467,8,34,10,34,12,34,470,9,34,
        1,35,1,35,3,35,474,8,35,1,35,1,35,1,35,1,35,3,35,480,8,35,3,35,482,
        8,35,1,36,1,36,1,36,3,36,487,8,36,1,37,1,37,1,38,1,38,1,38,1,38,
        3,38,495,8,38,1,38,1,38,1,38,1,38,1,38,3,38,502,8,38,5,38,504,8,
        38,10,38,12,38,507,9,38,1,38,1,38,3,38,511,8,38,1,39,1,39,1,39,3,
        39,516,8,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,3,40,527,
        8,40,1,41,1,41,1,41,1,41,1,42,1,42,1,43,1,43,1,43,1,43,1,44,1,44,
        1,44,1,44,1,44,1,44,1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,47,3,47,
        553,8,47,1,47,1,47,1,48,1,48,3,48,559,8,48,1,48,1,48,1,48,1,48,1,
        48,3,48,566,8,48,3,48,568,8,48,1,49,1,49,1,49,3,49,573,8,49,1,50,
        1,50,1,50,5,50,578,8,50,10,50,12,50,581,9,50,1,51,1,51,4,51,585,
        8,51,11,51,12,51,586,1,51,1,51,1,52,1,52,3,52,593,8,52,1,52,4,52,
        596,8,52,11,52,12,52,597,1,52,0,1,50,53,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,
        64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,
        0,9,2,0,9,12,53,53,2,0,51,51,60,60,1,0,28,33,1,0,23,24,1,0,25,27,
        2,0,24,24,36,36,2,0,13,15,54,56,2,0,22,22,37,41,2,0,43,43,53,53,
        628,0,108,1,0,0,0,2,114,1,0,0,0,4,116,1,0,0,0,6,133,1,0,0,0,8,135,
        1,0,0,0,10,155,1,0,0,0,12,177,1,0,0,0,14,183,1,0,0,0,16,188,1,0,
        0,0,18,204,1,0,0,0,20,214,1,0,0,0,22,224,1,0,0,0,24,234,1,0,0,0,
        26,240,1,0,0,0,28,248,1,0,0,0,30,258,1,0,0,0,32,265,1,0,0,0,34,273,
        1,0,0,0,36,279,1,0,0,0,38,281,1,0,0,0,40,289,1,0,0,0,42,297,1,0,
        0,0,44,305,1,0,0,0,46,313,1,0,0,0,48,324,1,0,0,0,50,329,1,0,0,0,
        52,358,1,0,0,0,54,360,1,0,0,0,56,398,1,0,0,0,58,400,1,0,0,0,60,426,
        1,0,0,0,62,428,1,0,0,0,64,448,1,0,0,0,66,450,1,0,0,0,68,454,1,0,
        0,0,70,481,1,0,0,0,72,486,1,0,0,0,74,488,1,0,0,0,76,490,1,0,0,0,
        78,512,1,0,0,0,80,526,1,0,0,0,82,528,1,0,0,0,84,532,1,0,0,0,86,534,
        1,0,0,0,88,538,1,0,0,0,90,545,1,0,0,0,92,547,1,0,0,0,94,549,1,0,
        0,0,96,567,1,0,0,0,98,569,1,0,0,0,100,574,1,0,0,0,102,582,1,0,0,
        0,104,595,1,0,0,0,106,109,3,6,3,0,107,109,3,56,28,0,108,106,1,0,
        0,0,108,107,1,0,0,0,109,110,1,0,0,0,110,108,1,0,0,0,110,111,1,0,
        0,0,111,112,1,0,0,0,112,113,5,0,0,1,113,1,1,0,0,0,114,115,7,0,0,
        0,115,3,1,0,0,0,116,117,7,1,0,0,117,5,1,0,0,0,118,119,3,8,4,0,119,
        120,3,4,2,0,120,134,1,0,0,0,121,122,3,10,5,0,122,123,3,4,2,0,123,
        134,1,0,0,0,124,125,3,12,6,0,125,126,3,4,2,0,126,134,1,0,0,0,127,
        128,3,14,7,0,128,129,3,4,2,0,129,134,1,0,0,0,130,131,3,16,8,0,131,
        132,3,4,2,0,132,134,1,0,0,0,133,118,1,0,0,0,133,121,1,0,0,0,133,
        124,1,0,0,0,133,127,1,0,0,0,133,130,1,0,0,0,134,7,1,0,0,0,135,136,
        5,17,0,0,136,141,5,53,0,0,137,138,5,50,0,0,138,140,5,53,0,0,139,
        137,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,
        145,1,0,0,0,143,141,1,0,0,0,144,146,3,104,52,0,145,144,1,0,0,0,145,
        146,1,0,0,0,146,153,1,0,0,0,147,154,3,2,1,0,148,150,3,2,1,0,149,
        148,1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,152,5,21,0,0,152,
        154,3,36,18,0,153,147,1,0,0,0,153,149,1,0,0,0,154,9,1,0,0,0,155,
        156,5,5,0,0,156,157,5,53,0,0,157,159,5,44,0,0,158,160,3,32,16,0,
        159,158,1,0,0,0,159,160,1,0,0,0,160,161,1,0,0,0,161,166,5,45,0,0,
        162,164,3,104,52,0,163,162,1,0,0,0,163,164,1,0,0,0,164,165,1,0,0,
        0,165,167,3,2,1,0,166,163,1,0,0,0,166,167,1,0,0,0,167,168,1,0,0,
        0,168,172,5,46,0,0,169,171,3,56,28,0,170,169,1,0,0,0,171,174,1,0,
        0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,175,1,0,0,0,174,172,1,0,
        0,0,175,176,5,47,0,0,176,11,1,0,0,0,177,178,5,6,0,0,178,181,5,53,
        0,0,179,182,3,18,9,0,180,182,3,22,11,0,181,179,1,0,0,0,181,180,1,
        0,0,0,182,13,1,0,0,0,183,184,5,16,0,0,184,185,5,53,0,0,185,186,5,
        21,0,0,186,187,3,36,18,0,187,15,1,0,0,0,188,189,5,5,0,0,189,190,
        5,44,0,0,190,191,5,53,0,0,191,192,5,53,0,0,192,193,5,45,0,0,193,
        194,5,53,0,0,194,196,5,44,0,0,195,197,3,32,16,0,196,195,1,0,0,0,
        196,197,1,0,0,0,197,198,1,0,0,0,198,200,5,45,0,0,199,201,3,2,1,0,
        200,199,1,0,0,0,200,201,1,0,0,0,201,202,1,0,0,0,202,203,3,102,51,
        0,203,17,1,0,0,0,204,205,5,7,0,0,205,209,5,46,0,0,206,208,3,20,10,
        0,207,206,1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,
        0,210,212,1,0,0,0,211,209,1,0,0,0,212,213,5,47,0,0,213,19,1,0,0,
        0,214,220,5,53,0,0,215,217,3,104,52,0,216,215,1,0,0,0,216,217,1,
        0,0,0,217,218,1,0,0,0,218,221,3,2,1,0,219,221,3,18,9,0,220,216,1,
        0,0,0,220,219,1,0,0,0,221,222,1,0,0,0,222,223,3,4,2,0,223,21,1,0,
        0,0,224,225,5,8,0,0,225,229,5,46,0,0,226,228,3,30,15,0,227,226,1,
        0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,232,1,
        0,0,0,231,229,1,0,0,0,232,233,5,47,0,0,233,23,1,0,0,0,234,236,5,
        44,0,0,235,237,3,26,13,0,236,235,1,0,0,0,236,237,1,0,0,0,237,238,
        1,0,0,0,238,239,5,45,0,0,239,25,1,0,0,0,240,245,3,28,14,0,241,242,
        5,50,0,0,242,244,3,28,14,0,243,241,1,0,0,0,244,247,1,0,0,0,245,243,
        1,0,0,0,245,246,1,0,0,0,246,27,1,0,0,0,247,245,1,0,0,0,248,253,5,
        53,0,0,249,250,5,50,0,0,250,252,5,53,0,0,251,249,1,0,0,0,252,255,
        1,0,0,0,253,251,1,0,0,0,253,254,1,0,0,0,254,256,1,0,0,0,255,253,
        1,0,0,0,256,257,3,2,1,0,257,29,1,0,0,0,258,259,5,53,0,0,259,261,
        3,24,12,0,260,262,3,2,1,0,261,260,1,0,0,0,261,262,1,0,0,0,262,263,
        1,0,0,0,263,264,3,4,2,0,264,31,1,0,0,0,265,270,3,34,17,0,266,267,
        5,50,0,0,267,269,3,34,17,0,268,266,1,0,0,0,269,272,1,0,0,0,270,268,
        1,0,0,0,270,271,1,0,0,0,271,33,1,0,0,0,272,270,1,0,0,0,273,275,5,
        53,0,0,274,276,3,104,52,0,275,274,1,0,0,0,275,276,1,0,0,0,276,277,
        1,0,0,0,277,278,3,2,1,0,278,35,1,0,0,0,279,280,3,38,19,0,280,37,
        1,0,0,0,281,286,3,40,20,0,282,283,5,35,0,0,283,285,3,38,19,0,284,
        282,1,0,0,0,285,288,1,0,0,0,286,284,1,0,0,0,286,287,1,0,0,0,287,
        39,1,0,0,0,288,286,1,0,0,0,289,294,3,42,21,0,290,291,5,34,0,0,291,
        293,3,40,20,0,292,290,1,0,0,0,293,296,1,0,0,0,294,292,1,0,0,0,294,
        295,1,0,0,0,295,41,1,0,0,0,296,294,1,0,0,0,297,302,3,44,22,0,298,
        299,7,2,0,0,299,301,3,44,22,0,300,298,1,0,0,0,301,304,1,0,0,0,302,
        300,1,0,0,0,302,303,1,0,0,0,303,43,1,0,0,0,304,302,1,0,0,0,305,310,
        3,46,23,0,306,307,7,3,0,0,307,309,3,46,23,0,308,306,1,0,0,0,309,
        312,1,0,0,0,310,308,1,0,0,0,310,311,1,0,0,0,311,45,1,0,0,0,312,310,
        1,0,0,0,313,318,3,48,24,0,314,315,7,4,0,0,315,317,3,48,24,0,316,
        314,1,0,0,0,317,320,1,0,0,0,318,316,1,0,0,0,318,319,1,0,0,0,319,
        47,1,0,0,0,320,318,1,0,0,0,321,323,7,5,0,0,322,321,1,0,0,0,323,326,
        1,0,0,0,324,322,1,0,0,0,324,325,1,0,0,0,325,327,1,0,0,0,326,324,
        1,0,0,0,327,328,3,50,25,0,328,49,1,0,0,0,329,330,6,25,-1,0,330,331,
        3,52,26,0,331,348,1,0,0,0,332,333,10,3,0,0,333,334,5,48,0,0,334,
        335,3,36,18,0,335,336,5,49,0,0,336,347,1,0,0,0,337,338,10,2,0,0,
        338,339,5,42,0,0,339,347,5,53,0,0,340,341,10,1,0,0,341,343,5,44,
        0,0,342,344,3,100,50,0,343,342,1,0,0,0,343,344,1,0,0,0,344,345,1,
        0,0,0,345,347,5,45,0,0,346,332,1,0,0,0,346,337,1,0,0,0,346,340,1,
        0,0,0,347,350,1,0,0,0,348,346,1,0,0,0,348,349,1,0,0,0,349,51,1,0,
        0,0,350,348,1,0,0,0,351,352,5,44,0,0,352,353,3,36,18,0,353,354,5,
        45,0,0,354,359,1,0,0,0,355,359,3,54,27,0,356,359,3,96,48,0,357,359,
        5,53,0,0,358,351,1,0,0,0,358,355,1,0,0,0,358,356,1,0,0,0,358,357,
        1,0,0,0,359,53,1,0,0,0,360,361,7,6,0,0,361,55,1,0,0,0,362,363,3,
        68,34,0,363,364,3,4,2,0,364,399,1,0,0,0,365,366,3,76,38,0,366,367,
        3,4,2,0,367,399,1,0,0,0,368,369,3,78,39,0,369,370,3,4,2,0,370,399,
        1,0,0,0,371,372,3,90,45,0,372,373,3,4,2,0,373,399,1,0,0,0,374,375,
        3,92,46,0,375,376,3,4,2,0,376,399,1,0,0,0,377,378,3,96,48,0,378,
        379,3,4,2,0,379,399,1,0,0,0,380,381,3,98,49,0,381,382,3,4,2,0,382,
        399,1,0,0,0,383,384,3,8,4,0,384,385,3,4,2,0,385,399,1,0,0,0,386,
        387,3,12,6,0,387,388,3,4,2,0,388,399,1,0,0,0,389,390,3,16,8,0,390,
        391,3,4,2,0,391,399,1,0,0,0,392,393,3,14,7,0,393,394,3,4,2,0,394,
        399,1,0,0,0,395,396,3,102,51,0,396,397,3,4,2,0,397,399,1,0,0,0,398,
        362,1,0,0,0,398,365,1,0,0,0,398,368,1,0,0,0,398,371,1,0,0,0,398,
        374,1,0,0,0,398,377,1,0,0,0,398,380,1,0,0,0,398,383,1,0,0,0,398,
        386,1,0,0,0,398,389,1,0,0,0,398,392,1,0,0,0,398,395,1,0,0,0,399,
        57,1,0,0,0,400,401,3,104,52,0,401,402,3,2,1,0,402,403,3,60,30,0,
        403,59,1,0,0,0,404,405,5,46,0,0,405,410,3,60,30,0,406,407,5,50,0,
        0,407,409,3,60,30,0,408,406,1,0,0,0,409,412,1,0,0,0,410,408,1,0,
        0,0,410,411,1,0,0,0,411,413,1,0,0,0,412,410,1,0,0,0,413,414,5,47,
        0,0,414,427,1,0,0,0,415,416,5,46,0,0,416,421,3,36,18,0,417,418,5,
        50,0,0,418,420,3,36,18,0,419,417,1,0,0,0,420,423,1,0,0,0,421,419,
        1,0,0,0,421,422,1,0,0,0,422,424,1,0,0,0,423,421,1,0,0,0,424,425,
        5,47,0,0,425,427,1,0,0,0,426,404,1,0,0,0,426,415,1,0,0,0,427,61,
        1,0,0,0,428,429,5,53,0,0,429,441,5,46,0,0,430,435,3,66,33,0,431,
        432,5,50,0,0,432,434,3,66,33,0,433,431,1,0,0,0,434,437,1,0,0,0,435,
        433,1,0,0,0,435,436,1,0,0,0,436,439,1,0,0,0,437,435,1,0,0,0,438,
        440,5,50,0,0,439,438,1,0,0,0,439,440,1,0,0,0,440,442,1,0,0,0,441,
        430,1,0,0,0,441,442,1,0,0,0,442,443,1,0,0,0,443,444,5,47,0,0,444,
        63,1,0,0,0,445,449,3,36,18,0,446,449,3,58,29,0,447,449,3,62,31,0,
        448,445,1,0,0,0,448,446,1,0,0,0,448,447,1,0,0,0,449,65,1,0,0,0,450,
        451,5,53,0,0,451,452,5,52,0,0,452,453,3,64,32,0,453,67,1,0,0,0,454,
        459,3,70,35,0,455,456,5,50,0,0,456,458,3,70,35,0,457,455,1,0,0,0,
        458,461,1,0,0,0,459,457,1,0,0,0,459,460,1,0,0,0,460,462,1,0,0,0,
        461,459,1,0,0,0,462,463,3,74,37,0,463,468,3,72,36,0,464,465,5,50,
        0,0,465,467,3,72,36,0,466,464,1,0,0,0,467,470,1,0,0,0,468,466,1,
        0,0,0,468,469,1,0,0,0,469,69,1,0,0,0,470,468,1,0,0,0,471,474,3,96,
        48,0,472,474,5,53,0,0,473,471,1,0,0,0,473,472,1,0,0,0,474,475,1,
        0,0,0,475,476,5,42,0,0,476,482,3,70,35,0,477,479,5,53,0,0,478,480,
        3,104,52,0,479,478,1,0,0,0,479,480,1,0,0,0,480,482,1,0,0,0,481,473,
        1,0,0,0,481,477,1,0,0,0,482,71,1,0,0,0,483,487,3,36,18,0,484,487,
        3,58,29,0,485,487,3,62,31,0,486,483,1,0,0,0,486,484,1,0,0,0,486,
        485,1,0,0,0,487,73,1,0,0,0,488,489,7,7,0,0,489,75,1,0,0,0,490,491,
        5,1,0,0,491,492,3,36,18,0,492,494,3,102,51,0,493,495,5,60,0,0,494,
        493,1,0,0,0,494,495,1,0,0,0,495,505,1,0,0,0,496,497,5,2,0,0,497,
        498,5,1,0,0,498,499,3,36,18,0,499,501,3,102,51,0,500,502,5,60,0,
        0,501,500,1,0,0,0,501,502,1,0,0,0,502,504,1,0,0,0,503,496,1,0,0,
        0,504,507,1,0,0,0,505,503,1,0,0,0,505,506,1,0,0,0,506,510,1,0,0,
        0,507,505,1,0,0,0,508,509,5,2,0,0,509,511,3,102,51,0,510,508,1,0,
        0,0,510,511,1,0,0,0,511,77,1,0,0,0,512,515,5,3,0,0,513,516,3,80,
        40,0,514,516,3,88,44,0,515,513,1,0,0,0,515,514,1,0,0,0,516,517,1,
        0,0,0,517,518,3,102,51,0,518,79,1,0,0,0,519,527,3,84,42,0,520,521,
        3,82,41,0,521,522,5,51,0,0,522,523,3,84,42,0,523,524,5,51,0,0,524,
        525,3,86,43,0,525,527,1,0,0,0,526,519,1,0,0,0,526,520,1,0,0,0,527,
        81,1,0,0,0,528,529,5,53,0,0,529,530,5,22,0,0,530,531,3,36,18,0,531,
        83,1,0,0,0,532,533,3,36,18,0,533,85,1,0,0,0,534,535,5,53,0,0,535,
        536,3,74,37,0,536,537,3,36,18,0,537,87,1,0,0,0,538,539,7,8,0,0,539,
        540,5,50,0,0,540,541,5,53,0,0,541,542,5,22,0,0,542,543,5,20,0,0,
        543,544,5,53,0,0,544,89,1,0,0,0,545,546,5,19,0,0,546,91,1,0,0,0,
        547,548,5,18,0,0,548,93,1,0,0,0,549,550,5,53,0,0,550,552,5,44,0,
        0,551,553,3,100,50,0,552,551,1,0,0,0,552,553,1,0,0,0,553,554,1,0,
        0,0,554,555,5,45,0,0,555,95,1,0,0,0,556,558,5,53,0,0,557,559,3,104,
        52,0,558,557,1,0,0,0,558,559,1,0,0,0,559,560,1,0,0,0,560,561,5,42,
        0,0,561,568,3,96,48,0,562,565,3,94,47,0,563,564,5,42,0,0,564,566,
        3,96,48,0,565,563,1,0,0,0,565,566,1,0,0,0,566,568,1,0,0,0,567,556,
        1,0,0,0,567,562,1,0,0,0,568,97,1,0,0,0,569,572,5,4,0,0,570,573,3,
        36,18,0,571,573,3,58,29,0,572,570,1,0,0,0,572,571,1,0,0,0,572,573,
        1,0,0,0,573,99,1,0,0,0,574,579,3,36,18,0,575,576,5,50,0,0,576,578,
        3,36,18,0,577,575,1,0,0,0,578,581,1,0,0,0,579,577,1,0,0,0,579,580,
        1,0,0,0,580,101,1,0,0,0,581,579,1,0,0,0,582,584,5,46,0,0,583,585,
        3,56,28,0,584,583,1,0,0,0,585,586,1,0,0,0,586,584,1,0,0,0,586,587,
        1,0,0,0,587,588,1,0,0,0,588,589,5,47,0,0,589,103,1,0,0,0,590,592,
        5,48,0,0,591,593,3,36,18,0,592,591,1,0,0,0,592,593,1,0,0,0,593,594,
        1,0,0,0,594,596,5,49,0,0,595,590,1,0,0,0,596,597,1,0,0,0,597,595,
        1,0,0,0,597,598,1,0,0,0,598,105,1,0,0,0,63,108,110,133,141,145,149,
        153,159,163,166,172,181,196,200,209,216,220,229,236,245,253,261,
        270,275,286,294,302,310,318,324,343,346,348,358,398,410,421,426,
        435,439,441,448,459,468,473,479,481,486,494,501,505,510,515,526,
        552,558,565,567,572,579,586,592,597
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
                     "'%='", "'.'", "'_'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "','", "';'", "':'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "TRUE", "FALSE", "NIL", "CONST", "VAR", 
                      "CONTINUE", "BREAK", "RANGE", "ASSIGN", "DECLARE", 
                      "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQ", "NEQ", 
                      "LT", "LEQ", "GT", "GEQ", "AND", "OR", "NOT", "PLUS_ASSIGN", 
                      "MINUS_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "DOT", "BLANK", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACKET", "RBRACKET", "COMMA", "SEMI", "COLON", 
                      "IDENTIFIER", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "BLOCK_COMMENT", "LINE_COMMENT", "WS", "NEWLINE", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_baseType = 1
    RULE_endOfStatement = 2
    RULE_declaration = 3
    RULE_varDecl = 4
    RULE_funcDecl = 5
    RULE_typeDecl = 6
    RULE_constDecl = 7
    RULE_methodDecl = 8
    RULE_structDefinition = 9
    RULE_structFields = 10
    RULE_interfaceDefinition = 11
    RULE_listParams = 12
    RULE_listIdentifier = 13
    RULE_listGroup = 14
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
    RULE_postfixExp = 25
    RULE_primaryExp = 26
    RULE_literal = 27
    RULE_statement = 28
    RULE_arrayLit = 29
    RULE_arraysBlock = 30
    RULE_structExpression = 31
    RULE_structBlock = 32
    RULE_structFieldsAssign = 33
    RULE_assignStatement = 34
    RULE_a1 = 35
    RULE_a2 = 36
    RULE_assignmentOperator = 37
    RULE_ifStatement = 38
    RULE_forStatement = 39
    RULE_forLoop = 40
    RULE_initilization = 41
    RULE_forCondition = 42
    RULE_forUpdate = 43
    RULE_forIteration = 44
    RULE_breakStatement = 45
    RULE_continueStatement = 46
    RULE_primaryCall = 47
    RULE_callStatement = 48
    RULE_returnStatement = 49
    RULE_arguments = 50
    RULE_block = 51
    RULE_arrayDims = 52

    ruleNames =  [ "program", "baseType", "endOfStatement", "declaration", 
                   "varDecl", "funcDecl", "typeDecl", "constDecl", "methodDecl", 
                   "structDefinition", "structFields", "interfaceDefinition", 
                   "listParams", "listIdentifier", "listGroup", "interfaceFields", 
                   "funcParams", "funcParam", "expression", "logicOrExp", 
                   "logicAndExp", "equalityExp", "additiveExp", "multiplicativeExp", 
                   "unaryExp", "postfixExp", "primaryExp", "literal", "statement", 
                   "arrayLit", "arraysBlock", "structExpression", "structBlock", 
                   "structFieldsAssign", "assignStatement", "a1", "a2", 
                   "assignmentOperator", "ifStatement", "forStatement", 
                   "forLoop", "initilization", "forCondition", "forUpdate", 
                   "forIteration", "breakStatement", "continueStatement", 
                   "primaryCall", "callStatement", "returnStatement", "arguments", 
                   "block", "arrayDims" ]

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
    BLANK=43
    LPAREN=44
    RPAREN=45
    LBRACE=46
    RBRACE=47
    LBRACKET=48
    RBRACKET=49
    COMMA=50
    SEMI=51
    COLON=52
    IDENTIFIER=53
    INT_LIT=54
    FLOAT_LIT=55
    STRING_LIT=56
    BLOCK_COMMENT=57
    LINE_COMMENT=58
    WS=59
    NEWLINE=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62
    ERROR_CHAR=63

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


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 108
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 106
                    self.declaration()
                    pass

                elif la_ == 2:
                    self.state = 107
                    self.statement()
                    pass


                self.state = 110 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 9077567999901818) != 0)):
                    break

            self.state = 112
            self.match(MiniGoParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 9007199254748672) != 0)):
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

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_endOfStatement




    def endOfStatement(self):

        localctx = MiniGoParser.EndOfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_endOfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            _la = self._input.LA(1)
            if not(_la==51 or _la==60):
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

        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


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
        self.enterRule(localctx, 6, self.RULE_declaration)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.varDecl()
                self.state = 119
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.funcDecl()
                self.state = 122
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.typeDecl()
                self.state = 125
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.constDecl()
                self.state = 128
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 130
                self.methodDecl()
                self.state = 131
                self.endOfStatement()
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
        self.enterRule(localctx, 8, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(MiniGoParser.VAR)
            self.state = 136
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 137
                self.match(MiniGoParser.COMMA)
                self.state = 138
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 144
                self.arrayDims()


            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 147
                self.baseType()
                pass

            elif la_ == 2:
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9007199254748672) != 0):
                    self.state = 148
                    self.baseType()


                self.state = 151
                self.match(MiniGoParser.ASSIGN)
                self.state = 152
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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def funcParams(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamsContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcDecl




    def funcDecl(self):

        localctx = MiniGoParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(MiniGoParser.FUNC)
            self.state = 156
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 157
            self.match(MiniGoParser.LPAREN)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 158
                self.funcParams()


            self.state = 161
            self.match(MiniGoParser.RPAREN)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9288674231459328) != 0):
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 162
                    self.arrayDims()


                self.state = 165
                self.baseType()


            self.state = 168
            self.match(MiniGoParser.LBRACE)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 9077567999901818) != 0):
                self.state = 169
                self.statement()
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 175
            self.match(MiniGoParser.RBRACE)
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
        self.enterRule(localctx, 12, self.RULE_typeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(MiniGoParser.TYPE)
            self.state = 178
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 179
                self.structDefinition()
                pass
            elif token in [8]:
                self.state = 180
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
        self.enterRule(localctx, 14, self.RULE_constDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(MiniGoParser.CONST)
            self.state = 184
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 185
            self.match(MiniGoParser.ASSIGN)
            self.state = 186
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
        self.enterRule(localctx, 16, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(MiniGoParser.FUNC)
            self.state = 189
            self.match(MiniGoParser.LPAREN)
            self.state = 190
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 191
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 192
            self.match(MiniGoParser.RPAREN)
            self.state = 193
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 194
            self.match(MiniGoParser.LPAREN)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 195
                self.funcParams()


            self.state = 198
            self.match(MiniGoParser.RPAREN)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9007199254748672) != 0):
                self.state = 199
                self.baseType()


            self.state = 202
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
        self.enterRule(localctx, 18, self.RULE_structDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(MiniGoParser.STRUCT)
            self.state = 205
            self.match(MiniGoParser.LBRACE)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 206
                self.structFields()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 212
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

        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def structDefinition(self):
            return self.getTypedRuleContext(MiniGoParser.StructDefinitionContext,0)


        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structFields




    def structFields(self):

        localctx = MiniGoParser.StructFieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_structFields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12, 48, 53]:
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 215
                    self.arrayDims()


                self.state = 218
                self.baseType()
                pass
            elif token in [7]:
                self.state = 219
                self.structDefinition()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 222
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
        self.enterRule(localctx, 22, self.RULE_interfaceDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(MiniGoParser.INTERFACE)
            self.state = 225
            self.match(MiniGoParser.LBRACE)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 226
                self.interfaceFields()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 232
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

        def listIdentifier(self):
            return self.getTypedRuleContext(MiniGoParser.ListIdentifierContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_listParams




    def listParams(self):

        localctx = MiniGoParser.ListParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_listParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(MiniGoParser.LPAREN)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 235
                self.listIdentifier()


            self.state = 238
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

        def listGroup(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ListGroupContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ListGroupContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_listIdentifier




    def listIdentifier(self):

        localctx = MiniGoParser.ListIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_listIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.listGroup()
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 241
                self.match(MiniGoParser.COMMA)
                self.state = 242
                self.listGroup()
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListGroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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

        def getRuleIndex(self):
            return MiniGoParser.RULE_listGroup




    def listGroup(self):

        localctx = MiniGoParser.ListGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listGroup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 249
                self.match(MiniGoParser.COMMA)
                self.state = 250
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 256
            self.baseType()
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
            self.state = 258
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 259
            self.listParams()
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9007199254748672) != 0):
                self.state = 260
                self.baseType()


            self.state = 263
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
            self.state = 265
            self.funcParam()
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 266
                self.match(MiniGoParser.COMMA)
                self.state = 267
                self.funcParam()
                self.state = 272
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
            self.state = 273
            self.match(MiniGoParser.IDENTIFIER)

            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 274
                self.arrayDims()


            self.state = 277
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
            self.state = 279
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
            self.state = 281
            self.logicAndExp()
            self.state = 286
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 282
                    self.match(MiniGoParser.OR)
                    self.state = 283
                    self.logicOrExp() 
                self.state = 288
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
            self.state = 289
            self.equalityExp()
            self.state = 294
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 290
                    self.match(MiniGoParser.AND)
                    self.state = 291
                    self.logicAndExp() 
                self.state = 296
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
            self.state = 297
            self.additiveExp()
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16911433728) != 0):
                self.state = 298
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16911433728) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 299
                self.additiveExp()
                self.state = 304
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
            self.state = 305
            self.multiplicativeExp()
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23 or _la==24:
                self.state = 306
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 307
                self.multiplicativeExp()
                self.state = 312
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
            self.state = 313
            self.unaryExp()
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0):
                self.state = 314
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 315
                self.unaryExp()
                self.state = 320
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

        def postfixExp(self):
            return self.getTypedRuleContext(MiniGoParser.PostfixExpContext,0)


        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.MINUS)
            else:
                return self.getToken(MiniGoParser.MINUS, i)

        def NOT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NOT)
            else:
                return self.getToken(MiniGoParser.NOT, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_unaryExp




    def unaryExp(self):

        localctx = MiniGoParser.UnaryExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_unaryExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24 or _la==36:
                self.state = 321
                _la = self._input.LA(1)
                if not(_la==24 or _la==36):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 327
            self.postfixExp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExp(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExpContext,0)


        def postfixExp(self):
            return self.getTypedRuleContext(MiniGoParser.PostfixExpContext,0)


        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def arguments(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_postfixExp



    def postfixExp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.PostfixExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_postfixExp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.primaryExp()
            self._ctx.stop = self._input.LT(-1)
            self.state = 348
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 346
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.PostfixExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExp)
                        self.state = 332
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 333
                        self.match(MiniGoParser.LBRACKET)
                        self.state = 334
                        self.expression()
                        self.state = 335
                        self.match(MiniGoParser.RBRACKET)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.PostfixExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExp)
                        self.state = 337
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 338
                        self.match(MiniGoParser.DOT)
                        self.state = 339
                        self.match(MiniGoParser.IDENTIFIER)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.PostfixExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExp)
                        self.state = 340
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 341
                        self.match(MiniGoParser.LPAREN)
                        self.state = 343
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135125649743470592) != 0):
                            self.state = 342
                            self.arguments()


                        self.state = 345
                        self.match(MiniGoParser.RPAREN)
                        pass

             
                self.state = 350
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def callStatement(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primaryExp




    def primaryExp(self):

        localctx = MiniGoParser.PrimaryExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_primaryExp)
        try:
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.match(MiniGoParser.LPAREN)
                self.state = 352
                self.expression()
                self.state = 353
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 356
                self.callStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 357
                self.match(MiniGoParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126100789566431232) != 0)):
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStatement(self):
            return self.getTypedRuleContext(MiniGoParser.AssignStatementContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


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


        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def typeDecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypeDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclContext,0)


        def constDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_statement)
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.assignStatement()
                self.state = 363
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.ifStatement()
                self.state = 366
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 368
                self.forStatement()
                self.state = 369
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 371
                self.breakStatement()
                self.state = 372
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 374
                self.continueStatement()
                self.state = 375
                self.endOfStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 377
                self.callStatement()
                self.state = 378
                self.endOfStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 380
                self.returnStatement()
                self.state = 381
                self.endOfStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 383
                self.varDecl()
                self.state = 384
                self.endOfStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 386
                self.typeDecl()
                self.state = 387
                self.endOfStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 389
                self.methodDecl()
                self.state = 390
                self.endOfStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 392
                self.constDecl()
                self.state = 393
                self.endOfStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 395
                self.block()
                self.state = 396
                self.endOfStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def arraysBlock(self):
            return self.getTypedRuleContext(MiniGoParser.ArraysBlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLit




    def arrayLit(self):

        localctx = MiniGoParser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.arrayDims()
            self.state = 401
            self.baseType()
            self.state = 402
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
        self.enterRule(localctx, 60, self.RULE_arraysBlock)
        self._la = 0 # Token type
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.match(MiniGoParser.LBRACE)
                self.state = 405
                self.arraysBlock()
                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==50:
                    self.state = 406
                    self.match(MiniGoParser.COMMA)
                    self.state = 407
                    self.arraysBlock()
                    self.state = 412
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 413
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.match(MiniGoParser.LBRACE)
                self.state = 416
                self.expression()
                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==50:
                    self.state = 417
                    self.match(MiniGoParser.COMMA)
                    self.state = 418
                    self.expression()
                    self.state = 423
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 424
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

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def structFieldsAssign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StructFieldsAssignContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StructFieldsAssignContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structExpression




    def structExpression(self):

        localctx = MiniGoParser.StructExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_structExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 429
            self.match(MiniGoParser.LBRACE)
            self.state = 441
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 430
                self.structFieldsAssign()
                self.state = 435
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 431
                        self.match(MiniGoParser.COMMA)
                        self.state = 432
                        self.structFieldsAssign() 
                    self.state = 437
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

                self.state = 439
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==50:
                    self.state = 438
                    self.match(MiniGoParser.COMMA)




            self.state = 443
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def structExpression(self):
            return self.getTypedRuleContext(MiniGoParser.StructExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structBlock




    def structBlock(self):

        localctx = MiniGoParser.StructBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_structBlock)
        try:
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 446
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 447
                self.structExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructFieldsAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def structBlock(self):
            return self.getTypedRuleContext(MiniGoParser.StructBlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structFieldsAssign




    def structFieldsAssign(self):

        localctx = MiniGoParser.StructFieldsAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_structFieldsAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 451
            self.match(MiniGoParser.COLON)
            self.state = 452
            self.structBlock()
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

        def assignmentOperator(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentOperatorContext,0)


        def a2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.A2Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.A2Context,i)


        def a1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.A1Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.A1Context,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignStatement




    def assignStatement(self):

        localctx = MiniGoParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_assignStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.a1()
            self.state = 459
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 455
                self.match(MiniGoParser.COMMA)
                self.state = 456
                self.a1()
                self.state = 461
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 462
            self.assignmentOperator()
            self.state = 463
            self.a2()
            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 464
                self.match(MiniGoParser.COMMA)
                self.state = 465
                self.a2()
                self.state = 470
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class A1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def a1(self):
            return self.getTypedRuleContext(MiniGoParser.A1Context,0)


        def callStatement(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_a1




    def a1(self):

        localctx = MiniGoParser.A1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_a1)
        self._la = 0 # Token type
        try:
            self.state = 481
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                if la_ == 1:
                    self.state = 471
                    self.callStatement()
                    pass

                elif la_ == 2:
                    self.state = 472
                    self.match(MiniGoParser.IDENTIFIER)
                    pass


                self.state = 475
                self.match(MiniGoParser.DOT)
                self.state = 476
                self.a1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 477
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 479
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 478
                    self.arrayDims()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class A2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def structExpression(self):
            return self.getTypedRuleContext(MiniGoParser.StructExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_a2




    def a2(self):

        localctx = MiniGoParser.A2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_a2)
        try:
            self.state = 486
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 483
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 484
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 485
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
        self.enterRule(localctx, 74, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4260611751936) != 0)):
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


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ELSE)
            else:
                return self.getToken(MiniGoParser.ELSE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ifStatement




    def ifStatement(self):

        localctx = MiniGoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.match(MiniGoParser.IF)
            self.state = 491
            self.expression()
            self.state = 492
            self.block()
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 493
                self.match(MiniGoParser.NEWLINE)


            self.state = 505
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 496
                    self.match(MiniGoParser.ELSE)
                    self.state = 497
                    self.match(MiniGoParser.IF)
                    self.state = 498
                    self.expression()
                    self.state = 499
                    self.block()
                    self.state = 501
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                    if la_ == 1:
                        self.state = 500
                        self.match(MiniGoParser.NEWLINE)

             
                self.state = 507
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

            self.state = 510
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 508
                self.match(MiniGoParser.ELSE)
                self.state = 509
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
        self.enterRule(localctx, 78, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(MiniGoParser.FOR)
            self.state = 515
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 513
                self.forLoop()
                pass

            elif la_ == 2:
                self.state = 514
                self.forIteration()
                pass


            self.state = 517
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
        self.enterRule(localctx, 80, self.RULE_forLoop)
        try:
            self.state = 526
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 519
                self.forCondition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 520
                self.initilization()
                self.state = 521
                self.match(MiniGoParser.SEMI)
                self.state = 522
                self.forCondition()
                self.state = 523
                self.match(MiniGoParser.SEMI)
                self.state = 524
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
        self.enterRule(localctx, 82, self.RULE_initilization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 529
            self.match(MiniGoParser.DECLARE)
            self.state = 530
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
        self.enterRule(localctx, 84, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
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
        self.enterRule(localctx, 86, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 535
            self.assignmentOperator()
            self.state = 536
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
        self.enterRule(localctx, 88, self.RULE_forIteration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            _la = self._input.LA(1)
            if not(_la==43 or _la==53):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 539
            self.match(MiniGoParser.COMMA)
            self.state = 540
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 541
            self.match(MiniGoParser.DECLARE)
            self.state = 542
            self.match(MiniGoParser.RANGE)
            self.state = 543
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
        self.enterRule(localctx, 90, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
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
        self.enterRule(localctx, 92, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.match(MiniGoParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def arguments(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_primaryCall




    def primaryCall(self):

        localctx = MiniGoParser.PrimaryCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_primaryCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 550
            self.match(MiniGoParser.LPAREN)
            self.state = 552
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135125649743470592) != 0):
                self.state = 551
                self.arguments()


            self.state = 554
            self.match(MiniGoParser.RPAREN)
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

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def callStatement(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementContext,0)


        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def primaryCall(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryCallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callStatement




    def callStatement(self):

        localctx = MiniGoParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_callStatement)
        self._la = 0 # Token type
        try:
            self.state = 567
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 556
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 558
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 557
                    self.arrayDims()


                self.state = 560
                self.match(MiniGoParser.DOT)
                self.state = 561
                self.callStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 562
                self.primaryCall()
                self.state = 565
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                if la_ == 1:
                    self.state = 563
                    self.match(MiniGoParser.DOT)
                    self.state = 564
                    self.callStatement()


                pass


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


        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStatement




    def returnStatement(self):

        localctx = MiniGoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(MiniGoParser.RETURN)
            self.state = 572
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 24, 36, 44, 53, 54, 55, 56]:
                self.state = 570
                self.expression()
                pass
            elif token in [48]:
                self.state = 571
                self.arrayLit()
                pass
            elif token in [51, 60]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return MiniGoParser.RULE_arguments




    def arguments(self):

        localctx = MiniGoParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.expression()
            self.state = 579
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 575
                self.match(MiniGoParser.COMMA)
                self.state = 576
                self.expression()
                self.state = 581
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 102, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 582
            self.match(MiniGoParser.LBRACE)
            self.state = 584 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 583
                self.statement()
                self.state = 586 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 9077567999901818) != 0)):
                    break

            self.state = 588
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
        self.enterRule(localctx, 104, self.RULE_arrayDims)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 590
                self.match(MiniGoParser.LBRACKET)
                self.state = 592
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135125649743470592) != 0):
                    self.state = 591
                    self.expression()


                self.state = 594
                self.match(MiniGoParser.RBRACKET)
                self.state = 597 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==48):
                    break

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
        self._predicates[25] = self.postfixExp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def postfixExp_sempred(self, localctx:PostfixExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




