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
        buf.write("\u01d5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\7\2V\n\2\f\2\16\2Y\13")
        buf.write("\2\3\2\5\2\\\n\2\3\2\7\2_\n\2\f\2\16\2b\13\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\5\4p\n\4\3\5\3")
        buf.write("\5\3\6\3\6\5\6v\n\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\5\b\u0081\n\b\3\t\3\t\3\t\3\t\7\t\u0087\n\t\f\t\16")
        buf.write("\t\u008a\13\t\3\t\5\t\u008d\n\t\3\t\3\t\5\t\u0091\n\t")
        buf.write("\3\t\3\t\5\t\u0095\n\t\3\t\3\t\3\n\3\n\3\n\3\n\5\n\u009d")
        buf.write("\n\n\3\n\3\n\5\n\u00a1\n\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u00aa\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00ba\n\r\3\r\3\r\5\r\u00be")
        buf.write("\n\r\3\r\3\r\3\r\3\16\3\16\3\16\7\16\u00c6\n\16\f\16\16")
        buf.write("\16\u00c9\13\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\7\21\u00dc")
        buf.write("\n\21\f\21\16\21\u00df\13\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\7\22\u00e6\n\22\f\22\16\22\u00e9\13\22\3\23\3\23\3\23")
        buf.write("\5\23\u00ee\n\23\3\23\3\23\3\24\3\24\3\24\7\24\u00f5\n")
        buf.write("\24\f\24\16\24\u00f8\13\24\3\25\3\25\3\25\3\26\3\26\3")
        buf.write("\26\3\26\5\26\u0101\n\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0112")
        buf.write("\n\26\f\26\16\26\u0115\13\26\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u011b\n\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0124")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u0130\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3")
        buf.write("\32\3\32\3\32\7\32\u013c\n\32\f\32\16\32\u013f\13\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\7\32\u0147\n\32\f\32\16\32")
        buf.write("\u014a\13\32\3\32\3\32\5\32\u014e\n\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\5\33\u0156\n\33\7\33\u0158\n\33\f\33\16")
        buf.write("\33\u015b\13\33\3\33\3\33\3\34\3\34\3\34\3\34\5\34\u0163")
        buf.write("\n\34\3\34\3\34\3\34\5\34\u0168\n\34\3\34\3\34\3\35\3")
        buf.write("\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\7\36\u017a\n\36\f\36\16\36\u017d\13\36\3\36")
        buf.write("\3\36\5\36\u0181\n\36\3\36\3\36\3\37\3\37\3\37\5\37\u0188")
        buf.write("\n\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \5 \u0193\n \3!\3")
        buf.write("!\3!\3!\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3&\3&\3&\3\'\3\'\3\'\5\'\u01af\n\'\3\'\3\'\3\'\3")
        buf.write("\'\7\'\u01b5\n\'\f\'\16\'\u01b8\13\'\5\'\u01ba\n\'\3\'")
        buf.write("\3\'\3\'\3(\3(\5(\u01c1\n(\3(\3(\3)\3)\7)\u01c7\n)\f)")
        buf.write("\16)\u01ca\13)\3)\3)\3*\3*\3*\6*\u01d1\n*\r*\16*\u01d2")
        buf.write("\3*\2\3*+\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&")
        buf.write("(*,.\60\62\64\668:<>@BDFHJLNPR\2\13\3\2\f\17\4\3\66\66")
        buf.write("@@\4\2\33\33\'\'\3\2\37$\3\2\32\33\3\2\34\36\4\2\13\f")
        buf.write("\16\17\4\2\31\31(,\4\2..88\2\u01ea\2W\3\2\2\2\4e\3\2\2")
        buf.write("\2\6o\3\2\2\2\bq\3\2\2\2\nu\3\2\2\2\fy\3\2\2\2\16\u0080")
        buf.write("\3\2\2\2\20\u0082\3\2\2\2\22\u0098\3\2\2\2\24\u00a5\3")
        buf.write("\2\2\2\26\u00ab\3\2\2\2\30\u00b1\3\2\2\2\32\u00c2\3\2")
        buf.write("\2\2\34\u00cd\3\2\2\2\36\u00d1\3\2\2\2 \u00d7\3\2\2\2")
        buf.write("\"\u00e2\3\2\2\2$\u00ea\3\2\2\2&\u00f1\3\2\2\2(\u00f9")
        buf.write("\3\2\2\2*\u0100\3\2\2\2,\u0123\3\2\2\2.\u012f\3\2\2\2")
        buf.write("\60\u0131\3\2\2\2\62\u014d\3\2\2\2\64\u014f\3\2\2\2\66")
        buf.write("\u015e\3\2\2\28\u016b\3\2\2\2:\u016d\3\2\2\2<\u0184\3")
        buf.write("\2\2\2>\u0192\3\2\2\2@\u0194\3\2\2\2B\u0198\3\2\2\2D\u019a")
        buf.write("\3\2\2\2F\u019e\3\2\2\2H\u01a5\3\2\2\2J\u01a8\3\2\2\2")
        buf.write("L\u01ab\3\2\2\2N\u01be\3\2\2\2P\u01c4\3\2\2\2R\u01d0\3")
        buf.write("\2\2\2TV\5\16\b\2UT\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2")
        buf.write("\2\2X[\3\2\2\2YW\3\2\2\2Z\\\5\4\3\2[Z\3\2\2\2[\\\3\2\2")
        buf.write("\2\\`\3\2\2\2]_\5\16\b\2^]\3\2\2\2_b\3\2\2\2`^\3\2\2\2")
        buf.write("`a\3\2\2\2ac\3\2\2\2b`\3\2\2\2cd\7\2\2\3d\3\3\2\2\2ef")
        buf.write("\7\b\2\2fg\7\3\2\2gh\7/\2\2hi\7\60\2\2ij\5P)\2jk\b\3\1")
        buf.write("\2k\5\3\2\2\2lp\5\b\5\2mp\5\n\6\2np\78\2\2ol\3\2\2\2o")
        buf.write("m\3\2\2\2on\3\2\2\2p\7\3\2\2\2qr\t\2\2\2r\t\3\2\2\2sv")
        buf.write("\5\b\5\2tv\78\2\2us\3\2\2\2ut\3\2\2\2vw\3\2\2\2wx\5R*")
        buf.write("\2x\13\3\2\2\2yz\t\3\2\2z\r\3\2\2\2{\u0081\5\20\t\2|\u0081")
        buf.write("\5\22\n\2}\u0081\5\24\13\2~\u0081\5\26\f\2\177\u0081\5")
        buf.write("\30\r\2\u0080{\3\2\2\2\u0080|\3\2\2\2\u0080}\3\2\2\2\u0080")
        buf.write("~\3\2\2\2\u0080\177\3\2\2\2\u0081\17\3\2\2\2\u0082\u0083")
        buf.write("\7\24\2\2\u0083\u0088\78\2\2\u0084\u0085\7\65\2\2\u0085")
        buf.write("\u0087\78\2\2\u0086\u0084\3\2\2\2\u0087\u008a\3\2\2\2")
        buf.write("\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008c\3")
        buf.write("\2\2\2\u008a\u0088\3\2\2\2\u008b\u008d\5R*\2\u008c\u008b")
        buf.write("\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u0094\3\2\2\2\u008e")
        buf.write("\u0095\5\6\4\2\u008f\u0091\5\6\4\2\u0090\u008f\3\2\2\2")
        buf.write("\u0090\u0091\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\7")
        buf.write("\30\2\2\u0093\u0095\5*\26\2\u0094\u008e\3\2\2\2\u0094")
        buf.write("\u0090\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\5\f\7\2")
        buf.write("\u0097\21\3\2\2\2\u0098\u0099\7\b\2\2\u0099\u009a\78\2")
        buf.write("\2\u009a\u009c\7/\2\2\u009b\u009d\5&\24\2\u009c\u009b")
        buf.write("\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\u00a0\7\60\2\2\u009f\u00a1\5\6\4\2\u00a0\u009f\3\2\2")
        buf.write("\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3")
        buf.write("\5P)\2\u00a3\u00a4\5\f\7\2\u00a4\23\3\2\2\2\u00a5\u00a6")
        buf.write("\7\t\2\2\u00a6\u00a9\78\2\2\u00a7\u00aa\5\32\16\2\u00a8")
        buf.write("\u00aa\5\36\20\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8\3\2\2")
        buf.write("\2\u00aa\25\3\2\2\2\u00ab\u00ac\7\23\2\2\u00ac\u00ad\7")
        buf.write("8\2\2\u00ad\u00ae\7\30\2\2\u00ae\u00af\5*\26\2\u00af\u00b0")
        buf.write("\5\f\7\2\u00b0\27\3\2\2\2\u00b1\u00b2\7\b\2\2\u00b2\u00b3")
        buf.write("\7/\2\2\u00b3\u00b4\78\2\2\u00b4\u00b5\78\2\2\u00b5\u00b6")
        buf.write("\7\60\2\2\u00b6\u00b7\78\2\2\u00b7\u00b9\7/\2\2\u00b8")
        buf.write("\u00ba\5&\24\2\u00b9\u00b8\3\2\2\2\u00b9\u00ba\3\2\2\2")
        buf.write("\u00ba\u00bb\3\2\2\2\u00bb\u00bd\7\60\2\2\u00bc\u00be")
        buf.write("\5\6\4\2\u00bd\u00bc\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00bf\3\2\2\2\u00bf\u00c0\5P)\2\u00c0\u00c1\5\f\7\2\u00c1")
        buf.write("\31\3\2\2\2\u00c2\u00c3\7\n\2\2\u00c3\u00c7\7\61\2\2\u00c4")
        buf.write("\u00c6\5\34\17\2\u00c5\u00c4\3\2\2\2\u00c6\u00c9\3\2\2")
        buf.write("\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00ca")
        buf.write("\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cb\7\62\2\2\u00cb")
        buf.write("\u00cc\5\f\7\2\u00cc\33\3\2\2\2\u00cd\u00ce\78\2\2\u00ce")
        buf.write("\u00cf\5\6\4\2\u00cf\u00d0\5\f\7\2\u00d0\35\3\2\2\2\u00d1")
        buf.write("\u00d2\7\13\2\2\u00d2\u00d3\7\61\2\2\u00d3\u00d4\5$\23")
        buf.write("\2\u00d4\u00d5\7\62\2\2\u00d5\u00d6\5\f\7\2\u00d6\37\3")
        buf.write("\2\2\2\u00d7\u00dd\7/\2\2\u00d8\u00d9\5\"\22\2\u00d9\u00da")
        buf.write("\5\6\4\2\u00da\u00dc\3\2\2\2\u00db\u00d8\3\2\2\2\u00dc")
        buf.write("\u00df\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2")
        buf.write("\u00de\u00e0\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e1\7")
        buf.write("\60\2\2\u00e1!\3\2\2\2\u00e2\u00e7\78\2\2\u00e3\u00e4")
        buf.write("\7\65\2\2\u00e4\u00e6\78\2\2\u00e5\u00e3\3\2\2\2\u00e6")
        buf.write("\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8#\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00eb\78\2\2")
        buf.write("\u00eb\u00ed\5 \21\2\u00ec\u00ee\5\6\4\2\u00ed\u00ec\3")
        buf.write("\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0")
        buf.write("\5\f\7\2\u00f0%\3\2\2\2\u00f1\u00f6\5(\25\2\u00f2\u00f3")
        buf.write("\7\65\2\2\u00f3\u00f5\5(\25\2\u00f4\u00f2\3\2\2\2\u00f5")
        buf.write("\u00f8\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2")
        buf.write("\u00f7\'\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f9\u00fa\78\2")
        buf.write("\2\u00fa\u00fb\5\6\4\2\u00fb)\3\2\2\2\u00fc\u00fd\b\26")
        buf.write("\1\2\u00fd\u00fe\t\4\2\2\u00fe\u0101\5,\27\2\u00ff\u0101")
        buf.write("\5,\27\2\u0100\u00fc\3\2\2\2\u0100\u00ff\3\2\2\2\u0101")
        buf.write("\u0113\3\2\2\2\u0102\u0103\f\t\2\2\u0103\u0104\7&\2\2")
        buf.write("\u0104\u0112\5,\27\2\u0105\u0106\f\b\2\2\u0106\u0107\7")
        buf.write("%\2\2\u0107\u0112\5,\27\2\u0108\u0109\f\7\2\2\u0109\u010a")
        buf.write("\t\5\2\2\u010a\u0112\5,\27\2\u010b\u010c\f\6\2\2\u010c")
        buf.write("\u010d\t\6\2\2\u010d\u0112\5,\27\2\u010e\u010f\f\5\2\2")
        buf.write("\u010f\u0110\t\7\2\2\u0110\u0112\5,\27\2\u0111\u0102\3")
        buf.write("\2\2\2\u0111\u0105\3\2\2\2\u0111\u0108\3\2\2\2\u0111\u010b")
        buf.write("\3\2\2\2\u0111\u010e\3\2\2\2\u0112\u0115\3\2\2\2\u0113")
        buf.write("\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114+\3\2\2\2\u0115")
        buf.write("\u0113\3\2\2\2\u0116\u011a\78\2\2\u0117\u011b\5R*\2\u0118")
        buf.write("\u0119\7-\2\2\u0119\u011b\78\2\2\u011a\u0117\3\2\2\2\u011a")
        buf.write("\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u0124\3\2\2\2")
        buf.write("\u011c\u0124\79\2\2\u011d\u0124\7:\2\2\u011e\u0124\7;")
        buf.write("\2\2\u011f\u0120\7/\2\2\u0120\u0121\5*\26\2\u0121\u0122")
        buf.write("\7\60\2\2\u0122\u0124\3\2\2\2\u0123\u0116\3\2\2\2\u0123")
        buf.write("\u011c\3\2\2\2\u0123\u011d\3\2\2\2\u0123\u011e\3\2\2\2")
        buf.write("\u0123\u011f\3\2\2\2\u0124-\3\2\2\2\u0125\u0130\5\66\34")
        buf.write("\2\u0126\u0130\5:\36\2\u0127\u0130\5<\37\2\u0128\u0130")
        buf.write("\5H%\2\u0129\u0130\5J&\2\u012a\u0130\5L\'\2\u012b\u0130")
        buf.write("\5N(\2\u012c\u0130\5\60\31\2\u012d\u0130\5\20\t\2\u012e")
        buf.write("\u0130\5\26\f\2\u012f\u0125\3\2\2\2\u012f\u0126\3\2\2")
        buf.write("\2\u012f\u0127\3\2\2\2\u012f\u0128\3\2\2\2\u012f\u0129")
        buf.write("\3\2\2\2\u012f\u012a\3\2\2\2\u012f\u012b\3\2\2\2\u012f")
        buf.write("\u012c\3\2\2\2\u012f\u012d\3\2\2\2\u012f\u012e\3\2\2\2")
        buf.write("\u0130/\3\2\2\2\u0131\u0132\78\2\2\u0132\u0133\7\31\2")
        buf.write("\2\u0133\u0134\5R*\2\u0134\u0135\t\b\2\2\u0135\u0136\5")
        buf.write("\62\32\2\u0136\61\3\2\2\2\u0137\u0138\7\61\2\2\u0138\u013d")
        buf.write("\5\62\32\2\u0139\u013a\7\65\2\2\u013a\u013c\5\62\32\2")
        buf.write("\u013b\u0139\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3")
        buf.write("\2\2\2\u013d\u013e\3\2\2\2\u013e\u0140\3\2\2\2\u013f\u013d")
        buf.write("\3\2\2\2\u0140\u0141\7\62\2\2\u0141\u014e\3\2\2\2\u0142")
        buf.write("\u0143\7\61\2\2\u0143\u0148\5*\26\2\u0144\u0145\7\65\2")
        buf.write("\2\u0145\u0147\5*\26\2\u0146\u0144\3\2\2\2\u0147\u014a")
        buf.write("\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149")
        buf.write("\u014b\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014c\7\62\2")
        buf.write("\2\u014c\u014e\3\2\2\2\u014d\u0137\3\2\2\2\u014d\u0142")
        buf.write("\3\2\2\2\u014e\63\3\2\2\2\u014f\u0150\78\2\2\u0150\u0159")
        buf.write("\7\61\2\2\u0151\u0152\78\2\2\u0152\u0153\7\67\2\2\u0153")
        buf.write("\u0155\5*\26\2\u0154\u0156\7\65\2\2\u0155\u0154\3\2\2")
        buf.write("\2\u0155\u0156\3\2\2\2\u0156\u0158\3\2\2\2\u0157\u0151")
        buf.write("\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u0159")
        buf.write("\u015a\3\2\2\2\u015a\u015c\3\2\2\2\u015b\u0159\3\2\2\2")
        buf.write("\u015c\u015d\7\62\2\2\u015d\65\3\2\2\2\u015e\u0162\78")
        buf.write("\2\2\u015f\u0163\5R*\2\u0160\u0161\7-\2\2\u0161\u0163")
        buf.write("\78\2\2\u0162\u015f\3\2\2\2\u0162\u0160\3\2\2\2\u0162")
        buf.write("\u0163\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0167\58\35\2")
        buf.write("\u0165\u0168\5*\26\2\u0166\u0168\5\64\33\2\u0167\u0165")
        buf.write("\3\2\2\2\u0167\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169")
        buf.write("\u016a\5\f\7\2\u016a\67\3\2\2\2\u016b\u016c\t\t\2\2\u016c")
        buf.write("9\3\2\2\2\u016d\u016e\7\4\2\2\u016e\u016f\7/\2\2\u016f")
        buf.write("\u0170\5*\26\2\u0170\u0171\7\60\2\2\u0171\u017b\5P)\2")
        buf.write("\u0172\u0173\7\5\2\2\u0173\u0174\7\4\2\2\u0174\u0175\7")
        buf.write("/\2\2\u0175\u0176\5*\26\2\u0176\u0177\7\60\2\2\u0177\u0178")
        buf.write("\5P)\2\u0178\u017a\3\2\2\2\u0179\u0172\3\2\2\2\u017a\u017d")
        buf.write("\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c")
        buf.write("\u0180\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u017f\7\5\2\2")
        buf.write("\u017f\u0181\5P)\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2")
        buf.write("\2\2\u0181\u0182\3\2\2\2\u0182\u0183\5\f\7\2\u0183;\3")
        buf.write("\2\2\2\u0184\u0187\7\6\2\2\u0185\u0188\5> \2\u0186\u0188")
        buf.write("\5F$\2\u0187\u0185\3\2\2\2\u0187\u0186\3\2\2\2\u0188\u0189")
        buf.write("\3\2\2\2\u0189\u018a\5P)\2\u018a=\3\2\2\2\u018b\u0193")
        buf.write("\5B\"\2\u018c\u018d\5@!\2\u018d\u018e\7\66\2\2\u018e\u018f")
        buf.write("\5B\"\2\u018f\u0190\7\66\2\2\u0190\u0191\5D#\2\u0191\u0193")
        buf.write("\3\2\2\2\u0192\u018b\3\2\2\2\u0192\u018c\3\2\2\2\u0193")
        buf.write("?\3\2\2\2\u0194\u0195\78\2\2\u0195\u0196\7\31\2\2\u0196")
        buf.write("\u0197\5*\26\2\u0197A\3\2\2\2\u0198\u0199\5*\26\2\u0199")
        buf.write("C\3\2\2\2\u019a\u019b\78\2\2\u019b\u019c\58\35\2\u019c")
        buf.write("\u019d\5*\26\2\u019dE\3\2\2\2\u019e\u019f\t\n\2\2\u019f")
        buf.write("\u01a0\7\65\2\2\u01a0\u01a1\78\2\2\u01a1\u01a2\7\31\2")
        buf.write("\2\u01a2\u01a3\7\27\2\2\u01a3\u01a4\78\2\2\u01a4G\3\2")
        buf.write("\2\2\u01a5\u01a6\7\26\2\2\u01a6\u01a7\5\f\7\2\u01a7I\3")
        buf.write("\2\2\2\u01a8\u01a9\7\25\2\2\u01a9\u01aa\5\f\7\2\u01aa")
        buf.write("K\3\2\2\2\u01ab\u01ae\78\2\2\u01ac\u01ad\7-\2\2\u01ad")
        buf.write("\u01af\78\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2")
        buf.write("\u01af\u01b0\3\2\2\2\u01b0\u01b9\7/\2\2\u01b1\u01b6\5")
        buf.write("*\26\2\u01b2\u01b3\7\65\2\2\u01b3\u01b5\5*\26\2\u01b4")
        buf.write("\u01b2\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2")
        buf.write("\u01b6\u01b7\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3")
        buf.write("\2\2\2\u01b9\u01b1\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bb")
        buf.write("\3\2\2\2\u01bb\u01bc\7\60\2\2\u01bc\u01bd\5\f\7\2\u01bd")
        buf.write("M\3\2\2\2\u01be\u01c0\7\7\2\2\u01bf\u01c1\5*\26\2\u01c0")
        buf.write("\u01bf\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2\3\2\2\2")
        buf.write("\u01c2\u01c3\5\f\7\2\u01c3O\3\2\2\2\u01c4\u01c8\7\61\2")
        buf.write("\2\u01c5\u01c7\5.\30\2\u01c6\u01c5\3\2\2\2\u01c7\u01ca")
        buf.write("\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9")
        buf.write("\u01cb\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cc\7\62\2")
        buf.write("\2\u01ccQ\3\2\2\2\u01cd\u01ce\7\63\2\2\u01ce\u01cf\79")
        buf.write("\2\2\u01cf\u01d1\7\64\2\2\u01d0\u01cd\3\2\2\2\u01d1\u01d2")
        buf.write("\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3")
        buf.write("S\3\2\2\2-W[`ou\u0080\u0088\u008c\u0090\u0094\u009c\u00a0")
        buf.write("\u00a9\u00b9\u00bd\u00c7\u00dd\u00e7\u00ed\u00f6\u0100")
        buf.write("\u0111\u0113\u011a\u0123\u012f\u013d\u0148\u014d\u0155")
        buf.write("\u0159\u0162\u0167\u017b\u0180\u0187\u0192\u01ae\u01b6")
        buf.write("\u01b9\u01c0\u01c8\u01d2")
        return buf.getvalue()


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
                     "<INVALID>", "<INVALID>", "'\n'" ]

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
                      "BOOL_LIT", "BLOCK_COMMENT", "LINE_COMMENT", "WS", 
                      "NEWLINE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_mainFunction = 1
    RULE_tYPE = 2
    RULE_baseType = 3
    RULE_arrayType = 4
    RULE_endOfStatement = 5
    RULE_declaration = 6
    RULE_varDecl = 7
    RULE_funcDecl = 8
    RULE_typeDecl = 9
    RULE_constDecl = 10
    RULE_methodDecl = 11
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

    ruleNames =  [ "program", "mainFunction", "tYPE", "baseType", "arrayType", 
                   "endOfStatement", "declaration", "varDecl", "funcDecl", 
                   "typeDecl", "constDecl", "methodDecl", "structDefinition", 
                   "structFields", "interfaceDefinition", "listParams", 
                   "listIdentifier", "interfaceFields", "funcParams", "funcParam", 
                   "expression", "term", "statement", "arrayLiteral", "arraysBlock", 
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
    BOOL_LIT=58
    BLOCK_COMMENT=59
    LINE_COMMENT=60
    WS=61
    NEWLINE=62
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

            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 88
                self.mainFunction()


            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0):
                self.state = 91
                self.declaration()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
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
            self.state = 99
            self.match(MiniGoParser.FUNC)
            self.state = 100
            self.match(MiniGoParser.T__0)
            self.state = 101
            self.match(MiniGoParser.LPAREN)
            self.state = 102
            self.match(MiniGoParser.RPAREN)
            self.state = 103
            self.block()
            print("main function")
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

        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

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
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.baseType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.arrayType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 108
                self.match(MiniGoParser.IDENTIFIER)
                pass


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

        def getRuleIndex(self):
            return MiniGoParser.RULE_baseType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseType" ):
                return visitor.visitBaseType(self)
            else:
                return visitor.visitChildren(self)




    def baseType(self):

        localctx = MiniGoParser.BaseTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
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


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = MiniGoParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN]:
                self.state = 113
                self.baseType()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.state = 114
                self.match(MiniGoParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 117
            self.arrayDims()
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
        self.enterRule(localctx, 10, self.RULE_endOfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            _la = self._input.LA(1)
            if not(((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.SEMI - -1)) | (1 << (MiniGoParser.NEWLINE - -1)))) != 0)):
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
        self.enterRule(localctx, 12, self.RULE_declaration)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.funcDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                self.typeDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 124
                self.constDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 125
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
        self.enterRule(localctx, 14, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(MiniGoParser.VAR)
            self.state = 129
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 130
                self.match(MiniGoParser.COMMA)
                self.state = 131
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 137
                self.arrayDims()


            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 140
                self.tYPE()
                pass

            elif la_ == 2:
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 141
                    self.tYPE()


                self.state = 144
                self.match(MiniGoParser.ASSIGN)
                self.state = 145
                self.expression(0)
                pass


            self.state = 148
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
        self.enterRule(localctx, 16, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(MiniGoParser.FUNC)
            self.state = 151
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 152
            self.match(MiniGoParser.LPAREN)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 153
                self.funcParams()


            self.state = 156
            self.match(MiniGoParser.RPAREN)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 157
                self.tYPE()


            self.state = 160
            self.block()
            self.state = 161
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

        def structDefinition(self):
            return self.getTypedRuleContext(MiniGoParser.StructDefinitionContext,0)


        def interfaceDefinition(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceDefinitionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typeDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDecl" ):
                return visitor.visitTypeDecl(self)
            else:
                return visitor.visitChildren(self)




    def typeDecl(self):

        localctx = MiniGoParser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_typeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(MiniGoParser.TYPE)
            self.state = 164
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.state = 165
                self.structDefinition()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 166
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
        self.enterRule(localctx, 20, self.RULE_constDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(MiniGoParser.CONST)
            self.state = 170
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 171
            self.match(MiniGoParser.ASSIGN)
            self.state = 172
            self.expression(0)
            self.state = 173
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
        self.enterRule(localctx, 22, self.RULE_methodDecl)
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
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 182
                self.funcParams()


            self.state = 185
            self.match(MiniGoParser.RPAREN)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 186
                self.tYPE()


            self.state = 189
            self.block()
            self.state = 190
            self.endOfStatement()
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
            self.state = 192
            self.match(MiniGoParser.STRUCT)
            self.state = 193
            self.match(MiniGoParser.LBRACE)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 194
                self.structFields()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 203
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 204
            self.tYPE()
            self.state = 205
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
            self.state = 207
            self.match(MiniGoParser.INTERFACE)
            self.state = 208
            self.match(MiniGoParser.LBRACE)
            self.state = 209
            self.interfaceFields()
            self.state = 210
            self.match(MiniGoParser.RBRACE)
            self.state = 211
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
            self.state = 213
            self.match(MiniGoParser.LPAREN)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 214
                self.listIdentifier()
                self.state = 215
                self.tYPE()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 222
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
            self.state = 224
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 225
                self.match(MiniGoParser.COMMA)
                self.state = 226
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 231
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
            self.state = 232
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 233
            self.listParams()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 234
                self.tYPE()


            self.state = 237
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
            self.state = 239
            self.funcParam()
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 240
                self.match(MiniGoParser.COMMA)
                self.state = 241
                self.funcParam()
                self.state = 246
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
            self.state = 247
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 248
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
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.state = 251
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 252
                self.term()
                pass
            elif token in [MiniGoParser.LPAREN, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 253
                self.term()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 271
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 256
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 257
                        self.match(MiniGoParser.OR)
                        self.state = 258
                        self.term()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 259
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 260
                        self.match(MiniGoParser.AND)
                        self.state = 261
                        self.term()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 262
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 263
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LEQ) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GEQ))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 264
                        self.term()
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 265
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 266
                        _la = self._input.LA(1)
                        if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 267
                        self.term()
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 268
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 269
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 270
                        self.term()
                        pass

             
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 280
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 277
                    self.arrayDims()

                elif la_ == 2:
                    self.state = 278
                    self.match(MiniGoParser.DOT)
                    self.state = 279
                    self.match(MiniGoParser.IDENTIFIER)


                pass
            elif token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 283
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 284
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.LPAREN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 285
                self.match(MiniGoParser.LPAREN)
                self.state = 286
                self.expression(0)
                self.state = 287
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
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 291
                self.assignStatement()
                pass

            elif la_ == 2:
                self.state = 292
                self.ifStatement()
                pass

            elif la_ == 3:
                self.state = 293
                self.forStatement()
                pass

            elif la_ == 4:
                self.state = 294
                self.breakStatement()
                pass

            elif la_ == 5:
                self.state = 295
                self.continueStatement()
                pass

            elif la_ == 6:
                self.state = 296
                self.callStatement()
                pass

            elif la_ == 7:
                self.state = 297
                self.returnStatement()
                pass

            elif la_ == 8:
                self.state = 298
                self.arrayLiteral()
                pass

            elif la_ == 9:
                self.state = 299
                self.varDecl()
                pass

            elif la_ == 10:
                self.state = 300
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
            self.state = 303
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 304
            self.match(MiniGoParser.DECLARE)

            self.state = 305
            self.arrayDims()
            self.state = 306
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INTERFACE) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 307
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
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(MiniGoParser.LBRACE)
                self.state = 310
                self.arraysBlock()
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 311
                    self.match(MiniGoParser.COMMA)
                    self.state = 312
                    self.arraysBlock()
                    self.state = 317
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 318
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.match(MiniGoParser.LBRACE)
                self.state = 321
                self.expression(0)
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 322
                    self.match(MiniGoParser.COMMA)
                    self.state = 323
                    self.expression(0)
                    self.state = 328
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 329
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
            self.state = 333
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 334
            self.match(MiniGoParser.LBRACE)
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 335
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 336
                self.match(MiniGoParser.COLON)
                self.state = 337
                self.expression(0)
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.COMMA:
                    self.state = 338
                    self.match(MiniGoParser.COMMA)


                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 346
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
            self.state = 348
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 352
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACKET]:
                self.state = 349
                self.arrayDims()
                pass
            elif token in [MiniGoParser.DOT]:
                self.state = 350
                self.match(MiniGoParser.DOT)
                self.state = 351
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.DECLARE, MiniGoParser.PLUS_ASSIGN, MiniGoParser.MINUS_ASSIGN, MiniGoParser.MUL_ASSIGN, MiniGoParser.DIV_ASSIGN, MiniGoParser.MOD_ASSIGN]:
                pass
            else:
                pass
            self.state = 354
            self.assignmentOperator()
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 355
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 356
                self.structExpression()
                pass


            self.state = 359
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
            self.state = 361
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
            self.state = 363
            self.match(MiniGoParser.IF)
            self.state = 364
            self.match(MiniGoParser.LPAREN)
            self.state = 365
            self.expression(0)
            self.state = 366
            self.match(MiniGoParser.RPAREN)
            self.state = 367
            self.block()
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 368
                    self.match(MiniGoParser.ELSE)
                    self.state = 369
                    self.match(MiniGoParser.IF)
                    self.state = 370
                    self.match(MiniGoParser.LPAREN)
                    self.state = 371
                    self.expression(0)
                    self.state = 372
                    self.match(MiniGoParser.RPAREN)
                    self.state = 373
                    self.block() 
                self.state = 379
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 380
                self.match(MiniGoParser.ELSE)
                self.state = 381
                self.block()


            self.state = 384
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
            self.state = 386
            self.match(MiniGoParser.FOR)
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 387
                self.forLoop()
                pass

            elif la_ == 2:
                self.state = 388
                self.forIteration()
                pass


            self.state = 391
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
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.forCondition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.initilization()
                self.state = 395
                self.match(MiniGoParser.SEMI)
                self.state = 396
                self.forCondition()
                self.state = 397
                self.match(MiniGoParser.SEMI)
                self.state = 398
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
            self.state = 402
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 403
            self.match(MiniGoParser.DECLARE)
            self.state = 404
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
            self.state = 406
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
            self.state = 408
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 409
            self.assignmentOperator()
            self.state = 410
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
            self.state = 412
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.BLANK or _la==MiniGoParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 413
            self.match(MiniGoParser.COMMA)
            self.state = 414
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 415
            self.match(MiniGoParser.DECLARE)
            self.state = 416
            self.match(MiniGoParser.RANGE)
            self.state = 417
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
            self.state = 419
            self.match(MiniGoParser.BREAK)
            self.state = 420
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
            self.state = 422
            self.match(MiniGoParser.CONTINUE)
            self.state = 423
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
            self.state = 425
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 428
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.DOT:
                self.state = 426
                self.match(MiniGoParser.DOT)
                self.state = 427
                self.match(MiniGoParser.IDENTIFIER)


            self.state = 430
            self.match(MiniGoParser.LPAREN)
            self.state = 439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 431
                self.expression(0)
                self.state = 436
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 432
                    self.match(MiniGoParser.COMMA)
                    self.state = 433
                    self.expression(0)
                    self.state = 438
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 441
            self.match(MiniGoParser.RPAREN)
            self.state = 442
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
            self.state = 444
            self.match(MiniGoParser.RETURN)
            self.state = 446
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 445
                self.expression(0)


            self.state = 448
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
            self.state = 450
            self.match(MiniGoParser.LBRACE)
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 451
                self.statement()
                self.state = 456
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 457
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
            self.state = 462 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 459
                    self.match(MiniGoParser.LBRACKET)
                    self.state = 460
                    self.match(MiniGoParser.INT_LIT)
                    self.state = 461
                    self.match(MiniGoParser.RBRACKET)

                else:
                    raise NoViableAltException(self)
                self.state = 464 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
         




