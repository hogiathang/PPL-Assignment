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
        buf.write("\u02f9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\3\2\6\2\u009c\n\2\r\2\16\2\u009d\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00b1")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\5\5\u00bc\n\5")
        buf.write("\3\6\3\6\3\6\3\6\5\6\u00c2\n\6\3\7\3\7\3\7\3\7\6\7\u00c8")
        buf.write("\n\7\r\7\16\7\u00c9\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u00d2")
        buf.write("\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\5\r\u00e6\n\r\3\16\3\16\5\16")
        buf.write("\u00ea\n\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\5\20\u00f3")
        buf.write("\n\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\5\22\u00fd")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u0111\n")
        buf.write("\25\f\25\16\25\u0114\13\25\3\25\3\25\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\7\26\u0120\n\26\f\26\16\26\u0123")
        buf.write("\13\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\5\27\u012c\n")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u0137\n\30\3\31\3\31\3\31\3\31\5\31\u013d\n\31\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0147\n\32\3\33")
        buf.write("\3\33\7\33\u014b\n\33\f\33\16\33\u014e\13\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0159\n\34\3")
        buf.write("\35\3\35\7\35\u015d\n\35\f\35\16\35\u0160\13\35\3\35\3")
        buf.write("\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\5\37\u016e\n\37\3 \3 \3 \3 \3 \3 \7 \u0176\n \f \16 ")
        buf.write("\u0179\13 \3!\3!\3!\3!\3!\3!\7!\u0181\n!\f!\16!\u0184")
        buf.write("\13!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u018d\n\"\f\"\16")
        buf.write("\"\u0190\13\"\3#\3#\3#\3#\3#\3#\3#\7#\u0199\n#\f#\16#")
        buf.write("\u019c\13#\3$\3$\3$\3$\3$\3$\3$\7$\u01a5\n$\f$\16$\u01a8")
        buf.write("\13$\3%\3%\3%\3%\5%\u01ae\n%\3&\3&\7&\u01b2\n&\f&\16&")
        buf.write("\u01b5\13&\3\'\3\'\3\'\5\'\u01ba\n\'\3\'\5\'\u01bd\n\'")
        buf.write("\3\'\3\'\5\'\u01c1\n\'\3(\3(\3(\3(\6(\u01c7\n(\r(\16(")
        buf.write("\u01c8\3)\3)\5)\u01cd\n)\3)\3)\3*\3*\3*\7*\u01d4\n*\f")
        buf.write("*\16*\u01d7\13*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u01f1\n+\3,\3,\5")
        buf.write(",\u01f5\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u020f\n-\3.\3.\3.\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\5/\u021d\n/\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\7\61\u0227\n\61\f\61\16\61\u022a")
        buf.write("\13\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\7\61\u0234")
        buf.write("\n\61\f\61\16\61\u0237\13\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\7\61\u023e\n\61\f\61\16\61\u0241\13\61\3\61\3\61\5\61")
        buf.write("\u0245\n\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\7\62\u024e")
        buf.write("\n\62\f\62\16\62\u0251\13\62\3\62\3\62\3\62\3\62\5\62")
        buf.write("\u0257\n\62\3\63\3\63\5\63\u025b\n\63\3\64\3\64\3\64\3")
        buf.write("\64\7\64\u0261\n\64\f\64\16\64\u0264\13\64\3\64\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\7\64\u0270\n\64")
        buf.write("\f\64\16\64\u0273\13\64\3\64\3\64\5\64\u0277\n\64\3\65")
        buf.write("\3\65\3\66\3\66\5\66\u027d\n\66\3\67\3\67\38\38\38\38")
        buf.write("\38\38\38\38\38\78\u028a\n8\f8\168\u028d\138\38\38\39")
        buf.write("\39\3:\3:\3;\3;\5;\u0297\n;\3<\3<\3<\3<\3<\3<\3<\3<\5")
        buf.write("<\u02a1\n<\3<\3<\3<\5<\u02a6\n<\3=\3=\3=\3=\5=\u02ac\n")
        buf.write("=\3=\5=\u02af\n=\3>\3>\3>\5>\u02b4\n>\3>\3>\3?\3?\3?\3")
        buf.write("?\7?\u02bc\n?\f?\16?\u02bf\13?\3@\3@\3@\7@\u02c4\n@\f")
        buf.write("@\16@\u02c7\13@\3A\3A\3A\5A\u02cc\nA\3B\3B\3C\3C\3D\3")
        buf.write("D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3I\3I\3I\3I\3I\3I\5I\u02e4")
        buf.write("\nI\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\5J\u02f1\nJ\3K\3")
        buf.write("K\3L\3L\3M\3M\3M\2\7>@BDFN\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a")
        buf.write("\u008c\u008e\u0090\u0092\u0094\u0096\u0098\2\t\4\2--\67")
        buf.write("\67\3\2\36#\3\2\31\32\3\2\33\35\4\2\32\32&&\3\2\678\4")
        buf.write("\2\13\16\67\67\2\u0307\2\u009b\3\2\2\2\4\u00b0\3\2\2\2")
        buf.write("\6\u00b2\3\2\2\2\b\u00bb\3\2\2\2\n\u00c1\3\2\2\2\f\u00c7")
        buf.write("\3\2\2\2\16\u00cb\3\2\2\2\20\u00ce\3\2\2\2\22\u00d5\3")
        buf.write("\2\2\2\24\u00d9\3\2\2\2\26\u00dd\3\2\2\2\30\u00e5\3\2")
        buf.write("\2\2\32\u00e9\3\2\2\2\34\u00eb\3\2\2\2\36\u00f2\3\2\2")
        buf.write("\2 \u00f4\3\2\2\2\"\u00fc\3\2\2\2$\u00fe\3\2\2\2&\u0102")
        buf.write("\3\2\2\2(\u0104\3\2\2\2*\u0117\3\2\2\2,\u012b\3\2\2\2")
        buf.write(".\u0136\3\2\2\2\60\u013c\3\2\2\2\62\u0146\3\2\2\2\64\u0148")
        buf.write("\3\2\2\2\66\u0158\3\2\2\28\u015a\3\2\2\2:\u0163\3\2\2")
        buf.write("\2<\u016d\3\2\2\2>\u016f\3\2\2\2@\u017a\3\2\2\2B\u0185")
        buf.write("\3\2\2\2D\u0191\3\2\2\2F\u019d\3\2\2\2H\u01ad\3\2\2\2")
        buf.write("J\u01af\3\2\2\2L\u01c0\3\2\2\2N\u01c6\3\2\2\2P\u01ca\3")
        buf.write("\2\2\2R\u01d0\3\2\2\2T\u01f0\3\2\2\2V\u01f4\3\2\2\2X\u020e")
        buf.write("\3\2\2\2Z\u0210\3\2\2\2\\\u021c\3\2\2\2^\u021e\3\2\2\2")
        buf.write("`\u0244\3\2\2\2b\u0256\3\2\2\2d\u025a\3\2\2\2f\u0276\3")
        buf.write("\2\2\2h\u0278\3\2\2\2j\u027c\3\2\2\2l\u027e\3\2\2\2n\u0280")
        buf.write("\3\2\2\2p\u0290\3\2\2\2r\u0292\3\2\2\2t\u0296\3\2\2\2")
        buf.write("v\u02a5\3\2\2\2x\u02ae\3\2\2\2z\u02b0\3\2\2\2|\u02bd\3")
        buf.write("\2\2\2~\u02c0\3\2\2\2\u0080\u02cb\3\2\2\2\u0082\u02cd")
        buf.write("\3\2\2\2\u0084\u02cf\3\2\2\2\u0086\u02d1\3\2\2\2\u0088")
        buf.write("\u02d3\3\2\2\2\u008a\u02d5\3\2\2\2\u008c\u02d7\3\2\2\2")
        buf.write("\u008e\u02d9\3\2\2\2\u0090\u02e3\3\2\2\2\u0092\u02f0\3")
        buf.write("\2\2\2\u0094\u02f2\3\2\2\2\u0096\u02f4\3\2\2\2\u0098\u02f6")
        buf.write("\3\2\2\2\u009a\u009c\5\4\3\2\u009b\u009a\3\2\2\2\u009c")
        buf.write("\u009d\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2")
        buf.write("\u009e\u009f\3\2\2\2\u009f\u00a0\7\2\2\3\u00a0\3\3\2\2")
        buf.write("\2\u00a1\u00a2\5\6\4\2\u00a2\u00a3\5\u0098M\2\u00a3\u00b1")
        buf.write("\3\2\2\2\u00a4\u00a5\5*\26\2\u00a5\u00a6\5\u0098M\2\u00a6")
        buf.write("\u00b1\3\2\2\2\u00a7\u00a8\5\20\t\2\u00a8\u00a9\5\u0098")
        buf.write("M\2\u00a9\u00b1\3\2\2\2\u00aa\u00ab\5(\25\2\u00ab\u00ac")
        buf.write("\5\u0098M\2\u00ac\u00b1\3\2\2\2\u00ad\u00ae\5\62\32\2")
        buf.write("\u00ae\u00af\5\u0098M\2\u00af\u00b1\3\2\2\2\u00b0\u00a1")
        buf.write("\3\2\2\2\u00b0\u00a4\3\2\2\2\u00b0\u00a7\3\2\2\2\u00b0")
        buf.write("\u00aa\3\2\2\2\u00b0\u00ad\3\2\2\2\u00b1\5\3\2\2\2\u00b2")
        buf.write("\u00b3\7\23\2\2\u00b3\u00b4\7\67\2\2\u00b4\u00b5\5\b\5")
        buf.write("\2\u00b5\7\3\2\2\2\u00b6\u00b7\5\n\6\2\u00b7\u00b8\5\16")
        buf.write("\b\2\u00b8\u00bc\3\2\2\2\u00b9\u00bc\5\n\6\2\u00ba\u00bc")
        buf.write("\5\16\b\2\u00bb\u00b6\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb")
        buf.write("\u00ba\3\2\2\2\u00bc\t\3\2\2\2\u00bd\u00c2\5\u0096L\2")
        buf.write("\u00be\u00bf\5\f\7\2\u00bf\u00c0\5\u0096L\2\u00c0\u00c2")
        buf.write("\3\2\2\2\u00c1\u00bd\3\2\2\2\u00c1\u00be\3\2\2\2\u00c2")
        buf.write("\13\3\2\2\2\u00c3\u00c4\7\62\2\2\u00c4\u00c5\5\u0094K")
        buf.write("\2\u00c5\u00c6\7\63\2\2\u00c6\u00c8\3\2\2\2\u00c7\u00c3")
        buf.write("\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9")
        buf.write("\u00ca\3\2\2\2\u00ca\r\3\2\2\2\u00cb\u00cc\7\27\2\2\u00cc")
        buf.write("\u00cd\5<\37\2\u00cd\17\3\2\2\2\u00ce\u00cf\7\22\2\2\u00cf")
        buf.write("\u00d1\7\67\2\2\u00d0\u00d2\5\n\6\2\u00d1\u00d0\3\2\2")
        buf.write("\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4")
        buf.write("\5\16\b\2\u00d4\21\3\2\2\2\u00d5\u00d6\5\f\7\2\u00d6\u00d7")
        buf.write("\5\u0096L\2\u00d7\u00d8\5\24\13\2\u00d8\23\3\2\2\2\u00d9")
        buf.write("\u00da\7\60\2\2\u00da\u00db\5\26\f\2\u00db\u00dc\7\61")
        buf.write("\2\2\u00dc\25\3\2\2\2\u00dd\u00de\5\32\16\2\u00de\u00df")
        buf.write("\5\30\r\2\u00df\27\3\2\2\2\u00e0\u00e1\7\64\2\2\u00e1")
        buf.write("\u00e2\5\32\16\2\u00e2\u00e3\5\30\r\2\u00e3\u00e6\3\2")
        buf.write("\2\2\u00e4\u00e6\3\2\2\2\u00e5\u00e0\3\2\2\2\u00e5\u00e4")
        buf.write("\3\2\2\2\u00e6\31\3\2\2\2\u00e7\u00ea\5\24\13\2\u00e8")
        buf.write("\u00ea\5\u0090I\2\u00e9\u00e7\3\2\2\2\u00e9\u00e8\3\2")
        buf.write("\2\2\u00ea\33\3\2\2\2\u00eb\u00ec\7\67\2\2\u00ec\u00ed")
        buf.write("\7\60\2\2\u00ed\u00ee\5\36\20\2\u00ee\u00ef\7\61\2\2\u00ef")
        buf.write("\35\3\2\2\2\u00f0\u00f3\5 \21\2\u00f1\u00f3\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3\37\3\2\2\2\u00f4")
        buf.write("\u00f5\5$\23\2\u00f5\u00f6\5\"\22\2\u00f6!\3\2\2\2\u00f7")
        buf.write("\u00f8\7\64\2\2\u00f8\u00f9\5$\23\2\u00f9\u00fa\5\"\22")
        buf.write("\2\u00fa\u00fd\3\2\2\2\u00fb\u00fd\3\2\2\2\u00fc\u00f7")
        buf.write("\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd#\3\2\2\2\u00fe\u00ff")
        buf.write("\7\67\2\2\u00ff\u0100\7\66\2\2\u0100\u0101\5&\24\2\u0101")
        buf.write("%\3\2\2\2\u0102\u0103\5<\37\2\u0103\'\3\2\2\2\u0104\u0105")
        buf.write("\7\7\2\2\u0105\u0106\7.\2\2\u0106\u0107\7\67\2\2\u0107")
        buf.write("\u0108\7\67\2\2\u0108\u0109\7/\2\2\u0109\u010a\7\67\2")
        buf.write("\2\u010a\u010b\7.\2\2\u010b\u010c\5.\30\2\u010c\u010d")
        buf.write("\7/\2\2\u010d\u010e\5,\27\2\u010e\u0112\7\60\2\2\u010f")
        buf.write("\u0111\5T+\2\u0110\u010f\3\2\2\2\u0111\u0114\3\2\2\2\u0112")
        buf.write("\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0115\3\2\2\2")
        buf.write("\u0114\u0112\3\2\2\2\u0115\u0116\7\61\2\2\u0116)\3\2\2")
        buf.write("\2\u0117\u0118\7\7\2\2\u0118\u0119\7\67\2\2\u0119\u011a")
        buf.write("\7.\2\2\u011a\u011b\5.\30\2\u011b\u011c\7/\2\2\u011c\u011d")
        buf.write("\5,\27\2\u011d\u0121\7\60\2\2\u011e\u0120\5T+\2\u011f")
        buf.write("\u011e\3\2\2\2\u0120\u0123\3\2\2\2\u0121\u011f\3\2\2\2")
        buf.write("\u0121\u0122\3\2\2\2\u0122\u0124\3\2\2\2\u0123\u0121\3")
        buf.write("\2\2\2\u0124\u0125\7\61\2\2\u0125+\3\2\2\2\u0126\u012c")
        buf.write("\5\u0096L\2\u0127\u0128\5\f\7\2\u0128\u0129\5\u0096L\2")
        buf.write("\u0129\u012c\3\2\2\2\u012a\u012c\3\2\2\2\u012b\u0126\3")
        buf.write("\2\2\2\u012b\u0127\3\2\2\2\u012b\u012a\3\2\2\2\u012c-")
        buf.write("\3\2\2\2\u012d\u012e\5\60\31\2\u012e\u012f\5\n\6\2\u012f")
        buf.write("\u0130\7\64\2\2\u0130\u0131\5.\30\2\u0131\u0137\3\2\2")
        buf.write("\2\u0132\u0133\5\60\31\2\u0133\u0134\5\n\6\2\u0134\u0137")
        buf.write("\3\2\2\2\u0135\u0137\3\2\2\2\u0136\u012d\3\2\2\2\u0136")
        buf.write("\u0132\3\2\2\2\u0136\u0135\3\2\2\2\u0137/\3\2\2\2\u0138")
        buf.write("\u013d\7\67\2\2\u0139\u013a\7\67\2\2\u013a\u013b\7\64")
        buf.write("\2\2\u013b\u013d\5\60\31\2\u013c\u0138\3\2\2\2\u013c\u0139")
        buf.write("\3\2\2\2\u013d\61\3\2\2\2\u013e\u013f\7\b\2\2\u013f\u0140")
        buf.write("\7\67\2\2\u0140\u0141\7\t\2\2\u0141\u0147\5\64\33\2\u0142")
        buf.write("\u0143\7\b\2\2\u0143\u0144\7\67\2\2\u0144\u0145\7\n\2")
        buf.write("\2\u0145\u0147\58\35\2\u0146\u013e\3\2\2\2\u0146\u0142")
        buf.write("\3\2\2\2\u0147\63\3\2\2\2\u0148\u014c\7\60\2\2\u0149\u014b")
        buf.write("\5\66\34\2\u014a\u0149\3\2\2\2\u014b\u014e\3\2\2\2\u014c")
        buf.write("\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014f\3\2\2\2")
        buf.write("\u014e\u014c\3\2\2\2\u014f\u0150\7\61\2\2\u0150\65\3\2")
        buf.write("\2\2\u0151\u0152\7\67\2\2\u0152\u0153\5\n\6\2\u0153\u0154")
        buf.write("\5\u0098M\2\u0154\u0159\3\2\2\2\u0155\u0156\5(\25\2\u0156")
        buf.write("\u0157\5\u0098M\2\u0157\u0159\3\2\2\2\u0158\u0151\3\2")
        buf.write("\2\2\u0158\u0155\3\2\2\2\u0159\67\3\2\2\2\u015a\u015e")
        buf.write("\7\60\2\2\u015b\u015d\5:\36\2\u015c\u015b\3\2\2\2\u015d")
        buf.write("\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015f\u0161\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0162\7")
        buf.write("\61\2\2\u01629\3\2\2\2\u0163\u0164\7\67\2\2\u0164\u0165")
        buf.write("\7.\2\2\u0165\u0166\5.\30\2\u0166\u0167\7/\2\2\u0167\u0168")
        buf.write("\5,\27\2\u0168\u0169\5\u0098M\2\u0169;\3\2\2\2\u016a\u016e")
        buf.write("\5> \2\u016b\u016e\5\22\n\2\u016c\u016e\5\34\17\2\u016d")
        buf.write("\u016a\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016c\3\2\2\2")
        buf.write("\u016e=\3\2\2\2\u016f\u0170\b \1\2\u0170\u0171\5@!\2\u0171")
        buf.write("\u0177\3\2\2\2\u0172\u0173\f\4\2\2\u0173\u0174\7%\2\2")
        buf.write("\u0174\u0176\5@!\2\u0175\u0172\3\2\2\2\u0176\u0179\3\2")
        buf.write("\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178?\3")
        buf.write("\2\2\2\u0179\u0177\3\2\2\2\u017a\u017b\b!\1\2\u017b\u017c")
        buf.write("\5B\"\2\u017c\u0182\3\2\2\2\u017d\u017e\f\4\2\2\u017e")
        buf.write("\u017f\7$\2\2\u017f\u0181\5B\"\2\u0180\u017d\3\2\2\2\u0181")
        buf.write("\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2")
        buf.write("\u0183A\3\2\2\2\u0184\u0182\3\2\2\2\u0185\u0186\b\"\1")
        buf.write("\2\u0186\u0187\5D#\2\u0187\u018e\3\2\2\2\u0188\u0189\f")
        buf.write("\4\2\2\u0189\u018a\5\u0088E\2\u018a\u018b\5D#\2\u018b")
        buf.write("\u018d\3\2\2\2\u018c\u0188\3\2\2\2\u018d\u0190\3\2\2\2")
        buf.write("\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018fC\3\2\2")
        buf.write("\2\u0190\u018e\3\2\2\2\u0191\u0192\b#\1\2\u0192\u0193")
        buf.write("\5F$\2\u0193\u019a\3\2\2\2\u0194\u0195\f\4\2\2\u0195\u0196")
        buf.write("\5\u008aF\2\u0196\u0197\5F$\2\u0197\u0199\3\2\2\2\u0198")
        buf.write("\u0194\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3\2\2\2")
        buf.write("\u019a\u019b\3\2\2\2\u019bE\3\2\2\2\u019c\u019a\3\2\2")
        buf.write("\2\u019d\u019e\b$\1\2\u019e\u019f\5H%\2\u019f\u01a6\3")
        buf.write("\2\2\2\u01a0\u01a1\f\4\2\2\u01a1\u01a2\5\u008cG\2\u01a2")
        buf.write("\u01a3\5H%\2\u01a3\u01a5\3\2\2\2\u01a4\u01a0\3\2\2\2\u01a5")
        buf.write("\u01a8\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2")
        buf.write("\u01a7G\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a9\u01aa\5\u008e")
        buf.write("H\2\u01aa\u01ab\5H%\2\u01ab\u01ae\3\2\2\2\u01ac\u01ae")
        buf.write("\5J&\2\u01ad\u01a9\3\2\2\2\u01ad\u01ac\3\2\2\2\u01aeI")
        buf.write("\3\2\2\2\u01af\u01b3\5\u0092J\2\u01b0\u01b2\5L\'\2\u01b1")
        buf.write("\u01b0\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1\3\2\2\2")
        buf.write("\u01b3\u01b4\3\2\2\2\u01b4K\3\2\2\2\u01b5\u01b3\3\2\2")
        buf.write("\2\u01b6\u01b7\7,\2\2\u01b7\u01b9\7\67\2\2\u01b8\u01ba")
        buf.write("\5P)\2\u01b9\u01b8\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bc")
        buf.write("\3\2\2\2\u01bb\u01bd\5N(\2\u01bc\u01bb\3\2\2\2\u01bc\u01bd")
        buf.write("\3\2\2\2\u01bd\u01c1\3\2\2\2\u01be\u01c1\5N(\2\u01bf\u01c1")
        buf.write("\5P)\2\u01c0\u01b6\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01bf")
        buf.write("\3\2\2\2\u01c1M\3\2\2\2\u01c2\u01c3\7\62\2\2\u01c3\u01c4")
        buf.write("\5<\37\2\u01c4\u01c5\7\63\2\2\u01c5\u01c7\3\2\2\2\u01c6")
        buf.write("\u01c2\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c6\3\2\2\2")
        buf.write("\u01c8\u01c9\3\2\2\2\u01c9O\3\2\2\2\u01ca\u01cc\7.\2\2")
        buf.write("\u01cb\u01cd\5R*\2\u01cc\u01cb\3\2\2\2\u01cc\u01cd\3\2")
        buf.write("\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf\7/\2\2\u01cfQ\3\2")
        buf.write("\2\2\u01d0\u01d5\5<\37\2\u01d1\u01d2\7\64\2\2\u01d2\u01d4")
        buf.write("\5<\37\2\u01d3\u01d1\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5")
        buf.write("\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6S\3\2\2\2\u01d7")
        buf.write("\u01d5\3\2\2\2\u01d8\u01d9\5V,\2\u01d9\u01da\5\u0098M")
        buf.write("\2\u01da\u01f1\3\2\2\2\u01db\u01dc\5X-\2\u01dc\u01dd\5")
        buf.write("\u0098M\2\u01dd\u01f1\3\2\2\2\u01de\u01df\5`\61\2\u01df")
        buf.write("\u01e0\5\u0098M\2\u01e0\u01f1\3\2\2\2\u01e1\u01e2\5d\63")
        buf.write("\2\u01e2\u01e3\5\u0098M\2\u01e3\u01f1\3\2\2\2\u01e4\u01e5")
        buf.write("\5p9\2\u01e5\u01e6\5\u0098M\2\u01e6\u01f1\3\2\2\2\u01e7")
        buf.write("\u01e8\5r:\2\u01e8\u01e9\5\u0098M\2\u01e9\u01f1\3\2\2")
        buf.write("\2\u01ea\u01eb\5t;\2\u01eb\u01ec\5\u0098M\2\u01ec\u01f1")
        buf.write("\3\2\2\2\u01ed\u01ee\5\u0080A\2\u01ee\u01ef\5\u0098M\2")
        buf.write("\u01ef\u01f1\3\2\2\2\u01f0\u01d8\3\2\2\2\u01f0\u01db\3")
        buf.write("\2\2\2\u01f0\u01de\3\2\2\2\u01f0\u01e1\3\2\2\2\u01f0\u01e4")
        buf.write("\3\2\2\2\u01f0\u01e7\3\2\2\2\u01f0\u01ea\3\2\2\2\u01f0")
        buf.write("\u01ed\3\2\2\2\u01f1U\3\2\2\2\u01f2\u01f5\5\6\4\2\u01f3")
        buf.write("\u01f5\5\20\t\2\u01f4\u01f2\3\2\2\2\u01f4\u01f3\3\2\2")
        buf.write("\2\u01f5W\3\2\2\2\u01f6\u01f7\5Z.\2\u01f7\u01f8\7\30\2")
        buf.write("\2\u01f8\u01f9\5^\60\2\u01f9\u020f\3\2\2\2\u01fa\u01fb")
        buf.write("\5Z.\2\u01fb\u01fc\7\'\2\2\u01fc\u01fd\5^\60\2\u01fd\u020f")
        buf.write("\3\2\2\2\u01fe\u01ff\5Z.\2\u01ff\u0200\7(\2\2\u0200\u0201")
        buf.write("\5^\60\2\u0201\u020f\3\2\2\2\u0202\u0203\5Z.\2\u0203\u0204")
        buf.write("\7)\2\2\u0204\u0205\5^\60\2\u0205\u020f\3\2\2\2\u0206")
        buf.write("\u0207\5Z.\2\u0207\u0208\7*\2\2\u0208\u0209\5^\60\2\u0209")
        buf.write("\u020f\3\2\2\2\u020a\u020b\5Z.\2\u020b\u020c\7+\2\2\u020c")
        buf.write("\u020d\5^\60\2\u020d\u020f\3\2\2\2\u020e\u01f6\3\2\2\2")
        buf.write("\u020e\u01fa\3\2\2\2\u020e\u01fe\3\2\2\2\u020e\u0202\3")
        buf.write("\2\2\2\u020e\u0206\3\2\2\2\u020e\u020a\3\2\2\2\u020fY")
        buf.write("\3\2\2\2\u0210\u0211\7\67\2\2\u0211\u0212\5\\/\2\u0212")
        buf.write("[\3\2\2\2\u0213\u0214\7,\2\2\u0214\u0215\7\67\2\2\u0215")
        buf.write("\u021d\5\\/\2\u0216\u0217\7\62\2\2\u0217\u0218\5<\37\2")
        buf.write("\u0218\u0219\7\63\2\2\u0219\u021a\5\\/\2\u021a\u021d\3")
        buf.write("\2\2\2\u021b\u021d\3\2\2\2\u021c\u0213\3\2\2\2\u021c\u0216")
        buf.write("\3\2\2\2\u021c\u021b\3\2\2\2\u021d]\3\2\2\2\u021e\u021f")
        buf.write("\5<\37\2\u021f_\3\2\2\2\u0220\u0221\7\3\2\2\u0221\u0222")
        buf.write("\7.\2\2\u0222\u0223\5<\37\2\u0223\u0224\7/\2\2\u0224\u0228")
        buf.write("\7\60\2\2\u0225\u0227\5T+\2\u0226\u0225\3\2\2\2\u0227")
        buf.write("\u022a\3\2\2\2\u0228\u0226\3\2\2\2\u0228\u0229\3\2\2\2")
        buf.write("\u0229\u022b\3\2\2\2\u022a\u0228\3\2\2\2\u022b\u022c\7")
        buf.write("\61\2\2\u022c\u0245\3\2\2\2\u022d\u022e\7\3\2\2\u022e")
        buf.write("\u022f\7.\2\2\u022f\u0230\5<\37\2\u0230\u0231\7/\2\2\u0231")
        buf.write("\u0235\7\60\2\2\u0232\u0234\5T+\2\u0233\u0232\3\2\2\2")
        buf.write("\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2\u0235\u0236\3")
        buf.write("\2\2\2\u0236\u0238\3\2\2\2\u0237\u0235\3\2\2\2\u0238\u0239")
        buf.write("\7\61\2\2\u0239\u023a\5b\62\2\u023a\u023b\7\4\2\2\u023b")
        buf.write("\u023f\7\60\2\2\u023c\u023e\5T+\2\u023d\u023c\3\2\2\2")
        buf.write("\u023e\u0241\3\2\2\2\u023f\u023d\3\2\2\2\u023f\u0240\3")
        buf.write("\2\2\2\u0240\u0242\3\2\2\2\u0241\u023f\3\2\2\2\u0242\u0243")
        buf.write("\7\61\2\2\u0243\u0245\3\2\2\2\u0244\u0220\3\2\2\2\u0244")
        buf.write("\u022d\3\2\2\2\u0245a\3\2\2\2\u0246\u0247\7\4\2\2\u0247")
        buf.write("\u0248\7\3\2\2\u0248\u0249\7.\2\2\u0249\u024a\5<\37\2")
        buf.write("\u024a\u024b\7/\2\2\u024b\u024f\7\60\2\2\u024c\u024e\5")
        buf.write("T+\2\u024d\u024c\3\2\2\2\u024e\u0251\3\2\2\2\u024f\u024d")
        buf.write("\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u0252\3\2\2\2\u0251")
        buf.write("\u024f\3\2\2\2\u0252\u0253\7\61\2\2\u0253\u0254\5b\62")
        buf.write("\2\u0254\u0257\3\2\2\2\u0255\u0257\3\2\2\2\u0256\u0246")
        buf.write("\3\2\2\2\u0256\u0255\3\2\2\2\u0257c\3\2\2\2\u0258\u025b")
        buf.write("\5f\64\2\u0259\u025b\5n8\2\u025a\u0258\3\2\2\2\u025a\u0259")
        buf.write("\3\2\2\2\u025be\3\2\2\2\u025c\u025d\7\5\2\2\u025d\u025e")
        buf.write("\5h\65\2\u025e\u0262\7\60\2\2\u025f\u0261\5T+\2\u0260")
        buf.write("\u025f\3\2\2\2\u0261\u0264\3\2\2\2\u0262\u0260\3\2\2\2")
        buf.write("\u0262\u0263\3\2\2\2\u0263\u0265\3\2\2\2\u0264\u0262\3")
        buf.write("\2\2\2\u0265\u0266\7\61\2\2\u0266\u0277\3\2\2\2\u0267")
        buf.write("\u0268\7\5\2\2\u0268\u0269\5j\66\2\u0269\u026a\7\65\2")
        buf.write("\2\u026a\u026b\5h\65\2\u026b\u026c\7\65\2\2\u026c\u026d")
        buf.write("\5l\67\2\u026d\u0271\7\60\2\2\u026e\u0270\5T+\2\u026f")
        buf.write("\u026e\3\2\2\2\u0270\u0273\3\2\2\2\u0271\u026f\3\2\2\2")
        buf.write("\u0271\u0272\3\2\2\2\u0272\u0274\3\2\2\2\u0273\u0271\3")
        buf.write("\2\2\2\u0274\u0275\7\61\2\2\u0275\u0277\3\2\2\2\u0276")
        buf.write("\u025c\3\2\2\2\u0276\u0267\3\2\2\2\u0277g\3\2\2\2\u0278")
        buf.write("\u0279\5<\37\2\u0279i\3\2\2\2\u027a\u027d\5X-\2\u027b")
        buf.write("\u027d\5\6\4\2\u027c\u027a\3\2\2\2\u027c\u027b\3\2\2\2")
        buf.write("\u027dk\3\2\2\2\u027e\u027f\5X-\2\u027fm\3\2\2\2\u0280")
        buf.write("\u0281\7\5\2\2\u0281\u0282\5\u0082B\2\u0282\u0283\7\64")
        buf.write("\2\2\u0283\u0284\5\u0084C\2\u0284\u0285\7\30\2\2\u0285")
        buf.write("\u0286\7\26\2\2\u0286\u0287\5\u0086D\2\u0287\u028b\7\60")
        buf.write("\2\2\u0288\u028a\5T+\2\u0289\u0288\3\2\2\2\u028a\u028d")
        buf.write("\3\2\2\2\u028b\u0289\3\2\2\2\u028b\u028c\3\2\2\2\u028c")
        buf.write("\u028e\3\2\2\2\u028d\u028b\3\2\2\2\u028e\u028f\7\61\2")
        buf.write("\2\u028fo\3\2\2\2\u0290\u0291\7\25\2\2\u0291q\3\2\2\2")
        buf.write("\u0292\u0293\7\24\2\2\u0293s\3\2\2\2\u0294\u0297\5v<\2")
        buf.write("\u0295\u0297\5z>\2\u0296\u0294\3\2\2\2\u0296\u0295\3\2")
        buf.write("\2\2\u0297u\3\2\2\2\u0298\u0299\7\67\2\2\u0299\u029a\5")
        buf.write("|?\2\u029a\u029b\7,\2\2\u029b\u029c\5x=\2\u029c\u02a6")
        buf.write("\3\2\2\2\u029d\u029e\7\67\2\2\u029e\u02a0\7.\2\2\u029f")
        buf.write("\u02a1\5~@\2\u02a0\u029f\3\2\2\2\u02a0\u02a1\3\2\2\2\u02a1")
        buf.write("\u02a2\3\2\2\2\u02a2\u02a3\7/\2\2\u02a3\u02a4\7,\2\2\u02a4")
        buf.write("\u02a6\5x=\2\u02a5\u0298\3\2\2\2\u02a5\u029d\3\2\2\2\u02a6")
        buf.write("w\3\2\2\2\u02a7\u02af\5v<\2\u02a8\u02a9\7\67\2\2\u02a9")
        buf.write("\u02ab\7.\2\2\u02aa\u02ac\5~@\2\u02ab\u02aa\3\2\2\2\u02ab")
        buf.write("\u02ac\3\2\2\2\u02ac\u02ad\3\2\2\2\u02ad\u02af\7/\2\2")
        buf.write("\u02ae\u02a7\3\2\2\2\u02ae\u02a8\3\2\2\2\u02afy\3\2\2")
        buf.write("\2\u02b0\u02b1\7\67\2\2\u02b1\u02b3\7.\2\2\u02b2\u02b4")
        buf.write("\5~@\2\u02b3\u02b2\3\2\2\2\u02b3\u02b4\3\2\2\2\u02b4\u02b5")
        buf.write("\3\2\2\2\u02b5\u02b6\7/\2\2\u02b6{\3\2\2\2\u02b7\u02b8")
        buf.write("\7\62\2\2\u02b8\u02b9\5<\37\2\u02b9\u02ba\7\63\2\2\u02ba")
        buf.write("\u02bc\3\2\2\2\u02bb\u02b7\3\2\2\2\u02bc\u02bf\3\2\2\2")
        buf.write("\u02bd\u02bb\3\2\2\2\u02bd\u02be\3\2\2\2\u02be}\3\2\2")
        buf.write("\2\u02bf\u02bd\3\2\2\2\u02c0\u02c5\5<\37\2\u02c1\u02c2")
        buf.write("\7\64\2\2\u02c2\u02c4\5<\37\2\u02c3\u02c1\3\2\2\2\u02c4")
        buf.write("\u02c7\3\2\2\2\u02c5\u02c3\3\2\2\2\u02c5\u02c6\3\2\2\2")
        buf.write("\u02c6\177\3\2\2\2\u02c7\u02c5\3\2\2\2\u02c8\u02c9\7\6")
        buf.write("\2\2\u02c9\u02cc\5<\37\2\u02ca\u02cc\7\6\2\2\u02cb\u02c8")
        buf.write("\3\2\2\2\u02cb\u02ca\3\2\2\2\u02cc\u0081\3\2\2\2\u02cd")
        buf.write("\u02ce\t\2\2\2\u02ce\u0083\3\2\2\2\u02cf\u02d0\7\67\2")
        buf.write("\2\u02d0\u0085\3\2\2\2\u02d1\u02d2\5<\37\2\u02d2\u0087")
        buf.write("\3\2\2\2\u02d3\u02d4\t\3\2\2\u02d4\u0089\3\2\2\2\u02d5")
        buf.write("\u02d6\t\4\2\2\u02d6\u008b\3\2\2\2\u02d7\u02d8\t\5\2\2")
        buf.write("\u02d8\u008d\3\2\2\2\u02d9\u02da\t\6\2\2\u02da\u008f\3")
        buf.write("\2\2\2\u02db\u02e4\78\2\2\u02dc\u02e4\79\2\2\u02dd\u02e4")
        buf.write("\7:\2\2\u02de\u02e4\7\17\2\2\u02df\u02e4\7\20\2\2\u02e0")
        buf.write("\u02e4\7\21\2\2\u02e1\u02e4\5\34\17\2\u02e2\u02e4\7\67")
        buf.write("\2\2\u02e3\u02db\3\2\2\2\u02e3\u02dc\3\2\2\2\u02e3\u02dd")
        buf.write("\3\2\2\2\u02e3\u02de\3\2\2\2\u02e3\u02df\3\2\2\2\u02e3")
        buf.write("\u02e0\3\2\2\2\u02e3\u02e1\3\2\2\2\u02e3\u02e2\3\2\2\2")
        buf.write("\u02e4\u0091\3\2\2\2\u02e5\u02f1\7\67\2\2\u02e6\u02f1")
        buf.write("\78\2\2\u02e7\u02f1\79\2\2\u02e8\u02f1\7:\2\2\u02e9\u02f1")
        buf.write("\7\17\2\2\u02ea\u02f1\7\20\2\2\u02eb\u02f1\7\21\2\2\u02ec")
        buf.write("\u02ed\7.\2\2\u02ed\u02ee\5<\37\2\u02ee\u02ef\7/\2\2\u02ef")
        buf.write("\u02f1\3\2\2\2\u02f0\u02e5\3\2\2\2\u02f0\u02e6\3\2\2\2")
        buf.write("\u02f0\u02e7\3\2\2\2\u02f0\u02e8\3\2\2\2\u02f0\u02e9\3")
        buf.write("\2\2\2\u02f0\u02ea\3\2\2\2\u02f0\u02eb\3\2\2\2\u02f0\u02ec")
        buf.write("\3\2\2\2\u02f1\u0093\3\2\2\2\u02f2\u02f3\t\7\2\2\u02f3")
        buf.write("\u0095\3\2\2\2\u02f4\u02f5\t\b\2\2\u02f5\u0097\3\2\2\2")
        buf.write("\u02f6\u02f7\7\65\2\2\u02f7\u0099\3\2\2\2>\u009d\u00b0")
        buf.write("\u00bb\u00c1\u00c9\u00d1\u00e5\u00e9\u00f2\u00fc\u0112")
        buf.write("\u0121\u012b\u0136\u013c\u0146\u014c\u0158\u015e\u016d")
        buf.write("\u0177\u0182\u018e\u019a\u01a6\u01ad\u01b3\u01b9\u01bc")
        buf.write("\u01c0\u01c8\u01cc\u01d5\u01f0\u01f4\u020e\u021c\u0228")
        buf.write("\u0235\u023f\u0244\u024f\u0256\u025a\u0262\u0271\u0276")
        buf.write("\u027c\u028b\u0296\u02a0\u02a5\u02ab\u02ae\u02b3\u02bd")
        buf.write("\u02c5\u02cb\u02e3\u02f0")
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
    RULE_decl = 1
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
    RULE_structDeclBlock = 25
    RULE_structDeclField = 26
    RULE_interfaceDeclBlock = 27
    RULE_interfaceDeclField = 28
    RULE_expr = 29
    RULE_logicOrExpr = 30
    RULE_logicAndExpr = 31
    RULE_equalityExpr = 32
    RULE_additiveExpr = 33
    RULE_multiplicativeExpr = 34
    RULE_unaryExpr = 35
    RULE_primaryExpr = 36
    RULE_primarySuffix = 37
    RULE_arraySuffix = 38
    RULE_callSuffix = 39
    RULE_argList = 40
    RULE_statement = 41
    RULE_declarationStatement = 42
    RULE_assignStatement = 43
    RULE_assignStateLHS = 44
    RULE_assignStateLHSTail = 45
    RULE_assignStateRHS = 46
    RULE_ifStatement = 47
    RULE_elseIfStatement = 48
    RULE_forStatement = 49
    RULE_basicForStatement = 50
    RULE_forCondition = 51
    RULE_forInitilization = 52
    RULE_forUpdate = 53
    RULE_forRangeStatement = 54
    RULE_breakStatement = 55
    RULE_continueStatement = 56
    RULE_callStatement = 57
    RULE_methodCallStatement = 58
    RULE_methodCallStatementTail = 59
    RULE_funcCallStatement = 60
    RULE_callStatementArrayTail = 61
    RULE_callStatementParam = 62
    RULE_returnStatement = 63
    RULE_index = 64
    RULE_value = 65
    RULE_forArray = 66
    RULE_relationOp = 67
    RULE_addOp = 68
    RULE_mulOp = 69
    RULE_unaryOp = 70
    RULE_noArrayLit = 71
    RULE_term = 72
    RULE_intLitOrConstant = 73
    RULE_baseType = 74
    RULE_endOfStatement = 75

    ruleNames =  [ "program", "decl", "varDecl", "varDetail", "varDeclType", 
                   "arrayType", "varDeclExpr", "constDecl", "arrayLit", 
                   "arrayBlock", "arrayLitList", "arrayLitListTail", "arrayLitContent", 
                   "structLit", "optionalStructFields", "structFieldList", 
                   "structFieldListTail", "structFieldAssign", "structBlock", 
                   "methodDecl", "funcDecl", "funcType", "funcParam", "funcListIdentifiers", 
                   "typeDecl", "structDeclBlock", "structDeclField", "interfaceDeclBlock", 
                   "interfaceDeclField", "expr", "logicOrExpr", "logicAndExpr", 
                   "equalityExpr", "additiveExpr", "multiplicativeExpr", 
                   "unaryExpr", "primaryExpr", "primarySuffix", "arraySuffix", 
                   "callSuffix", "argList", "statement", "declarationStatement", 
                   "assignStatement", "assignStateLHS", "assignStateLHSTail", 
                   "assignStateRHS", "ifStatement", "elseIfStatement", "forStatement", 
                   "basicForStatement", "forCondition", "forInitilization", 
                   "forUpdate", "forRangeStatement", "breakStatement", "continueStatement", 
                   "callStatement", "methodCallStatement", "methodCallStatementTail", 
                   "funcCallStatement", "callStatementArrayTail", "callStatementParam", 
                   "returnStatement", "index", "value", "forArray", "relationOp", 
                   "addOp", "mulOp", "unaryOp", "noArrayLit", "term", "intLitOrConstant", 
                   "baseType", "endOfStatement" ]

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

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


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
            self.state = 153 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 152
                self.decl()
                self.state = 155 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 157
            self.match(MiniGoParser.EOF)
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
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.varDecl()
                self.state = 160
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.funcDecl()
                self.state = 163
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.constDecl()
                self.state = 166
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 168
                self.methodDecl()
                self.state = 169
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 171
                self.typeDecl()
                self.state = 172
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
            self.state = 176
            self.match(MiniGoParser.VAR)
            self.state = 177
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 178
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
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.varDeclType()
                self.state = 181
                self.varDeclExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.varDeclType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 184
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
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.baseType()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.arrayType()
                self.state = 189
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

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACKET)
            else:
                return self.getToken(MiniGoParser.LBRACKET, i)

        def intLitOrConstant(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.IntLitOrConstantContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.IntLitOrConstantContext,i)


        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACKET)
            else:
                return self.getToken(MiniGoParser.RBRACKET, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 193
                self.match(MiniGoParser.LBRACKET)
                self.state = 194
                self.intLitOrConstant()
                self.state = 195
                self.match(MiniGoParser.RBRACKET)
                self.state = 199 
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


    class VarDeclExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECLARE(self):
            return self.getToken(MiniGoParser.DECLARE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(MiniGoParser.DECLARE)
            self.state = 202
            self.expr()
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


        def varDeclType(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclTypeContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(MiniGoParser.CONST)
            self.state = 205
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 206
                self.varDeclType()


            self.state = 209
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
            self.state = 211
            self.arrayType()
            self.state = 212
            self.baseType()
            self.state = 213
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
            self.state = 215
            self.match(MiniGoParser.LBRACE)
            self.state = 216
            self.arrayLitList()
            self.state = 217
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
            self.state = 219
            self.arrayLitContent()
            self.state = 220
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
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.match(MiniGoParser.COMMA)
                self.state = 223
                self.arrayLitContent()
                self.state = 224
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
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.arrayBlock()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
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
            self.state = 233
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 234
            self.match(MiniGoParser.LBRACE)
            self.state = 235
            self.optionalStructFields()
            self.state = 236
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
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
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
            self.state = 242
            self.structFieldAssign()
            self.state = 243
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
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(MiniGoParser.COMMA)
                self.state = 246
                self.structFieldAssign()
                self.state = 247
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
            self.state = 252
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 253
            self.match(MiniGoParser.COLON)
            self.state = 254
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
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.expr()
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
            self.state = 258
            self.match(MiniGoParser.FUNC)
            self.state = 259
            self.match(MiniGoParser.LPAREN)
            self.state = 260
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 261
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 262
            self.match(MiniGoParser.RPAREN)
            self.state = 263
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 264
            self.match(MiniGoParser.LPAREN)
            self.state = 265
            self.funcParam()
            self.state = 266
            self.match(MiniGoParser.RPAREN)
            self.state = 267
            self.funcType()
            self.state = 268
            self.match(MiniGoParser.LBRACE)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 269
                self.statement()
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 275
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
            self.state = 277
            self.match(MiniGoParser.FUNC)
            self.state = 278
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 279
            self.match(MiniGoParser.LPAREN)
            self.state = 280
            self.funcParam()
            self.state = 281
            self.match(MiniGoParser.RPAREN)
            self.state = 282
            self.funcType()
            self.state = 283
            self.match(MiniGoParser.LBRACE)
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 284
                self.statement()
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 290
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
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.baseType()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.arrayType()
                self.state = 294
                self.baseType()
                pass
            elif token in [MiniGoParser.LBRACE, MiniGoParser.SEMI]:
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
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.funcListIdentifiers()
                self.state = 300
                self.varDeclType()
                self.state = 301
                self.match(MiniGoParser.COMMA)
                self.state = 302
                self.funcParam()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.funcListIdentifiers()
                self.state = 305
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
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 312
                self.match(MiniGoParser.COMMA)
                self.state = 313
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
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(MiniGoParser.TYPE)
                self.state = 317
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 318
                self.match(MiniGoParser.STRUCT)
                self.state = 319
                self.structDeclBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.match(MiniGoParser.TYPE)
                self.state = 321
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 322
                self.match(MiniGoParser.INTERFACE)
                self.state = 323
                self.interfaceDeclBlock()
                pass


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

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def structDeclField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StructDeclFieldContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StructDeclFieldContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structDeclBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDeclBlock" ):
                return visitor.visitStructDeclBlock(self)
            else:
                return visitor.visitChildren(self)




    def structDeclBlock(self):

        localctx = MiniGoParser.StructDeclBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_structDeclBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(MiniGoParser.LBRACE)
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.FUNC or _la==MiniGoParser.IDENTIFIER:
                self.state = 327
                self.structDeclField()
                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 333
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

        def varDeclType(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclTypeContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structDeclField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDeclField" ):
                return visitor.visitStructDeclField(self)
            else:
                return visitor.visitChildren(self)




    def structDeclField(self):

        localctx = MiniGoParser.StructDeclFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_structDeclField)
        try:
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 336
                self.varDeclType()
                self.state = 337
                self.endOfStatement()
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.methodDecl()
                self.state = 340
                self.endOfStatement()
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


    class InterfaceDeclBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def interfaceDeclField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.InterfaceDeclFieldContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.InterfaceDeclFieldContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceDeclBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDeclBlock" ):
                return visitor.visitInterfaceDeclBlock(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDeclBlock(self):

        localctx = MiniGoParser.InterfaceDeclBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_interfaceDeclBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(MiniGoParser.LBRACE)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 345
                self.interfaceDeclField()
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 351
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceDeclField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDeclField" ):
                return visitor.visitInterfaceDeclField(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDeclField(self):

        localctx = MiniGoParser.InterfaceDeclFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_interfaceDeclField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 354
            self.match(MiniGoParser.LPAREN)
            self.state = 355
            self.funcParam()
            self.state = 356
            self.match(MiniGoParser.RPAREN)
            self.state = 357
            self.funcType()
            self.state = 358
            self.endOfStatement()
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


        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MiniGoParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.logicOrExpr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 362
                self.structLit()
                pass


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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_logicOrExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.logicAndExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 373
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogicOrExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicOrExpr)
                    self.state = 368
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 369
                    self.match(MiniGoParser.OR)
                    self.state = 370
                    self.logicAndExpr(0) 
                self.state = 375
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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_logicAndExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.equalityExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 384
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogicAndExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicAndExpr)
                    self.state = 379
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 380
                    self.match(MiniGoParser.AND)
                    self.state = 381
                    self.equalityExpr(0) 
                self.state = 386
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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_equalityExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.additiveExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 396
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.EqualityExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpr)
                    self.state = 390
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 391
                    self.relationOp()
                    self.state = 392
                    self.additiveExpr(0) 
                self.state = 398
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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_additiveExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.multiplicativeExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 408
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.AdditiveExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpr)
                    self.state = 402
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 403
                    self.addOp()
                    self.state = 404
                    self.multiplicativeExpr(0) 
                self.state = 410
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
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_multiplicativeExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.unaryExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 420
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.MultiplicativeExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpr)
                    self.state = 414
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 415
                    self.mulOp()
                    self.state = 416
                    self.unaryExpr() 
                self.state = 422
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
        self.enterRule(localctx, 70, self.RULE_unaryExpr)
        try:
            self.state = 427
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.unaryOp()
                self.state = 424
                self.unaryExpr()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.LPAREN, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
                self.primaryExpr()
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


        def primarySuffix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.PrimarySuffixContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.PrimarySuffixContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_primaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpr(self):

        localctx = MiniGoParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_primaryExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.term()
            self.state = 433
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 430
                    self.primarySuffix() 
                self.state = 435
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimarySuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def callSuffix(self):
            return self.getTypedRuleContext(MiniGoParser.CallSuffixContext,0)


        def arraySuffix(self):
            return self.getTypedRuleContext(MiniGoParser.ArraySuffixContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_primarySuffix

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimarySuffix" ):
                return visitor.visitPrimarySuffix(self)
            else:
                return visitor.visitChildren(self)




    def primarySuffix(self):

        localctx = MiniGoParser.PrimarySuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_primarySuffix)
        try:
            self.state = 446
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.match(MiniGoParser.DOT)
                self.state = 437
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 439
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 438
                    self.callSuffix()


                self.state = 442
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 441
                    self.arraySuffix()


                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.arraySuffix()
                pass
            elif token in [MiniGoParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 445
                self.callSuffix()
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


    class ArraySuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACKET)
            else:
                return self.getToken(MiniGoParser.LBRACKET, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACKET)
            else:
                return self.getToken(MiniGoParser.RBRACKET, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arraySuffix

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraySuffix" ):
                return visitor.visitArraySuffix(self)
            else:
                return visitor.visitChildren(self)




    def arraySuffix(self):

        localctx = MiniGoParser.ArraySuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_arraySuffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 448
                    self.match(MiniGoParser.LBRACKET)
                    self.state = 449
                    self.expr()
                    self.state = 450
                    self.match(MiniGoParser.RBRACKET)

                else:
                    raise NoViableAltException(self)
                self.state = 454 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallSuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def argList(self):
            return self.getTypedRuleContext(MiniGoParser.ArgListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callSuffix

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallSuffix" ):
                return visitor.visitCallSuffix(self)
            else:
                return visitor.visitChildren(self)




    def callSuffix(self):

        localctx = MiniGoParser.CallSuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_callSuffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.match(MiniGoParser.LPAREN)
            self.state = 458
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 457
                self.argList()


            self.state = 460
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_argList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = MiniGoParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.expr()
            self.state = 467
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 463
                self.match(MiniGoParser.COMMA)
                self.state = 464
                self.expr()
                self.state = 469
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 82, self.RULE_statement)
        try:
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                self.declarationStatement()
                self.state = 471
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 473
                self.assignStatement()
                self.state = 474
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 476
                self.ifStatement()
                self.state = 477
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 479
                self.forStatement()
                self.state = 480
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 482
                self.breakStatement()
                self.state = 483
                self.endOfStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 485
                self.continueStatement()
                self.state = 486
                self.endOfStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 488
                self.callStatement()
                self.state = 489
                self.endOfStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 491
                self.returnStatement()
                self.state = 492
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
        self.enterRule(localctx, 84, self.RULE_declarationStatement)
        try:
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                self.varDecl()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
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
        self.enterRule(localctx, 86, self.RULE_assignStatement)
        try:
            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 500
                self.assignStateLHS()
                self.state = 501
                self.match(MiniGoParser.ASSIGN)
                self.state = 502
                self.assignStateRHS()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 504
                self.assignStateLHS()
                self.state = 505
                self.match(MiniGoParser.PLUS_ASSIGN)
                self.state = 506
                self.assignStateRHS()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 508
                self.assignStateLHS()
                self.state = 509
                self.match(MiniGoParser.MINUS_ASSIGN)
                self.state = 510
                self.assignStateRHS()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 512
                self.assignStateLHS()
                self.state = 513
                self.match(MiniGoParser.MUL_ASSIGN)
                self.state = 514
                self.assignStateRHS()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 516
                self.assignStateLHS()
                self.state = 517
                self.match(MiniGoParser.DIV_ASSIGN)
                self.state = 518
                self.assignStateRHS()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 520
                self.assignStateLHS()
                self.state = 521
                self.match(MiniGoParser.MOD_ASSIGN)
                self.state = 522
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
        self.enterRule(localctx, 88, self.RULE_assignStateLHS)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 527
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
        self.enterRule(localctx, 90, self.RULE_assignStateLHSTail)
        try:
            self.state = 538
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 529
                self.match(MiniGoParser.DOT)
                self.state = 530
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 531
                self.assignStateLHSTail()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 532
                self.match(MiniGoParser.LBRACKET)
                self.state = 533
                self.expr()
                self.state = 534
                self.match(MiniGoParser.RBRACKET)
                self.state = 535
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


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignStateRHS

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStateRHS" ):
                return visitor.visitAssignStateRHS(self)
            else:
                return visitor.visitChildren(self)




    def assignStateRHS(self):

        localctx = MiniGoParser.AssignStateRHSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_assignStateRHS)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.expr()
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
        self.enterRule(localctx, 94, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.state = 578
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 542
                self.match(MiniGoParser.IF)
                self.state = 543
                self.match(MiniGoParser.LPAREN)
                self.state = 544
                self.expr()
                self.state = 545
                self.match(MiniGoParser.RPAREN)
                self.state = 546
                self.match(MiniGoParser.LBRACE)
                self.state = 550
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 547
                    self.statement()
                    self.state = 552
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 553
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 555
                self.match(MiniGoParser.IF)
                self.state = 556
                self.match(MiniGoParser.LPAREN)
                self.state = 557
                self.expr()
                self.state = 558
                self.match(MiniGoParser.RPAREN)
                self.state = 559
                self.match(MiniGoParser.LBRACE)
                self.state = 563
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 560
                    self.statement()
                    self.state = 565
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 566
                self.match(MiniGoParser.RBRACE)
                self.state = 567
                self.elseIfStatement()
                self.state = 568
                self.match(MiniGoParser.ELSE)
                self.state = 569
                self.match(MiniGoParser.LBRACE)
                self.state = 573
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 570
                    self.statement()
                    self.state = 575
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 576
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
        self.enterRule(localctx, 96, self.RULE_elseIfStatement)
        self._la = 0 # Token type
        try:
            self.state = 596
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 580
                self.match(MiniGoParser.ELSE)
                self.state = 581
                self.match(MiniGoParser.IF)
                self.state = 582
                self.match(MiniGoParser.LPAREN)
                self.state = 583
                self.expr()
                self.state = 584
                self.match(MiniGoParser.RPAREN)
                self.state = 585
                self.match(MiniGoParser.LBRACE)
                self.state = 589
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 586
                    self.statement()
                    self.state = 591
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 592
                self.match(MiniGoParser.RBRACE)
                self.state = 593
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
        self.enterRule(localctx, 98, self.RULE_forStatement)
        try:
            self.state = 600
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 598
                self.basicForStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 599
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
        self.enterRule(localctx, 100, self.RULE_basicForStatement)
        self._la = 0 # Token type
        try:
            self.state = 628
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 602
                self.match(MiniGoParser.FOR)
                self.state = 603
                self.forCondition()
                self.state = 604
                self.match(MiniGoParser.LBRACE)
                self.state = 608
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 605
                    self.statement()
                    self.state = 610
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 611
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 613
                self.match(MiniGoParser.FOR)
                self.state = 614
                self.forInitilization()
                self.state = 615
                self.match(MiniGoParser.SEMI)
                self.state = 616
                self.forCondition()
                self.state = 617
                self.match(MiniGoParser.SEMI)
                self.state = 618
                self.forUpdate()
                self.state = 619
                self.match(MiniGoParser.LBRACE)
                self.state = 623
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 620
                    self.statement()
                    self.state = 625
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 626
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
        self.enterRule(localctx, 102, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 630
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
        self.enterRule(localctx, 104, self.RULE_forInitilization)
        try:
            self.state = 634
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 632
                self.assignStatement()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 633
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
        self.enterRule(localctx, 106, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 636
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
        self.enterRule(localctx, 108, self.RULE_forRangeStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 638
            self.match(MiniGoParser.FOR)
            self.state = 639
            self.index()
            self.state = 640
            self.match(MiniGoParser.COMMA)
            self.state = 641
            self.value()
            self.state = 642
            self.match(MiniGoParser.ASSIGN)
            self.state = 643
            self.match(MiniGoParser.RANGE)
            self.state = 644
            self.forArray()
            self.state = 645
            self.match(MiniGoParser.LBRACE)
            self.state = 649
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 646
                self.statement()
                self.state = 651
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 652
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
        self.enterRule(localctx, 110, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 654
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
        self.enterRule(localctx, 112, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 656
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

        def methodCallStatement(self):
            return self.getTypedRuleContext(MiniGoParser.MethodCallStatementContext,0)


        def funcCallStatement(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def callStatement(self):

        localctx = MiniGoParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_callStatement)
        try:
            self.state = 660
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 658
                self.methodCallStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 659
                self.funcCallStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallStatementContext(ParserRuleContext):
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

        def methodCallStatementTail(self):
            return self.getTypedRuleContext(MiniGoParser.MethodCallStatementTailContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def callStatementParam(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementParamContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodCallStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCallStatement" ):
                return visitor.visitMethodCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def methodCallStatement(self):

        localctx = MiniGoParser.MethodCallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_methodCallStatement)
        self._la = 0 # Token type
        try:
            self.state = 675
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 662
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 663
                self.callStatementArrayTail()
                self.state = 664
                self.match(MiniGoParser.DOT)
                self.state = 665
                self.methodCallStatementTail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 667
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 668
                self.match(MiniGoParser.LPAREN)
                self.state = 670
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 669
                    self.callStatementParam()


                self.state = 672
                self.match(MiniGoParser.RPAREN)
                self.state = 673
                self.match(MiniGoParser.DOT)
                self.state = 674
                self.methodCallStatementTail()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallStatementTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodCallStatement(self):
            return self.getTypedRuleContext(MiniGoParser.MethodCallStatementContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def callStatementParam(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementParamContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodCallStatementTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCallStatementTail" ):
                return visitor.visitMethodCallStatementTail(self)
            else:
                return visitor.visitChildren(self)




    def methodCallStatementTail(self):

        localctx = MiniGoParser.MethodCallStatementTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_methodCallStatementTail)
        self._la = 0 # Token type
        try:
            self.state = 684
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 677
                self.methodCallStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 678
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 679
                self.match(MiniGoParser.LPAREN)
                self.state = 681
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 680
                    self.callStatementParam()


                self.state = 683
                self.match(MiniGoParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallStatementContext(ParserRuleContext):
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

        def callStatementParam(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementParamContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcCallStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallStatement" ):
                return visitor.visitFuncCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def funcCallStatement(self):

        localctx = MiniGoParser.FuncCallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_funcCallStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 686
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 687
            self.match(MiniGoParser.LPAREN)
            self.state = 689
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 688
                self.callStatementParam()


            self.state = 691
            self.match(MiniGoParser.RPAREN)
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

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACKET)
            else:
                return self.getToken(MiniGoParser.LBRACKET, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACKET)
            else:
                return self.getToken(MiniGoParser.RBRACKET, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_callStatementArrayTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatementArrayTail" ):
                return visitor.visitCallStatementArrayTail(self)
            else:
                return visitor.visitChildren(self)




    def callStatementArrayTail(self):

        localctx = MiniGoParser.CallStatementArrayTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_callStatementArrayTail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 699
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.LBRACKET:
                self.state = 693
                self.match(MiniGoParser.LBRACKET)
                self.state = 694
                self.expr()
                self.state = 695
                self.match(MiniGoParser.RBRACKET)
                self.state = 701
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_callStatementParam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatementParam" ):
                return visitor.visitCallStatementParam(self)
            else:
                return visitor.visitChildren(self)




    def callStatementParam(self):

        localctx = MiniGoParser.CallStatementParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_callStatementParam)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 702
            self.expr()
            self.state = 707
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 703
                self.match(MiniGoParser.COMMA)
                self.state = 704
                self.expr()
                self.state = 709
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MiniGoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_returnStatement)
        try:
            self.state = 713
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 710
                self.match(MiniGoParser.RETURN)
                self.state = 711
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 712
                self.match(MiniGoParser.RETURN)
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
        self.enterRule(localctx, 128, self.RULE_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 715
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
        self.enterRule(localctx, 130, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 717
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
        self.enterRule(localctx, 132, self.RULE_forArray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 719
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
        self.enterRule(localctx, 134, self.RULE_relationOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 721
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
        self.enterRule(localctx, 136, self.RULE_addOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 723
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
        self.enterRule(localctx, 138, self.RULE_mulOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 725
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
        self.enterRule(localctx, 140, self.RULE_unaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 727
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
        self.enterRule(localctx, 142, self.RULE_noArrayLit)
        try:
            self.state = 737
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 729
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 730
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 731
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 732
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 733
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 734
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 735
                self.structLit()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 736
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
        self.enterRule(localctx, 144, self.RULE_term)
        try:
            self.state = 750
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 739
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 740
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 741
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 742
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 743
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 744
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 745
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.LPAREN]:
                self.enterOuterAlt(localctx, 8)
                self.state = 746
                self.match(MiniGoParser.LPAREN)
                self.state = 747
                self.expr()
                self.state = 748
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
        self.enterRule(localctx, 146, self.RULE_intLitOrConstant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 752
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
        self.enterRule(localctx, 148, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 754
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

        def getRuleIndex(self):
            return MiniGoParser.RULE_endOfStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndOfStatement" ):
                return visitor.visitEndOfStatement(self)
            else:
                return visitor.visitChildren(self)




    def endOfStatement(self):

        localctx = MiniGoParser.EndOfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_endOfStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 756
            self.match(MiniGoParser.SEMI)
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
        self._predicates[30] = self.logicOrExpr_sempred
        self._predicates[31] = self.logicAndExpr_sempred
        self._predicates[32] = self.equalityExpr_sempred
        self._predicates[33] = self.additiveExpr_sempred
        self._predicates[34] = self.multiplicativeExpr_sempred
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
         




