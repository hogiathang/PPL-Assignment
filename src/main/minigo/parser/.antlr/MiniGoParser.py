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
        4,1,64,625,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,1,0,5,0,106,
        8,0,10,0,12,0,109,9,0,1,0,3,0,112,8,0,1,0,5,0,115,8,0,10,0,12,0,
        118,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,
        1,4,1,4,1,4,1,4,3,4,138,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,
        148,8,4,3,4,150,8,4,1,5,1,5,1,5,1,5,5,5,156,8,5,10,5,12,5,159,9,
        5,1,5,3,5,162,8,5,1,5,1,5,3,5,166,8,5,1,5,1,5,3,5,170,8,5,1,6,1,
        6,1,6,1,6,3,6,176,8,6,1,6,1,6,3,6,180,8,6,1,6,3,6,183,8,6,1,6,1,
        6,1,7,1,7,1,7,1,7,3,7,191,8,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,3,9,206,8,9,1,9,1,9,3,9,210,8,9,1,9,1,9,1,10,1,
        10,1,10,5,10,217,8,10,10,10,12,10,220,9,10,1,10,1,10,1,11,1,11,3,
        11,226,8,11,1,11,1,11,3,11,230,8,11,1,11,1,11,1,12,1,12,1,12,5,12,
        237,8,12,10,12,12,12,240,9,12,1,12,1,12,1,13,1,13,1,13,1,13,5,13,
        248,8,13,10,13,12,13,251,9,13,1,13,1,13,1,14,1,14,1,14,5,14,258,
        8,14,10,14,12,14,261,9,14,1,15,1,15,1,15,3,15,266,8,15,1,15,1,15,
        1,16,1,16,1,16,5,16,273,8,16,10,16,12,16,276,9,16,1,17,1,17,3,17,
        280,8,17,1,17,1,17,1,18,1,18,1,19,1,19,1,19,5,19,289,8,19,10,19,
        12,19,292,9,19,1,20,1,20,1,20,5,20,297,8,20,10,20,12,20,300,9,20,
        1,21,1,21,1,21,5,21,305,8,21,10,21,12,21,308,9,21,1,22,1,22,1,22,
        5,22,313,8,22,10,22,12,22,316,9,22,1,23,1,23,1,23,5,23,321,8,23,
        10,23,12,23,324,9,23,1,24,1,24,1,24,3,24,329,8,24,1,25,1,25,1,25,
        1,25,1,25,3,25,336,8,25,1,26,1,26,1,26,1,26,1,26,3,26,343,8,26,1,
        26,5,26,346,8,26,10,26,12,26,349,9,26,1,27,1,27,1,27,1,27,1,27,1,
        27,3,27,357,8,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,367,
        8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,404,8,29,
        3,29,406,8,29,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,5,31,416,8,
        31,10,31,12,31,419,9,31,1,31,1,31,1,31,1,31,1,31,1,31,5,31,427,8,
        31,10,31,12,31,430,9,31,1,31,1,31,3,31,434,8,31,1,32,1,32,1,32,1,
        32,1,32,5,32,441,8,32,10,32,12,32,444,9,32,1,32,3,32,447,8,32,3,
        32,449,8,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,3,33,460,
        8,33,1,33,1,33,1,33,1,33,3,33,466,8,33,1,33,5,33,469,8,33,10,33,
        12,33,472,9,33,1,33,3,33,475,8,33,3,33,477,8,33,1,33,1,33,3,33,481,
        8,33,1,34,1,34,1,34,1,34,1,35,1,35,1,35,5,35,490,8,35,10,35,12,35,
        493,9,35,1,35,1,35,1,35,1,35,5,35,499,8,35,10,35,12,35,502,9,35,
        1,36,1,36,1,36,5,36,507,8,36,10,36,12,36,510,9,36,1,36,3,36,513,
        8,36,1,37,1,37,1,37,3,37,518,8,37,1,38,1,38,1,39,1,39,1,39,1,39,
        3,39,526,8,39,1,39,1,39,1,39,1,39,1,39,3,39,533,8,39,5,39,535,8,
        39,10,39,12,39,538,9,39,1,39,1,39,3,39,542,8,39,1,40,1,40,1,40,3,
        40,547,8,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,1,41,1,41,3,41,558,
        8,41,1,42,1,42,1,42,1,42,1,43,1,43,1,44,1,44,1,44,1,44,1,45,1,45,
        1,45,1,45,1,45,1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,48,3,48,
        584,8,48,1,48,1,48,1,48,1,48,5,48,590,8,48,10,48,12,48,593,9,48,
        3,48,595,8,48,1,48,1,48,1,49,1,49,1,49,1,49,1,49,1,49,3,49,605,8,
        49,1,50,1,50,5,50,609,8,50,10,50,12,50,612,9,50,1,50,1,50,1,51,1,
        51,3,51,618,8,51,1,51,4,51,621,8,51,11,51,12,51,622,1,51,0,0,52,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,
        90,92,94,96,98,100,102,0,8,2,0,10,13,54,54,2,1,52,52,61,61,1,0,29,
        34,1,0,24,25,1,0,26,28,2,0,25,25,37,37,2,0,23,23,38,42,2,0,44,44,
        54,54,663,0,107,1,0,0,0,2,121,1,0,0,0,4,128,1,0,0,0,6,130,1,0,0,
        0,8,149,1,0,0,0,10,151,1,0,0,0,12,171,1,0,0,0,14,186,1,0,0,0,16,
        192,1,0,0,0,18,197,1,0,0,0,20,213,1,0,0,0,22,223,1,0,0,0,24,233,
        1,0,0,0,26,243,1,0,0,0,28,254,1,0,0,0,30,262,1,0,0,0,32,269,1,0,
        0,0,34,277,1,0,0,0,36,283,1,0,0,0,38,285,1,0,0,0,40,293,1,0,0,0,
        42,301,1,0,0,0,44,309,1,0,0,0,46,317,1,0,0,0,48,328,1,0,0,0,50,335,
        1,0,0,0,52,342,1,0,0,0,54,356,1,0,0,0,56,366,1,0,0,0,58,405,1,0,
        0,0,60,407,1,0,0,0,62,433,1,0,0,0,64,435,1,0,0,0,66,480,1,0,0,0,
        68,482,1,0,0,0,70,486,1,0,0,0,72,503,1,0,0,0,74,517,1,0,0,0,76,519,
        1,0,0,0,78,521,1,0,0,0,80,543,1,0,0,0,82,557,1,0,0,0,84,559,1,0,
        0,0,86,563,1,0,0,0,88,565,1,0,0,0,90,569,1,0,0,0,92,576,1,0,0,0,
        94,578,1,0,0,0,96,580,1,0,0,0,98,598,1,0,0,0,100,606,1,0,0,0,102,
        620,1,0,0,0,104,106,3,8,4,0,105,104,1,0,0,0,106,109,1,0,0,0,107,
        105,1,0,0,0,107,108,1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,110,
        112,3,2,1,0,111,110,1,0,0,0,111,112,1,0,0,0,112,116,1,0,0,0,113,
        115,3,8,4,0,114,113,1,0,0,0,115,118,1,0,0,0,116,114,1,0,0,0,116,
        117,1,0,0,0,117,119,1,0,0,0,118,116,1,0,0,0,119,120,5,0,0,1,120,
        1,1,0,0,0,121,122,5,6,0,0,122,123,5,1,0,0,123,124,5,45,0,0,124,125,
        5,46,0,0,125,126,3,100,50,0,126,127,3,6,3,0,127,3,1,0,0,0,128,129,
        7,0,0,0,129,5,1,0,0,0,130,131,7,1,0,0,131,7,1,0,0,0,132,133,3,10,
        5,0,133,134,3,6,3,0,134,150,1,0,0,0,135,137,3,12,6,0,136,138,3,6,
        3,0,137,136,1,0,0,0,137,138,1,0,0,0,138,150,1,0,0,0,139,140,3,14,
        7,0,140,141,3,6,3,0,141,150,1,0,0,0,142,143,3,16,8,0,143,144,3,6,
        3,0,144,150,1,0,0,0,145,147,3,18,9,0,146,148,3,6,3,0,147,146,1,0,
        0,0,147,148,1,0,0,0,148,150,1,0,0,0,149,132,1,0,0,0,149,135,1,0,
        0,0,149,139,1,0,0,0,149,142,1,0,0,0,149,145,1,0,0,0,150,9,1,0,0,
        0,151,152,5,18,0,0,152,157,5,54,0,0,153,154,5,51,0,0,154,156,5,54,
        0,0,155,153,1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,157,158,1,0,
        0,0,158,161,1,0,0,0,159,157,1,0,0,0,160,162,3,102,51,0,161,160,1,
        0,0,0,161,162,1,0,0,0,162,169,1,0,0,0,163,170,3,4,2,0,164,166,3,
        4,2,0,165,164,1,0,0,0,165,166,1,0,0,0,166,167,1,0,0,0,167,168,5,
        22,0,0,168,170,3,36,18,0,169,163,1,0,0,0,169,165,1,0,0,0,170,11,
        1,0,0,0,171,172,5,6,0,0,172,173,5,54,0,0,173,175,5,45,0,0,174,176,
        3,32,16,0,175,174,1,0,0,0,175,176,1,0,0,0,176,177,1,0,0,0,177,182,
        5,46,0,0,178,180,3,102,51,0,179,178,1,0,0,0,179,180,1,0,0,0,180,
        181,1,0,0,0,181,183,3,4,2,0,182,179,1,0,0,0,182,183,1,0,0,0,183,
        184,1,0,0,0,184,185,3,100,50,0,185,13,1,0,0,0,186,187,5,7,0,0,187,
        190,5,54,0,0,188,191,3,20,10,0,189,191,3,24,12,0,190,188,1,0,0,0,
        190,189,1,0,0,0,191,15,1,0,0,0,192,193,5,17,0,0,193,194,5,54,0,0,
        194,195,5,22,0,0,195,196,3,36,18,0,196,17,1,0,0,0,197,198,5,6,0,
        0,198,199,5,45,0,0,199,200,5,54,0,0,200,201,5,54,0,0,201,202,5,46,
        0,0,202,203,5,54,0,0,203,205,5,45,0,0,204,206,3,32,16,0,205,204,
        1,0,0,0,205,206,1,0,0,0,206,207,1,0,0,0,207,209,5,46,0,0,208,210,
        3,4,2,0,209,208,1,0,0,0,209,210,1,0,0,0,210,211,1,0,0,0,211,212,
        3,100,50,0,212,19,1,0,0,0,213,214,5,8,0,0,214,218,5,47,0,0,215,217,
        3,22,11,0,216,215,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,
        1,0,0,0,219,221,1,0,0,0,220,218,1,0,0,0,221,222,5,48,0,0,222,21,
        1,0,0,0,223,229,5,54,0,0,224,226,3,102,51,0,225,224,1,0,0,0,225,
        226,1,0,0,0,226,227,1,0,0,0,227,230,3,4,2,0,228,230,3,20,10,0,229,
        225,1,0,0,0,229,228,1,0,0,0,230,231,1,0,0,0,231,232,3,6,3,0,232,
        23,1,0,0,0,233,234,5,9,0,0,234,238,5,47,0,0,235,237,3,30,15,0,236,
        235,1,0,0,0,237,240,1,0,0,0,238,236,1,0,0,0,238,239,1,0,0,0,239,
        241,1,0,0,0,240,238,1,0,0,0,241,242,5,48,0,0,242,25,1,0,0,0,243,
        249,5,45,0,0,244,245,3,28,14,0,245,246,3,4,2,0,246,248,1,0,0,0,247,
        244,1,0,0,0,248,251,1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,250,
        252,1,0,0,0,251,249,1,0,0,0,252,253,5,46,0,0,253,27,1,0,0,0,254,
        259,5,54,0,0,255,256,5,51,0,0,256,258,5,54,0,0,257,255,1,0,0,0,258,
        261,1,0,0,0,259,257,1,0,0,0,259,260,1,0,0,0,260,29,1,0,0,0,261,259,
        1,0,0,0,262,263,5,54,0,0,263,265,3,26,13,0,264,266,3,4,2,0,265,264,
        1,0,0,0,265,266,1,0,0,0,266,267,1,0,0,0,267,268,3,6,3,0,268,31,1,
        0,0,0,269,274,3,34,17,0,270,271,5,51,0,0,271,273,3,34,17,0,272,270,
        1,0,0,0,273,276,1,0,0,0,274,272,1,0,0,0,274,275,1,0,0,0,275,33,1,
        0,0,0,276,274,1,0,0,0,277,279,5,54,0,0,278,280,3,102,51,0,279,278,
        1,0,0,0,279,280,1,0,0,0,280,281,1,0,0,0,281,282,3,4,2,0,282,35,1,
        0,0,0,283,284,3,38,19,0,284,37,1,0,0,0,285,290,3,40,20,0,286,287,
        5,36,0,0,287,289,3,38,19,0,288,286,1,0,0,0,289,292,1,0,0,0,290,288,
        1,0,0,0,290,291,1,0,0,0,291,39,1,0,0,0,292,290,1,0,0,0,293,298,3,
        42,21,0,294,295,5,35,0,0,295,297,3,40,20,0,296,294,1,0,0,0,297,300,
        1,0,0,0,298,296,1,0,0,0,298,299,1,0,0,0,299,41,1,0,0,0,300,298,1,
        0,0,0,301,306,3,44,22,0,302,303,7,2,0,0,303,305,3,44,22,0,304,302,
        1,0,0,0,305,308,1,0,0,0,306,304,1,0,0,0,306,307,1,0,0,0,307,43,1,
        0,0,0,308,306,1,0,0,0,309,314,3,46,23,0,310,311,7,3,0,0,311,313,
        3,46,23,0,312,310,1,0,0,0,313,316,1,0,0,0,314,312,1,0,0,0,314,315,
        1,0,0,0,315,45,1,0,0,0,316,314,1,0,0,0,317,322,3,48,24,0,318,319,
        7,4,0,0,319,321,3,48,24,0,320,318,1,0,0,0,321,324,1,0,0,0,322,320,
        1,0,0,0,322,323,1,0,0,0,323,47,1,0,0,0,324,322,1,0,0,0,325,326,7,
        5,0,0,326,329,3,48,24,0,327,329,3,50,25,0,328,325,1,0,0,0,328,327,
        1,0,0,0,329,49,1,0,0,0,330,336,3,52,26,0,331,332,5,45,0,0,332,333,
        3,36,18,0,333,334,5,46,0,0,334,336,1,0,0,0,335,330,1,0,0,0,335,331,
        1,0,0,0,336,51,1,0,0,0,337,343,3,56,28,0,338,339,5,45,0,0,339,340,
        3,36,18,0,340,341,5,46,0,0,341,343,1,0,0,0,342,337,1,0,0,0,342,338,
        1,0,0,0,343,347,1,0,0,0,344,346,3,54,27,0,345,344,1,0,0,0,346,349,
        1,0,0,0,347,345,1,0,0,0,347,348,1,0,0,0,348,53,1,0,0,0,349,347,1,
        0,0,0,350,351,5,49,0,0,351,352,3,36,18,0,352,353,5,50,0,0,353,357,
        1,0,0,0,354,355,5,43,0,0,355,357,3,56,28,0,356,350,1,0,0,0,356,354,
        1,0,0,0,357,55,1,0,0,0,358,367,5,55,0,0,359,367,5,56,0,0,360,367,
        5,57,0,0,361,367,5,14,0,0,362,367,5,15,0,0,363,367,5,16,0,0,364,
        367,3,96,48,0,365,367,5,54,0,0,366,358,1,0,0,0,366,359,1,0,0,0,366,
        360,1,0,0,0,366,361,1,0,0,0,366,362,1,0,0,0,366,363,1,0,0,0,366,
        364,1,0,0,0,366,365,1,0,0,0,367,57,1,0,0,0,368,369,3,70,35,0,369,
        370,3,6,3,0,370,406,1,0,0,0,371,372,3,78,39,0,372,373,3,6,3,0,373,
        406,1,0,0,0,374,375,3,80,40,0,375,376,3,6,3,0,376,406,1,0,0,0,377,
        378,3,92,46,0,378,379,3,6,3,0,379,406,1,0,0,0,380,381,3,94,47,0,
        381,382,3,6,3,0,382,406,1,0,0,0,383,384,3,96,48,0,384,385,3,6,3,
        0,385,406,1,0,0,0,386,387,3,98,49,0,387,388,3,6,3,0,388,406,1,0,
        0,0,389,390,3,10,5,0,390,391,3,6,3,0,391,406,1,0,0,0,392,393,3,14,
        7,0,393,394,3,6,3,0,394,406,1,0,0,0,395,396,3,18,9,0,396,397,3,6,
        3,0,397,406,1,0,0,0,398,399,3,16,8,0,399,400,3,6,3,0,400,406,1,0,
        0,0,401,403,3,100,50,0,402,404,3,6,3,0,403,402,1,0,0,0,403,404,1,
        0,0,0,404,406,1,0,0,0,405,368,1,0,0,0,405,371,1,0,0,0,405,374,1,
        0,0,0,405,377,1,0,0,0,405,380,1,0,0,0,405,383,1,0,0,0,405,386,1,
        0,0,0,405,389,1,0,0,0,405,392,1,0,0,0,405,395,1,0,0,0,405,398,1,
        0,0,0,405,401,1,0,0,0,406,59,1,0,0,0,407,408,3,102,51,0,408,409,
        3,4,2,0,409,410,3,62,31,0,410,61,1,0,0,0,411,412,5,47,0,0,412,417,
        3,62,31,0,413,414,5,51,0,0,414,416,3,62,31,0,415,413,1,0,0,0,416,
        419,1,0,0,0,417,415,1,0,0,0,417,418,1,0,0,0,418,420,1,0,0,0,419,
        417,1,0,0,0,420,421,5,48,0,0,421,434,1,0,0,0,422,423,5,47,0,0,423,
        428,3,36,18,0,424,425,5,51,0,0,425,427,3,36,18,0,426,424,1,0,0,0,
        427,430,1,0,0,0,428,426,1,0,0,0,428,429,1,0,0,0,429,431,1,0,0,0,
        430,428,1,0,0,0,431,432,5,48,0,0,432,434,1,0,0,0,433,411,1,0,0,0,
        433,422,1,0,0,0,434,63,1,0,0,0,435,436,5,54,0,0,436,448,5,47,0,0,
        437,442,3,68,34,0,438,439,5,51,0,0,439,441,3,68,34,0,440,438,1,0,
        0,0,441,444,1,0,0,0,442,440,1,0,0,0,442,443,1,0,0,0,443,446,1,0,
        0,0,444,442,1,0,0,0,445,447,5,51,0,0,446,445,1,0,0,0,446,447,1,0,
        0,0,447,449,1,0,0,0,448,437,1,0,0,0,448,449,1,0,0,0,449,450,1,0,
        0,0,450,451,5,48,0,0,451,65,1,0,0,0,452,481,3,36,18,0,453,481,3,
        60,30,0,454,481,3,64,32,0,455,456,3,20,10,0,456,476,5,47,0,0,457,
        458,5,54,0,0,458,460,5,53,0,0,459,457,1,0,0,0,459,460,1,0,0,0,460,
        461,1,0,0,0,461,470,3,36,18,0,462,465,5,51,0,0,463,464,5,54,0,0,
        464,466,5,53,0,0,465,463,1,0,0,0,465,466,1,0,0,0,466,467,1,0,0,0,
        467,469,3,36,18,0,468,462,1,0,0,0,469,472,1,0,0,0,470,468,1,0,0,
        0,470,471,1,0,0,0,471,474,1,0,0,0,472,470,1,0,0,0,473,475,5,51,0,
        0,474,473,1,0,0,0,474,475,1,0,0,0,475,477,1,0,0,0,476,459,1,0,0,
        0,476,477,1,0,0,0,477,478,1,0,0,0,478,479,5,48,0,0,479,481,1,0,0,
        0,480,452,1,0,0,0,480,453,1,0,0,0,480,454,1,0,0,0,480,455,1,0,0,
        0,481,67,1,0,0,0,482,483,5,54,0,0,483,484,5,53,0,0,484,485,3,66,
        33,0,485,69,1,0,0,0,486,491,3,72,36,0,487,488,5,51,0,0,488,490,3,
        72,36,0,489,487,1,0,0,0,490,493,1,0,0,0,491,489,1,0,0,0,491,492,
        1,0,0,0,492,494,1,0,0,0,493,491,1,0,0,0,494,495,3,76,38,0,495,500,
        3,74,37,0,496,497,5,51,0,0,497,499,3,74,37,0,498,496,1,0,0,0,499,
        502,1,0,0,0,500,498,1,0,0,0,500,501,1,0,0,0,501,71,1,0,0,0,502,500,
        1,0,0,0,503,508,5,54,0,0,504,505,5,43,0,0,505,507,5,54,0,0,506,504,
        1,0,0,0,507,510,1,0,0,0,508,506,1,0,0,0,508,509,1,0,0,0,509,512,
        1,0,0,0,510,508,1,0,0,0,511,513,3,102,51,0,512,511,1,0,0,0,512,513,
        1,0,0,0,513,73,1,0,0,0,514,518,3,36,18,0,515,518,3,60,30,0,516,518,
        3,64,32,0,517,514,1,0,0,0,517,515,1,0,0,0,517,516,1,0,0,0,518,75,
        1,0,0,0,519,520,7,6,0,0,520,77,1,0,0,0,521,522,5,2,0,0,522,523,3,
        36,18,0,523,525,3,100,50,0,524,526,5,61,0,0,525,524,1,0,0,0,525,
        526,1,0,0,0,526,536,1,0,0,0,527,528,5,3,0,0,528,529,5,2,0,0,529,
        530,3,36,18,0,530,532,3,100,50,0,531,533,5,61,0,0,532,531,1,0,0,
        0,532,533,1,0,0,0,533,535,1,0,0,0,534,527,1,0,0,0,535,538,1,0,0,
        0,536,534,1,0,0,0,536,537,1,0,0,0,537,541,1,0,0,0,538,536,1,0,0,
        0,539,540,5,3,0,0,540,542,3,100,50,0,541,539,1,0,0,0,541,542,1,0,
        0,0,542,79,1,0,0,0,543,546,5,4,0,0,544,547,3,82,41,0,545,547,3,90,
        45,0,546,544,1,0,0,0,546,545,1,0,0,0,547,548,1,0,0,0,548,549,3,100,
        50,0,549,81,1,0,0,0,550,558,3,86,43,0,551,552,3,84,42,0,552,553,
        5,52,0,0,553,554,3,86,43,0,554,555,5,52,0,0,555,556,3,88,44,0,556,
        558,1,0,0,0,557,550,1,0,0,0,557,551,1,0,0,0,558,83,1,0,0,0,559,560,
        5,54,0,0,560,561,5,23,0,0,561,562,3,36,18,0,562,85,1,0,0,0,563,564,
        3,36,18,0,564,87,1,0,0,0,565,566,5,54,0,0,566,567,3,76,38,0,567,
        568,3,36,18,0,568,89,1,0,0,0,569,570,7,7,0,0,570,571,5,51,0,0,571,
        572,5,54,0,0,572,573,5,23,0,0,573,574,5,21,0,0,574,575,5,54,0,0,
        575,91,1,0,0,0,576,577,5,20,0,0,577,93,1,0,0,0,578,579,5,19,0,0,
        579,95,1,0,0,0,580,583,5,54,0,0,581,582,5,43,0,0,582,584,5,54,0,
        0,583,581,1,0,0,0,583,584,1,0,0,0,584,585,1,0,0,0,585,594,5,45,0,
        0,586,591,3,36,18,0,587,588,5,51,0,0,588,590,3,36,18,0,589,587,1,
        0,0,0,590,593,1,0,0,0,591,589,1,0,0,0,591,592,1,0,0,0,592,595,1,
        0,0,0,593,591,1,0,0,0,594,586,1,0,0,0,594,595,1,0,0,0,595,596,1,
        0,0,0,596,597,5,46,0,0,597,97,1,0,0,0,598,604,5,5,0,0,599,605,3,
        36,18,0,600,601,3,102,51,0,601,602,3,4,2,0,602,603,3,62,31,0,603,
        605,1,0,0,0,604,599,1,0,0,0,604,600,1,0,0,0,604,605,1,0,0,0,605,
        99,1,0,0,0,606,610,5,47,0,0,607,609,3,58,29,0,608,607,1,0,0,0,609,
        612,1,0,0,0,610,608,1,0,0,0,610,611,1,0,0,0,611,613,1,0,0,0,612,
        610,1,0,0,0,613,614,5,48,0,0,614,101,1,0,0,0,615,617,5,49,0,0,616,
        618,3,36,18,0,617,616,1,0,0,0,617,618,1,0,0,0,618,619,1,0,0,0,619,
        621,5,50,0,0,620,615,1,0,0,0,621,622,1,0,0,0,622,620,1,0,0,0,622,
        623,1,0,0,0,623,103,1,0,0,0,68,107,111,116,137,147,149,157,161,165,
        169,175,179,182,190,205,209,218,225,229,238,249,259,265,274,279,
        290,298,306,314,322,328,335,342,347,356,366,403,405,417,428,433,
        442,446,448,459,465,470,474,476,480,491,500,508,512,517,525,532,
        536,541,546,557,583,591,594,604,610,617,622
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
    RULE_postfixExp = 26
    RULE_postfixOp = 27
    RULE_term = 28
    RULE_statement = 29
    RULE_arrayLit = 30
    RULE_arraysBlock = 31
    RULE_structExpression = 32
    RULE_structBlock = 33
    RULE_structFieldsAssign = 34
    RULE_assignStatement = 35
    RULE_a1 = 36
    RULE_a2 = 37
    RULE_assignmentOperator = 38
    RULE_ifStatement = 39
    RULE_forStatement = 40
    RULE_forLoop = 41
    RULE_initilization = 42
    RULE_forCondition = 43
    RULE_forUpdate = 44
    RULE_forIteration = 45
    RULE_breakStatement = 46
    RULE_continueStatement = 47
    RULE_callStatement = 48
    RULE_returnStatement = 49
    RULE_block = 50
    RULE_arrayDims = 51

    ruleNames =  [ "program", "mainFunction", "baseType", "endOfStatement", 
                   "declaration", "varDecl", "funcDecl", "typeDecl", "constDecl", 
                   "methodDecl", "structDefinition", "structFields", "interfaceDefinition", 
                   "listParams", "listIdentifier", "interfaceFields", "funcParams", 
                   "funcParam", "expression", "logicOrExp", "logicAndExp", 
                   "equalityExp", "additiveExp", "multiplicativeExp", "unaryExp", 
                   "primaryExp", "postfixExp", "postfixOp", "term", "statement", 
                   "arrayLit", "arraysBlock", "structExpression", "structBlock", 
                   "structFieldsAssign", "assignStatement", "a1", "a2", 
                   "assignmentOperator", "ifStatement", "forStatement", 
                   "forLoop", "initilization", "forCondition", "forUpdate", 
                   "forIteration", "breakStatement", "continueStatement", 
                   "callStatement", "returnStatement", "block", "arrayDims" ]

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
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 104
                    self.declaration() 
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 110
                self.mainFunction()


            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 393408) != 0):
                self.state = 113
                self.declaration()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
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
            self.state = 121
            self.match(MiniGoParser.FUNC)
            self.state = 122
            self.match(MiniGoParser.T__0)
            self.state = 123
            self.match(MiniGoParser.LPAREN)
            self.state = 124
            self.match(MiniGoParser.RPAREN)
            self.state = 125
            self.block()
            self.state = 126
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
            self.state = 128
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
            self.state = 130
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
        self.enterRule(localctx, 8, self.RULE_declaration)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.varDecl()
                self.state = 133
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.funcDecl()
                self.state = 137
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 136
                    self.endOfStatement()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.typeDecl()
                self.state = 140
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.constDecl()
                self.state = 143
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 145
                self.methodDecl()
                self.state = 147
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 146
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
        self.enterRule(localctx, 10, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(MiniGoParser.VAR)
            self.state = 152
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 153
                self.match(MiniGoParser.COMMA)
                self.state = 154
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 160
                self.arrayDims()


            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 163
                self.baseType()
                pass

            elif la_ == 2:
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398509497344) != 0):
                    self.state = 164
                    self.baseType()


                self.state = 167
                self.match(MiniGoParser.ASSIGN)
                self.state = 168
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
            self.state = 171
            self.match(MiniGoParser.FUNC)
            self.state = 172
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 173
            self.match(MiniGoParser.LPAREN)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 174
                self.funcParams()


            self.state = 177
            self.match(MiniGoParser.RPAREN)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18577348462918656) != 0):
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 178
                    self.arrayDims()


                self.state = 181
                self.baseType()


            self.state = 184
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
            self.state = 186
            self.match(MiniGoParser.TYPE)
            self.state = 187
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.state = 188
                self.structDefinition()
                pass
            elif token in [9]:
                self.state = 189
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
            self.state = 192
            self.match(MiniGoParser.CONST)
            self.state = 193
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 194
            self.match(MiniGoParser.ASSIGN)
            self.state = 195
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
            self.state = 197
            self.match(MiniGoParser.FUNC)
            self.state = 198
            self.match(MiniGoParser.LPAREN)
            self.state = 199
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 200
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 201
            self.match(MiniGoParser.RPAREN)
            self.state = 202
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 203
            self.match(MiniGoParser.LPAREN)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 204
                self.funcParams()


            self.state = 207
            self.match(MiniGoParser.RPAREN)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398509497344) != 0):
                self.state = 208
                self.baseType()


            self.state = 211
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
            self.state = 213
            self.match(MiniGoParser.STRUCT)
            self.state = 214
            self.match(MiniGoParser.LBRACE)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==54:
                self.state = 215
                self.structFields()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 221
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
        self.enterRule(localctx, 22, self.RULE_structFields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12, 13, 49, 54]:
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 224
                    self.arrayDims()


                self.state = 227
                self.baseType()
                pass
            elif token in [8]:
                self.state = 228
                self.structDefinition()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 231
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
            self.state = 233
            self.match(MiniGoParser.INTERFACE)
            self.state = 234
            self.match(MiniGoParser.LBRACE)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==54:
                self.state = 235
                self.interfaceFields()
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 241
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
            self.state = 243
            self.match(MiniGoParser.LPAREN)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==54:
                self.state = 244
                self.listIdentifier()
                self.state = 245
                self.baseType()
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 252
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
            self.state = 254
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 255
                self.match(MiniGoParser.COMMA)
                self.state = 256
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 261
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
            self.state = 262
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 263
            self.listParams()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014398509497344) != 0):
                self.state = 264
                self.baseType()


            self.state = 267
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
            self.state = 269
            self.funcParam()
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 270
                self.match(MiniGoParser.COMMA)
                self.state = 271
                self.funcParam()
                self.state = 276
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
            self.state = 277
            self.match(MiniGoParser.IDENTIFIER)

            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 278
                self.arrayDims()


            self.state = 281
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
            self.state = 283
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
            self.state = 285
            self.logicAndExp()
            self.state = 290
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 286
                    self.match(MiniGoParser.OR)
                    self.state = 287
                    self.logicOrExp() 
                self.state = 292
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
            self.state = 293
            self.equalityExp()
            self.state = 298
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 294
                    self.match(MiniGoParser.AND)
                    self.state = 295
                    self.logicAndExp() 
                self.state = 300
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
            self.state = 301
            self.additiveExp()
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33822867456) != 0):
                self.state = 302
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33822867456) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 303
                self.additiveExp()
                self.state = 308
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
            self.state = 309
            self.multiplicativeExp()
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24 or _la==25:
                self.state = 310
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 311
                self.multiplicativeExp()
                self.state = 316
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
            self.state = 317
            self.unaryExp()
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0):
                self.state = 318
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 319
                self.unaryExp()
                self.state = 324
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
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                _la = self._input.LA(1)
                if not(_la==25 or _la==37):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 326
                self.unaryExp()
                pass
            elif token in [14, 15, 16, 45, 54, 55, 56, 57]:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
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

        def postfixExp(self):
            return self.getTypedRuleContext(MiniGoParser.PostfixExpContext,0)


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
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.postfixExp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.match(MiniGoParser.LPAREN)
                self.state = 332
                self.expression()
                self.state = 333
                self.match(MiniGoParser.RPAREN)
                pass


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

        def term(self):
            return self.getTypedRuleContext(MiniGoParser.TermContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def postfixOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.PostfixOpContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.PostfixOpContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_postfixExp




    def postfixExp(self):

        localctx = MiniGoParser.PostfixExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_postfixExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15, 16, 54, 55, 56, 57]:
                self.state = 337
                self.term()
                pass
            elif token in [45]:
                self.state = 338
                self.match(MiniGoParser.LPAREN)
                self.state = 339
                self.expression()
                self.state = 340
                self.match(MiniGoParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43 or _la==49:
                self.state = 344
                self.postfixOp()
                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def term(self):
            return self.getTypedRuleContext(MiniGoParser.TermContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_postfixOp




    def postfixOp(self):

        localctx = MiniGoParser.PostfixOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_postfixOp)
        try:
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.match(MiniGoParser.LBRACKET)
                self.state = 351
                self.expression()
                self.state = 352
                self.match(MiniGoParser.RBRACKET)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.match(MiniGoParser.DOT)
                self.state = 355
                self.term()
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

        def callStatement(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_term




    def term(self):

        localctx = MiniGoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_term)
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 360
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 361
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 362
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 363
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 364
                self.callStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 365
                self.match(MiniGoParser.IDENTIFIER)
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
        self.enterRule(localctx, 58, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.assignStatement()
                self.state = 369
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.ifStatement()
                self.state = 372
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 374
                self.forStatement()
                self.state = 375
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 377
                self.breakStatement()
                self.state = 378
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 380
                self.continueStatement()
                self.state = 381
                self.endOfStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 383
                self.callStatement()
                self.state = 384
                self.endOfStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 386
                self.returnStatement()
                self.state = 387
                self.endOfStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 389
                self.varDecl()
                self.state = 390
                self.endOfStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 392
                self.typeDecl()
                self.state = 393
                self.endOfStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 395
                self.methodDecl()
                self.state = 396
                self.endOfStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 398
                self.constDecl()
                self.state = 399
                self.endOfStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 401
                self.block()
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & 4620693217682128897) != 0):
                    self.state = 402
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
        self.enterRule(localctx, 60, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.arrayDims()
            self.state = 408
            self.baseType()
            self.state = 409
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
        self.enterRule(localctx, 62, self.RULE_arraysBlock)
        self._la = 0 # Token type
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.match(MiniGoParser.LBRACE)
                self.state = 412
                self.arraysBlock()
                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==51:
                    self.state = 413
                    self.match(MiniGoParser.COMMA)
                    self.state = 414
                    self.arraysBlock()
                    self.state = 419
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 420
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.match(MiniGoParser.LBRACE)
                self.state = 423
                self.expression()
                self.state = 428
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==51:
                    self.state = 424
                    self.match(MiniGoParser.COMMA)
                    self.state = 425
                    self.expression()
                    self.state = 430
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 431
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
        self.enterRule(localctx, 64, self.RULE_structExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 436
            self.match(MiniGoParser.LBRACE)
            self.state = 448
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 437
                self.structFieldsAssign()
                self.state = 442
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 438
                        self.match(MiniGoParser.COMMA)
                        self.state = 439
                        self.structFieldsAssign() 
                    self.state = 444
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

                self.state = 446
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==51:
                    self.state = 445
                    self.match(MiniGoParser.COMMA)




            self.state = 450
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def structExpression(self):
            return self.getTypedRuleContext(MiniGoParser.StructExpressionContext,0)


        def structDefinition(self):
            return self.getTypedRuleContext(MiniGoParser.StructDefinitionContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COLON)
            else:
                return self.getToken(MiniGoParser.COLON, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structBlock




    def structBlock(self):

        localctx = MiniGoParser.StructBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_structBlock)
        self._la = 0 # Token type
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 454
                self.structExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 455
                self.structDefinition()
                self.state = 456
                self.match(MiniGoParser.LBRACE)
                self.state = 476
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 270251299486941184) != 0):
                    self.state = 459
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        self.state = 457
                        self.match(MiniGoParser.IDENTIFIER)
                        self.state = 458
                        self.match(MiniGoParser.COLON)


                    self.state = 461
                    self.expression()
                    self.state = 470
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 462
                            self.match(MiniGoParser.COMMA)
                            self.state = 465
                            self._errHandler.sync(self)
                            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                            if la_ == 1:
                                self.state = 463
                                self.match(MiniGoParser.IDENTIFIER)
                                self.state = 464
                                self.match(MiniGoParser.COLON)


                            self.state = 467
                            self.expression() 
                        self.state = 472
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

                    self.state = 474
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==51:
                        self.state = 473
                        self.match(MiniGoParser.COMMA)




                self.state = 478
                self.match(MiniGoParser.RBRACE)
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
        self.enterRule(localctx, 68, self.RULE_structFieldsAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 483
            self.match(MiniGoParser.COLON)
            self.state = 484
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
        self.enterRule(localctx, 70, self.RULE_assignStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.a1()
            self.state = 491
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 487
                self.match(MiniGoParser.COMMA)
                self.state = 488
                self.a1()
                self.state = 493
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 494
            self.assignmentOperator()
            self.state = 495
            self.a2()
            self.state = 500
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==51:
                self.state = 496
                self.match(MiniGoParser.COMMA)
                self.state = 497
                self.a2()
                self.state = 502
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DOT)
            else:
                return self.getToken(MiniGoParser.DOT, i)

        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_a1




    def a1(self):

        localctx = MiniGoParser.A1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_a1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 508
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 504
                self.match(MiniGoParser.DOT)
                self.state = 505
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 510
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 512
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 511
                self.arrayDims()


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
        self.enterRule(localctx, 74, self.RULE_a2)
        try:
            self.state = 517
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 514
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 516
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
        self.enterRule(localctx, 76, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
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
        self.enterRule(localctx, 78, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(MiniGoParser.IF)
            self.state = 522
            self.expression()
            self.state = 523
            self.block()
            self.state = 525
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.state = 524
                self.match(MiniGoParser.NEWLINE)


            self.state = 536
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 527
                    self.match(MiniGoParser.ELSE)
                    self.state = 528
                    self.match(MiniGoParser.IF)
                    self.state = 529
                    self.expression()
                    self.state = 530
                    self.block()
                    self.state = 532
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                    if la_ == 1:
                        self.state = 531
                        self.match(MiniGoParser.NEWLINE)

             
                self.state = 538
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

            self.state = 541
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 539
                self.match(MiniGoParser.ELSE)
                self.state = 540
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
        self.enterRule(localctx, 80, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
            self.match(MiniGoParser.FOR)
            self.state = 546
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.state = 544
                self.forLoop()
                pass

            elif la_ == 2:
                self.state = 545
                self.forIteration()
                pass


            self.state = 548
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
        self.enterRule(localctx, 82, self.RULE_forLoop)
        try:
            self.state = 557
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 550
                self.forCondition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 551
                self.initilization()
                self.state = 552
                self.match(MiniGoParser.SEMI)
                self.state = 553
                self.forCondition()
                self.state = 554
                self.match(MiniGoParser.SEMI)
                self.state = 555
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
        self.enterRule(localctx, 84, self.RULE_initilization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 560
            self.match(MiniGoParser.DECLARE)
            self.state = 561
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
        self.enterRule(localctx, 86, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
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
        self.enterRule(localctx, 88, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 566
            self.assignmentOperator()
            self.state = 567
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
        self.enterRule(localctx, 90, self.RULE_forIteration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            _la = self._input.LA(1)
            if not(_la==44 or _la==54):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 570
            self.match(MiniGoParser.COMMA)
            self.state = 571
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 572
            self.match(MiniGoParser.DECLARE)
            self.state = 573
            self.match(MiniGoParser.RANGE)
            self.state = 574
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
        self.enterRule(localctx, 92, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
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
        self.enterRule(localctx, 94, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
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
        self.enterRule(localctx, 96, self.RULE_callStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 583
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 581
                self.match(MiniGoParser.DOT)
                self.state = 582
                self.match(MiniGoParser.IDENTIFIER)


            self.state = 585
            self.match(MiniGoParser.LPAREN)
            self.state = 594
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 270251299486941184) != 0):
                self.state = 586
                self.expression()
                self.state = 591
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==51:
                    self.state = 587
                    self.match(MiniGoParser.COMMA)
                    self.state = 588
                    self.expression()
                    self.state = 593
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 596
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


        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def arraysBlock(self):
            return self.getTypedRuleContext(MiniGoParser.ArraysBlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStatement




    def returnStatement(self):

        localctx = MiniGoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 598
            self.match(MiniGoParser.RETURN)
            self.state = 604
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15, 16, 25, 37, 45, 54, 55, 56, 57]:
                self.state = 599
                self.expression()
                pass
            elif token in [49]:
                self.state = 600
                self.arrayDims()
                self.state = 601
                self.baseType()
                self.state = 602
                self.arraysBlock()
                pass
            elif token in [-1, 52, 61]:
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
        self.enterRule(localctx, 100, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self.match(MiniGoParser.LBRACE)
            self.state = 610
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 18155135999803636) != 0):
                self.state = 607
                self.statement()
                self.state = 612
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 613
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
        self.enterRule(localctx, 102, self.RULE_arrayDims)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 620 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 615
                self.match(MiniGoParser.LBRACKET)
                self.state = 617
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 270251299486941184) != 0):
                    self.state = 616
                    self.expression()


                self.state = 619
                self.match(MiniGoParser.RBRACKET)
                self.state = 622 
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





