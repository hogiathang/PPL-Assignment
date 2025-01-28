# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u01cb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\7\2V\n\2\f\2\16\2Y\13")
        buf.write("\2\3\2\3\2\7\2]\n\2\f\2\16\2`\13\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\5\6p\n\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\5\7w\n\7\3\b\3\b\3\b\3\b\7\b}\n\b\f\b\16")
        buf.write("\b\u0080\13\b\3\b\5\b\u0083\n\b\3\b\3\b\5\b\u0087\n\b")
        buf.write("\3\b\3\b\5\b\u008b\n\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u0093")
        buf.write("\n\t\3\t\3\t\5\t\u0097\n\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\5\f\u00b0\n\f\3\f\3\f\3\f\3\r\3\r\5\r")
        buf.write("\u00b7\n\r\3\16\3\16\3\16\7\16\u00bc\n\16\f\16\16\16\u00bf")
        buf.write("\13\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\7\21\u00d2\n\21")
        buf.write("\f\21\16\21\u00d5\13\21\3\21\3\21\3\22\3\22\3\22\7\22")
        buf.write("\u00dc\n\22\f\22\16\22\u00df\13\22\3\23\3\23\3\23\5\23")
        buf.write("\u00e4\n\23\3\23\3\23\3\24\3\24\3\24\7\24\u00eb\n\24\f")
        buf.write("\24\16\24\u00ee\13\24\3\25\3\25\3\25\3\26\3\26\3\26\3")
        buf.write("\26\5\26\u00f7\n\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0108\n")
        buf.write("\26\f\26\16\26\u010b\13\26\3\27\3\27\3\27\3\27\5\27\u0111")
        buf.write("\n\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u011a\n")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u0126\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3")
        buf.write("\32\3\32\3\32\7\32\u0132\n\32\f\32\16\32\u0135\13\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\7\32\u013d\n\32\f\32\16\32")
        buf.write("\u0140\13\32\3\32\3\32\5\32\u0144\n\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\5\33\u014c\n\33\7\33\u014e\n\33\f\33\16")
        buf.write("\33\u0151\13\33\3\33\3\33\3\34\3\34\3\34\3\34\5\34\u0159")
        buf.write("\n\34\3\34\3\34\3\34\5\34\u015e\n\34\3\34\3\34\3\35\3")
        buf.write("\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\7\36\u0170\n\36\f\36\16\36\u0173\13\36\3\36")
        buf.write("\3\36\5\36\u0177\n\36\3\36\3\36\3\37\3\37\3\37\5\37\u017e")
        buf.write("\n\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \5 \u0189\n \3!\3")
        buf.write("!\3!\3!\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3&\3&\3&\3\'\3\'\3\'\5\'\u01a5\n\'\3\'\3\'\3\'\3")
        buf.write("\'\7\'\u01ab\n\'\f\'\16\'\u01ae\13\'\5\'\u01b0\n\'\3\'")
        buf.write("\3\'\3\'\3(\3(\5(\u01b7\n(\3(\3(\3)\3)\7)\u01bd\n)\f)")
        buf.write("\16)\u01c0\13)\3)\3)\3*\3*\3*\6*\u01c7\n*\r*\16*\u01c8")
        buf.write("\3*\2\3*+\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&")
        buf.write("(*,.\60\62\64\668:<>@BDFHJLNPR\2\13\3\2\r\20\4\3\4\4\67")
        buf.write("\67\4\2\34\34((\3\2 %\3\2\33\34\3\2\35\37\4\2\f\r\17\20")
        buf.write("\4\2\32\32)-\4\2//99\2\u01dc\2W\3\2\2\2\4c\3\2\2\2\6i")
        buf.write("\3\2\2\2\bk\3\2\2\2\no\3\2\2\2\fv\3\2\2\2\16x\3\2\2\2")
        buf.write("\20\u008e\3\2\2\2\22\u009b\3\2\2\2\24\u009f\3\2\2\2\26")
        buf.write("\u00a5\3\2\2\2\30\u00b6\3\2\2\2\32\u00b8\3\2\2\2\34\u00c3")
        buf.write("\3\2\2\2\36\u00c7\3\2\2\2 \u00cd\3\2\2\2\"\u00d8\3\2\2")
        buf.write("\2$\u00e0\3\2\2\2&\u00e7\3\2\2\2(\u00ef\3\2\2\2*\u00f6")
        buf.write("\3\2\2\2,\u0119\3\2\2\2.\u0125\3\2\2\2\60\u0127\3\2\2")
        buf.write("\2\62\u0143\3\2\2\2\64\u0145\3\2\2\2\66\u0154\3\2\2\2")
        buf.write("8\u0161\3\2\2\2:\u0163\3\2\2\2<\u017a\3\2\2\2>\u0188\3")
        buf.write("\2\2\2@\u018a\3\2\2\2B\u018e\3\2\2\2D\u0190\3\2\2\2F\u0194")
        buf.write("\3\2\2\2H\u019b\3\2\2\2J\u019e\3\2\2\2L\u01a1\3\2\2\2")
        buf.write("N\u01b4\3\2\2\2P\u01ba\3\2\2\2R\u01c6\3\2\2\2TV\5\f\7")
        buf.write("\2UT\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2XZ\3\2\2\2Y")
        buf.write("W\3\2\2\2Z^\5\4\3\2[]\5\f\7\2\\[\3\2\2\2]`\3\2\2\2^\\")
        buf.write("\3\2\2\2^_\3\2\2\2_a\3\2\2\2`^\3\2\2\2ab\7\2\2\3b\3\3")
        buf.write("\2\2\2cd\7\t\2\2de\7\3\2\2ef\7\60\2\2fg\7\61\2\2gh\5P")
        buf.write(")\2h\5\3\2\2\2ij\t\2\2\2j\7\3\2\2\2kl\t\3\2\2l\t\3\2\2")
        buf.write("\2mp\5\f\7\2np\5.\30\2om\3\2\2\2on\3\2\2\2p\13\3\2\2\2")
        buf.write("qw\5\16\b\2rw\5\20\t\2sw\5\22\n\2tw\5\24\13\2uw\5\26\f")
        buf.write("\2vq\3\2\2\2vr\3\2\2\2vs\3\2\2\2vt\3\2\2\2vu\3\2\2\2w")
        buf.write("\r\3\2\2\2xy\7\25\2\2y~\79\2\2z{\7\66\2\2{}\79\2\2|z\3")
        buf.write("\2\2\2}\u0080\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\u0082")
        buf.write("\3\2\2\2\u0080~\3\2\2\2\u0081\u0083\5R*\2\u0082\u0081")
        buf.write("\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u008a\3\2\2\2\u0084")
        buf.write("\u008b\5\6\4\2\u0085\u0087\5\6\4\2\u0086\u0085\3\2\2\2")
        buf.write("\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\7")
        buf.write("\31\2\2\u0089\u008b\5*\26\2\u008a\u0084\3\2\2\2\u008a")
        buf.write("\u0086\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\5\b\5\2")
        buf.write("\u008d\17\3\2\2\2\u008e\u008f\7\t\2\2\u008f\u0090\79\2")
        buf.write("\2\u0090\u0092\7\60\2\2\u0091\u0093\5&\24\2\u0092\u0091")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\u0096\7\61\2\2\u0095\u0097\5\6\4\2\u0096\u0095\3\2\2")
        buf.write("\2\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099")
        buf.write("\5P)\2\u0099\u009a\5\b\5\2\u009a\21\3\2\2\2\u009b\u009c")
        buf.write("\7\n\2\2\u009c\u009d\79\2\2\u009d\u009e\5\30\r\2\u009e")
        buf.write("\23\3\2\2\2\u009f\u00a0\7\24\2\2\u00a0\u00a1\79\2\2\u00a1")
        buf.write("\u00a2\7\31\2\2\u00a2\u00a3\5*\26\2\u00a3\u00a4\5\b\5")
        buf.write("\2\u00a4\25\3\2\2\2\u00a5\u00a6\7\t\2\2\u00a6\u00a7\7")
        buf.write("\60\2\2\u00a7\u00a8\79\2\2\u00a8\u00a9\79\2\2\u00a9\u00aa")
        buf.write("\7\61\2\2\u00aa\u00ab\79\2\2\u00ab\u00ac\7\60\2\2\u00ac")
        buf.write("\u00ad\5&\24\2\u00ad\u00af\7\61\2\2\u00ae\u00b0\5\6\4")
        buf.write("\2\u00af\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1")
        buf.write("\3\2\2\2\u00b1\u00b2\5P)\2\u00b2\u00b3\5\b\5\2\u00b3\27")
        buf.write("\3\2\2\2\u00b4\u00b7\5\32\16\2\u00b5\u00b7\5\36\20\2\u00b6")
        buf.write("\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\31\3\2\2\2\u00b8")
        buf.write("\u00b9\7\13\2\2\u00b9\u00bd\7\62\2\2\u00ba\u00bc\5\34")
        buf.write("\17\2\u00bb\u00ba\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd\u00bb")
        buf.write("\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c0\3\2\2\2\u00bf")
        buf.write("\u00bd\3\2\2\2\u00c0\u00c1\7\63\2\2\u00c1\u00c2\5\b\5")
        buf.write("\2\u00c2\33\3\2\2\2\u00c3\u00c4\79\2\2\u00c4\u00c5\5\6")
        buf.write("\4\2\u00c5\u00c6\5\b\5\2\u00c6\35\3\2\2\2\u00c7\u00c8")
        buf.write("\7\f\2\2\u00c8\u00c9\7\62\2\2\u00c9\u00ca\5$\23\2\u00ca")
        buf.write("\u00cb\7\63\2\2\u00cb\u00cc\5\b\5\2\u00cc\37\3\2\2\2\u00cd")
        buf.write("\u00d3\7\60\2\2\u00ce\u00cf\5\"\22\2\u00cf\u00d0\5\6\4")
        buf.write("\2\u00d0\u00d2\3\2\2\2\u00d1\u00ce\3\2\2\2\u00d2\u00d5")
        buf.write("\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4")
        buf.write("\u00d6\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d7\7\61\2")
        buf.write("\2\u00d7!\3\2\2\2\u00d8\u00dd\79\2\2\u00d9\u00da\7\66")
        buf.write("\2\2\u00da\u00dc\79\2\2\u00db\u00d9\3\2\2\2\u00dc\u00df")
        buf.write("\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de")
        buf.write("#\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e1\79\2\2\u00e1")
        buf.write("\u00e3\5 \21\2\u00e2\u00e4\5\6\4\2\u00e3\u00e2\3\2\2\2")
        buf.write("\u00e3\u00e4\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6\5")
        buf.write("\b\5\2\u00e6%\3\2\2\2\u00e7\u00ec\5(\25\2\u00e8\u00e9")
        buf.write("\7\66\2\2\u00e9\u00eb\5(\25\2\u00ea\u00e8\3\2\2\2\u00eb")
        buf.write("\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2")
        buf.write("\u00ed\'\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f0\79\2")
        buf.write("\2\u00f0\u00f1\5\6\4\2\u00f1)\3\2\2\2\u00f2\u00f3\b\26")
        buf.write("\1\2\u00f3\u00f4\t\4\2\2\u00f4\u00f7\5,\27\2\u00f5\u00f7")
        buf.write("\5,\27\2\u00f6\u00f2\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7")
        buf.write("\u0109\3\2\2\2\u00f8\u00f9\f\t\2\2\u00f9\u00fa\7\'\2\2")
        buf.write("\u00fa\u0108\5,\27\2\u00fb\u00fc\f\b\2\2\u00fc\u00fd\7")
        buf.write("&\2\2\u00fd\u0108\5,\27\2\u00fe\u00ff\f\7\2\2\u00ff\u0100")
        buf.write("\t\5\2\2\u0100\u0108\5,\27\2\u0101\u0102\f\6\2\2\u0102")
        buf.write("\u0103\t\6\2\2\u0103\u0108\5,\27\2\u0104\u0105\f\5\2\2")
        buf.write("\u0105\u0106\t\7\2\2\u0106\u0108\5,\27\2\u0107\u00f8\3")
        buf.write("\2\2\2\u0107\u00fb\3\2\2\2\u0107\u00fe\3\2\2\2\u0107\u0101")
        buf.write("\3\2\2\2\u0107\u0104\3\2\2\2\u0108\u010b\3\2\2\2\u0109")
        buf.write("\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a+\3\2\2\2\u010b")
        buf.write("\u0109\3\2\2\2\u010c\u0110\79\2\2\u010d\u0111\5R*\2\u010e")
        buf.write("\u010f\7.\2\2\u010f\u0111\79\2\2\u0110\u010d\3\2\2\2\u0110")
        buf.write("\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u011a\3\2\2\2")
        buf.write("\u0112\u011a\7:\2\2\u0113\u011a\7;\2\2\u0114\u011a\7<")
        buf.write("\2\2\u0115\u0116\7\60\2\2\u0116\u0117\5*\26\2\u0117\u0118")
        buf.write("\7\61\2\2\u0118\u011a\3\2\2\2\u0119\u010c\3\2\2\2\u0119")
        buf.write("\u0112\3\2\2\2\u0119\u0113\3\2\2\2\u0119\u0114\3\2\2\2")
        buf.write("\u0119\u0115\3\2\2\2\u011a-\3\2\2\2\u011b\u0126\5\66\34")
        buf.write("\2\u011c\u0126\5:\36\2\u011d\u0126\5<\37\2\u011e\u0126")
        buf.write("\5H%\2\u011f\u0126\5J&\2\u0120\u0126\5L\'\2\u0121\u0126")
        buf.write("\5N(\2\u0122\u0126\5\60\31\2\u0123\u0126\5\16\b\2\u0124")
        buf.write("\u0126\5\24\13\2\u0125\u011b\3\2\2\2\u0125\u011c\3\2\2")
        buf.write("\2\u0125\u011d\3\2\2\2\u0125\u011e\3\2\2\2\u0125\u011f")
        buf.write("\3\2\2\2\u0125\u0120\3\2\2\2\u0125\u0121\3\2\2\2\u0125")
        buf.write("\u0122\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0124\3\2\2\2")
        buf.write("\u0126/\3\2\2\2\u0127\u0128\79\2\2\u0128\u0129\7\32\2")
        buf.write("\2\u0129\u012a\5R*\2\u012a\u012b\t\b\2\2\u012b\u012c\5")
        buf.write("\62\32\2\u012c\61\3\2\2\2\u012d\u012e\7\62\2\2\u012e\u0133")
        buf.write("\5\62\32\2\u012f\u0130\7\66\2\2\u0130\u0132\5\62\32\2")
        buf.write("\u0131\u012f\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0131\3")
        buf.write("\2\2\2\u0133\u0134\3\2\2\2\u0134\u0136\3\2\2\2\u0135\u0133")
        buf.write("\3\2\2\2\u0136\u0137\7\63\2\2\u0137\u0144\3\2\2\2\u0138")
        buf.write("\u0139\7\62\2\2\u0139\u013e\5*\26\2\u013a\u013b\7\66\2")
        buf.write("\2\u013b\u013d\5*\26\2\u013c\u013a\3\2\2\2\u013d\u0140")
        buf.write("\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f")
        buf.write("\u0141\3\2\2\2\u0140\u013e\3\2\2\2\u0141\u0142\7\63\2")
        buf.write("\2\u0142\u0144\3\2\2\2\u0143\u012d\3\2\2\2\u0143\u0138")
        buf.write("\3\2\2\2\u0144\63\3\2\2\2\u0145\u0146\79\2\2\u0146\u014f")
        buf.write("\7\62\2\2\u0147\u0148\79\2\2\u0148\u0149\78\2\2\u0149")
        buf.write("\u014b\5*\26\2\u014a\u014c\7\66\2\2\u014b\u014a\3\2\2")
        buf.write("\2\u014b\u014c\3\2\2\2\u014c\u014e\3\2\2\2\u014d\u0147")
        buf.write("\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u0150\u0152\3\2\2\2\u0151\u014f\3\2\2\2")
        buf.write("\u0152\u0153\7\63\2\2\u0153\65\3\2\2\2\u0154\u0158\79")
        buf.write("\2\2\u0155\u0159\5R*\2\u0156\u0157\7.\2\2\u0157\u0159")
        buf.write("\79\2\2\u0158\u0155\3\2\2\2\u0158\u0156\3\2\2\2\u0158")
        buf.write("\u0159\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015d\58\35\2")
        buf.write("\u015b\u015e\5*\26\2\u015c\u015e\5\64\33\2\u015d\u015b")
        buf.write("\3\2\2\2\u015d\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f")
        buf.write("\u0160\5\b\5\2\u0160\67\3\2\2\2\u0161\u0162\t\t\2\2\u0162")
        buf.write("9\3\2\2\2\u0163\u0164\7\5\2\2\u0164\u0165\7\60\2\2\u0165")
        buf.write("\u0166\5*\26\2\u0166\u0167\7\61\2\2\u0167\u0171\5P)\2")
        buf.write("\u0168\u0169\7\6\2\2\u0169\u016a\7\5\2\2\u016a\u016b\7")
        buf.write("\60\2\2\u016b\u016c\5*\26\2\u016c\u016d\7\61\2\2\u016d")
        buf.write("\u016e\5P)\2\u016e\u0170\3\2\2\2\u016f\u0168\3\2\2\2\u0170")
        buf.write("\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172\3\2\2\2")
        buf.write("\u0172\u0176\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0175\7")
        buf.write("\6\2\2\u0175\u0177\5P)\2\u0176\u0174\3\2\2\2\u0176\u0177")
        buf.write("\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u0179\5\b\5\2\u0179")
        buf.write(";\3\2\2\2\u017a\u017d\7\7\2\2\u017b\u017e\5> \2\u017c")
        buf.write("\u017e\5F$\2\u017d\u017b\3\2\2\2\u017d\u017c\3\2\2\2\u017e")
        buf.write("\u017f\3\2\2\2\u017f\u0180\5P)\2\u0180=\3\2\2\2\u0181")
        buf.write("\u0189\5B\"\2\u0182\u0183\5@!\2\u0183\u0184\7\67\2\2\u0184")
        buf.write("\u0185\5B\"\2\u0185\u0186\7\67\2\2\u0186\u0187\5D#\2\u0187")
        buf.write("\u0189\3\2\2\2\u0188\u0181\3\2\2\2\u0188\u0182\3\2\2\2")
        buf.write("\u0189?\3\2\2\2\u018a\u018b\79\2\2\u018b\u018c\7\32\2")
        buf.write("\2\u018c\u018d\5*\26\2\u018dA\3\2\2\2\u018e\u018f\5*\26")
        buf.write("\2\u018fC\3\2\2\2\u0190\u0191\79\2\2\u0191\u0192\58\35")
        buf.write("\2\u0192\u0193\5*\26\2\u0193E\3\2\2\2\u0194\u0195\t\n")
        buf.write("\2\2\u0195\u0196\7\66\2\2\u0196\u0197\79\2\2\u0197\u0198")
        buf.write("\7\32\2\2\u0198\u0199\7\30\2\2\u0199\u019a\79\2\2\u019a")
        buf.write("G\3\2\2\2\u019b\u019c\7\27\2\2\u019c\u019d\5\b\5\2\u019d")
        buf.write("I\3\2\2\2\u019e\u019f\7\26\2\2\u019f\u01a0\5\b\5\2\u01a0")
        buf.write("K\3\2\2\2\u01a1\u01a4\79\2\2\u01a2\u01a3\7.\2\2\u01a3")
        buf.write("\u01a5\79\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2")
        buf.write("\u01a5\u01a6\3\2\2\2\u01a6\u01af\7\60\2\2\u01a7\u01ac")
        buf.write("\5*\26\2\u01a8\u01a9\7\66\2\2\u01a9\u01ab\5*\26\2\u01aa")
        buf.write("\u01a8\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2")
        buf.write("\u01ac\u01ad\3\2\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3")
        buf.write("\2\2\2\u01af\u01a7\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b1")
        buf.write("\3\2\2\2\u01b1\u01b2\7\61\2\2\u01b2\u01b3\5\b\5\2\u01b3")
        buf.write("M\3\2\2\2\u01b4\u01b6\7\b\2\2\u01b5\u01b7\5*\26\2\u01b6")
        buf.write("\u01b5\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\3\2\2\2")
        buf.write("\u01b8\u01b9\5\b\5\2\u01b9O\3\2\2\2\u01ba\u01be\7\62\2")
        buf.write("\2\u01bb\u01bd\5.\30\2\u01bc\u01bb\3\2\2\2\u01bd\u01c0")
        buf.write("\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf")
        buf.write("\u01c1\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01c2\7\63\2")
        buf.write("\2\u01c2Q\3\2\2\2\u01c3\u01c4\7\64\2\2\u01c4\u01c5\7:")
        buf.write("\2\2\u01c5\u01c7\7\65\2\2\u01c6\u01c3\3\2\2\2\u01c7\u01c8")
        buf.write("\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9")
        buf.write("S\3\2\2\2*W^ov~\u0082\u0086\u008a\u0092\u0096\u00af\u00b6")
        buf.write("\u00bd\u00d3\u00dd\u00e3\u00ec\u00f6\u0107\u0109\u0110")
        buf.write("\u0119\u0125\u0133\u013e\u0143\u014b\u014f\u0158\u015d")
        buf.write("\u0171\u0176\u017d\u0188\u01a4\u01ac\u01af\u01b6\u01be")
        buf.write("\u01c8")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'\n'", "'if'", "'else'", "'for'", 
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
        self.checkVersion("4.9.2")
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainFunction" ):
                return visitor.visitMainFunction(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTYPE" ):
                return visitor.visitTYPE(self)
            else:
                return visitor.visitChildren(self)




    def tYPE(self):

        localctx = MiniGoParser.TYPEContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tYPE)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndOfStatement" ):
                return visitor.visitEndOfStatement(self)
            else:
                return visitor.visitChildren(self)




    def endOfStatement(self):

        localctx = MiniGoParser.EndOfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_endOfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            _la = self._input.LA(1)
            if not(((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.T__1 - -1)) | (1 << (MiniGoParser.SEMI - -1)))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParserRuleSpec" ):
                return visitor.visitParserRuleSpec(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.COMMA:
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
            if _la==MiniGoParser.LBRACKET:
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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 143
                self.funcParams()


            self.state = 146
            self.match(MiniGoParser.RPAREN)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDecl" ):
                return visitor.visitTypeDecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDecl" ):
                return visitor.visitConstDecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDefinition" ):
                return visitor.visitTypeDefinition(self)
            else:
                return visitor.visitChildren(self)




    def typeDefinition(self):

        localctx = MiniGoParser.TypeDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_typeDefinition)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.structDefinition()
                pass
            elif token in [MiniGoParser.INTERFACE]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDefinition" ):
                return visitor.visitStructDefinition(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.IDENTIFIER:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFields" ):
                return visitor.visitStructFields(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDefinition" ):
                return visitor.visitInterfaceDefinition(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListParams" ):
                return visitor.visitListParams(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.IDENTIFIER:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListIdentifier" ):
                return visitor.visitListIdentifier(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceFields" ):
                return visitor.visitInterfaceFields(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncParams" ):
                return visitor.visitFuncParams(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncParam" ):
                return visitor.visitFuncParam(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



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
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.state = 241
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 242
                self.term()
                pass
            elif token in [MiniGoParser.LPAREN, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
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
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LEQ) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GEQ))) != 0)):
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
                        if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
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
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = MiniGoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_term)
        try:
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
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
            elif token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 273
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 274
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.LPAREN]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




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
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INTERFACE) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraysBlock" ):
                return visitor.visitArraysBlock(self)
            else:
                return visitor.visitChildren(self)




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
                while _la==MiniGoParser.COMMA:
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
                while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructExpression" ):
                return visitor.visitStructExpression(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 325
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 326
                self.match(MiniGoParser.COLON)
                self.state = 327
                self.expression(0)
                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




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
            if token in [MiniGoParser.LBRACKET]:
                self.state = 339
                self.arrayDims()
                pass
            elif token in [MiniGoParser.DOT]:
                self.state = 340
                self.match(MiniGoParser.DOT)
                self.state = 341
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.DECLARE, MiniGoParser.PLUS_ASSIGN, MiniGoParser.MINUS_ASSIGN, MiniGoParser.MUL_ASSIGN, MiniGoParser.DIV_ASSIGN, MiniGoParser.MOD_ASSIGN]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = MiniGoParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DECLARE) | (1 << MiniGoParser.PLUS_ASSIGN) | (1 << MiniGoParser.MINUS_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.ELSE:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitilization" ):
                return visitor.visitInitilization(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForIteration" ):
                return visitor.visitForIteration(self)
            else:
                return visitor.visitChildren(self)




    def forIteration(self):

        localctx = MiniGoParser.ForIterationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_forIteration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.BLANK or _la==MiniGoParser.IDENTIFIER):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.DOT:
                self.state = 416
                self.match(MiniGoParser.DOT)
                self.state = 417
                self.match(MiniGoParser.IDENTIFIER)


            self.state = 420
            self.match(MiniGoParser.LPAREN)
            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 421
                self.expression(0)
                self.state = 426
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDims" ):
                return visitor.visitArrayDims(self)
            else:
                return visitor.visitChildren(self)




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
         




