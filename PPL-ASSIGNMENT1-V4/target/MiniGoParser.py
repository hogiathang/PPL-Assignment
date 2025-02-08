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
        buf.write("\u025a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\7\6\u008e\n\6\f\6\16\6\u0091\13\6\3\6\5\6\u0094\n\6\3")
        buf.write("\6\3\6\5\6\u0098\n\6\3\6\3\6\5\6\u009c\n\6\3\7\3\7\3\7")
        buf.write("\3\7\5\7\u00a2\n\7\3\7\3\7\5\7\u00a6\n\7\3\7\5\7\u00a9")
        buf.write("\n\7\3\7\3\7\7\7\u00ad\n\7\f\7\16\7\u00b0\13\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\5\b\u00b8\n\b\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00c7\n\n\3\n\3\n\5\n")
        buf.write("\u00cb\n\n\3\n\3\n\3\13\3\13\3\13\7\13\u00d2\n\13\f\13")
        buf.write("\16\13\u00d5\13\13\3\13\3\13\3\f\3\f\5\f\u00db\n\f\3\f")
        buf.write("\3\f\5\f\u00df\n\f\3\f\3\f\3\r\3\r\3\r\7\r\u00e6\n\r\f")
        buf.write("\r\16\r\u00e9\13\r\3\r\3\r\3\16\3\16\5\16\u00ef\n\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\7\17\u00f6\n\17\f\17\16\17\u00f9")
        buf.write("\13\17\3\20\3\20\3\20\7\20\u00fe\n\20\f\20\16\20\u0101")
        buf.write("\13\20\3\20\3\20\3\21\3\21\3\21\5\21\u0108\n\21\3\21\3")
        buf.write("\21\3\22\3\22\3\22\7\22\u010f\n\22\f\22\16\22\u0112\13")
        buf.write("\22\3\23\3\23\5\23\u0116\n\23\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\25\7\25\u011f\n\25\f\25\16\25\u0122\13\25\3\26")
        buf.write("\3\26\3\26\7\26\u0127\n\26\f\26\16\26\u012a\13\26\3\27")
        buf.write("\3\27\3\27\7\27\u012f\n\27\f\27\16\27\u0132\13\27\3\30")
        buf.write("\3\30\3\30\7\30\u0137\n\30\f\30\16\30\u013a\13\30\3\31")
        buf.write("\3\31\3\31\7\31\u013f\n\31\f\31\16\31\u0142\13\31\3\32")
        buf.write("\7\32\u0145\n\32\f\32\16\32\u0148\13\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\5\33\u015a\n\33\3\33\7\33\u015d\n\33\f\33\16")
        buf.write("\33\u0160\13\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u0169\n\34\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0191\n")
        buf.write("\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \7 \u019b\n \f \16")
        buf.write(" \u019e\13 \3 \3 \3 \3 \3 \3 \7 \u01a6\n \f \16 \u01a9")
        buf.write("\13 \3 \3 \5 \u01ad\n \3!\3!\3!\3!\3!\7!\u01b4\n!\f!\16")
        buf.write("!\u01b7\13!\3!\5!\u01ba\n!\5!\u01bc\n!\3!\3!\3\"\3\"\3")
        buf.write("\"\5\"\u01c3\n\"\3#\3#\3#\3#\3$\3$\3$\7$\u01cc\n$\f$\16")
        buf.write("$\u01cf\13$\3$\3$\3$\3$\7$\u01d5\n$\f$\16$\u01d8\13$\3")
        buf.write("%\3%\5%\u01dc\n%\3%\3%\3%\3%\5%\u01e2\n%\5%\u01e4\n%\3")
        buf.write("&\3&\3&\5&\u01e9\n&\3\'\3\'\3(\3(\3(\3(\5(\u01f1\n(\3")
        buf.write("(\3(\3(\3(\3(\5(\u01f8\n(\7(\u01fa\n(\f(\16(\u01fd\13")
        buf.write("(\3(\3(\5(\u0201\n(\3)\3)\3)\5)\u0206\n)\3)\3)\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\5*\u0211\n*\3+\3+\3+\3+\3,\3,\3-\3-\3-\3")
        buf.write("-\3.\3.\3.\3.\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61")
        buf.write("\5\61\u022b\n\61\3\61\3\61\3\62\3\62\5\62\u0231\n\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\5\62\u0238\n\62\5\62\u023a\n\62")
        buf.write("\3\63\3\63\3\63\5\63\u023f\n\63\3\64\3\64\3\64\7\64\u0244")
        buf.write("\n\64\f\64\16\64\u0247\13\64\3\65\3\65\6\65\u024b\n\65")
        buf.write("\r\65\16\65\u024c\3\65\3\65\3\66\3\66\5\66\u0253\n\66")
        buf.write("\3\66\6\66\u0256\n\66\r\66\16\66\u0257\3\66\2\3\64\67")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhj\2\13\4\2\13\16\67\67")
        buf.write("\4\2\65\65>>\3\2\36#\3\2\31\32\3\2\33\35\4\2\32\32&&\4")
        buf.write("\2\17\218:\4\2\30\30\'+\4\2--\67\67\2\u0276\2n\3\2\2\2")
        buf.write("\4t\3\2\2\2\6v\3\2\2\2\b\u0087\3\2\2\2\n\u0089\3\2\2\2")
        buf.write("\f\u009d\3\2\2\2\16\u00b3\3\2\2\2\20\u00b9\3\2\2\2\22")
        buf.write("\u00be\3\2\2\2\24\u00ce\3\2\2\2\26\u00d8\3\2\2\2\30\u00e2")
        buf.write("\3\2\2\2\32\u00ec\3\2\2\2\34\u00f2\3\2\2\2\36\u00fa\3")
        buf.write("\2\2\2 \u0104\3\2\2\2\"\u010b\3\2\2\2$\u0113\3\2\2\2&")
        buf.write("\u0119\3\2\2\2(\u011b\3\2\2\2*\u0123\3\2\2\2,\u012b\3")
        buf.write("\2\2\2.\u0133\3\2\2\2\60\u013b\3\2\2\2\62\u0146\3\2\2")
        buf.write("\2\64\u014b\3\2\2\2\66\u0168\3\2\2\28\u016a\3\2\2\2:\u0190")
        buf.write("\3\2\2\2<\u0192\3\2\2\2>\u01ac\3\2\2\2@\u01ae\3\2\2\2")
        buf.write("B\u01c2\3\2\2\2D\u01c4\3\2\2\2F\u01c8\3\2\2\2H\u01e3\3")
        buf.write("\2\2\2J\u01e8\3\2\2\2L\u01ea\3\2\2\2N\u01ec\3\2\2\2P\u0202")
        buf.write("\3\2\2\2R\u0210\3\2\2\2T\u0212\3\2\2\2V\u0216\3\2\2\2")
        buf.write("X\u0218\3\2\2\2Z\u021c\3\2\2\2\\\u0223\3\2\2\2^\u0225")
        buf.write("\3\2\2\2`\u0227\3\2\2\2b\u0239\3\2\2\2d\u023b\3\2\2\2")
        buf.write("f\u0240\3\2\2\2h\u0248\3\2\2\2j\u0255\3\2\2\2lo\5\b\5")
        buf.write("\2mo\5:\36\2nl\3\2\2\2nm\3\2\2\2op\3\2\2\2pn\3\2\2\2p")
        buf.write("q\3\2\2\2qr\3\2\2\2rs\7\2\2\3s\3\3\2\2\2tu\t\2\2\2u\5")
        buf.write("\3\2\2\2vw\t\3\2\2w\7\3\2\2\2xy\5\n\6\2yz\5\6\4\2z\u0088")
        buf.write("\3\2\2\2{|\5\f\7\2|}\5\6\4\2}\u0088\3\2\2\2~\177\5\16")
        buf.write("\b\2\177\u0080\5\6\4\2\u0080\u0088\3\2\2\2\u0081\u0082")
        buf.write("\5\20\t\2\u0082\u0083\5\6\4\2\u0083\u0088\3\2\2\2\u0084")
        buf.write("\u0085\5\22\n\2\u0085\u0086\5\6\4\2\u0086\u0088\3\2\2")
        buf.write("\2\u0087x\3\2\2\2\u0087{\3\2\2\2\u0087~\3\2\2\2\u0087")
        buf.write("\u0081\3\2\2\2\u0087\u0084\3\2\2\2\u0088\t\3\2\2\2\u0089")
        buf.write("\u008a\7\23\2\2\u008a\u008f\7\67\2\2\u008b\u008c\7\64")
        buf.write("\2\2\u008c\u008e\7\67\2\2\u008d\u008b\3\2\2\2\u008e\u0091")
        buf.write("\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write("\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0094\5j\66\2")
        buf.write("\u0093\u0092\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u009b\3")
        buf.write("\2\2\2\u0095\u009c\5\4\3\2\u0096\u0098\5\4\3\2\u0097\u0096")
        buf.write("\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\3\2\2\2\u0099")
        buf.write("\u009a\7\27\2\2\u009a\u009c\5&\24\2\u009b\u0095\3\2\2")
        buf.write("\2\u009b\u0097\3\2\2\2\u009c\13\3\2\2\2\u009d\u009e\7")
        buf.write("\7\2\2\u009e\u009f\7\67\2\2\u009f\u00a1\7.\2\2\u00a0\u00a2")
        buf.write("\5\"\22\2\u00a1\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00a3\3\2\2\2\u00a3\u00a8\7/\2\2\u00a4\u00a6\5j\66\2")
        buf.write("\u00a5\u00a4\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\3")
        buf.write("\2\2\2\u00a7\u00a9\5\4\3\2\u00a8\u00a5\3\2\2\2\u00a8\u00a9")
        buf.write("\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ae\7\60\2\2\u00ab")
        buf.write("\u00ad\5:\36\2\u00ac\u00ab\3\2\2\2\u00ad\u00b0\3\2\2\2")
        buf.write("\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b1\3")
        buf.write("\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b2\7\61\2\2\u00b2")
        buf.write("\r\3\2\2\2\u00b3\u00b4\7\b\2\2\u00b4\u00b7\7\67\2\2\u00b5")
        buf.write("\u00b8\5\24\13\2\u00b6\u00b8\5\30\r\2\u00b7\u00b5\3\2")
        buf.write("\2\2\u00b7\u00b6\3\2\2\2\u00b8\17\3\2\2\2\u00b9\u00ba")
        buf.write("\7\22\2\2\u00ba\u00bb\7\67\2\2\u00bb\u00bc\7\27\2\2\u00bc")
        buf.write("\u00bd\5&\24\2\u00bd\21\3\2\2\2\u00be\u00bf\7\7\2\2\u00bf")
        buf.write("\u00c0\7.\2\2\u00c0\u00c1\7\67\2\2\u00c1\u00c2\7\67\2")
        buf.write("\2\u00c2\u00c3\7/\2\2\u00c3\u00c4\7\67\2\2\u00c4\u00c6")
        buf.write("\7.\2\2\u00c5\u00c7\5\"\22\2\u00c6\u00c5\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00ca\7/\2\2")
        buf.write("\u00c9\u00cb\5\4\3\2\u00ca\u00c9\3\2\2\2\u00ca\u00cb\3")
        buf.write("\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\5h\65\2\u00cd\23")
        buf.write("\3\2\2\2\u00ce\u00cf\7\t\2\2\u00cf\u00d3\7\60\2\2\u00d0")
        buf.write("\u00d2\5\26\f\2\u00d1\u00d0\3\2\2\2\u00d2\u00d5\3\2\2")
        buf.write("\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d6")
        buf.write("\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d7\7\61\2\2\u00d7")
        buf.write("\25\3\2\2\2\u00d8\u00de\7\67\2\2\u00d9\u00db\5j\66\2\u00da")
        buf.write("\u00d9\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dc\3\2\2\2")
        buf.write("\u00dc\u00df\5\4\3\2\u00dd\u00df\5\24\13\2\u00de\u00da")
        buf.write("\3\2\2\2\u00de\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0")
        buf.write("\u00e1\5\6\4\2\u00e1\27\3\2\2\2\u00e2\u00e3\7\n\2\2\u00e3")
        buf.write("\u00e7\7\60\2\2\u00e4\u00e6\5 \21\2\u00e5\u00e4\3\2\2")
        buf.write("\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8")
        buf.write("\3\2\2\2\u00e8\u00ea\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea")
        buf.write("\u00eb\7\61\2\2\u00eb\31\3\2\2\2\u00ec\u00ee\7.\2\2\u00ed")
        buf.write("\u00ef\5\34\17\2\u00ee\u00ed\3\2\2\2\u00ee\u00ef\3\2\2")
        buf.write("\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1\7/\2\2\u00f1\33\3\2")
        buf.write("\2\2\u00f2\u00f7\5\36\20\2\u00f3\u00f4\7\64\2\2\u00f4")
        buf.write("\u00f6\5\36\20\2\u00f5\u00f3\3\2\2\2\u00f6\u00f9\3\2\2")
        buf.write("\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\35\3")
        buf.write("\2\2\2\u00f9\u00f7\3\2\2\2\u00fa\u00ff\7\67\2\2\u00fb")
        buf.write("\u00fc\7\64\2\2\u00fc\u00fe\7\67\2\2\u00fd\u00fb\3\2\2")
        buf.write("\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100")
        buf.write("\3\2\2\2\u0100\u0102\3\2\2\2\u0101\u00ff\3\2\2\2\u0102")
        buf.write("\u0103\5\4\3\2\u0103\37\3\2\2\2\u0104\u0105\7\67\2\2\u0105")
        buf.write("\u0107\5\32\16\2\u0106\u0108\5\4\3\2\u0107\u0106\3\2\2")
        buf.write("\2\u0107\u0108\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a")
        buf.write("\5\6\4\2\u010a!\3\2\2\2\u010b\u0110\5$\23\2\u010c\u010d")
        buf.write("\7\64\2\2\u010d\u010f\5$\23\2\u010e\u010c\3\2\2\2\u010f")
        buf.write("\u0112\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2")
        buf.write("\u0111#\3\2\2\2\u0112\u0110\3\2\2\2\u0113\u0115\7\67\2")
        buf.write("\2\u0114\u0116\5j\66\2\u0115\u0114\3\2\2\2\u0115\u0116")
        buf.write("\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\5\4\3\2\u0118")
        buf.write("%\3\2\2\2\u0119\u011a\5(\25\2\u011a\'\3\2\2\2\u011b\u0120")
        buf.write("\5*\26\2\u011c\u011d\7%\2\2\u011d\u011f\5(\25\2\u011e")
        buf.write("\u011c\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2")
        buf.write("\u0120\u0121\3\2\2\2\u0121)\3\2\2\2\u0122\u0120\3\2\2")
        buf.write("\2\u0123\u0128\5,\27\2\u0124\u0125\7$\2\2\u0125\u0127")
        buf.write("\5*\26\2\u0126\u0124\3\2\2\2\u0127\u012a\3\2\2\2\u0128")
        buf.write("\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129+\3\2\2\2\u012a")
        buf.write("\u0128\3\2\2\2\u012b\u0130\5.\30\2\u012c\u012d\t\4\2\2")
        buf.write("\u012d\u012f\5.\30\2\u012e\u012c\3\2\2\2\u012f\u0132\3")
        buf.write("\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131-")
        buf.write("\3\2\2\2\u0132\u0130\3\2\2\2\u0133\u0138\5\60\31\2\u0134")
        buf.write("\u0135\t\5\2\2\u0135\u0137\5\60\31\2\u0136\u0134\3\2\2")
        buf.write("\2\u0137\u013a\3\2\2\2\u0138\u0136\3\2\2\2\u0138\u0139")
        buf.write("\3\2\2\2\u0139/\3\2\2\2\u013a\u0138\3\2\2\2\u013b\u0140")
        buf.write("\5\62\32\2\u013c\u013d\t\6\2\2\u013d\u013f\5\62\32\2\u013e")
        buf.write("\u013c\3\2\2\2\u013f\u0142\3\2\2\2\u0140\u013e\3\2\2\2")
        buf.write("\u0140\u0141\3\2\2\2\u0141\61\3\2\2\2\u0142\u0140\3\2")
        buf.write("\2\2\u0143\u0145\t\7\2\2\u0144\u0143\3\2\2\2\u0145\u0148")
        buf.write("\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147")
        buf.write("\u0149\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014a\5\64\33")
        buf.write("\2\u014a\63\3\2\2\2\u014b\u014c\b\33\1\2\u014c\u014d\5")
        buf.write("\66\34\2\u014d\u015e\3\2\2\2\u014e\u014f\f\5\2\2\u014f")
        buf.write("\u0150\7\62\2\2\u0150\u0151\5&\24\2\u0151\u0152\7\63\2")
        buf.write("\2\u0152\u015d\3\2\2\2\u0153\u0154\f\4\2\2\u0154\u0155")
        buf.write("\7,\2\2\u0155\u015d\7\67\2\2\u0156\u0157\f\3\2\2\u0157")
        buf.write("\u0159\7.\2\2\u0158\u015a\5f\64\2\u0159\u0158\3\2\2\2")
        buf.write("\u0159\u015a\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015d\7")
        buf.write("/\2\2\u015c\u014e\3\2\2\2\u015c\u0153\3\2\2\2\u015c\u0156")
        buf.write("\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e")
        buf.write("\u015f\3\2\2\2\u015f\65\3\2\2\2\u0160\u015e\3\2\2\2\u0161")
        buf.write("\u0162\7.\2\2\u0162\u0163\5&\24\2\u0163\u0164\7/\2\2\u0164")
        buf.write("\u0169\3\2\2\2\u0165\u0169\58\35\2\u0166\u0169\5b\62\2")
        buf.write("\u0167\u0169\7\67\2\2\u0168\u0161\3\2\2\2\u0168\u0165")
        buf.write("\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0167\3\2\2\2\u0169")
        buf.write("\67\3\2\2\2\u016a\u016b\t\b\2\2\u016b9\3\2\2\2\u016c\u016d")
        buf.write("\5F$\2\u016d\u016e\5\6\4\2\u016e\u0191\3\2\2\2\u016f\u0170")
        buf.write("\5N(\2\u0170\u0171\5\6\4\2\u0171\u0191\3\2\2\2\u0172\u0173")
        buf.write("\5P)\2\u0173\u0174\5\6\4\2\u0174\u0191\3\2\2\2\u0175\u0176")
        buf.write("\5\\/\2\u0176\u0177\5\6\4\2\u0177\u0191\3\2\2\2\u0178")
        buf.write("\u0179\5^\60\2\u0179\u017a\5\6\4\2\u017a\u0191\3\2\2\2")
        buf.write("\u017b\u017c\5b\62\2\u017c\u017d\5\6\4\2\u017d\u0191\3")
        buf.write("\2\2\2\u017e\u017f\5d\63\2\u017f\u0180\5\6\4\2\u0180\u0191")
        buf.write("\3\2\2\2\u0181\u0182\5\n\6\2\u0182\u0183\5\6\4\2\u0183")
        buf.write("\u0191\3\2\2\2\u0184\u0185\5\16\b\2\u0185\u0186\5\6\4")
        buf.write("\2\u0186\u0191\3\2\2\2\u0187\u0188\5\22\n\2\u0188\u0189")
        buf.write("\5\6\4\2\u0189\u0191\3\2\2\2\u018a\u018b\5\20\t\2\u018b")
        buf.write("\u018c\5\6\4\2\u018c\u0191\3\2\2\2\u018d\u018e\5h\65\2")
        buf.write("\u018e\u018f\5\6\4\2\u018f\u0191\3\2\2\2\u0190\u016c\3")
        buf.write("\2\2\2\u0190\u016f\3\2\2\2\u0190\u0172\3\2\2\2\u0190\u0175")
        buf.write("\3\2\2\2\u0190\u0178\3\2\2\2\u0190\u017b\3\2\2\2\u0190")
        buf.write("\u017e\3\2\2\2\u0190\u0181\3\2\2\2\u0190\u0184\3\2\2\2")
        buf.write("\u0190\u0187\3\2\2\2\u0190\u018a\3\2\2\2\u0190\u018d\3")
        buf.write("\2\2\2\u0191;\3\2\2\2\u0192\u0193\5j\66\2\u0193\u0194")
        buf.write("\5\4\3\2\u0194\u0195\5> \2\u0195=\3\2\2\2\u0196\u0197")
        buf.write("\7\60\2\2\u0197\u019c\5> \2\u0198\u0199\7\64\2\2\u0199")
        buf.write("\u019b\5> \2\u019a\u0198\3\2\2\2\u019b\u019e\3\2\2\2\u019c")
        buf.write("\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019f\3\2\2\2")
        buf.write("\u019e\u019c\3\2\2\2\u019f\u01a0\7\61\2\2\u01a0\u01ad")
        buf.write("\3\2\2\2\u01a1\u01a2\7\60\2\2\u01a2\u01a7\5&\24\2\u01a3")
        buf.write("\u01a4\7\64\2\2\u01a4\u01a6\5&\24\2\u01a5\u01a3\3\2\2")
        buf.write("\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8")
        buf.write("\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa")
        buf.write("\u01ab\7\61\2\2\u01ab\u01ad\3\2\2\2\u01ac\u0196\3\2\2")
        buf.write("\2\u01ac\u01a1\3\2\2\2\u01ad?\3\2\2\2\u01ae\u01af\7\67")
        buf.write("\2\2\u01af\u01bb\7\60\2\2\u01b0\u01b5\5D#\2\u01b1\u01b2")
        buf.write("\7\64\2\2\u01b2\u01b4\5D#\2\u01b3\u01b1\3\2\2\2\u01b4")
        buf.write("\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2")
        buf.write("\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8\u01ba\7")
        buf.write("\64\2\2\u01b9\u01b8\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba")
        buf.write("\u01bc\3\2\2\2\u01bb\u01b0\3\2\2\2\u01bb\u01bc\3\2\2\2")
        buf.write("\u01bc\u01bd\3\2\2\2\u01bd\u01be\7\61\2\2\u01beA\3\2\2")
        buf.write("\2\u01bf\u01c3\5&\24\2\u01c0\u01c3\5<\37\2\u01c1\u01c3")
        buf.write("\5@!\2\u01c2\u01bf\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c1")
        buf.write("\3\2\2\2\u01c3C\3\2\2\2\u01c4\u01c5\7\67\2\2\u01c5\u01c6")
        buf.write("\7\66\2\2\u01c6\u01c7\5B\"\2\u01c7E\3\2\2\2\u01c8\u01cd")
        buf.write("\5H%\2\u01c9\u01ca\7\64\2\2\u01ca\u01cc\5H%\2\u01cb\u01c9")
        buf.write("\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd")
        buf.write("\u01ce\3\2\2\2\u01ce\u01d0\3\2\2\2\u01cf\u01cd\3\2\2\2")
        buf.write("\u01d0\u01d1\5L\'\2\u01d1\u01d6\5J&\2\u01d2\u01d3\7\64")
        buf.write("\2\2\u01d3\u01d5\5J&\2\u01d4\u01d2\3\2\2\2\u01d5\u01d8")
        buf.write("\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7")
        buf.write("G\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01dc\5b\62\2\u01da")
        buf.write("\u01dc\7\67\2\2\u01db\u01d9\3\2\2\2\u01db\u01da\3\2\2")
        buf.write("\2\u01dc\u01dd\3\2\2\2\u01dd\u01de\7,\2\2\u01de\u01e4")
        buf.write("\5H%\2\u01df\u01e1\7\67\2\2\u01e0\u01e2\5j\66\2\u01e1")
        buf.write("\u01e0\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e4\3\2\2\2")
        buf.write("\u01e3\u01db\3\2\2\2\u01e3\u01df\3\2\2\2\u01e4I\3\2\2")
        buf.write("\2\u01e5\u01e9\5&\24\2\u01e6\u01e9\5<\37\2\u01e7\u01e9")
        buf.write("\5@!\2\u01e8\u01e5\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e7")
        buf.write("\3\2\2\2\u01e9K\3\2\2\2\u01ea\u01eb\t\t\2\2\u01ebM\3\2")
        buf.write("\2\2\u01ec\u01ed\7\3\2\2\u01ed\u01ee\5&\24\2\u01ee\u01f0")
        buf.write("\5h\65\2\u01ef\u01f1\7>\2\2\u01f0\u01ef\3\2\2\2\u01f0")
        buf.write("\u01f1\3\2\2\2\u01f1\u01fb\3\2\2\2\u01f2\u01f3\7\4\2\2")
        buf.write("\u01f3\u01f4\7\3\2\2\u01f4\u01f5\5&\24\2\u01f5\u01f7\5")
        buf.write("h\65\2\u01f6\u01f8\7>\2\2\u01f7\u01f6\3\2\2\2\u01f7\u01f8")
        buf.write("\3\2\2\2\u01f8\u01fa\3\2\2\2\u01f9\u01f2\3\2\2\2\u01fa")
        buf.write("\u01fd\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2")
        buf.write("\u01fc\u0200\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe\u01ff\7")
        buf.write("\4\2\2\u01ff\u0201\5h\65\2\u0200\u01fe\3\2\2\2\u0200\u0201")
        buf.write("\3\2\2\2\u0201O\3\2\2\2\u0202\u0205\7\5\2\2\u0203\u0206")
        buf.write("\5R*\2\u0204\u0206\5Z.\2\u0205\u0203\3\2\2\2\u0205\u0204")
        buf.write("\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0208\5h\65\2\u0208")
        buf.write("Q\3\2\2\2\u0209\u0211\5V,\2\u020a\u020b\5T+\2\u020b\u020c")
        buf.write("\7\65\2\2\u020c\u020d\5V,\2\u020d\u020e\7\65\2\2\u020e")
        buf.write("\u020f\5X-\2\u020f\u0211\3\2\2\2\u0210\u0209\3\2\2\2\u0210")
        buf.write("\u020a\3\2\2\2\u0211S\3\2\2\2\u0212\u0213\7\67\2\2\u0213")
        buf.write("\u0214\7\30\2\2\u0214\u0215\5&\24\2\u0215U\3\2\2\2\u0216")
        buf.write("\u0217\5&\24\2\u0217W\3\2\2\2\u0218\u0219\7\67\2\2\u0219")
        buf.write("\u021a\5L\'\2\u021a\u021b\5&\24\2\u021bY\3\2\2\2\u021c")
        buf.write("\u021d\t\n\2\2\u021d\u021e\7\64\2\2\u021e\u021f\7\67\2")
        buf.write("\2\u021f\u0220\7\30\2\2\u0220\u0221\7\26\2\2\u0221\u0222")
        buf.write("\7\67\2\2\u0222[\3\2\2\2\u0223\u0224\7\25\2\2\u0224]\3")
        buf.write("\2\2\2\u0225\u0226\7\24\2\2\u0226_\3\2\2\2\u0227\u0228")
        buf.write("\7\67\2\2\u0228\u022a\7.\2\2\u0229\u022b\5f\64\2\u022a")
        buf.write("\u0229\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022c\3\2\2\2")
        buf.write("\u022c\u022d\7/\2\2\u022da\3\2\2\2\u022e\u0230\7\67\2")
        buf.write("\2\u022f\u0231\5j\66\2\u0230\u022f\3\2\2\2\u0230\u0231")
        buf.write("\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0233\7,\2\2\u0233")
        buf.write("\u023a\5b\62\2\u0234\u0237\5`\61\2\u0235\u0236\7,\2\2")
        buf.write("\u0236\u0238\5b\62\2\u0237\u0235\3\2\2\2\u0237\u0238\3")
        buf.write("\2\2\2\u0238\u023a\3\2\2\2\u0239\u022e\3\2\2\2\u0239\u0234")
        buf.write("\3\2\2\2\u023ac\3\2\2\2\u023b\u023e\7\6\2\2\u023c\u023f")
        buf.write("\5&\24\2\u023d\u023f\5<\37\2\u023e\u023c\3\2\2\2\u023e")
        buf.write("\u023d\3\2\2\2\u023e\u023f\3\2\2\2\u023fe\3\2\2\2\u0240")
        buf.write("\u0245\5&\24\2\u0241\u0242\7\64\2\2\u0242\u0244\5&\24")
        buf.write("\2\u0243\u0241\3\2\2\2\u0244\u0247\3\2\2\2\u0245\u0243")
        buf.write("\3\2\2\2\u0245\u0246\3\2\2\2\u0246g\3\2\2\2\u0247\u0245")
        buf.write("\3\2\2\2\u0248\u024a\7\60\2\2\u0249\u024b\5:\36\2\u024a")
        buf.write("\u0249\3\2\2\2\u024b\u024c\3\2\2\2\u024c\u024a\3\2\2\2")
        buf.write("\u024c\u024d\3\2\2\2\u024d\u024e\3\2\2\2\u024e\u024f\7")
        buf.write("\61\2\2\u024fi\3\2\2\2\u0250\u0252\7\62\2\2\u0251\u0253")
        buf.write("\5&\24\2\u0252\u0251\3\2\2\2\u0252\u0253\3\2\2\2\u0253")
        buf.write("\u0254\3\2\2\2\u0254\u0256\7\63\2\2\u0255\u0250\3\2\2")
        buf.write("\2\u0256\u0257\3\2\2\2\u0257\u0255\3\2\2\2\u0257\u0258")
        buf.write("\3\2\2\2\u0258k\3\2\2\2Anp\u0087\u008f\u0093\u0097\u009b")
        buf.write("\u00a1\u00a5\u00a8\u00ae\u00b7\u00c6\u00ca\u00d3\u00da")
        buf.write("\u00de\u00e7\u00ee\u00f7\u00ff\u0107\u0110\u0115\u0120")
        buf.write("\u0128\u0130\u0138\u0140\u0146\u0159\u015c\u015e\u0168")
        buf.write("\u0190\u019c\u01a7\u01ac\u01b5\u01b9\u01bb\u01c2\u01cd")
        buf.write("\u01d6\u01db\u01e1\u01e3\u01e8\u01f0\u01f7\u01fb\u0200")
        buf.write("\u0205\u0210\u022a\u0230\u0237\u0239\u023e\u0245\u024c")
        buf.write("\u0252\u0257")
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.LBRACE) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseType" ):
                return visitor.visitBaseType(self)
            else:
                return visitor.visitChildren(self)




    def baseType(self):

        localctx = MiniGoParser.BaseTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
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
        self.enterRule(localctx, 4, self.RULE_endOfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
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

            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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
            self.state = 155
            self.match(MiniGoParser.FUNC)
            self.state = 156
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 157
            self.match(MiniGoParser.LPAREN)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 158
                self.funcParams()


            self.state = 161
            self.match(MiniGoParser.RPAREN)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACKET:
                    self.state = 162
                    self.arrayDims()


                self.state = 165
                self.baseType()


            self.state = 168
            self.match(MiniGoParser.LBRACE)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.LBRACE) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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
            self.state = 177
            self.match(MiniGoParser.TYPE)
            self.state = 178
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.state = 179
                self.structDefinition()
                pass
            elif token in [MiniGoParser.INTERFACE]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 195
                self.funcParams()


            self.state = 198
            self.match(MiniGoParser.RPAREN)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDefinition" ):
                return visitor.visitStructDefinition(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.IDENTIFIER:
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
            self.state = 214
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.IDENTIFIER]:
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACKET:
                    self.state = 215
                    self.arrayDims()


                self.state = 218
                self.baseType()
                pass
            elif token in [MiniGoParser.STRUCT]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDefinition" ):
                return visitor.visitInterfaceDefinition(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.IDENTIFIER:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListParams" ):
                return visitor.visitListParams(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.IDENTIFIER:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListIdentifier" ):
                return visitor.visitListIdentifier(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListGroup" ):
                return visitor.visitListGroup(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.COMMA:
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
            self.state = 258
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 259
            self.listParams()
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
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
            self.state = 265
            self.funcParam()
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
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
            self.state = 273
            self.match(MiniGoParser.IDENTIFIER)

            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
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
            self.state = 297
            self.additiveExp()
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LEQ) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GEQ))) != 0):
                self.state = 298
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LEQ) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GEQ))) != 0)):
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
            self.state = 305
            self.multiplicativeExp()
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS:
                self.state = 306
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
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
            self.state = 313
            self.unaryExp()
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0):
                self.state = 314
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
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
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.MINUS or _la==MiniGoParser.NOT:
                self.state = 321
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
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
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExp" ):
                return visitor.visitPrimaryExp(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLit" ):
                return visitor.visitArrayLit(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraysBlock" ):
                return visitor.visitArraysBlock(self)
            else:
                return visitor.visitChildren(self)




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
                while _la==MiniGoParser.COMMA:
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
                while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructExpression" ):
                return visitor.visitStructExpression(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.IDENTIFIER:
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
                if _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructBlock" ):
                return visitor.visitStructBlock(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFieldsAssign" ):
                return visitor.visitStructFieldsAssign(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.COMMA:
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
            while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA1" ):
                return visitor.visitA1(self)
            else:
                return visitor.visitChildren(self)




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
                if _la==MiniGoParser.LBRACKET:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA2" ):
                return visitor.visitA2(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = MiniGoParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
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
            if _la==MiniGoParser.ELSE:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitilization" ):
                return visitor.visitInitilization(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForIteration" ):
                return visitor.visitForIteration(self)
            else:
                return visitor.visitChildren(self)




    def forIteration(self):

        localctx = MiniGoParser.ForIterationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_forIteration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.BLANK or _la==MiniGoParser.IDENTIFIER):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryCall" ):
                return visitor.visitPrimaryCall(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
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
                if _la==MiniGoParser.LBRACKET:
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
            self.state = 569
            self.match(MiniGoParser.RETURN)
            self.state = 572
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 570
                self.expression()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.state = 571
                self.arrayLit()
                pass
            elif token in [MiniGoParser.SEMI, MiniGoParser.NEWLINE]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.LBRACE) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDims" ):
                return visitor.visitArrayDims(self)
            else:
                return visitor.visitChildren(self)




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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 591
                    self.expression()


                self.state = 594
                self.match(MiniGoParser.RBRACKET)
                self.state = 597 
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
         




