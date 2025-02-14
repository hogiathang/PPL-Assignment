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
        buf.write("\u028a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\6\2t\n")
        buf.write("\2\r\2\16\2u\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u008d\n")
        buf.write("\5\3\6\3\6\3\6\3\6\7\6\u0093\n\6\f\6\16\6\u0096\13\6\3")
        buf.write("\6\3\6\3\6\3\6\5\6\u009c\n\6\3\7\3\7\3\7\6\7\u00a1\n\7")
        buf.write("\r\7\16\7\u00a2\3\7\3\7\3\7\5\7\u00a8\n\7\3\b\3\b\3\b")
        buf.write("\6\b\u00ad\n\b\r\b\16\b\u00ae\3\b\5\b\u00b2\n\b\3\b\3")
        buf.write("\b\3\b\3\b\6\b\u00b8\n\b\r\b\16\b\u00b9\3\b\3\b\3\b\3")
        buf.write("\t\5\t\u00c0\n\t\3\t\3\t\3\t\5\t\u00c5\n\t\3\n\3\n\3\n")
        buf.write("\3\n\5\n\u00cb\n\n\3\n\5\n\u00ce\n\n\3\n\3\n\7\n\u00d2")
        buf.write("\n\n\f\n\16\n\u00d5\13\n\3\n\3\n\3\13\3\13\3\13\3\13\5")
        buf.write("\13\u00dd\n\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\5\r\u00ec\n\r\3\r\5\r\u00ef\n\r\3\r\3\r\7")
        buf.write("\r\u00f3\n\r\f\r\16\r\u00f6\13\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\7\16\u00fd\n\16\f\16\16\16\u0100\13\16\3\16\3\16\3\17")
        buf.write("\3\17\5\17\u0106\n\17\3\17\3\17\3\17\3\20\3\20\3\20\7")
        buf.write("\20\u010e\n\20\f\20\16\20\u0111\13\20\3\20\3\20\3\21\3")
        buf.write("\21\3\21\5\21\u0118\n\21\3\21\5\21\u011b\n\21\3\21\3\21")
        buf.write("\3\22\3\22\5\22\u0121\n\22\3\22\3\22\3\23\3\23\3\23\7")
        buf.write("\23\u0128\n\23\f\23\16\23\u012b\13\23\3\24\3\24\3\24\7")
        buf.write("\24\u0130\n\24\f\24\16\24\u0133\13\24\3\24\3\24\3\25\3")
        buf.write("\25\5\25\u0139\n\25\3\26\3\26\3\27\3\27\3\27\7\27\u0140")
        buf.write("\n\27\f\27\16\27\u0143\13\27\3\30\3\30\3\30\7\30\u0148")
        buf.write("\n\30\f\30\16\30\u014b\13\30\3\31\3\31\3\31\7\31\u0150")
        buf.write("\n\31\f\31\16\31\u0153\13\31\3\32\3\32\3\32\7\32\u0158")
        buf.write("\n\32\f\32\16\32\u015b\13\32\3\33\3\33\3\33\7\33\u0160")
        buf.write("\n\33\f\33\16\33\u0163\13\33\3\34\7\34\u0166\n\34\f\34")
        buf.write("\16\34\u0169\13\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u017b")
        buf.write("\n\35\3\35\7\35\u017e\n\35\f\35\16\35\u0181\13\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u018a\n\36\3\37\3")
        buf.write("\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u01af")
        buf.write("\n \3!\3!\3!\3!\3\"\3\"\3\"\3\"\7\"\u01b9\n\"\f\"\16\"")
        buf.write("\u01bc\13\"\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u01c4\n\"\f\"")
        buf.write("\16\"\u01c7\13\"\3\"\5\"\u01ca\n\"\5\"\u01cc\n\"\3\"\5")
        buf.write("\"\u01cf\n\"\3#\3#\3#\3#\3#\3#\3#\5#\u01d8\n#\3$\3$\3")
        buf.write("$\3$\3$\7$\u01df\n$\f$\16$\u01e2\13$\3$\5$\u01e5\n$\5")
        buf.write("$\u01e7\n$\3$\3$\3%\3%\3%\5%\u01ee\n%\3&\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\7\'\u01f7\n\'\f\'\16\'\u01fa\13\'\3\'\3\'\3\'")
        buf.write("\3\'\7\'\u0200\n\'\f\'\16\'\u0203\13\'\3(\3(\5(\u0207")
        buf.write("\n(\3(\3(\3(\3(\5(\u020d\n(\3(\3(\5(\u0211\n(\5(\u0213")
        buf.write("\n(\3)\3)\3)\5)\u0218\n)\3*\3*\3+\3+\3+\3+\5+\u0220\n")
        buf.write("+\3+\3+\3+\3+\3+\5+\u0227\n+\7+\u0229\n+\f+\16+\u022c")
        buf.write("\13+\3+\3+\5+\u0230\n+\3,\3,\3,\5,\u0235\n,\3,\3,\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\5-\u0240\n-\3.\3.\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\64\5\64\u025a\n\64\3\64\3")
        buf.write("\64\3\65\3\65\5\65\u0260\n\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\5\65\u0267\n\65\5\65\u0269\n\65\3\66\3\66\3\66\3\66\5")
        buf.write("\66\u026f\n\66\3\67\3\67\3\67\7\67\u0274\n\67\f\67\16")
        buf.write("\67\u0277\13\67\38\38\68\u027b\n8\r8\168\u027c\38\38\3")
        buf.write("9\39\59\u0283\n9\39\69\u0286\n9\r9\169\u0287\39\2\38:")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnp\2\r\4\2\13\16\67")
        buf.write("\67\4\3\65\65>>\3\2\678\3\2\36#\3\2\31\32\3\2\33\35\4")
        buf.write("\2\32\32&&\4\2\17\218:\4\2\64\64>>\4\2\30\30\'+\4\2--")
        buf.write("\67\67\2\u02b1\2s\3\2\2\2\4y\3\2\2\2\6{\3\2\2\2\b\u008c")
        buf.write("\3\2\2\2\n\u008e\3\2\2\2\f\u00a0\3\2\2\2\16\u00b1\3\2")
        buf.write("\2\2\20\u00bf\3\2\2\2\22\u00c6\3\2\2\2\24\u00d8\3\2\2")
        buf.write("\2\26\u00de\3\2\2\2\30\u00e3\3\2\2\2\32\u00f9\3\2\2\2")
        buf.write("\34\u0103\3\2\2\2\36\u010a\3\2\2\2 \u0114\3\2\2\2\"\u011e")
        buf.write("\3\2\2\2$\u0124\3\2\2\2&\u012c\3\2\2\2(\u0136\3\2\2\2")
        buf.write("*\u013a\3\2\2\2,\u013c\3\2\2\2.\u0144\3\2\2\2\60\u014c")
        buf.write("\3\2\2\2\62\u0154\3\2\2\2\64\u015c\3\2\2\2\66\u0167\3")
        buf.write("\2\2\28\u016c\3\2\2\2:\u0189\3\2\2\2<\u018b\3\2\2\2>\u01ae")
        buf.write("\3\2\2\2@\u01b0\3\2\2\2B\u01ce\3\2\2\2D\u01d7\3\2\2\2")
        buf.write("F\u01d9\3\2\2\2H\u01ed\3\2\2\2J\u01ef\3\2\2\2L\u01f3\3")
        buf.write("\2\2\2N\u0212\3\2\2\2P\u0217\3\2\2\2R\u0219\3\2\2\2T\u021b")
        buf.write("\3\2\2\2V\u0231\3\2\2\2X\u023f\3\2\2\2Z\u0241\3\2\2\2")
        buf.write("\\\u0245\3\2\2\2^\u0247\3\2\2\2`\u024b\3\2\2\2b\u0252")
        buf.write("\3\2\2\2d\u0254\3\2\2\2f\u0256\3\2\2\2h\u0268\3\2\2\2")
        buf.write("j\u026a\3\2\2\2l\u0270\3\2\2\2n\u0278\3\2\2\2p\u0285\3")
        buf.write("\2\2\2rt\5\b\5\2sr\3\2\2\2tu\3\2\2\2us\3\2\2\2uv\3\2\2")
        buf.write("\2vw\3\2\2\2wx\7\2\2\3x\3\3\2\2\2yz\t\2\2\2z\5\3\2\2\2")
        buf.write("{|\t\3\2\2|\7\3\2\2\2}~\5\n\6\2~\177\5\6\4\2\177\u008d")
        buf.write("\3\2\2\2\u0080\u0081\5\22\n\2\u0081\u0082\5\6\4\2\u0082")
        buf.write("\u008d\3\2\2\2\u0083\u0084\5\24\13\2\u0084\u0085\5\6\4")
        buf.write("\2\u0085\u008d\3\2\2\2\u0086\u0087\5\26\f\2\u0087\u0088")
        buf.write("\5\6\4\2\u0088\u008d\3\2\2\2\u0089\u008a\5\30\r\2\u008a")
        buf.write("\u008b\5\6\4\2\u008b\u008d\3\2\2\2\u008c}\3\2\2\2\u008c")
        buf.write("\u0080\3\2\2\2\u008c\u0083\3\2\2\2\u008c\u0086\3\2\2\2")
        buf.write("\u008c\u0089\3\2\2\2\u008d\t\3\2\2\2\u008e\u008f\7\23")
        buf.write("\2\2\u008f\u0094\7\67\2\2\u0090\u0091\7\64\2\2\u0091\u0093")
        buf.write("\7\67\2\2\u0092\u0090\3\2\2\2\u0093\u0096\3\2\2\2\u0094")
        buf.write("\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u009b\3\2\2\2")
        buf.write("\u0096\u0094\3\2\2\2\u0097\u009c\5\4\3\2\u0098\u009c\5")
        buf.write("\20\t\2\u0099\u009c\5\f\7\2\u009a\u009c\5\16\b\2\u009b")
        buf.write("\u0097\3\2\2\2\u009b\u0098\3\2\2\2\u009b\u0099\3\2\2\2")
        buf.write("\u009b\u009a\3\2\2\2\u009c\13\3\2\2\2\u009d\u009e\7\62")
        buf.write("\2\2\u009e\u009f\t\4\2\2\u009f\u00a1\7\63\2\2\u00a0\u009d")
        buf.write("\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2")
        buf.write("\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a7\5\4\3\2")
        buf.write("\u00a5\u00a6\7\27\2\2\u00a6\u00a8\5B\"\2\u00a7\u00a5\3")
        buf.write("\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\r\3\2\2\2\u00a9\u00aa")
        buf.write("\7\62\2\2\u00aa\u00ab\t\4\2\2\u00ab\u00ad\7\63\2\2\u00ac")
        buf.write("\u00a9\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00ac\3\2\2\2")
        buf.write("\u00ae\u00af\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2\5")
        buf.write("\4\3\2\u00b1\u00ac\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3")
        buf.write("\3\2\2\2\u00b3\u00b7\7\27\2\2\u00b4\u00b5\7\62\2\2\u00b5")
        buf.write("\u00b6\t\4\2\2\u00b6\u00b8\7\63\2\2\u00b7\u00b4\3\2\2")
        buf.write("\2\u00b8\u00b9\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\5\4\3\2\u00bc")
        buf.write("\u00bd\5B\"\2\u00bd\17\3\2\2\2\u00be\u00c0\5\4\3\2\u00bf")
        buf.write("\u00be\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1\3\2\2\2")
        buf.write("\u00c1\u00c4\7\27\2\2\u00c2\u00c5\5*\26\2\u00c3\u00c5")
        buf.write("\5F$\2\u00c4\u00c2\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\21")
        buf.write("\3\2\2\2\u00c6\u00c7\7\7\2\2\u00c7\u00c8\7\67\2\2\u00c8")
        buf.write("\u00cd\5\"\22\2\u00c9\u00cb\5p9\2\u00ca\u00c9\3\2\2\2")
        buf.write("\u00ca\u00cb\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00ce\5")
        buf.write("\4\3\2\u00cd\u00ca\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf")
        buf.write("\3\2\2\2\u00cf\u00d3\7\60\2\2\u00d0\u00d2\5> \2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2")
        buf.write("\u00d3\u00d4\3\2\2\2\u00d4\u00d6\3\2\2\2\u00d5\u00d3\3")
        buf.write("\2\2\2\u00d6\u00d7\7\61\2\2\u00d7\23\3\2\2\2\u00d8\u00d9")
        buf.write("\7\b\2\2\u00d9\u00dc\7\67\2\2\u00da\u00dd\5\32\16\2\u00db")
        buf.write("\u00dd\5\36\20\2\u00dc\u00da\3\2\2\2\u00dc\u00db\3\2\2")
        buf.write("\2\u00dd\25\3\2\2\2\u00de\u00df\7\22\2\2\u00df\u00e0\7")
        buf.write("\67\2\2\u00e0\u00e1\7\27\2\2\u00e1\u00e2\5*\26\2\u00e2")
        buf.write("\27\3\2\2\2\u00e3\u00e4\7\7\2\2\u00e4\u00e5\7.\2\2\u00e5")
        buf.write("\u00e6\7\67\2\2\u00e6\u00e7\7\67\2\2\u00e7\u00e8\7/\2")
        buf.write("\2\u00e8\u00e9\7\67\2\2\u00e9\u00ee\5\"\22\2\u00ea\u00ec")
        buf.write("\5p9\2\u00eb\u00ea\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ed")
        buf.write("\3\2\2\2\u00ed\u00ef\5\4\3\2\u00ee\u00eb\3\2\2\2\u00ee")
        buf.write("\u00ef\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f4\7\60\2")
        buf.write("\2\u00f1\u00f3\5> \2\u00f2\u00f1\3\2\2\2\u00f3\u00f6\3")
        buf.write("\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7")
        buf.write("\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f8\7\61\2\2\u00f8")
        buf.write("\31\3\2\2\2\u00f9\u00fa\7\t\2\2\u00fa\u00fe\7\60\2\2\u00fb")
        buf.write("\u00fd\5\34\17\2\u00fc\u00fb\3\2\2\2\u00fd\u0100\3\2\2")
        buf.write("\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0101")
        buf.write("\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0102\7\61\2\2\u0102")
        buf.write("\33\3\2\2\2\u0103\u0105\7\67\2\2\u0104\u0106\5p9\2\u0105")
        buf.write("\u0104\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0107\3\2\2\2")
        buf.write("\u0107\u0108\5\4\3\2\u0108\u0109\5\6\4\2\u0109\35\3\2")
        buf.write("\2\2\u010a\u010b\7\n\2\2\u010b\u010f\7\60\2\2\u010c\u010e")
        buf.write("\5 \21\2\u010d\u010c\3\2\2\2\u010e\u0111\3\2\2\2\u010f")
        buf.write("\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0112\3\2\2\2")
        buf.write("\u0111\u010f\3\2\2\2\u0112\u0113\7\61\2\2\u0113\37\3\2")
        buf.write("\2\2\u0114\u0115\7\67\2\2\u0115\u011a\5\"\22\2\u0116\u0118")
        buf.write("\5p9\2\u0117\u0116\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0119")
        buf.write("\3\2\2\2\u0119\u011b\5\4\3\2\u011a\u0117\3\2\2\2\u011a")
        buf.write("\u011b\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011d\5\6\4\2")
        buf.write("\u011d!\3\2\2\2\u011e\u0120\7.\2\2\u011f\u0121\5$\23\2")
        buf.write("\u0120\u011f\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122\3")
        buf.write("\2\2\2\u0122\u0123\7/\2\2\u0123#\3\2\2\2\u0124\u0129\5")
        buf.write("&\24\2\u0125\u0126\7\64\2\2\u0126\u0128\5&\24\2\u0127")
        buf.write("\u0125\3\2\2\2\u0128\u012b\3\2\2\2\u0129\u0127\3\2\2\2")
        buf.write("\u0129\u012a\3\2\2\2\u012a%\3\2\2\2\u012b\u0129\3\2\2")
        buf.write("\2\u012c\u0131\5(\25\2\u012d\u012e\7\64\2\2\u012e\u0130")
        buf.write("\5(\25\2\u012f\u012d\3\2\2\2\u0130\u0133\3\2\2\2\u0131")
        buf.write("\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0134\3\2\2\2")
        buf.write("\u0133\u0131\3\2\2\2\u0134\u0135\5\4\3\2\u0135\'\3\2\2")
        buf.write("\2\u0136\u0138\7\67\2\2\u0137\u0139\5p9\2\u0138\u0137")
        buf.write("\3\2\2\2\u0138\u0139\3\2\2\2\u0139)\3\2\2\2\u013a\u013b")
        buf.write("\5,\27\2\u013b+\3\2\2\2\u013c\u0141\5.\30\2\u013d\u013e")
        buf.write("\7%\2\2\u013e\u0140\5,\27\2\u013f\u013d\3\2\2\2\u0140")
        buf.write("\u0143\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142\3\2\2\2")
        buf.write("\u0142-\3\2\2\2\u0143\u0141\3\2\2\2\u0144\u0149\5\60\31")
        buf.write("\2\u0145\u0146\7$\2\2\u0146\u0148\5.\30\2\u0147\u0145")
        buf.write("\3\2\2\2\u0148\u014b\3\2\2\2\u0149\u0147\3\2\2\2\u0149")
        buf.write("\u014a\3\2\2\2\u014a/\3\2\2\2\u014b\u0149\3\2\2\2\u014c")
        buf.write("\u0151\5\62\32\2\u014d\u014e\t\5\2\2\u014e\u0150\5\62")
        buf.write("\32\2\u014f\u014d\3\2\2\2\u0150\u0153\3\2\2\2\u0151\u014f")
        buf.write("\3\2\2\2\u0151\u0152\3\2\2\2\u0152\61\3\2\2\2\u0153\u0151")
        buf.write("\3\2\2\2\u0154\u0159\5\64\33\2\u0155\u0156\t\6\2\2\u0156")
        buf.write("\u0158\5\64\33\2\u0157\u0155\3\2\2\2\u0158\u015b\3\2\2")
        buf.write("\2\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\63\3")
        buf.write("\2\2\2\u015b\u0159\3\2\2\2\u015c\u0161\5\66\34\2\u015d")
        buf.write("\u015e\t\7\2\2\u015e\u0160\5\66\34\2\u015f\u015d\3\2\2")
        buf.write("\2\u0160\u0163\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162")
        buf.write("\3\2\2\2\u0162\65\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0166")
        buf.write("\t\b\2\2\u0165\u0164\3\2\2\2\u0166\u0169\3\2\2\2\u0167")
        buf.write("\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u016a\3\2\2\2")
        buf.write("\u0169\u0167\3\2\2\2\u016a\u016b\58\35\2\u016b\67\3\2")
        buf.write("\2\2\u016c\u016d\b\35\1\2\u016d\u016e\5:\36\2\u016e\u017f")
        buf.write("\3\2\2\2\u016f\u0170\f\5\2\2\u0170\u0171\7\62\2\2\u0171")
        buf.write("\u0172\5*\26\2\u0172\u0173\7\63\2\2\u0173\u017e\3\2\2")
        buf.write("\2\u0174\u0175\f\4\2\2\u0175\u0176\7,\2\2\u0176\u017e")
        buf.write("\7\67\2\2\u0177\u0178\f\3\2\2\u0178\u017a\7.\2\2\u0179")
        buf.write("\u017b\5l\67\2\u017a\u0179\3\2\2\2\u017a\u017b\3\2\2\2")
        buf.write("\u017b\u017c\3\2\2\2\u017c\u017e\7/\2\2\u017d\u016f\3")
        buf.write("\2\2\2\u017d\u0174\3\2\2\2\u017d\u0177\3\2\2\2\u017e\u0181")
        buf.write("\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("9\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u0183\7.\2\2\u0183")
        buf.write("\u0184\5*\26\2\u0184\u0185\7/\2\2\u0185\u018a\3\2\2\2")
        buf.write("\u0186\u018a\5<\37\2\u0187\u018a\5h\65\2\u0188\u018a\7")
        buf.write("\67\2\2\u0189\u0182\3\2\2\2\u0189\u0186\3\2\2\2\u0189")
        buf.write("\u0187\3\2\2\2\u0189\u0188\3\2\2\2\u018a;\3\2\2\2\u018b")
        buf.write("\u018c\t\t\2\2\u018c=\3\2\2\2\u018d\u018e\5L\'\2\u018e")
        buf.write("\u018f\5\6\4\2\u018f\u01af\3\2\2\2\u0190\u0191\5T+\2\u0191")
        buf.write("\u0192\5\6\4\2\u0192\u01af\3\2\2\2\u0193\u0194\5V,\2\u0194")
        buf.write("\u0195\5\6\4\2\u0195\u01af\3\2\2\2\u0196\u0197\5b\62\2")
        buf.write("\u0197\u0198\5\6\4\2\u0198\u01af\3\2\2\2\u0199\u019a\5")
        buf.write("d\63\2\u019a\u019b\5\6\4\2\u019b\u01af\3\2\2\2\u019c\u019d")
        buf.write("\5h\65\2\u019d\u019e\5\6\4\2\u019e\u01af\3\2\2\2\u019f")
        buf.write("\u01a0\5j\66\2\u01a0\u01a1\5\6\4\2\u01a1\u01af\3\2\2\2")
        buf.write("\u01a2\u01a3\5\n\6\2\u01a3\u01a4\5\6\4\2\u01a4\u01af\3")
        buf.write("\2\2\2\u01a5\u01a6\5\24\13\2\u01a6\u01a7\5\6\4\2\u01a7")
        buf.write("\u01af\3\2\2\2\u01a8\u01a9\5\30\r\2\u01a9\u01aa\5\6\4")
        buf.write("\2\u01aa\u01af\3\2\2\2\u01ab\u01ac\5\26\f\2\u01ac\u01ad")
        buf.write("\5\6\4\2\u01ad\u01af\3\2\2\2\u01ae\u018d\3\2\2\2\u01ae")
        buf.write("\u0190\3\2\2\2\u01ae\u0193\3\2\2\2\u01ae\u0196\3\2\2\2")
        buf.write("\u01ae\u0199\3\2\2\2\u01ae\u019c\3\2\2\2\u01ae\u019f\3")
        buf.write("\2\2\2\u01ae\u01a2\3\2\2\2\u01ae\u01a5\3\2\2\2\u01ae\u01a8")
        buf.write("\3\2\2\2\u01ae\u01ab\3\2\2\2\u01af?\3\2\2\2\u01b0\u01b1")
        buf.write("\5p9\2\u01b1\u01b2\5\4\3\2\u01b2\u01b3\5B\"\2\u01b3A\3")
        buf.write("\2\2\2\u01b4\u01b5\7\60\2\2\u01b5\u01ba\5B\"\2\u01b6\u01b7")
        buf.write("\7\64\2\2\u01b7\u01b9\5B\"\2\u01b8\u01b6\3\2\2\2\u01b9")
        buf.write("\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2")
        buf.write("\u01bb\u01bd\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01be\7")
        buf.write("\61\2\2\u01be\u01cf\3\2\2\2\u01bf\u01cb\7\60\2\2\u01c0")
        buf.write("\u01c5\5D#\2\u01c1\u01c2\7\64\2\2\u01c2\u01c4\5D#\2\u01c3")
        buf.write("\u01c1\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2")
        buf.write("\u01c5\u01c6\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3")
        buf.write("\2\2\2\u01c8\u01ca\7\64\2\2\u01c9\u01c8\3\2\2\2\u01c9")
        buf.write("\u01ca\3\2\2\2\u01ca\u01cc\3\2\2\2\u01cb\u01c0\3\2\2\2")
        buf.write("\u01cb\u01cc\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01cf\7")
        buf.write("\61\2\2\u01ce\u01b4\3\2\2\2\u01ce\u01bf\3\2\2\2\u01cf")
        buf.write("C\3\2\2\2\u01d0\u01d8\78\2\2\u01d1\u01d8\79\2\2\u01d2")
        buf.write("\u01d8\7:\2\2\u01d3\u01d8\7\17\2\2\u01d4\u01d8\7\20\2")
        buf.write("\2\u01d5\u01d8\7\21\2\2\u01d6\u01d8\5F$\2\u01d7\u01d0")
        buf.write("\3\2\2\2\u01d7\u01d1\3\2\2\2\u01d7\u01d2\3\2\2\2\u01d7")
        buf.write("\u01d3\3\2\2\2\u01d7\u01d4\3\2\2\2\u01d7\u01d5\3\2\2\2")
        buf.write("\u01d7\u01d6\3\2\2\2\u01d8E\3\2\2\2\u01d9\u01da\7\67\2")
        buf.write("\2\u01da\u01e6\7\60\2\2\u01db\u01e0\5J&\2\u01dc\u01dd")
        buf.write("\7\64\2\2\u01dd\u01df\5J&\2\u01de\u01dc\3\2\2\2\u01df")
        buf.write("\u01e2\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2")
        buf.write("\u01e1\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01e5\t")
        buf.write("\n\2\2\u01e4\u01e3\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e7")
        buf.write("\3\2\2\2\u01e6\u01db\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7")
        buf.write("\u01e8\3\2\2\2\u01e8\u01e9\7\61\2\2\u01e9G\3\2\2\2\u01ea")
        buf.write("\u01ee\5*\26\2\u01eb\u01ee\5@!\2\u01ec\u01ee\5F$\2\u01ed")
        buf.write("\u01ea\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ec\3\2\2\2")
        buf.write("\u01eeI\3\2\2\2\u01ef\u01f0\7\67\2\2\u01f0\u01f1\7\66")
        buf.write("\2\2\u01f1\u01f2\5H%\2\u01f2K\3\2\2\2\u01f3\u01f8\5N(")
        buf.write("\2\u01f4\u01f5\7\64\2\2\u01f5\u01f7\5N(\2\u01f6\u01f4")
        buf.write("\3\2\2\2\u01f7\u01fa\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8")
        buf.write("\u01f9\3\2\2\2\u01f9\u01fb\3\2\2\2\u01fa\u01f8\3\2\2\2")
        buf.write("\u01fb\u01fc\5R*\2\u01fc\u0201\5P)\2\u01fd\u01fe\7\64")
        buf.write("\2\2\u01fe\u0200\5P)\2\u01ff\u01fd\3\2\2\2\u0200\u0203")
        buf.write("\3\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202")
        buf.write("M\3\2\2\2\u0203\u0201\3\2\2\2\u0204\u0207\5h\65\2\u0205")
        buf.write("\u0207\7\67\2\2\u0206\u0204\3\2\2\2\u0206\u0205\3\2\2")
        buf.write("\2\u0207\u0208\3\2\2\2\u0208\u0209\7,\2\2\u0209\u0213")
        buf.write("\5N(\2\u020a\u020c\7\67\2\2\u020b\u020d\5p9\2\u020c\u020b")
        buf.write("\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u0210\3\2\2\2\u020e")
        buf.write("\u020f\7,\2\2\u020f\u0211\5N(\2\u0210\u020e\3\2\2\2\u0210")
        buf.write("\u0211\3\2\2\2\u0211\u0213\3\2\2\2\u0212\u0206\3\2\2\2")
        buf.write("\u0212\u020a\3\2\2\2\u0213O\3\2\2\2\u0214\u0218\5*\26")
        buf.write("\2\u0215\u0218\5@!\2\u0216\u0218\5F$\2\u0217\u0214\3\2")
        buf.write("\2\2\u0217\u0215\3\2\2\2\u0217\u0216\3\2\2\2\u0218Q\3")
        buf.write("\2\2\2\u0219\u021a\t\13\2\2\u021aS\3\2\2\2\u021b\u021c")
        buf.write("\7\3\2\2\u021c\u021d\5*\26\2\u021d\u021f\5n8\2\u021e\u0220")
        buf.write("\7>\2\2\u021f\u021e\3\2\2\2\u021f\u0220\3\2\2\2\u0220")
        buf.write("\u022a\3\2\2\2\u0221\u0222\7\4\2\2\u0222\u0223\7\3\2\2")
        buf.write("\u0223\u0224\5*\26\2\u0224\u0226\5n8\2\u0225\u0227\7>")
        buf.write("\2\2\u0226\u0225\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u0229")
        buf.write("\3\2\2\2\u0228\u0221\3\2\2\2\u0229\u022c\3\2\2\2\u022a")
        buf.write("\u0228\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022f\3\2\2\2")
        buf.write("\u022c\u022a\3\2\2\2\u022d\u022e\7\4\2\2\u022e\u0230\5")
        buf.write("n8\2\u022f\u022d\3\2\2\2\u022f\u0230\3\2\2\2\u0230U\3")
        buf.write("\2\2\2\u0231\u0234\7\5\2\2\u0232\u0235\5X-\2\u0233\u0235")
        buf.write("\5`\61\2\u0234\u0232\3\2\2\2\u0234\u0233\3\2\2\2\u0235")
        buf.write("\u0236\3\2\2\2\u0236\u0237\5n8\2\u0237W\3\2\2\2\u0238")
        buf.write("\u0240\5\\/\2\u0239\u023a\5Z.\2\u023a\u023b\7\65\2\2\u023b")
        buf.write("\u023c\5\\/\2\u023c\u023d\7\65\2\2\u023d\u023e\5^\60\2")
        buf.write("\u023e\u0240\3\2\2\2\u023f\u0238\3\2\2\2\u023f\u0239\3")
        buf.write("\2\2\2\u0240Y\3\2\2\2\u0241\u0242\7\67\2\2\u0242\u0243")
        buf.write("\7\30\2\2\u0243\u0244\5*\26\2\u0244[\3\2\2\2\u0245\u0246")
        buf.write("\5*\26\2\u0246]\3\2\2\2\u0247\u0248\7\67\2\2\u0248\u0249")
        buf.write("\5R*\2\u0249\u024a\5*\26\2\u024a_\3\2\2\2\u024b\u024c")
        buf.write("\t\f\2\2\u024c\u024d\7\64\2\2\u024d\u024e\7\67\2\2\u024e")
        buf.write("\u024f\7\30\2\2\u024f\u0250\7\26\2\2\u0250\u0251\7\67")
        buf.write("\2\2\u0251a\3\2\2\2\u0252\u0253\7\25\2\2\u0253c\3\2\2")
        buf.write("\2\u0254\u0255\7\24\2\2\u0255e\3\2\2\2\u0256\u0257\7\67")
        buf.write("\2\2\u0257\u0259\7.\2\2\u0258\u025a\5l\67\2\u0259\u0258")
        buf.write("\3\2\2\2\u0259\u025a\3\2\2\2\u025a\u025b\3\2\2\2\u025b")
        buf.write("\u025c\7/\2\2\u025cg\3\2\2\2\u025d\u025f\7\67\2\2\u025e")
        buf.write("\u0260\5p9\2\u025f\u025e\3\2\2\2\u025f\u0260\3\2\2\2\u0260")
        buf.write("\u0261\3\2\2\2\u0261\u0262\7,\2\2\u0262\u0269\5h\65\2")
        buf.write("\u0263\u0266\5f\64\2\u0264\u0265\7,\2\2\u0265\u0267\5")
        buf.write("h\65\2\u0266\u0264\3\2\2\2\u0266\u0267\3\2\2\2\u0267\u0269")
        buf.write("\3\2\2\2\u0268\u025d\3\2\2\2\u0268\u0263\3\2\2\2\u0269")
        buf.write("i\3\2\2\2\u026a\u026e\7\6\2\2\u026b\u026f\5*\26\2\u026c")
        buf.write("\u026f\5@!\2\u026d\u026f\5F$\2\u026e\u026b\3\2\2\2\u026e")
        buf.write("\u026c\3\2\2\2\u026e\u026d\3\2\2\2\u026e\u026f\3\2\2\2")
        buf.write("\u026fk\3\2\2\2\u0270\u0275\5*\26\2\u0271\u0272\7\64\2")
        buf.write("\2\u0272\u0274\5*\26\2\u0273\u0271\3\2\2\2\u0274\u0277")
        buf.write("\3\2\2\2\u0275\u0273\3\2\2\2\u0275\u0276\3\2\2\2\u0276")
        buf.write("m\3\2\2\2\u0277\u0275\3\2\2\2\u0278\u027a\7\60\2\2\u0279")
        buf.write("\u027b\5> \2\u027a\u0279\3\2\2\2\u027b\u027c\3\2\2\2\u027c")
        buf.write("\u027a\3\2\2\2\u027c\u027d\3\2\2\2\u027d\u027e\3\2\2\2")
        buf.write("\u027e\u027f\7\61\2\2\u027fo\3\2\2\2\u0280\u0282\7\62")
        buf.write("\2\2\u0281\u0283\5*\26\2\u0282\u0281\3\2\2\2\u0282\u0283")
        buf.write("\3\2\2\2\u0283\u0284\3\2\2\2\u0284\u0286\7\63\2\2\u0285")
        buf.write("\u0280\3\2\2\2\u0286\u0287\3\2\2\2\u0287\u0285\3\2\2\2")
        buf.write("\u0287\u0288\3\2\2\2\u0288q\3\2\2\2Hu\u008c\u0094\u009b")
        buf.write("\u00a2\u00a7\u00ae\u00b1\u00b9\u00bf\u00c4\u00ca\u00cd")
        buf.write("\u00d3\u00dc\u00eb\u00ee\u00f4\u00fe\u0105\u010f\u0117")
        buf.write("\u011a\u0120\u0129\u0131\u0138\u0141\u0149\u0151\u0159")
        buf.write("\u0161\u0167\u017a\u017d\u017f\u0189\u01ae\u01ba\u01c5")
        buf.write("\u01c9\u01cb\u01ce\u01d7\u01e0\u01e4\u01e6\u01ed\u01f8")
        buf.write("\u0201\u0206\u020c\u0210\u0212\u0217\u021f\u0226\u022a")
        buf.write("\u022f\u0234\u023f\u0259\u025f\u0266\u0268\u026e\u0275")
        buf.write("\u027c\u0282\u0287")
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
    RULE_arrayLit = 31
    RULE_arraysBlock = 32
    RULE_literals = 33
    RULE_structLit = 34
    RULE_structBlock = 35
    RULE_structFieldsAssign = 36
    RULE_assignStatement = 37
    RULE_a1 = 38
    RULE_a2 = 39
    RULE_assignmentOperator = 40
    RULE_ifStatement = 41
    RULE_forStatement = 42
    RULE_forLoop = 43
    RULE_initilization = 44
    RULE_forCondition = 45
    RULE_forUpdate = 46
    RULE_forIteration = 47
    RULE_breakStatement = 48
    RULE_continueStatement = 49
    RULE_primaryCall = 50
    RULE_callStatement = 51
    RULE_returnStatement = 52
    RULE_arguments = 53
    RULE_block = 54
    RULE_arrayDims = 55

    ruleNames =  [ "program", "baseType", "endOfStatement", "declaration", 
                   "varDecl", "arrayDecl", "arrayLitDecl", "assignDecl", 
                   "funcDecl", "typeDecl", "constDecl", "methodDecl", "structDefinition", 
                   "structFields", "interfaceDefinition", "interfaceFields", 
                   "listParams", "listIdentifier", "listGroup", "funcParam", 
                   "expression", "logicOrExp", "logicAndExp", "equalityExp", 
                   "additiveExp", "multiplicativeExp", "unaryExp", "postfixExp", 
                   "primaryExp", "literal", "statement", "arrayLit", "arraysBlock", 
                   "literals", "structLit", "structBlock", "structFieldsAssign", 
                   "assignStatement", "a1", "a2", "assignmentOperator", 
                   "ifStatement", "forStatement", "forLoop", "initilization", 
                   "forCondition", "forUpdate", "forIteration", "breakStatement", 
                   "continueStatement", "primaryCall", "callStatement", 
                   "returnStatement", "arguments", "block", "arrayDims" ]

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
            self.state = 113 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 112
                self.declaration()
                self.state = 115 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 117
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
            self.state = 119
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
            self.state = 121
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
        self.enterRule(localctx, 6, self.RULE_declaration)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.varDecl()
                self.state = 124
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.funcDecl()
                self.state = 127
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.typeDecl()
                self.state = 130
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.constDecl()
                self.state = 133
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 135
                self.methodDecl()
                self.state = 136
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


        def assignDecl(self):
            return self.getTypedRuleContext(MiniGoParser.AssignDeclContext,0)


        def arrayDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDeclContext,0)


        def arrayLitDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitDeclContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

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
            self.state = 140
            self.match(MiniGoParser.VAR)
            self.state = 141
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 142
                self.match(MiniGoParser.COMMA)
                self.state = 143
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 149
                self.baseType()
                pass

            elif la_ == 2:
                self.state = 150
                self.assignDecl()
                pass

            elif la_ == 3:
                self.state = 151
                self.arrayDecl()
                pass

            elif la_ == 4:
                self.state = 152
                self.arrayLitDecl()
                pass


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

        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


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

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def arraysBlock(self):
            return self.getTypedRuleContext(MiniGoParser.ArraysBlockContext,0)


        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INT_LIT)
            else:
                return self.getToken(MiniGoParser.INT_LIT, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

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
            self.state = 158 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 155
                self.match(MiniGoParser.LBRACKET)
                self.state = 156
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.IDENTIFIER or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 157
                self.match(MiniGoParser.RBRACKET)
                self.state = 160 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LBRACKET):
                    break

            self.state = 162
            self.baseType()
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ASSIGN:
                self.state = 163
                self.match(MiniGoParser.ASSIGN)
                self.state = 164
                self.arraysBlock()


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

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INT_LIT)
            else:
                return self.getToken(MiniGoParser.INT_LIT, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

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
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 170 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 167
                    self.match(MiniGoParser.LBRACKET)
                    self.state = 168
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.IDENTIFIER or _la==MiniGoParser.INT_LIT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 169
                    self.match(MiniGoParser.RBRACKET)
                    self.state = 172 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==MiniGoParser.LBRACKET):
                        break

                self.state = 174
                self.baseType()


            self.state = 177
            self.match(MiniGoParser.ASSIGN)
            self.state = 181 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 178
                self.match(MiniGoParser.LBRACKET)
                self.state = 179
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.IDENTIFIER or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 180
                self.match(MiniGoParser.RBRACKET)
                self.state = 183 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.LBRACKET):
                    break

            self.state = 185
            self.baseType()
            self.state = 186
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


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


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
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 188
                self.baseType()


            self.state = 191
            self.match(MiniGoParser.ASSIGN)
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 192
                self.expression()
                pass

            elif la_ == 2:
                self.state = 193
                self.structLit()
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


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

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
        self.enterRule(localctx, 16, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(MiniGoParser.FUNC)
            self.state = 197
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 198
            self.listParams()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACKET:
                    self.state = 199
                    self.arrayDims()


                self.state = 202
                self.baseType()


            self.state = 205
            self.match(MiniGoParser.LBRACE)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 206
                self.statement()
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
            self.state = 214
            self.match(MiniGoParser.TYPE)
            self.state = 215
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.state = 216
                self.structDefinition()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 217
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
            self.state = 220
            self.match(MiniGoParser.CONST)
            self.state = 221
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 222
            self.match(MiniGoParser.ASSIGN)
            self.state = 223
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


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

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
            self.state = 225
            self.match(MiniGoParser.FUNC)
            self.state = 226
            self.match(MiniGoParser.LPAREN)
            self.state = 227
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 228
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 229
            self.match(MiniGoParser.RPAREN)
            self.state = 230
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 231
            self.listParams()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACKET:
                    self.state = 232
                    self.arrayDims()


                self.state = 235
                self.baseType()


            self.state = 238
            self.match(MiniGoParser.LBRACE)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 239
                self.statement()
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 245
            self.match(MiniGoParser.RBRACE)
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
            self.state = 247
            self.match(MiniGoParser.STRUCT)
            self.state = 248
            self.match(MiniGoParser.LBRACE)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 249
                self.structFields()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 255
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
            self.state = 257
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 258
                self.arrayDims()


            self.state = 261
            self.baseType()
            self.state = 262
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
            self.state = 264
            self.match(MiniGoParser.INTERFACE)
            self.state = 265
            self.match(MiniGoParser.LBRACE)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 266
                self.interfaceFields()
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 272
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
            self.state = 274
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 275
            self.listParams()
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACKET:
                    self.state = 276
                    self.arrayDims()


                self.state = 279
                self.baseType()


            self.state = 282
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
            self.state = 284
            self.match(MiniGoParser.LPAREN)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 285
                self.listIdentifier()


            self.state = 288
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
            self.state = 290
            self.listGroup()
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 291
                self.match(MiniGoParser.COMMA)
                self.state = 292
                self.listGroup()
                self.state = 297
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
            self.state = 298
            self.funcParam()
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 299
                self.match(MiniGoParser.COMMA)
                self.state = 300
                self.funcParam()
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 306
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
            self.state = 308
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 309
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
            self.state = 312
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
        self.enterRule(localctx, 42, self.RULE_logicOrExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.logicAndExp()
            self.state = 319
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 315
                    self.match(MiniGoParser.OR)
                    self.state = 316
                    self.logicOrExp() 
                self.state = 321
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        self.enterRule(localctx, 44, self.RULE_logicAndExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.equalityExp()
            self.state = 327
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 323
                    self.match(MiniGoParser.AND)
                    self.state = 324
                    self.logicAndExp() 
                self.state = 329
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
            self.state = 330
            self.additiveExp()
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LEQ) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GEQ))) != 0):
                self.state = 331
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LEQ) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 332
                self.additiveExp()
                self.state = 337
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
            self.state = 338
            self.multiplicativeExp()
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS:
                self.state = 339
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 340
                self.multiplicativeExp()
                self.state = 345
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
            self.state = 346
            self.unaryExp()
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0):
                self.state = 347
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 348
                self.unaryExp()
                self.state = 353
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
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.MINUS or _la==MiniGoParser.NOT:
                self.state = 354
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 359
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 360
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
            self.state = 363
            self.primaryExp()
            self._ctx.stop = self._input.LT(-1)
            self.state = 381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 379
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.PostfixExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExp)
                        self.state = 365
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 366
                        self.match(MiniGoParser.LBRACKET)
                        self.state = 367
                        self.expression()
                        self.state = 368
                        self.match(MiniGoParser.RBRACKET)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.PostfixExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExp)
                        self.state = 370
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 371
                        self.match(MiniGoParser.DOT)
                        self.state = 372
                        self.match(MiniGoParser.IDENTIFIER)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.PostfixExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExp)
                        self.state = 373
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 374
                        self.match(MiniGoParser.LPAREN)
                        self.state = 376
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                            self.state = 375
                            self.arguments()


                        self.state = 378
                        self.match(MiniGoParser.RPAREN)
                        pass

             
                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.match(MiniGoParser.LPAREN)
                self.state = 385
                self.expression()
                self.state = 386
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 389
                self.callStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 390
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
            self.state = 393
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
            self.state = 428
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.assignStatement()
                self.state = 396
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.ifStatement()
                self.state = 399
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 401
                self.forStatement()
                self.state = 402
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 404
                self.breakStatement()
                self.state = 405
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 407
                self.continueStatement()
                self.state = 408
                self.endOfStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 410
                self.callStatement()
                self.state = 411
                self.endOfStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 413
                self.returnStatement()
                self.state = 414
                self.endOfStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 416
                self.varDecl()
                self.state = 417
                self.endOfStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 419
                self.typeDecl()
                self.state = 420
                self.endOfStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 422
                self.methodDecl()
                self.state = 423
                self.endOfStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 425
                self.constDecl()
                self.state = 426
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
        self.enterRule(localctx, 62, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.arrayDims()
            self.state = 431
            self.baseType()
            self.state = 432
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

        def literals(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.LiteralsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.LiteralsContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arraysBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraysBlock" ):
                return visitor.visitArraysBlock(self)
            else:
                return visitor.visitChildren(self)




    def arraysBlock(self):

        localctx = MiniGoParser.ArraysBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_arraysBlock)
        self._la = 0 # Token type
        try:
            self.state = 460
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.match(MiniGoParser.LBRACE)
                self.state = 435
                self.arraysBlock()
                self.state = 440
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 436
                    self.match(MiniGoParser.COMMA)
                    self.state = 437
                    self.arraysBlock()
                    self.state = 442
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 443
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.match(MiniGoParser.LBRACE)
                self.state = 457
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 446
                    self.literals()
                    self.state = 451
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 447
                            self.match(MiniGoParser.COMMA)
                            self.state = 448
                            self.literals() 
                        self.state = 453
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

                    self.state = 455
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MiniGoParser.COMMA:
                        self.state = 454
                        self.match(MiniGoParser.COMMA)




                self.state = 459
                self.match(MiniGoParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
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

        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = MiniGoParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_literals)
        try:
            self.state = 469
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 464
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 465
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 466
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 467
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 7)
                self.state = 468
                self.structLit()
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


    class StructLitContext(ParserRuleContext):
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

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructLit" ):
                return visitor.visitStructLit(self)
            else:
                return visitor.visitChildren(self)




    def structLit(self):

        localctx = MiniGoParser.StructLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_structLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 472
            self.match(MiniGoParser.LBRACE)
            self.state = 484
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 473
                self.structFieldsAssign()
                self.state = 478
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 474
                        self.match(MiniGoParser.COMMA)
                        self.state = 475
                        self.structFieldsAssign() 
                    self.state = 480
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

                self.state = 482
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.COMMA or _la==MiniGoParser.NEWLINE:
                    self.state = 481
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.COMMA or _la==MiniGoParser.NEWLINE):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()




            self.state = 486
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


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructBlock" ):
                return visitor.visitStructBlock(self)
            else:
                return visitor.visitChildren(self)




    def structBlock(self):

        localctx = MiniGoParser.StructBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_structBlock)
        try:
            self.state = 491
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 490
                self.structLit()
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
        self.enterRule(localctx, 72, self.RULE_structFieldsAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 494
            self.match(MiniGoParser.COLON)
            self.state = 495
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
        self.enterRule(localctx, 74, self.RULE_assignStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.a1()
            self.state = 502
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 498
                self.match(MiniGoParser.COMMA)
                self.state = 499
                self.a1()
                self.state = 504
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 505
            self.assignmentOperator()
            self.state = 506
            self.a2()
            self.state = 511
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 507
                self.match(MiniGoParser.COMMA)
                self.state = 508
                self.a2()
                self.state = 513
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
        self.enterRule(localctx, 76, self.RULE_a1)
        self._la = 0 # Token type
        try:
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                if la_ == 1:
                    self.state = 514
                    self.callStatement()
                    pass

                elif la_ == 2:
                    self.state = 515
                    self.match(MiniGoParser.IDENTIFIER)
                    pass


                self.state = 518
                self.match(MiniGoParser.DOT)
                self.state = 519
                self.a1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 520
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 522
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACKET:
                    self.state = 521
                    self.arrayDims()


                self.state = 526
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.DOT:
                    self.state = 524
                    self.match(MiniGoParser.DOT)
                    self.state = 525
                    self.a1()


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


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_a2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA2" ):
                return visitor.visitA2(self)
            else:
                return visitor.visitChildren(self)




    def a2(self):

        localctx = MiniGoParser.A2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_a2)
        try:
            self.state = 533
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 532
                self.structLit()
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
        self.enterRule(localctx, 80, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
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
        self.enterRule(localctx, 82, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(MiniGoParser.IF)
            self.state = 538
            self.expression()
            self.state = 539
            self.block()
            self.state = 541
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.state = 540
                self.match(MiniGoParser.NEWLINE)


            self.state = 552
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 543
                    self.match(MiniGoParser.ELSE)
                    self.state = 544
                    self.match(MiniGoParser.IF)
                    self.state = 545
                    self.expression()
                    self.state = 546
                    self.block()
                    self.state = 548
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                    if la_ == 1:
                        self.state = 547
                        self.match(MiniGoParser.NEWLINE)

             
                self.state = 554
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

            self.state = 557
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 555
                self.match(MiniGoParser.ELSE)
                self.state = 556
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
        self.enterRule(localctx, 84, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.match(MiniGoParser.FOR)
            self.state = 562
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.state = 560
                self.forLoop()
                pass

            elif la_ == 2:
                self.state = 561
                self.forIteration()
                pass


            self.state = 564
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
        self.enterRule(localctx, 86, self.RULE_forLoop)
        try:
            self.state = 573
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 566
                self.forCondition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 567
                self.initilization()
                self.state = 568
                self.match(MiniGoParser.SEMI)
                self.state = 569
                self.forCondition()
                self.state = 570
                self.match(MiniGoParser.SEMI)
                self.state = 571
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
        self.enterRule(localctx, 88, self.RULE_initilization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 575
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 576
            self.match(MiniGoParser.DECLARE)
            self.state = 577
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
        self.enterRule(localctx, 90, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
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
        self.enterRule(localctx, 92, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 582
            self.assignmentOperator()
            self.state = 583
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
        self.enterRule(localctx, 94, self.RULE_forIteration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.BLANK or _la==MiniGoParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 586
            self.match(MiniGoParser.COMMA)
            self.state = 587
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 588
            self.match(MiniGoParser.DECLARE)
            self.state = 589
            self.match(MiniGoParser.RANGE)
            self.state = 590
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
        self.enterRule(localctx, 96, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
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
        self.enterRule(localctx, 98, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
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
        self.enterRule(localctx, 100, self.RULE_primaryCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 597
            self.match(MiniGoParser.LPAREN)
            self.state = 599
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 598
                self.arguments()


            self.state = 601
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
        self.enterRule(localctx, 102, self.RULE_callStatement)
        self._la = 0 # Token type
        try:
            self.state = 614
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 603
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 605
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACKET:
                    self.state = 604
                    self.arrayDims()


                self.state = 607
                self.match(MiniGoParser.DOT)
                self.state = 608
                self.callStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 609
                self.primaryCall()
                self.state = 612
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                if la_ == 1:
                    self.state = 610
                    self.match(MiniGoParser.DOT)
                    self.state = 611
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


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MiniGoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 616
            self.match(MiniGoParser.RETURN)
            self.state = 620
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 617
                self.expression()

            elif la_ == 2:
                self.state = 618
                self.arrayLit()

            elif la_ == 3:
                self.state = 619
                self.structLit()


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
        self.enterRule(localctx, 106, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self.expression()
            self.state = 627
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 623
                self.match(MiniGoParser.COMMA)
                self.state = 624
                self.expression()
                self.state = 629
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
        self.enterRule(localctx, 108, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 630
            self.match(MiniGoParser.LBRACE)
            self.state = 632 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 631
                self.statement()
                self.state = 634 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                    break

            self.state = 636
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
        self.enterRule(localctx, 110, self.RULE_arrayDims)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 638
                self.match(MiniGoParser.LBRACKET)
                self.state = 640
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 639
                    self.expression()


                self.state = 642
                self.match(MiniGoParser.RBRACKET)
                self.state = 645 
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
         




