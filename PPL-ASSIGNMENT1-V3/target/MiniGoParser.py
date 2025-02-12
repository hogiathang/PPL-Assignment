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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u0251\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\3\2\3\2\6\2o\n\2\r\2\16\2p\3\2\3")
        buf.write("\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u0088\n\5\3\6\3\6\3\6\3\6")
        buf.write("\7\6\u008e\n\6\f\6\16\6\u0091\13\6\3\6\3\6\3\6\3\6\5\6")
        buf.write("\u0097\n\6\3\7\3\7\3\7\3\7\3\7\5\7\u009e\n\7\5\7\u00a0")
        buf.write("\n\7\3\b\3\b\3\b\5\b\u00a5\n\b\3\b\3\b\3\b\3\b\3\b\6\b")
        buf.write("\u00ac\n\b\r\b\16\b\u00ad\3\b\3\b\3\b\3\t\5\t\u00b4\n")
        buf.write("\t\3\t\3\t\3\t\5\t\u00b9\n\t\3\n\3\n\3\n\3\n\5\n\u00bf")
        buf.write("\n\n\3\n\5\n\u00c2\n\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u00ca\n\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\5\r\u00d9\n\r\3\r\5\r\u00dc\n\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\7\16\u00e3\n\16\f\16\16\16\u00e6\13\16\3\16")
        buf.write("\3\16\3\17\3\17\5\17\u00ec\n\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\7\20\u00f4\n\20\f\20\16\20\u00f7\13\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\5\21\u00fe\n\21\3\21\5\21\u0101\n\21")
        buf.write("\3\21\3\21\3\22\3\22\5\22\u0107\n\22\3\22\3\22\3\23\3")
        buf.write("\23\3\23\7\23\u010e\n\23\f\23\16\23\u0111\13\23\3\24\3")
        buf.write("\24\3\24\7\24\u0116\n\24\f\24\16\24\u0119\13\24\3\24\3")
        buf.write("\24\3\25\3\25\5\25\u011f\n\25\3\26\3\26\3\27\3\27\3\27")
        buf.write("\7\27\u0126\n\27\f\27\16\27\u0129\13\27\3\30\3\30\3\30")
        buf.write("\7\30\u012e\n\30\f\30\16\30\u0131\13\30\3\31\3\31\3\31")
        buf.write("\7\31\u0136\n\31\f\31\16\31\u0139\13\31\3\32\3\32\3\32")
        buf.write("\7\32\u013e\n\32\f\32\16\32\u0141\13\32\3\33\3\33\3\33")
        buf.write("\7\33\u0146\n\33\f\33\16\33\u0149\13\33\3\34\7\34\u014c")
        buf.write("\n\34\f\34\16\34\u014f\13\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\5\35\u0161\n\35\3\35\7\35\u0164\n\35\f\35\16\35\u0167")
        buf.write("\13\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0170\n")
        buf.write("\36\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \5 \u0195\n \3!\3!\3!\7!\u019a\n!\f!\16!\u019d\13")
        buf.write("!\3!\3!\3!\3!\7!\u01a3\n!\f!\16!\u01a6\13!\3\"\3\"\3\"")
        buf.write("\3\"\7\"\u01ac\n\"\f\"\16\"\u01af\13\"\3#\3#\3#\5#\u01b4")
        buf.write("\n#\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\7%\u01c0\n%\f%\16%\u01c3")
        buf.write("\13%\3%\3%\5%\u01c7\n%\3&\3&\3&\5&\u01cc\n&\3&\3&\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3*\3*\3*\3*\3+")
        buf.write("\3+\3+\3+\3+\3+\3+\3,\3,\3-\3-\3.\3.\3.\3.\5.\u01ef\n")
        buf.write(".\3/\3/\3/\3/\7/\u01f5\n/\f/\16/\u01f8\13/\3/\3/\5/\u01fc")
        buf.write("\n/\3/\3/\3\60\3\60\3\60\7\60\u0203\n\60\f\60\16\60\u0206")
        buf.write("\13\60\3\61\3\61\7\61\u020a\n\61\f\61\16\61\u020d\13\61")
        buf.write("\3\61\3\61\3\62\3\62\5\62\u0213\n\62\3\62\6\62\u0216\n")
        buf.write("\62\r\62\16\62\u0217\3\63\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\64\7\64\u0222\n\64\f\64\16\64\u0225\13\64\3\64\3\64")
        buf.write("\5\64\u0229\n\64\3\64\3\64\3\64\5\64\u022e\n\64\7\64\u0230")
        buf.write("\n\64\f\64\16\64\u0233\13\64\3\64\5\64\u0236\n\64\5\64")
        buf.write("\u0238\n\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\7\65\u0241")
        buf.write("\n\65\f\65\16\65\u0244\13\65\5\65\u0246\n\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\5\66\u024f\n\66\3\66\2\38\67")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhj\2\f\4\2\65\65>>\4\2")
        buf.write("\13\16\67\67\3\2\36#\3\2\31\32\3\2\33\35\4\2\32\32&&\4")
        buf.write("\2\17\218:\4\2\30\30\'+\4\2--\67\67\4\2\64\64>>\2\u026e")
        buf.write("\2n\3\2\2\2\4t\3\2\2\2\6v\3\2\2\2\b\u0087\3\2\2\2\n\u0089")
        buf.write("\3\2\2\2\f\u0098\3\2\2\2\16\u00a4\3\2\2\2\20\u00b3\3\2")
        buf.write("\2\2\22\u00ba\3\2\2\2\24\u00c5\3\2\2\2\26\u00cb\3\2\2")
        buf.write("\2\30\u00d0\3\2\2\2\32\u00df\3\2\2\2\34\u00e9\3\2\2\2")
        buf.write("\36\u00f0\3\2\2\2 \u00fa\3\2\2\2\"\u0104\3\2\2\2$\u010a")
        buf.write("\3\2\2\2&\u0112\3\2\2\2(\u011c\3\2\2\2*\u0120\3\2\2\2")
        buf.write(",\u0122\3\2\2\2.\u012a\3\2\2\2\60\u0132\3\2\2\2\62\u013a")
        buf.write("\3\2\2\2\64\u0142\3\2\2\2\66\u014d\3\2\2\28\u0152\3\2")
        buf.write("\2\2:\u016f\3\2\2\2<\u0171\3\2\2\2>\u0194\3\2\2\2@\u0196")
        buf.write("\3\2\2\2B\u01a7\3\2\2\2D\u01b3\3\2\2\2F\u01b5\3\2\2\2")
        buf.write("H\u01b7\3\2\2\2J\u01c8\3\2\2\2L\u01cf\3\2\2\2N\u01d5\3")
        buf.write("\2\2\2P\u01d9\3\2\2\2R\u01db\3\2\2\2T\u01df\3\2\2\2V\u01e6")
        buf.write("\3\2\2\2X\u01e8\3\2\2\2Z\u01ea\3\2\2\2\\\u01f0\3\2\2\2")
        buf.write("^\u01ff\3\2\2\2`\u0207\3\2\2\2b\u0215\3\2\2\2d\u0219\3")
        buf.write("\2\2\2f\u021d\3\2\2\2h\u023b\3\2\2\2j\u0249\3\2\2\2lo")
        buf.write("\5\b\5\2mo\5> \2nl\3\2\2\2nm\3\2\2\2op\3\2\2\2pn\3\2\2")
        buf.write("\2pq\3\2\2\2qr\3\2\2\2rs\7\2\2\3s\3\3\2\2\2tu\t\2\2\2")
        buf.write("u\5\3\2\2\2vw\t\3\2\2w\7\3\2\2\2xy\5\n\6\2yz\5\4\3\2z")
        buf.write("\u0088\3\2\2\2{|\5\22\n\2|}\5\4\3\2}\u0088\3\2\2\2~\177")
        buf.write("\5\24\13\2\177\u0080\5\4\3\2\u0080\u0088\3\2\2\2\u0081")
        buf.write("\u0082\5\26\f\2\u0082\u0083\5\4\3\2\u0083\u0088\3\2\2")
        buf.write("\2\u0084\u0085\5\30\r\2\u0085\u0086\5\4\3\2\u0086\u0088")
        buf.write("\3\2\2\2\u0087x\3\2\2\2\u0087{\3\2\2\2\u0087~\3\2\2\2")
        buf.write("\u0087\u0081\3\2\2\2\u0087\u0084\3\2\2\2\u0088\t\3\2\2")
        buf.write("\2\u0089\u008a\7\23\2\2\u008a\u008f\7\67\2\2\u008b\u008c")
        buf.write("\7\64\2\2\u008c\u008e\7\67\2\2\u008d\u008b\3\2\2\2\u008e")
        buf.write("\u0091\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2")
        buf.write("\u0090\u0096\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0097\5")
        buf.write("\f\7\2\u0093\u0097\5\6\4\2\u0094\u0097\5\20\t\2\u0095")
        buf.write("\u0097\5\16\b\2\u0096\u0092\3\2\2\2\u0096\u0093\3\2\2")
        buf.write("\2\u0096\u0094\3\2\2\2\u0096\u0095\3\2\2\2\u0096\u0097")
        buf.write("\3\2\2\2\u0097\13\3\2\2\2\u0098\u0099\5b\62\2\u0099\u009f")
        buf.write("\5\6\4\2\u009a\u009d\7\27\2\2\u009b\u009e\5f\64\2\u009c")
        buf.write("\u009e\5*\26\2\u009d\u009b\3\2\2\2\u009d\u009c\3\2\2\2")
        buf.write("\u009e\u00a0\3\2\2\2\u009f\u009a\3\2\2\2\u009f\u00a0\3")
        buf.write("\2\2\2\u00a0\r\3\2\2\2\u00a1\u00a2\5b\62\2\u00a2\u00a3")
        buf.write("\5\6\4\2\u00a3\u00a5\3\2\2\2\u00a4\u00a1\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00ab\7\27\2")
        buf.write("\2\u00a7\u00a8\7\62\2\2\u00a8\u00a9\5*\26\2\u00a9\u00aa")
        buf.write("\7\63\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00a7\3\2\2\2\u00ac")
        buf.write("\u00ad\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2")
        buf.write("\u00ae\u00af\3\2\2\2\u00af\u00b0\5\6\4\2\u00b0\u00b1\5")
        buf.write("f\64\2\u00b1\17\3\2\2\2\u00b2\u00b4\5\6\4\2\u00b3\u00b2")
        buf.write("\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5")
        buf.write("\u00b8\7\27\2\2\u00b6\u00b9\5*\26\2\u00b7\u00b9\5h\65")
        buf.write("\2\u00b8\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\21\3")
        buf.write("\2\2\2\u00ba\u00bb\7\7\2\2\u00bb\u00bc\7\67\2\2\u00bc")
        buf.write("\u00c1\5\"\22\2\u00bd\u00bf\5b\62\2\u00be\u00bd\3\2\2")
        buf.write("\2\u00be\u00bf\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c2")
        buf.write("\5\6\4\2\u00c1\u00be\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2")
        buf.write("\u00c3\3\2\2\2\u00c3\u00c4\5`\61\2\u00c4\23\3\2\2\2\u00c5")
        buf.write("\u00c6\7\b\2\2\u00c6\u00c9\7\67\2\2\u00c7\u00ca\5\32\16")
        buf.write("\2\u00c8\u00ca\5\36\20\2\u00c9\u00c7\3\2\2\2\u00c9\u00c8")
        buf.write("\3\2\2\2\u00ca\25\3\2\2\2\u00cb\u00cc\7\22\2\2\u00cc\u00cd")
        buf.write("\7\67\2\2\u00cd\u00ce\7\27\2\2\u00ce\u00cf\5*\26\2\u00cf")
        buf.write("\27\3\2\2\2\u00d0\u00d1\7\7\2\2\u00d1\u00d2\7.\2\2\u00d2")
        buf.write("\u00d3\7\67\2\2\u00d3\u00d4\7\67\2\2\u00d4\u00d5\7/\2")
        buf.write("\2\u00d5\u00d6\7\67\2\2\u00d6\u00db\5\"\22\2\u00d7\u00d9")
        buf.write("\5b\62\2\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9")
        buf.write("\u00da\3\2\2\2\u00da\u00dc\5\6\4\2\u00db\u00d8\3\2\2\2")
        buf.write("\u00db\u00dc\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\5")
        buf.write("`\61\2\u00de\31\3\2\2\2\u00df\u00e0\7\t\2\2\u00e0\u00e4")
        buf.write("\7\60\2\2\u00e1\u00e3\5\34\17\2\u00e2\u00e1\3\2\2\2\u00e3")
        buf.write("\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2")
        buf.write("\u00e5\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00e8\7")
        buf.write("\61\2\2\u00e8\33\3\2\2\2\u00e9\u00eb\7\67\2\2\u00ea\u00ec")
        buf.write("\5b\62\2\u00eb\u00ea\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec")
        buf.write("\u00ed\3\2\2\2\u00ed\u00ee\5\6\4\2\u00ee\u00ef\5\4\3\2")
        buf.write("\u00ef\35\3\2\2\2\u00f0\u00f1\7\n\2\2\u00f1\u00f5\7\60")
        buf.write("\2\2\u00f2\u00f4\5 \21\2\u00f3\u00f2\3\2\2\2\u00f4\u00f7")
        buf.write("\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6")
        buf.write("\u00f8\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\u00f9\7\61\2")
        buf.write("\2\u00f9\37\3\2\2\2\u00fa\u00fb\7\67\2\2\u00fb\u0100\5")
        buf.write("\"\22\2\u00fc\u00fe\5b\62\2\u00fd\u00fc\3\2\2\2\u00fd")
        buf.write("\u00fe\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0101\5\6\4\2")
        buf.write("\u0100\u00fd\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102\3")
        buf.write("\2\2\2\u0102\u0103\5\4\3\2\u0103!\3\2\2\2\u0104\u0106")
        buf.write("\7.\2\2\u0105\u0107\5$\23\2\u0106\u0105\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109\7/\2\2")
        buf.write("\u0109#\3\2\2\2\u010a\u010f\5&\24\2\u010b\u010c\7\64\2")
        buf.write("\2\u010c\u010e\5&\24\2\u010d\u010b\3\2\2\2\u010e\u0111")
        buf.write("\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110")
        buf.write("%\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0117\5(\25\2\u0113")
        buf.write("\u0114\7\64\2\2\u0114\u0116\5(\25\2\u0115\u0113\3\2\2")
        buf.write("\2\u0116\u0119\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118")
        buf.write("\3\2\2\2\u0118\u011a\3\2\2\2\u0119\u0117\3\2\2\2\u011a")
        buf.write("\u011b\5\6\4\2\u011b\'\3\2\2\2\u011c\u011e\7\67\2\2\u011d")
        buf.write("\u011f\5b\62\2\u011e\u011d\3\2\2\2\u011e\u011f\3\2\2\2")
        buf.write("\u011f)\3\2\2\2\u0120\u0121\5,\27\2\u0121+\3\2\2\2\u0122")
        buf.write("\u0127\5.\30\2\u0123\u0124\7%\2\2\u0124\u0126\5.\30\2")
        buf.write("\u0125\u0123\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125\3")
        buf.write("\2\2\2\u0127\u0128\3\2\2\2\u0128-\3\2\2\2\u0129\u0127")
        buf.write("\3\2\2\2\u012a\u012f\5\60\31\2\u012b\u012c\7$\2\2\u012c")
        buf.write("\u012e\5\60\31\2\u012d\u012b\3\2\2\2\u012e\u0131\3\2\2")
        buf.write("\2\u012f\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130/\3\2")
        buf.write("\2\2\u0131\u012f\3\2\2\2\u0132\u0137\5\62\32\2\u0133\u0134")
        buf.write("\t\4\2\2\u0134\u0136\5\62\32\2\u0135\u0133\3\2\2\2\u0136")
        buf.write("\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2")
        buf.write("\u0138\61\3\2\2\2\u0139\u0137\3\2\2\2\u013a\u013f\5\64")
        buf.write("\33\2\u013b\u013c\t\5\2\2\u013c\u013e\5\64\33\2\u013d")
        buf.write("\u013b\3\2\2\2\u013e\u0141\3\2\2\2\u013f\u013d\3\2\2\2")
        buf.write("\u013f\u0140\3\2\2\2\u0140\63\3\2\2\2\u0141\u013f\3\2")
        buf.write("\2\2\u0142\u0147\5\66\34\2\u0143\u0144\t\6\2\2\u0144\u0146")
        buf.write("\5\66\34\2\u0145\u0143\3\2\2\2\u0146\u0149\3\2\2\2\u0147")
        buf.write("\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148\65\3\2\2\2\u0149")
        buf.write("\u0147\3\2\2\2\u014a\u014c\t\7\2\2\u014b\u014a\3\2\2\2")
        buf.write("\u014c\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3")
        buf.write("\2\2\2\u014e\u0150\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0151")
        buf.write("\58\35\2\u0151\67\3\2\2\2\u0152\u0153\b\35\1\2\u0153\u0154")
        buf.write("\5:\36\2\u0154\u0165\3\2\2\2\u0155\u0156\f\5\2\2\u0156")
        buf.write("\u0157\7\62\2\2\u0157\u0158\5*\26\2\u0158\u0159\7\63\2")
        buf.write("\2\u0159\u0164\3\2\2\2\u015a\u015b\f\4\2\2\u015b\u015c")
        buf.write("\7,\2\2\u015c\u0164\7\67\2\2\u015d\u015e\f\3\2\2\u015e")
        buf.write("\u0160\7.\2\2\u015f\u0161\5^\60\2\u0160\u015f\3\2\2\2")
        buf.write("\u0160\u0161\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0164\7")
        buf.write("/\2\2\u0163\u0155\3\2\2\2\u0163\u015a\3\2\2\2\u0163\u015d")
        buf.write("\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0165")
        buf.write("\u0166\3\2\2\2\u01669\3\2\2\2\u0167\u0165\3\2\2\2\u0168")
        buf.write("\u0169\7.\2\2\u0169\u016a\5*\26\2\u016a\u016b\7/\2\2\u016b")
        buf.write("\u0170\3\2\2\2\u016c\u0170\5<\37\2\u016d\u0170\5\\/\2")
        buf.write("\u016e\u0170\7\67\2\2\u016f\u0168\3\2\2\2\u016f\u016c")
        buf.write("\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u016e\3\2\2\2\u0170")
        buf.write(";\3\2\2\2\u0171\u0172\t\b\2\2\u0172=\3\2\2\2\u0173\u0174")
        buf.write("\5@!\2\u0174\u0175\5\4\3\2\u0175\u0195\3\2\2\2\u0176\u0177")
        buf.write("\5H%\2\u0177\u0178\5\4\3\2\u0178\u0195\3\2\2\2\u0179\u017a")
        buf.write("\5J&\2\u017a\u017b\5\4\3\2\u017b\u0195\3\2\2\2\u017c\u017d")
        buf.write("\5V,\2\u017d\u017e\5\4\3\2\u017e\u0195\3\2\2\2\u017f\u0180")
        buf.write("\5X-\2\u0180\u0181\5\4\3\2\u0181\u0195\3\2\2\2\u0182\u0183")
        buf.write("\5\\/\2\u0183\u0184\5\4\3\2\u0184\u0195\3\2\2\2\u0185")
        buf.write("\u0186\5Z.\2\u0186\u0187\5\4\3\2\u0187\u0195\3\2\2\2\u0188")
        buf.write("\u0189\5\n\6\2\u0189\u018a\5\4\3\2\u018a\u0195\3\2\2\2")
        buf.write("\u018b\u018c\5\24\13\2\u018c\u018d\5\4\3\2\u018d\u0195")
        buf.write("\3\2\2\2\u018e\u018f\5\30\r\2\u018f\u0190\5\4\3\2\u0190")
        buf.write("\u0195\3\2\2\2\u0191\u0192\5\26\f\2\u0192\u0193\5\4\3")
        buf.write("\2\u0193\u0195\3\2\2\2\u0194\u0173\3\2\2\2\u0194\u0176")
        buf.write("\3\2\2\2\u0194\u0179\3\2\2\2\u0194\u017c\3\2\2\2\u0194")
        buf.write("\u017f\3\2\2\2\u0194\u0182\3\2\2\2\u0194\u0185\3\2\2\2")
        buf.write("\u0194\u0188\3\2\2\2\u0194\u018b\3\2\2\2\u0194\u018e\3")
        buf.write("\2\2\2\u0194\u0191\3\2\2\2\u0195?\3\2\2\2\u0196\u019b")
        buf.write("\5B\"\2\u0197\u0198\7\64\2\2\u0198\u019a\5B\"\2\u0199")
        buf.write("\u0197\3\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2")
        buf.write("\u019b\u019c\3\2\2\2\u019c\u019e\3\2\2\2\u019d\u019b\3")
        buf.write("\2\2\2\u019e\u019f\5F$\2\u019f\u01a4\5D#\2\u01a0\u01a1")
        buf.write("\7\64\2\2\u01a1\u01a3\5D#\2\u01a2\u01a0\3\2\2\2\u01a3")
        buf.write("\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2")
        buf.write("\u01a5A\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7\u01ad\7\67\2")
        buf.write("\2\u01a8\u01ac\5b\62\2\u01a9\u01aa\7,\2\2\u01aa\u01ac")
        buf.write("\7\67\2\2\u01ab\u01a8\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac")
        buf.write("\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2")
        buf.write("\u01aeC\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b4\5*\26")
        buf.write("\2\u01b1\u01b4\5d\63\2\u01b2\u01b4\5h\65\2\u01b3\u01b0")
        buf.write("\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4")
        buf.write("E\3\2\2\2\u01b5\u01b6\t\t\2\2\u01b6G\3\2\2\2\u01b7\u01b8")
        buf.write("\7\3\2\2\u01b8\u01b9\5*\26\2\u01b9\u01c1\5`\61\2\u01ba")
        buf.write("\u01bb\7\4\2\2\u01bb\u01bc\7\3\2\2\u01bc\u01bd\5*\26\2")
        buf.write("\u01bd\u01be\5`\61\2\u01be\u01c0\3\2\2\2\u01bf\u01ba\3")
        buf.write("\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2")
        buf.write("\3\2\2\2\u01c2\u01c6\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4")
        buf.write("\u01c5\7\4\2\2\u01c5\u01c7\5`\61\2\u01c6\u01c4\3\2\2\2")
        buf.write("\u01c6\u01c7\3\2\2\2\u01c7I\3\2\2\2\u01c8\u01cb\7\5\2")
        buf.write("\2\u01c9\u01cc\5L\'\2\u01ca\u01cc\5T+\2\u01cb\u01c9\3")
        buf.write("\2\2\2\u01cb\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce")
        buf.write("\5`\61\2\u01ceK\3\2\2\2\u01cf\u01d0\5N(\2\u01d0\u01d1")
        buf.write("\7\65\2\2\u01d1\u01d2\5P)\2\u01d2\u01d3\7\65\2\2\u01d3")
        buf.write("\u01d4\5R*\2\u01d4M\3\2\2\2\u01d5\u01d6\7\67\2\2\u01d6")
        buf.write("\u01d7\7\30\2\2\u01d7\u01d8\5*\26\2\u01d8O\3\2\2\2\u01d9")
        buf.write("\u01da\5*\26\2\u01daQ\3\2\2\2\u01db\u01dc\7\67\2\2\u01dc")
        buf.write("\u01dd\5F$\2\u01dd\u01de\5*\26\2\u01deS\3\2\2\2\u01df")
        buf.write("\u01e0\t\n\2\2\u01e0\u01e1\7\64\2\2\u01e1\u01e2\7\67\2")
        buf.write("\2\u01e2\u01e3\7\30\2\2\u01e3\u01e4\7\26\2\2\u01e4\u01e5")
        buf.write("\7\67\2\2\u01e5U\3\2\2\2\u01e6\u01e7\7\25\2\2\u01e7W\3")
        buf.write("\2\2\2\u01e8\u01e9\7\24\2\2\u01e9Y\3\2\2\2\u01ea\u01ee")
        buf.write("\7\6\2\2\u01eb\u01ef\5*\26\2\u01ec\u01ef\5d\63\2\u01ed")
        buf.write("\u01ef\5h\65\2\u01ee\u01eb\3\2\2\2\u01ee\u01ec\3\2\2\2")
        buf.write("\u01ee\u01ed\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef[\3\2\2")
        buf.write("\2\u01f0\u01f6\7\67\2\2\u01f1\u01f5\5b\62\2\u01f2\u01f3")
        buf.write("\7,\2\2\u01f3\u01f5\7\67\2\2\u01f4\u01f1\3\2\2\2\u01f4")
        buf.write("\u01f2\3\2\2\2\u01f5\u01f8\3\2\2\2\u01f6\u01f4\3\2\2\2")
        buf.write("\u01f6\u01f7\3\2\2\2\u01f7\u01f9\3\2\2\2\u01f8\u01f6\3")
        buf.write("\2\2\2\u01f9\u01fb\7.\2\2\u01fa\u01fc\5^\60\2\u01fb\u01fa")
        buf.write("\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd")
        buf.write("\u01fe\7/\2\2\u01fe]\3\2\2\2\u01ff\u0204\5*\26\2\u0200")
        buf.write("\u0201\7\64\2\2\u0201\u0203\5*\26\2\u0202\u0200\3\2\2")
        buf.write("\2\u0203\u0206\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0205")
        buf.write("\3\2\2\2\u0205_\3\2\2\2\u0206\u0204\3\2\2\2\u0207\u020b")
        buf.write("\7\60\2\2\u0208\u020a\5> \2\u0209\u0208\3\2\2\2\u020a")
        buf.write("\u020d\3\2\2\2\u020b\u0209\3\2\2\2\u020b\u020c\3\2\2\2")
        buf.write("\u020c\u020e\3\2\2\2\u020d\u020b\3\2\2\2\u020e\u020f\7")
        buf.write("\61\2\2\u020fa\3\2\2\2\u0210\u0212\7\62\2\2\u0211\u0213")
        buf.write("\5*\26\2\u0212\u0211\3\2\2\2\u0212\u0213\3\2\2\2\u0213")
        buf.write("\u0214\3\2\2\2\u0214\u0216\7\63\2\2\u0215\u0210\3\2\2")
        buf.write("\2\u0216\u0217\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0218")
        buf.write("\3\2\2\2\u0218c\3\2\2\2\u0219\u021a\5b\62\2\u021a\u021b")
        buf.write("\5\6\4\2\u021b\u021c\5f\64\2\u021ce\3\2\2\2\u021d\u0237")
        buf.write("\7\60\2\2\u021e\u0223\5f\64\2\u021f\u0220\7\64\2\2\u0220")
        buf.write("\u0222\5f\64\2\u0221\u021f\3\2\2\2\u0222\u0225\3\2\2\2")
        buf.write("\u0223\u0221\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u0238\3")
        buf.write("\2\2\2\u0225\u0223\3\2\2\2\u0226\u0229\5*\26\2\u0227\u0229")
        buf.write("\5h\65\2\u0228\u0226\3\2\2\2\u0228\u0227\3\2\2\2\u0229")
        buf.write("\u0231\3\2\2\2\u022a\u022d\7\64\2\2\u022b\u022e\5*\26")
        buf.write("\2\u022c\u022e\5h\65\2\u022d\u022b\3\2\2\2\u022d\u022c")
        buf.write("\3\2\2\2\u022e\u0230\3\2\2\2\u022f\u022a\3\2\2\2\u0230")
        buf.write("\u0233\3\2\2\2\u0231\u022f\3\2\2\2\u0231\u0232\3\2\2\2")
        buf.write("\u0232\u0235\3\2\2\2\u0233\u0231\3\2\2\2\u0234\u0236\t")
        buf.write("\13\2\2\u0235\u0234\3\2\2\2\u0235\u0236\3\2\2\2\u0236")
        buf.write("\u0238\3\2\2\2\u0237\u021e\3\2\2\2\u0237\u0228\3\2\2\2")
        buf.write("\u0238\u0239\3\2\2\2\u0239\u023a\7\61\2\2\u023ag\3\2\2")
        buf.write("\2\u023b\u023c\7\67\2\2\u023c\u0245\7\60\2\2\u023d\u0242")
        buf.write("\5j\66\2\u023e\u023f\7\64\2\2\u023f\u0241\5j\66\2\u0240")
        buf.write("\u023e\3\2\2\2\u0241\u0244\3\2\2\2\u0242\u0240\3\2\2\2")
        buf.write("\u0242\u0243\3\2\2\2\u0243\u0246\3\2\2\2\u0244\u0242\3")
        buf.write("\2\2\2\u0245\u023d\3\2\2\2\u0245\u0246\3\2\2\2\u0246\u0247")
        buf.write("\3\2\2\2\u0247\u0248\7\61\2\2\u0248i\3\2\2\2\u0249\u024a")
        buf.write("\7\67\2\2\u024a\u024e\7\66\2\2\u024b\u024f\5*\26\2\u024c")
        buf.write("\u024f\5d\63\2\u024d\u024f\5h\65\2\u024e\u024b\3\2\2\2")
        buf.write("\u024e\u024c\3\2\2\2\u024e\u024d\3\2\2\2\u024fk\3\2\2")
        buf.write("\2?np\u0087\u008f\u0096\u009d\u009f\u00a4\u00ad\u00b3")
        buf.write("\u00b8\u00be\u00c1\u00c9\u00d8\u00db\u00e4\u00eb\u00f5")
        buf.write("\u00fd\u0100\u0106\u010f\u0117\u011e\u0127\u012f\u0137")
        buf.write("\u013f\u0147\u014d\u0160\u0163\u0165\u016f\u0194\u019b")
        buf.write("\u01a4\u01ab\u01ad\u01b3\u01c1\u01c6\u01cb\u01ee\u01f4")
        buf.write("\u01f6\u01fb\u0204\u020b\u0212\u0217\u0223\u0228\u022d")
        buf.write("\u0231\u0235\u0237\u0242\u0245\u024e")
        return buf.getvalue()


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
                     "<INVALID>", "'\n'" ]

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
    RULE_endOfStatement = 1
    RULE_baseType = 2
    RULE_declaration = 3
    RULE_varDecl = 4
    RULE_arrayDecl = 5
    RULE_arrayLitDecl = 6
    RULE_assignDecl = 7
    RULE_funcDecl = 8
    RULE_typeDecl = 9
    RULE_constDecl = 10
    RULE_methodDecl = 11
    RULE_structDefinition = 12
    RULE_structFields = 13
    RULE_interfaceDefinition = 14
    RULE_interfaceFields = 15
    RULE_listParams = 16
    RULE_listIdentifier = 17
    RULE_listGroup = 18
    RULE_funcParam = 19
    RULE_expression = 20
    RULE_logicOrExp = 21
    RULE_logicAndExp = 22
    RULE_equalityExp = 23
    RULE_additiveExp = 24
    RULE_multiplicativeExp = 25
    RULE_unaryExp = 26
    RULE_postfixExp = 27
    RULE_primaryExp = 28
    RULE_literal = 29
    RULE_statement = 30
    RULE_assignStatement = 31
    RULE_assignTarget = 32
    RULE_assignValue = 33
    RULE_assignmentOperator = 34
    RULE_ifStatement = 35
    RULE_forStatement = 36
    RULE_forLoop = 37
    RULE_initilization = 38
    RULE_forCondition = 39
    RULE_forUpdate = 40
    RULE_forIteration = 41
    RULE_breakStatement = 42
    RULE_continueStatement = 43
    RULE_returnStatement = 44
    RULE_callStatement = 45
    RULE_arguments = 46
    RULE_block = 47
    RULE_arrayDims = 48
    RULE_arrayLit = 49
    RULE_arraysBlock = 50
    RULE_structExpression = 51
    RULE_structFieldsAssign = 52

    ruleNames =  [ "program", "endOfStatement", "baseType", "declaration", 
                   "varDecl", "arrayDecl", "arrayLitDecl", "assignDecl", 
                   "funcDecl", "typeDecl", "constDecl", "methodDecl", "structDefinition", 
                   "structFields", "interfaceDefinition", "interfaceFields", 
                   "listParams", "listIdentifier", "listGroup", "funcParam", 
                   "expression", "logicOrExp", "logicAndExp", "equalityExp", 
                   "additiveExp", "multiplicativeExp", "unaryExp", "postfixExp", 
                   "primaryExp", "literal", "statement", "assignStatement", 
                   "assignTarget", "assignValue", "assignmentOperator", 
                   "ifStatement", "forStatement", "forLoop", "initilization", 
                   "forCondition", "forUpdate", "forIteration", "breakStatement", 
                   "continueStatement", "returnStatement", "callStatement", 
                   "arguments", "block", "arrayDims", "arrayLit", "arraysBlock", 
                   "structExpression", "structFieldsAssign" ]

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


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndOfStatement" ):
                return visitor.visitEndOfStatement(self)
            else:
                return visitor.visitChildren(self)




    def endOfStatement(self):

        localctx = MiniGoParser.EndOfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_endOfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NEWLINE):
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
            self.state = 116
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

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def arrayDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDeclContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def assignDecl(self):
            return self.getTypedRuleContext(MiniGoParser.AssignDeclContext,0)


        def arrayLitDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitDeclContext,0)


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
            self.state = 135
            self.match(MiniGoParser.VAR)
            self.state = 136
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 137
                self.match(MiniGoParser.COMMA)
                self.state = 138
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 144
                self.arrayDecl()

            elif la_ == 2:
                self.state = 145
                self.baseType()

            elif la_ == 3:
                self.state = 146
                self.assignDecl()

            elif la_ == 4:
                self.state = 147
                self.arrayLitDecl()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def arraysBlock(self):
            return self.getTypedRuleContext(MiniGoParser.ArraysBlockContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDecl" ):
                return visitor.visitArrayDecl(self)
            else:
                return visitor.visitChildren(self)




    def arrayDecl(self):

        localctx = MiniGoParser.ArrayDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arrayDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.arrayDims()
            self.state = 151
            self.baseType()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ASSIGN:
                self.state = 152
                self.match(MiniGoParser.ASSIGN)
                self.state = 155
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.LBRACE]:
                    self.state = 153
                    self.arraysBlock()
                    pass
                elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                    self.state = 154
                    self.expression()
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


    class ArrayLitDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def baseType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BaseTypeContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,i)


        def arraysBlock(self):
            return self.getTypedRuleContext(MiniGoParser.ArraysBlockContext,0)


        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


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
            return MiniGoParser.RULE_arrayLitDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLitDecl" ):
                return visitor.visitArrayLitDecl(self)
            else:
                return visitor.visitChildren(self)




    def arrayLitDecl(self):

        localctx = MiniGoParser.ArrayLitDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arrayLitDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 159
                self.arrayDims()
                self.state = 160
                self.baseType()


            self.state = 164
            self.match(MiniGoParser.ASSIGN)
            self.state = 169 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 165
                self.match(MiniGoParser.LBRACKET)
                self.state = 166
                self.expression()
                self.state = 167
                self.match(MiniGoParser.RBRACKET)
                self.state = 171 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LBRACKET):
                    break

            self.state = 173
            self.baseType()
            self.state = 174
            self.arraysBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def structExpression(self):
            return self.getTypedRuleContext(MiniGoParser.StructExpressionContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignDecl" ):
                return visitor.visitAssignDecl(self)
            else:
                return visitor.visitChildren(self)




    def assignDecl(self):

        localctx = MiniGoParser.AssignDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 176
                self.baseType()


            self.state = 179
            self.match(MiniGoParser.ASSIGN)
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 180
                self.expression()
                pass

            elif la_ == 2:
                self.state = 181
                self.structExpression()
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

        def listParams(self):
            return self.getTypedRuleContext(MiniGoParser.ListParamsContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


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
        self.enterRule(localctx, 16, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(MiniGoParser.FUNC)
            self.state = 185
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 186
            self.listParams()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACKET:
                    self.state = 187
                    self.arrayDims()


                self.state = 190
                self.baseType()


            self.state = 193
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
        self.enterRule(localctx, 18, self.RULE_typeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(MiniGoParser.TYPE)
            self.state = 196
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.state = 197
                self.structDefinition()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 198
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
        self.enterRule(localctx, 20, self.RULE_constDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(MiniGoParser.CONST)
            self.state = 202
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 203
            self.match(MiniGoParser.ASSIGN)
            self.state = 204
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

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def listParams(self):
            return self.getTypedRuleContext(MiniGoParser.ListParamsContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


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
            self.state = 206
            self.match(MiniGoParser.FUNC)
            self.state = 207
            self.match(MiniGoParser.LPAREN)
            self.state = 208
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 209
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 210
            self.match(MiniGoParser.RPAREN)
            self.state = 211
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 212
            self.listParams()
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACKET:
                    self.state = 213
                    self.arrayDims()


                self.state = 216
                self.baseType()


            self.state = 219
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
        self.enterRule(localctx, 24, self.RULE_structDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(MiniGoParser.STRUCT)
            self.state = 222
            self.match(MiniGoParser.LBRACE)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 223
                self.structFields()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 229
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
        self.enterRule(localctx, 26, self.RULE_structFields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 232
                self.arrayDims()


            self.state = 235
            self.baseType()
            self.state = 236
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
        self.enterRule(localctx, 28, self.RULE_interfaceDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MiniGoParser.INTERFACE)
            self.state = 239
            self.match(MiniGoParser.LBRACE)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 240
                self.interfaceFields()
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 246
            self.match(MiniGoParser.RBRACE)
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


        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


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
            self.state = 248
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 249
            self.listParams()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACKET:
                    self.state = 250
                    self.arrayDims()


                self.state = 253
                self.baseType()


            self.state = 256
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

        def listIdentifier(self):
            return self.getTypedRuleContext(MiniGoParser.ListIdentifierContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_listParams

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListParams" ):
                return visitor.visitListParams(self)
            else:
                return visitor.visitChildren(self)




    def listParams(self):

        localctx = MiniGoParser.ListParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_listParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(MiniGoParser.LPAREN)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 259
                self.listIdentifier()


            self.state = 262
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListIdentifier" ):
                return visitor.visitListIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def listIdentifier(self):

        localctx = MiniGoParser.ListIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_listIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.listGroup()
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 265
                self.match(MiniGoParser.COMMA)
                self.state = 266
                self.listGroup()
                self.state = 271
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

        def funcParam(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FuncParamContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FuncParamContext,i)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_listGroup

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListGroup" ):
                return visitor.visitListGroup(self)
            else:
                return visitor.visitChildren(self)




    def listGroup(self):

        localctx = MiniGoParser.ListGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_listGroup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.funcParam()
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 273
                self.match(MiniGoParser.COMMA)
                self.state = 274
                self.funcParam()
                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 280
            self.baseType()
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
        self.enterRule(localctx, 38, self.RULE_funcParam)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 283
                self.arrayDims()


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
        self.enterRule(localctx, 40, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
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

        def logicAndExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.LogicAndExpContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.LogicAndExpContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.OR)
            else:
                return self.getToken(MiniGoParser.OR, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_logicOrExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOrExp" ):
                return visitor.visitLogicOrExp(self)
            else:
                return visitor.visitChildren(self)




    def logicOrExp(self):

        localctx = MiniGoParser.LogicOrExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_logicOrExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.logicAndExp()
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.OR:
                self.state = 289
                self.match(MiniGoParser.OR)
                self.state = 290
                self.logicAndExp()
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def equalityExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.EqualityExpContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.EqualityExpContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.AND)
            else:
                return self.getToken(MiniGoParser.AND, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_logicAndExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicAndExp" ):
                return visitor.visitLogicAndExp(self)
            else:
                return visitor.visitChildren(self)




    def logicAndExp(self):

        localctx = MiniGoParser.LogicAndExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_logicAndExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.equalityExp()
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.AND:
                self.state = 297
                self.match(MiniGoParser.AND)
                self.state = 298
                self.equalityExp()
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 46, self.RULE_equalityExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.additiveExp()
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LEQ) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GEQ))) != 0):
                self.state = 305
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LEQ) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 306
                self.additiveExp()
                self.state = 311
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
        self.enterRule(localctx, 48, self.RULE_additiveExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.multiplicativeExp()
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS:
                self.state = 313
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 314
                self.multiplicativeExp()
                self.state = 319
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
        self.enterRule(localctx, 50, self.RULE_multiplicativeExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.unaryExp()
            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0):
                self.state = 321
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 322
                self.unaryExp()
                self.state = 327
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExp" ):
                return visitor.visitUnaryExp(self)
            else:
                return visitor.visitChildren(self)




    def unaryExp(self):

        localctx = MiniGoParser.UnaryExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_unaryExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.MINUS or _la==MiniGoParser.NOT:
                self.state = 328
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 334
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixExp" ):
                return visitor.visitPostfixExp(self)
            else:
                return visitor.visitChildren(self)



    def postfixExp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.PostfixExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_postfixExp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.primaryExp()
            self._ctx.stop = self._input.LT(-1)
            self.state = 355
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 353
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.PostfixExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExp)
                        self.state = 339
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 340
                        self.match(MiniGoParser.LBRACKET)
                        self.state = 341
                        self.expression()
                        self.state = 342
                        self.match(MiniGoParser.RBRACKET)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.PostfixExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExp)
                        self.state = 344
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 345
                        self.match(MiniGoParser.DOT)
                        self.state = 346
                        self.match(MiniGoParser.IDENTIFIER)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.PostfixExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExp)
                        self.state = 347
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 348
                        self.match(MiniGoParser.LPAREN)
                        self.state = 350
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                            self.state = 349
                            self.arguments()


                        self.state = 352
                        self.match(MiniGoParser.RPAREN)
                        pass

             
                self.state = 357
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExp" ):
                return visitor.visitPrimaryExp(self)
            else:
                return visitor.visitChildren(self)




    def primaryExp(self):

        localctx = MiniGoParser.PrimaryExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_primaryExp)
        try:
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.match(MiniGoParser.LPAREN)
                self.state = 359
                self.expression()
                self.state = 360
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 363
                self.callStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 364
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0)):
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_statement)
        try:
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
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

        def assignTarget(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.AssignTargetContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.AssignTargetContext,i)


        def assignmentOperator(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentOperatorContext,0)


        def assignValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.AssignValueContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.AssignValueContext,i)


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
        self.enterRule(localctx, 62, self.RULE_assignStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.assignTarget()
            self.state = 409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 405
                self.match(MiniGoParser.COMMA)
                self.state = 406
                self.assignTarget()
                self.state = 411
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 412
            self.assignmentOperator()
            self.state = 413
            self.assignValue()
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 414
                self.match(MiniGoParser.COMMA)
                self.state = 415
                self.assignValue()
                self.state = 420
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignTargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def arrayDims(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ArrayDimsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DOT)
            else:
                return self.getToken(MiniGoParser.DOT, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignTarget

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignTarget" ):
                return visitor.visitAssignTarget(self)
            else:
                return visitor.visitChildren(self)




    def assignTarget(self):

        localctx = MiniGoParser.AssignTargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_assignTarget)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.DOT or _la==MiniGoParser.LBRACKET:
                self.state = 425
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.LBRACKET]:
                    self.state = 422
                    self.arrayDims()
                    pass
                elif token in [MiniGoParser.DOT]:
                    self.state = 423
                    self.match(MiniGoParser.DOT)
                    self.state = 424
                    self.match(MiniGoParser.IDENTIFIER)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 429
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignValueContext(ParserRuleContext):
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
            return MiniGoParser.RULE_assignValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignValue" ):
                return visitor.visitAssignValue(self)
            else:
                return visitor.visitChildren(self)




    def assignValue(self):

        localctx = MiniGoParser.AssignValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_assignValue)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 432
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
        self.enterRule(localctx, 68, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
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
        self.enterRule(localctx, 70, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(MiniGoParser.IF)
            self.state = 438
            self.expression()
            self.state = 439
            self.block()
            self.state = 447
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 440
                    self.match(MiniGoParser.ELSE)
                    self.state = 441
                    self.match(MiniGoParser.IF)
                    self.state = 442
                    self.expression()
                    self.state = 443
                    self.block() 
                self.state = 449
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 450
                self.match(MiniGoParser.ELSE)
                self.state = 451
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
        self.enterRule(localctx, 72, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(MiniGoParser.FOR)
            self.state = 457
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 455
                self.forLoop()
                pass

            elif la_ == 2:
                self.state = 456
                self.forIteration()
                pass


            self.state = 459
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

        def initilization(self):
            return self.getTypedRuleContext(MiniGoParser.InitilizationContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def forCondition(self):
            return self.getTypedRuleContext(MiniGoParser.ForConditionContext,0)


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
        self.enterRule(localctx, 74, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self.initilization()
            self.state = 462
            self.match(MiniGoParser.SEMI)
            self.state = 463
            self.forCondition()
            self.state = 464
            self.match(MiniGoParser.SEMI)
            self.state = 465
            self.forUpdate()
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
        self.enterRule(localctx, 76, self.RULE_initilization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 468
            self.match(MiniGoParser.DECLARE)
            self.state = 469
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
        self.enterRule(localctx, 78, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
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
        self.enterRule(localctx, 80, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 474
            self.assignmentOperator()
            self.state = 475
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
        self.enterRule(localctx, 82, self.RULE_forIteration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.BLANK or _la==MiniGoParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 478
            self.match(MiniGoParser.COMMA)
            self.state = 479
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 480
            self.match(MiniGoParser.DECLARE)
            self.state = 481
            self.match(MiniGoParser.RANGE)
            self.state = 482
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
        self.enterRule(localctx, 84, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
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
        self.enterRule(localctx, 86, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(MiniGoParser.CONTINUE)
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


        def structExpression(self):
            return self.getTypedRuleContext(MiniGoParser.StructExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MiniGoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(MiniGoParser.RETURN)
            self.state = 492
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 489
                self.expression()

            elif la_ == 2:
                self.state = 490
                self.arrayLit()

            elif la_ == 3:
                self.state = 491
                self.structExpression()


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

        def arrayDims(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ArrayDimsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DOT)
            else:
                return self.getToken(MiniGoParser.DOT, i)

        def arguments(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def callStatement(self):

        localctx = MiniGoParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_callStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 500
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.DOT or _la==MiniGoParser.LBRACKET:
                self.state = 498
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.LBRACKET]:
                    self.state = 495
                    self.arrayDims()
                    pass
                elif token in [MiniGoParser.DOT]:
                    self.state = 496
                    self.match(MiniGoParser.DOT)
                    self.state = 497
                    self.match(MiniGoParser.IDENTIFIER)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 502
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 503
            self.match(MiniGoParser.LPAREN)
            self.state = 505
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 504
                self.arguments()


            self.state = 507
            self.match(MiniGoParser.RPAREN)
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = MiniGoParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.expression()
            self.state = 514
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 510
                self.match(MiniGoParser.COMMA)
                self.state = 511
                self.expression()
                self.state = 516
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(MiniGoParser.LBRACE)
            self.state = 521
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 518
                self.statement()
                self.state = 523
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 524
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDims" ):
                return visitor.visitArrayDims(self)
            else:
                return visitor.visitChildren(self)




    def arrayDims(self):

        localctx = MiniGoParser.ArrayDimsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_arrayDims)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 526
                    self.match(MiniGoParser.LBRACKET)
                    self.state = 528
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                        self.state = 527
                        self.expression()


                    self.state = 530
                    self.match(MiniGoParser.RBRACKET)

                else:
                    raise NoViableAltException(self)
                self.state = 533 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

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
        self.enterRule(localctx, 98, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            self.arrayDims()
            self.state = 536
            self.baseType()
            self.state = 537
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

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def arraysBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ArraysBlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ArraysBlockContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def structExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StructExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StructExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arraysBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraysBlock" ):
                return visitor.visitArraysBlock(self)
            else:
                return visitor.visitChildren(self)




    def arraysBlock(self):

        localctx = MiniGoParser.ArraysBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_arraysBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self.match(MiniGoParser.LBRACE)
            self.state = 565
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACE]:
                self.state = 540
                self.arraysBlock()
                self.state = 545
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 541
                    self.match(MiniGoParser.COMMA)
                    self.state = 542
                    self.arraysBlock()
                    self.state = 547
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 550
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 548
                    self.expression()
                    pass

                elif la_ == 2:
                    self.state = 549
                    self.structExpression()
                    pass


                self.state = 559
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 552
                        self.match(MiniGoParser.COMMA)
                        self.state = 555
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                        if la_ == 1:
                            self.state = 553
                            self.expression()
                            pass

                        elif la_ == 2:
                            self.state = 554
                            self.structExpression()
                            pass

                 
                    self.state = 561
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

                self.state = 563
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.COMMA or _la==MiniGoParser.NEWLINE:
                    self.state = 562
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.COMMA or _la==MiniGoParser.NEWLINE):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                pass
            else:
                raise NoViableAltException(self)

            self.state = 567
            self.match(MiniGoParser.RBRACE)
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
        self.enterRule(localctx, 102, self.RULE_structExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 570
            self.match(MiniGoParser.LBRACE)
            self.state = 579
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 571
                self.structFieldsAssign()
                self.state = 576
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 572
                    self.match(MiniGoParser.COMMA)
                    self.state = 573
                    self.structFieldsAssign()
                    self.state = 578
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 581
            self.match(MiniGoParser.RBRACE)
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

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def structExpression(self):
            return self.getTypedRuleContext(MiniGoParser.StructExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structFieldsAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFieldsAssign" ):
                return visitor.visitStructFieldsAssign(self)
            else:
                return visitor.visitChildren(self)




    def structFieldsAssign(self):

        localctx = MiniGoParser.StructFieldsAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_structFieldsAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 584
            self.match(MiniGoParser.COLON)
            self.state = 588
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.state = 585
                self.expression()
                pass

            elif la_ == 2:
                self.state = 586
                self.arrayLit()
                pass

            elif la_ == 3:
                self.state = 587
                self.structExpression()
                pass


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
        self._predicates[27] = self.postfixExp_sempred
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
         




