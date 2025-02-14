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
        buf.write("\u02d3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\3\2\6\2\u0092\n\2\r\2\16\2\u0093")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3\u00a7\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\5\5\u00b2\n\5\3\6\3\6\3\6\3\6\5\6\u00b8\n\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00c3\n\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\5\b\u00cb\n\b\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\5\r\u00e1\n\r\3\16\3\16\5\16\u00e5\n\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\5\20\u00ee\n\20\3\21\3")
        buf.write("\21\3\21\3\22\3\22\3\22\3\22\3\22\5\22\u00f8\n\22\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\5\24\u0101\n\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\7\25\u010f\n\25\f\25\16\25\u0112\13\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u011e\n\26\f")
        buf.write("\26\16\26\u0121\13\26\3\26\3\26\3\27\3\27\3\27\3\27\3")
        buf.write("\27\5\27\u012a\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\5\30\u0135\n\30\3\31\3\31\3\31\3\31\5\31\u013b")
        buf.write("\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0145")
        buf.write("\n\32\3\33\3\33\3\33\3\33\5\33\u014b\n\33\3\34\3\34\3")
        buf.write("\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\5\35\u015a\n\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\5\37\u0169\n\37\3 \3 \3!")
        buf.write("\3!\3!\3!\3!\3!\7!\u0173\n!\f!\16!\u0176\13!\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\7\"\u017e\n\"\f\"\16\"\u0181\13\"\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\7#\u018a\n#\f#\16#\u018d\13#\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\7$\u0196\n$\f$\16$\u0199\13$\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\7%\u01a2\n%\f%\16%\u01a5\13%\3&\3&\3&\3&\5")
        buf.write("&\u01ab\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\7\'\u01b8\n\'\f\'\16\'\u01bb\13\'\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\5")
        buf.write("(\u01d5\n(\3)\3)\5)\u01d9\n)\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\5*\u01f3")
        buf.write("\n*\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u0201\n,\3")
        buf.write("-\3-\3-\5-\u0206\n-\3.\3.\3.\3.\3.\3.\7.\u020e\n.\f.\16")
        buf.write(".\u0211\13.\3.\3.\3.\3.\3.\3.\3.\3.\7.\u021b\n.\f.\16")
        buf.write(".\u021e\13.\3.\3.\3.\3.\3.\7.\u0225\n.\f.\16.\u0228\13")
        buf.write(".\3.\3.\5.\u022c\n.\3/\3/\3/\3/\3/\3/\3/\7/\u0235\n/\f")
        buf.write("/\16/\u0238\13/\3/\3/\3/\3/\5/\u023e\n/\3\60\3\60\5\60")
        buf.write("\u0242\n\60\3\61\3\61\3\61\3\61\7\61\u0248\n\61\f\61\16")
        buf.write("\61\u024b\13\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\7\61\u0257\n\61\f\61\16\61\u025a\13\61\3\61")
        buf.write("\3\61\5\61\u025e\n\61\3\62\3\62\3\63\3\63\5\63\u0264\n")
        buf.write("\63\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\7\65\u0271\n\65\f\65\16\65\u0274\13\65\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\38\38\38\38\38\38\38\38\38")
        buf.write("\38\38\38\38\38\38\58\u028d\n8\39\39\39\39\39\39\59\u0295")
        buf.write("\n9\3:\3:\3:\3:\3:\3:\5:\u029d\n:\3;\3;\3;\3<\3<\3<\3")
        buf.write("<\5<\u02a6\n<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3")
        buf.write("C\3D\3D\3D\3D\3D\3D\3D\3D\5D\u02be\nD\3E\3E\3E\3E\3E\3")
        buf.write("E\3E\3E\3E\3E\3E\5E\u02cb\nE\3F\3F\3G\3G\3H\3H\3H\2\b")
        buf.write("@BDFHLI\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(",.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write("\u0082\u0084\u0086\u0088\u008a\u008c\u008e\2\n\4\2--\67")
        buf.write("\67\3\2\36#\3\2\31\32\3\2\33\35\4\2\32\32&&\3\2\678\4")
        buf.write("\2\13\16\67\67\4\2\65\65>>\2\u02e2\2\u0091\3\2\2\2\4\u00a6")
        buf.write("\3\2\2\2\6\u00a8\3\2\2\2\b\u00b1\3\2\2\2\n\u00b7\3\2\2")
        buf.write("\2\f\u00c2\3\2\2\2\16\u00ca\3\2\2\2\20\u00cc\3\2\2\2\22")
        buf.write("\u00d0\3\2\2\2\24\u00d4\3\2\2\2\26\u00d8\3\2\2\2\30\u00e0")
        buf.write("\3\2\2\2\32\u00e4\3\2\2\2\34\u00e6\3\2\2\2\36\u00ed\3")
        buf.write("\2\2\2 \u00ef\3\2\2\2\"\u00f7\3\2\2\2$\u00f9\3\2\2\2&")
        buf.write("\u0100\3\2\2\2(\u0102\3\2\2\2*\u0115\3\2\2\2,\u0129\3")
        buf.write("\2\2\2.\u0134\3\2\2\2\60\u013a\3\2\2\2\62\u0144\3\2\2")
        buf.write("\2\64\u014a\3\2\2\2\66\u014c\3\2\2\28\u0159\3\2\2\2:\u015b")
        buf.write("\3\2\2\2<\u0168\3\2\2\2>\u016a\3\2\2\2@\u016c\3\2\2\2")
        buf.write("B\u0177\3\2\2\2D\u0182\3\2\2\2F\u018e\3\2\2\2H\u019a\3")
        buf.write("\2\2\2J\u01aa\3\2\2\2L\u01ac\3\2\2\2N\u01d4\3\2\2\2P\u01d8")
        buf.write("\3\2\2\2R\u01f2\3\2\2\2T\u01f4\3\2\2\2V\u0200\3\2\2\2")
        buf.write("X\u0205\3\2\2\2Z\u022b\3\2\2\2\\\u023d\3\2\2\2^\u0241")
        buf.write("\3\2\2\2`\u025d\3\2\2\2b\u025f\3\2\2\2d\u0263\3\2\2\2")
        buf.write("f\u0265\3\2\2\2h\u0267\3\2\2\2j\u0277\3\2\2\2l\u0279\3")
        buf.write("\2\2\2n\u028c\3\2\2\2p\u0294\3\2\2\2r\u029c\3\2\2\2t\u029e")
        buf.write("\3\2\2\2v\u02a5\3\2\2\2x\u02a7\3\2\2\2z\u02a9\3\2\2\2")
        buf.write("|\u02ab\3\2\2\2~\u02ad\3\2\2\2\u0080\u02af\3\2\2\2\u0082")
        buf.write("\u02b1\3\2\2\2\u0084\u02b3\3\2\2\2\u0086\u02bd\3\2\2\2")
        buf.write("\u0088\u02ca\3\2\2\2\u008a\u02cc\3\2\2\2\u008c\u02ce\3")
        buf.write("\2\2\2\u008e\u02d0\3\2\2\2\u0090\u0092\5\4\3\2\u0091\u0090")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0091\3\2\2\2\u0093")
        buf.write("\u0094\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0096\7\2\2\3")
        buf.write("\u0096\3\3\2\2\2\u0097\u0098\5\6\4\2\u0098\u0099\5\u008e")
        buf.write("H\2\u0099\u00a7\3\2\2\2\u009a\u009b\5*\26\2\u009b\u009c")
        buf.write("\5\u008eH\2\u009c\u00a7\3\2\2\2\u009d\u009e\5\20\t\2\u009e")
        buf.write("\u009f\5\u008eH\2\u009f\u00a7\3\2\2\2\u00a0\u00a1\5(\25")
        buf.write("\2\u00a1\u00a2\5\u008eH\2\u00a2\u00a7\3\2\2\2\u00a3\u00a4")
        buf.write("\5\62\32\2\u00a4\u00a5\5\u008eH\2\u00a5\u00a7\3\2\2\2")
        buf.write("\u00a6\u0097\3\2\2\2\u00a6\u009a\3\2\2\2\u00a6\u009d\3")
        buf.write("\2\2\2\u00a6\u00a0\3\2\2\2\u00a6\u00a3\3\2\2\2\u00a7\5")
        buf.write("\3\2\2\2\u00a8\u00a9\7\23\2\2\u00a9\u00aa\7\67\2\2\u00aa")
        buf.write("\u00ab\5\b\5\2\u00ab\7\3\2\2\2\u00ac\u00ad\5\n\6\2\u00ad")
        buf.write("\u00ae\5\16\b\2\u00ae\u00b2\3\2\2\2\u00af\u00b2\5\n\6")
        buf.write("\2\u00b0\u00b2\5\16\b\2\u00b1\u00ac\3\2\2\2\u00b1\u00af")
        buf.write("\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\t\3\2\2\2\u00b3\u00b8")
        buf.write("\5\u008cG\2\u00b4\u00b5\5\f\7\2\u00b5\u00b6\5\u008cG\2")
        buf.write("\u00b6\u00b8\3\2\2\2\u00b7\u00b3\3\2\2\2\u00b7\u00b4\3")
        buf.write("\2\2\2\u00b8\13\3\2\2\2\u00b9\u00ba\7\62\2\2\u00ba\u00bb")
        buf.write("\5\u008aF\2\u00bb\u00bc\7\63\2\2\u00bc\u00bd\5\f\7\2\u00bd")
        buf.write("\u00c3\3\2\2\2\u00be\u00bf\7\62\2\2\u00bf\u00c0\5\u008a")
        buf.write("F\2\u00c0\u00c1\7\63\2\2\u00c1\u00c3\3\2\2\2\u00c2\u00b9")
        buf.write("\3\2\2\2\u00c2\u00be\3\2\2\2\u00c3\r\3\2\2\2\u00c4\u00c5")
        buf.write("\7\27\2\2\u00c5\u00cb\5> \2\u00c6\u00c7\7\27\2\2\u00c7")
        buf.write("\u00cb\5\22\n\2\u00c8\u00c9\7\27\2\2\u00c9\u00cb\5\34")
        buf.write("\17\2\u00ca\u00c4\3\2\2\2\u00ca\u00c6\3\2\2\2\u00ca\u00c8")
        buf.write("\3\2\2\2\u00cb\17\3\2\2\2\u00cc\u00cd\7\22\2\2\u00cd\u00ce")
        buf.write("\7\67\2\2\u00ce\u00cf\5\16\b\2\u00cf\21\3\2\2\2\u00d0")
        buf.write("\u00d1\5\f\7\2\u00d1\u00d2\5\u008cG\2\u00d2\u00d3\5\24")
        buf.write("\13\2\u00d3\23\3\2\2\2\u00d4\u00d5\7\60\2\2\u00d5\u00d6")
        buf.write("\5\26\f\2\u00d6\u00d7\7\61\2\2\u00d7\25\3\2\2\2\u00d8")
        buf.write("\u00d9\5\32\16\2\u00d9\u00da\5\30\r\2\u00da\27\3\2\2\2")
        buf.write("\u00db\u00dc\7\64\2\2\u00dc\u00dd\5\32\16\2\u00dd\u00de")
        buf.write("\5\30\r\2\u00de\u00e1\3\2\2\2\u00df\u00e1\3\2\2\2\u00e0")
        buf.write("\u00db\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1\31\3\2\2\2\u00e2")
        buf.write("\u00e5\5\24\13\2\u00e3\u00e5\5\u0086D\2\u00e4\u00e2\3")
        buf.write("\2\2\2\u00e4\u00e3\3\2\2\2\u00e5\33\3\2\2\2\u00e6\u00e7")
        buf.write("\7\67\2\2\u00e7\u00e8\7\60\2\2\u00e8\u00e9\5\36\20\2\u00e9")
        buf.write("\u00ea\7\61\2\2\u00ea\35\3\2\2\2\u00eb\u00ee\5 \21\2\u00ec")
        buf.write("\u00ee\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ec\3\2\2\2")
        buf.write("\u00ee\37\3\2\2\2\u00ef\u00f0\5$\23\2\u00f0\u00f1\5\"")
        buf.write("\22\2\u00f1!\3\2\2\2\u00f2\u00f3\7\64\2\2\u00f3\u00f4")
        buf.write("\5$\23\2\u00f4\u00f5\5\"\22\2\u00f5\u00f8\3\2\2\2\u00f6")
        buf.write("\u00f8\3\2\2\2\u00f7\u00f2\3\2\2\2\u00f7\u00f6\3\2\2\2")
        buf.write("\u00f8#\3\2\2\2\u00f9\u00fa\7\67\2\2\u00fa\u00fb\7\66")
        buf.write("\2\2\u00fb\u00fc\5&\24\2\u00fc%\3\2\2\2\u00fd\u0101\5")
        buf.write("> \2\u00fe\u0101\5\22\n\2\u00ff\u0101\5\34\17\2\u0100")
        buf.write("\u00fd\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u00ff\3\2\2\2")
        buf.write("\u0101\'\3\2\2\2\u0102\u0103\7\7\2\2\u0103\u0104\7.\2")
        buf.write("\2\u0104\u0105\7\67\2\2\u0105\u0106\7\67\2\2\u0106\u0107")
        buf.write("\7/\2\2\u0107\u0108\7\67\2\2\u0108\u0109\7.\2\2\u0109")
        buf.write("\u010a\5.\30\2\u010a\u010b\7/\2\2\u010b\u010c\5,\27\2")
        buf.write("\u010c\u0110\7\60\2\2\u010d\u010f\5N(\2\u010e\u010d\3")
        buf.write("\2\2\2\u010f\u0112\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u0111")
        buf.write("\3\2\2\2\u0111\u0113\3\2\2\2\u0112\u0110\3\2\2\2\u0113")
        buf.write("\u0114\7\61\2\2\u0114)\3\2\2\2\u0115\u0116\7\7\2\2\u0116")
        buf.write("\u0117\7\67\2\2\u0117\u0118\7.\2\2\u0118\u0119\5.\30\2")
        buf.write("\u0119\u011a\7/\2\2\u011a\u011b\5,\27\2\u011b\u011f\7")
        buf.write("\60\2\2\u011c\u011e\5N(\2\u011d\u011c\3\2\2\2\u011e\u0121")
        buf.write("\3\2\2\2\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120")
        buf.write("\u0122\3\2\2\2\u0121\u011f\3\2\2\2\u0122\u0123\7\61\2")
        buf.write("\2\u0123+\3\2\2\2\u0124\u012a\5\u008cG\2\u0125\u0126\5")
        buf.write("\f\7\2\u0126\u0127\5\u008cG\2\u0127\u012a\3\2\2\2\u0128")
        buf.write("\u012a\3\2\2\2\u0129\u0124\3\2\2\2\u0129\u0125\3\2\2\2")
        buf.write("\u0129\u0128\3\2\2\2\u012a-\3\2\2\2\u012b\u012c\5\60\31")
        buf.write("\2\u012c\u012d\5\n\6\2\u012d\u012e\7\64\2\2\u012e\u012f")
        buf.write("\5.\30\2\u012f\u0135\3\2\2\2\u0130\u0131\5\60\31\2\u0131")
        buf.write("\u0132\5\n\6\2\u0132\u0135\3\2\2\2\u0133\u0135\3\2\2\2")
        buf.write("\u0134\u012b\3\2\2\2\u0134\u0130\3\2\2\2\u0134\u0133\3")
        buf.write("\2\2\2\u0135/\3\2\2\2\u0136\u013b\7\67\2\2\u0137\u0138")
        buf.write("\7\67\2\2\u0138\u0139\7\64\2\2\u0139\u013b\5\60\31\2\u013a")
        buf.write("\u0136\3\2\2\2\u013a\u0137\3\2\2\2\u013b\61\3\2\2\2\u013c")
        buf.write("\u013d\7\b\2\2\u013d\u013e\7\67\2\2\u013e\u013f\7\t\2")
        buf.write("\2\u013f\u0145\5\66\34\2\u0140\u0141\7\b\2\2\u0141\u0142")
        buf.write("\7\67\2\2\u0142\u0143\7\n\2\2\u0143\u0145\5:\36\2\u0144")
        buf.write("\u013c\3\2\2\2\u0144\u0140\3\2\2\2\u0145\63\3\2\2\2\u0146")
        buf.write("\u014b\5\u008cG\2\u0147\u0148\5\f\7\2\u0148\u0149\5\u008c")
        buf.write("G\2\u0149\u014b\3\2\2\2\u014a\u0146\3\2\2\2\u014a\u0147")
        buf.write("\3\2\2\2\u014b\65\3\2\2\2\u014c\u014d\7\60\2\2\u014d\u014e")
        buf.write("\58\35\2\u014e\u014f\7\61\2\2\u014f\67\3\2\2\2\u0150\u0151")
        buf.write("\7\67\2\2\u0151\u0152\5\64\33\2\u0152\u0153\5\u008eH\2")
        buf.write("\u0153\u0154\58\35\2\u0154\u015a\3\2\2\2\u0155\u0156\7")
        buf.write("\67\2\2\u0156\u0157\5\64\33\2\u0157\u0158\5\u008eH\2\u0158")
        buf.write("\u015a\3\2\2\2\u0159\u0150\3\2\2\2\u0159\u0155\3\2\2\2")
        buf.write("\u015a9\3\2\2\2\u015b\u015c\7\60\2\2\u015c\u015d\5<\37")
        buf.write("\2\u015d\u015e\7\61\2\2\u015e;\3\2\2\2\u015f\u0160\7\67")
        buf.write("\2\2\u0160\u0161\7.\2\2\u0161\u0162\5.\30\2\u0162\u0163")
        buf.write("\7/\2\2\u0163\u0164\5,\27\2\u0164\u0165\5\u008eH\2\u0165")
        buf.write("\u0166\5<\37\2\u0166\u0169\3\2\2\2\u0167\u0169\3\2\2\2")
        buf.write("\u0168\u015f\3\2\2\2\u0168\u0167\3\2\2\2\u0169=\3\2\2")
        buf.write("\2\u016a\u016b\5@!\2\u016b?\3\2\2\2\u016c\u016d\b!\1\2")
        buf.write("\u016d\u016e\5B\"\2\u016e\u0174\3\2\2\2\u016f\u0170\f")
        buf.write("\4\2\2\u0170\u0171\7%\2\2\u0171\u0173\5B\"\2\u0172\u016f")
        buf.write("\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174")
        buf.write("\u0175\3\2\2\2\u0175A\3\2\2\2\u0176\u0174\3\2\2\2\u0177")
        buf.write("\u0178\b\"\1\2\u0178\u0179\5D#\2\u0179\u017f\3\2\2\2\u017a")
        buf.write("\u017b\f\4\2\2\u017b\u017c\7$\2\2\u017c\u017e\5D#\2\u017d")
        buf.write("\u017a\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u017f\u0180\3\2\2\2\u0180C\3\2\2\2\u0181\u017f\3\2\2")
        buf.write("\2\u0182\u0183\b#\1\2\u0183\u0184\5F$\2\u0184\u018b\3")
        buf.write("\2\2\2\u0185\u0186\f\4\2\2\u0186\u0187\5~@\2\u0187\u0188")
        buf.write("\5F$\2\u0188\u018a\3\2\2\2\u0189\u0185\3\2\2\2\u018a\u018d")
        buf.write("\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018c")
        buf.write("E\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u018f\b$\1\2\u018f")
        buf.write("\u0190\5H%\2\u0190\u0197\3\2\2\2\u0191\u0192\f\4\2\2\u0192")
        buf.write("\u0193\5\u0080A\2\u0193\u0194\5H%\2\u0194\u0196\3\2\2")
        buf.write("\2\u0195\u0191\3\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195")
        buf.write("\3\2\2\2\u0197\u0198\3\2\2\2\u0198G\3\2\2\2\u0199\u0197")
        buf.write("\3\2\2\2\u019a\u019b\b%\1\2\u019b\u019c\5J&\2\u019c\u01a3")
        buf.write("\3\2\2\2\u019d\u019e\f\4\2\2\u019e\u019f\5\u0082B\2\u019f")
        buf.write("\u01a0\5J&\2\u01a0\u01a2\3\2\2\2\u01a1\u019d\3\2\2\2\u01a2")
        buf.write("\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a4I\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01a7\5\u0084")
        buf.write("C\2\u01a7\u01a8\5J&\2\u01a8\u01ab\3\2\2\2\u01a9\u01ab")
        buf.write("\5L\'\2\u01aa\u01a6\3\2\2\2\u01aa\u01a9\3\2\2\2\u01ab")
        buf.write("K\3\2\2\2\u01ac\u01ad\b\'\1\2\u01ad\u01ae\5\u0088E\2\u01ae")
        buf.write("\u01b9\3\2\2\2\u01af\u01b0\f\5\2\2\u01b0\u01b1\7,\2\2")
        buf.write("\u01b1\u01b8\7\67\2\2\u01b2\u01b3\f\4\2\2\u01b3\u01b4")
        buf.write("\7\62\2\2\u01b4\u01b5\5> \2\u01b5\u01b6\7\63\2\2\u01b6")
        buf.write("\u01b8\3\2\2\2\u01b7\u01af\3\2\2\2\u01b7\u01b2\3\2\2\2")
        buf.write("\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3")
        buf.write("\2\2\2\u01baM\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bc\u01bd")
        buf.write("\5P)\2\u01bd\u01be\5\u008eH\2\u01be\u01d5\3\2\2\2\u01bf")
        buf.write("\u01c0\5R*\2\u01c0\u01c1\5\u008eH\2\u01c1\u01d5\3\2\2")
        buf.write("\2\u01c2\u01c3\5Z.\2\u01c3\u01c4\5\u008eH\2\u01c4\u01d5")
        buf.write("\3\2\2\2\u01c5\u01c6\5^\60\2\u01c6\u01c7\5\u008eH\2\u01c7")
        buf.write("\u01d5\3\2\2\2\u01c8\u01c9\5j\66\2\u01c9\u01ca\5\u008e")
        buf.write("H\2\u01ca\u01d5\3\2\2\2\u01cb\u01cc\5l\67\2\u01cc\u01cd")
        buf.write("\5\u008eH\2\u01cd\u01d5\3\2\2\2\u01ce\u01cf\5n8\2\u01cf")
        buf.write("\u01d0\5\u008eH\2\u01d0\u01d5\3\2\2\2\u01d1\u01d2\5t;")
        buf.write("\2\u01d2\u01d3\5\u008eH\2\u01d3\u01d5\3\2\2\2\u01d4\u01bc")
        buf.write("\3\2\2\2\u01d4\u01bf\3\2\2\2\u01d4\u01c2\3\2\2\2\u01d4")
        buf.write("\u01c5\3\2\2\2\u01d4\u01c8\3\2\2\2\u01d4\u01cb\3\2\2\2")
        buf.write("\u01d4\u01ce\3\2\2\2\u01d4\u01d1\3\2\2\2\u01d5O\3\2\2")
        buf.write("\2\u01d6\u01d9\5\6\4\2\u01d7\u01d9\5\20\t\2\u01d8\u01d6")
        buf.write("\3\2\2\2\u01d8\u01d7\3\2\2\2\u01d9Q\3\2\2\2\u01da\u01db")
        buf.write("\5T+\2\u01db\u01dc\7\30\2\2\u01dc\u01dd\5X-\2\u01dd\u01f3")
        buf.write("\3\2\2\2\u01de\u01df\5T+\2\u01df\u01e0\7\'\2\2\u01e0\u01e1")
        buf.write("\5X-\2\u01e1\u01f3\3\2\2\2\u01e2\u01e3\5T+\2\u01e3\u01e4")
        buf.write("\7(\2\2\u01e4\u01e5\5X-\2\u01e5\u01f3\3\2\2\2\u01e6\u01e7")
        buf.write("\5T+\2\u01e7\u01e8\7)\2\2\u01e8\u01e9\5X-\2\u01e9\u01f3")
        buf.write("\3\2\2\2\u01ea\u01eb\5T+\2\u01eb\u01ec\7*\2\2\u01ec\u01ed")
        buf.write("\5X-\2\u01ed\u01f3\3\2\2\2\u01ee\u01ef\5T+\2\u01ef\u01f0")
        buf.write("\7+\2\2\u01f0\u01f1\5X-\2\u01f1\u01f3\3\2\2\2\u01f2\u01da")
        buf.write("\3\2\2\2\u01f2\u01de\3\2\2\2\u01f2\u01e2\3\2\2\2\u01f2")
        buf.write("\u01e6\3\2\2\2\u01f2\u01ea\3\2\2\2\u01f2\u01ee\3\2\2\2")
        buf.write("\u01f3S\3\2\2\2\u01f4\u01f5\7\67\2\2\u01f5\u01f6\5V,\2")
        buf.write("\u01f6U\3\2\2\2\u01f7\u01f8\7,\2\2\u01f8\u01f9\7\67\2")
        buf.write("\2\u01f9\u0201\5V,\2\u01fa\u01fb\7\62\2\2\u01fb\u01fc")
        buf.write("\5> \2\u01fc\u01fd\7\63\2\2\u01fd\u01fe\5V,\2\u01fe\u0201")
        buf.write("\3\2\2\2\u01ff\u0201\3\2\2\2\u0200\u01f7\3\2\2\2\u0200")
        buf.write("\u01fa\3\2\2\2\u0200\u01ff\3\2\2\2\u0201W\3\2\2\2\u0202")
        buf.write("\u0206\5> \2\u0203\u0206\5\22\n\2\u0204\u0206\5\34\17")
        buf.write("\2\u0205\u0202\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0204")
        buf.write("\3\2\2\2\u0206Y\3\2\2\2\u0207\u0208\7\3\2\2\u0208\u0209")
        buf.write("\7.\2\2\u0209\u020a\5> \2\u020a\u020b\7/\2\2\u020b\u020f")
        buf.write("\7\60\2\2\u020c\u020e\5N(\2\u020d\u020c\3\2\2\2\u020e")
        buf.write("\u0211\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u0210\3\2\2\2")
        buf.write("\u0210\u0212\3\2\2\2\u0211\u020f\3\2\2\2\u0212\u0213\7")
        buf.write("\61\2\2\u0213\u022c\3\2\2\2\u0214\u0215\7\3\2\2\u0215")
        buf.write("\u0216\7.\2\2\u0216\u0217\5> \2\u0217\u0218\7/\2\2\u0218")
        buf.write("\u021c\7\60\2\2\u0219\u021b\5N(\2\u021a\u0219\3\2\2\2")
        buf.write("\u021b\u021e\3\2\2\2\u021c\u021a\3\2\2\2\u021c\u021d\3")
        buf.write("\2\2\2\u021d\u021f\3\2\2\2\u021e\u021c\3\2\2\2\u021f\u0220")
        buf.write("\7\61\2\2\u0220\u0221\5\\/\2\u0221\u0222\7\4\2\2\u0222")
        buf.write("\u0226\7\60\2\2\u0223\u0225\5N(\2\u0224\u0223\3\2\2\2")
        buf.write("\u0225\u0228\3\2\2\2\u0226\u0224\3\2\2\2\u0226\u0227\3")
        buf.write("\2\2\2\u0227\u0229\3\2\2\2\u0228\u0226\3\2\2\2\u0229\u022a")
        buf.write("\7\61\2\2\u022a\u022c\3\2\2\2\u022b\u0207\3\2\2\2\u022b")
        buf.write("\u0214\3\2\2\2\u022c[\3\2\2\2\u022d\u022e\7\4\2\2\u022e")
        buf.write("\u022f\7\3\2\2\u022f\u0230\7.\2\2\u0230\u0231\5> \2\u0231")
        buf.write("\u0232\7/\2\2\u0232\u0236\7\60\2\2\u0233\u0235\5N(\2\u0234")
        buf.write("\u0233\3\2\2\2\u0235\u0238\3\2\2\2\u0236\u0234\3\2\2\2")
        buf.write("\u0236\u0237\3\2\2\2\u0237\u0239\3\2\2\2\u0238\u0236\3")
        buf.write("\2\2\2\u0239\u023a\7\61\2\2\u023a\u023b\5\\/\2\u023b\u023e")
        buf.write("\3\2\2\2\u023c\u023e\3\2\2\2\u023d\u022d\3\2\2\2\u023d")
        buf.write("\u023c\3\2\2\2\u023e]\3\2\2\2\u023f\u0242\5`\61\2\u0240")
        buf.write("\u0242\5h\65\2\u0241\u023f\3\2\2\2\u0241\u0240\3\2\2\2")
        buf.write("\u0242_\3\2\2\2\u0243\u0244\7\5\2\2\u0244\u0245\5b\62")
        buf.write("\2\u0245\u0249\7\60\2\2\u0246\u0248\5N(\2\u0247\u0246")
        buf.write("\3\2\2\2\u0248\u024b\3\2\2\2\u0249\u0247\3\2\2\2\u0249")
        buf.write("\u024a\3\2\2\2\u024a\u024c\3\2\2\2\u024b\u0249\3\2\2\2")
        buf.write("\u024c\u024d\7\61\2\2\u024d\u025e\3\2\2\2\u024e\u024f")
        buf.write("\7\5\2\2\u024f\u0250\5d\63\2\u0250\u0251\7\65\2\2\u0251")
        buf.write("\u0252\5b\62\2\u0252\u0253\7\65\2\2\u0253\u0254\5f\64")
        buf.write("\2\u0254\u0258\7\60\2\2\u0255\u0257\5N(\2\u0256\u0255")
        buf.write("\3\2\2\2\u0257\u025a\3\2\2\2\u0258\u0256\3\2\2\2\u0258")
        buf.write("\u0259\3\2\2\2\u0259\u025b\3\2\2\2\u025a\u0258\3\2\2\2")
        buf.write("\u025b\u025c\7\61\2\2\u025c\u025e\3\2\2\2\u025d\u0243")
        buf.write("\3\2\2\2\u025d\u024e\3\2\2\2\u025ea\3\2\2\2\u025f\u0260")
        buf.write("\5> \2\u0260c\3\2\2\2\u0261\u0264\5R*\2\u0262\u0264\5")
        buf.write("\6\4\2\u0263\u0261\3\2\2\2\u0263\u0262\3\2\2\2\u0264e")
        buf.write("\3\2\2\2\u0265\u0266\5R*\2\u0266g\3\2\2\2\u0267\u0268")
        buf.write("\7\5\2\2\u0268\u0269\5x=\2\u0269\u026a\7\64\2\2\u026a")
        buf.write("\u026b\5z>\2\u026b\u026c\7\30\2\2\u026c\u026d\7\26\2\2")
        buf.write("\u026d\u026e\5|?\2\u026e\u0272\7\60\2\2\u026f\u0271\5")
        buf.write("N(\2\u0270\u026f\3\2\2\2\u0271\u0274\3\2\2\2\u0272\u0270")
        buf.write("\3\2\2\2\u0272\u0273\3\2\2\2\u0273\u0275\3\2\2\2\u0274")
        buf.write("\u0272\3\2\2\2\u0275\u0276\7\61\2\2\u0276i\3\2\2\2\u0277")
        buf.write("\u0278\7\25\2\2\u0278k\3\2\2\2\u0279\u027a\7\24\2\2\u027a")
        buf.write("m\3\2\2\2\u027b\u027c\7\67\2\2\u027c\u027d\5p9\2\u027d")
        buf.write("\u027e\7,\2\2\u027e\u027f\5n8\2\u027f\u028d\3\2\2\2\u0280")
        buf.write("\u0281\7\67\2\2\u0281\u0282\7.\2\2\u0282\u0283\5r:\2\u0283")
        buf.write("\u0284\7/\2\2\u0284\u0285\7,\2\2\u0285\u0286\5n8\2\u0286")
        buf.write("\u028d\3\2\2\2\u0287\u0288\7\67\2\2\u0288\u0289\7.\2\2")
        buf.write("\u0289\u028a\5r:\2\u028a\u028b\7/\2\2\u028b\u028d\3\2")
        buf.write("\2\2\u028c\u027b\3\2\2\2\u028c\u0280\3\2\2\2\u028c\u0287")
        buf.write("\3\2\2\2\u028do\3\2\2\2\u028e\u028f\7\62\2\2\u028f\u0290")
        buf.write("\5> \2\u0290\u0291\7\63\2\2\u0291\u0292\5p9\2\u0292\u0295")
        buf.write("\3\2\2\2\u0293\u0295\3\2\2\2\u0294\u028e\3\2\2\2\u0294")
        buf.write("\u0293\3\2\2\2\u0295q\3\2\2\2\u0296\u0297\5> \2\u0297")
        buf.write("\u0298\7\64\2\2\u0298\u0299\5r:\2\u0299\u029d\3\2\2\2")
        buf.write("\u029a\u029d\5> \2\u029b\u029d\3\2\2\2\u029c\u0296\3\2")
        buf.write("\2\2\u029c\u029a\3\2\2\2\u029c\u029b\3\2\2\2\u029ds\3")
        buf.write("\2\2\2\u029e\u029f\7\6\2\2\u029f\u02a0\5v<\2\u02a0u\3")
        buf.write("\2\2\2\u02a1\u02a6\5> \2\u02a2\u02a6\5\22\n\2\u02a3\u02a6")
        buf.write("\5\34\17\2\u02a4\u02a6\3\2\2\2\u02a5\u02a1\3\2\2\2\u02a5")
        buf.write("\u02a2\3\2\2\2\u02a5\u02a3\3\2\2\2\u02a5\u02a4\3\2\2\2")
        buf.write("\u02a6w\3\2\2\2\u02a7\u02a8\t\2\2\2\u02a8y\3\2\2\2\u02a9")
        buf.write("\u02aa\7\67\2\2\u02aa{\3\2\2\2\u02ab\u02ac\5> \2\u02ac")
        buf.write("}\3\2\2\2\u02ad\u02ae\t\3\2\2\u02ae\177\3\2\2\2\u02af")
        buf.write("\u02b0\t\4\2\2\u02b0\u0081\3\2\2\2\u02b1\u02b2\t\5\2\2")
        buf.write("\u02b2\u0083\3\2\2\2\u02b3\u02b4\t\6\2\2\u02b4\u0085\3")
        buf.write("\2\2\2\u02b5\u02be\78\2\2\u02b6\u02be\79\2\2\u02b7\u02be")
        buf.write("\7:\2\2\u02b8\u02be\7\17\2\2\u02b9\u02be\7\20\2\2\u02ba")
        buf.write("\u02be\7\21\2\2\u02bb\u02be\5\34\17\2\u02bc\u02be\7\67")
        buf.write("\2\2\u02bd\u02b5\3\2\2\2\u02bd\u02b6\3\2\2\2\u02bd\u02b7")
        buf.write("\3\2\2\2\u02bd\u02b8\3\2\2\2\u02bd\u02b9\3\2\2\2\u02bd")
        buf.write("\u02ba\3\2\2\2\u02bd\u02bb\3\2\2\2\u02bd\u02bc\3\2\2\2")
        buf.write("\u02be\u0087\3\2\2\2\u02bf\u02cb\7\67\2\2\u02c0\u02cb")
        buf.write("\78\2\2\u02c1\u02cb\79\2\2\u02c2\u02cb\7:\2\2\u02c3\u02cb")
        buf.write("\7\17\2\2\u02c4\u02cb\7\20\2\2\u02c5\u02cb\7\21\2\2\u02c6")
        buf.write("\u02c7\7.\2\2\u02c7\u02c8\5> \2\u02c8\u02c9\7/\2\2\u02c9")
        buf.write("\u02cb\3\2\2\2\u02ca\u02bf\3\2\2\2\u02ca\u02c0\3\2\2\2")
        buf.write("\u02ca\u02c1\3\2\2\2\u02ca\u02c2\3\2\2\2\u02ca\u02c3\3")
        buf.write("\2\2\2\u02ca\u02c4\3\2\2\2\u02ca\u02c5\3\2\2\2\u02ca\u02c6")
        buf.write("\3\2\2\2\u02cb\u0089\3\2\2\2\u02cc\u02cd\t\7\2\2\u02cd")
        buf.write("\u008b\3\2\2\2\u02ce\u02cf\t\b\2\2\u02cf\u008d\3\2\2\2")
        buf.write("\u02d0\u02d1\t\t\2\2\u02d1\u008f\3\2\2\2\65\u0093\u00a6")
        buf.write("\u00b1\u00b7\u00c2\u00ca\u00e0\u00e4\u00ed\u00f7\u0100")
        buf.write("\u0110\u011f\u0129\u0134\u013a\u0144\u014a\u0159\u0168")
        buf.write("\u0174\u017f\u018b\u0197\u01a3\u01aa\u01b7\u01b9\u01d4")
        buf.write("\u01d8\u01f2\u0200\u0205\u020f\u021c\u0226\u022b\u0236")
        buf.write("\u023d\u0241\u0249\u0258\u025d\u0263\u0272\u028c\u0294")
        buf.write("\u029c\u02a5\u02bd\u02ca")
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
                      "CONTINUE", "BREAK", "RANGE", "DECLARE", "ASSIGN", 
                      "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQ", "NEQ", 
                      "LT", "LEQ", "GT", "GEQ", "AND", "OR", "NOT", "PLUS_ASSIGN", 
                      "MINUS_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "DOT", "BLANK", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACKET", "RBRACKET", "COMMA", "SEMI", "COLON", 
                      "IDENTIFIER", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "BLOCK_COMMENT", "LINE_COMMENT", "WS", "NEWLINE", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_varDecl = 2
    RULE_varDetail = 3
    RULE_varDeclType = 4
    RULE_arrayType = 5
    RULE_varDeclExpr = 6
    RULE_constDecl = 7
    RULE_arrayLit = 8
    RULE_arrayBlock = 9
    RULE_arrayLitList = 10
    RULE_arrayLitListTail = 11
    RULE_arrayLitContent = 12
    RULE_structLit = 13
    RULE_optionalStructFields = 14
    RULE_structFieldList = 15
    RULE_structFieldListTail = 16
    RULE_structFieldAssign = 17
    RULE_structBlock = 18
    RULE_methodDecl = 19
    RULE_funcDecl = 20
    RULE_funcType = 21
    RULE_funcParam = 22
    RULE_funcListIdentifiers = 23
    RULE_typeDecl = 24
    RULE_structType = 25
    RULE_structDeclBlock = 26
    RULE_structDeclField = 27
    RULE_interfaceDeclBlock = 28
    RULE_interfaceDeclField = 29
    RULE_expr = 30
    RULE_logicOrExpr = 31
    RULE_logicAndExpr = 32
    RULE_equalityExpr = 33
    RULE_additiveExpr = 34
    RULE_multiplicativeExpr = 35
    RULE_unaryExpr = 36
    RULE_primaryExpr = 37
    RULE_statement = 38
    RULE_declarationStatement = 39
    RULE_assignStatement = 40
    RULE_assignStateLHS = 41
    RULE_assignStateLHSTail = 42
    RULE_assignStateRHS = 43
    RULE_ifStatement = 44
    RULE_elseIfStatement = 45
    RULE_forStatement = 46
    RULE_basicForStatement = 47
    RULE_forCondition = 48
    RULE_forInitilization = 49
    RULE_forUpdate = 50
    RULE_forRangeStatement = 51
    RULE_breakStatement = 52
    RULE_continueStatement = 53
    RULE_callStatement = 54
    RULE_callStatementArrayTail = 55
    RULE_callStatementParam = 56
    RULE_returnStatement = 57
    RULE_returnStatementTail = 58
    RULE_index = 59
    RULE_value = 60
    RULE_forArray = 61
    RULE_relationOp = 62
    RULE_addOp = 63
    RULE_mulOp = 64
    RULE_unaryOp = 65
    RULE_noArrayLit = 66
    RULE_term = 67
    RULE_intLitOrConstant = 68
    RULE_baseType = 69
    RULE_endOfStatement = 70

    ruleNames =  [ "program", "declaration", "varDecl", "varDetail", "varDeclType", 
                   "arrayType", "varDeclExpr", "constDecl", "arrayLit", 
                   "arrayBlock", "arrayLitList", "arrayLitListTail", "arrayLitContent", 
                   "structLit", "optionalStructFields", "structFieldList", 
                   "structFieldListTail", "structFieldAssign", "structBlock", 
                   "methodDecl", "funcDecl", "funcType", "funcParam", "funcListIdentifiers", 
                   "typeDecl", "structType", "structDeclBlock", "structDeclField", 
                   "interfaceDeclBlock", "interfaceDeclField", "expr", "logicOrExpr", 
                   "logicAndExpr", "equalityExpr", "additiveExpr", "multiplicativeExpr", 
                   "unaryExpr", "primaryExpr", "statement", "declarationStatement", 
                   "assignStatement", "assignStateLHS", "assignStateLHSTail", 
                   "assignStateRHS", "ifStatement", "elseIfStatement", "forStatement", 
                   "basicForStatement", "forCondition", "forInitilization", 
                   "forUpdate", "forRangeStatement", "breakStatement", "continueStatement", 
                   "callStatement", "callStatementArrayTail", "callStatementParam", 
                   "returnStatement", "returnStatementTail", "index", "value", 
                   "forArray", "relationOp", "addOp", "mulOp", "unaryOp", 
                   "noArrayLit", "term", "intLitOrConstant", "baseType", 
                   "endOfStatement" ]

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
    DECLARE=21
    ASSIGN=22
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
            self.state = 143 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 142
                self.declaration()
                self.state = 145 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 147
            self.match(MiniGoParser.EOF)
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


        def constDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclContext,0)


        def typeDecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypeDeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MiniGoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.varDecl()
                self.state = 150
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.funcDecl()
                self.state = 153
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 155
                self.constDecl()
                self.state = 156
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 158
                self.methodDecl()
                self.state = 159
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 161
                self.typeDecl()
                self.state = 162
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

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def varDetail(self):
            return self.getTypedRuleContext(MiniGoParser.VarDetailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = MiniGoParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(MiniGoParser.VAR)
            self.state = 167
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 168
            self.varDetail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDetailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclType(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclTypeContext,0)


        def varDeclExpr(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDetail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDetail" ):
                return visitor.visitVarDetail(self)
            else:
                return visitor.visitChildren(self)




    def varDetail(self):

        localctx = MiniGoParser.VarDetailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDetail)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.varDeclType()
                self.state = 171
                self.varDeclExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.varDeclType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.varDeclExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDeclType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclType" ):
                return visitor.visitVarDeclType(self)
            else:
                return visitor.visitChildren(self)




    def varDeclType(self):

        localctx = MiniGoParser.VarDeclTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varDeclType)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.baseType()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.arrayType()
                self.state = 179
                self.baseType()
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


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def intLitOrConstant(self):
            return self.getTypedRuleContext(MiniGoParser.IntLitOrConstantContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = MiniGoParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arrayType)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(MiniGoParser.LBRACKET)
                self.state = 184
                self.intLitOrConstant()
                self.state = 185
                self.match(MiniGoParser.RBRACKET)
                self.state = 186
                self.arrayType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(MiniGoParser.LBRACKET)
                self.state = 189
                self.intLitOrConstant()
                self.state = 190
                self.match(MiniGoParser.RBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECLARE(self):
            return self.getToken(MiniGoParser.DECLARE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDeclExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclExpr" ):
                return visitor.visitVarDeclExpr(self)
            else:
                return visitor.visitChildren(self)




    def varDeclExpr(self):

        localctx = MiniGoParser.VarDeclExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_varDeclExpr)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(MiniGoParser.DECLARE)
                self.state = 195
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.match(MiniGoParser.DECLARE)
                self.state = 197
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 198
                self.match(MiniGoParser.DECLARE)
                self.state = 199
                self.structLit()
                pass


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

        def varDeclExpr(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclExprContext,0)


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
            self.state = 202
            self.match(MiniGoParser.CONST)
            self.state = 203
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 204
            self.varDeclExpr()
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

        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def arrayBlock(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayBlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLit" ):
                return visitor.visitArrayLit(self)
            else:
                return visitor.visitChildren(self)




    def arrayLit(self):

        localctx = MiniGoParser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.arrayType()
            self.state = 207
            self.baseType()
            self.state = 208
            self.arrayBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def arrayLitList(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitListContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayBlock" ):
                return visitor.visitArrayBlock(self)
            else:
                return visitor.visitChildren(self)




    def arrayBlock(self):

        localctx = MiniGoParser.ArrayBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arrayBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(MiniGoParser.LBRACE)
            self.state = 211
            self.arrayLitList()
            self.state = 212
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayLitContent(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContentContext,0)


        def arrayLitListTail(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitListTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLitList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLitList" ):
                return visitor.visitArrayLitList(self)
            else:
                return visitor.visitChildren(self)




    def arrayLitList(self):

        localctx = MiniGoParser.ArrayLitListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arrayLitList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.arrayLitContent()
            self.state = 215
            self.arrayLitListTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLitListTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def arrayLitContent(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContentContext,0)


        def arrayLitListTail(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitListTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLitListTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLitListTail" ):
                return visitor.visitArrayLitListTail(self)
            else:
                return visitor.visitChildren(self)




    def arrayLitListTail(self):

        localctx = MiniGoParser.ArrayLitListTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrayLitListTail)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(MiniGoParser.COMMA)
                self.state = 218
                self.arrayLitContent()
                self.state = 219
                self.arrayLitListTail()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

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


    class ArrayLitContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayBlock(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayBlockContext,0)


        def noArrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.NoArrayLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLitContent

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLitContent" ):
                return visitor.visitArrayLitContent(self)
            else:
                return visitor.visitChildren(self)




    def arrayLitContent(self):

        localctx = MiniGoParser.ArrayLitContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arrayLitContent)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.arrayBlock()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.noArrayLit()
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

        def optionalStructFields(self):
            return self.getTypedRuleContext(MiniGoParser.OptionalStructFieldsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructLit" ):
                return visitor.visitStructLit(self)
            else:
                return visitor.visitChildren(self)




    def structLit(self):

        localctx = MiniGoParser.StructLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_structLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 229
            self.match(MiniGoParser.LBRACE)
            self.state = 230
            self.optionalStructFields()
            self.state = 231
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionalStructFieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structFieldList(self):
            return self.getTypedRuleContext(MiniGoParser.StructFieldListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_optionalStructFields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptionalStructFields" ):
                return visitor.visitOptionalStructFields(self)
            else:
                return visitor.visitChildren(self)




    def optionalStructFields(self):

        localctx = MiniGoParser.OptionalStructFieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_optionalStructFields)
        try:
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.structFieldList()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

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


    class StructFieldListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structFieldAssign(self):
            return self.getTypedRuleContext(MiniGoParser.StructFieldAssignContext,0)


        def structFieldListTail(self):
            return self.getTypedRuleContext(MiniGoParser.StructFieldListTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structFieldList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFieldList" ):
                return visitor.visitStructFieldList(self)
            else:
                return visitor.visitChildren(self)




    def structFieldList(self):

        localctx = MiniGoParser.StructFieldListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_structFieldList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.structFieldAssign()
            self.state = 238
            self.structFieldListTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructFieldListTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def structFieldAssign(self):
            return self.getTypedRuleContext(MiniGoParser.StructFieldAssignContext,0)


        def structFieldListTail(self):
            return self.getTypedRuleContext(MiniGoParser.StructFieldListTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structFieldListTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFieldListTail" ):
                return visitor.visitStructFieldListTail(self)
            else:
                return visitor.visitChildren(self)




    def structFieldListTail(self):

        localctx = MiniGoParser.StructFieldListTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_structFieldListTail)
        try:
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(MiniGoParser.COMMA)
                self.state = 241
                self.structFieldAssign()
                self.state = 242
                self.structFieldListTail()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

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


    class StructFieldAssignContext(ParserRuleContext):
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
            return MiniGoParser.RULE_structFieldAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFieldAssign" ):
                return visitor.visitStructFieldAssign(self)
            else:
                return visitor.visitChildren(self)




    def structFieldAssign(self):

        localctx = MiniGoParser.StructFieldAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_structFieldAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 248
            self.match(MiniGoParser.COLON)
            self.state = 249
            self.structBlock()
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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


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
        self.enterRule(localctx, 36, self.RULE_structBlock)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 253
                self.structLit()
                pass


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

        def funcParam(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamContext,0)


        def funcType(self):
            return self.getTypedRuleContext(MiniGoParser.FuncTypeContext,0)


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
            return MiniGoParser.RULE_methodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = MiniGoParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(MiniGoParser.FUNC)
            self.state = 257
            self.match(MiniGoParser.LPAREN)
            self.state = 258
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 259
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 260
            self.match(MiniGoParser.RPAREN)
            self.state = 261
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 262
            self.match(MiniGoParser.LPAREN)
            self.state = 263
            self.funcParam()
            self.state = 264
            self.match(MiniGoParser.RPAREN)
            self.state = 265
            self.funcType()
            self.state = 266
            self.match(MiniGoParser.LBRACE)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 267
                self.statement()
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 273
            self.match(MiniGoParser.RBRACE)
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

        def funcParam(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def funcType(self):
            return self.getTypedRuleContext(MiniGoParser.FuncTypeContext,0)


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
            return MiniGoParser.RULE_funcDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = MiniGoParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(MiniGoParser.FUNC)
            self.state = 276
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 277
            self.match(MiniGoParser.LPAREN)
            self.state = 278
            self.funcParam()
            self.state = 279
            self.match(MiniGoParser.RPAREN)
            self.state = 280
            self.funcType()
            self.state = 281
            self.match(MiniGoParser.LBRACE)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 282
                self.statement()
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 288
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncType" ):
                return visitor.visitFuncType(self)
            else:
                return visitor.visitChildren(self)




    def funcType(self):

        localctx = MiniGoParser.FuncTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_funcType)
        try:
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.baseType()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.arrayType()
                self.state = 292
                self.baseType()
                pass
            elif token in [MiniGoParser.LBRACE, MiniGoParser.SEMI, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 3)

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


    class FuncParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcListIdentifiers(self):
            return self.getTypedRuleContext(MiniGoParser.FuncListIdentifiersContext,0)


        def varDeclType(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclTypeContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def funcParam(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcParam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncParam" ):
                return visitor.visitFuncParam(self)
            else:
                return visitor.visitChildren(self)




    def funcParam(self):

        localctx = MiniGoParser.FuncParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_funcParam)
        try:
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.funcListIdentifiers()
                self.state = 298
                self.varDeclType()
                self.state = 299
                self.match(MiniGoParser.COMMA)
                self.state = 300
                self.funcParam()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.funcListIdentifiers()
                self.state = 303
                self.varDeclType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncListIdentifiersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def funcListIdentifiers(self):
            return self.getTypedRuleContext(MiniGoParser.FuncListIdentifiersContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcListIdentifiers

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncListIdentifiers" ):
                return visitor.visitFuncListIdentifiers(self)
            else:
                return visitor.visitChildren(self)




    def funcListIdentifiers(self):

        localctx = MiniGoParser.FuncListIdentifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_funcListIdentifiers)
        try:
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 310
                self.match(MiniGoParser.COMMA)
                self.state = 311
                self.funcListIdentifiers()
                pass


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

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def structDeclBlock(self):
            return self.getTypedRuleContext(MiniGoParser.StructDeclBlockContext,0)


        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def interfaceDeclBlock(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceDeclBlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typeDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDecl" ):
                return visitor.visitTypeDecl(self)
            else:
                return visitor.visitChildren(self)




    def typeDecl(self):

        localctx = MiniGoParser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typeDecl)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(MiniGoParser.TYPE)
                self.state = 315
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 316
                self.match(MiniGoParser.STRUCT)
                self.state = 317
                self.structDeclBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.match(MiniGoParser.TYPE)
                self.state = 319
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 320
                self.match(MiniGoParser.INTERFACE)
                self.state = 321
                self.interfaceDeclBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructType" ):
                return visitor.visitStructType(self)
            else:
                return visitor.visitChildren(self)




    def structType(self):

        localctx = MiniGoParser.StructTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_structType)
        try:
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.baseType()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.arrayType()
                self.state = 326
                self.baseType()
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


    class StructDeclBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def structDeclField(self):
            return self.getTypedRuleContext(MiniGoParser.StructDeclFieldContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structDeclBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDeclBlock" ):
                return visitor.visitStructDeclBlock(self)
            else:
                return visitor.visitChildren(self)




    def structDeclBlock(self):

        localctx = MiniGoParser.StructDeclBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_structDeclBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(MiniGoParser.LBRACE)
            self.state = 331
            self.structDeclField()
            self.state = 332
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def structType(self):
            return self.getTypedRuleContext(MiniGoParser.StructTypeContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def structDeclField(self):
            return self.getTypedRuleContext(MiniGoParser.StructDeclFieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structDeclField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDeclField" ):
                return visitor.visitStructDeclField(self)
            else:
                return visitor.visitChildren(self)




    def structDeclField(self):

        localctx = MiniGoParser.StructDeclFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_structDeclField)
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 335
                self.structType()
                self.state = 336
                self.endOfStatement()
                self.state = 337
                self.structDeclField()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 340
                self.structType()
                self.state = 341
                self.endOfStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDeclBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def interfaceDeclField(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceDeclFieldContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceDeclBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDeclBlock" ):
                return visitor.visitInterfaceDeclBlock(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDeclBlock(self):

        localctx = MiniGoParser.InterfaceDeclBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_interfaceDeclBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(MiniGoParser.LBRACE)
            self.state = 346
            self.interfaceDeclField()
            self.state = 347
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDeclFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def funcParam(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def funcType(self):
            return self.getTypedRuleContext(MiniGoParser.FuncTypeContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def interfaceDeclField(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceDeclFieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceDeclField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDeclField" ):
                return visitor.visitInterfaceDeclField(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDeclField(self):

        localctx = MiniGoParser.InterfaceDeclFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_interfaceDeclField)
        try:
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 350
                self.match(MiniGoParser.LPAREN)
                self.state = 351
                self.funcParam()
                self.state = 352
                self.match(MiniGoParser.RPAREN)
                self.state = 353
                self.funcType()
                self.state = 354
                self.endOfStatement()
                self.state = 355
                self.interfaceDeclField()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicOrExpr(self):
            return self.getTypedRuleContext(MiniGoParser.LogicOrExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MiniGoParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.logicOrExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicOrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicAndExpr(self):
            return self.getTypedRuleContext(MiniGoParser.LogicAndExprContext,0)


        def logicOrExpr(self):
            return self.getTypedRuleContext(MiniGoParser.LogicOrExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_logicOrExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOrExpr" ):
                return visitor.visitLogicOrExpr(self)
            else:
                return visitor.visitChildren(self)



    def logicOrExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LogicOrExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_logicOrExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.logicAndExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogicOrExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicOrExpr)
                    self.state = 365
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 366
                    self.match(MiniGoParser.OR)
                    self.state = 367
                    self.logicAndExpr(0) 
                self.state = 372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LogicAndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpr(self):
            return self.getTypedRuleContext(MiniGoParser.EqualityExprContext,0)


        def logicAndExpr(self):
            return self.getTypedRuleContext(MiniGoParser.LogicAndExprContext,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_logicAndExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicAndExpr" ):
                return visitor.visitLogicAndExpr(self)
            else:
                return visitor.visitChildren(self)



    def logicAndExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LogicAndExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_logicAndExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.equalityExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogicAndExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicAndExpr)
                    self.state = 376
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 377
                    self.match(MiniGoParser.AND)
                    self.state = 378
                    self.equalityExpr(0) 
                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EqualityExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self):
            return self.getTypedRuleContext(MiniGoParser.AdditiveExprContext,0)


        def equalityExpr(self):
            return self.getTypedRuleContext(MiniGoParser.EqualityExprContext,0)


        def relationOp(self):
            return self.getTypedRuleContext(MiniGoParser.RelationOpContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_equalityExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpr" ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)



    def equalityExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.EqualityExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_equalityExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.additiveExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 393
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.EqualityExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpr)
                    self.state = 387
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 388
                    self.relationOp()
                    self.state = 389
                    self.additiveExpr(0) 
                self.state = 395
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpr(self):
            return self.getTypedRuleContext(MiniGoParser.MultiplicativeExprContext,0)


        def additiveExpr(self):
            return self.getTypedRuleContext(MiniGoParser.AdditiveExprContext,0)


        def addOp(self):
            return self.getTypedRuleContext(MiniGoParser.AddOpContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_additiveExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)



    def additiveExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.AdditiveExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_additiveExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.multiplicativeExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 405
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.AdditiveExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpr)
                    self.state = 399
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 400
                    self.addOp()
                    self.state = 401
                    self.multiplicativeExpr(0) 
                self.state = 407
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.UnaryExprContext,0)


        def multiplicativeExpr(self):
            return self.getTypedRuleContext(MiniGoParser.MultiplicativeExprContext,0)


        def mulOp(self):
            return self.getTypedRuleContext(MiniGoParser.MulOpContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_multiplicativeExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpr" ):
                return visitor.visitMultiplicativeExpr(self)
            else:
                return visitor.visitChildren(self)



    def multiplicativeExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.MultiplicativeExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_multiplicativeExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.unaryExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 417
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.MultiplicativeExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpr)
                    self.state = 411
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 412
                    self.mulOp()
                    self.state = 413
                    self.unaryExpr() 
                self.state = 419
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryOp(self):
            return self.getTypedRuleContext(MiniGoParser.UnaryOpContext,0)


        def unaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.UnaryExprContext,0)


        def primaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_unaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = MiniGoParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_unaryExpr)
        try:
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.unaryOp()
                self.state = 421
                self.unaryExpr()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.LPAREN, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.primaryExpr(0)
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


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(MiniGoParser.TermContext,0)


        def primaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExprContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)



    def primaryExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.PrimaryExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_primaryExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 439
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 437
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.PrimaryExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primaryExpr)
                        self.state = 429
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 430
                        self.match(MiniGoParser.DOT)
                        self.state = 431
                        self.match(MiniGoParser.IDENTIFIER)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.PrimaryExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primaryExpr)
                        self.state = 432
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 433
                        self.match(MiniGoParser.LBRACKET)
                        self.state = 434
                        self.expr()
                        self.state = 435
                        self.match(MiniGoParser.RBRACKET)
                        pass

             
                self.state = 441
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarationStatement(self):
            return self.getTypedRuleContext(MiniGoParser.DeclarationStatementContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


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


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_statement)
        try:
            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.declarationStatement()
                self.state = 443
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.assignStatement()
                self.state = 446
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 448
                self.ifStatement()
                self.state = 449
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 451
                self.forStatement()
                self.state = 452
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 454
                self.breakStatement()
                self.state = 455
                self.endOfStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 457
                self.continueStatement()
                self.state = 458
                self.endOfStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 460
                self.callStatement()
                self.state = 461
                self.endOfStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 463
                self.returnStatement()
                self.state = 464
                self.endOfStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def constDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declarationStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationStatement" ):
                return visitor.visitDeclarationStatement(self)
            else:
                return visitor.visitChildren(self)




    def declarationStatement(self):

        localctx = MiniGoParser.DeclarationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_declarationStatement)
        try:
            self.state = 470
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 468
                self.varDecl()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 469
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


    class AssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStateLHS(self):
            return self.getTypedRuleContext(MiniGoParser.AssignStateLHSContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def assignStateRHS(self):
            return self.getTypedRuleContext(MiniGoParser.AssignStateRHSContext,0)


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
            return MiniGoParser.RULE_assignStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignStatement(self):

        localctx = MiniGoParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_assignStatement)
        try:
            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.assignStateLHS()
                self.state = 473
                self.match(MiniGoParser.ASSIGN)
                self.state = 474
                self.assignStateRHS()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 476
                self.assignStateLHS()
                self.state = 477
                self.match(MiniGoParser.PLUS_ASSIGN)
                self.state = 478
                self.assignStateRHS()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 480
                self.assignStateLHS()
                self.state = 481
                self.match(MiniGoParser.MINUS_ASSIGN)
                self.state = 482
                self.assignStateRHS()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 484
                self.assignStateLHS()
                self.state = 485
                self.match(MiniGoParser.MUL_ASSIGN)
                self.state = 486
                self.assignStateRHS()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 488
                self.assignStateLHS()
                self.state = 489
                self.match(MiniGoParser.DIV_ASSIGN)
                self.state = 490
                self.assignStateRHS()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 492
                self.assignStateLHS()
                self.state = 493
                self.match(MiniGoParser.MOD_ASSIGN)
                self.state = 494
                self.assignStateRHS()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStateLHSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def assignStateLHSTail(self):
            return self.getTypedRuleContext(MiniGoParser.AssignStateLHSTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignStateLHS

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStateLHS" ):
                return visitor.visitAssignStateLHS(self)
            else:
                return visitor.visitChildren(self)




    def assignStateLHS(self):

        localctx = MiniGoParser.AssignStateLHSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_assignStateLHS)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 499
            self.assignStateLHSTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStateLHSTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def assignStateLHSTail(self):
            return self.getTypedRuleContext(MiniGoParser.AssignStateLHSTailContext,0)


        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignStateLHSTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStateLHSTail" ):
                return visitor.visitAssignStateLHSTail(self)
            else:
                return visitor.visitChildren(self)




    def assignStateLHSTail(self):

        localctx = MiniGoParser.AssignStateLHSTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_assignStateLHSTail)
        try:
            self.state = 510
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                self.match(MiniGoParser.DOT)
                self.state = 502
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 503
                self.assignStateLHSTail()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 504
                self.match(MiniGoParser.LBRACKET)
                self.state = 505
                self.expr()
                self.state = 506
                self.match(MiniGoParser.RBRACKET)
                self.state = 507
                self.assignStateLHSTail()
                pass
            elif token in [MiniGoParser.ASSIGN, MiniGoParser.PLUS_ASSIGN, MiniGoParser.MINUS_ASSIGN, MiniGoParser.MUL_ASSIGN, MiniGoParser.DIV_ASSIGN, MiniGoParser.MOD_ASSIGN]:
                self.enterOuterAlt(localctx, 3)

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


    class AssignStateRHSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignStateRHS

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStateRHS" ):
                return visitor.visitAssignStateRHS(self)
            else:
                return visitor.visitChildren(self)




    def assignStateRHS(self):

        localctx = MiniGoParser.AssignStateRHSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_assignStateRHS)
        try:
            self.state = 515
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 512
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 514
                self.structLit()
                pass


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

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACE)
            else:
                return self.getToken(MiniGoParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACE)
            else:
                return self.getToken(MiniGoParser.RBRACE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def elseIfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ElseIfStatementContext,0)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniGoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.state = 553
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 517
                self.match(MiniGoParser.IF)
                self.state = 518
                self.match(MiniGoParser.LPAREN)
                self.state = 519
                self.expr()
                self.state = 520
                self.match(MiniGoParser.RPAREN)
                self.state = 521
                self.match(MiniGoParser.LBRACE)
                self.state = 525
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 522
                    self.statement()
                    self.state = 527
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 528
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 530
                self.match(MiniGoParser.IF)
                self.state = 531
                self.match(MiniGoParser.LPAREN)
                self.state = 532
                self.expr()
                self.state = 533
                self.match(MiniGoParser.RPAREN)
                self.state = 534
                self.match(MiniGoParser.LBRACE)
                self.state = 538
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 535
                    self.statement()
                    self.state = 540
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 541
                self.match(MiniGoParser.RBRACE)
                self.state = 542
                self.elseIfStatement()
                self.state = 543
                self.match(MiniGoParser.ELSE)
                self.state = 544
                self.match(MiniGoParser.LBRACE)
                self.state = 548
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 545
                    self.statement()
                    self.state = 550
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 551
                self.match(MiniGoParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def elseIfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ElseIfStatementContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elseIfStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseIfStatement" ):
                return visitor.visitElseIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def elseIfStatement(self):

        localctx = MiniGoParser.ElseIfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_elseIfStatement)
        self._la = 0 # Token type
        try:
            self.state = 571
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 555
                self.match(MiniGoParser.ELSE)
                self.state = 556
                self.match(MiniGoParser.IF)
                self.state = 557
                self.match(MiniGoParser.LPAREN)
                self.state = 558
                self.expr()
                self.state = 559
                self.match(MiniGoParser.RPAREN)
                self.state = 560
                self.match(MiniGoParser.LBRACE)
                self.state = 564
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 561
                    self.statement()
                    self.state = 566
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 567
                self.match(MiniGoParser.RBRACE)
                self.state = 568
                self.elseIfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


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

        def basicForStatement(self):
            return self.getTypedRuleContext(MiniGoParser.BasicForStatementContext,0)


        def forRangeStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ForRangeStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = MiniGoParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_forStatement)
        try:
            self.state = 575
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 573
                self.basicForStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 574
                self.forRangeStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BasicForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def forCondition(self):
            return self.getTypedRuleContext(MiniGoParser.ForConditionContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def forInitilization(self):
            return self.getTypedRuleContext(MiniGoParser.ForInitilizationContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def forUpdate(self):
            return self.getTypedRuleContext(MiniGoParser.ForUpdateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_basicForStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasicForStatement" ):
                return visitor.visitBasicForStatement(self)
            else:
                return visitor.visitChildren(self)




    def basicForStatement(self):

        localctx = MiniGoParser.BasicForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_basicForStatement)
        self._la = 0 # Token type
        try:
            self.state = 603
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 577
                self.match(MiniGoParser.FOR)
                self.state = 578
                self.forCondition()
                self.state = 579
                self.match(MiniGoParser.LBRACE)
                self.state = 583
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 580
                    self.statement()
                    self.state = 585
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 586
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 588
                self.match(MiniGoParser.FOR)
                self.state = 589
                self.forInitilization()
                self.state = 590
                self.match(MiniGoParser.SEMI)
                self.state = 591
                self.forCondition()
                self.state = 592
                self.match(MiniGoParser.SEMI)
                self.state = 593
                self.forUpdate()
                self.state = 594
                self.match(MiniGoParser.LBRACE)
                self.state = 598
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 595
                    self.statement()
                    self.state = 600
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 601
                self.match(MiniGoParser.RBRACE)
                pass


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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forCondition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




    def forCondition(self):

        localctx = MiniGoParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitilizationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStatement(self):
            return self.getTypedRuleContext(MiniGoParser.AssignStatementContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forInitilization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInitilization" ):
                return visitor.visitForInitilization(self)
            else:
                return visitor.visitChildren(self)




    def forInitilization(self):

        localctx = MiniGoParser.ForInitilizationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_forInitilization)
        try:
            self.state = 609
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 607
                self.assignStatement()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 608
                self.varDecl()
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


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStatement(self):
            return self.getTypedRuleContext(MiniGoParser.AssignStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forUpdate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = MiniGoParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            self.assignStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForRangeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def index(self):
            return self.getTypedRuleContext(MiniGoParser.IndexContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def value(self):
            return self.getTypedRuleContext(MiniGoParser.ValueContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def forArray(self):
            return self.getTypedRuleContext(MiniGoParser.ForArrayContext,0)


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
            return MiniGoParser.RULE_forRangeStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForRangeStatement" ):
                return visitor.visitForRangeStatement(self)
            else:
                return visitor.visitChildren(self)




    def forRangeStatement(self):

        localctx = MiniGoParser.ForRangeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_forRangeStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 613
            self.match(MiniGoParser.FOR)
            self.state = 614
            self.index()
            self.state = 615
            self.match(MiniGoParser.COMMA)
            self.state = 616
            self.value()
            self.state = 617
            self.match(MiniGoParser.ASSIGN)
            self.state = 618
            self.match(MiniGoParser.RANGE)
            self.state = 619
            self.forArray()
            self.state = 620
            self.match(MiniGoParser.LBRACE)
            self.state = 624
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 621
                self.statement()
                self.state = 626
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 627
            self.match(MiniGoParser.RBRACE)
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
        self.enterRule(localctx, 104, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
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
        self.enterRule(localctx, 106, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 631
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

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def callStatementArrayTail(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementArrayTailContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def callStatement(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def callStatementParam(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementParamContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_callStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def callStatement(self):

        localctx = MiniGoParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_callStatement)
        try:
            self.state = 650
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 633
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 634
                self.callStatementArrayTail()
                self.state = 635
                self.match(MiniGoParser.DOT)
                self.state = 636
                self.callStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 638
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 639
                self.match(MiniGoParser.LPAREN)
                self.state = 640
                self.callStatementParam()
                self.state = 641
                self.match(MiniGoParser.RPAREN)
                self.state = 642
                self.match(MiniGoParser.DOT)
                self.state = 643
                self.callStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 645
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 646
                self.match(MiniGoParser.LPAREN)
                self.state = 647
                self.callStatementParam()
                self.state = 648
                self.match(MiniGoParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStatementArrayTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def callStatementArrayTail(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementArrayTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callStatementArrayTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatementArrayTail" ):
                return visitor.visitCallStatementArrayTail(self)
            else:
                return visitor.visitChildren(self)




    def callStatementArrayTail(self):

        localctx = MiniGoParser.CallStatementArrayTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_callStatementArrayTail)
        try:
            self.state = 658
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 652
                self.match(MiniGoParser.LBRACKET)
                self.state = 653
                self.expr()
                self.state = 654
                self.match(MiniGoParser.RBRACKET)
                self.state = 655
                self.callStatementArrayTail()
                pass
            elif token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 2)

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


    class CallStatementParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def callStatementParam(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementParamContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callStatementParam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatementParam" ):
                return visitor.visitCallStatementParam(self)
            else:
                return visitor.visitChildren(self)




    def callStatementParam(self):

        localctx = MiniGoParser.CallStatementParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_callStatementParam)
        try:
            self.state = 666
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 660
                self.expr()
                self.state = 661
                self.match(MiniGoParser.COMMA)
                self.state = 662
                self.callStatementParam()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 664
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

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

        def returnStatementTail(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnStatementTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MiniGoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 668
            self.match(MiniGoParser.RETURN)
            self.state = 669
            self.returnStatementTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStatementTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatementTail" ):
                return visitor.visitReturnStatementTail(self)
            else:
                return visitor.visitChildren(self)




    def returnStatementTail(self):

        localctx = MiniGoParser.ReturnStatementTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_returnStatementTail)
        try:
            self.state = 675
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 671
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 672
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 673
                self.structLit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def BLANK(self):
            return self.getToken(MiniGoParser.BLANK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = MiniGoParser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 677
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.BLANK or _la==MiniGoParser.IDENTIFIER):
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


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = MiniGoParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 679
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forArray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForArray" ):
                return visitor.visitForArray(self)
            else:
                return visitor.visitChildren(self)




    def forArray(self):

        localctx = MiniGoParser.ForArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_forArray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 681
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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

        def getRuleIndex(self):
            return MiniGoParser.RULE_relationOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationOp" ):
                return visitor.visitRelationOp(self)
            else:
                return visitor.visitChildren(self)




    def relationOp(self):

        localctx = MiniGoParser.RelationOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_relationOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 683
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LEQ) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GEQ))) != 0)):
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


    class AddOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_addOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddOp" ):
                return visitor.visitAddOp(self)
            else:
                return visitor.visitChildren(self)




    def addOp(self):

        localctx = MiniGoParser.AddOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_addOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 685
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
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


    class MulOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_mulOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulOp" ):
                return visitor.visitMulOp(self)
            else:
                return visitor.visitChildren(self)




    def mulOp(self):

        localctx = MiniGoParser.MulOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_mulOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 687
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
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


    class UnaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_unaryOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOp" ):
                return visitor.visitUnaryOp(self)
            else:
                return visitor.visitChildren(self)




    def unaryOp(self):

        localctx = MiniGoParser.UnaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_unaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 689
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
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


    class NoArrayLitContext(ParserRuleContext):
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


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_noArrayLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoArrayLit" ):
                return visitor.visitNoArrayLit(self)
            else:
                return visitor.visitChildren(self)




    def noArrayLit(self):

        localctx = MiniGoParser.NoArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_noArrayLit)
        try:
            self.state = 699
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 691
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 692
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 693
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 694
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 695
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 696
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 697
                self.structLit()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 698
                self.match(MiniGoParser.IDENTIFIER)
                pass


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

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

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

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


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
        self.enterRule(localctx, 134, self.RULE_term)
        try:
            self.state = 712
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 701
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 702
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 703
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 704
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 705
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 706
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 707
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.LPAREN]:
                self.enterOuterAlt(localctx, 8)
                self.state = 708
                self.match(MiniGoParser.LPAREN)
                self.state = 709
                self.expr()
                self.state = 710
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


    class IntLitOrConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_intLitOrConstant

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLitOrConstant" ):
                return visitor.visitIntLitOrConstant(self)
            else:
                return visitor.visitChildren(self)




    def intLitOrConstant(self):

        localctx = MiniGoParser.IntLitOrConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_intLitOrConstant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 714
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.IDENTIFIER or _la==MiniGoParser.INT_LIT):
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
        self.enterRule(localctx, 138, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 716
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
        self.enterRule(localctx, 140, self.RULE_endOfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 718
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[31] = self.logicOrExpr_sempred
        self._predicates[32] = self.logicAndExpr_sempred
        self._predicates[33] = self.equalityExpr_sempred
        self._predicates[34] = self.additiveExpr_sempred
        self._predicates[35] = self.multiplicativeExpr_sempred
        self._predicates[37] = self.primaryExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logicOrExpr_sempred(self, localctx:LogicOrExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def logicAndExpr_sempred(self, localctx:LogicAndExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def equalityExpr_sempred(self, localctx:EqualityExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def additiveExpr_sempred(self, localctx:AdditiveExprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def multiplicativeExpr_sempred(self, localctx:MultiplicativeExprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def primaryExpr_sempred(self, localctx:PrimaryExprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




