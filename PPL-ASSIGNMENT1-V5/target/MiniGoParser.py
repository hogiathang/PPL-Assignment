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
        buf.write("\u030d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("M\4N\tN\3\2\6\2\u009e\n\2\r\2\16\2\u009f\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3\u00b3\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("\u00be\n\5\3\6\3\6\3\6\3\6\5\6\u00c4\n\6\3\7\3\7\3\7\3")
        buf.write("\7\6\7\u00ca\n\7\r\7\16\7\u00cb\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\5\t\u00d4\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\5\r\u00e8\n\r\3")
        buf.write("\16\3\16\5\16\u00ec\n\16\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\5\20\u00f5\n\20\3\21\3\21\3\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\5\22\u00ff\n\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u010f\n")
        buf.write("\25\3\25\3\25\3\25\3\25\7\25\u0115\n\25\f\25\16\25\u0118")
        buf.write("\13\25\3\25\3\25\3\26\3\26\3\26\3\26\5\26\u0120\n\26\3")
        buf.write("\26\3\26\3\26\3\26\7\26\u0126\n\26\f\26\16\26\u0129\13")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\5\27\u0132\n\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u013c\n")
        buf.write("\30\3\31\3\31\3\31\3\31\5\31\u0142\n\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\5\32\u014c\n\32\3\33\3\33\7")
        buf.write("\33\u0150\n\33\f\33\16\33\u0153\13\33\3\33\3\33\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\5\34\u015e\n\34\3\35\3\35")
        buf.write("\7\35\u0162\n\35\f\35\16\35\u0165\13\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\5\36\u016c\n\36\3\36\3\36\3\36\3\36\3\37\3")
        buf.write("\37\3 \3 \3 \3 \3 \3 \7 \u017a\n \f \16 \u017d\13 \3!")
        buf.write("\3!\3!\3!\3!\3!\7!\u0185\n!\f!\16!\u0188\13!\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\7\"\u0191\n\"\f\"\16\"\u0194\13\"\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\7#\u019d\n#\f#\16#\u01a0\13#\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\7$\u01a9\n$\f$\16$\u01ac\13$\3%\3%\3")
        buf.write("%\3%\5%\u01b2\n%\3&\3&\7&\u01b6\n&\f&\16&\u01b9\13&\3")
        buf.write("\'\3\'\3\'\5\'\u01be\n\'\3\'\5\'\u01c1\n\'\3\'\3\'\5\'")
        buf.write("\u01c5\n\'\3(\3(\3(\3(\6(\u01cb\n(\r(\16(\u01cc\3)\3)")
        buf.write("\5)\u01d1\n)\3)\3)\3*\3*\3*\7*\u01d8\n*\f*\16*\u01db\13")
        buf.write("*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\5+\u01f5\n+\3,\3,\5,\u01f9\n,\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\5-\u0213\n-\3.\3.\3.\3/\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\5/\u0221\n/\3\60\3\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\7\61\u022b\n\61\f\61\16\61\u022e\13\61\3\61\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\7\62\u023b")
        buf.write("\n\62\f\62\16\62\u023e\13\62\3\62\3\62\7\62\u0242\n\62")
        buf.write("\f\62\16\62\u0245\13\62\3\63\3\63\3\63\7\63\u024a\n\63")
        buf.write("\f\63\16\63\u024d\13\63\3\63\5\63\u0250\n\63\3\64\3\64")
        buf.write("\5\64\u0254\n\64\3\65\3\65\3\65\3\65\7\65\u025a\n\65\f")
        buf.write("\65\16\65\u025d\13\65\3\65\3\65\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\7\65\u0269\n\65\f\65\16\65\u026c\13")
        buf.write("\65\3\65\3\65\5\65\u0270\n\65\3\66\3\66\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u027d\n\67\38\38\3")
        buf.write("8\38\38\38\38\38\38\38\38\38\38\38\38\38\38\38\58\u0291")
        buf.write("\n8\39\39\39\39\39\39\39\39\39\79\u029c\n9\f9\169\u029f")
        buf.write("\139\39\39\3:\3:\3;\3;\3<\3<\5<\u02a9\n<\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\3=\5=\u02b3\n=\3=\3=\3=\5=\u02b8\n=\3>\3>\3>\3")
        buf.write(">\5>\u02be\n>\3>\5>\u02c1\n>\3?\3?\3?\5?\u02c6\n?\3?\3")
        buf.write("?\3@\3@\3@\3@\7@\u02ce\n@\f@\16@\u02d1\13@\3A\3A\3A\7")
        buf.write("A\u02d6\nA\fA\16A\u02d9\13A\3B\3B\3B\5B\u02de\nB\3C\3")
        buf.write("C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3J\3J\3J\3")
        buf.write("J\3J\3J\5J\u02f6\nJ\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3K\3")
        buf.write("K\3K\5K\u0305\nK\3L\3L\3M\3M\3N\3N\3N\2\7>@BDFO\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096")
        buf.write("\u0098\u009a\2\t\4\2--\67\67\3\2\36#\3\2\31\32\3\2\33")
        buf.write("\35\4\2\32\32&&\3\2\678\4\2\13\16\67\67\2\u0321\2\u009d")
        buf.write("\3\2\2\2\4\u00b2\3\2\2\2\6\u00b4\3\2\2\2\b\u00bd\3\2\2")
        buf.write("\2\n\u00c3\3\2\2\2\f\u00c9\3\2\2\2\16\u00cd\3\2\2\2\20")
        buf.write("\u00d0\3\2\2\2\22\u00d7\3\2\2\2\24\u00db\3\2\2\2\26\u00df")
        buf.write("\3\2\2\2\30\u00e7\3\2\2\2\32\u00eb\3\2\2\2\34\u00ed\3")
        buf.write("\2\2\2\36\u00f4\3\2\2\2 \u00f6\3\2\2\2\"\u00fe\3\2\2\2")
        buf.write("$\u0100\3\2\2\2&\u0104\3\2\2\2(\u0106\3\2\2\2*\u011b\3")
        buf.write("\2\2\2,\u0131\3\2\2\2.\u013b\3\2\2\2\60\u0141\3\2\2\2")
        buf.write("\62\u014b\3\2\2\2\64\u014d\3\2\2\2\66\u015d\3\2\2\28\u015f")
        buf.write("\3\2\2\2:\u0168\3\2\2\2<\u0171\3\2\2\2>\u0173\3\2\2\2")
        buf.write("@\u017e\3\2\2\2B\u0189\3\2\2\2D\u0195\3\2\2\2F\u01a1\3")
        buf.write("\2\2\2H\u01b1\3\2\2\2J\u01b3\3\2\2\2L\u01c4\3\2\2\2N\u01ca")
        buf.write("\3\2\2\2P\u01ce\3\2\2\2R\u01d4\3\2\2\2T\u01f4\3\2\2\2")
        buf.write("V\u01f8\3\2\2\2X\u0212\3\2\2\2Z\u0214\3\2\2\2\\\u0220")
        buf.write("\3\2\2\2^\u0222\3\2\2\2`\u0224\3\2\2\2b\u0243\3\2\2\2")
        buf.write("d\u024f\3\2\2\2f\u0253\3\2\2\2h\u026f\3\2\2\2j\u0271\3")
        buf.write("\2\2\2l\u027c\3\2\2\2n\u0290\3\2\2\2p\u0292\3\2\2\2r\u02a2")
        buf.write("\3\2\2\2t\u02a4\3\2\2\2v\u02a8\3\2\2\2x\u02b7\3\2\2\2")
        buf.write("z\u02c0\3\2\2\2|\u02c2\3\2\2\2~\u02cf\3\2\2\2\u0080\u02d2")
        buf.write("\3\2\2\2\u0082\u02dd\3\2\2\2\u0084\u02df\3\2\2\2\u0086")
        buf.write("\u02e1\3\2\2\2\u0088\u02e3\3\2\2\2\u008a\u02e5\3\2\2\2")
        buf.write("\u008c\u02e7\3\2\2\2\u008e\u02e9\3\2\2\2\u0090\u02eb\3")
        buf.write("\2\2\2\u0092\u02f5\3\2\2\2\u0094\u0304\3\2\2\2\u0096\u0306")
        buf.write("\3\2\2\2\u0098\u0308\3\2\2\2\u009a\u030a\3\2\2\2\u009c")
        buf.write("\u009e\5\4\3\2\u009d\u009c\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3")
        buf.write("\2\2\2\u00a1\u00a2\7\2\2\3\u00a2\3\3\2\2\2\u00a3\u00a4")
        buf.write("\5\6\4\2\u00a4\u00a5\5\u009aN\2\u00a5\u00b3\3\2\2\2\u00a6")
        buf.write("\u00a7\5*\26\2\u00a7\u00a8\5\u009aN\2\u00a8\u00b3\3\2")
        buf.write("\2\2\u00a9\u00aa\5\20\t\2\u00aa\u00ab\5\u009aN\2\u00ab")
        buf.write("\u00b3\3\2\2\2\u00ac\u00ad\5(\25\2\u00ad\u00ae\5\u009a")
        buf.write("N\2\u00ae\u00b3\3\2\2\2\u00af\u00b0\5\62\32\2\u00b0\u00b1")
        buf.write("\5\u009aN\2\u00b1\u00b3\3\2\2\2\u00b2\u00a3\3\2\2\2\u00b2")
        buf.write("\u00a6\3\2\2\2\u00b2\u00a9\3\2\2\2\u00b2\u00ac\3\2\2\2")
        buf.write("\u00b2\u00af\3\2\2\2\u00b3\5\3\2\2\2\u00b4\u00b5\7\23")
        buf.write("\2\2\u00b5\u00b6\7\67\2\2\u00b6\u00b7\5\b\5\2\u00b7\7")
        buf.write("\3\2\2\2\u00b8\u00b9\5\n\6\2\u00b9\u00ba\5\16\b\2\u00ba")
        buf.write("\u00be\3\2\2\2\u00bb\u00be\5\n\6\2\u00bc\u00be\5\16\b")
        buf.write("\2\u00bd\u00b8\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00bc")
        buf.write("\3\2\2\2\u00be\t\3\2\2\2\u00bf\u00c4\5\u0098M\2\u00c0")
        buf.write("\u00c1\5\f\7\2\u00c1\u00c2\5\u0098M\2\u00c2\u00c4\3\2")
        buf.write("\2\2\u00c3\u00bf\3\2\2\2\u00c3\u00c0\3\2\2\2\u00c4\13")
        buf.write("\3\2\2\2\u00c5\u00c6\7\62\2\2\u00c6\u00c7\5\u0096L\2\u00c7")
        buf.write("\u00c8\7\63\2\2\u00c8\u00ca\3\2\2\2\u00c9\u00c5\3\2\2")
        buf.write("\2\u00ca\u00cb\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc")
        buf.write("\3\2\2\2\u00cc\r\3\2\2\2\u00cd\u00ce\7\27\2\2\u00ce\u00cf")
        buf.write("\5<\37\2\u00cf\17\3\2\2\2\u00d0\u00d1\7\22\2\2\u00d1\u00d3")
        buf.write("\7\67\2\2\u00d2\u00d4\5\n\6\2\u00d3\u00d2\3\2\2\2\u00d3")
        buf.write("\u00d4\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d6\5\16\b")
        buf.write("\2\u00d6\21\3\2\2\2\u00d7\u00d8\5\f\7\2\u00d8\u00d9\5")
        buf.write("\u0098M\2\u00d9\u00da\5\24\13\2\u00da\23\3\2\2\2\u00db")
        buf.write("\u00dc\7\60\2\2\u00dc\u00dd\5\26\f\2\u00dd\u00de\7\61")
        buf.write("\2\2\u00de\25\3\2\2\2\u00df\u00e0\5\32\16\2\u00e0\u00e1")
        buf.write("\5\30\r\2\u00e1\27\3\2\2\2\u00e2\u00e3\7\64\2\2\u00e3")
        buf.write("\u00e4\5\32\16\2\u00e4\u00e5\5\30\r\2\u00e5\u00e8\3\2")
        buf.write("\2\2\u00e6\u00e8\3\2\2\2\u00e7\u00e2\3\2\2\2\u00e7\u00e6")
        buf.write("\3\2\2\2\u00e8\31\3\2\2\2\u00e9\u00ec\5\24\13\2\u00ea")
        buf.write("\u00ec\5\u0092J\2\u00eb\u00e9\3\2\2\2\u00eb\u00ea\3\2")
        buf.write("\2\2\u00ec\33\3\2\2\2\u00ed\u00ee\7\67\2\2\u00ee\u00ef")
        buf.write("\7\60\2\2\u00ef\u00f0\5\36\20\2\u00f0\u00f1\7\61\2\2\u00f1")
        buf.write("\35\3\2\2\2\u00f2\u00f5\5 \21\2\u00f3\u00f5\3\2\2\2\u00f4")
        buf.write("\u00f2\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5\37\3\2\2\2\u00f6")
        buf.write("\u00f7\5$\23\2\u00f7\u00f8\5\"\22\2\u00f8!\3\2\2\2\u00f9")
        buf.write("\u00fa\7\64\2\2\u00fa\u00fb\5$\23\2\u00fb\u00fc\5\"\22")
        buf.write("\2\u00fc\u00ff\3\2\2\2\u00fd\u00ff\3\2\2\2\u00fe\u00f9")
        buf.write("\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff#\3\2\2\2\u0100\u0101")
        buf.write("\7\67\2\2\u0101\u0102\7\66\2\2\u0102\u0103\5&\24\2\u0103")
        buf.write("%\3\2\2\2\u0104\u0105\5<\37\2\u0105\'\3\2\2\2\u0106\u0107")
        buf.write("\7\7\2\2\u0107\u0108\7.\2\2\u0108\u0109\7\67\2\2\u0109")
        buf.write("\u010a\7\67\2\2\u010a\u010b\7/\2\2\u010b\u010c\7\67\2")
        buf.write("\2\u010c\u010e\7.\2\2\u010d\u010f\5.\30\2\u010e\u010d")
        buf.write("\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0110\3\2\2\2\u0110")
        buf.write("\u0111\7/\2\2\u0111\u0112\5,\27\2\u0112\u0116\7\60\2\2")
        buf.write("\u0113\u0115\5T+\2\u0114\u0113\3\2\2\2\u0115\u0118\3\2")
        buf.write("\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0119")
        buf.write("\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011a\7\61\2\2\u011a")
        buf.write(")\3\2\2\2\u011b\u011c\7\7\2\2\u011c\u011d\7\67\2\2\u011d")
        buf.write("\u011f\7.\2\2\u011e\u0120\5.\30\2\u011f\u011e\3\2\2\2")
        buf.write("\u011f\u0120\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122\7")
        buf.write("/\2\2\u0122\u0123\5,\27\2\u0123\u0127\7\60\2\2\u0124\u0126")
        buf.write("\5T+\2\u0125\u0124\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125")
        buf.write("\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u012a\3\2\2\2\u0129")
        buf.write("\u0127\3\2\2\2\u012a\u012b\7\61\2\2\u012b+\3\2\2\2\u012c")
        buf.write("\u0132\5\u0098M\2\u012d\u012e\5\f\7\2\u012e\u012f\5\u0098")
        buf.write("M\2\u012f\u0132\3\2\2\2\u0130\u0132\3\2\2\2\u0131\u012c")
        buf.write("\3\2\2\2\u0131\u012d\3\2\2\2\u0131\u0130\3\2\2\2\u0132")
        buf.write("-\3\2\2\2\u0133\u0134\5\60\31\2\u0134\u0135\5\n\6\2\u0135")
        buf.write("\u0136\7\64\2\2\u0136\u0137\5.\30\2\u0137\u013c\3\2\2")
        buf.write("\2\u0138\u0139\5\60\31\2\u0139\u013a\5\n\6\2\u013a\u013c")
        buf.write("\3\2\2\2\u013b\u0133\3\2\2\2\u013b\u0138\3\2\2\2\u013c")
        buf.write("/\3\2\2\2\u013d\u0142\7\67\2\2\u013e\u013f\7\67\2\2\u013f")
        buf.write("\u0140\7\64\2\2\u0140\u0142\5\60\31\2\u0141\u013d\3\2")
        buf.write("\2\2\u0141\u013e\3\2\2\2\u0142\61\3\2\2\2\u0143\u0144")
        buf.write("\7\b\2\2\u0144\u0145\7\67\2\2\u0145\u0146\7\t\2\2\u0146")
        buf.write("\u014c\5\64\33\2\u0147\u0148\7\b\2\2\u0148\u0149\7\67")
        buf.write("\2\2\u0149\u014a\7\n\2\2\u014a\u014c\58\35\2\u014b\u0143")
        buf.write("\3\2\2\2\u014b\u0147\3\2\2\2\u014c\63\3\2\2\2\u014d\u0151")
        buf.write("\7\60\2\2\u014e\u0150\5\66\34\2\u014f\u014e\3\2\2\2\u0150")
        buf.write("\u0153\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2")
        buf.write("\u0152\u0154\3\2\2\2\u0153\u0151\3\2\2\2\u0154\u0155\7")
        buf.write("\61\2\2\u0155\65\3\2\2\2\u0156\u0157\7\67\2\2\u0157\u0158")
        buf.write("\5\n\6\2\u0158\u0159\5\u009aN\2\u0159\u015e\3\2\2\2\u015a")
        buf.write("\u015b\5(\25\2\u015b\u015c\5\u009aN\2\u015c\u015e\3\2")
        buf.write("\2\2\u015d\u0156\3\2\2\2\u015d\u015a\3\2\2\2\u015e\67")
        buf.write("\3\2\2\2\u015f\u0163\7\60\2\2\u0160\u0162\5:\36\2\u0161")
        buf.write("\u0160\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3\2\2\2")
        buf.write("\u0163\u0164\3\2\2\2\u0164\u0166\3\2\2\2\u0165\u0163\3")
        buf.write("\2\2\2\u0166\u0167\7\61\2\2\u01679\3\2\2\2\u0168\u0169")
        buf.write("\7\67\2\2\u0169\u016b\7.\2\2\u016a\u016c\5.\30\2\u016b")
        buf.write("\u016a\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d\3\2\2\2")
        buf.write("\u016d\u016e\7/\2\2\u016e\u016f\5,\27\2\u016f\u0170\5")
        buf.write("\u009aN\2\u0170;\3\2\2\2\u0171\u0172\5> \2\u0172=\3\2")
        buf.write("\2\2\u0173\u0174\b \1\2\u0174\u0175\5@!\2\u0175\u017b")
        buf.write("\3\2\2\2\u0176\u0177\f\4\2\2\u0177\u0178\7%\2\2\u0178")
        buf.write("\u017a\5@!\2\u0179\u0176\3\2\2\2\u017a\u017d\3\2\2\2\u017b")
        buf.write("\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c?\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017e\u017f\b!\1\2\u017f\u0180\5B\"\2\u0180")
        buf.write("\u0186\3\2\2\2\u0181\u0182\f\4\2\2\u0182\u0183\7$\2\2")
        buf.write("\u0183\u0185\5B\"\2\u0184\u0181\3\2\2\2\u0185\u0188\3")
        buf.write("\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187A")
        buf.write("\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a\b\"\1\2\u018a")
        buf.write("\u018b\5D#\2\u018b\u0192\3\2\2\2\u018c\u018d\f\4\2\2\u018d")
        buf.write("\u018e\5\u008aF\2\u018e\u018f\5D#\2\u018f\u0191\3\2\2")
        buf.write("\2\u0190\u018c\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190")
        buf.write("\3\2\2\2\u0192\u0193\3\2\2\2\u0193C\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0195\u0196\b#\1\2\u0196\u0197\5F$\2\u0197\u019e")
        buf.write("\3\2\2\2\u0198\u0199\f\4\2\2\u0199\u019a\5\u008cG\2\u019a")
        buf.write("\u019b\5F$\2\u019b\u019d\3\2\2\2\u019c\u0198\3\2\2\2\u019d")
        buf.write("\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3\2\2\2")
        buf.write("\u019fE\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a2\b$\1\2")
        buf.write("\u01a2\u01a3\5H%\2\u01a3\u01aa\3\2\2\2\u01a4\u01a5\f\4")
        buf.write("\2\2\u01a5\u01a6\5\u008eH\2\u01a6\u01a7\5H%\2\u01a7\u01a9")
        buf.write("\3\2\2\2\u01a8\u01a4\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa")
        buf.write("\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01abG\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ad\u01ae\5\u0090I\2\u01ae\u01af\5H%")
        buf.write("\2\u01af\u01b2\3\2\2\2\u01b0\u01b2\5J&\2\u01b1\u01ad\3")
        buf.write("\2\2\2\u01b1\u01b0\3\2\2\2\u01b2I\3\2\2\2\u01b3\u01b7")
        buf.write("\5\u0094K\2\u01b4\u01b6\5L\'\2\u01b5\u01b4\3\2\2\2\u01b6")
        buf.write("\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2")
        buf.write("\u01b8K\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba\u01bb\7,\2\2")
        buf.write("\u01bb\u01bd\7\67\2\2\u01bc\u01be\5P)\2\u01bd\u01bc\3")
        buf.write("\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01c0\3\2\2\2\u01bf\u01c1")
        buf.write("\5N(\2\u01c0\u01bf\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c5")
        buf.write("\3\2\2\2\u01c2\u01c5\5N(\2\u01c3\u01c5\5P)\2\u01c4\u01ba")
        buf.write("\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5")
        buf.write("M\3\2\2\2\u01c6\u01c7\7\62\2\2\u01c7\u01c8\5<\37\2\u01c8")
        buf.write("\u01c9\7\63\2\2\u01c9\u01cb\3\2\2\2\u01ca\u01c6\3\2\2")
        buf.write("\2\u01cb\u01cc\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd")
        buf.write("\3\2\2\2\u01cdO\3\2\2\2\u01ce\u01d0\7.\2\2\u01cf\u01d1")
        buf.write("\5R*\2\u01d0\u01cf\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d2")
        buf.write("\3\2\2\2\u01d2\u01d3\7/\2\2\u01d3Q\3\2\2\2\u01d4\u01d9")
        buf.write("\5<\37\2\u01d5\u01d6\7\64\2\2\u01d6\u01d8\5<\37\2\u01d7")
        buf.write("\u01d5\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2")
        buf.write("\u01d9\u01da\3\2\2\2\u01daS\3\2\2\2\u01db\u01d9\3\2\2")
        buf.write("\2\u01dc\u01dd\5V,\2\u01dd\u01de\5\u009aN\2\u01de\u01f5")
        buf.write("\3\2\2\2\u01df\u01e0\5X-\2\u01e0\u01e1\5\u009aN\2\u01e1")
        buf.write("\u01f5\3\2\2\2\u01e2\u01e3\5`\61\2\u01e3\u01e4\5\u009a")
        buf.write("N\2\u01e4\u01f5\3\2\2\2\u01e5\u01e6\5f\64\2\u01e6\u01e7")
        buf.write("\5\u009aN\2\u01e7\u01f5\3\2\2\2\u01e8\u01e9\5r:\2\u01e9")
        buf.write("\u01ea\5\u009aN\2\u01ea\u01f5\3\2\2\2\u01eb\u01ec\5t;")
        buf.write("\2\u01ec\u01ed\5\u009aN\2\u01ed\u01f5\3\2\2\2\u01ee\u01ef")
        buf.write("\5v<\2\u01ef\u01f0\5\u009aN\2\u01f0\u01f5\3\2\2\2\u01f1")
        buf.write("\u01f2\5\u0082B\2\u01f2\u01f3\5\u009aN\2\u01f3\u01f5\3")
        buf.write("\2\2\2\u01f4\u01dc\3\2\2\2\u01f4\u01df\3\2\2\2\u01f4\u01e2")
        buf.write("\3\2\2\2\u01f4\u01e5\3\2\2\2\u01f4\u01e8\3\2\2\2\u01f4")
        buf.write("\u01eb\3\2\2\2\u01f4\u01ee\3\2\2\2\u01f4\u01f1\3\2\2\2")
        buf.write("\u01f5U\3\2\2\2\u01f6\u01f9\5\6\4\2\u01f7\u01f9\5\20\t")
        buf.write("\2\u01f8\u01f6\3\2\2\2\u01f8\u01f7\3\2\2\2\u01f9W\3\2")
        buf.write("\2\2\u01fa\u01fb\5Z.\2\u01fb\u01fc\7\30\2\2\u01fc\u01fd")
        buf.write("\5^\60\2\u01fd\u0213\3\2\2\2\u01fe\u01ff\5Z.\2\u01ff\u0200")
        buf.write("\7\'\2\2\u0200\u0201\5^\60\2\u0201\u0213\3\2\2\2\u0202")
        buf.write("\u0203\5Z.\2\u0203\u0204\7(\2\2\u0204\u0205\5^\60\2\u0205")
        buf.write("\u0213\3\2\2\2\u0206\u0207\5Z.\2\u0207\u0208\7)\2\2\u0208")
        buf.write("\u0209\5^\60\2\u0209\u0213\3\2\2\2\u020a\u020b\5Z.\2\u020b")
        buf.write("\u020c\7*\2\2\u020c\u020d\5^\60\2\u020d\u0213\3\2\2\2")
        buf.write("\u020e\u020f\5Z.\2\u020f\u0210\7+\2\2\u0210\u0211\5^\60")
        buf.write("\2\u0211\u0213\3\2\2\2\u0212\u01fa\3\2\2\2\u0212\u01fe")
        buf.write("\3\2\2\2\u0212\u0202\3\2\2\2\u0212\u0206\3\2\2\2\u0212")
        buf.write("\u020a\3\2\2\2\u0212\u020e\3\2\2\2\u0213Y\3\2\2\2\u0214")
        buf.write("\u0215\7\67\2\2\u0215\u0216\5\\/\2\u0216[\3\2\2\2\u0217")
        buf.write("\u0218\7,\2\2\u0218\u0219\7\67\2\2\u0219\u0221\5\\/\2")
        buf.write("\u021a\u021b\7\62\2\2\u021b\u021c\5<\37\2\u021c\u021d")
        buf.write("\7\63\2\2\u021d\u021e\5\\/\2\u021e\u0221\3\2\2\2\u021f")
        buf.write("\u0221\3\2\2\2\u0220\u0217\3\2\2\2\u0220\u021a\3\2\2\2")
        buf.write("\u0220\u021f\3\2\2\2\u0221]\3\2\2\2\u0222\u0223\5<\37")
        buf.write("\2\u0223_\3\2\2\2\u0224\u0225\7\3\2\2\u0225\u0226\7.\2")
        buf.write("\2\u0226\u0227\5<\37\2\u0227\u0228\7/\2\2\u0228\u022c")
        buf.write("\7\60\2\2\u0229\u022b\5T+\2\u022a\u0229\3\2\2\2\u022b")
        buf.write("\u022e\3\2\2\2\u022c\u022a\3\2\2\2\u022c\u022d\3\2\2\2")
        buf.write("\u022d\u022f\3\2\2\2\u022e\u022c\3\2\2\2\u022f\u0230\7")
        buf.write("\61\2\2\u0230\u0231\5b\62\2\u0231\u0232\5d\63\2\u0232")
        buf.write("a\3\2\2\2\u0233\u0234\7\4\2\2\u0234\u0235\7\3\2\2\u0235")
        buf.write("\u0236\7.\2\2\u0236\u0237\5<\37\2\u0237\u0238\7/\2\2\u0238")
        buf.write("\u023c\7\60\2\2\u0239\u023b\5T+\2\u023a\u0239\3\2\2\2")
        buf.write("\u023b\u023e\3\2\2\2\u023c\u023a\3\2\2\2\u023c\u023d\3")
        buf.write("\2\2\2\u023d\u023f\3\2\2\2\u023e\u023c\3\2\2\2\u023f\u0240")
        buf.write("\7\61\2\2\u0240\u0242\3\2\2\2\u0241\u0233\3\2\2\2\u0242")
        buf.write("\u0245\3\2\2\2\u0243\u0241\3\2\2\2\u0243\u0244\3\2\2\2")
        buf.write("\u0244c\3\2\2\2\u0245\u0243\3\2\2\2\u0246\u0247\7\4\2")
        buf.write("\2\u0247\u024b\7\60\2\2\u0248\u024a\5T+\2\u0249\u0248")
        buf.write("\3\2\2\2\u024a\u024d\3\2\2\2\u024b\u0249\3\2\2\2\u024b")
        buf.write("\u024c\3\2\2\2\u024c\u024e\3\2\2\2\u024d\u024b\3\2\2\2")
        buf.write("\u024e\u0250\7\61\2\2\u024f\u0246\3\2\2\2\u024f\u0250")
        buf.write("\3\2\2\2\u0250e\3\2\2\2\u0251\u0254\5h\65\2\u0252\u0254")
        buf.write("\5p9\2\u0253\u0251\3\2\2\2\u0253\u0252\3\2\2\2\u0254g")
        buf.write("\3\2\2\2\u0255\u0256\7\5\2\2\u0256\u0257\5j\66\2\u0257")
        buf.write("\u025b\7\60\2\2\u0258\u025a\5T+\2\u0259\u0258\3\2\2\2")
        buf.write("\u025a\u025d\3\2\2\2\u025b\u0259\3\2\2\2\u025b\u025c\3")
        buf.write("\2\2\2\u025c\u025e\3\2\2\2\u025d\u025b\3\2\2\2\u025e\u025f")
        buf.write("\7\61\2\2\u025f\u0270\3\2\2\2\u0260\u0261\7\5\2\2\u0261")
        buf.write("\u0262\5l\67\2\u0262\u0263\7\65\2\2\u0263\u0264\5j\66")
        buf.write("\2\u0264\u0265\7\65\2\2\u0265\u0266\5n8\2\u0266\u026a")
        buf.write("\7\60\2\2\u0267\u0269\5T+\2\u0268\u0267\3\2\2\2\u0269")
        buf.write("\u026c\3\2\2\2\u026a\u0268\3\2\2\2\u026a\u026b\3\2\2\2")
        buf.write("\u026b\u026d\3\2\2\2\u026c\u026a\3\2\2\2\u026d\u026e\7")
        buf.write("\61\2\2\u026e\u0270\3\2\2\2\u026f\u0255\3\2\2\2\u026f")
        buf.write("\u0260\3\2\2\2\u0270i\3\2\2\2\u0271\u0272\5<\37\2\u0272")
        buf.write("k\3\2\2\2\u0273\u027d\5X-\2\u0274\u0275\7\23\2\2\u0275")
        buf.write("\u0276\7\67\2\2\u0276\u027d\5\16\b\2\u0277\u0278\7\23")
        buf.write("\2\2\u0278\u0279\7\67\2\2\u0279\u027a\5\n\6\2\u027a\u027b")
        buf.write("\5\16\b\2\u027b\u027d\3\2\2\2\u027c\u0273\3\2\2\2\u027c")
        buf.write("\u0274\3\2\2\2\u027c\u0277\3\2\2\2\u027dm\3\2\2\2\u027e")
        buf.write("\u027f\7\67\2\2\u027f\u0280\7\30\2\2\u0280\u0291\5<\37")
        buf.write("\2\u0281\u0282\7\67\2\2\u0282\u0283\7\'\2\2\u0283\u0291")
        buf.write("\5<\37\2\u0284\u0285\7\67\2\2\u0285\u0286\7(\2\2\u0286")
        buf.write("\u0291\5<\37\2\u0287\u0288\7\67\2\2\u0288\u0289\7)\2\2")
        buf.write("\u0289\u0291\5<\37\2\u028a\u028b\7\67\2\2\u028b\u028c")
        buf.write("\7*\2\2\u028c\u0291\5<\37\2\u028d\u028e\7\67\2\2\u028e")
        buf.write("\u028f\7+\2\2\u028f\u0291\5<\37\2\u0290\u027e\3\2\2\2")
        buf.write("\u0290\u0281\3\2\2\2\u0290\u0284\3\2\2\2\u0290\u0287\3")
        buf.write("\2\2\2\u0290\u028a\3\2\2\2\u0290\u028d\3\2\2\2\u0291o")
        buf.write("\3\2\2\2\u0292\u0293\7\5\2\2\u0293\u0294\5\u0084C\2\u0294")
        buf.write("\u0295\7\64\2\2\u0295\u0296\5\u0086D\2\u0296\u0297\7\30")
        buf.write("\2\2\u0297\u0298\7\26\2\2\u0298\u0299\5\u0088E\2\u0299")
        buf.write("\u029d\7\60\2\2\u029a\u029c\5T+\2\u029b\u029a\3\2\2\2")
        buf.write("\u029c\u029f\3\2\2\2\u029d\u029b\3\2\2\2\u029d\u029e\3")
        buf.write("\2\2\2\u029e\u02a0\3\2\2\2\u029f\u029d\3\2\2\2\u02a0\u02a1")
        buf.write("\7\61\2\2\u02a1q\3\2\2\2\u02a2\u02a3\7\25\2\2\u02a3s\3")
        buf.write("\2\2\2\u02a4\u02a5\7\24\2\2\u02a5u\3\2\2\2\u02a6\u02a9")
        buf.write("\5x=\2\u02a7\u02a9\5|?\2\u02a8\u02a6\3\2\2\2\u02a8\u02a7")
        buf.write("\3\2\2\2\u02a9w\3\2\2\2\u02aa\u02ab\7\67\2\2\u02ab\u02ac")
        buf.write("\5~@\2\u02ac\u02ad\7,\2\2\u02ad\u02ae\5z>\2\u02ae\u02b8")
        buf.write("\3\2\2\2\u02af\u02b0\7\67\2\2\u02b0\u02b2\7.\2\2\u02b1")
        buf.write("\u02b3\5\u0080A\2\u02b2\u02b1\3\2\2\2\u02b2\u02b3\3\2")
        buf.write("\2\2\u02b3\u02b4\3\2\2\2\u02b4\u02b5\7/\2\2\u02b5\u02b6")
        buf.write("\7,\2\2\u02b6\u02b8\5z>\2\u02b7\u02aa\3\2\2\2\u02b7\u02af")
        buf.write("\3\2\2\2\u02b8y\3\2\2\2\u02b9\u02c1\5x=\2\u02ba\u02bb")
        buf.write("\7\67\2\2\u02bb\u02bd\7.\2\2\u02bc\u02be\5\u0080A\2\u02bd")
        buf.write("\u02bc\3\2\2\2\u02bd\u02be\3\2\2\2\u02be\u02bf\3\2\2\2")
        buf.write("\u02bf\u02c1\7/\2\2\u02c0\u02b9\3\2\2\2\u02c0\u02ba\3")
        buf.write("\2\2\2\u02c1{\3\2\2\2\u02c2\u02c3\7\67\2\2\u02c3\u02c5")
        buf.write("\7.\2\2\u02c4\u02c6\5\u0080A\2\u02c5\u02c4\3\2\2\2\u02c5")
        buf.write("\u02c6\3\2\2\2\u02c6\u02c7\3\2\2\2\u02c7\u02c8\7/\2\2")
        buf.write("\u02c8}\3\2\2\2\u02c9\u02ca\7\62\2\2\u02ca\u02cb\5<\37")
        buf.write("\2\u02cb\u02cc\7\63\2\2\u02cc\u02ce\3\2\2\2\u02cd\u02c9")
        buf.write("\3\2\2\2\u02ce\u02d1\3\2\2\2\u02cf\u02cd\3\2\2\2\u02cf")
        buf.write("\u02d0\3\2\2\2\u02d0\177\3\2\2\2\u02d1\u02cf\3\2\2\2\u02d2")
        buf.write("\u02d7\5<\37\2\u02d3\u02d4\7\64\2\2\u02d4\u02d6\5<\37")
        buf.write("\2\u02d5\u02d3\3\2\2\2\u02d6\u02d9\3\2\2\2\u02d7\u02d5")
        buf.write("\3\2\2\2\u02d7\u02d8\3\2\2\2\u02d8\u0081\3\2\2\2\u02d9")
        buf.write("\u02d7\3\2\2\2\u02da\u02db\7\6\2\2\u02db\u02de\5<\37\2")
        buf.write("\u02dc\u02de\7\6\2\2\u02dd\u02da\3\2\2\2\u02dd\u02dc\3")
        buf.write("\2\2\2\u02de\u0083\3\2\2\2\u02df\u02e0\t\2\2\2\u02e0\u0085")
        buf.write("\3\2\2\2\u02e1\u02e2\7\67\2\2\u02e2\u0087\3\2\2\2\u02e3")
        buf.write("\u02e4\5<\37\2\u02e4\u0089\3\2\2\2\u02e5\u02e6\t\3\2\2")
        buf.write("\u02e6\u008b\3\2\2\2\u02e7\u02e8\t\4\2\2\u02e8\u008d\3")
        buf.write("\2\2\2\u02e9\u02ea\t\5\2\2\u02ea\u008f\3\2\2\2\u02eb\u02ec")
        buf.write("\t\6\2\2\u02ec\u0091\3\2\2\2\u02ed\u02f6\78\2\2\u02ee")
        buf.write("\u02f6\79\2\2\u02ef\u02f6\7:\2\2\u02f0\u02f6\7\17\2\2")
        buf.write("\u02f1\u02f6\7\20\2\2\u02f2\u02f6\7\21\2\2\u02f3\u02f6")
        buf.write("\5\34\17\2\u02f4\u02f6\7\67\2\2\u02f5\u02ed\3\2\2\2\u02f5")
        buf.write("\u02ee\3\2\2\2\u02f5\u02ef\3\2\2\2\u02f5\u02f0\3\2\2\2")
        buf.write("\u02f5\u02f1\3\2\2\2\u02f5\u02f2\3\2\2\2\u02f5\u02f3\3")
        buf.write("\2\2\2\u02f5\u02f4\3\2\2\2\u02f6\u0093\3\2\2\2\u02f7\u0305")
        buf.write("\7\67\2\2\u02f8\u0305\78\2\2\u02f9\u0305\79\2\2\u02fa")
        buf.write("\u0305\7:\2\2\u02fb\u0305\7\17\2\2\u02fc\u0305\7\20\2")
        buf.write("\2\u02fd\u0305\7\21\2\2\u02fe\u02ff\7.\2\2\u02ff\u0300")
        buf.write("\5<\37\2\u0300\u0301\7/\2\2\u0301\u0305\3\2\2\2\u0302")
        buf.write("\u0305\5\22\n\2\u0303\u0305\5\34\17\2\u0304\u02f7\3\2")
        buf.write("\2\2\u0304\u02f8\3\2\2\2\u0304\u02f9\3\2\2\2\u0304\u02fa")
        buf.write("\3\2\2\2\u0304\u02fb\3\2\2\2\u0304\u02fc\3\2\2\2\u0304")
        buf.write("\u02fd\3\2\2\2\u0304\u02fe\3\2\2\2\u0304\u0302\3\2\2\2")
        buf.write("\u0304\u0303\3\2\2\2\u0305\u0095\3\2\2\2\u0306\u0307\t")
        buf.write("\7\2\2\u0307\u0097\3\2\2\2\u0308\u0309\t\b\2\2\u0309\u0099")
        buf.write("\3\2\2\2\u030a\u030b\7\65\2\2\u030b\u009b\3\2\2\2@\u009f")
        buf.write("\u00b2\u00bd\u00c3\u00cb\u00d3\u00e7\u00eb\u00f4\u00fe")
        buf.write("\u010e\u0116\u011f\u0127\u0131\u013b\u0141\u014b\u0151")
        buf.write("\u015d\u0163\u016b\u017b\u0186\u0192\u019e\u01aa\u01b1")
        buf.write("\u01b7\u01bd\u01c0\u01c4\u01cc\u01d0\u01d9\u01f4\u01f8")
        buf.write("\u0212\u0220\u022c\u023c\u0243\u024b\u024f\u0253\u025b")
        buf.write("\u026a\u026f\u027c\u0290\u029d\u02a8\u02b2\u02b7\u02bd")
        buf.write("\u02c0\u02c5\u02cf\u02d7\u02dd\u02f5\u0304")
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
    RULE_elseStatement = 49
    RULE_forStatement = 50
    RULE_basicForStatement = 51
    RULE_forCondition = 52
    RULE_forInitilization = 53
    RULE_forUpdate = 54
    RULE_forRangeStatement = 55
    RULE_breakStatement = 56
    RULE_continueStatement = 57
    RULE_callStatement = 58
    RULE_methodCallStatement = 59
    RULE_methodCallStatementTail = 60
    RULE_funcCallStatement = 61
    RULE_callStatementArrayTail = 62
    RULE_callStatementParam = 63
    RULE_returnStatement = 64
    RULE_index = 65
    RULE_value = 66
    RULE_forArray = 67
    RULE_relationOp = 68
    RULE_addOp = 69
    RULE_mulOp = 70
    RULE_unaryOp = 71
    RULE_noArrayLit = 72
    RULE_term = 73
    RULE_intLitOrConstant = 74
    RULE_baseType = 75
    RULE_endOfStatement = 76

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
                   "assignStateRHS", "ifStatement", "elseIfStatement", "elseStatement", 
                   "forStatement", "basicForStatement", "forCondition", 
                   "forInitilization", "forUpdate", "forRangeStatement", 
                   "breakStatement", "continueStatement", "callStatement", 
                   "methodCallStatement", "methodCallStatementTail", "funcCallStatement", 
                   "callStatementArrayTail", "callStatementParam", "returnStatement", 
                   "index", "value", "forArray", "relationOp", "addOp", 
                   "mulOp", "unaryOp", "noArrayLit", "term", "intLitOrConstant", 
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
            self.state = 155 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 154
                self.decl()
                self.state = 157 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 159
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
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.varDecl()
                self.state = 162
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.funcDecl()
                self.state = 165
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.constDecl()
                self.state = 168
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 170
                self.methodDecl()
                self.state = 171
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 173
                self.typeDecl()
                self.state = 174
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
            self.state = 178
            self.match(MiniGoParser.VAR)
            self.state = 179
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 180
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
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.varDeclType()
                self.state = 183
                self.varDeclExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.varDeclType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 186
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
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.baseType()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.arrayType()
                self.state = 191
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
            self.state = 199 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 195
                self.match(MiniGoParser.LBRACKET)
                self.state = 196
                self.intLitOrConstant()
                self.state = 197
                self.match(MiniGoParser.RBRACKET)
                self.state = 201 
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
            self.state = 203
            self.match(MiniGoParser.DECLARE)
            self.state = 204
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
            self.state = 206
            self.match(MiniGoParser.CONST)
            self.state = 207
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 208
                self.varDeclType()


            self.state = 211
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
            self.state = 213
            self.arrayType()
            self.state = 214
            self.baseType()
            self.state = 215
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
            self.state = 217
            self.match(MiniGoParser.LBRACE)
            self.state = 218
            self.arrayLitList()
            self.state = 219
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
            self.state = 221
            self.arrayLitContent()
            self.state = 222
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
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(MiniGoParser.COMMA)
                self.state = 225
                self.arrayLitContent()
                self.state = 226
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
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.arrayBlock()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
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
            self.state = 235
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 236
            self.match(MiniGoParser.LBRACE)
            self.state = 237
            self.optionalStructFields()
            self.state = 238
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
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
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
            self.state = 244
            self.structFieldAssign()
            self.state = 245
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
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(MiniGoParser.COMMA)
                self.state = 248
                self.structFieldAssign()
                self.state = 249
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
            self.state = 254
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 255
            self.match(MiniGoParser.COLON)
            self.state = 256
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
            self.state = 258
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

        def funcType(self):
            return self.getTypedRuleContext(MiniGoParser.FuncTypeContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def funcParam(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamContext,0)


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
            self.state = 260
            self.match(MiniGoParser.FUNC)
            self.state = 261
            self.match(MiniGoParser.LPAREN)
            self.state = 262
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 263
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 264
            self.match(MiniGoParser.RPAREN)
            self.state = 265
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 266
            self.match(MiniGoParser.LPAREN)
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 267
                self.funcParam()


            self.state = 270
            self.match(MiniGoParser.RPAREN)
            self.state = 271
            self.funcType()
            self.state = 272
            self.match(MiniGoParser.LBRACE)
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 273
                self.statement()
                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 279
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

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def funcType(self):
            return self.getTypedRuleContext(MiniGoParser.FuncTypeContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def funcParam(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamContext,0)


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
            self.state = 281
            self.match(MiniGoParser.FUNC)
            self.state = 282
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 283
            self.match(MiniGoParser.LPAREN)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 284
                self.funcParam()


            self.state = 287
            self.match(MiniGoParser.RPAREN)
            self.state = 288
            self.funcType()
            self.state = 289
            self.match(MiniGoParser.LBRACE)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 290
                self.statement()
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 296
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
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.baseType()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.arrayType()
                self.state = 300
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
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.funcListIdentifiers()
                self.state = 306
                self.varDeclType()
                self.state = 307
                self.match(MiniGoParser.COMMA)
                self.state = 308
                self.funcParam()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.funcListIdentifiers()
                self.state = 311
                self.varDeclType()
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
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 317
                self.match(MiniGoParser.COMMA)
                self.state = 318
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
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.match(MiniGoParser.TYPE)
                self.state = 322
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 323
                self.match(MiniGoParser.STRUCT)
                self.state = 324
                self.structDeclBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.match(MiniGoParser.TYPE)
                self.state = 326
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 327
                self.match(MiniGoParser.INTERFACE)
                self.state = 328
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
            self.state = 331
            self.match(MiniGoParser.LBRACE)
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.FUNC or _la==MiniGoParser.IDENTIFIER:
                self.state = 332
                self.structDeclField()
                self.state = 337
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 338
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
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 341
                self.varDeclType()
                self.state = 342
                self.endOfStatement()
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.methodDecl()
                self.state = 345
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
            self.state = 349
            self.match(MiniGoParser.LBRACE)
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 350
                self.interfaceDeclField()
                self.state = 355
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 356
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

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def funcType(self):
            return self.getTypedRuleContext(MiniGoParser.FuncTypeContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def funcParam(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 359
            self.match(MiniGoParser.LPAREN)
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 360
                self.funcParam()


            self.state = 363
            self.match(MiniGoParser.RPAREN)
            self.state = 364
            self.funcType()
            self.state = 365
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
            self.enterOuterAlt(localctx, 1)
            self.state = 367
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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_logicOrExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.logicAndExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogicOrExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicOrExpr)
                    self.state = 372
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 373
                    self.match(MiniGoParser.OR)
                    self.state = 374
                    self.logicAndExpr(0) 
                self.state = 379
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
            self.state = 381
            self.equalityExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 388
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogicAndExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicAndExpr)
                    self.state = 383
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 384
                    self.match(MiniGoParser.AND)
                    self.state = 385
                    self.equalityExpr(0) 
                self.state = 390
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
            self.state = 392
            self.additiveExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 400
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.EqualityExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpr)
                    self.state = 394
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 395
                    self.relationOp()
                    self.state = 396
                    self.additiveExpr(0) 
                self.state = 402
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
            self.state = 404
            self.multiplicativeExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 412
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.AdditiveExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpr)
                    self.state = 406
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 407
                    self.addOp()
                    self.state = 408
                    self.multiplicativeExpr(0) 
                self.state = 414
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
            self.state = 416
            self.unaryExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 424
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.MultiplicativeExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpr)
                    self.state = 418
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 419
                    self.mulOp()
                    self.state = 420
                    self.unaryExpr() 
                self.state = 426
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.unaryOp()
                self.state = 428
                self.unaryExpr()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
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
            self.state = 433
            self.term()
            self.state = 437
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 434
                    self.primarySuffix() 
                self.state = 439
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
            self.state = 450
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.match(MiniGoParser.DOT)
                self.state = 441
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 443
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 442
                    self.callSuffix()


                self.state = 446
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 445
                    self.arraySuffix()


                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.arraySuffix()
                pass
            elif token in [MiniGoParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 449
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
            self.state = 456 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 452
                    self.match(MiniGoParser.LBRACKET)
                    self.state = 453
                    self.expr()
                    self.state = 454
                    self.match(MiniGoParser.RBRACKET)

                else:
                    raise NoViableAltException(self)
                self.state = 458 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
            self.state = 460
            self.match(MiniGoParser.LPAREN)
            self.state = 462
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 461
                self.argList()


            self.state = 464
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
            self.state = 466
            self.expr()
            self.state = 471
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 467
                self.match(MiniGoParser.COMMA)
                self.state = 468
                self.expr()
                self.state = 473
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
            self.state = 498
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.declarationStatement()
                self.state = 475
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 477
                self.assignStatement()
                self.state = 478
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 480
                self.ifStatement()
                self.state = 481
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 483
                self.forStatement()
                self.state = 484
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 486
                self.breakStatement()
                self.state = 487
                self.endOfStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 489
                self.continueStatement()
                self.state = 490
                self.endOfStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 492
                self.callStatement()
                self.state = 493
                self.endOfStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 495
                self.returnStatement()
                self.state = 496
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
            self.state = 502
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 500
                self.varDecl()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
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
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 504
                self.assignStateLHS()
                self.state = 505
                self.match(MiniGoParser.ASSIGN)
                self.state = 506
                self.assignStateRHS()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 508
                self.assignStateLHS()
                self.state = 509
                self.match(MiniGoParser.PLUS_ASSIGN)
                self.state = 510
                self.assignStateRHS()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 512
                self.assignStateLHS()
                self.state = 513
                self.match(MiniGoParser.MINUS_ASSIGN)
                self.state = 514
                self.assignStateRHS()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 516
                self.assignStateLHS()
                self.state = 517
                self.match(MiniGoParser.MUL_ASSIGN)
                self.state = 518
                self.assignStateRHS()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 520
                self.assignStateLHS()
                self.state = 521
                self.match(MiniGoParser.DIV_ASSIGN)
                self.state = 522
                self.assignStateRHS()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 524
                self.assignStateLHS()
                self.state = 525
                self.match(MiniGoParser.MOD_ASSIGN)
                self.state = 526
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
            self.state = 530
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 531
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
            self.state = 542
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 533
                self.match(MiniGoParser.DOT)
                self.state = 534
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 535
                self.assignStateLHSTail()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 536
                self.match(MiniGoParser.LBRACKET)
                self.state = 537
                self.expr()
                self.state = 538
                self.match(MiniGoParser.RBRACKET)
                self.state = 539
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
            self.state = 544
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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def elseIfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ElseIfStatementContext,0)


        def elseStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ElseStatementContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self.match(MiniGoParser.IF)
            self.state = 547
            self.match(MiniGoParser.LPAREN)
            self.state = 548
            self.expr()
            self.state = 549
            self.match(MiniGoParser.RPAREN)
            self.state = 550
            self.match(MiniGoParser.LBRACE)
            self.state = 554
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 551
                self.statement()
                self.state = 556
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 557
            self.match(MiniGoParser.RBRACE)
            self.state = 558
            self.elseIfStatement()
            self.state = 559
            self.elseStatement()
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

        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ELSE)
            else:
                return self.getToken(MiniGoParser.ELSE, i)

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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

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
            self.enterOuterAlt(localctx, 1)
            self.state = 577
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 561
                    self.match(MiniGoParser.ELSE)
                    self.state = 562
                    self.match(MiniGoParser.IF)
                    self.state = 563
                    self.match(MiniGoParser.LPAREN)
                    self.state = 564
                    self.expr()
                    self.state = 565
                    self.match(MiniGoParser.RPAREN)
                    self.state = 566
                    self.match(MiniGoParser.LBRACE)
                    self.state = 570
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                        self.state = 567
                        self.statement()
                        self.state = 572
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 573
                    self.match(MiniGoParser.RBRACE) 
                self.state = 579
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

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
            return MiniGoParser.RULE_elseStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStatement" ):
                return visitor.visitElseStatement(self)
            else:
                return visitor.visitChildren(self)




    def elseStatement(self):

        localctx = MiniGoParser.ElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_elseStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 580
                self.match(MiniGoParser.ELSE)
                self.state = 581
                self.match(MiniGoParser.LBRACE)
                self.state = 585
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 582
                    self.statement()
                    self.state = 587
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 588
                self.match(MiniGoParser.RBRACE)


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
        self.enterRule(localctx, 100, self.RULE_forStatement)
        try:
            self.state = 593
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 591
                self.basicForStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 592
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
        self.enterRule(localctx, 102, self.RULE_basicForStatement)
        self._la = 0 # Token type
        try:
            self.state = 621
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 595
                self.match(MiniGoParser.FOR)
                self.state = 596
                self.forCondition()
                self.state = 597
                self.match(MiniGoParser.LBRACE)
                self.state = 601
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 598
                    self.statement()
                    self.state = 603
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 604
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 606
                self.match(MiniGoParser.FOR)
                self.state = 607
                self.forInitilization()
                self.state = 608
                self.match(MiniGoParser.SEMI)
                self.state = 609
                self.forCondition()
                self.state = 610
                self.match(MiniGoParser.SEMI)
                self.state = 611
                self.forUpdate()
                self.state = 612
                self.match(MiniGoParser.LBRACE)
                self.state = 616
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 613
                    self.statement()
                    self.state = 618
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 619
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
        self.enterRule(localctx, 104, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
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


        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def varDeclExpr(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclExprContext,0)


        def varDeclType(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forInitilization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInitilization" ):
                return visitor.visitForInitilization(self)
            else:
                return visitor.visitChildren(self)




    def forInitilization(self):

        localctx = MiniGoParser.ForInitilizationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_forInitilization)
        try:
            self.state = 634
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 625
                self.assignStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 626
                self.match(MiniGoParser.VAR)
                self.state = 627
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 628
                self.varDeclExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 629
                self.match(MiniGoParser.VAR)
                self.state = 630
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 631
                self.varDeclType()
                self.state = 632
                self.varDeclExpr()
                pass


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

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


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
            return MiniGoParser.RULE_forUpdate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = MiniGoParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_forUpdate)
        try:
            self.state = 654
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 636
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 637
                self.match(MiniGoParser.ASSIGN)
                self.state = 638
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 639
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 640
                self.match(MiniGoParser.PLUS_ASSIGN)
                self.state = 641
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 642
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 643
                self.match(MiniGoParser.MINUS_ASSIGN)
                self.state = 644
                self.expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 645
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 646
                self.match(MiniGoParser.MUL_ASSIGN)
                self.state = 647
                self.expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 648
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 649
                self.match(MiniGoParser.DIV_ASSIGN)
                self.state = 650
                self.expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 651
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 652
                self.match(MiniGoParser.MOD_ASSIGN)
                self.state = 653
                self.expr()
                pass


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
        self.enterRule(localctx, 110, self.RULE_forRangeStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 656
            self.match(MiniGoParser.FOR)
            self.state = 657
            self.index()
            self.state = 658
            self.match(MiniGoParser.COMMA)
            self.state = 659
            self.value()
            self.state = 660
            self.match(MiniGoParser.ASSIGN)
            self.state = 661
            self.match(MiniGoParser.RANGE)
            self.state = 662
            self.forArray()
            self.state = 663
            self.match(MiniGoParser.LBRACE)
            self.state = 667
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 664
                self.statement()
                self.state = 669
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 670
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
        self.enterRule(localctx, 112, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 672
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
        self.enterRule(localctx, 114, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 674
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
        self.enterRule(localctx, 116, self.RULE_callStatement)
        try:
            self.state = 678
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 676
                self.methodCallStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 677
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
        self.enterRule(localctx, 118, self.RULE_methodCallStatement)
        self._la = 0 # Token type
        try:
            self.state = 693
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 680
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 681
                self.callStatementArrayTail()
                self.state = 682
                self.match(MiniGoParser.DOT)
                self.state = 683
                self.methodCallStatementTail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 685
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 686
                self.match(MiniGoParser.LPAREN)
                self.state = 688
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 687
                    self.callStatementParam()


                self.state = 690
                self.match(MiniGoParser.RPAREN)
                self.state = 691
                self.match(MiniGoParser.DOT)
                self.state = 692
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
        self.enterRule(localctx, 120, self.RULE_methodCallStatementTail)
        self._la = 0 # Token type
        try:
            self.state = 702
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 695
                self.methodCallStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 696
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 697
                self.match(MiniGoParser.LPAREN)
                self.state = 699
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 698
                    self.callStatementParam()


                self.state = 701
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
        self.enterRule(localctx, 122, self.RULE_funcCallStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 704
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 705
            self.match(MiniGoParser.LPAREN)
            self.state = 707
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 706
                self.callStatementParam()


            self.state = 709
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
        self.enterRule(localctx, 124, self.RULE_callStatementArrayTail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 717
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.LBRACKET:
                self.state = 711
                self.match(MiniGoParser.LBRACKET)
                self.state = 712
                self.expr()
                self.state = 713
                self.match(MiniGoParser.RBRACKET)
                self.state = 719
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
        self.enterRule(localctx, 126, self.RULE_callStatementParam)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 720
            self.expr()
            self.state = 725
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 721
                self.match(MiniGoParser.COMMA)
                self.state = 722
                self.expr()
                self.state = 727
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
        self.enterRule(localctx, 128, self.RULE_returnStatement)
        try:
            self.state = 731
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 728
                self.match(MiniGoParser.RETURN)
                self.state = 729
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 730
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
        self.enterRule(localctx, 130, self.RULE_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 733
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
        self.enterRule(localctx, 132, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 735
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
        self.enterRule(localctx, 134, self.RULE_forArray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 737
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
        self.enterRule(localctx, 136, self.RULE_relationOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 739
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
        self.enterRule(localctx, 138, self.RULE_addOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 741
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
        self.enterRule(localctx, 140, self.RULE_mulOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 743
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
        self.enterRule(localctx, 142, self.RULE_unaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 745
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
        self.enterRule(localctx, 144, self.RULE_noArrayLit)
        try:
            self.state = 755
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 747
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 748
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 749
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 750
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 751
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 752
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 753
                self.structLit()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 754
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

        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = MiniGoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_term)
        try:
            self.state = 770
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 757
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 758
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 759
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 760
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 761
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 762
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 763
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 764
                self.match(MiniGoParser.LPAREN)
                self.state = 765
                self.expr()
                self.state = 766
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 768
                self.arrayLit()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 769
                self.structLit()
                pass


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
        self.enterRule(localctx, 148, self.RULE_intLitOrConstant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 772
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
        self.enterRule(localctx, 150, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 774
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
        self.enterRule(localctx, 152, self.RULE_endOfStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 776
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
         




