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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u01bb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\3\2\6\2T\n\2\r\2\16\2U\3\2\3\2\3")
        buf.write("\3\3\3\3\4\3\4\3\5\3\5\5\5`\n\5\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6g\n\6\3\7\3\7\3\7\3\7\7\7m\n\7\f\7\16\7p\13\7\3\7\5")
        buf.write("\7s\n\7\3\7\3\7\5\7w\n\7\3\7\3\7\5\7{\n\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\5\b\u0083\n\b\3\b\3\b\5\b\u0087\n\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00a0")
        buf.write("\n\13\3\13\3\13\3\13\3\f\3\f\5\f\u00a7\n\f\3\r\3\r\3\r")
        buf.write("\7\r\u00ac\n\r\f\r\16\r\u00af\13\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\7\20\u00c2\n\20\f\20\16\20\u00c5\13\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\7\21\u00cc\n\21\f\21\16\21\u00cf")
        buf.write("\13\21\3\22\3\22\3\22\5\22\u00d4\n\22\3\22\3\22\3\23\3")
        buf.write("\23\3\23\7\23\u00db\n\23\f\23\16\23\u00de\13\23\3\24\3")
        buf.write("\24\3\24\3\25\3\25\3\25\3\25\5\25\u00e7\n\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\7\25\u00f8\n\25\f\25\16\25\u00fb\13\25\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u0101\n\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\5\26\u010a\n\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\5\27\u0116\n\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\7\31\u0122\n\31")
        buf.write("\f\31\16\31\u0125\13\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\7\31\u012d\n\31\f\31\16\31\u0130\13\31\3\31\3\31\5\31")
        buf.write("\u0134\n\31\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u013c\n")
        buf.write("\32\7\32\u013e\n\32\f\32\16\32\u0141\13\32\3\32\3\32\3")
        buf.write("\33\3\33\3\33\3\33\5\33\u0149\n\33\3\33\3\33\3\33\5\33")
        buf.write("\u014e\n\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u0160\n\35")
        buf.write("\f\35\16\35\u0163\13\35\3\35\3\35\5\35\u0167\n\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\5\36\u016e\n\36\3\36\3\36\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\5\37\u0179\n\37\3 \3 \3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3")
        buf.write("$\3%\3%\3%\3&\3&\3&\5&\u0195\n&\3&\3&\3&\3&\7&\u019b\n")
        buf.write("&\f&\16&\u019e\13&\5&\u01a0\n&\3&\3&\3&\3\'\3\'\5\'\u01a7")
        buf.write("\n\'\3\'\3\'\3(\3(\7(\u01ad\n(\f(\16(\u01b0\13(\3(\3(")
        buf.write("\3)\3)\3)\6)\u01b7\n)\r)\16)\u01b8\3)\2\3(*\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNP\2\13\4\2\13\13\16\20\4\3\66\66::\4\2\30\30")
        buf.write("$$\3\2\34!\3\2\27\30\3\2\31\33\4\2\n\13\17\20\3\2&+\4")
        buf.write("\2\26\26..\2\u01cc\2S\3\2\2\2\4Y\3\2\2\2\6[\3\2\2\2\b")
        buf.write("_\3\2\2\2\nf\3\2\2\2\fh\3\2\2\2\16~\3\2\2\2\20\u008b\3")
        buf.write("\2\2\2\22\u008f\3\2\2\2\24\u0095\3\2\2\2\26\u00a6\3\2")
        buf.write("\2\2\30\u00a8\3\2\2\2\32\u00b3\3\2\2\2\34\u00b7\3\2\2")
        buf.write("\2\36\u00bd\3\2\2\2 \u00c8\3\2\2\2\"\u00d0\3\2\2\2$\u00d7")
        buf.write("\3\2\2\2&\u00df\3\2\2\2(\u00e6\3\2\2\2*\u0109\3\2\2\2")
        buf.write(",\u0115\3\2\2\2.\u0117\3\2\2\2\60\u0133\3\2\2\2\62\u0135")
        buf.write("\3\2\2\2\64\u0144\3\2\2\2\66\u0151\3\2\2\28\u0153\3\2")
        buf.write("\2\2:\u016a\3\2\2\2<\u0178\3\2\2\2>\u017a\3\2\2\2@\u017e")
        buf.write("\3\2\2\2B\u0180\3\2\2\2D\u0184\3\2\2\2F\u018b\3\2\2\2")
        buf.write("H\u018e\3\2\2\2J\u0191\3\2\2\2L\u01a4\3\2\2\2N\u01aa\3")
        buf.write("\2\2\2P\u01b6\3\2\2\2RT\5\b\5\2SR\3\2\2\2TU\3\2\2\2US")
        buf.write("\3\2\2\2UV\3\2\2\2VW\3\2\2\2WX\7\2\2\3X\3\3\2\2\2YZ\t")
        buf.write("\2\2\2Z\5\3\2\2\2[\\\t\3\2\2\\\7\3\2\2\2]`\5\n\6\2^`\5")
        buf.write(",\27\2_]\3\2\2\2_^\3\2\2\2`\t\3\2\2\2ag\5\f\7\2bg\5\16")
        buf.write("\b\2cg\5\20\t\2dg\5\22\n\2eg\5\24\13\2fa\3\2\2\2fb\3\2")
        buf.write("\2\2fc\3\2\2\2fd\3\2\2\2fe\3\2\2\2g\13\3\2\2\2hi\7\r\2")
        buf.write("\2in\7\26\2\2jk\7\65\2\2km\7\26\2\2lj\3\2\2\2mp\3\2\2")
        buf.write("\2nl\3\2\2\2no\3\2\2\2or\3\2\2\2pn\3\2\2\2qs\5P)\2rq\3")
        buf.write("\2\2\2rs\3\2\2\2sz\3\2\2\2t{\5\4\3\2uw\5\4\3\2vu\3\2\2")
        buf.write("\2vw\3\2\2\2wx\3\2\2\2xy\7%\2\2y{\5(\25\2zt\3\2\2\2zv")
        buf.write("\3\2\2\2{|\3\2\2\2|}\5\6\4\2}\r\3\2\2\2~\177\7\7\2\2\177")
        buf.write("\u0080\7\26\2\2\u0080\u0082\7/\2\2\u0081\u0083\5$\23\2")
        buf.write("\u0082\u0081\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084\3")
        buf.write("\2\2\2\u0084\u0086\7\60\2\2\u0085\u0087\5\4\3\2\u0086")
        buf.write("\u0085\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2")
        buf.write("\u0088\u0089\5N(\2\u0089\u008a\5\6\4\2\u008a\17\3\2\2")
        buf.write("\2\u008b\u008c\7\b\2\2\u008c\u008d\7\26\2\2\u008d\u008e")
        buf.write("\5\26\f\2\u008e\21\3\2\2\2\u008f\u0090\7\f\2\2\u0090\u0091")
        buf.write("\7\26\2\2\u0091\u0092\7%\2\2\u0092\u0093\5(\25\2\u0093")
        buf.write("\u0094\5\6\4\2\u0094\23\3\2\2\2\u0095\u0096\7\7\2\2\u0096")
        buf.write("\u0097\7/\2\2\u0097\u0098\7\26\2\2\u0098\u0099\7\26\2")
        buf.write("\2\u0099\u009a\7\60\2\2\u009a\u009b\7\26\2\2\u009b\u009c")
        buf.write("\7/\2\2\u009c\u009d\5$\23\2\u009d\u009f\7\60\2\2\u009e")
        buf.write("\u00a0\5\4\3\2\u009f\u009e\3\2\2\2\u009f\u00a0\3\2\2\2")
        buf.write("\u00a0\u00a1\3\2\2\2\u00a1\u00a2\5N(\2\u00a2\u00a3\5\6")
        buf.write("\4\2\u00a3\25\3\2\2\2\u00a4\u00a7\5\30\r\2\u00a5\u00a7")
        buf.write("\5\34\17\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7")
        buf.write("\27\3\2\2\2\u00a8\u00a9\7\t\2\2\u00a9\u00ad\7\61\2\2\u00aa")
        buf.write("\u00ac\5\32\16\2\u00ab\u00aa\3\2\2\2\u00ac\u00af\3\2\2")
        buf.write("\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b0")
        buf.write("\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00b1\7\62\2\2\u00b1")
        buf.write("\u00b2\5\6\4\2\u00b2\31\3\2\2\2\u00b3\u00b4\7\26\2\2\u00b4")
        buf.write("\u00b5\5\4\3\2\u00b5\u00b6\5\6\4\2\u00b6\33\3\2\2\2\u00b7")
        buf.write("\u00b8\7\n\2\2\u00b8\u00b9\7\61\2\2\u00b9\u00ba\5\"\22")
        buf.write("\2\u00ba\u00bb\7\62\2\2\u00bb\u00bc\5\6\4\2\u00bc\35\3")
        buf.write("\2\2\2\u00bd\u00c3\7/\2\2\u00be\u00bf\5 \21\2\u00bf\u00c0")
        buf.write("\5\4\3\2\u00c0\u00c2\3\2\2\2\u00c1\u00be\3\2\2\2\u00c2")
        buf.write("\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2")
        buf.write("\u00c4\u00c6\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00c7\7")
        buf.write("\60\2\2\u00c7\37\3\2\2\2\u00c8\u00cd\7\26\2\2\u00c9\u00ca")
        buf.write("\7\65\2\2\u00ca\u00cc\7\26\2\2\u00cb\u00c9\3\2\2\2\u00cc")
        buf.write("\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2")
        buf.write("\u00ce!\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\7\26\2")
        buf.write("\2\u00d1\u00d3\5\36\20\2\u00d2\u00d4\5\4\3\2\u00d3\u00d2")
        buf.write("\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5")
        buf.write("\u00d6\5\6\4\2\u00d6#\3\2\2\2\u00d7\u00dc\5&\24\2\u00d8")
        buf.write("\u00d9\7\65\2\2\u00d9\u00db\5&\24\2\u00da\u00d8\3\2\2")
        buf.write("\2\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd")
        buf.write("\3\2\2\2\u00dd%\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e0")
        buf.write("\7\26\2\2\u00e0\u00e1\5\4\3\2\u00e1\'\3\2\2\2\u00e2\u00e3")
        buf.write("\b\25\1\2\u00e3\u00e4\t\4\2\2\u00e4\u00e7\5*\26\2\u00e5")
        buf.write("\u00e7\5*\26\2\u00e6\u00e2\3\2\2\2\u00e6\u00e5\3\2\2\2")
        buf.write("\u00e7\u00f9\3\2\2\2\u00e8\u00e9\f\t\2\2\u00e9\u00ea\7")
        buf.write("#\2\2\u00ea\u00f8\5*\26\2\u00eb\u00ec\f\b\2\2\u00ec\u00ed")
        buf.write("\7\"\2\2\u00ed\u00f8\5*\26\2\u00ee\u00ef\f\7\2\2\u00ef")
        buf.write("\u00f0\t\5\2\2\u00f0\u00f8\5*\26\2\u00f1\u00f2\f\6\2\2")
        buf.write("\u00f2\u00f3\t\6\2\2\u00f3\u00f8\5*\26\2\u00f4\u00f5\f")
        buf.write("\5\2\2\u00f5\u00f6\t\7\2\2\u00f6\u00f8\5*\26\2\u00f7\u00e8")
        buf.write("\3\2\2\2\u00f7\u00eb\3\2\2\2\u00f7\u00ee\3\2\2\2\u00f7")
        buf.write("\u00f1\3\2\2\2\u00f7\u00f4\3\2\2\2\u00f8\u00fb\3\2\2\2")
        buf.write("\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa)\3\2\2")
        buf.write("\2\u00fb\u00f9\3\2\2\2\u00fc\u0100\7\26\2\2\u00fd\u0101")
        buf.write("\5P)\2\u00fe\u00ff\7,\2\2\u00ff\u0101\7\26\2\2\u0100\u00fd")
        buf.write("\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101")
        buf.write("\u010a\3\2\2\2\u0102\u010a\7\67\2\2\u0103\u010a\78\2\2")
        buf.write("\u0104\u010a\79\2\2\u0105\u0106\7/\2\2\u0106\u0107\5(")
        buf.write("\25\2\u0107\u0108\7\60\2\2\u0108\u010a\3\2\2\2\u0109\u00fc")
        buf.write("\3\2\2\2\u0109\u0102\3\2\2\2\u0109\u0103\3\2\2\2\u0109")
        buf.write("\u0104\3\2\2\2\u0109\u0105\3\2\2\2\u010a+\3\2\2\2\u010b")
        buf.write("\u0116\5\64\33\2\u010c\u0116\58\35\2\u010d\u0116\5:\36")
        buf.write("\2\u010e\u0116\5F$\2\u010f\u0116\5H%\2\u0110\u0116\5J")
        buf.write("&\2\u0111\u0116\5L\'\2\u0112\u0116\5.\30\2\u0113\u0116")
        buf.write("\5\f\7\2\u0114\u0116\5\22\n\2\u0115\u010b\3\2\2\2\u0115")
        buf.write("\u010c\3\2\2\2\u0115\u010d\3\2\2\2\u0115\u010e\3\2\2\2")
        buf.write("\u0115\u010f\3\2\2\2\u0115\u0110\3\2\2\2\u0115\u0111\3")
        buf.write("\2\2\2\u0115\u0112\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0114")
        buf.write("\3\2\2\2\u0116-\3\2\2\2\u0117\u0118\7\26\2\2\u0118\u0119")
        buf.write("\7&\2\2\u0119\u011a\5P)\2\u011a\u011b\t\b\2\2\u011b\u011c")
        buf.write("\5\60\31\2\u011c/\3\2\2\2\u011d\u011e\7\61\2\2\u011e\u0123")
        buf.write("\5\60\31\2\u011f\u0120\7\65\2\2\u0120\u0122\5\60\31\2")
        buf.write("\u0121\u011f\3\2\2\2\u0122\u0125\3\2\2\2\u0123\u0121\3")
        buf.write("\2\2\2\u0123\u0124\3\2\2\2\u0124\u0126\3\2\2\2\u0125\u0123")
        buf.write("\3\2\2\2\u0126\u0127\7\62\2\2\u0127\u0134\3\2\2\2\u0128")
        buf.write("\u0129\7\61\2\2\u0129\u012e\5(\25\2\u012a\u012b\7\65\2")
        buf.write("\2\u012b\u012d\5(\25\2\u012c\u012a\3\2\2\2\u012d\u0130")
        buf.write("\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f")
        buf.write("\u0131\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0132\7\62\2")
        buf.write("\2\u0132\u0134\3\2\2\2\u0133\u011d\3\2\2\2\u0133\u0128")
        buf.write("\3\2\2\2\u0134\61\3\2\2\2\u0135\u0136\7\26\2\2\u0136\u013f")
        buf.write("\7\61\2\2\u0137\u0138\7\26\2\2\u0138\u0139\7-\2\2\u0139")
        buf.write("\u013b\5(\25\2\u013a\u013c\7\65\2\2\u013b\u013a\3\2\2")
        buf.write("\2\u013b\u013c\3\2\2\2\u013c\u013e\3\2\2\2\u013d\u0137")
        buf.write("\3\2\2\2\u013e\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u013f")
        buf.write("\u0140\3\2\2\2\u0140\u0142\3\2\2\2\u0141\u013f\3\2\2\2")
        buf.write("\u0142\u0143\7\62\2\2\u0143\63\3\2\2\2\u0144\u0148\7\26")
        buf.write("\2\2\u0145\u0149\5P)\2\u0146\u0147\7,\2\2\u0147\u0149")
        buf.write("\7\26\2\2\u0148\u0145\3\2\2\2\u0148\u0146\3\2\2\2\u0148")
        buf.write("\u0149\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014d\5\66\34")
        buf.write("\2\u014b\u014e\5(\25\2\u014c\u014e\5\62\32\2\u014d\u014b")
        buf.write("\3\2\2\2\u014d\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f")
        buf.write("\u0150\5\6\4\2\u0150\65\3\2\2\2\u0151\u0152\t\t\2\2\u0152")
        buf.write("\67\3\2\2\2\u0153\u0154\7\3\2\2\u0154\u0155\7/\2\2\u0155")
        buf.write("\u0156\5(\25\2\u0156\u0157\7\60\2\2\u0157\u0161\5N(\2")
        buf.write("\u0158\u0159\7\4\2\2\u0159\u015a\7\3\2\2\u015a\u015b\7")
        buf.write("/\2\2\u015b\u015c\5(\25\2\u015c\u015d\7\60\2\2\u015d\u015e")
        buf.write("\5N(\2\u015e\u0160\3\2\2\2\u015f\u0158\3\2\2\2\u0160\u0163")
        buf.write("\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0166\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0165\7\4\2\2")
        buf.write("\u0165\u0167\5N(\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2")
        buf.write("\2\2\u0167\u0168\3\2\2\2\u0168\u0169\5\6\4\2\u01699\3")
        buf.write("\2\2\2\u016a\u016d\7\5\2\2\u016b\u016e\5<\37\2\u016c\u016e")
        buf.write("\5D#\2\u016d\u016b\3\2\2\2\u016d\u016c\3\2\2\2\u016e\u016f")
        buf.write("\3\2\2\2\u016f\u0170\5N(\2\u0170;\3\2\2\2\u0171\u0179")
        buf.write("\5@!\2\u0172\u0173\5> \2\u0173\u0174\7\66\2\2\u0174\u0175")
        buf.write("\5@!\2\u0175\u0176\7\66\2\2\u0176\u0177\5B\"\2\u0177\u0179")
        buf.write("\3\2\2\2\u0178\u0171\3\2\2\2\u0178\u0172\3\2\2\2\u0179")
        buf.write("=\3\2\2\2\u017a\u017b\7\26\2\2\u017b\u017c\7&\2\2\u017c")
        buf.write("\u017d\5(\25\2\u017d?\3\2\2\2\u017e\u017f\5(\25\2\u017f")
        buf.write("A\3\2\2\2\u0180\u0181\7\26\2\2\u0181\u0182\5\66\34\2\u0182")
        buf.write("\u0183\5(\25\2\u0183C\3\2\2\2\u0184\u0185\t\n\2\2\u0185")
        buf.write("\u0186\7\65\2\2\u0186\u0187\7\26\2\2\u0187\u0188\7&\2")
        buf.write("\2\u0188\u0189\7\23\2\2\u0189\u018a\7\26\2\2\u018aE\3")
        buf.write("\2\2\2\u018b\u018c\7\22\2\2\u018c\u018d\5\6\4\2\u018d")
        buf.write("G\3\2\2\2\u018e\u018f\7\21\2\2\u018f\u0190\5\6\4\2\u0190")
        buf.write("I\3\2\2\2\u0191\u0194\7\26\2\2\u0192\u0193\7,\2\2\u0193")
        buf.write("\u0195\7\26\2\2\u0194\u0192\3\2\2\2\u0194\u0195\3\2\2")
        buf.write("\2\u0195\u0196\3\2\2\2\u0196\u019f\7/\2\2\u0197\u019c")
        buf.write("\5(\25\2\u0198\u0199\7\65\2\2\u0199\u019b\5(\25\2\u019a")
        buf.write("\u0198\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a\3\2\2\2")
        buf.write("\u019c\u019d\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3")
        buf.write("\2\2\2\u019f\u0197\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1")
        buf.write("\3\2\2\2\u01a1\u01a2\7\60\2\2\u01a2\u01a3\5\6\4\2\u01a3")
        buf.write("K\3\2\2\2\u01a4\u01a6\7\6\2\2\u01a5\u01a7\5(\25\2\u01a6")
        buf.write("\u01a5\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\3\2\2\2")
        buf.write("\u01a8\u01a9\5\6\4\2\u01a9M\3\2\2\2\u01aa\u01ae\7\61\2")
        buf.write("\2\u01ab\u01ad\5,\27\2\u01ac\u01ab\3\2\2\2\u01ad\u01b0")
        buf.write("\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af")
        buf.write("\u01b1\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b2\7\62\2")
        buf.write("\2\u01b2O\3\2\2\2\u01b3\u01b4\7\63\2\2\u01b4\u01b5\7\67")
        buf.write("\2\2\u01b5\u01b7\7\64\2\2\u01b6\u01b3\3\2\2\2\u01b7\u01b8")
        buf.write("\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9")
        buf.write("Q\3\2\2\2)U_fnrvz\u0082\u0086\u009f\u00a6\u00ad\u00c3")
        buf.write("\u00cd\u00d3\u00dc\u00e6\u00f7\u00f9\u0100\u0109\u0115")
        buf.write("\u0123\u012e\u0133\u013b\u013f\u0148\u014d\u0161\u0166")
        buf.write("\u016d\u0178\u0194\u019c\u019f\u01a6\u01ae\u01b8")
        return buf.getvalue()


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
                     "<INVALID>", "'\n'" ]

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
        self.checkVersion("4.9.2")
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
            self.state = 81 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 80
                self.parserRuleSpec()
                self.state = 83 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTYPE" ):
                return visitor.visitTYPE(self)
            else:
                return visitor.visitChildren(self)




    def tYPE(self):

        localctx = MiniGoParser.TYPEContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tYPE)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.INTERGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndOfStatement" ):
                return visitor.visitEndOfStatement(self)
            else:
                return visitor.visitChildren(self)




    def endOfStatement(self):

        localctx = MiniGoParser.EndOfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_endOfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not(((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.SEMI - -1)) | (1 << (MiniGoParser.NL - -1)))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParserRuleSpec" ):
                return visitor.visitParserRuleSpec(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.COMMA:
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
            if _la==MiniGoParser.LSB:
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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.INTERGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 127
                self.funcParams()


            self.state = 130
            self.match(MiniGoParser.RP)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.INTERGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDecl" ):
                return visitor.visitTypeDecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDecl" ):
                return visitor.visitConstDecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.INTERGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDefinition" ):
                return visitor.visitTypeDefinition(self)
            else:
                return visitor.visitChildren(self)




    def typeDefinition(self):

        localctx = MiniGoParser.TypeDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typeDefinition)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.structDefinition()
                pass
            elif token in [MiniGoParser.INTERFACE]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDefinition" ):
                return visitor.visitStructDefinition(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.IDENTIFIER:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFields" ):
                return visitor.visitStructFields(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDefinition" ):
                return visitor.visitInterfaceDefinition(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListParams" ):
                return visitor.visitListParams(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.IDENTIFIER:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListIdentifier" ):
                return visitor.visitListIdentifier(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceFields" ):
                return visitor.visitInterfaceFields(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.INTERGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncParams" ):
                return visitor.visitFuncParams(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncParam" ):
                return visitor.visitFuncParam(self)
            else:
                return visitor.visitChildren(self)




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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUBOP, MiniGoParser.NOTOP]:
                self.state = 225
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUBOP or _la==MiniGoParser.NOTOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 226
                self.term()
                pass
            elif token in [MiniGoParser.IDENTIFIER, MiniGoParser.LP, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT]:
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
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUALOP) | (1 << MiniGoParser.NOTEQUALOP) | (1 << MiniGoParser.LESSOP) | (1 << MiniGoParser.LESSEQUALOP) | (1 << MiniGoParser.GREATEROP) | (1 << MiniGoParser.GREATEREQUALOP))) != 0)):
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
                        if not(_la==MiniGoParser.ADDOP or _la==MiniGoParser.SUBOP):
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
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULOP) | (1 << MiniGoParser.DIVOP) | (1 << MiniGoParser.MODOP))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = MiniGoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_term)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
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
            elif token in [MiniGoParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(MiniGoParser.INTLIT)
                pass
            elif token in [MiniGoParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.match(MiniGoParser.FLOATLIT)
                pass
            elif token in [MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 258
                self.match(MiniGoParser.STRINGLIT)
                pass
            elif token in [MiniGoParser.LP]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




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
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INTERFACE) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraysBlock" ):
                return visitor.visitArraysBlock(self)
            else:
                return visitor.visitChildren(self)




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
                while _la==MiniGoParser.COMMA:
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
                while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructExpression" ):
                return visitor.visitStructExpression(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 309
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 310
                self.match(MiniGoParser.COLON)
                self.state = 311
                self.expression(0)
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




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
            if token in [MiniGoParser.LSB]:
                self.state = 323
                self.arrayDims()
                pass
            elif token in [MiniGoParser.DOT]:
                self.state = 324
                self.match(MiniGoParser.DOT)
                self.state = 325
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.SHORTASSIGNOP, MiniGoParser.INCASSIGNOP, MiniGoParser.DECASSIGNOP, MiniGoParser.MULASSIGNOP, MiniGoParser.DIVASSIGNOP, MiniGoParser.MODASSIGNOP]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = MiniGoParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SHORTASSIGNOP) | (1 << MiniGoParser.INCASSIGNOP) | (1 << MiniGoParser.DECASSIGNOP) | (1 << MiniGoParser.MULASSIGNOP) | (1 << MiniGoParser.DIVASSIGNOP) | (1 << MiniGoParser.MODASSIGNOP))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.ELSE:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitilization" ):
                return visitor.visitInitilization(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForIteration" ):
                return visitor.visitForIteration(self)
            else:
                return visitor.visitChildren(self)




    def forIteration(self):

        localctx = MiniGoParser.ForIterationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_forIteration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.IDENTIFIER or _la==MiniGoParser.BLANK):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.DOT:
                self.state = 400
                self.match(MiniGoParser.DOT)
                self.state = 401
                self.match(MiniGoParser.IDENTIFIER)


            self.state = 404
            self.match(MiniGoParser.LP)
            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.SUBOP) | (1 << MiniGoParser.NOTOP) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 405
                self.expression(0)
                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.SUBOP) | (1 << MiniGoParser.NOTOP) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.STRINGLIT))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDims" ):
                return visitor.visitArrayDims(self)
            else:
                return visitor.visitChildren(self)




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
         




