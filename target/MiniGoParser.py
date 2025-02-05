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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u0273\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\3\2\7\2l\n\2\f\2\16\2o\13\2\3\2\5\2r\n\2\3")
        buf.write("\2\7\2u\n\2\f\2\16\2x\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3\u0082\n\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\5\6\u008d\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0097")
        buf.write("\n\6\5\6\u0099\n\6\3\7\3\7\3\7\3\7\7\7\u009f\n\7\f\7\16")
        buf.write("\7\u00a2\13\7\3\7\5\7\u00a5\n\7\3\7\3\7\5\7\u00a9\n\7")
        buf.write("\3\7\3\7\5\7\u00ad\n\7\3\b\3\b\3\b\3\b\5\b\u00b3\n\b\3")
        buf.write("\b\3\b\5\b\u00b7\n\b\3\b\5\b\u00ba\n\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\5\t\u00c2\n\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\5\13\u00d1\n\13\3\13\3\13")
        buf.write("\5\13\u00d5\n\13\3\13\3\13\3\f\3\f\3\f\7\f\u00dc\n\f\f")
        buf.write("\f\16\f\u00df\13\f\3\f\3\f\3\r\3\r\5\r\u00e5\n\r\3\r\3")
        buf.write("\r\5\r\u00e9\n\r\3\r\3\r\3\16\3\16\3\16\7\16\u00f0\n\16")
        buf.write("\f\16\16\16\u00f3\13\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\7\17\u00fb\n\17\f\17\16\17\u00fe\13\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\7\20\u0105\n\20\f\20\16\20\u0108\13\20\3\21")
        buf.write("\3\21\3\21\5\21\u010d\n\21\3\21\3\21\3\22\3\22\3\22\7")
        buf.write("\22\u0114\n\22\f\22\16\22\u0117\13\22\3\23\3\23\5\23\u011b")
        buf.write("\n\23\3\23\3\23\3\24\3\24\3\25\3\25\3\25\7\25\u0124\n")
        buf.write("\25\f\25\16\25\u0127\13\25\3\26\3\26\3\26\7\26\u012c\n")
        buf.write("\26\f\26\16\26\u012f\13\26\3\27\3\27\3\27\7\27\u0134\n")
        buf.write("\27\f\27\16\27\u0137\13\27\3\30\3\30\3\30\7\30\u013c\n")
        buf.write("\30\f\30\16\30\u013f\13\30\3\31\3\31\3\31\7\31\u0144\n")
        buf.write("\31\f\31\16\31\u0147\13\31\3\32\3\32\3\32\5\32\u014c\n")
        buf.write("\32\3\33\3\33\3\33\3\33\3\33\5\33\u0153\n\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\5\34\u015a\n\34\3\34\7\34\u015d\n\34\f")
        buf.write("\34\16\34\u0160\13\34\3\35\3\35\3\35\3\35\3\35\3\35\5")
        buf.write("\35\u0168\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\5\36\u0172\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0197\n\37\5\37\u0199")
        buf.write("\n\37\3 \3 \3 \3 \3!\3!\3!\3!\7!\u01a3\n!\f!\16!\u01a6")
        buf.write("\13!\3!\3!\3!\3!\3!\3!\7!\u01ae\n!\f!\16!\u01b1\13!\3")
        buf.write("!\3!\5!\u01b5\n!\3\"\3\"\3\"\3\"\3\"\7\"\u01bc\n\"\f\"")
        buf.write("\16\"\u01bf\13\"\3\"\5\"\u01c2\n\"\5\"\u01c4\n\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\3#\3#\5#\u01cf\n#\3#\3#\3#\3#\5#\u01d5")
        buf.write("\n#\3#\7#\u01d8\n#\f#\16#\u01db\13#\3#\5#\u01de\n#\5#")
        buf.write("\u01e0\n#\3#\3#\5#\u01e4\n#\3$\3$\3$\3$\3%\3%\3%\7%\u01ed")
        buf.write("\n%\f%\16%\u01f0\13%\3%\3%\3%\3%\7%\u01f6\n%\f%\16%\u01f9")
        buf.write("\13%\3&\3&\3&\7&\u01fe\n&\f&\16&\u0201\13&\3&\5&\u0204")
        buf.write("\n&\3\'\3\'\3\'\5\'\u0209\n\'\3(\3(\3)\3)\3)\3)\5)\u0211")
        buf.write("\n)\3)\3)\3)\3)\3)\5)\u0218\n)\7)\u021a\n)\f)\16)\u021d")
        buf.write("\13)\3)\3)\5)\u0221\n)\3*\3*\3*\5*\u0226\n*\3*\3*\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\5+\u0231\n+\3,\3,\3,\3,\3-\3-\3.\3.\3")
        buf.write(".\3.\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\62\5\62\u024b\n\62\3\62\3\62\3\62\3\62\7\62\u0251\n")
        buf.write("\62\f\62\16\62\u0254\13\62\5\62\u0256\n\62\3\62\3\62\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\63\5\63\u0260\n\63\3\64\3\64")
        buf.write("\7\64\u0264\n\64\f\64\16\64\u0267\13\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\65\6\65\u026f\n\65\r\65\16\65\u0270\3\65")
        buf.write("\2\2\66\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(",.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh\2\n\4\2\f\17")
        buf.write("88\4\3\66\66??\3\2\37$\3\2\32\33\3\2\34\36\4\2\33\33\'")
        buf.write("\'\4\2\31\31(,\4\2..88\2\u0299\2m\3\2\2\2\4{\3\2\2\2\6")
        buf.write("\u0083\3\2\2\2\b\u0085\3\2\2\2\n\u0098\3\2\2\2\f\u009a")
        buf.write("\3\2\2\2\16\u00ae\3\2\2\2\20\u00bd\3\2\2\2\22\u00c3\3")
        buf.write("\2\2\2\24\u00c8\3\2\2\2\26\u00d8\3\2\2\2\30\u00e2\3\2")
        buf.write("\2\2\32\u00ec\3\2\2\2\34\u00f6\3\2\2\2\36\u0101\3\2\2")
        buf.write("\2 \u0109\3\2\2\2\"\u0110\3\2\2\2$\u0118\3\2\2\2&\u011e")
        buf.write("\3\2\2\2(\u0120\3\2\2\2*\u0128\3\2\2\2,\u0130\3\2\2\2")
        buf.write(".\u0138\3\2\2\2\60\u0140\3\2\2\2\62\u014b\3\2\2\2\64\u0152")
        buf.write("\3\2\2\2\66\u0159\3\2\2\28\u0167\3\2\2\2:\u0171\3\2\2")
        buf.write("\2<\u0198\3\2\2\2>\u019a\3\2\2\2@\u01b4\3\2\2\2B\u01b6")
        buf.write("\3\2\2\2D\u01e3\3\2\2\2F\u01e5\3\2\2\2H\u01e9\3\2\2\2")
        buf.write("J\u01fa\3\2\2\2L\u0208\3\2\2\2N\u020a\3\2\2\2P\u020c\3")
        buf.write("\2\2\2R\u0222\3\2\2\2T\u0230\3\2\2\2V\u0232\3\2\2\2X\u0236")
        buf.write("\3\2\2\2Z\u0238\3\2\2\2\\\u023c\3\2\2\2^\u0243\3\2\2\2")
        buf.write("`\u0245\3\2\2\2b\u0247\3\2\2\2d\u0259\3\2\2\2f\u0261\3")
        buf.write("\2\2\2h\u026e\3\2\2\2jl\5\n\6\2kj\3\2\2\2lo\3\2\2\2mk")
        buf.write("\3\2\2\2mn\3\2\2\2nq\3\2\2\2om\3\2\2\2pr\5\4\3\2qp\3\2")
        buf.write("\2\2qr\3\2\2\2rv\3\2\2\2su\5\n\6\2ts\3\2\2\2ux\3\2\2\2")
        buf.write("vt\3\2\2\2vw\3\2\2\2wy\3\2\2\2xv\3\2\2\2yz\7\2\2\3z\3")
        buf.write("\3\2\2\2{|\7\b\2\2|}\7\3\2\2}~\7/\2\2~\177\7\60\2\2\177")
        buf.write("\u0081\5f\64\2\u0080\u0082\5\b\5\2\u0081\u0080\3\2\2\2")
        buf.write("\u0081\u0082\3\2\2\2\u0082\5\3\2\2\2\u0083\u0084\t\2\2")
        buf.write("\2\u0084\7\3\2\2\2\u0085\u0086\t\3\2\2\u0086\t\3\2\2\2")
        buf.write("\u0087\u0088\5\f\7\2\u0088\u0089\5\b\5\2\u0089\u0099\3")
        buf.write("\2\2\2\u008a\u008c\5\16\b\2\u008b\u008d\5\b\5\2\u008c")
        buf.write("\u008b\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u0099\3\2\2\2")
        buf.write("\u008e\u008f\5\20\t\2\u008f\u0090\5\b\5\2\u0090\u0099")
        buf.write("\3\2\2\2\u0091\u0092\5\22\n\2\u0092\u0093\5\b\5\2\u0093")
        buf.write("\u0099\3\2\2\2\u0094\u0096\5\24\13\2\u0095\u0097\5\b\5")
        buf.write("\2\u0096\u0095\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0099")
        buf.write("\3\2\2\2\u0098\u0087\3\2\2\2\u0098\u008a\3\2\2\2\u0098")
        buf.write("\u008e\3\2\2\2\u0098\u0091\3\2\2\2\u0098\u0094\3\2\2\2")
        buf.write("\u0099\13\3\2\2\2\u009a\u009b\7\24\2\2\u009b\u00a0\78")
        buf.write("\2\2\u009c\u009d\7\65\2\2\u009d\u009f\78\2\2\u009e\u009c")
        buf.write("\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0")
        buf.write("\u00a1\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2")
        buf.write("\u00a3\u00a5\5h\65\2\u00a4\u00a3\3\2\2\2\u00a4\u00a5\3")
        buf.write("\2\2\2\u00a5\u00ac\3\2\2\2\u00a6\u00ad\5\6\4\2\u00a7\u00a9")
        buf.write("\5\6\4\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9")
        buf.write("\u00aa\3\2\2\2\u00aa\u00ab\7\30\2\2\u00ab\u00ad\5&\24")
        buf.write("\2\u00ac\u00a6\3\2\2\2\u00ac\u00a8\3\2\2\2\u00ad\r\3\2")
        buf.write("\2\2\u00ae\u00af\7\b\2\2\u00af\u00b0\78\2\2\u00b0\u00b2")
        buf.write("\7/\2\2\u00b1\u00b3\5\"\22\2\u00b2\u00b1\3\2\2\2\u00b2")
        buf.write("\u00b3\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b9\7\60\2")
        buf.write("\2\u00b5\u00b7\5h\65\2\u00b6\u00b5\3\2\2\2\u00b6\u00b7")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba\5\6\4\2\u00b9")
        buf.write("\u00b6\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\3\2\2\2")
        buf.write("\u00bb\u00bc\5f\64\2\u00bc\17\3\2\2\2\u00bd\u00be\7\t")
        buf.write("\2\2\u00be\u00c1\78\2\2\u00bf\u00c2\5\26\f\2\u00c0\u00c2")
        buf.write("\5\32\16\2\u00c1\u00bf\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2")
        buf.write("\21\3\2\2\2\u00c3\u00c4\7\23\2\2\u00c4\u00c5\78\2\2\u00c5")
        buf.write("\u00c6\7\30\2\2\u00c6\u00c7\5&\24\2\u00c7\23\3\2\2\2\u00c8")
        buf.write("\u00c9\7\b\2\2\u00c9\u00ca\7/\2\2\u00ca\u00cb\78\2\2\u00cb")
        buf.write("\u00cc\78\2\2\u00cc\u00cd\7\60\2\2\u00cd\u00ce\78\2\2")
        buf.write("\u00ce\u00d0\7/\2\2\u00cf\u00d1\5\"\22\2\u00d0\u00cf\3")
        buf.write("\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d4")
        buf.write("\7\60\2\2\u00d3\u00d5\5\6\4\2\u00d4\u00d3\3\2\2\2\u00d4")
        buf.write("\u00d5\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7\5f\64\2")
        buf.write("\u00d7\25\3\2\2\2\u00d8\u00d9\7\n\2\2\u00d9\u00dd\7\61")
        buf.write("\2\2\u00da\u00dc\5\30\r\2\u00db\u00da\3\2\2\2\u00dc\u00df")
        buf.write("\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de")
        buf.write("\u00e0\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e1\7\62\2")
        buf.write("\2\u00e1\27\3\2\2\2\u00e2\u00e8\78\2\2\u00e3\u00e5\5h")
        buf.write("\65\2\u00e4\u00e3\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6")
        buf.write("\3\2\2\2\u00e6\u00e9\5\6\4\2\u00e7\u00e9\5\26\f\2\u00e8")
        buf.write("\u00e4\3\2\2\2\u00e8\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2")
        buf.write("\u00ea\u00eb\5\b\5\2\u00eb\31\3\2\2\2\u00ec\u00ed\7\13")
        buf.write("\2\2\u00ed\u00f1\7\61\2\2\u00ee\u00f0\5 \21\2\u00ef\u00ee")
        buf.write("\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1")
        buf.write("\u00f2\3\2\2\2\u00f2\u00f4\3\2\2\2\u00f3\u00f1\3\2\2\2")
        buf.write("\u00f4\u00f5\7\62\2\2\u00f5\33\3\2\2\2\u00f6\u00fc\7/")
        buf.write("\2\2\u00f7\u00f8\5\36\20\2\u00f8\u00f9\5\6\4\2\u00f9\u00fb")
        buf.write("\3\2\2\2\u00fa\u00f7\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00ff\3\2\2\2")
        buf.write("\u00fe\u00fc\3\2\2\2\u00ff\u0100\7\60\2\2\u0100\35\3\2")
        buf.write("\2\2\u0101\u0106\78\2\2\u0102\u0103\7\65\2\2\u0103\u0105")
        buf.write("\78\2\2\u0104\u0102\3\2\2\2\u0105\u0108\3\2\2\2\u0106")
        buf.write("\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107\37\3\2\2\2\u0108")
        buf.write("\u0106\3\2\2\2\u0109\u010a\78\2\2\u010a\u010c\5\34\17")
        buf.write("\2\u010b\u010d\5\6\4\2\u010c\u010b\3\2\2\2\u010c\u010d")
        buf.write("\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u010f\5\b\5\2\u010f")
        buf.write("!\3\2\2\2\u0110\u0115\5$\23\2\u0111\u0112\7\65\2\2\u0112")
        buf.write("\u0114\5$\23\2\u0113\u0111\3\2\2\2\u0114\u0117\3\2\2\2")
        buf.write("\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116#\3\2\2")
        buf.write("\2\u0117\u0115\3\2\2\2\u0118\u011a\78\2\2\u0119\u011b")
        buf.write("\5h\65\2\u011a\u0119\3\2\2\2\u011a\u011b\3\2\2\2\u011b")
        buf.write("\u011c\3\2\2\2\u011c\u011d\5\6\4\2\u011d%\3\2\2\2\u011e")
        buf.write("\u011f\5(\25\2\u011f\'\3\2\2\2\u0120\u0125\5*\26\2\u0121")
        buf.write("\u0122\7&\2\2\u0122\u0124\5(\25\2\u0123\u0121\3\2\2\2")
        buf.write("\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3")
        buf.write("\2\2\2\u0126)\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u012d")
        buf.write("\5,\27\2\u0129\u012a\7%\2\2\u012a\u012c\5*\26\2\u012b")
        buf.write("\u0129\3\2\2\2\u012c\u012f\3\2\2\2\u012d\u012b\3\2\2\2")
        buf.write("\u012d\u012e\3\2\2\2\u012e+\3\2\2\2\u012f\u012d\3\2\2")
        buf.write("\2\u0130\u0135\5.\30\2\u0131\u0132\t\4\2\2\u0132\u0134")
        buf.write("\5.\30\2\u0133\u0131\3\2\2\2\u0134\u0137\3\2\2\2\u0135")
        buf.write("\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136-\3\2\2\2\u0137")
        buf.write("\u0135\3\2\2\2\u0138\u013d\5\60\31\2\u0139\u013a\t\5\2")
        buf.write("\2\u013a\u013c\5\60\31\2\u013b\u0139\3\2\2\2\u013c\u013f")
        buf.write("\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e")
        buf.write("/\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0145\5\62\32\2\u0141")
        buf.write("\u0142\t\6\2\2\u0142\u0144\5\62\32\2\u0143\u0141\3\2\2")
        buf.write("\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0146")
        buf.write("\3\2\2\2\u0146\61\3\2\2\2\u0147\u0145\3\2\2\2\u0148\u0149")
        buf.write("\t\7\2\2\u0149\u014c\5\62\32\2\u014a\u014c\5\64\33\2\u014b")
        buf.write("\u0148\3\2\2\2\u014b\u014a\3\2\2\2\u014c\63\3\2\2\2\u014d")
        buf.write("\u0153\5\66\34\2\u014e\u014f\7/\2\2\u014f\u0150\5&\24")
        buf.write("\2\u0150\u0151\7\60\2\2\u0151\u0153\3\2\2\2\u0152\u014d")
        buf.write("\3\2\2\2\u0152\u014e\3\2\2\2\u0153\65\3\2\2\2\u0154\u015a")
        buf.write("\5:\36\2\u0155\u0156\7/\2\2\u0156\u0157\5&\24\2\u0157")
        buf.write("\u0158\7\60\2\2\u0158\u015a\3\2\2\2\u0159\u0154\3\2\2")
        buf.write("\2\u0159\u0155\3\2\2\2\u015a\u015e\3\2\2\2\u015b\u015d")
        buf.write("\58\35\2\u015c\u015b\3\2\2\2\u015d\u0160\3\2\2\2\u015e")
        buf.write("\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\67\3\2\2\2\u0160")
        buf.write("\u015e\3\2\2\2\u0161\u0162\7\63\2\2\u0162\u0163\5&\24")
        buf.write("\2\u0163\u0164\7\64\2\2\u0164\u0168\3\2\2\2\u0165\u0166")
        buf.write("\7-\2\2\u0166\u0168\5:\36\2\u0167\u0161\3\2\2\2\u0167")
        buf.write("\u0165\3\2\2\2\u01689\3\2\2\2\u0169\u0172\79\2\2\u016a")
        buf.write("\u0172\7:\2\2\u016b\u0172\7;\2\2\u016c\u0172\7\20\2\2")
        buf.write("\u016d\u0172\7\21\2\2\u016e\u0172\7\22\2\2\u016f\u0172")
        buf.write("\5b\62\2\u0170\u0172\78\2\2\u0171\u0169\3\2\2\2\u0171")
        buf.write("\u016a\3\2\2\2\u0171\u016b\3\2\2\2\u0171\u016c\3\2\2\2")
        buf.write("\u0171\u016d\3\2\2\2\u0171\u016e\3\2\2\2\u0171\u016f\3")
        buf.write("\2\2\2\u0171\u0170\3\2\2\2\u0172;\3\2\2\2\u0173\u0174")
        buf.write("\5H%\2\u0174\u0175\5\b\5\2\u0175\u0199\3\2\2\2\u0176\u0177")
        buf.write("\5P)\2\u0177\u0178\5\b\5\2\u0178\u0199\3\2\2\2\u0179\u017a")
        buf.write("\5R*\2\u017a\u017b\5\b\5\2\u017b\u0199\3\2\2\2\u017c\u017d")
        buf.write("\5^\60\2\u017d\u017e\5\b\5\2\u017e\u0199\3\2\2\2\u017f")
        buf.write("\u0180\5`\61\2\u0180\u0181\5\b\5\2\u0181\u0199\3\2\2\2")
        buf.write("\u0182\u0183\5b\62\2\u0183\u0184\5\b\5\2\u0184\u0199\3")
        buf.write("\2\2\2\u0185\u0186\5d\63\2\u0186\u0187\5\b\5\2\u0187\u0199")
        buf.write("\3\2\2\2\u0188\u0189\5\f\7\2\u0189\u018a\5\b\5\2\u018a")
        buf.write("\u0199\3\2\2\2\u018b\u018c\5\20\t\2\u018c\u018d\5\b\5")
        buf.write("\2\u018d\u0199\3\2\2\2\u018e\u018f\5\24\13\2\u018f\u0190")
        buf.write("\5\b\5\2\u0190\u0199\3\2\2\2\u0191\u0192\5\22\n\2\u0192")
        buf.write("\u0193\5\b\5\2\u0193\u0199\3\2\2\2\u0194\u0196\5f\64\2")
        buf.write("\u0195\u0197\5\b\5\2\u0196\u0195\3\2\2\2\u0196\u0197\3")
        buf.write("\2\2\2\u0197\u0199\3\2\2\2\u0198\u0173\3\2\2\2\u0198\u0176")
        buf.write("\3\2\2\2\u0198\u0179\3\2\2\2\u0198\u017c\3\2\2\2\u0198")
        buf.write("\u017f\3\2\2\2\u0198\u0182\3\2\2\2\u0198\u0185\3\2\2\2")
        buf.write("\u0198\u0188\3\2\2\2\u0198\u018b\3\2\2\2\u0198\u018e\3")
        buf.write("\2\2\2\u0198\u0191\3\2\2\2\u0198\u0194\3\2\2\2\u0199=")
        buf.write("\3\2\2\2\u019a\u019b\5h\65\2\u019b\u019c\5\6\4\2\u019c")
        buf.write("\u019d\5@!\2\u019d?\3\2\2\2\u019e\u019f\7\61\2\2\u019f")
        buf.write("\u01a4\5@!\2\u01a0\u01a1\7\65\2\2\u01a1\u01a3\5@!\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2")
        buf.write("\u01a4\u01a5\3\2\2\2\u01a5\u01a7\3\2\2\2\u01a6\u01a4\3")
        buf.write("\2\2\2\u01a7\u01a8\7\62\2\2\u01a8\u01b5\3\2\2\2\u01a9")
        buf.write("\u01aa\7\61\2\2\u01aa\u01af\5&\24\2\u01ab\u01ac\7\65\2")
        buf.write("\2\u01ac\u01ae\5&\24\2\u01ad\u01ab\3\2\2\2\u01ae\u01b1")
        buf.write("\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0")
        buf.write("\u01b2\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b3\7\62\2")
        buf.write("\2\u01b3\u01b5\3\2\2\2\u01b4\u019e\3\2\2\2\u01b4\u01a9")
        buf.write("\3\2\2\2\u01b5A\3\2\2\2\u01b6\u01b7\78\2\2\u01b7\u01c3")
        buf.write("\7\61\2\2\u01b8\u01bd\5F$\2\u01b9\u01ba\7\65\2\2\u01ba")
        buf.write("\u01bc\5F$\2\u01bb\u01b9\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01c1\3\2\2\2")
        buf.write("\u01bf\u01bd\3\2\2\2\u01c0\u01c2\7\65\2\2\u01c1\u01c0")
        buf.write("\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c4\3\2\2\2\u01c3")
        buf.write("\u01b8\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5\3\2\2\2")
        buf.write("\u01c5\u01c6\7\62\2\2\u01c6C\3\2\2\2\u01c7\u01e4\5&\24")
        buf.write("\2\u01c8\u01e4\5> \2\u01c9\u01e4\5B\"\2\u01ca\u01cb\5")
        buf.write("\26\f\2\u01cb\u01df\7\61\2\2\u01cc\u01cd\78\2\2\u01cd")
        buf.write("\u01cf\7\67\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2")
        buf.write("\2\u01cf\u01d0\3\2\2\2\u01d0\u01d9\5&\24\2\u01d1\u01d4")
        buf.write("\7\65\2\2\u01d2\u01d3\78\2\2\u01d3\u01d5\7\67\2\2\u01d4")
        buf.write("\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d6\3\2\2\2")
        buf.write("\u01d6\u01d8\5&\24\2\u01d7\u01d1\3\2\2\2\u01d8\u01db\3")
        buf.write("\2\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01dd")
        buf.write("\3\2\2\2\u01db\u01d9\3\2\2\2\u01dc\u01de\7\65\2\2\u01dd")
        buf.write("\u01dc\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01e0\3\2\2\2")
        buf.write("\u01df\u01ce\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e1\3")
        buf.write("\2\2\2\u01e1\u01e2\7\62\2\2\u01e2\u01e4\3\2\2\2\u01e3")
        buf.write("\u01c7\3\2\2\2\u01e3\u01c8\3\2\2\2\u01e3\u01c9\3\2\2\2")
        buf.write("\u01e3\u01ca\3\2\2\2\u01e4E\3\2\2\2\u01e5\u01e6\78\2\2")
        buf.write("\u01e6\u01e7\7\67\2\2\u01e7\u01e8\5D#\2\u01e8G\3\2\2\2")
        buf.write("\u01e9\u01ee\5J&\2\u01ea\u01eb\7\65\2\2\u01eb\u01ed\5")
        buf.write("J&\2\u01ec\u01ea\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec")
        buf.write("\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f1\3\2\2\2\u01f0")
        buf.write("\u01ee\3\2\2\2\u01f1\u01f2\5N(\2\u01f2\u01f7\5L\'\2\u01f3")
        buf.write("\u01f4\7\65\2\2\u01f4\u01f6\5L\'\2\u01f5\u01f3\3\2\2\2")
        buf.write("\u01f6\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f8\3")
        buf.write("\2\2\2\u01f8I\3\2\2\2\u01f9\u01f7\3\2\2\2\u01fa\u01ff")
        buf.write("\78\2\2\u01fb\u01fc\7-\2\2\u01fc\u01fe\78\2\2\u01fd\u01fb")
        buf.write("\3\2\2\2\u01fe\u0201\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff")
        buf.write("\u0200\3\2\2\2\u0200\u0203\3\2\2\2\u0201\u01ff\3\2\2\2")
        buf.write("\u0202\u0204\5h\65\2\u0203\u0202\3\2\2\2\u0203\u0204\3")
        buf.write("\2\2\2\u0204K\3\2\2\2\u0205\u0209\5&\24\2\u0206\u0209")
        buf.write("\5> \2\u0207\u0209\5B\"\2\u0208\u0205\3\2\2\2\u0208\u0206")
        buf.write("\3\2\2\2\u0208\u0207\3\2\2\2\u0209M\3\2\2\2\u020a\u020b")
        buf.write("\t\b\2\2\u020bO\3\2\2\2\u020c\u020d\7\4\2\2\u020d\u020e")
        buf.write("\5&\24\2\u020e\u0210\5f\64\2\u020f\u0211\7?\2\2\u0210")
        buf.write("\u020f\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u021b\3\2\2\2")
        buf.write("\u0212\u0213\7\5\2\2\u0213\u0214\7\4\2\2\u0214\u0215\5")
        buf.write("&\24\2\u0215\u0217\5f\64\2\u0216\u0218\7?\2\2\u0217\u0216")
        buf.write("\3\2\2\2\u0217\u0218\3\2\2\2\u0218\u021a\3\2\2\2\u0219")
        buf.write("\u0212\3\2\2\2\u021a\u021d\3\2\2\2\u021b\u0219\3\2\2\2")
        buf.write("\u021b\u021c\3\2\2\2\u021c\u0220\3\2\2\2\u021d\u021b\3")
        buf.write("\2\2\2\u021e\u021f\7\5\2\2\u021f\u0221\5f\64\2\u0220\u021e")
        buf.write("\3\2\2\2\u0220\u0221\3\2\2\2\u0221Q\3\2\2\2\u0222\u0225")
        buf.write("\7\6\2\2\u0223\u0226\5T+\2\u0224\u0226\5\\/\2\u0225\u0223")
        buf.write("\3\2\2\2\u0225\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227")
        buf.write("\u0228\5f\64\2\u0228S\3\2\2\2\u0229\u0231\5X-\2\u022a")
        buf.write("\u022b\5V,\2\u022b\u022c\7\66\2\2\u022c\u022d\5X-\2\u022d")
        buf.write("\u022e\7\66\2\2\u022e\u022f\5Z.\2\u022f\u0231\3\2\2\2")
        buf.write("\u0230\u0229\3\2\2\2\u0230\u022a\3\2\2\2\u0231U\3\2\2")
        buf.write("\2\u0232\u0233\78\2\2\u0233\u0234\7\31\2\2\u0234\u0235")
        buf.write("\5&\24\2\u0235W\3\2\2\2\u0236\u0237\5&\24\2\u0237Y\3\2")
        buf.write("\2\2\u0238\u0239\78\2\2\u0239\u023a\5N(\2\u023a\u023b")
        buf.write("\5&\24\2\u023b[\3\2\2\2\u023c\u023d\t\t\2\2\u023d\u023e")
        buf.write("\7\65\2\2\u023e\u023f\78\2\2\u023f\u0240\7\31\2\2\u0240")
        buf.write("\u0241\7\27\2\2\u0241\u0242\78\2\2\u0242]\3\2\2\2\u0243")
        buf.write("\u0244\7\26\2\2\u0244_\3\2\2\2\u0245\u0246\7\25\2\2\u0246")
        buf.write("a\3\2\2\2\u0247\u024a\78\2\2\u0248\u0249\7-\2\2\u0249")
        buf.write("\u024b\78\2\2\u024a\u0248\3\2\2\2\u024a\u024b\3\2\2\2")
        buf.write("\u024b\u024c\3\2\2\2\u024c\u0255\7/\2\2\u024d\u0252\5")
        buf.write("&\24\2\u024e\u024f\7\65\2\2\u024f\u0251\5&\24\2\u0250")
        buf.write("\u024e\3\2\2\2\u0251\u0254\3\2\2\2\u0252\u0250\3\2\2\2")
        buf.write("\u0252\u0253\3\2\2\2\u0253\u0256\3\2\2\2\u0254\u0252\3")
        buf.write("\2\2\2\u0255\u024d\3\2\2\2\u0255\u0256\3\2\2\2\u0256\u0257")
        buf.write("\3\2\2\2\u0257\u0258\7\60\2\2\u0258c\3\2\2\2\u0259\u025f")
        buf.write("\7\7\2\2\u025a\u0260\5&\24\2\u025b\u025c\5h\65\2\u025c")
        buf.write("\u025d\5\6\4\2\u025d\u025e\5@!\2\u025e\u0260\3\2\2\2\u025f")
        buf.write("\u025a\3\2\2\2\u025f\u025b\3\2\2\2\u025f\u0260\3\2\2\2")
        buf.write("\u0260e\3\2\2\2\u0261\u0265\7\61\2\2\u0262\u0264\5<\37")
        buf.write("\2\u0263\u0262\3\2\2\2\u0264\u0267\3\2\2\2\u0265\u0263")
        buf.write("\3\2\2\2\u0265\u0266\3\2\2\2\u0266\u0268\3\2\2\2\u0267")
        buf.write("\u0265\3\2\2\2\u0268\u0269\7\62\2\2\u0269g\3\2\2\2\u026a")
        buf.write("\u026b\7\63\2\2\u026b\u026c\5&\24\2\u026c\u026d\7\64\2")
        buf.write("\2\u026d\u026f\3\2\2\2\u026e\u026a\3\2\2\2\u026f\u0270")
        buf.write("\3\2\2\2\u0270\u026e\3\2\2\2\u0270\u0271\3\2\2\2\u0271")
        buf.write("i\3\2\2\2Fmqv\u0081\u008c\u0096\u0098\u00a0\u00a4\u00a8")
        buf.write("\u00ac\u00b2\u00b6\u00b9\u00c1\u00d0\u00d4\u00dd\u00e4")
        buf.write("\u00e8\u00f1\u00fc\u0106\u010c\u0115\u011a\u0125\u012d")
        buf.write("\u0135\u013d\u0145\u014b\u0152\u0159\u015e\u0167\u0171")
        buf.write("\u0196\u0198\u01a4\u01af\u01b4\u01bd\u01c1\u01c3\u01ce")
        buf.write("\u01d4\u01d9\u01dd\u01df\u01e3\u01ee\u01f7\u01ff\u0203")
        buf.write("\u0208\u0210\u0217\u021b\u0220\u0225\u0230\u024a\u0252")
        buf.write("\u0255\u025f\u0265\u0270")
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
                     "<INVALID>", "'\n'" ]

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0):
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
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseType" ):
                return visitor.visitBaseType(self)
            else:
                return visitor.visitChildren(self)




    def baseType(self):

        localctx = MiniGoParser.BaseTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
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
            self.state = 131
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MiniGoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaration)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.varDecl()
                self.state = 134
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.funcDecl()
                self.state = 138
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 137
                    self.endOfStatement()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 140
                self.typeDecl()
                self.state = 141
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 143
                self.constDecl()
                self.state = 144
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 146
                self.methodDecl()
                self.state = 148
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 147
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
            self.state = 152
            self.match(MiniGoParser.VAR)
            self.state = 153
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 154
                self.match(MiniGoParser.COMMA)
                self.state = 155
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 161
                self.arrayDims()


            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 164
                self.baseType()
                pass

            elif la_ == 2:
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 165
                    self.baseType()


                self.state = 168
                self.match(MiniGoParser.ASSIGN)
                self.state = 169
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
            self.state = 172
            self.match(MiniGoParser.FUNC)
            self.state = 173
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 174
            self.match(MiniGoParser.LPAREN)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 175
                self.funcParams()


            self.state = 178
            self.match(MiniGoParser.RPAREN)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACKET:
                    self.state = 179
                    self.arrayDims()


                self.state = 182
                self.baseType()


            self.state = 185
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
            self.state = 187
            self.match(MiniGoParser.TYPE)
            self.state = 188
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.state = 189
                self.structDefinition()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 190
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
            self.state = 193
            self.match(MiniGoParser.CONST)
            self.state = 194
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 195
            self.match(MiniGoParser.ASSIGN)
            self.state = 196
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
            self.state = 198
            self.match(MiniGoParser.FUNC)
            self.state = 199
            self.match(MiniGoParser.LPAREN)
            self.state = 200
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 201
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 202
            self.match(MiniGoParser.RPAREN)
            self.state = 203
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 204
            self.match(MiniGoParser.LPAREN)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 205
                self.funcParams()


            self.state = 208
            self.match(MiniGoParser.RPAREN)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 209
                self.baseType()


            self.state = 212
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDefinition" ):
                return visitor.visitStructDefinition(self)
            else:
                return visitor.visitChildren(self)




    def structDefinition(self):

        localctx = MiniGoParser.StructDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_structDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(MiniGoParser.STRUCT)
            self.state = 215
            self.match(MiniGoParser.LBRACE)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 216
                self.structFields()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 222
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFields" ):
                return visitor.visitStructFields(self)
            else:
                return visitor.visitChildren(self)




    def structFields(self):

        localctx = MiniGoParser.StructFieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_structFields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.IDENTIFIER]:
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACKET:
                    self.state = 225
                    self.arrayDims()


                self.state = 228
                self.baseType()
                pass
            elif token in [MiniGoParser.STRUCT]:
                self.state = 229
                self.structDefinition()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 232
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDefinition" ):
                return visitor.visitInterfaceDefinition(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDefinition(self):

        localctx = MiniGoParser.InterfaceDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_interfaceDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(MiniGoParser.INTERFACE)
            self.state = 235
            self.match(MiniGoParser.LBRACE)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 236
                self.interfaceFields()
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 242
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
            self.state = 244
            self.match(MiniGoParser.LPAREN)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 245
                self.listIdentifier()
                self.state = 246
                self.baseType()
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 253
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
        self.enterRule(localctx, 28, self.RULE_listIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 256
                self.match(MiniGoParser.COMMA)
                self.state = 257
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 262
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceFields" ):
                return visitor.visitInterfaceFields(self)
            else:
                return visitor.visitChildren(self)




    def interfaceFields(self):

        localctx = MiniGoParser.InterfaceFieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_interfaceFields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 264
            self.listParams()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 265
                self.baseType()


            self.state = 268
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
        self.enterRule(localctx, 32, self.RULE_funcParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.funcParam()
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 271
                self.match(MiniGoParser.COMMA)
                self.state = 272
                self.funcParam()
                self.state = 277
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncParam" ):
                return visitor.visitFuncParam(self)
            else:
                return visitor.visitChildren(self)




    def funcParam(self):

        localctx = MiniGoParser.FuncParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_funcParam)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(MiniGoParser.IDENTIFIER)

            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 279
                self.arrayDims()


            self.state = 282
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniGoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOrExp" ):
                return visitor.visitLogicOrExp(self)
            else:
                return visitor.visitChildren(self)




    def logicOrExp(self):

        localctx = MiniGoParser.LogicOrExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_logicOrExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.logicAndExp()
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 287
                    self.match(MiniGoParser.OR)
                    self.state = 288
                    self.logicOrExp() 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicAndExp" ):
                return visitor.visitLogicAndExp(self)
            else:
                return visitor.visitChildren(self)




    def logicAndExp(self):

        localctx = MiniGoParser.LogicAndExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_logicAndExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.equalityExp()
            self.state = 299
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 295
                    self.match(MiniGoParser.AND)
                    self.state = 296
                    self.logicAndExp() 
                self.state = 301
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExp" ):
                return visitor.visitEqualityExp(self)
            else:
                return visitor.visitChildren(self)




    def equalityExp(self):

        localctx = MiniGoParser.EqualityExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_equalityExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.additiveExp()
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LEQ) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GEQ))) != 0):
                self.state = 303
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LEQ) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 304
                self.additiveExp()
                self.state = 309
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExp" ):
                return visitor.visitAdditiveExp(self)
            else:
                return visitor.visitChildren(self)




    def additiveExp(self):

        localctx = MiniGoParser.AdditiveExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_additiveExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.multiplicativeExp()
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS:
                self.state = 311
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 312
                self.multiplicativeExp()
                self.state = 317
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExp" ):
                return visitor.visitMultiplicativeExp(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExp(self):

        localctx = MiniGoParser.MultiplicativeExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_multiplicativeExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.unaryExp()
            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0):
                self.state = 319
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 320
                self.unaryExp()
                self.state = 325
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExp" ):
                return visitor.visitUnaryExp(self)
            else:
                return visitor.visitChildren(self)




    def unaryExp(self):

        localctx = MiniGoParser.UnaryExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_unaryExp)
        self._la = 0 # Token type
        try:
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 327
                self.unaryExp()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.LPAREN, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExp" ):
                return visitor.visitPrimaryExp(self)
            else:
                return visitor.visitChildren(self)




    def primaryExp(self):

        localctx = MiniGoParser.PrimaryExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_primaryExp)
        try:
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.postfixExp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.match(MiniGoParser.LPAREN)
                self.state = 333
                self.expression()
                self.state = 334
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixExp" ):
                return visitor.visitPostfixExp(self)
            else:
                return visitor.visitChildren(self)




    def postfixExp(self):

        localctx = MiniGoParser.PostfixExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_postfixExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 338
                self.term()
                pass
            elif token in [MiniGoParser.LPAREN]:
                self.state = 339
                self.match(MiniGoParser.LPAREN)
                self.state = 340
                self.expression()
                self.state = 341
                self.match(MiniGoParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.DOT or _la==MiniGoParser.LBRACKET:
                self.state = 345
                self.postfixOp()
                self.state = 350
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixOp" ):
                return visitor.visitPostfixOp(self)
            else:
                return visitor.visitChildren(self)




    def postfixOp(self):

        localctx = MiniGoParser.PostfixOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_postfixOp)
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.match(MiniGoParser.LBRACKET)
                self.state = 352
                self.expression()
                self.state = 353
                self.match(MiniGoParser.RBRACKET)
                pass
            elif token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.match(MiniGoParser.DOT)
                self.state = 356
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = MiniGoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_term)
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 361
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 362
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 363
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 364
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 365
                self.callStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 366
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.assignStatement()
                self.state = 370
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.ifStatement()
                self.state = 373
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 375
                self.forStatement()
                self.state = 376
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 378
                self.breakStatement()
                self.state = 379
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 381
                self.continueStatement()
                self.state = 382
                self.endOfStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 384
                self.callStatement()
                self.state = 385
                self.endOfStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 387
                self.returnStatement()
                self.state = 388
                self.endOfStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 390
                self.varDecl()
                self.state = 391
                self.endOfStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 393
                self.typeDecl()
                self.state = 394
                self.endOfStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 396
                self.methodDecl()
                self.state = 397
                self.endOfStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 399
                self.constDecl()
                self.state = 400
                self.endOfStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 402
                self.block()
                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.SEMI - -1)) | (1 << (MiniGoParser.NEWLINE - -1)))) != 0):
                    self.state = 403
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLit" ):
                return visitor.visitArrayLit(self)
            else:
                return visitor.visitChildren(self)




    def arrayLit(self):

        localctx = MiniGoParser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.arrayDims()
            self.state = 409
            self.baseType()
            self.state = 410
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
        self.enterRule(localctx, 62, self.RULE_arraysBlock)
        self._la = 0 # Token type
        try:
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.match(MiniGoParser.LBRACE)
                self.state = 413
                self.arraysBlock()
                self.state = 418
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 414
                    self.match(MiniGoParser.COMMA)
                    self.state = 415
                    self.arraysBlock()
                    self.state = 420
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 421
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.match(MiniGoParser.LBRACE)
                self.state = 424
                self.expression()
                self.state = 429
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 425
                    self.match(MiniGoParser.COMMA)
                    self.state = 426
                    self.expression()
                    self.state = 431
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 432
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructExpression" ):
                return visitor.visitStructExpression(self)
            else:
                return visitor.visitChildren(self)




    def structExpression(self):

        localctx = MiniGoParser.StructExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_structExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 437
            self.match(MiniGoParser.LBRACE)
            self.state = 449
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 438
                self.structFieldsAssign()
                self.state = 443
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 439
                        self.match(MiniGoParser.COMMA)
                        self.state = 440
                        self.structFieldsAssign() 
                    self.state = 445
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

                self.state = 447
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.COMMA:
                    self.state = 446
                    self.match(MiniGoParser.COMMA)




            self.state = 451
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructBlock" ):
                return visitor.visitStructBlock(self)
            else:
                return visitor.visitChildren(self)




    def structBlock(self):

        localctx = MiniGoParser.StructBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_structBlock)
        self._la = 0 # Token type
        try:
            self.state = 481
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 455
                self.structExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 456
                self.structDefinition()
                self.state = 457
                self.match(MiniGoParser.LBRACE)
                self.state = 477
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 460
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                    if la_ == 1:
                        self.state = 458
                        self.match(MiniGoParser.IDENTIFIER)
                        self.state = 459
                        self.match(MiniGoParser.COLON)


                    self.state = 462
                    self.expression()
                    self.state = 471
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 463
                            self.match(MiniGoParser.COMMA)
                            self.state = 466
                            self._errHandler.sync(self)
                            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                            if la_ == 1:
                                self.state = 464
                                self.match(MiniGoParser.IDENTIFIER)
                                self.state = 465
                                self.match(MiniGoParser.COLON)


                            self.state = 468
                            self.expression() 
                        self.state = 473
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

                    self.state = 475
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MiniGoParser.COMMA:
                        self.state = 474
                        self.match(MiniGoParser.COMMA)




                self.state = 479
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFieldsAssign" ):
                return visitor.visitStructFieldsAssign(self)
            else:
                return visitor.visitChildren(self)




    def structFieldsAssign(self):

        localctx = MiniGoParser.StructFieldsAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_structFieldsAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 484
            self.match(MiniGoParser.COLON)
            self.state = 485
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignStatement(self):

        localctx = MiniGoParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_assignStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.a1()
            self.state = 492
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 488
                self.match(MiniGoParser.COMMA)
                self.state = 489
                self.a1()
                self.state = 494
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 495
            self.assignmentOperator()
            self.state = 496
            self.a2()
            self.state = 501
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 497
                self.match(MiniGoParser.COMMA)
                self.state = 498
                self.a2()
                self.state = 503
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA1" ):
                return visitor.visitA1(self)
            else:
                return visitor.visitChildren(self)




    def a1(self):

        localctx = MiniGoParser.A1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_a1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 509
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.DOT:
                self.state = 505
                self.match(MiniGoParser.DOT)
                self.state = 506
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 511
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 513
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 512
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA2" ):
                return visitor.visitA2(self)
            else:
                return visitor.visitChildren(self)




    def a2(self):

        localctx = MiniGoParser.A2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_a2)
        try:
            self.state = 518
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 515
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 516
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 517
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = MiniGoParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniGoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self.match(MiniGoParser.IF)
            self.state = 523
            self.expression()
            self.state = 524
            self.block()
            self.state = 526
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.state = 525
                self.match(MiniGoParser.NEWLINE)


            self.state = 537
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,58,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 528
                    self.match(MiniGoParser.ELSE)
                    self.state = 529
                    self.match(MiniGoParser.IF)
                    self.state = 530
                    self.expression()
                    self.state = 531
                    self.block()
                    self.state = 533
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                    if la_ == 1:
                        self.state = 532
                        self.match(MiniGoParser.NEWLINE)

             
                self.state = 539
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,58,self._ctx)

            self.state = 542
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 540
                self.match(MiniGoParser.ELSE)
                self.state = 541
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = MiniGoParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.match(MiniGoParser.FOR)
            self.state = 547
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.state = 545
                self.forLoop()
                pass

            elif la_ == 2:
                self.state = 546
                self.forIteration()
                pass


            self.state = 549
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
        self.enterRule(localctx, 82, self.RULE_forLoop)
        try:
            self.state = 558
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.forCondition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 552
                self.initilization()
                self.state = 553
                self.match(MiniGoParser.SEMI)
                self.state = 554
                self.forCondition()
                self.state = 555
                self.match(MiniGoParser.SEMI)
                self.state = 556
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
        self.enterRule(localctx, 84, self.RULE_initilization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 561
            self.match(MiniGoParser.DECLARE)
            self.state = 562
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




    def forCondition(self):

        localctx = MiniGoParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = MiniGoParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 567
            self.assignmentOperator()
            self.state = 568
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForIteration" ):
                return visitor.visitForIteration(self)
            else:
                return visitor.visitChildren(self)




    def forIteration(self):

        localctx = MiniGoParser.ForIterationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_forIteration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.BLANK or _la==MiniGoParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 571
            self.match(MiniGoParser.COMMA)
            self.state = 572
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 573
            self.match(MiniGoParser.DECLARE)
            self.state = 574
            self.match(MiniGoParser.RANGE)
            self.state = 575
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = MiniGoParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = MiniGoParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def callStatement(self):

        localctx = MiniGoParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_callStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 584
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.DOT:
                self.state = 582
                self.match(MiniGoParser.DOT)
                self.state = 583
                self.match(MiniGoParser.IDENTIFIER)


            self.state = 586
            self.match(MiniGoParser.LPAREN)
            self.state = 595
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 587
                self.expression()
                self.state = 592
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 588
                    self.match(MiniGoParser.COMMA)
                    self.state = 589
                    self.expression()
                    self.state = 594
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 597
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MiniGoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            self.match(MiniGoParser.RETURN)
            self.state = 605
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 600
                self.expression()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.state = 601
                self.arrayDims()
                self.state = 602
                self.baseType()
                self.state = 603
                self.arraysBlock()
                pass
            elif token in [MiniGoParser.EOF, MiniGoParser.SEMI, MiniGoParser.NEWLINE]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self.match(MiniGoParser.LBRACE)
            self.state = 611
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.LBRACE) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 608
                self.statement()
                self.state = 613
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 614
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


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
        self.enterRule(localctx, 102, self.RULE_arrayDims)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 620 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 616
                self.match(MiniGoParser.LBRACKET)
                self.state = 617
                self.expression()
                self.state = 618
                self.match(MiniGoParser.RBRACKET)
                self.state = 622 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LBRACKET):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





