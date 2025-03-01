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
        buf.write("\u030e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\6\2\u0096\n")
        buf.write("\2\r\2\16\2\u0097\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00ab\n\3\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\5\5\u00b6\n\5\3\6\3\6\3\6")
        buf.write("\3\6\5\6\u00bc\n\6\3\7\3\7\3\7\3\7\6\7\u00c2\n\7\r\7\16")
        buf.write("\7\u00c3\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u00cc\n\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\7\13\u00d8\n\13\f")
        buf.write("\13\16\13\u00db\13\13\3\13\3\13\3\f\3\f\5\f\u00e1\n\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\5\16\u00ea\n\16\3\17\3")
        buf.write("\17\3\17\7\17\u00ef\n\17\f\17\16\17\u00f2\13\17\3\20\3")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\5\21\u0100\n\21\3\21\3\21\3\21\3\21\7\21\u0106\n\21\f")
        buf.write("\21\16\21\u0109\13\21\3\21\3\21\3\22\3\22\3\22\3\22\5")
        buf.write("\22\u0111\n\22\3\22\3\22\3\22\3\22\7\22\u0117\n\22\f\22")
        buf.write("\16\22\u011a\13\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\5\23\u0123\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\5\24\u012d\n\24\3\25\3\25\3\25\3\25\5\25\u0133\n\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u013d\n")
        buf.write("\26\3\27\3\27\7\27\u0141\n\27\f\27\16\27\u0144\13\27\3")
        buf.write("\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u014f")
        buf.write("\n\30\3\31\3\31\7\31\u0153\n\31\f\31\16\31\u0156\13\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\5\32\u015d\n\32\3\32\3\32\3")
        buf.write("\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34")
        buf.write("\u016b\n\34\f\34\16\34\u016e\13\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\7\35\u0176\n\35\f\35\16\35\u0179\13\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u0182\n\36\f\36\16")
        buf.write("\36\u0185\13\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37")
        buf.write("\u018e\n\37\f\37\16\37\u0191\13\37\3 \3 \3 \3 \3 \3 \3")
        buf.write(" \7 \u019a\n \f \16 \u019d\13 \3!\3!\3!\3!\5!\u01a3\n")
        buf.write("!\3\"\3\"\5\"\u01a7\n\"\3\"\7\"\u01aa\n\"\f\"\16\"\u01ad")
        buf.write("\13\"\3#\3#\3#\5#\u01b2\n#\3#\5#\u01b5\n#\3#\5#\u01b8")
        buf.write("\n#\3$\3$\3$\3$\6$\u01be\n$\r$\16$\u01bf\3%\3%\5%\u01c4")
        buf.write("\n%\3%\3%\3&\3&\3&\7&\u01cb\n&\f&\16&\u01ce\13&\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u01e8\n\'\3(")
        buf.write("\3(\5(\u01ec\n(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u0206\n)\3*\3*\3")
        buf.write("*\3*\3*\7*\u020d\n*\f*\16*\u0210\13*\3*\5*\u0213\n*\3")
        buf.write("+\3+\3+\3+\3+\3+\7+\u021b\n+\f+\16+\u021e\13+\3+\5+\u0221")
        buf.write("\n+\3,\3,\3-\3-\3-\3-\3-\3-\7-\u022b\n-\f-\16-\u022e\13")
        buf.write("-\3-\3-\7-\u0232\n-\f-\16-\u0235\13-\3-\5-\u0238\n-\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\7.\u0241\n.\f.\16.\u0244\13.\3.\3")
        buf.write(".\3/\3/\3/\7/\u024b\n/\f/\16/\u024e\13/\3/\3/\3\60\3\60")
        buf.write("\5\60\u0254\n\60\3\61\3\61\3\61\3\61\7\61\u025a\n\61\f")
        buf.write("\61\16\61\u025d\13\61\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\7\61\u0269\n\61\f\61\16\61\u026c\13")
        buf.write("\61\3\61\3\61\5\61\u0270\n\61\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u027d\n\63\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u0291\n\64\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u029c\n\65")
        buf.write("\f\65\16\65\u029f\13\65\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\38\38\58\u02a9\n8\39\69\u02ac\n9\r9\169\u02ad\39\39\3")
        buf.write("9\59\u02b3\n9\39\39\3:\3:\3:\5:\u02ba\n:\3:\3:\3:\3:\5")
        buf.write(":\u02c0\n:\3:\5:\u02c3\n:\3;\3;\3;\5;\u02c8\n;\3;\3;\3")
        buf.write("<\3<\3<\3<\6<\u02d0\n<\r<\16<\u02d1\3=\3=\3=\7=\u02d7")
        buf.write("\n=\f=\16=\u02da\13=\3>\3>\3>\5>\u02df\n>\3?\3?\3@\3@")
        buf.write("\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3F\3F\3F\3F\3F\3")
        buf.write("F\5F\u02f7\nF\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\5")
        buf.write("G\u0306\nG\3H\3H\3I\3I\3J\3J\3J\2\7\668:<>K\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086")
        buf.write("\u0088\u008a\u008c\u008e\u0090\u0092\2\t\4\2--\67\67\3")
        buf.write("\2\36#\3\2\31\32\3\2\33\35\4\2\32\32&&\3\2\678\4\2\13")
        buf.write("\16\67\67\2\u0329\2\u0095\3\2\2\2\4\u00aa\3\2\2\2\6\u00ac")
        buf.write("\3\2\2\2\b\u00b5\3\2\2\2\n\u00bb\3\2\2\2\f\u00c1\3\2\2")
        buf.write("\2\16\u00c5\3\2\2\2\20\u00c8\3\2\2\2\22\u00cf\3\2\2\2")
        buf.write("\24\u00d3\3\2\2\2\26\u00e0\3\2\2\2\30\u00e2\3\2\2\2\32")
        buf.write("\u00e9\3\2\2\2\34\u00eb\3\2\2\2\36\u00f3\3\2\2\2 \u00f7")
        buf.write("\3\2\2\2\"\u010c\3\2\2\2$\u0122\3\2\2\2&\u012c\3\2\2\2")
        buf.write("(\u0132\3\2\2\2*\u013c\3\2\2\2,\u013e\3\2\2\2.\u014e\3")
        buf.write("\2\2\2\60\u0150\3\2\2\2\62\u0159\3\2\2\2\64\u0162\3\2")
        buf.write("\2\2\66\u0164\3\2\2\28\u016f\3\2\2\2:\u017a\3\2\2\2<\u0186")
        buf.write("\3\2\2\2>\u0192\3\2\2\2@\u01a2\3\2\2\2B\u01a4\3\2\2\2")
        buf.write("D\u01b7\3\2\2\2F\u01bd\3\2\2\2H\u01c1\3\2\2\2J\u01c7\3")
        buf.write("\2\2\2L\u01e7\3\2\2\2N\u01eb\3\2\2\2P\u0205\3\2\2\2R\u0207")
        buf.write("\3\2\2\2T\u0214\3\2\2\2V\u0222\3\2\2\2X\u0224\3\2\2\2")
        buf.write("Z\u0239\3\2\2\2\\\u0247\3\2\2\2^\u0253\3\2\2\2`\u026f")
        buf.write("\3\2\2\2b\u0271\3\2\2\2d\u027c\3\2\2\2f\u0290\3\2\2\2")
        buf.write("h\u0292\3\2\2\2j\u02a2\3\2\2\2l\u02a4\3\2\2\2n\u02a8\3")
        buf.write("\2\2\2p\u02ab\3\2\2\2r\u02c2\3\2\2\2t\u02c4\3\2\2\2v\u02cf")
        buf.write("\3\2\2\2x\u02d3\3\2\2\2z\u02de\3\2\2\2|\u02e0\3\2\2\2")
        buf.write("~\u02e2\3\2\2\2\u0080\u02e4\3\2\2\2\u0082\u02e6\3\2\2")
        buf.write("\2\u0084\u02e8\3\2\2\2\u0086\u02ea\3\2\2\2\u0088\u02ec")
        buf.write("\3\2\2\2\u008a\u02f6\3\2\2\2\u008c\u0305\3\2\2\2\u008e")
        buf.write("\u0307\3\2\2\2\u0090\u0309\3\2\2\2\u0092\u030b\3\2\2\2")
        buf.write("\u0094\u0096\5\4\3\2\u0095\u0094\3\2\2\2\u0096\u0097\3")
        buf.write("\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u009a\7\2\2\3\u009a\3\3\2\2\2\u009b\u009c")
        buf.write("\5\6\4\2\u009c\u009d\5\u0092J\2\u009d\u00ab\3\2\2\2\u009e")
        buf.write("\u009f\5\"\22\2\u009f\u00a0\5\u0092J\2\u00a0\u00ab\3\2")
        buf.write("\2\2\u00a1\u00a2\5\20\t\2\u00a2\u00a3\5\u0092J\2\u00a3")
        buf.write("\u00ab\3\2\2\2\u00a4\u00a5\5 \21\2\u00a5\u00a6\5\u0092")
        buf.write("J\2\u00a6\u00ab\3\2\2\2\u00a7\u00a8\5*\26\2\u00a8\u00a9")
        buf.write("\5\u0092J\2\u00a9\u00ab\3\2\2\2\u00aa\u009b\3\2\2\2\u00aa")
        buf.write("\u009e\3\2\2\2\u00aa\u00a1\3\2\2\2\u00aa\u00a4\3\2\2\2")
        buf.write("\u00aa\u00a7\3\2\2\2\u00ab\5\3\2\2\2\u00ac\u00ad\7\23")
        buf.write("\2\2\u00ad\u00ae\7\67\2\2\u00ae\u00af\5\b\5\2\u00af\7")
        buf.write("\3\2\2\2\u00b0\u00b1\5\n\6\2\u00b1\u00b2\5\16\b\2\u00b2")
        buf.write("\u00b6\3\2\2\2\u00b3\u00b6\5\n\6\2\u00b4\u00b6\5\16\b")
        buf.write("\2\u00b5\u00b0\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b4")
        buf.write("\3\2\2\2\u00b6\t\3\2\2\2\u00b7\u00bc\5\u0090I\2\u00b8")
        buf.write("\u00b9\5\f\7\2\u00b9\u00ba\5\u0090I\2\u00ba\u00bc\3\2")
        buf.write("\2\2\u00bb\u00b7\3\2\2\2\u00bb\u00b8\3\2\2\2\u00bc\13")
        buf.write("\3\2\2\2\u00bd\u00be\7\62\2\2\u00be\u00bf\5\u008eH\2\u00bf")
        buf.write("\u00c0\7\63\2\2\u00c0\u00c2\3\2\2\2\u00c1\u00bd\3\2\2")
        buf.write("\2\u00c2\u00c3\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4")
        buf.write("\3\2\2\2\u00c4\r\3\2\2\2\u00c5\u00c6\7\27\2\2\u00c6\u00c7")
        buf.write("\5\64\33\2\u00c7\17\3\2\2\2\u00c8\u00c9\7\22\2\2\u00c9")
        buf.write("\u00cb\7\67\2\2\u00ca\u00cc\5\n\6\2\u00cb\u00ca\3\2\2")
        buf.write("\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce")
        buf.write("\5\16\b\2\u00ce\21\3\2\2\2\u00cf\u00d0\5\f\7\2\u00d0\u00d1")
        buf.write("\5\u0090I\2\u00d1\u00d2\5\24\13\2\u00d2\23\3\2\2\2\u00d3")
        buf.write("\u00d4\7\60\2\2\u00d4\u00d9\5\26\f\2\u00d5\u00d6\7\64")
        buf.write("\2\2\u00d6\u00d8\5\26\f\2\u00d7\u00d5\3\2\2\2\u00d8\u00db")
        buf.write("\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("\u00dc\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00dd\7\61\2")
        buf.write("\2\u00dd\25\3\2\2\2\u00de\u00e1\5\24\13\2\u00df\u00e1")
        buf.write("\5\u008aF\2\u00e0\u00de\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1")
        buf.write("\27\3\2\2\2\u00e2\u00e3\7\67\2\2\u00e3\u00e4\7\60\2\2")
        buf.write("\u00e4\u00e5\5\32\16\2\u00e5\u00e6\7\61\2\2\u00e6\31\3")
        buf.write("\2\2\2\u00e7\u00ea\5\34\17\2\u00e8\u00ea\3\2\2\2\u00e9")
        buf.write("\u00e7\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea\33\3\2\2\2\u00eb")
        buf.write("\u00f0\5\36\20\2\u00ec\u00ed\7\64\2\2\u00ed\u00ef\5\36")
        buf.write("\20\2\u00ee\u00ec\3\2\2\2\u00ef\u00f2\3\2\2\2\u00f0\u00ee")
        buf.write("\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\35\3\2\2\2\u00f2\u00f0")
        buf.write("\3\2\2\2\u00f3\u00f4\7\67\2\2\u00f4\u00f5\7\66\2\2\u00f5")
        buf.write("\u00f6\5\64\33\2\u00f6\37\3\2\2\2\u00f7\u00f8\7\7\2\2")
        buf.write("\u00f8\u00f9\7.\2\2\u00f9\u00fa\7\67\2\2\u00fa\u00fb\7")
        buf.write("\67\2\2\u00fb\u00fc\7/\2\2\u00fc\u00fd\7\67\2\2\u00fd")
        buf.write("\u00ff\7.\2\2\u00fe\u0100\5&\24\2\u00ff\u00fe\3\2\2\2")
        buf.write("\u00ff\u0100\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102\7")
        buf.write("/\2\2\u0102\u0103\5$\23\2\u0103\u0107\7\60\2\2\u0104\u0106")
        buf.write("\5L\'\2\u0105\u0104\3\2\2\2\u0106\u0109\3\2\2\2\u0107")
        buf.write("\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u010a\3\2\2\2")
        buf.write("\u0109\u0107\3\2\2\2\u010a\u010b\7\61\2\2\u010b!\3\2\2")
        buf.write("\2\u010c\u010d\7\7\2\2\u010d\u010e\7\67\2\2\u010e\u0110")
        buf.write("\7.\2\2\u010f\u0111\5&\24\2\u0110\u010f\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113\7/\2\2")
        buf.write("\u0113\u0114\5$\23\2\u0114\u0118\7\60\2\2\u0115\u0117")
        buf.write("\5L\'\2\u0116\u0115\3\2\2\2\u0117\u011a\3\2\2\2\u0118")
        buf.write("\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011b\3\2\2\2")
        buf.write("\u011a\u0118\3\2\2\2\u011b\u011c\7\61\2\2\u011c#\3\2\2")
        buf.write("\2\u011d\u0123\5\u0090I\2\u011e\u011f\5\f\7\2\u011f\u0120")
        buf.write("\5\u0090I\2\u0120\u0123\3\2\2\2\u0121\u0123\3\2\2\2\u0122")
        buf.write("\u011d\3\2\2\2\u0122\u011e\3\2\2\2\u0122\u0121\3\2\2\2")
        buf.write("\u0123%\3\2\2\2\u0124\u0125\5(\25\2\u0125\u0126\5\n\6")
        buf.write("\2\u0126\u0127\7\64\2\2\u0127\u0128\5&\24\2\u0128\u012d")
        buf.write("\3\2\2\2\u0129\u012a\5(\25\2\u012a\u012b\5\n\6\2\u012b")
        buf.write("\u012d\3\2\2\2\u012c\u0124\3\2\2\2\u012c\u0129\3\2\2\2")
        buf.write("\u012d\'\3\2\2\2\u012e\u0133\7\67\2\2\u012f\u0130\7\67")
        buf.write("\2\2\u0130\u0131\7\64\2\2\u0131\u0133\5(\25\2\u0132\u012e")
        buf.write("\3\2\2\2\u0132\u012f\3\2\2\2\u0133)\3\2\2\2\u0134\u0135")
        buf.write("\7\b\2\2\u0135\u0136\7\67\2\2\u0136\u0137\7\t\2\2\u0137")
        buf.write("\u013d\5,\27\2\u0138\u0139\7\b\2\2\u0139\u013a\7\67\2")
        buf.write("\2\u013a\u013b\7\n\2\2\u013b\u013d\5\60\31\2\u013c\u0134")
        buf.write("\3\2\2\2\u013c\u0138\3\2\2\2\u013d+\3\2\2\2\u013e\u0142")
        buf.write("\7\60\2\2\u013f\u0141\5.\30\2\u0140\u013f\3\2\2\2\u0141")
        buf.write("\u0144\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2")
        buf.write("\u0143\u0145\3\2\2\2\u0144\u0142\3\2\2\2\u0145\u0146\7")
        buf.write("\61\2\2\u0146-\3\2\2\2\u0147\u0148\7\67\2\2\u0148\u0149")
        buf.write("\5\n\6\2\u0149\u014a\5\u0092J\2\u014a\u014f\3\2\2\2\u014b")
        buf.write("\u014c\5 \21\2\u014c\u014d\5\u0092J\2\u014d\u014f\3\2")
        buf.write("\2\2\u014e\u0147\3\2\2\2\u014e\u014b\3\2\2\2\u014f/\3")
        buf.write("\2\2\2\u0150\u0154\7\60\2\2\u0151\u0153\5\62\32\2\u0152")
        buf.write("\u0151\3\2\2\2\u0153\u0156\3\2\2\2\u0154\u0152\3\2\2\2")
        buf.write("\u0154\u0155\3\2\2\2\u0155\u0157\3\2\2\2\u0156\u0154\3")
        buf.write("\2\2\2\u0157\u0158\7\61\2\2\u0158\61\3\2\2\2\u0159\u015a")
        buf.write("\7\67\2\2\u015a\u015c\7.\2\2\u015b\u015d\5&\24\2\u015c")
        buf.write("\u015b\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\3\2\2\2")
        buf.write("\u015e\u015f\7/\2\2\u015f\u0160\5$\23\2\u0160\u0161\5")
        buf.write("\u0092J\2\u0161\63\3\2\2\2\u0162\u0163\5\66\34\2\u0163")
        buf.write("\65\3\2\2\2\u0164\u0165\b\34\1\2\u0165\u0166\58\35\2\u0166")
        buf.write("\u016c\3\2\2\2\u0167\u0168\f\4\2\2\u0168\u0169\7%\2\2")
        buf.write("\u0169\u016b\58\35\2\u016a\u0167\3\2\2\2\u016b\u016e\3")
        buf.write("\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d\67")
        buf.write("\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0170\b\35\1\2\u0170")
        buf.write("\u0171\5:\36\2\u0171\u0177\3\2\2\2\u0172\u0173\f\4\2\2")
        buf.write("\u0173\u0174\7$\2\2\u0174\u0176\5:\36\2\u0175\u0172\3")
        buf.write("\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178")
        buf.write("\3\2\2\2\u01789\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u017b")
        buf.write("\b\36\1\2\u017b\u017c\5<\37\2\u017c\u0183\3\2\2\2\u017d")
        buf.write("\u017e\f\4\2\2\u017e\u017f\5\u0082B\2\u017f\u0180\5<\37")
        buf.write("\2\u0180\u0182\3\2\2\2\u0181\u017d\3\2\2\2\u0182\u0185")
        buf.write("\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write(";\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u0187\b\37\1\2\u0187")
        buf.write("\u0188\5> \2\u0188\u018f\3\2\2\2\u0189\u018a\f\4\2\2\u018a")
        buf.write("\u018b\5\u0084C\2\u018b\u018c\5> \2\u018c\u018e\3\2\2")
        buf.write("\2\u018d\u0189\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d")
        buf.write("\3\2\2\2\u018f\u0190\3\2\2\2\u0190=\3\2\2\2\u0191\u018f")
        buf.write("\3\2\2\2\u0192\u0193\b \1\2\u0193\u0194\5@!\2\u0194\u019b")
        buf.write("\3\2\2\2\u0195\u0196\f\4\2\2\u0196\u0197\5\u0086D\2\u0197")
        buf.write("\u0198\5@!\2\u0198\u019a\3\2\2\2\u0199\u0195\3\2\2\2\u019a")
        buf.write("\u019d\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3\2\2\2")
        buf.write("\u019c?\3\2\2\2\u019d\u019b\3\2\2\2\u019e\u019f\5\u0088")
        buf.write("E\2\u019f\u01a0\5@!\2\u01a0\u01a3\3\2\2\2\u01a1\u01a3")
        buf.write("\5B\"\2\u01a2\u019e\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3")
        buf.write("A\3\2\2\2\u01a4\u01a6\5\u008cG\2\u01a5\u01a7\5H%\2\u01a6")
        buf.write("\u01a5\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01ab\3\2\2\2")
        buf.write("\u01a8\u01aa\5D#\2\u01a9\u01a8\3\2\2\2\u01aa\u01ad\3\2")
        buf.write("\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01acC\3")
        buf.write("\2\2\2\u01ad\u01ab\3\2\2\2\u01ae\u01af\7,\2\2\u01af\u01b1")
        buf.write("\7\67\2\2\u01b0\u01b2\5H%\2\u01b1\u01b0\3\2\2\2\u01b1")
        buf.write("\u01b2\3\2\2\2\u01b2\u01b4\3\2\2\2\u01b3\u01b5\5F$\2\u01b4")
        buf.write("\u01b3\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b8\3\2\2\2")
        buf.write("\u01b6\u01b8\5F$\2\u01b7\u01ae\3\2\2\2\u01b7\u01b6\3\2")
        buf.write("\2\2\u01b8E\3\2\2\2\u01b9\u01ba\7\62\2\2\u01ba\u01bb\5")
        buf.write("\64\33\2\u01bb\u01bc\7\63\2\2\u01bc\u01be\3\2\2\2\u01bd")
        buf.write("\u01b9\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01bd\3\2\2\2")
        buf.write("\u01bf\u01c0\3\2\2\2\u01c0G\3\2\2\2\u01c1\u01c3\7.\2\2")
        buf.write("\u01c2\u01c4\5J&\2\u01c3\u01c2\3\2\2\2\u01c3\u01c4\3\2")
        buf.write("\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c6\7/\2\2\u01c6I\3\2")
        buf.write("\2\2\u01c7\u01cc\5\64\33\2\u01c8\u01c9\7\64\2\2\u01c9")
        buf.write("\u01cb\5\64\33\2\u01ca\u01c8\3\2\2\2\u01cb\u01ce\3\2\2")
        buf.write("\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cdK\3\2")
        buf.write("\2\2\u01ce\u01cc\3\2\2\2\u01cf\u01d0\5N(\2\u01d0\u01d1")
        buf.write("\5\u0092J\2\u01d1\u01e8\3\2\2\2\u01d2\u01d3\5P)\2\u01d3")
        buf.write("\u01d4\5\u0092J\2\u01d4\u01e8\3\2\2\2\u01d5\u01d6\5X-")
        buf.write("\2\u01d6\u01d7\5\u0092J\2\u01d7\u01e8\3\2\2\2\u01d8\u01d9")
        buf.write("\5^\60\2\u01d9\u01da\5\u0092J\2\u01da\u01e8\3\2\2\2\u01db")
        buf.write("\u01dc\5j\66\2\u01dc\u01dd\5\u0092J\2\u01dd\u01e8\3\2")
        buf.write("\2\2\u01de\u01df\5l\67\2\u01df\u01e0\5\u0092J\2\u01e0")
        buf.write("\u01e8\3\2\2\2\u01e1\u01e2\5n8\2\u01e2\u01e3\5\u0092J")
        buf.write("\2\u01e3\u01e8\3\2\2\2\u01e4\u01e5\5z>\2\u01e5\u01e6\5")
        buf.write("\u0092J\2\u01e6\u01e8\3\2\2\2\u01e7\u01cf\3\2\2\2\u01e7")
        buf.write("\u01d2\3\2\2\2\u01e7\u01d5\3\2\2\2\u01e7\u01d8\3\2\2\2")
        buf.write("\u01e7\u01db\3\2\2\2\u01e7\u01de\3\2\2\2\u01e7\u01e1\3")
        buf.write("\2\2\2\u01e7\u01e4\3\2\2\2\u01e8M\3\2\2\2\u01e9\u01ec")
        buf.write("\5\6\4\2\u01ea\u01ec\5\20\t\2\u01eb\u01e9\3\2\2\2\u01eb")
        buf.write("\u01ea\3\2\2\2\u01ecO\3\2\2\2\u01ed\u01ee\5R*\2\u01ee")
        buf.write("\u01ef\7\30\2\2\u01ef\u01f0\5V,\2\u01f0\u0206\3\2\2\2")
        buf.write("\u01f1\u01f2\5R*\2\u01f2\u01f3\7\'\2\2\u01f3\u01f4\5V")
        buf.write(",\2\u01f4\u0206\3\2\2\2\u01f5\u01f6\5R*\2\u01f6\u01f7")
        buf.write("\7(\2\2\u01f7\u01f8\5V,\2\u01f8\u0206\3\2\2\2\u01f9\u01fa")
        buf.write("\5R*\2\u01fa\u01fb\7)\2\2\u01fb\u01fc\5V,\2\u01fc\u0206")
        buf.write("\3\2\2\2\u01fd\u01fe\5R*\2\u01fe\u01ff\7*\2\2\u01ff\u0200")
        buf.write("\5V,\2\u0200\u0206\3\2\2\2\u0201\u0202\5R*\2\u0202\u0203")
        buf.write("\7+\2\2\u0203\u0204\5V,\2\u0204\u0206\3\2\2\2\u0205\u01ed")
        buf.write("\3\2\2\2\u0205\u01f1\3\2\2\2\u0205\u01f5\3\2\2\2\u0205")
        buf.write("\u01f9\3\2\2\2\u0205\u01fd\3\2\2\2\u0205\u0201\3\2\2\2")
        buf.write("\u0206Q\3\2\2\2\u0207\u020e\7\67\2\2\u0208\u0209\7\62")
        buf.write("\2\2\u0209\u020a\5\64\33\2\u020a\u020b\7\63\2\2\u020b")
        buf.write("\u020d\3\2\2\2\u020c\u0208\3\2\2\2\u020d\u0210\3\2\2\2")
        buf.write("\u020e\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u0212\3")
        buf.write("\2\2\2\u0210\u020e\3\2\2\2\u0211\u0213\5T+\2\u0212\u0211")
        buf.write("\3\2\2\2\u0212\u0213\3\2\2\2\u0213S\3\2\2\2\u0214\u0215")
        buf.write("\7,\2\2\u0215\u021c\7\67\2\2\u0216\u0217\7\62\2\2\u0217")
        buf.write("\u0218\5\64\33\2\u0218\u0219\7\63\2\2\u0219\u021b\3\2")
        buf.write("\2\2\u021a\u0216\3\2\2\2\u021b\u021e\3\2\2\2\u021c\u021a")
        buf.write("\3\2\2\2\u021c\u021d\3\2\2\2\u021d\u0220\3\2\2\2\u021e")
        buf.write("\u021c\3\2\2\2\u021f\u0221\5T+\2\u0220\u021f\3\2\2\2\u0220")
        buf.write("\u0221\3\2\2\2\u0221U\3\2\2\2\u0222\u0223\5\64\33\2\u0223")
        buf.write("W\3\2\2\2\u0224\u0225\7\3\2\2\u0225\u0226\7.\2\2\u0226")
        buf.write("\u0227\5\64\33\2\u0227\u0228\7/\2\2\u0228\u022c\7\60\2")
        buf.write("\2\u0229\u022b\5L\'\2\u022a\u0229\3\2\2\2\u022b\u022e")
        buf.write("\3\2\2\2\u022c\u022a\3\2\2\2\u022c\u022d\3\2\2\2\u022d")
        buf.write("\u022f\3\2\2\2\u022e\u022c\3\2\2\2\u022f\u0233\7\61\2")
        buf.write("\2\u0230\u0232\5Z.\2\u0231\u0230\3\2\2\2\u0232\u0235\3")
        buf.write("\2\2\2\u0233\u0231\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0237")
        buf.write("\3\2\2\2\u0235\u0233\3\2\2\2\u0236\u0238\5\\/\2\u0237")
        buf.write("\u0236\3\2\2\2\u0237\u0238\3\2\2\2\u0238Y\3\2\2\2\u0239")
        buf.write("\u023a\7\4\2\2\u023a\u023b\7\3\2\2\u023b\u023c\7.\2\2")
        buf.write("\u023c\u023d\5\64\33\2\u023d\u023e\7/\2\2\u023e\u0242")
        buf.write("\7\60\2\2\u023f\u0241\5L\'\2\u0240\u023f\3\2\2\2\u0241")
        buf.write("\u0244\3\2\2\2\u0242\u0240\3\2\2\2\u0242\u0243\3\2\2\2")
        buf.write("\u0243\u0245\3\2\2\2\u0244\u0242\3\2\2\2\u0245\u0246\7")
        buf.write("\61\2\2\u0246[\3\2\2\2\u0247\u0248\7\4\2\2\u0248\u024c")
        buf.write("\7\60\2\2\u0249\u024b\5L\'\2\u024a\u0249\3\2\2\2\u024b")
        buf.write("\u024e\3\2\2\2\u024c\u024a\3\2\2\2\u024c\u024d\3\2\2\2")
        buf.write("\u024d\u024f\3\2\2\2\u024e\u024c\3\2\2\2\u024f\u0250\7")
        buf.write("\61\2\2\u0250]\3\2\2\2\u0251\u0254\5`\61\2\u0252\u0254")
        buf.write("\5h\65\2\u0253\u0251\3\2\2\2\u0253\u0252\3\2\2\2\u0254")
        buf.write("_\3\2\2\2\u0255\u0256\7\5\2\2\u0256\u0257\5b\62\2\u0257")
        buf.write("\u025b\7\60\2\2\u0258\u025a\5L\'\2\u0259\u0258\3\2\2\2")
        buf.write("\u025a\u025d\3\2\2\2\u025b\u0259\3\2\2\2\u025b\u025c\3")
        buf.write("\2\2\2\u025c\u025e\3\2\2\2\u025d\u025b\3\2\2\2\u025e\u025f")
        buf.write("\7\61\2\2\u025f\u0270\3\2\2\2\u0260\u0261\7\5\2\2\u0261")
        buf.write("\u0262\5d\63\2\u0262\u0263\7\65\2\2\u0263\u0264\5b\62")
        buf.write("\2\u0264\u0265\7\65\2\2\u0265\u0266\5f\64\2\u0266\u026a")
        buf.write("\7\60\2\2\u0267\u0269\5L\'\2\u0268\u0267\3\2\2\2\u0269")
        buf.write("\u026c\3\2\2\2\u026a\u0268\3\2\2\2\u026a\u026b\3\2\2\2")
        buf.write("\u026b\u026d\3\2\2\2\u026c\u026a\3\2\2\2\u026d\u026e\7")
        buf.write("\61\2\2\u026e\u0270\3\2\2\2\u026f\u0255\3\2\2\2\u026f")
        buf.write("\u0260\3\2\2\2\u0270a\3\2\2\2\u0271\u0272\5\64\33\2\u0272")
        buf.write("c\3\2\2\2\u0273\u027d\5P)\2\u0274\u0275\7\23\2\2\u0275")
        buf.write("\u0276\7\67\2\2\u0276\u027d\5\16\b\2\u0277\u0278\7\23")
        buf.write("\2\2\u0278\u0279\7\67\2\2\u0279\u027a\5\n\6\2\u027a\u027b")
        buf.write("\5\16\b\2\u027b\u027d\3\2\2\2\u027c\u0273\3\2\2\2\u027c")
        buf.write("\u0274\3\2\2\2\u027c\u0277\3\2\2\2\u027de\3\2\2\2\u027e")
        buf.write("\u027f\7\67\2\2\u027f\u0280\7\30\2\2\u0280\u0291\5\64")
        buf.write("\33\2\u0281\u0282\7\67\2\2\u0282\u0283\7\'\2\2\u0283\u0291")
        buf.write("\5\64\33\2\u0284\u0285\7\67\2\2\u0285\u0286\7(\2\2\u0286")
        buf.write("\u0291\5\64\33\2\u0287\u0288\7\67\2\2\u0288\u0289\7)\2")
        buf.write("\2\u0289\u0291\5\64\33\2\u028a\u028b\7\67\2\2\u028b\u028c")
        buf.write("\7*\2\2\u028c\u0291\5\64\33\2\u028d\u028e\7\67\2\2\u028e")
        buf.write("\u028f\7+\2\2\u028f\u0291\5\64\33\2\u0290\u027e\3\2\2")
        buf.write("\2\u0290\u0281\3\2\2\2\u0290\u0284\3\2\2\2\u0290\u0287")
        buf.write("\3\2\2\2\u0290\u028a\3\2\2\2\u0290\u028d\3\2\2\2\u0291")
        buf.write("g\3\2\2\2\u0292\u0293\7\5\2\2\u0293\u0294\5|?\2\u0294")
        buf.write("\u0295\7\64\2\2\u0295\u0296\5~@\2\u0296\u0297\7\30\2\2")
        buf.write("\u0297\u0298\7\26\2\2\u0298\u0299\5\u0080A\2\u0299\u029d")
        buf.write("\7\60\2\2\u029a\u029c\5L\'\2\u029b\u029a\3\2\2\2\u029c")
        buf.write("\u029f\3\2\2\2\u029d\u029b\3\2\2\2\u029d\u029e\3\2\2\2")
        buf.write("\u029e\u02a0\3\2\2\2\u029f\u029d\3\2\2\2\u02a0\u02a1\7")
        buf.write("\61\2\2\u02a1i\3\2\2\2\u02a2\u02a3\7\25\2\2\u02a3k\3\2")
        buf.write("\2\2\u02a4\u02a5\7\24\2\2\u02a5m\3\2\2\2\u02a6\u02a9\5")
        buf.write("p9\2\u02a7\u02a9\5t;\2\u02a8\u02a6\3\2\2\2\u02a8\u02a7")
        buf.write("\3\2\2\2\u02a9o\3\2\2\2\u02aa\u02ac\5r:\2\u02ab\u02aa")
        buf.write("\3\2\2\2\u02ac\u02ad\3\2\2\2\u02ad\u02ab\3\2\2\2\u02ad")
        buf.write("\u02ae\3\2\2\2\u02ae\u02af\3\2\2\2\u02af\u02b0\7\67\2")
        buf.write("\2\u02b0\u02b2\7.\2\2\u02b1\u02b3\5x=\2\u02b2\u02b1\3")
        buf.write("\2\2\2\u02b2\u02b3\3\2\2\2\u02b3\u02b4\3\2\2\2\u02b4\u02b5")
        buf.write("\7/\2\2\u02b5q\3\2\2\2\u02b6\u02b7\7\67\2\2\u02b7\u02b9")
        buf.write("\7.\2\2\u02b8\u02ba\5x=\2\u02b9\u02b8\3\2\2\2\u02b9\u02ba")
        buf.write("\3\2\2\2\u02ba\u02bb\3\2\2\2\u02bb\u02bc\7/\2\2\u02bc")
        buf.write("\u02c3\7,\2\2\u02bd\u02bf\7\67\2\2\u02be\u02c0\5v<\2\u02bf")
        buf.write("\u02be\3\2\2\2\u02bf\u02c0\3\2\2\2\u02c0\u02c1\3\2\2\2")
        buf.write("\u02c1\u02c3\7,\2\2\u02c2\u02b6\3\2\2\2\u02c2\u02bd\3")
        buf.write("\2\2\2\u02c3s\3\2\2\2\u02c4\u02c5\7\67\2\2\u02c5\u02c7")
        buf.write("\7.\2\2\u02c6\u02c8\5x=\2\u02c7\u02c6\3\2\2\2\u02c7\u02c8")
        buf.write("\3\2\2\2\u02c8\u02c9\3\2\2\2\u02c9\u02ca\7/\2\2\u02ca")
        buf.write("u\3\2\2\2\u02cb\u02cc\7\62\2\2\u02cc\u02cd\5\64\33\2\u02cd")
        buf.write("\u02ce\7\63\2\2\u02ce\u02d0\3\2\2\2\u02cf\u02cb\3\2\2")
        buf.write("\2\u02d0\u02d1\3\2\2\2\u02d1\u02cf\3\2\2\2\u02d1\u02d2")
        buf.write("\3\2\2\2\u02d2w\3\2\2\2\u02d3\u02d8\5\64\33\2\u02d4\u02d5")
        buf.write("\7\64\2\2\u02d5\u02d7\5\64\33\2\u02d6\u02d4\3\2\2\2\u02d7")
        buf.write("\u02da\3\2\2\2\u02d8\u02d6\3\2\2\2\u02d8\u02d9\3\2\2\2")
        buf.write("\u02d9y\3\2\2\2\u02da\u02d8\3\2\2\2\u02db\u02dc\7\6\2")
        buf.write("\2\u02dc\u02df\5\64\33\2\u02dd\u02df\7\6\2\2\u02de\u02db")
        buf.write("\3\2\2\2\u02de\u02dd\3\2\2\2\u02df{\3\2\2\2\u02e0\u02e1")
        buf.write("\t\2\2\2\u02e1}\3\2\2\2\u02e2\u02e3\7\67\2\2\u02e3\177")
        buf.write("\3\2\2\2\u02e4\u02e5\5\64\33\2\u02e5\u0081\3\2\2\2\u02e6")
        buf.write("\u02e7\t\3\2\2\u02e7\u0083\3\2\2\2\u02e8\u02e9\t\4\2\2")
        buf.write("\u02e9\u0085\3\2\2\2\u02ea\u02eb\t\5\2\2\u02eb\u0087\3")
        buf.write("\2\2\2\u02ec\u02ed\t\6\2\2\u02ed\u0089\3\2\2\2\u02ee\u02f7")
        buf.write("\78\2\2\u02ef\u02f7\79\2\2\u02f0\u02f7\7:\2\2\u02f1\u02f7")
        buf.write("\7\17\2\2\u02f2\u02f7\7\20\2\2\u02f3\u02f7\7\21\2\2\u02f4")
        buf.write("\u02f7\5\30\r\2\u02f5\u02f7\7\67\2\2\u02f6\u02ee\3\2\2")
        buf.write("\2\u02f6\u02ef\3\2\2\2\u02f6\u02f0\3\2\2\2\u02f6\u02f1")
        buf.write("\3\2\2\2\u02f6\u02f2\3\2\2\2\u02f6\u02f3\3\2\2\2\u02f6")
        buf.write("\u02f4\3\2\2\2\u02f6\u02f5\3\2\2\2\u02f7\u008b\3\2\2\2")
        buf.write("\u02f8\u0306\7\67\2\2\u02f9\u0306\78\2\2\u02fa\u0306\7")
        buf.write("9\2\2\u02fb\u0306\7:\2\2\u02fc\u0306\7\17\2\2\u02fd\u0306")
        buf.write("\7\20\2\2\u02fe\u0306\7\21\2\2\u02ff\u0300\7.\2\2\u0300")
        buf.write("\u0301\5\64\33\2\u0301\u0302\7/\2\2\u0302\u0306\3\2\2")
        buf.write("\2\u0303\u0306\5\22\n\2\u0304\u0306\5\30\r\2\u0305\u02f8")
        buf.write("\3\2\2\2\u0305\u02f9\3\2\2\2\u0305\u02fa\3\2\2\2\u0305")
        buf.write("\u02fb\3\2\2\2\u0305\u02fc\3\2\2\2\u0305\u02fd\3\2\2\2")
        buf.write("\u0305\u02fe\3\2\2\2\u0305\u02ff\3\2\2\2\u0305\u0303\3")
        buf.write("\2\2\2\u0305\u0304\3\2\2\2\u0306\u008d\3\2\2\2\u0307\u0308")
        buf.write("\t\7\2\2\u0308\u008f\3\2\2\2\u0309\u030a\t\b\2\2\u030a")
        buf.write("\u0091\3\2\2\2\u030b\u030c\7\65\2\2\u030c\u0093\3\2\2")
        buf.write("\2E\u0097\u00aa\u00b5\u00bb\u00c3\u00cb\u00d9\u00e0\u00e9")
        buf.write("\u00f0\u00ff\u0107\u0110\u0118\u0122\u012c\u0132\u013c")
        buf.write("\u0142\u014e\u0154\u015c\u016c\u0177\u0183\u018f\u019b")
        buf.write("\u01a2\u01a6\u01ab\u01b1\u01b4\u01b7\u01bf\u01c3\u01cc")
        buf.write("\u01e7\u01eb\u0205\u020e\u0212\u021c\u0220\u022c\u0233")
        buf.write("\u0237\u0242\u024c\u0253\u025b\u026a\u026f\u027c\u0290")
        buf.write("\u029d\u02a8\u02ad\u02b2\u02b9\u02bf\u02c2\u02c7\u02d1")
        buf.write("\u02d8\u02de\u02f6\u0305")
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
    RULE_arrayLitContent = 10
    RULE_structLit = 11
    RULE_optionalStructFields = 12
    RULE_structFieldList = 13
    RULE_structFieldAssign = 14
    RULE_methodDecl = 15
    RULE_funcDecl = 16
    RULE_funcType = 17
    RULE_funcParam = 18
    RULE_funcListIdentifiers = 19
    RULE_typeDecl = 20
    RULE_structDeclBlock = 21
    RULE_structDeclField = 22
    RULE_interfaceDeclBlock = 23
    RULE_interfaceDeclField = 24
    RULE_expr = 25
    RULE_logicOrExpr = 26
    RULE_logicAndExpr = 27
    RULE_equalityExpr = 28
    RULE_additiveExpr = 29
    RULE_multiplicativeExpr = 30
    RULE_unaryExpr = 31
    RULE_primaryExpr = 32
    RULE_primarySuffix = 33
    RULE_arraySuffix = 34
    RULE_callSuffix = 35
    RULE_argList = 36
    RULE_statement = 37
    RULE_declarationStatement = 38
    RULE_assignStatement = 39
    RULE_assignStateLHS = 40
    RULE_assignTail = 41
    RULE_assignStateRHS = 42
    RULE_ifStatement = 43
    RULE_elseIfStatement = 44
    RULE_elseStatement = 45
    RULE_forStatement = 46
    RULE_basicForStatement = 47
    RULE_forCondition = 48
    RULE_forInitilization = 49
    RULE_forUpdate = 50
    RULE_forRangeStatement = 51
    RULE_breakStatement = 52
    RULE_continueStatement = 53
    RULE_callStatement = 54
    RULE_methodCallStatement = 55
    RULE_methodCallHead = 56
    RULE_funcCallStatement = 57
    RULE_callStatementArrayTail = 58
    RULE_callStatementParam = 59
    RULE_returnStatement = 60
    RULE_index = 61
    RULE_value = 62
    RULE_forArray = 63
    RULE_relationOp = 64
    RULE_addOp = 65
    RULE_mulOp = 66
    RULE_unaryOp = 67
    RULE_noArrayLit = 68
    RULE_term = 69
    RULE_intLitOrConstant = 70
    RULE_baseType = 71
    RULE_endOfStatement = 72

    ruleNames =  [ "program", "decl", "varDecl", "varDetail", "varDeclType", 
                   "arrayType", "varDeclExpr", "constDecl", "arrayLit", 
                   "arrayBlock", "arrayLitContent", "structLit", "optionalStructFields", 
                   "structFieldList", "structFieldAssign", "methodDecl", 
                   "funcDecl", "funcType", "funcParam", "funcListIdentifiers", 
                   "typeDecl", "structDeclBlock", "structDeclField", "interfaceDeclBlock", 
                   "interfaceDeclField", "expr", "logicOrExpr", "logicAndExpr", 
                   "equalityExpr", "additiveExpr", "multiplicativeExpr", 
                   "unaryExpr", "primaryExpr", "primarySuffix", "arraySuffix", 
                   "callSuffix", "argList", "statement", "declarationStatement", 
                   "assignStatement", "assignStateLHS", "assignTail", "assignStateRHS", 
                   "ifStatement", "elseIfStatement", "elseStatement", "forStatement", 
                   "basicForStatement", "forCondition", "forInitilization", 
                   "forUpdate", "forRangeStatement", "breakStatement", "continueStatement", 
                   "callStatement", "methodCallStatement", "methodCallHead", 
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
            self.state = 147 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 146
                self.decl()
                self.state = 149 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 151
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
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.varDecl()
                self.state = 154
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.funcDecl()
                self.state = 157
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.constDecl()
                self.state = 160
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
                self.methodDecl()
                self.state = 163
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 165
                self.typeDecl()
                self.state = 166
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
            self.state = 170
            self.match(MiniGoParser.VAR)
            self.state = 171
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 172
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
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.varDeclType()
                self.state = 175
                self.varDeclExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.varDeclType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 178
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
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.baseType()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.arrayType()
                self.state = 183
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
            self.state = 191 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 187
                self.match(MiniGoParser.LBRACKET)
                self.state = 188
                self.intLitOrConstant()
                self.state = 189
                self.match(MiniGoParser.RBRACKET)
                self.state = 193 
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
            self.state = 195
            self.match(MiniGoParser.DECLARE)
            self.state = 196
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
            self.state = 198
            self.match(MiniGoParser.CONST)
            self.state = 199
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 200
                self.varDeclType()


            self.state = 203
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
            self.state = 205
            self.arrayType()
            self.state = 206
            self.baseType()
            self.state = 207
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

        def arrayLitContent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ArrayLitContentContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ArrayLitContentContext,i)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(MiniGoParser.LBRACE)
            self.state = 210
            self.arrayLitContent()
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 211
                self.match(MiniGoParser.COMMA)
                self.state = 212
                self.arrayLitContent()
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 218
            self.match(MiniGoParser.RBRACE)
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
        self.enterRule(localctx, 20, self.RULE_arrayLitContent)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.arrayBlock()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
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
        self.enterRule(localctx, 22, self.RULE_structLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 225
            self.match(MiniGoParser.LBRACE)
            self.state = 226
            self.optionalStructFields()
            self.state = 227
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
        self.enterRule(localctx, 24, self.RULE_optionalStructFields)
        try:
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
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

        def structFieldAssign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StructFieldAssignContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StructFieldAssignContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structFieldList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFieldList" ):
                return visitor.visitStructFieldList(self)
            else:
                return visitor.visitChildren(self)




    def structFieldList(self):

        localctx = MiniGoParser.StructFieldListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_structFieldList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.structFieldAssign()
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 234
                self.match(MiniGoParser.COMMA)
                self.state = 235
                self.structFieldAssign()
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structFieldAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFieldAssign" ):
                return visitor.visitStructFieldAssign(self)
            else:
                return visitor.visitChildren(self)




    def structFieldAssign(self):

        localctx = MiniGoParser.StructFieldAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_structFieldAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 242
            self.match(MiniGoParser.COLON)
            self.state = 243
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
        self.enterRule(localctx, 30, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(MiniGoParser.FUNC)
            self.state = 246
            self.match(MiniGoParser.LPAREN)
            self.state = 247
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 248
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 249
            self.match(MiniGoParser.RPAREN)
            self.state = 250
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 251
            self.match(MiniGoParser.LPAREN)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 252
                self.funcParam()


            self.state = 255
            self.match(MiniGoParser.RPAREN)
            self.state = 256
            self.funcType()
            self.state = 257
            self.match(MiniGoParser.LBRACE)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 258
                self.statement()
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 264
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
        self.enterRule(localctx, 32, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(MiniGoParser.FUNC)
            self.state = 267
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 268
            self.match(MiniGoParser.LPAREN)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 269
                self.funcParam()


            self.state = 272
            self.match(MiniGoParser.RPAREN)
            self.state = 273
            self.funcType()
            self.state = 274
            self.match(MiniGoParser.LBRACE)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 275
                self.statement()
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 281
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
        self.enterRule(localctx, 34, self.RULE_funcType)
        try:
            self.state = 288
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.baseType()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.arrayType()
                self.state = 285
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
        self.enterRule(localctx, 36, self.RULE_funcParam)
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.funcListIdentifiers()
                self.state = 291
                self.varDeclType()
                self.state = 292
                self.match(MiniGoParser.COMMA)
                self.state = 293
                self.funcParam()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.funcListIdentifiers()
                self.state = 296
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
        self.enterRule(localctx, 38, self.RULE_funcListIdentifiers)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 302
                self.match(MiniGoParser.COMMA)
                self.state = 303
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
        self.enterRule(localctx, 40, self.RULE_typeDecl)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.match(MiniGoParser.TYPE)
                self.state = 307
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 308
                self.match(MiniGoParser.STRUCT)
                self.state = 309
                self.structDeclBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.match(MiniGoParser.TYPE)
                self.state = 311
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 312
                self.match(MiniGoParser.INTERFACE)
                self.state = 313
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
        self.enterRule(localctx, 42, self.RULE_structDeclBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(MiniGoParser.LBRACE)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.FUNC or _la==MiniGoParser.IDENTIFIER:
                self.state = 317
                self.structDeclField()
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 323
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
        self.enterRule(localctx, 44, self.RULE_structDeclField)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 326
                self.varDeclType()
                self.state = 327
                self.endOfStatement()
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.methodDecl()
                self.state = 330
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
        self.enterRule(localctx, 46, self.RULE_interfaceDeclBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(MiniGoParser.LBRACE)
            self.state = 338
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 335
                self.interfaceDeclField()
                self.state = 340
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 341
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
        self.enterRule(localctx, 48, self.RULE_interfaceDeclField)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 344
            self.match(MiniGoParser.LPAREN)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 345
                self.funcParam()


            self.state = 348
            self.match(MiniGoParser.RPAREN)
            self.state = 349
            self.funcType()
            self.state = 350
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
        self.enterRule(localctx, 50, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_logicOrExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.logicAndExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 362
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogicOrExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicOrExpr)
                    self.state = 357
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 358
                    self.match(MiniGoParser.OR)
                    self.state = 359
                    self.logicAndExpr(0) 
                self.state = 364
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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_logicAndExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.equalityExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 373
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogicAndExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicAndExpr)
                    self.state = 368
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 369
                    self.match(MiniGoParser.AND)
                    self.state = 370
                    self.equalityExpr(0) 
                self.state = 375
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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_equalityExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.additiveExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 385
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.EqualityExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpr)
                    self.state = 379
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 380
                    self.relationOp()
                    self.state = 381
                    self.additiveExpr(0) 
                self.state = 387
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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_additiveExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.multiplicativeExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 397
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.AdditiveExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpr)
                    self.state = 391
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 392
                    self.addOp()
                    self.state = 393
                    self.multiplicativeExpr(0) 
                self.state = 399
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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_multiplicativeExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.unaryExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 409
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.MultiplicativeExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpr)
                    self.state = 403
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 404
                    self.mulOp()
                    self.state = 405
                    self.unaryExpr() 
                self.state = 411
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
        self.enterRule(localctx, 62, self.RULE_unaryExpr)
        try:
            self.state = 416
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.unaryOp()
                self.state = 413
                self.unaryExpr()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
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


        def callSuffix(self):
            return self.getTypedRuleContext(MiniGoParser.CallSuffixContext,0)


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
        self.enterRule(localctx, 64, self.RULE_primaryExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.term()
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 419
                self.callSuffix()


            self.state = 425
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 422
                    self.primarySuffix() 
                self.state = 427
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        self.enterRule(localctx, 66, self.RULE_primarySuffix)
        try:
            self.state = 437
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.match(MiniGoParser.DOT)
                self.state = 429
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 431
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 430
                    self.callSuffix()


                self.state = 434
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                if la_ == 1:
                    self.state = 433
                    self.arraySuffix()


                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.arraySuffix()
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
        self.enterRule(localctx, 68, self.RULE_arraySuffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 439
                    self.match(MiniGoParser.LBRACKET)
                    self.state = 440
                    self.expr()
                    self.state = 441
                    self.match(MiniGoParser.RBRACKET)

                else:
                    raise NoViableAltException(self)
                self.state = 445 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        self.enterRule(localctx, 70, self.RULE_callSuffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(MiniGoParser.LPAREN)
            self.state = 449
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 448
                self.argList()


            self.state = 451
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
        self.enterRule(localctx, 72, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.expr()
            self.state = 458
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 454
                self.match(MiniGoParser.COMMA)
                self.state = 455
                self.expr()
                self.state = 460
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
        self.enterRule(localctx, 74, self.RULE_statement)
        try:
            self.state = 485
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.declarationStatement()
                self.state = 462
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
                self.assignStatement()
                self.state = 465
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 467
                self.ifStatement()
                self.state = 468
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 470
                self.forStatement()
                self.state = 471
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 473
                self.breakStatement()
                self.state = 474
                self.endOfStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 476
                self.continueStatement()
                self.state = 477
                self.endOfStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 479
                self.callStatement()
                self.state = 480
                self.endOfStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 482
                self.returnStatement()
                self.state = 483
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
        self.enterRule(localctx, 76, self.RULE_declarationStatement)
        try:
            self.state = 489
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 487
                self.varDecl()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 488
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
        self.enterRule(localctx, 78, self.RULE_assignStatement)
        try:
            self.state = 515
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.assignStateLHS()
                self.state = 492
                self.match(MiniGoParser.ASSIGN)
                self.state = 493
                self.assignStateRHS()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
                self.assignStateLHS()
                self.state = 496
                self.match(MiniGoParser.PLUS_ASSIGN)
                self.state = 497
                self.assignStateRHS()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 499
                self.assignStateLHS()
                self.state = 500
                self.match(MiniGoParser.MINUS_ASSIGN)
                self.state = 501
                self.assignStateRHS()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 503
                self.assignStateLHS()
                self.state = 504
                self.match(MiniGoParser.MUL_ASSIGN)
                self.state = 505
                self.assignStateRHS()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 507
                self.assignStateLHS()
                self.state = 508
                self.match(MiniGoParser.DIV_ASSIGN)
                self.state = 509
                self.assignStateRHS()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 511
                self.assignStateLHS()
                self.state = 512
                self.match(MiniGoParser.MOD_ASSIGN)
                self.state = 513
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

        def assignTail(self):
            return self.getTypedRuleContext(MiniGoParser.AssignTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignStateLHS

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStateLHS" ):
                return visitor.visitAssignStateLHS(self)
            else:
                return visitor.visitChildren(self)




    def assignStateLHS(self):

        localctx = MiniGoParser.AssignStateLHSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_assignStateLHS)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 524
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.LBRACKET:
                self.state = 518
                self.match(MiniGoParser.LBRACKET)
                self.state = 519
                self.expr()
                self.state = 520
                self.match(MiniGoParser.RBRACKET)
                self.state = 526
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 528
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.DOT:
                self.state = 527
                self.assignTail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

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

        def assignTail(self):
            return self.getTypedRuleContext(MiniGoParser.AssignTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignTail" ):
                return visitor.visitAssignTail(self)
            else:
                return visitor.visitChildren(self)




    def assignTail(self):

        localctx = MiniGoParser.AssignTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_assignTail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.match(MiniGoParser.DOT)
            self.state = 531
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 538
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.LBRACKET:
                self.state = 532
                self.match(MiniGoParser.LBRACKET)
                self.state = 533
                self.expr()
                self.state = 534
                self.match(MiniGoParser.RBRACKET)
                self.state = 540
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 542
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.DOT:
                self.state = 541
                self.assignTail()


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
        self.enterRule(localctx, 84, self.RULE_assignStateRHS)
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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def elseIfStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ElseIfStatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ElseIfStatementContext,i)


        def elseStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ElseStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniGoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_ifStatement)
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
            self.state = 561
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 558
                    self.elseIfStatement() 
                self.state = 563
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

            self.state = 565
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 564
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
        self.enterRule(localctx, 88, self.RULE_elseIfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
            self.match(MiniGoParser.ELSE)
            self.state = 568
            self.match(MiniGoParser.IF)
            self.state = 569
            self.match(MiniGoParser.LPAREN)
            self.state = 570
            self.expr()
            self.state = 571
            self.match(MiniGoParser.RPAREN)
            self.state = 572
            self.match(MiniGoParser.LBRACE)
            self.state = 576
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 573
                self.statement()
                self.state = 578
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 579
            self.match(MiniGoParser.RBRACE)
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
        self.enterRule(localctx, 90, self.RULE_elseStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.match(MiniGoParser.ELSE)
            self.state = 582
            self.match(MiniGoParser.LBRACE)
            self.state = 586
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 583
                self.statement()
                self.state = 588
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 589
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
        self.enterRule(localctx, 92, self.RULE_forStatement)
        try:
            self.state = 593
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
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
        self.enterRule(localctx, 94, self.RULE_basicForStatement)
        self._la = 0 # Token type
        try:
            self.state = 621
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
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
        self.enterRule(localctx, 96, self.RULE_forCondition)
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
        self.enterRule(localctx, 98, self.RULE_forInitilization)
        try:
            self.state = 634
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
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
        self.enterRule(localctx, 100, self.RULE_forUpdate)
        try:
            self.state = 654
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
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
        self.enterRule(localctx, 102, self.RULE_forRangeStatement)
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
        self.enterRule(localctx, 104, self.RULE_breakStatement)
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
        self.enterRule(localctx, 106, self.RULE_continueStatement)
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
        self.enterRule(localctx, 108, self.RULE_callStatement)
        try:
            self.state = 678
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
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

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def methodCallHead(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.MethodCallHeadContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.MethodCallHeadContext,i)


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
        self.enterRule(localctx, 110, self.RULE_methodCallStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 681 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 680
                    self.methodCallHead()

                else:
                    raise NoViableAltException(self)
                self.state = 683 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

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
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallHeadContext(ParserRuleContext):
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

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def callStatementParam(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementParamContext,0)


        def callStatementArrayTail(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementArrayTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodCallHead

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCallHead" ):
                return visitor.visitMethodCallHead(self)
            else:
                return visitor.visitChildren(self)




    def methodCallHead(self):

        localctx = MiniGoParser.MethodCallHeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_methodCallHead)
        self._la = 0 # Token type
        try:
            self.state = 704
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 692
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 693
                self.match(MiniGoParser.LPAREN)
                self.state = 695
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 694
                    self.callStatementParam()


                self.state = 697
                self.match(MiniGoParser.RPAREN)
                self.state = 698
                self.match(MiniGoParser.DOT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 699
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 701
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACKET:
                    self.state = 700
                    self.callStatementArrayTail()


                self.state = 703
                self.match(MiniGoParser.DOT)
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
        self.enterRule(localctx, 114, self.RULE_funcCallStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 707
            self.match(MiniGoParser.LPAREN)
            self.state = 709
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 708
                self.callStatementParam()


            self.state = 711
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
        self.enterRule(localctx, 116, self.RULE_callStatementArrayTail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 717 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 713
                self.match(MiniGoParser.LBRACKET)
                self.state = 714
                self.expr()
                self.state = 715
                self.match(MiniGoParser.RBRACKET)
                self.state = 719 
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
        self.enterRule(localctx, 118, self.RULE_callStatementParam)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 721
            self.expr()
            self.state = 726
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 722
                self.match(MiniGoParser.COMMA)
                self.state = 723
                self.expr()
                self.state = 728
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
        self.enterRule(localctx, 120, self.RULE_returnStatement)
        try:
            self.state = 732
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 729
                self.match(MiniGoParser.RETURN)
                self.state = 730
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 731
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
        self.enterRule(localctx, 122, self.RULE_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 734
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
        self.enterRule(localctx, 124, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 736
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
        self.enterRule(localctx, 126, self.RULE_forArray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 738
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
        self.enterRule(localctx, 128, self.RULE_relationOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 740
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
        self.enterRule(localctx, 130, self.RULE_addOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 742
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
        self.enterRule(localctx, 132, self.RULE_mulOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 744
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
        self.enterRule(localctx, 134, self.RULE_unaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 746
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
        self.enterRule(localctx, 136, self.RULE_noArrayLit)
        try:
            self.state = 756
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 748
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 749
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 750
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 751
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 752
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 753
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 754
                self.structLit()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 755
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
        self.enterRule(localctx, 138, self.RULE_term)
        try:
            self.state = 771
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 758
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 759
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 760
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 761
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 762
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 763
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 764
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 765
                self.match(MiniGoParser.LPAREN)
                self.state = 766
                self.expr()
                self.state = 767
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 769
                self.arrayLit()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 770
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
        self.enterRule(localctx, 140, self.RULE_intLitOrConstant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 773
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
        self.enterRule(localctx, 142, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 775
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
        self.enterRule(localctx, 144, self.RULE_endOfStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 777
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
        self._predicates[26] = self.logicOrExpr_sempred
        self._predicates[27] = self.logicAndExpr_sempred
        self._predicates[28] = self.equalityExpr_sempred
        self._predicates[29] = self.additiveExpr_sempred
        self._predicates[30] = self.multiplicativeExpr_sempred
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
         




