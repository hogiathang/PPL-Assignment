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
        4,1,65,457,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,1,0,5,0,84,8,0,10,0,12,0,87,9,0,1,0,1,0,5,0,91,8,0,10,
        0,12,0,94,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,
        4,1,4,3,4,110,8,4,1,5,1,5,1,5,1,5,1,5,3,5,117,8,5,1,6,1,6,1,6,1,
        6,5,6,123,8,6,10,6,12,6,126,9,6,1,6,3,6,129,8,6,1,6,1,6,3,6,133,
        8,6,1,6,1,6,3,6,137,8,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,145,8,7,1,7,
        1,7,3,7,149,8,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,174,8,
        10,1,10,1,10,1,10,1,11,1,11,3,11,181,8,11,1,12,1,12,1,12,5,12,186,
        8,12,10,12,12,12,189,9,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,
        1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,5,15,208,8,15,10,15,
        12,15,211,9,15,1,15,1,15,1,16,1,16,1,16,5,16,218,8,16,10,16,12,16,
        221,9,16,1,17,1,17,1,17,3,17,226,8,17,1,17,1,17,1,18,1,18,1,18,5,
        18,233,8,18,10,18,12,18,236,9,18,1,19,1,19,1,19,1,20,1,20,1,20,1,
        20,3,20,245,8,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,5,20,262,8,20,10,20,12,20,265,9,20,1,
        21,1,21,1,21,1,21,3,21,271,8,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,3,21,280,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,3,22,292,8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,
        24,5,24,304,8,24,10,24,12,24,307,9,24,1,24,1,24,1,24,1,24,1,24,1,
        24,5,24,315,8,24,10,24,12,24,318,9,24,1,24,1,24,3,24,322,8,24,1,
        25,1,25,1,25,1,25,1,25,1,25,3,25,330,8,25,5,25,332,8,25,10,25,12,
        25,335,9,25,1,25,1,25,1,26,1,26,1,26,1,26,3,26,343,8,26,1,26,1,26,
        1,26,3,26,348,8,26,1,26,1,26,1,27,1,27,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,5,28,366,8,28,10,28,12,28,369,
        9,28,1,28,1,28,3,28,373,8,28,1,28,1,28,1,29,1,29,1,29,3,29,380,8,
        29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,391,8,30,1,
        31,1,31,1,31,1,31,1,32,1,32,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,
        34,1,34,1,34,1,34,1,35,1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,3,
        37,419,8,37,1,37,1,37,1,37,1,37,5,37,425,8,37,10,37,12,37,428,9,
        37,3,37,430,8,37,1,37,1,37,1,37,1,38,1,38,3,38,437,8,38,1,38,1,38,
        1,39,1,39,5,39,443,8,39,10,39,12,39,446,9,39,1,39,1,39,1,40,1,40,
        1,40,4,40,453,8,40,11,40,12,40,454,1,40,0,1,40,41,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,74,76,78,80,0,9,1,0,11,14,2,1,2,2,53,53,
        2,0,26,26,38,38,1,0,30,35,1,0,25,26,1,0,27,29,2,0,10,11,13,14,2,
        0,24,24,39,43,2,0,45,45,55,55,474,0,85,1,0,0,0,2,97,1,0,0,0,4,103,
        1,0,0,0,6,105,1,0,0,0,8,109,1,0,0,0,10,116,1,0,0,0,12,118,1,0,0,
        0,14,140,1,0,0,0,16,153,1,0,0,0,18,157,1,0,0,0,20,163,1,0,0,0,22,
        180,1,0,0,0,24,182,1,0,0,0,26,193,1,0,0,0,28,197,1,0,0,0,30,203,
        1,0,0,0,32,214,1,0,0,0,34,222,1,0,0,0,36,229,1,0,0,0,38,237,1,0,
        0,0,40,244,1,0,0,0,42,279,1,0,0,0,44,291,1,0,0,0,46,293,1,0,0,0,
        48,321,1,0,0,0,50,323,1,0,0,0,52,338,1,0,0,0,54,351,1,0,0,0,56,353,
        1,0,0,0,58,376,1,0,0,0,60,390,1,0,0,0,62,392,1,0,0,0,64,396,1,0,
        0,0,66,398,1,0,0,0,68,402,1,0,0,0,70,409,1,0,0,0,72,412,1,0,0,0,
        74,415,1,0,0,0,76,434,1,0,0,0,78,440,1,0,0,0,80,452,1,0,0,0,82,84,
        3,10,5,0,83,82,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,
        86,88,1,0,0,0,87,85,1,0,0,0,88,92,3,2,1,0,89,91,3,10,5,0,90,89,1,
        0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,
        92,1,0,0,0,95,96,5,0,0,1,96,1,1,0,0,0,97,98,5,7,0,0,98,99,5,1,0,
        0,99,100,5,46,0,0,100,101,5,47,0,0,101,102,3,78,39,0,102,3,1,0,0,
        0,103,104,7,0,0,0,104,5,1,0,0,0,105,106,7,1,0,0,106,7,1,0,0,0,107,
        110,3,10,5,0,108,110,3,44,22,0,109,107,1,0,0,0,109,108,1,0,0,0,110,
        9,1,0,0,0,111,117,3,12,6,0,112,117,3,14,7,0,113,117,3,16,8,0,114,
        117,3,18,9,0,115,117,3,20,10,0,116,111,1,0,0,0,116,112,1,0,0,0,116,
        113,1,0,0,0,116,114,1,0,0,0,116,115,1,0,0,0,117,11,1,0,0,0,118,119,
        5,19,0,0,119,124,5,55,0,0,120,121,5,52,0,0,121,123,5,55,0,0,122,
        120,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,
        128,1,0,0,0,126,124,1,0,0,0,127,129,3,80,40,0,128,127,1,0,0,0,128,
        129,1,0,0,0,129,136,1,0,0,0,130,137,3,4,2,0,131,133,3,4,2,0,132,
        131,1,0,0,0,132,133,1,0,0,0,133,134,1,0,0,0,134,135,5,23,0,0,135,
        137,3,40,20,0,136,130,1,0,0,0,136,132,1,0,0,0,137,138,1,0,0,0,138,
        139,3,6,3,0,139,13,1,0,0,0,140,141,5,7,0,0,141,142,5,55,0,0,142,
        144,5,46,0,0,143,145,3,36,18,0,144,143,1,0,0,0,144,145,1,0,0,0,145,
        146,1,0,0,0,146,148,5,47,0,0,147,149,3,4,2,0,148,147,1,0,0,0,148,
        149,1,0,0,0,149,150,1,0,0,0,150,151,3,78,39,0,151,152,3,6,3,0,152,
        15,1,0,0,0,153,154,5,8,0,0,154,155,5,55,0,0,155,156,3,22,11,0,156,
        17,1,0,0,0,157,158,5,18,0,0,158,159,5,55,0,0,159,160,5,23,0,0,160,
        161,3,40,20,0,161,162,3,6,3,0,162,19,1,0,0,0,163,164,5,7,0,0,164,
        165,5,46,0,0,165,166,5,55,0,0,166,167,5,55,0,0,167,168,5,47,0,0,
        168,169,5,55,0,0,169,170,5,46,0,0,170,171,3,36,18,0,171,173,5,47,
        0,0,172,174,3,4,2,0,173,172,1,0,0,0,173,174,1,0,0,0,174,175,1,0,
        0,0,175,176,3,78,39,0,176,177,3,6,3,0,177,21,1,0,0,0,178,181,3,24,
        12,0,179,181,3,28,14,0,180,178,1,0,0,0,180,179,1,0,0,0,181,23,1,
        0,0,0,182,183,5,9,0,0,183,187,5,48,0,0,184,186,3,26,13,0,185,184,
        1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,190,
        1,0,0,0,189,187,1,0,0,0,190,191,5,49,0,0,191,192,3,6,3,0,192,25,
        1,0,0,0,193,194,5,55,0,0,194,195,3,4,2,0,195,196,3,6,3,0,196,27,
        1,0,0,0,197,198,5,10,0,0,198,199,5,48,0,0,199,200,3,34,17,0,200,
        201,5,49,0,0,201,202,3,6,3,0,202,29,1,0,0,0,203,209,5,46,0,0,204,
        205,3,32,16,0,205,206,3,4,2,0,206,208,1,0,0,0,207,204,1,0,0,0,208,
        211,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,212,1,0,0,0,211,
        209,1,0,0,0,212,213,5,47,0,0,213,31,1,0,0,0,214,219,5,55,0,0,215,
        216,5,52,0,0,216,218,5,55,0,0,217,215,1,0,0,0,218,221,1,0,0,0,219,
        217,1,0,0,0,219,220,1,0,0,0,220,33,1,0,0,0,221,219,1,0,0,0,222,223,
        5,55,0,0,223,225,3,30,15,0,224,226,3,4,2,0,225,224,1,0,0,0,225,226,
        1,0,0,0,226,227,1,0,0,0,227,228,3,6,3,0,228,35,1,0,0,0,229,234,3,
        38,19,0,230,231,5,52,0,0,231,233,3,38,19,0,232,230,1,0,0,0,233,236,
        1,0,0,0,234,232,1,0,0,0,234,235,1,0,0,0,235,37,1,0,0,0,236,234,1,
        0,0,0,237,238,5,55,0,0,238,239,3,4,2,0,239,39,1,0,0,0,240,241,6,
        20,-1,0,241,242,7,2,0,0,242,245,3,42,21,0,243,245,3,42,21,0,244,
        240,1,0,0,0,244,243,1,0,0,0,245,263,1,0,0,0,246,247,10,7,0,0,247,
        248,5,37,0,0,248,262,3,42,21,0,249,250,10,6,0,0,250,251,5,36,0,0,
        251,262,3,42,21,0,252,253,10,5,0,0,253,254,7,3,0,0,254,262,3,42,
        21,0,255,256,10,4,0,0,256,257,7,4,0,0,257,262,3,42,21,0,258,259,
        10,3,0,0,259,260,7,5,0,0,260,262,3,42,21,0,261,246,1,0,0,0,261,249,
        1,0,0,0,261,252,1,0,0,0,261,255,1,0,0,0,261,258,1,0,0,0,262,265,
        1,0,0,0,263,261,1,0,0,0,263,264,1,0,0,0,264,41,1,0,0,0,265,263,1,
        0,0,0,266,270,5,55,0,0,267,271,3,80,40,0,268,269,5,44,0,0,269,271,
        5,55,0,0,270,267,1,0,0,0,270,268,1,0,0,0,270,271,1,0,0,0,271,280,
        1,0,0,0,272,280,5,56,0,0,273,280,5,57,0,0,274,280,5,58,0,0,275,276,
        5,46,0,0,276,277,3,40,20,0,277,278,5,47,0,0,278,280,1,0,0,0,279,
        266,1,0,0,0,279,272,1,0,0,0,279,273,1,0,0,0,279,274,1,0,0,0,279,
        275,1,0,0,0,280,43,1,0,0,0,281,292,3,52,26,0,282,292,3,56,28,0,283,
        292,3,58,29,0,284,292,3,70,35,0,285,292,3,72,36,0,286,292,3,74,37,
        0,287,292,3,76,38,0,288,292,3,46,23,0,289,292,3,12,6,0,290,292,3,
        18,9,0,291,281,1,0,0,0,291,282,1,0,0,0,291,283,1,0,0,0,291,284,1,
        0,0,0,291,285,1,0,0,0,291,286,1,0,0,0,291,287,1,0,0,0,291,288,1,
        0,0,0,291,289,1,0,0,0,291,290,1,0,0,0,292,45,1,0,0,0,293,294,5,55,
        0,0,294,295,5,24,0,0,295,296,3,80,40,0,296,297,7,6,0,0,297,298,3,
        48,24,0,298,47,1,0,0,0,299,300,5,48,0,0,300,305,3,48,24,0,301,302,
        5,52,0,0,302,304,3,48,24,0,303,301,1,0,0,0,304,307,1,0,0,0,305,303,
        1,0,0,0,305,306,1,0,0,0,306,308,1,0,0,0,307,305,1,0,0,0,308,309,
        5,49,0,0,309,322,1,0,0,0,310,311,5,48,0,0,311,316,3,40,20,0,312,
        313,5,52,0,0,313,315,3,40,20,0,314,312,1,0,0,0,315,318,1,0,0,0,316,
        314,1,0,0,0,316,317,1,0,0,0,317,319,1,0,0,0,318,316,1,0,0,0,319,
        320,5,49,0,0,320,322,1,0,0,0,321,299,1,0,0,0,321,310,1,0,0,0,322,
        49,1,0,0,0,323,324,5,55,0,0,324,333,5,48,0,0,325,326,5,55,0,0,326,
        327,5,54,0,0,327,329,3,40,20,0,328,330,5,52,0,0,329,328,1,0,0,0,
        329,330,1,0,0,0,330,332,1,0,0,0,331,325,1,0,0,0,332,335,1,0,0,0,
        333,331,1,0,0,0,333,334,1,0,0,0,334,336,1,0,0,0,335,333,1,0,0,0,
        336,337,5,49,0,0,337,51,1,0,0,0,338,342,5,55,0,0,339,343,3,80,40,
        0,340,341,5,44,0,0,341,343,5,55,0,0,342,339,1,0,0,0,342,340,1,0,
        0,0,342,343,1,0,0,0,343,344,1,0,0,0,344,347,3,54,27,0,345,348,3,
        40,20,0,346,348,3,50,25,0,347,345,1,0,0,0,347,346,1,0,0,0,348,349,
        1,0,0,0,349,350,3,6,3,0,350,53,1,0,0,0,351,352,7,7,0,0,352,55,1,
        0,0,0,353,354,5,3,0,0,354,355,5,46,0,0,355,356,3,40,20,0,356,357,
        5,47,0,0,357,367,3,78,39,0,358,359,5,4,0,0,359,360,5,3,0,0,360,361,
        5,46,0,0,361,362,3,40,20,0,362,363,5,47,0,0,363,364,3,78,39,0,364,
        366,1,0,0,0,365,358,1,0,0,0,366,369,1,0,0,0,367,365,1,0,0,0,367,
        368,1,0,0,0,368,372,1,0,0,0,369,367,1,0,0,0,370,371,5,4,0,0,371,
        373,3,78,39,0,372,370,1,0,0,0,372,373,1,0,0,0,373,374,1,0,0,0,374,
        375,3,6,3,0,375,57,1,0,0,0,376,379,5,5,0,0,377,380,3,60,30,0,378,
        380,3,68,34,0,379,377,1,0,0,0,379,378,1,0,0,0,380,381,1,0,0,0,381,
        382,3,78,39,0,382,59,1,0,0,0,383,391,3,64,32,0,384,385,3,62,31,0,
        385,386,5,53,0,0,386,387,3,64,32,0,387,388,5,53,0,0,388,389,3,66,
        33,0,389,391,1,0,0,0,390,383,1,0,0,0,390,384,1,0,0,0,391,61,1,0,
        0,0,392,393,5,55,0,0,393,394,5,24,0,0,394,395,3,40,20,0,395,63,1,
        0,0,0,396,397,3,40,20,0,397,65,1,0,0,0,398,399,5,55,0,0,399,400,
        3,54,27,0,400,401,3,40,20,0,401,67,1,0,0,0,402,403,7,8,0,0,403,404,
        5,52,0,0,404,405,5,55,0,0,405,406,5,24,0,0,406,407,5,22,0,0,407,
        408,5,55,0,0,408,69,1,0,0,0,409,410,5,21,0,0,410,411,3,6,3,0,411,
        71,1,0,0,0,412,413,5,20,0,0,413,414,3,6,3,0,414,73,1,0,0,0,415,418,
        5,55,0,0,416,417,5,44,0,0,417,419,5,55,0,0,418,416,1,0,0,0,418,419,
        1,0,0,0,419,420,1,0,0,0,420,429,5,46,0,0,421,426,3,40,20,0,422,423,
        5,52,0,0,423,425,3,40,20,0,424,422,1,0,0,0,425,428,1,0,0,0,426,424,
        1,0,0,0,426,427,1,0,0,0,427,430,1,0,0,0,428,426,1,0,0,0,429,421,
        1,0,0,0,429,430,1,0,0,0,430,431,1,0,0,0,431,432,5,47,0,0,432,433,
        3,6,3,0,433,75,1,0,0,0,434,436,5,6,0,0,435,437,3,40,20,0,436,435,
        1,0,0,0,436,437,1,0,0,0,437,438,1,0,0,0,438,439,3,6,3,0,439,77,1,
        0,0,0,440,444,5,48,0,0,441,443,3,44,22,0,442,441,1,0,0,0,443,446,
        1,0,0,0,444,442,1,0,0,0,444,445,1,0,0,0,445,447,1,0,0,0,446,444,
        1,0,0,0,447,448,5,49,0,0,448,79,1,0,0,0,449,450,5,50,0,0,450,451,
        5,56,0,0,451,453,5,51,0,0,452,449,1,0,0,0,453,454,1,0,0,0,454,452,
        1,0,0,0,454,455,1,0,0,0,455,81,1,0,0,0,40,85,92,109,116,124,128,
        132,136,144,148,173,180,187,209,219,225,234,244,261,263,270,279,
        291,305,316,321,329,333,342,347,367,372,379,390,418,426,429,436,
        444,454
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'\\n'", "'if'", "'else'", "'for'", 
                     "'return'", "'func'", "'type'", "'struct'", "'interface'", 
                     "'string'", "'int'", "'float'", "'boolean'", "'true'", 
                     "'false'", "'nil'", "'const'", "'var'", "'continue'", 
                     "'break'", "'range'", "'='", "':='", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'&&'", "'||'", "'!'", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'.'", "'_'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "IF", "ELSE", 
                      "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
                      "STRING", "INT", "FLOAT", "BOOLEAN", "TRUE", "FALSE", 
                      "NIL", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "ASSIGN", "DECLARE", "PLUS", "MINUS", "MUL", "DIV", 
                      "MOD", "EQ", "NEQ", "LT", "LEQ", "GT", "GEQ", "AND", 
                      "OR", "NOT", "PLUS_ASSIGN", "MINUS_ASSIGN", "MUL_ASSIGN", 
                      "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "BLANK", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
                      "COMMA", "SEMI", "COLON", "IDENTIFIER", "INT_LIT", 
                      "FLOAT_LIT", "STRING_LIT", "BOOL_LIT", "BLOCK_COMMENT", 
                      "LINE_COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_mainFunction = 1
    RULE_tYPE = 2
    RULE_endOfStatement = 3
    RULE_parserRuleSpec = 4
    RULE_declaration = 5
    RULE_varDecl = 6
    RULE_funcDecl = 7
    RULE_typeDecl = 8
    RULE_constDecl = 9
    RULE_methodDecl = 10
    RULE_typeDefinition = 11
    RULE_structDefinition = 12
    RULE_structFields = 13
    RULE_interfaceDefinition = 14
    RULE_listParams = 15
    RULE_listIdentifier = 16
    RULE_interfaceFields = 17
    RULE_funcParams = 18
    RULE_funcParam = 19
    RULE_expression = 20
    RULE_term = 21
    RULE_statement = 22
    RULE_arrayLiteral = 23
    RULE_arraysBlock = 24
    RULE_structExpression = 25
    RULE_assignStatement = 26
    RULE_assignmentOperator = 27
    RULE_ifStatement = 28
    RULE_forStatement = 29
    RULE_forLoop = 30
    RULE_initilization = 31
    RULE_forCondition = 32
    RULE_forUpdate = 33
    RULE_forIteration = 34
    RULE_breakStatement = 35
    RULE_continueStatement = 36
    RULE_callStatement = 37
    RULE_returnStatement = 38
    RULE_block = 39
    RULE_arrayDims = 40

    ruleNames =  [ "program", "mainFunction", "tYPE", "endOfStatement", 
                   "parserRuleSpec", "declaration", "varDecl", "funcDecl", 
                   "typeDecl", "constDecl", "methodDecl", "typeDefinition", 
                   "structDefinition", "structFields", "interfaceDefinition", 
                   "listParams", "listIdentifier", "interfaceFields", "funcParams", 
                   "funcParam", "expression", "term", "statement", "arrayLiteral", 
                   "arraysBlock", "structExpression", "assignStatement", 
                   "assignmentOperator", "ifStatement", "forStatement", 
                   "forLoop", "initilization", "forCondition", "forUpdate", 
                   "forIteration", "breakStatement", "continueStatement", 
                   "callStatement", "returnStatement", "block", "arrayDims" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    IF=3
    ELSE=4
    FOR=5
    RETURN=6
    FUNC=7
    TYPE=8
    STRUCT=9
    INTERFACE=10
    STRING=11
    INT=12
    FLOAT=13
    BOOLEAN=14
    TRUE=15
    FALSE=16
    NIL=17
    CONST=18
    VAR=19
    CONTINUE=20
    BREAK=21
    RANGE=22
    ASSIGN=23
    DECLARE=24
    PLUS=25
    MINUS=26
    MUL=27
    DIV=28
    MOD=29
    EQ=30
    NEQ=31
    LT=32
    LEQ=33
    GT=34
    GEQ=35
    AND=36
    OR=37
    NOT=38
    PLUS_ASSIGN=39
    MINUS_ASSIGN=40
    MUL_ASSIGN=41
    DIV_ASSIGN=42
    MOD_ASSIGN=43
    DOT=44
    BLANK=45
    LPAREN=46
    RPAREN=47
    LBRACE=48
    RBRACE=49
    LBRACKET=50
    RBRACKET=51
    COMMA=52
    SEMI=53
    COLON=54
    IDENTIFIER=55
    INT_LIT=56
    FLOAT_LIT=57
    STRING_LIT=58
    BOOL_LIT=59
    BLOCK_COMMENT=60
    LINE_COMMENT=61
    WS=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64
    ERROR_CHAR=65

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

        def mainFunction(self):
            return self.getTypedRuleContext(MiniGoParser.MainFunctionContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclarationContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 82
                    self.declaration() 
                self.state = 87
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 88
            self.mainFunction()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 786816) != 0):
                self.state = 89
                self.declaration()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_mainFunction




    def mainFunction(self):

        localctx = MiniGoParser.MainFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mainFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(MiniGoParser.FUNC)
            self.state = 98
            self.match(MiniGoParser.T__0)
            self.state = 99
            self.match(MiniGoParser.LPAREN)
            self.state = 100
            self.match(MiniGoParser.RPAREN)
            self.state = 101
            self.block()
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

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

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
        self.enterRule(localctx, 4, self.RULE_tYPE)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0)):
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

        def getRuleIndex(self):
            return MiniGoParser.RULE_endOfStatement




    def endOfStatement(self):

        localctx = MiniGoParser.EndOfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_endOfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            _la = self._input.LA(1)
            if not(((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & 18014398509481993) != 0)):
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

        def declaration(self):
            return self.getTypedRuleContext(MiniGoParser.DeclarationContext,0)


        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parserRuleSpec




    def parserRuleSpec(self):

        localctx = MiniGoParser.ParserRuleSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parserRuleSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 107
                self.declaration()
                pass

            elif la_ == 2:
                self.state = 108
                self.statement()
                pass


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
        self.enterRule(localctx, 10, self.RULE_declaration)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.funcDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                self.typeDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 114
                self.constDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 115
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def tYPE(self):
            return self.getTypedRuleContext(MiniGoParser.TYPEContext,0)


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
        self.enterRule(localctx, 12, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(MiniGoParser.VAR)
            self.state = 119
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==52:
                self.state = 120
                self.match(MiniGoParser.COMMA)
                self.state = 121
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 127
                self.arrayDims()


            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 130
                self.tYPE()
                pass

            elif la_ == 2:
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0):
                    self.state = 131
                    self.tYPE()


                self.state = 134
                self.match(MiniGoParser.ASSIGN)
                self.state = 135
                self.expression(0)
                pass


            self.state = 138
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

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

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
        self.enterRule(localctx, 14, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(MiniGoParser.FUNC)
            self.state = 141
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 142
            self.match(MiniGoParser.LPAREN)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 143
                self.funcParams()


            self.state = 146
            self.match(MiniGoParser.RPAREN)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0):
                self.state = 147
                self.tYPE()


            self.state = 150
            self.block()
            self.state = 151
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
        self.enterRule(localctx, 16, self.RULE_typeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(MiniGoParser.TYPE)
            self.state = 154
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 155
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

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constDecl




    def constDecl(self):

        localctx = MiniGoParser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(MiniGoParser.CONST)
            self.state = 158
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 159
            self.match(MiniGoParser.ASSIGN)
            self.state = 160
            self.expression(0)
            self.state = 161
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
        self.enterRule(localctx, 20, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(MiniGoParser.FUNC)
            self.state = 164
            self.match(MiniGoParser.LPAREN)
            self.state = 165
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 166
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 167
            self.match(MiniGoParser.RPAREN)
            self.state = 168
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 169
            self.match(MiniGoParser.LPAREN)

            self.state = 170
            self.funcParams()
            self.state = 171
            self.match(MiniGoParser.RPAREN)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0):
                self.state = 172
                self.tYPE()


            self.state = 175
            self.block()
            self.state = 176
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
        self.enterRule(localctx, 22, self.RULE_typeDefinition)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.structDefinition()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

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
        self.enterRule(localctx, 24, self.RULE_structDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(MiniGoParser.STRUCT)
            self.state = 183
            self.match(MiniGoParser.LBRACE)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 184
                self.structFields()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 190
            self.match(MiniGoParser.RBRACE)
            self.state = 191
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
        self.enterRule(localctx, 26, self.RULE_structFields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 194
            self.tYPE()
            self.state = 195
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

        def interfaceFields(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceFieldsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceDefinition




    def interfaceDefinition(self):

        localctx = MiniGoParser.InterfaceDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_interfaceDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(MiniGoParser.INTERFACE)
            self.state = 198
            self.match(MiniGoParser.LBRACE)
            self.state = 199
            self.interfaceFields()
            self.state = 200
            self.match(MiniGoParser.RBRACE)
            self.state = 201
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

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

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
        self.enterRule(localctx, 30, self.RULE_listParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(MiniGoParser.LPAREN)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 204
                self.listIdentifier()
                self.state = 205
                self.tYPE()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 212
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
        self.enterRule(localctx, 32, self.RULE_listIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==52:
                self.state = 215
                self.match(MiniGoParser.COMMA)
                self.state = 216
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 221
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
        self.enterRule(localctx, 34, self.RULE_interfaceFields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 223
            self.listParams()
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0):
                self.state = 224
                self.tYPE()


            self.state = 227
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
        self.enterRule(localctx, 36, self.RULE_funcParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.funcParam()
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==52:
                self.state = 230
                self.match(MiniGoParser.COMMA)
                self.state = 231
                self.funcParam()
                self.state = 236
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
        self.enterRule(localctx, 38, self.RULE_funcParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 238
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


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniGoParser.NEQ, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LEQ(self):
            return self.getToken(MiniGoParser.LEQ, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GEQ(self):
            return self.getToken(MiniGoParser.GEQ, 0)

        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 38]:
                self.state = 241
                _la = self._input.LA(1)
                if not(_la==26 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 242
                self.term()
                pass
            elif token in [46, 55, 56, 57, 58]:
                self.state = 243
                self.term()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 261
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 246
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 247
                        self.match(MiniGoParser.OR)
                        self.state = 248
                        self.term()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 249
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 250
                        self.match(MiniGoParser.AND)
                        self.state = 251
                        self.term()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 252
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 253
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67645734912) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 254
                        self.term()
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 255
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 256
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 257
                        self.term()
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 258
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 259
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 260
                        self.term()
                        pass

             
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_term




    def term(self):

        localctx = MiniGoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_term)
        try:
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 270
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 267
                    self.arrayDims()

                elif la_ == 2:
                    self.state = 268
                    self.match(MiniGoParser.DOT)
                    self.state = 269
                    self.match(MiniGoParser.IDENTIFIER)


                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 3)
                self.state = 273
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 4)
                self.state = 274
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 5)
                self.state = 275
                self.match(MiniGoParser.LPAREN)
                self.state = 276
                self.expression(0)
                self.state = 277
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
        self.enterRule(localctx, 44, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 281
                self.assignStatement()
                pass

            elif la_ == 2:
                self.state = 282
                self.ifStatement()
                pass

            elif la_ == 3:
                self.state = 283
                self.forStatement()
                pass

            elif la_ == 4:
                self.state = 284
                self.breakStatement()
                pass

            elif la_ == 5:
                self.state = 285
                self.continueStatement()
                pass

            elif la_ == 6:
                self.state = 286
                self.callStatement()
                pass

            elif la_ == 7:
                self.state = 287
                self.returnStatement()
                pass

            elif la_ == 8:
                self.state = 288
                self.arrayLiteral()
                pass

            elif la_ == 9:
                self.state = 289
                self.varDecl()
                pass

            elif la_ == 10:
                self.state = 290
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

        def DECLARE(self):
            return self.getToken(MiniGoParser.DECLARE, 0)

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
        self.enterRule(localctx, 46, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 294
            self.match(MiniGoParser.DECLARE)

            self.state = 295
            self.arrayDims()
            self.state = 296
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 27648) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 297
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
        self.enterRule(localctx, 48, self.RULE_arraysBlock)
        self._la = 0 # Token type
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(MiniGoParser.LBRACE)
                self.state = 300
                self.arraysBlock()
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==52:
                    self.state = 301
                    self.match(MiniGoParser.COMMA)
                    self.state = 302
                    self.arraysBlock()
                    self.state = 307
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 308
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.match(MiniGoParser.LBRACE)
                self.state = 311
                self.expression(0)
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==52:
                    self.state = 312
                    self.match(MiniGoParser.COMMA)
                    self.state = 313
                    self.expression(0)
                    self.state = 318
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 319
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
        self.enterRule(localctx, 50, self.RULE_structExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 324
            self.match(MiniGoParser.LBRACE)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 325
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 326
                self.match(MiniGoParser.COLON)
                self.state = 327
                self.expression(0)
                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52:
                    self.state = 328
                    self.match(MiniGoParser.COMMA)


                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 336
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
        self.enterRule(localctx, 52, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.state = 339
                self.arrayDims()
                pass
            elif token in [44]:
                self.state = 340
                self.match(MiniGoParser.DOT)
                self.state = 341
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [24, 39, 40, 41, 42, 43]:
                pass
            else:
                pass
            self.state = 344
            self.assignmentOperator()
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 345
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 346
                self.structExpression()
                pass


            self.state = 349
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
        self.enterRule(localctx, 54, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17042447007744) != 0)):
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

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

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
        self.enterRule(localctx, 56, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(MiniGoParser.IF)
            self.state = 354
            self.match(MiniGoParser.LPAREN)
            self.state = 355
            self.expression(0)
            self.state = 356
            self.match(MiniGoParser.RPAREN)
            self.state = 357
            self.block()
            self.state = 367
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 358
                    self.match(MiniGoParser.ELSE)
                    self.state = 359
                    self.match(MiniGoParser.IF)
                    self.state = 360
                    self.match(MiniGoParser.LPAREN)
                    self.state = 361
                    self.expression(0)
                    self.state = 362
                    self.match(MiniGoParser.RPAREN)
                    self.state = 363
                    self.block() 
                self.state = 369
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

            self.state = 372
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 370
                self.match(MiniGoParser.ELSE)
                self.state = 371
                self.block()


            self.state = 374
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
        self.enterRule(localctx, 58, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(MiniGoParser.FOR)
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 377
                self.forLoop()
                pass

            elif la_ == 2:
                self.state = 378
                self.forIteration()
                pass


            self.state = 381
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
        self.enterRule(localctx, 60, self.RULE_forLoop)
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.forCondition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.initilization()
                self.state = 385
                self.match(MiniGoParser.SEMI)
                self.state = 386
                self.forCondition()
                self.state = 387
                self.match(MiniGoParser.SEMI)
                self.state = 388
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
        self.enterRule(localctx, 62, self.RULE_initilization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 393
            self.match(MiniGoParser.DECLARE)
            self.state = 394
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
        self.enterRule(localctx, 64, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
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
        self.enterRule(localctx, 66, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 399
            self.assignmentOperator()
            self.state = 400
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
        self.enterRule(localctx, 68, self.RULE_forIteration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            _la = self._input.LA(1)
            if not(_la==45 or _la==55):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 403
            self.match(MiniGoParser.COMMA)
            self.state = 404
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 405
            self.match(MiniGoParser.DECLARE)
            self.state = 406
            self.match(MiniGoParser.RANGE)
            self.state = 407
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
        self.enterRule(localctx, 70, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(MiniGoParser.BREAK)
            self.state = 410
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
        self.enterRule(localctx, 72, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(MiniGoParser.CONTINUE)
            self.state = 413
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

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

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
        self.enterRule(localctx, 74, self.RULE_callStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 416
                self.match(MiniGoParser.DOT)
                self.state = 417
                self.match(MiniGoParser.IDENTIFIER)


            self.state = 420
            self.match(MiniGoParser.LPAREN)
            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 540502598973652992) != 0):
                self.state = 421
                self.expression(0)
                self.state = 426
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==52:
                    self.state = 422
                    self.match(MiniGoParser.COMMA)
                    self.state = 423
                    self.expression(0)
                    self.state = 428
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 431
            self.match(MiniGoParser.RPAREN)
            self.state = 432
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
        self.enterRule(localctx, 76, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(MiniGoParser.RETURN)
            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 540502598973652992) != 0):
                self.state = 435
                self.expression(0)


            self.state = 438
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
        self.enterRule(localctx, 78, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(MiniGoParser.LBRACE)
            self.state = 444
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 36028797022896232) != 0):
                self.state = 441
                self.statement()
                self.state = 446
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 447
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

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INT_LIT)
            else:
                return self.getToken(MiniGoParser.INT_LIT, i)

        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACKET)
            else:
                return self.getToken(MiniGoParser.RBRACKET, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayDims




    def arrayDims(self):

        localctx = MiniGoParser.ArrayDimsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_arrayDims)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 449
                    self.match(MiniGoParser.LBRACKET)
                    self.state = 450
                    self.match(MiniGoParser.INT_LIT)
                    self.state = 451
                    self.match(MiniGoParser.RBRACKET)

                else:
                    raise NoViableAltException(self)
                self.state = 454 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

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
        self._predicates[20] = self.expression_sempred
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
         




