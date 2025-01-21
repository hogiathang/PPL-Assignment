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
        buf.write("\u0174\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2\6\2H\n\2\r\2")
        buf.write("\16\2I\3\2\3\2\3\3\3\3\3\4\3\4\5\4R\n\4\3\5\3\5\3\5\3")
        buf.write("\5\5\5X\n\5\3\6\3\6\3\6\5\6]\n\6\3\6\3\6\5\6a\n\6\3\6")
        buf.write("\3\6\5\6e\n\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7m\n\7\3\7\3\7")
        buf.write("\5\7q\n\7\3\7\3\7\5\7u\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\5\n\u0083\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\6\f\u008e\n\f\r\f\16\f\u008f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\7\17\u00a0\n\17\f\17\16\17\u00a3\13\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\7\20\u00aa\n\20\f\20\16\20\u00ad\13")
        buf.write("\20\3\21\3\21\3\21\7\21\u00b2\n\21\f\21\16\21\u00b5\13")
        buf.write("\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u00be\n\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\7\23\u00cf\n\23\f\23\16\23\u00d2")
        buf.write("\13\23\3\24\3\24\3\24\3\24\5\24\u00d8\n\24\3\24\3\24\3")
        buf.write("\24\3\24\5\24\u00de\n\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\5\25\u00e7\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\27\3\27\3\27\3\27\7\27\u00f3\n\27\f\27\16\27\u00f6\13")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u00fe\n\27\f\27")
        buf.write("\16\27\u0101\13\27\3\27\3\27\5\27\u0105\n\27\3\30\3\30")
        buf.write("\3\30\3\30\5\30\u010b\n\30\3\30\3\30\3\30\3\30\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\7\32\u011f\n\32\f\32\16\32\u0122\13\32\3\32")
        buf.write("\3\32\5\32\u0126\n\32\3\33\3\33\3\33\3\33\5\33\u012c\n")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\5\33\u0133\n\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\5\33\u013b\n\33\3\33\3\33\3\34\3")
        buf.write("\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3!\5!\u0152\n!\3!\3!\3!\3!\7!\u0158")
        buf.write("\n!\f!\16!\u015b\13!\5!\u015d\n!\3!\3!\3!\3\"\3\"\3\"")
        buf.write("\3\"\7\"\u0166\n\"\f\"\16\"\u0169\13\"\3\"\3\"\3#\3#\3")
        buf.write("#\6#\u0170\n#\r#\16#\u0171\3#\2\3$$\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BD\2\n")
        buf.write("\4\2\13\13\16\20\4\2\30\30$$\3\2\34!\3\2\27\30\3\2\31")
        buf.write("\33\4\2\n\13\17\20\3\2&+\4\2\26\26..\2\u017f\2G\3\2\2")
        buf.write("\2\4M\3\2\2\2\6Q\3\2\2\2\bW\3\2\2\2\nY\3\2\2\2\fh\3\2")
        buf.write("\2\2\16v\3\2\2\2\20z\3\2\2\2\22\u0082\3\2\2\2\24\u0084")
        buf.write("\3\2\2\2\26\u008d\3\2\2\2\30\u0091\3\2\2\2\32\u0096\3")
        buf.write("\2\2\2\34\u009b\3\2\2\2\36\u00a6\3\2\2\2 \u00ae\3\2\2")
        buf.write("\2\"\u00b6\3\2\2\2$\u00bd\3\2\2\2&\u00dd\3\2\2\2(\u00e6")
        buf.write("\3\2\2\2*\u00e8\3\2\2\2,\u0104\3\2\2\2.\u0106\3\2\2\2")
        buf.write("\60\u0110\3\2\2\2\62\u0112\3\2\2\2\64\u0127\3\2\2\2\66")
        buf.write("\u013e\3\2\2\28\u0142\3\2\2\2:\u0144\3\2\2\2<\u0148\3")
        buf.write("\2\2\2>\u014b\3\2\2\2@\u014e\3\2\2\2B\u0161\3\2\2\2D\u016f")
        buf.write("\3\2\2\2FH\5\6\4\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2")
        buf.write("\2\2JK\3\2\2\2KL\7\2\2\3L\3\3\2\2\2MN\t\2\2\2N\5\3\2\2")
        buf.write("\2OR\5\b\5\2PR\5(\25\2QO\3\2\2\2QP\3\2\2\2R\7\3\2\2\2")
        buf.write("SX\5\n\6\2TX\5\f\7\2UX\5\16\b\2VX\5\20\t\2WS\3\2\2\2W")
        buf.write("T\3\2\2\2WU\3\2\2\2WV\3\2\2\2X\t\3\2\2\2YZ\7\r\2\2Z\\")
        buf.write("\7\26\2\2[]\5D#\2\\[\3\2\2\2\\]\3\2\2\2]d\3\2\2\2^e\5")
        buf.write("\4\3\2_a\5\4\3\2`_\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\7%\2")
        buf.write("\2ce\5$\23\2d^\3\2\2\2d`\3\2\2\2ef\3\2\2\2fg\7\66\2\2")
        buf.write("g\13\3\2\2\2hi\7\7\2\2ij\7\26\2\2jl\7/\2\2km\5 \21\2l")
        buf.write("k\3\2\2\2lm\3\2\2\2mn\3\2\2\2np\7\60\2\2oq\5\4\3\2po\3")
        buf.write("\2\2\2pq\3\2\2\2qr\3\2\2\2rt\5B\"\2su\7\66\2\2ts\3\2\2")
        buf.write("\2tu\3\2\2\2u\r\3\2\2\2vw\7\b\2\2wx\7\26\2\2xy\5\22\n")
        buf.write("\2y\17\3\2\2\2z{\7\f\2\2{|\7\26\2\2|}\7%\2\2}~\5$\23\2")
        buf.write("~\177\7\66\2\2\177\21\3\2\2\2\u0080\u0083\5\24\13\2\u0081")
        buf.write("\u0083\5\30\r\2\u0082\u0080\3\2\2\2\u0082\u0081\3\2\2")
        buf.write("\2\u0083\23\3\2\2\2\u0084\u0085\7\t\2\2\u0085\u0086\7")
        buf.write("\61\2\2\u0086\u0087\5\26\f\2\u0087\u0088\7\62\2\2\u0088")
        buf.write("\25\3\2\2\2\u0089\u008a\7\26\2\2\u008a\u008b\5\4\3\2\u008b")
        buf.write("\u008c\7\66\2\2\u008c\u008e\3\2\2\2\u008d\u0089\3\2\2")
        buf.write("\2\u008e\u008f\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090")
        buf.write("\3\2\2\2\u0090\27\3\2\2\2\u0091\u0092\7\n\2\2\u0092\u0093")
        buf.write("\7\61\2\2\u0093\u0094\5\32\16\2\u0094\u0095\7\62\2\2\u0095")
        buf.write("\31\3\2\2\2\u0096\u0097\7\26\2\2\u0097\u0098\5\34\17\2")
        buf.write("\u0098\u0099\5\4\3\2\u0099\u009a\7\66\2\2\u009a\33\3\2")
        buf.write("\2\2\u009b\u00a1\7/\2\2\u009c\u009d\5\36\20\2\u009d\u009e")
        buf.write("\5\4\3\2\u009e\u00a0\3\2\2\2\u009f\u009c\3\2\2\2\u00a0")
        buf.write("\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a2\u00a4\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\7")
        buf.write("\60\2\2\u00a5\35\3\2\2\2\u00a6\u00ab\7\26\2\2\u00a7\u00a8")
        buf.write("\7\65\2\2\u00a8\u00aa\7\26\2\2\u00a9\u00a7\3\2\2\2\u00aa")
        buf.write("\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2")
        buf.write("\u00ac\37\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00b3\5\"")
        buf.write("\22\2\u00af\u00b0\7\65\2\2\u00b0\u00b2\5\"\22\2\u00b1")
        buf.write("\u00af\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2")
        buf.write("\u00b3\u00b4\3\2\2\2\u00b4!\3\2\2\2\u00b5\u00b3\3\2\2")
        buf.write("\2\u00b6\u00b7\7\26\2\2\u00b7\u00b8\5\4\3\2\u00b8#\3\2")
        buf.write("\2\2\u00b9\u00ba\b\23\1\2\u00ba\u00bb\t\3\2\2\u00bb\u00be")
        buf.write("\5&\24\2\u00bc\u00be\5&\24\2\u00bd\u00b9\3\2\2\2\u00bd")
        buf.write("\u00bc\3\2\2\2\u00be\u00d0\3\2\2\2\u00bf\u00c0\f\t\2\2")
        buf.write("\u00c0\u00c1\7#\2\2\u00c1\u00cf\5&\24\2\u00c2\u00c3\f")
        buf.write("\b\2\2\u00c3\u00c4\7\"\2\2\u00c4\u00cf\5&\24\2\u00c5\u00c6")
        buf.write("\f\7\2\2\u00c6\u00c7\t\4\2\2\u00c7\u00cf\5&\24\2\u00c8")
        buf.write("\u00c9\f\6\2\2\u00c9\u00ca\t\5\2\2\u00ca\u00cf\5&\24\2")
        buf.write("\u00cb\u00cc\f\5\2\2\u00cc\u00cd\t\6\2\2\u00cd\u00cf\5")
        buf.write("&\24\2\u00ce\u00bf\3\2\2\2\u00ce\u00c2\3\2\2\2\u00ce\u00c5")
        buf.write("\3\2\2\2\u00ce\u00c8\3\2\2\2\u00ce\u00cb\3\2\2\2\u00cf")
        buf.write("\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2")
        buf.write("\u00d1%\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d7\7\26\2")
        buf.write("\2\u00d4\u00d8\5D#\2\u00d5\u00d6\7,\2\2\u00d6\u00d8\7")
        buf.write("\26\2\2\u00d7\u00d4\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7")
        buf.write("\u00d8\3\2\2\2\u00d8\u00de\3\2\2\2\u00d9\u00da\7/\2\2")
        buf.write("\u00da\u00db\5$\23\2\u00db\u00dc\7\60\2\2\u00dc\u00de")
        buf.write("\3\2\2\2\u00dd\u00d3\3\2\2\2\u00dd\u00d9\3\2\2\2\u00de")
        buf.write("\'\3\2\2\2\u00df\u00e7\5.\30\2\u00e0\u00e7\5\62\32\2\u00e1")
        buf.write("\u00e7\5\64\33\2\u00e2\u00e7\5<\37\2\u00e3\u00e7\5> \2")
        buf.write("\u00e4\u00e7\5@!\2\u00e5\u00e7\5*\26\2\u00e6\u00df\3\2")
        buf.write("\2\2\u00e6\u00e0\3\2\2\2\u00e6\u00e1\3\2\2\2\u00e6\u00e2")
        buf.write("\3\2\2\2\u00e6\u00e3\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6")
        buf.write("\u00e5\3\2\2\2\u00e7)\3\2\2\2\u00e8\u00e9\7\26\2\2\u00e9")
        buf.write("\u00ea\7&\2\2\u00ea\u00eb\5D#\2\u00eb\u00ec\t\7\2\2\u00ec")
        buf.write("\u00ed\5,\27\2\u00ed+\3\2\2\2\u00ee\u00ef\7\61\2\2\u00ef")
        buf.write("\u00f4\5,\27\2\u00f0\u00f1\7\65\2\2\u00f1\u00f3\5,\27")
        buf.write("\2\u00f2\u00f0\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2")
        buf.write("\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7\3\2\2\2\u00f6")
        buf.write("\u00f4\3\2\2\2\u00f7\u00f8\7\62\2\2\u00f8\u0105\3\2\2")
        buf.write("\2\u00f9\u00fa\7\61\2\2\u00fa\u00ff\5$\23\2\u00fb\u00fc")
        buf.write("\7\65\2\2\u00fc\u00fe\5$\23\2\u00fd\u00fb\3\2\2\2\u00fe")
        buf.write("\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2")
        buf.write("\u0100\u0102\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u0103\7")
        buf.write("\62\2\2\u0103\u0105\3\2\2\2\u0104\u00ee\3\2\2\2\u0104")
        buf.write("\u00f9\3\2\2\2\u0105-\3\2\2\2\u0106\u010a\7\26\2\2\u0107")
        buf.write("\u010b\5D#\2\u0108\u0109\7,\2\2\u0109\u010b\7\26\2\2\u010a")
        buf.write("\u0107\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2")
        buf.write("\u010b\u010c\3\2\2\2\u010c\u010d\5\60\31\2\u010d\u010e")
        buf.write("\5$\23\2\u010e\u010f\7\66\2\2\u010f/\3\2\2\2\u0110\u0111")
        buf.write("\t\b\2\2\u0111\61\3\2\2\2\u0112\u0113\7\3\2\2\u0113\u0114")
        buf.write("\7/\2\2\u0114\u0115\5$\23\2\u0115\u0116\7\60\2\2\u0116")
        buf.write("\u0120\5B\"\2\u0117\u0118\7\4\2\2\u0118\u0119\7\3\2\2")
        buf.write("\u0119\u011a\7/\2\2\u011a\u011b\5$\23\2\u011b\u011c\7")
        buf.write("\60\2\2\u011c\u011d\5B\"\2\u011d\u011f\3\2\2\2\u011e\u0117")
        buf.write("\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0120")
        buf.write("\u0121\3\2\2\2\u0121\u0125\3\2\2\2\u0122\u0120\3\2\2\2")
        buf.write("\u0123\u0124\7\4\2\2\u0124\u0126\5B\"\2\u0125\u0123\3")
        buf.write("\2\2\2\u0125\u0126\3\2\2\2\u0126\63\3\2\2\2\u0127\u013a")
        buf.write("\7\5\2\2\u0128\u0129\5\66\34\2\u0129\u012a\7\66\2\2\u012a")
        buf.write("\u012c\3\2\2\2\u012b\u0128\3\2\2\2\u012b\u012c\3\2\2\2")
        buf.write("\u012c\u012d\3\2\2\2\u012d\u0132\58\35\2\u012e\u012f\7")
        buf.write("\66\2\2\u012f\u0130\5:\36\2\u0130\u0131\5B\"\2\u0131\u0133")
        buf.write("\3\2\2\2\u0132\u012e\3\2\2\2\u0132\u0133\3\2\2\2\u0133")
        buf.write("\u013b\3\2\2\2\u0134\u0135\t\t\2\2\u0135\u0136\7\65\2")
        buf.write("\2\u0136\u0137\7\26\2\2\u0137\u0138\7&\2\2\u0138\u0139")
        buf.write("\7\23\2\2\u0139\u013b\7\26\2\2\u013a\u012b\3\2\2\2\u013a")
        buf.write("\u0134\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\5B\"\2")
        buf.write("\u013d\65\3\2\2\2\u013e\u013f\7\26\2\2\u013f\u0140\7\66")
        buf.write("\2\2\u0140\u0141\5$\23\2\u0141\67\3\2\2\2\u0142\u0143")
        buf.write("\5$\23\2\u01439\3\2\2\2\u0144\u0145\7\26\2\2\u0145\u0146")
        buf.write("\5\60\31\2\u0146\u0147\5$\23\2\u0147;\3\2\2\2\u0148\u0149")
        buf.write("\7\22\2\2\u0149\u014a\7\66\2\2\u014a=\3\2\2\2\u014b\u014c")
        buf.write("\7\21\2\2\u014c\u014d\7\66\2\2\u014d?\3\2\2\2\u014e\u0151")
        buf.write("\7\26\2\2\u014f\u0150\7,\2\2\u0150\u0152\7\26\2\2\u0151")
        buf.write("\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0153\3\2\2\2")
        buf.write("\u0153\u015c\7/\2\2\u0154\u0159\5$\23\2\u0155\u0156\7")
        buf.write("\65\2\2\u0156\u0158\5$\23\2\u0157\u0155\3\2\2\2\u0158")
        buf.write("\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2")
        buf.write("\u015a\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015c\u0154\3")
        buf.write("\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f")
        buf.write("\7\60\2\2\u015f\u0160\7\66\2\2\u0160A\3\2\2\2\u0161\u0167")
        buf.write("\7\61\2\2\u0162\u0163\5(\25\2\u0163\u0164\7\66\2\2\u0164")
        buf.write("\u0166\3\2\2\2\u0165\u0162\3\2\2\2\u0166\u0169\3\2\2\2")
        buf.write("\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u016a\3")
        buf.write("\2\2\2\u0169\u0167\3\2\2\2\u016a\u016b\7\62\2\2\u016b")
        buf.write("C\3\2\2\2\u016c\u016d\7\63\2\2\u016d\u016e\7\67\2\2\u016e")
        buf.write("\u0170\7\64\2\2\u016f\u016c\3\2\2\2\u0170\u0171\3\2\2")
        buf.write("\2\u0171\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172E\3\2")
        buf.write("\2\2$IQW\\`dlpt\u0082\u008f\u00a1\u00ab\u00b3\u00bd\u00ce")
        buf.write("\u00d0\u00d7\u00dd\u00e6\u00f4\u00ff\u0104\u010a\u0120")
        buf.write("\u0125\u012b\u0132\u013a\u0151\u0159\u015c\u0167\u0171")
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
    RULE_parserRuleSpec = 2
    RULE_decl = 3
    RULE_varDecl = 4
    RULE_funcDecl = 5
    RULE_typeDecl = 6
    RULE_constDecl = 7
    RULE_typeDefinition = 8
    RULE_structDefinition = 9
    RULE_structFields = 10
    RULE_interfaceDefinition = 11
    RULE_interfaceFields = 12
    RULE_listParams = 13
    RULE_listIdentifier = 14
    RULE_funcParams = 15
    RULE_funcParam = 16
    RULE_expression = 17
    RULE_term = 18
    RULE_statement = 19
    RULE_arrayLiteral = 20
    RULE_arraysBlock = 21
    RULE_assignStatement = 22
    RULE_assignmentOperator = 23
    RULE_ifStatement = 24
    RULE_forStatement = 25
    RULE_initilization = 26
    RULE_forCondition = 27
    RULE_forUpdate = 28
    RULE_breakStatement = 29
    RULE_continueStatement = 30
    RULE_callStatement = 31
    RULE_block = 32
    RULE_arrayDims = 33

    ruleNames =  [ "program", "tYPE", "parserRuleSpec", "decl", "varDecl", 
                   "funcDecl", "typeDecl", "constDecl", "typeDefinition", 
                   "structDefinition", "structFields", "interfaceDefinition", 
                   "interfaceFields", "listParams", "listIdentifier", "funcParams", 
                   "funcParam", "expression", "term", "statement", "arrayLiteral", 
                   "arraysBlock", "assignStatement", "assignmentOperator", 
                   "ifStatement", "forStatement", "initilization", "forCondition", 
                   "forUpdate", "breakStatement", "continueStatement", "callStatement", 
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
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self.parserRuleSpec()
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                    break

            self.state = 73
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
            self.state = 75
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
        self.enterRule(localctx, 4, self.RULE_parserRuleSpec)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC, MiniGoParser.TYPE, MiniGoParser.CONST, MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.decl()
                pass
            elif token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.statement()
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.varDecl()
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.funcDecl()
                pass
            elif token in [MiniGoParser.TYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.typeDecl()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.constDecl()
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


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def tYPE(self):
            return self.getTypedRuleContext(MiniGoParser.TYPEContext,0)


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
        self.enterRule(localctx, 8, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(MiniGoParser.VAR)
            self.state = 88
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LSB:
                self.state = 89
                self.arrayDims()


            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 92
                self.tYPE()
                pass

            elif la_ == 2:
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.INTERGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0):
                    self.state = 93
                    self.tYPE()


                self.state = 96
                self.match(MiniGoParser.ASSIGNOP)
                self.state = 97
                self.expression(0)
                pass


            self.state = 100
            self.match(MiniGoParser.SEMI)
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


        def funcParams(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamsContext,0)


        def tYPE(self):
            return self.getTypedRuleContext(MiniGoParser.TYPEContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = MiniGoParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(MiniGoParser.FUNC)
            self.state = 103
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 104
            self.match(MiniGoParser.LP)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 105
                self.funcParams()


            self.state = 108
            self.match(MiniGoParser.RP)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.INTERGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0):
                self.state = 109
                self.tYPE()


            self.state = 112
            self.block()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 113
                self.match(MiniGoParser.SEMI)


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
        self.enterRule(localctx, 12, self.RULE_typeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(MiniGoParser.TYPE)
            self.state = 117
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 118
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


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_constDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDecl" ):
                return visitor.visitConstDecl(self)
            else:
                return visitor.visitChildren(self)




    def constDecl(self):

        localctx = MiniGoParser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(MiniGoParser.CONST)
            self.state = 121
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 122
            self.match(MiniGoParser.ASSIGNOP)
            self.state = 123
            self.expression(0)
            self.state = 124
            self.match(MiniGoParser.SEMI)
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
        self.enterRule(localctx, 16, self.RULE_typeDefinition)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.structDefinition()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
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

        def structFields(self):
            return self.getTypedRuleContext(MiniGoParser.StructFieldsContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDefinition" ):
                return visitor.visitStructDefinition(self)
            else:
                return visitor.visitChildren(self)




    def structDefinition(self):

        localctx = MiniGoParser.StructDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_structDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(MiniGoParser.STRUCT)
            self.state = 131
            self.match(MiniGoParser.LB)
            self.state = 132
            self.structFields()
            self.state = 133
            self.match(MiniGoParser.RB)
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def tYPE(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.TYPEContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.TYPEContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structFields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFields" ):
                return visitor.visitStructFields(self)
            else:
                return visitor.visitChildren(self)




    def structFields(self):

        localctx = MiniGoParser.StructFieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_structFields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 135
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 136
                self.tYPE()
                self.state = 137
                self.match(MiniGoParser.SEMI)
                self.state = 141 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.IDENTIFIER):
                    break

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

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDefinition" ):
                return visitor.visitInterfaceDefinition(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDefinition(self):

        localctx = MiniGoParser.InterfaceDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_interfaceDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(MiniGoParser.INTERFACE)
            self.state = 144
            self.match(MiniGoParser.LB)
            self.state = 145
            self.interfaceFields()
            self.state = 146
            self.match(MiniGoParser.RB)
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


        def tYPE(self):
            return self.getTypedRuleContext(MiniGoParser.TYPEContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceFields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceFields" ):
                return visitor.visitInterfaceFields(self)
            else:
                return visitor.visitChildren(self)




    def interfaceFields(self):

        localctx = MiniGoParser.InterfaceFieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_interfaceFields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 149
            self.listParams()
            self.state = 150
            self.tYPE()
            self.state = 151
            self.match(MiniGoParser.SEMI)
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
        self.enterRule(localctx, 26, self.RULE_listParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(MiniGoParser.LP)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 154
                self.listIdentifier()
                self.state = 155
                self.tYPE()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
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
        self.enterRule(localctx, 28, self.RULE_listIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 165
                self.match(MiniGoParser.COMMA)
                self.state = 166
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 30, self.RULE_funcParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.funcParam()
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 173
                self.match(MiniGoParser.COMMA)
                self.state = 174
                self.funcParam()
                self.state = 179
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
        self.enterRule(localctx, 32, self.RULE_funcParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 181
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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUBOP, MiniGoParser.NOTOP]:
                self.state = 184
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUBOP or _la==MiniGoParser.NOTOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 185
                self.term()
                pass
            elif token in [MiniGoParser.IDENTIFIER, MiniGoParser.LP]:
                self.state = 186
                self.term()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 204
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 189
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 190
                        self.match(MiniGoParser.OROP)
                        self.state = 191
                        self.term()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 192
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 193
                        self.match(MiniGoParser.ANDOP)
                        self.state = 194
                        self.term()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 195
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 196
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUALOP) | (1 << MiniGoParser.NOTEQUALOP) | (1 << MiniGoParser.LESSOP) | (1 << MiniGoParser.LESSEQUALOP) | (1 << MiniGoParser.GREATEROP) | (1 << MiniGoParser.GREATEREQUALOP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 197
                        self.term()
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 198
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 199
                        _la = self._input.LA(1)
                        if not(_la==MiniGoParser.ADDOP or _la==MiniGoParser.SUBOP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 200
                        self.term()
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 201
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 202
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULOP) | (1 << MiniGoParser.DIVOP) | (1 << MiniGoParser.MODOP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 203
                        self.term()
                        pass

             
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self.enterRule(localctx, 36, self.RULE_term)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 213
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 210
                    self.arrayDims()

                elif la_ == 2:
                    self.state = 211
                    self.match(MiniGoParser.DOT)
                    self.state = 212
                    self.match(MiniGoParser.IDENTIFIER)


                pass
            elif token in [MiniGoParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(MiniGoParser.LP)
                self.state = 216
                self.expression(0)
                self.state = 217
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


        def arrayLiteral(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_statement)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.assignStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.ifStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.forStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 224
                self.breakStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 225
                self.continueStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 226
                self.callStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 227
                self.arrayLiteral()
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
        self.enterRule(localctx, 40, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 231
            self.match(MiniGoParser.SHORTASSIGNOP)

            self.state = 232
            self.arrayDims()
            self.state = 233
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INTERFACE) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 234
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
        self.enterRule(localctx, 42, self.RULE_arraysBlock)
        self._la = 0 # Token type
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(MiniGoParser.LB)
                self.state = 237
                self.arraysBlock()
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 238
                    self.match(MiniGoParser.COMMA)
                    self.state = 239
                    self.arraysBlock()
                    self.state = 244
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 245
                self.match(MiniGoParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.match(MiniGoParser.LB)
                self.state = 248
                self.expression(0)
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 249
                    self.match(MiniGoParser.COMMA)
                    self.state = 250
                    self.expression(0)
                    self.state = 255
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 256
                self.match(MiniGoParser.RB)
                pass


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


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

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
        self.enterRule(localctx, 44, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LSB]:
                self.state = 261
                self.arrayDims()
                pass
            elif token in [MiniGoParser.DOT]:
                self.state = 262
                self.match(MiniGoParser.DOT)
                self.state = 263
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.SHORTASSIGNOP, MiniGoParser.INCASSIGNOP, MiniGoParser.DECASSIGNOP, MiniGoParser.MULASSIGNOP, MiniGoParser.DIVASSIGNOP, MiniGoParser.MODASSIGNOP]:
                pass
            else:
                pass
            self.state = 266
            self.assignmentOperator()
            self.state = 267
            self.expression(0)
            self.state = 268
            self.match(MiniGoParser.SEMI)
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
        self.enterRule(localctx, 46, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
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
        self.enterRule(localctx, 48, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(MiniGoParser.IF)
            self.state = 273
            self.match(MiniGoParser.LP)
            self.state = 274
            self.expression(0)
            self.state = 275
            self.match(MiniGoParser.RP)
            self.state = 276
            self.block()
            self.state = 286
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 277
                    self.match(MiniGoParser.ELSE)
                    self.state = 278
                    self.match(MiniGoParser.IF)
                    self.state = 279
                    self.match(MiniGoParser.LP)
                    self.state = 280
                    self.expression(0)
                    self.state = 281
                    self.match(MiniGoParser.RP)
                    self.state = 282
                    self.block() 
                self.state = 288
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 289
                self.match(MiniGoParser.ELSE)
                self.state = 290
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

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def forCondition(self):
            return self.getTypedRuleContext(MiniGoParser.ForConditionContext,0)


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
            return MiniGoParser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = MiniGoParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(MiniGoParser.FOR)
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 297
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 294
                    self.initilization()
                    self.state = 295
                    self.match(MiniGoParser.SEMI)


                self.state = 299
                self.forCondition()
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.SEMI:
                    self.state = 300
                    self.match(MiniGoParser.SEMI)
                    self.state = 301
                    self.forUpdate()
                    self.state = 302
                    self.block()


                pass

            elif la_ == 2:
                self.state = 306
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.IDENTIFIER or _la==MiniGoParser.BLANK):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 307
                self.match(MiniGoParser.COMMA)
                self.state = 308
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 309
                self.match(MiniGoParser.SHORTASSIGNOP)
                self.state = 310
                self.match(MiniGoParser.RANGE)
                self.state = 311
                self.match(MiniGoParser.IDENTIFIER)
                pass


            self.state = 314
            self.block()
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

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

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
        self.enterRule(localctx, 52, self.RULE_initilization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 317
            self.match(MiniGoParser.SEMI)
            self.state = 318
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
        self.enterRule(localctx, 54, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
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
        self.enterRule(localctx, 56, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 323
            self.assignmentOperator()
            self.state = 324
            self.expression(0)
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

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = MiniGoParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(MiniGoParser.BREAK)
            self.state = 327
            self.match(MiniGoParser.SEMI)
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

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continueStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = MiniGoParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(MiniGoParser.CONTINUE)
            self.state = 330
            self.match(MiniGoParser.SEMI)
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

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

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
        self.enterRule(localctx, 62, self.RULE_callStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.DOT:
                self.state = 333
                self.match(MiniGoParser.DOT)
                self.state = 334
                self.match(MiniGoParser.IDENTIFIER)


            self.state = 337
            self.match(MiniGoParser.LP)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.SUBOP) | (1 << MiniGoParser.NOTOP) | (1 << MiniGoParser.LP))) != 0):
                self.state = 338
                self.expression(0)
                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 339
                    self.match(MiniGoParser.COMMA)
                    self.state = 340
                    self.expression(0)
                    self.state = 345
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 348
            self.match(MiniGoParser.RP)
            self.state = 349
            self.match(MiniGoParser.SEMI)
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


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(MiniGoParser.LB)
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 352
                self.statement()
                self.state = 353
                self.match(MiniGoParser.SEMI)
                self.state = 359
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 360
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
        self.enterRule(localctx, 66, self.RULE_arrayDims)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 362
                    self.match(MiniGoParser.LSB)
                    self.state = 363
                    self.match(MiniGoParser.INTLIT)
                    self.state = 364
                    self.match(MiniGoParser.RSB)

                else:
                    raise NoViableAltException(self)
                self.state = 367 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        self._predicates[17] = self.expression_sempred
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
         




