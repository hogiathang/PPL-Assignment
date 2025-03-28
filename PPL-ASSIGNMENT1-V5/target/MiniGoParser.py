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
        buf.write("\u0312\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2\6\2\u0098")
        buf.write("\n\2\r\2\16\2\u0099\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00ad\n\3\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\5\5\u00b8\n\5\3\6\3\6\3")
        buf.write("\6\3\6\5\6\u00be\n\6\3\7\3\7\3\7\3\7\6\7\u00c4\n\7\r\7")
        buf.write("\16\7\u00c5\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\7\13\u00d7\n\13\f\13\16\13\u00da")
        buf.write("\13\13\3\13\3\13\3\f\3\f\5\f\u00e0\n\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\5\16\u00e9\n\16\3\17\3\17\3\17\7\17\u00ee")
        buf.write("\n\17\f\17\16\17\u00f1\13\17\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00ff\n\21\3")
        buf.write("\21\3\21\3\21\3\21\7\21\u0105\n\21\f\21\16\21\u0108\13")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\3\22\5\22\u0110\n\22\3\22")
        buf.write("\3\22\3\22\3\22\7\22\u0116\n\22\f\22\16\22\u0119\13\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\5\23\u0122\n\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u012c\n\24")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u0132\n\25\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\5\26\u013c\n\26\3\27\3\27\7\27")
        buf.write("\u0140\n\27\f\27\16\27\u0143\13\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\7\31\u014d\n\31\f\31\16\31\u0150")
        buf.write("\13\31\3\31\3\31\3\32\3\32\3\32\5\32\u0157\n\32\3\32\3")
        buf.write("\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u0165\n\33\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\7\35\u016f\n\35\f\35\16\35\u0172\13\35\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\7\36\u017a\n\36\f\36\16\36\u017d\13")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u0186\n\37")
        buf.write("\f\37\16\37\u0189\13\37\3 \3 \3 \3 \3 \3 \3 \7 \u0192")
        buf.write("\n \f \16 \u0195\13 \3!\3!\3!\3!\3!\3!\3!\7!\u019e\n!")
        buf.write("\f!\16!\u01a1\13!\3\"\3\"\3\"\3\"\5\"\u01a7\n\"\3#\3#")
        buf.write("\5#\u01ab\n#\3#\7#\u01ae\n#\f#\16#\u01b1\13#\3$\3$\3$")
        buf.write("\5$\u01b6\n$\3$\5$\u01b9\n$\3$\5$\u01bc\n$\3%\3%\3%\3")
        buf.write("%\6%\u01c2\n%\r%\16%\u01c3\3&\3&\5&\u01c8\n&\3&\3&\3\'")
        buf.write("\3\'\3\'\7\'\u01cf\n\'\f\'\16\'\u01d2\13\'\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\5(\u01ec\n(\3)\3)\5)\u01f0\n)\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\5*\u020a\n*\3+\3+\3+\3+\3+\7+\u0211\n+\f+\16+\u0214")
        buf.write("\13+\3+\5+\u0217\n+\3,\3,\3,\3,\3,\3,\7,\u021f\n,\f,\16")
        buf.write(",\u0222\13,\3,\5,\u0225\n,\3-\3-\3.\3.\3.\3.\3.\3.\7.")
        buf.write("\u022f\n.\f.\16.\u0232\13.\3.\3.\7.\u0236\n.\f.\16.\u0239")
        buf.write("\13.\3.\5.\u023c\n.\3/\3/\3/\3/\3/\3/\3/\7/\u0245\n/\f")
        buf.write("/\16/\u0248\13/\3/\3/\3\60\3\60\3\60\7\60\u024f\n\60\f")
        buf.write("\60\16\60\u0252\13\60\3\60\3\60\3\61\3\61\5\61\u0258\n")
        buf.write("\61\3\62\3\62\3\62\3\62\7\62\u025e\n\62\f\62\16\62\u0261")
        buf.write("\13\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3")
        buf.write("\62\7\62\u026d\n\62\f\62\16\62\u0270\13\62\3\62\3\62\5")
        buf.write("\62\u0274\n\62\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\5\64\u0281\n\64\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\5\65\u0295\n\65\3\66\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\3\66\7\66\u02a0\n\66\f\66\16\66\u02a3")
        buf.write("\13\66\3\66\3\66\3\67\3\67\38\38\39\39\59\u02ad\n9\3:")
        buf.write("\6:\u02b0\n:\r:\16:\u02b1\3:\3:\3:\5:\u02b7\n:\3:\3:\3")
        buf.write(";\3;\3;\5;\u02be\n;\3;\3;\3;\3;\5;\u02c4\n;\3;\5;\u02c7")
        buf.write("\n;\3<\3<\3<\5<\u02cc\n<\3<\3<\3=\3=\3=\3=\6=\u02d4\n")
        buf.write("=\r=\16=\u02d5\3>\3>\3>\7>\u02db\n>\f>\16>\u02de\13>\3")
        buf.write("?\3?\3?\5?\u02e3\n?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3")
        buf.write("E\3F\3F\3G\3G\3G\3G\3G\3G\3G\3G\5G\u02fb\nG\3H\3H\3H\3")
        buf.write("H\3H\3H\3H\3H\3H\3H\3H\3H\3H\5H\u030a\nH\3I\3I\3J\3J\3")
        buf.write("K\3K\3K\2\78:<>@L\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln")
        buf.write("prtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e")
        buf.write("\u0090\u0092\u0094\2\t\4\2--\67\67\3\2\36#\3\2\31\32\3")
        buf.write("\2\33\35\4\2\32\32&&\3\2\678\4\2\13\16\67\67\2\u032b\2")
        buf.write("\u0097\3\2\2\2\4\u00ac\3\2\2\2\6\u00ae\3\2\2\2\b\u00b7")
        buf.write("\3\2\2\2\n\u00bd\3\2\2\2\f\u00c3\3\2\2\2\16\u00c7\3\2")
        buf.write("\2\2\20\u00ca\3\2\2\2\22\u00ce\3\2\2\2\24\u00d2\3\2\2")
        buf.write("\2\26\u00df\3\2\2\2\30\u00e1\3\2\2\2\32\u00e8\3\2\2\2")
        buf.write("\34\u00ea\3\2\2\2\36\u00f2\3\2\2\2 \u00f6\3\2\2\2\"\u010b")
        buf.write("\3\2\2\2$\u0121\3\2\2\2&\u012b\3\2\2\2(\u0131\3\2\2\2")
        buf.write("*\u013b\3\2\2\2,\u013d\3\2\2\2.\u0146\3\2\2\2\60\u014a")
        buf.write("\3\2\2\2\62\u0153\3\2\2\2\64\u0164\3\2\2\2\66\u0166\3")
        buf.write("\2\2\28\u0168\3\2\2\2:\u0173\3\2\2\2<\u017e\3\2\2\2>\u018a")
        buf.write("\3\2\2\2@\u0196\3\2\2\2B\u01a6\3\2\2\2D\u01a8\3\2\2\2")
        buf.write("F\u01bb\3\2\2\2H\u01c1\3\2\2\2J\u01c5\3\2\2\2L\u01cb\3")
        buf.write("\2\2\2N\u01eb\3\2\2\2P\u01ef\3\2\2\2R\u0209\3\2\2\2T\u020b")
        buf.write("\3\2\2\2V\u0218\3\2\2\2X\u0226\3\2\2\2Z\u0228\3\2\2\2")
        buf.write("\\\u023d\3\2\2\2^\u024b\3\2\2\2`\u0257\3\2\2\2b\u0273")
        buf.write("\3\2\2\2d\u0275\3\2\2\2f\u0280\3\2\2\2h\u0294\3\2\2\2")
        buf.write("j\u0296\3\2\2\2l\u02a6\3\2\2\2n\u02a8\3\2\2\2p\u02ac\3")
        buf.write("\2\2\2r\u02af\3\2\2\2t\u02c6\3\2\2\2v\u02c8\3\2\2\2x\u02d3")
        buf.write("\3\2\2\2z\u02d7\3\2\2\2|\u02e2\3\2\2\2~\u02e4\3\2\2\2")
        buf.write("\u0080\u02e6\3\2\2\2\u0082\u02e8\3\2\2\2\u0084\u02ea\3")
        buf.write("\2\2\2\u0086\u02ec\3\2\2\2\u0088\u02ee\3\2\2\2\u008a\u02f0")
        buf.write("\3\2\2\2\u008c\u02fa\3\2\2\2\u008e\u0309\3\2\2\2\u0090")
        buf.write("\u030b\3\2\2\2\u0092\u030d\3\2\2\2\u0094\u030f\3\2\2\2")
        buf.write("\u0096\u0098\5\4\3\2\u0097\u0096\3\2\2\2\u0098\u0099\3")
        buf.write("\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b")
        buf.write("\3\2\2\2\u009b\u009c\7\2\2\3\u009c\3\3\2\2\2\u009d\u009e")
        buf.write("\5\6\4\2\u009e\u009f\5\u0094K\2\u009f\u00ad\3\2\2\2\u00a0")
        buf.write("\u00a1\5\"\22\2\u00a1\u00a2\5\u0094K\2\u00a2\u00ad\3\2")
        buf.write("\2\2\u00a3\u00a4\5\20\t\2\u00a4\u00a5\5\u0094K\2\u00a5")
        buf.write("\u00ad\3\2\2\2\u00a6\u00a7\5 \21\2\u00a7\u00a8\5\u0094")
        buf.write("K\2\u00a8\u00ad\3\2\2\2\u00a9\u00aa\5*\26\2\u00aa\u00ab")
        buf.write("\5\u0094K\2\u00ab\u00ad\3\2\2\2\u00ac\u009d\3\2\2\2\u00ac")
        buf.write("\u00a0\3\2\2\2\u00ac\u00a3\3\2\2\2\u00ac\u00a6\3\2\2\2")
        buf.write("\u00ac\u00a9\3\2\2\2\u00ad\5\3\2\2\2\u00ae\u00af\7\23")
        buf.write("\2\2\u00af\u00b0\7\67\2\2\u00b0\u00b1\5\b\5\2\u00b1\7")
        buf.write("\3\2\2\2\u00b2\u00b3\5\n\6\2\u00b3\u00b4\5\16\b\2\u00b4")
        buf.write("\u00b8\3\2\2\2\u00b5\u00b8\5\n\6\2\u00b6\u00b8\5\16\b")
        buf.write("\2\u00b7\u00b2\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b6")
        buf.write("\3\2\2\2\u00b8\t\3\2\2\2\u00b9\u00be\5\u0092J\2\u00ba")
        buf.write("\u00bb\5\f\7\2\u00bb\u00bc\5\u0092J\2\u00bc\u00be\3\2")
        buf.write("\2\2\u00bd\u00b9\3\2\2\2\u00bd\u00ba\3\2\2\2\u00be\13")
        buf.write("\3\2\2\2\u00bf\u00c0\7\62\2\2\u00c0\u00c1\5\u0090I\2\u00c1")
        buf.write("\u00c2\7\63\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00bf\3\2\2")
        buf.write("\2\u00c4\u00c5\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6")
        buf.write("\3\2\2\2\u00c6\r\3\2\2\2\u00c7\u00c8\7\27\2\2\u00c8\u00c9")
        buf.write("\5\66\34\2\u00c9\17\3\2\2\2\u00ca\u00cb\7\22\2\2\u00cb")
        buf.write("\u00cc\7\67\2\2\u00cc\u00cd\5\16\b\2\u00cd\21\3\2\2\2")
        buf.write("\u00ce\u00cf\5\f\7\2\u00cf\u00d0\5\u0092J\2\u00d0\u00d1")
        buf.write("\5\24\13\2\u00d1\23\3\2\2\2\u00d2\u00d3\7\60\2\2\u00d3")
        buf.write("\u00d8\5\26\f\2\u00d4\u00d5\7\64\2\2\u00d5\u00d7\5\26")
        buf.write("\f\2\u00d6\u00d4\3\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d6")
        buf.write("\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00db\3\2\2\2\u00da")
        buf.write("\u00d8\3\2\2\2\u00db\u00dc\7\61\2\2\u00dc\25\3\2\2\2\u00dd")
        buf.write("\u00e0\5\24\13\2\u00de\u00e0\5\u008cG\2\u00df\u00dd\3")
        buf.write("\2\2\2\u00df\u00de\3\2\2\2\u00e0\27\3\2\2\2\u00e1\u00e2")
        buf.write("\7\67\2\2\u00e2\u00e3\7\60\2\2\u00e3\u00e4\5\32\16\2\u00e4")
        buf.write("\u00e5\7\61\2\2\u00e5\31\3\2\2\2\u00e6\u00e9\5\34\17\2")
        buf.write("\u00e7\u00e9\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7\3")
        buf.write("\2\2\2\u00e9\33\3\2\2\2\u00ea\u00ef\5\36\20\2\u00eb\u00ec")
        buf.write("\7\64\2\2\u00ec\u00ee\5\36\20\2\u00ed\u00eb\3\2\2\2\u00ee")
        buf.write("\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2")
        buf.write("\u00f0\35\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3\7\67")
        buf.write("\2\2\u00f3\u00f4\7\66\2\2\u00f4\u00f5\5\66\34\2\u00f5")
        buf.write("\37\3\2\2\2\u00f6\u00f7\7\7\2\2\u00f7\u00f8\7.\2\2\u00f8")
        buf.write("\u00f9\7\67\2\2\u00f9\u00fa\7\67\2\2\u00fa\u00fb\7/\2")
        buf.write("\2\u00fb\u00fc\7\67\2\2\u00fc\u00fe\7.\2\2\u00fd\u00ff")
        buf.write("\5&\24\2\u00fe\u00fd\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff")
        buf.write("\u0100\3\2\2\2\u0100\u0101\7/\2\2\u0101\u0102\5$\23\2")
        buf.write("\u0102\u0106\7\60\2\2\u0103\u0105\5N(\2\u0104\u0103\3")
        buf.write("\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107")
        buf.write("\3\2\2\2\u0107\u0109\3\2\2\2\u0108\u0106\3\2\2\2\u0109")
        buf.write("\u010a\7\61\2\2\u010a!\3\2\2\2\u010b\u010c\7\7\2\2\u010c")
        buf.write("\u010d\7\67\2\2\u010d\u010f\7.\2\2\u010e\u0110\5&\24\2")
        buf.write("\u010f\u010e\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111\3")
        buf.write("\2\2\2\u0111\u0112\7/\2\2\u0112\u0113\5$\23\2\u0113\u0117")
        buf.write("\7\60\2\2\u0114\u0116\5N(\2\u0115\u0114\3\2\2\2\u0116")
        buf.write("\u0119\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2")
        buf.write("\u0118\u011a\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u011b\7")
        buf.write("\61\2\2\u011b#\3\2\2\2\u011c\u0122\5\u0092J\2\u011d\u011e")
        buf.write("\5\f\7\2\u011e\u011f\5\u0092J\2\u011f\u0122\3\2\2\2\u0120")
        buf.write("\u0122\3\2\2\2\u0121\u011c\3\2\2\2\u0121\u011d\3\2\2\2")
        buf.write("\u0121\u0120\3\2\2\2\u0122%\3\2\2\2\u0123\u0124\5(\25")
        buf.write("\2\u0124\u0125\5\n\6\2\u0125\u0126\7\64\2\2\u0126\u0127")
        buf.write("\5&\24\2\u0127\u012c\3\2\2\2\u0128\u0129\5(\25\2\u0129")
        buf.write("\u012a\5\n\6\2\u012a\u012c\3\2\2\2\u012b\u0123\3\2\2\2")
        buf.write("\u012b\u0128\3\2\2\2\u012c\'\3\2\2\2\u012d\u0132\7\67")
        buf.write("\2\2\u012e\u012f\7\67\2\2\u012f\u0130\7\64\2\2\u0130\u0132")
        buf.write("\5(\25\2\u0131\u012d\3\2\2\2\u0131\u012e\3\2\2\2\u0132")
        buf.write(")\3\2\2\2\u0133\u0134\7\b\2\2\u0134\u0135\7\67\2\2\u0135")
        buf.write("\u0136\7\t\2\2\u0136\u013c\5,\27\2\u0137\u0138\7\b\2\2")
        buf.write("\u0138\u0139\7\67\2\2\u0139\u013a\7\n\2\2\u013a\u013c")
        buf.write("\5\60\31\2\u013b\u0133\3\2\2\2\u013b\u0137\3\2\2\2\u013c")
        buf.write("+\3\2\2\2\u013d\u0141\7\60\2\2\u013e\u0140\5.\30\2\u013f")
        buf.write("\u013e\3\2\2\2\u0140\u0143\3\2\2\2\u0141\u013f\3\2\2\2")
        buf.write("\u0141\u0142\3\2\2\2\u0142\u0144\3\2\2\2\u0143\u0141\3")
        buf.write("\2\2\2\u0144\u0145\7\61\2\2\u0145-\3\2\2\2\u0146\u0147")
        buf.write("\7\67\2\2\u0147\u0148\5\n\6\2\u0148\u0149\5\u0094K\2\u0149")
        buf.write("/\3\2\2\2\u014a\u014e\7\60\2\2\u014b\u014d\5\62\32\2\u014c")
        buf.write("\u014b\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2")
        buf.write("\u014e\u014f\3\2\2\2\u014f\u0151\3\2\2\2\u0150\u014e\3")
        buf.write("\2\2\2\u0151\u0152\7\61\2\2\u0152\61\3\2\2\2\u0153\u0154")
        buf.write("\7\67\2\2\u0154\u0156\7.\2\2\u0155\u0157\5\64\33\2\u0156")
        buf.write("\u0155\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0158\u0159\7/\2\2\u0159\u015a\5$\23\2\u015a\u015b\5")
        buf.write("\u0094K\2\u015b\63\3\2\2\2\u015c\u015d\5(\25\2\u015d\u015e")
        buf.write("\5\n\6\2\u015e\u015f\7\64\2\2\u015f\u0160\5\64\33\2\u0160")
        buf.write("\u0165\3\2\2\2\u0161\u0162\5(\25\2\u0162\u0163\5\n\6\2")
        buf.write("\u0163\u0165\3\2\2\2\u0164\u015c\3\2\2\2\u0164\u0161\3")
        buf.write("\2\2\2\u0165\65\3\2\2\2\u0166\u0167\58\35\2\u0167\67\3")
        buf.write("\2\2\2\u0168\u0169\b\35\1\2\u0169\u016a\5:\36\2\u016a")
        buf.write("\u0170\3\2\2\2\u016b\u016c\f\4\2\2\u016c\u016d\7%\2\2")
        buf.write("\u016d\u016f\5:\36\2\u016e\u016b\3\2\2\2\u016f\u0172\3")
        buf.write("\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u01719")
        buf.write("\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u0174\b\36\1\2\u0174")
        buf.write("\u0175\5<\37\2\u0175\u017b\3\2\2\2\u0176\u0177\f\4\2\2")
        buf.write("\u0177\u0178\7$\2\2\u0178\u017a\5<\37\2\u0179\u0176\3")
        buf.write("\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c")
        buf.write("\3\2\2\2\u017c;\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u017f")
        buf.write("\b\37\1\2\u017f\u0180\5> \2\u0180\u0187\3\2\2\2\u0181")
        buf.write("\u0182\f\4\2\2\u0182\u0183\5\u0084C\2\u0183\u0184\5> ")
        buf.write("\2\u0184\u0186\3\2\2\2\u0185\u0181\3\2\2\2\u0186\u0189")
        buf.write("\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188")
        buf.write("=\3\2\2\2\u0189\u0187\3\2\2\2\u018a\u018b\b \1\2\u018b")
        buf.write("\u018c\5@!\2\u018c\u0193\3\2\2\2\u018d\u018e\f\4\2\2\u018e")
        buf.write("\u018f\5\u0086D\2\u018f\u0190\5@!\2\u0190\u0192\3\2\2")
        buf.write("\2\u0191\u018d\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191")
        buf.write("\3\2\2\2\u0193\u0194\3\2\2\2\u0194?\3\2\2\2\u0195\u0193")
        buf.write("\3\2\2\2\u0196\u0197\b!\1\2\u0197\u0198\5B\"\2\u0198\u019f")
        buf.write("\3\2\2\2\u0199\u019a\f\4\2\2\u019a\u019b\5\u0088E\2\u019b")
        buf.write("\u019c\5B\"\2\u019c\u019e\3\2\2\2\u019d\u0199\3\2\2\2")
        buf.write("\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3")
        buf.write("\2\2\2\u01a0A\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a3")
        buf.write("\5\u008aF\2\u01a3\u01a4\5B\"\2\u01a4\u01a7\3\2\2\2\u01a5")
        buf.write("\u01a7\5D#\2\u01a6\u01a2\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7")
        buf.write("C\3\2\2\2\u01a8\u01aa\5\u008eH\2\u01a9\u01ab\5J&\2\u01aa")
        buf.write("\u01a9\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01af\3\2\2\2")
        buf.write("\u01ac\u01ae\5F$\2\u01ad\u01ac\3\2\2\2\u01ae\u01b1\3\2")
        buf.write("\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0E\3")
        buf.write("\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b3\7,\2\2\u01b3\u01b5")
        buf.write("\7\67\2\2\u01b4\u01b6\5J&\2\u01b5\u01b4\3\2\2\2\u01b5")
        buf.write("\u01b6\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7\u01b9\5H%\2\u01b8")
        buf.write("\u01b7\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bc\3\2\2\2")
        buf.write("\u01ba\u01bc\5H%\2\u01bb\u01b2\3\2\2\2\u01bb\u01ba\3\2")
        buf.write("\2\2\u01bcG\3\2\2\2\u01bd\u01be\7\62\2\2\u01be\u01bf\5")
        buf.write("\66\34\2\u01bf\u01c0\7\63\2\2\u01c0\u01c2\3\2\2\2\u01c1")
        buf.write("\u01bd\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c1\3\2\2\2")
        buf.write("\u01c3\u01c4\3\2\2\2\u01c4I\3\2\2\2\u01c5\u01c7\7.\2\2")
        buf.write("\u01c6\u01c8\5L\'\2\u01c7\u01c6\3\2\2\2\u01c7\u01c8\3")
        buf.write("\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca\7/\2\2\u01caK\3")
        buf.write("\2\2\2\u01cb\u01d0\5\66\34\2\u01cc\u01cd\7\64\2\2\u01cd")
        buf.write("\u01cf\5\66\34\2\u01ce\u01cc\3\2\2\2\u01cf\u01d2\3\2\2")
        buf.write("\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1M\3\2")
        buf.write("\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d4\5P)\2\u01d4\u01d5")
        buf.write("\5\u0094K\2\u01d5\u01ec\3\2\2\2\u01d6\u01d7\5R*\2\u01d7")
        buf.write("\u01d8\5\u0094K\2\u01d8\u01ec\3\2\2\2\u01d9\u01da\5Z.")
        buf.write("\2\u01da\u01db\5\u0094K\2\u01db\u01ec\3\2\2\2\u01dc\u01dd")
        buf.write("\5`\61\2\u01dd\u01de\5\u0094K\2\u01de\u01ec\3\2\2\2\u01df")
        buf.write("\u01e0\5l\67\2\u01e0\u01e1\5\u0094K\2\u01e1\u01ec\3\2")
        buf.write("\2\2\u01e2\u01e3\5n8\2\u01e3\u01e4\5\u0094K\2\u01e4\u01ec")
        buf.write("\3\2\2\2\u01e5\u01e6\5p9\2\u01e6\u01e7\5\u0094K\2\u01e7")
        buf.write("\u01ec\3\2\2\2\u01e8\u01e9\5|?\2\u01e9\u01ea\5\u0094K")
        buf.write("\2\u01ea\u01ec\3\2\2\2\u01eb\u01d3\3\2\2\2\u01eb\u01d6")
        buf.write("\3\2\2\2\u01eb\u01d9\3\2\2\2\u01eb\u01dc\3\2\2\2\u01eb")
        buf.write("\u01df\3\2\2\2\u01eb\u01e2\3\2\2\2\u01eb\u01e5\3\2\2\2")
        buf.write("\u01eb\u01e8\3\2\2\2\u01ecO\3\2\2\2\u01ed\u01f0\5\6\4")
        buf.write("\2\u01ee\u01f0\5\20\t\2\u01ef\u01ed\3\2\2\2\u01ef\u01ee")
        buf.write("\3\2\2\2\u01f0Q\3\2\2\2\u01f1\u01f2\5T+\2\u01f2\u01f3")
        buf.write("\7\30\2\2\u01f3\u01f4\5X-\2\u01f4\u020a\3\2\2\2\u01f5")
        buf.write("\u01f6\5T+\2\u01f6\u01f7\7\'\2\2\u01f7\u01f8\5X-\2\u01f8")
        buf.write("\u020a\3\2\2\2\u01f9\u01fa\5T+\2\u01fa\u01fb\7(\2\2\u01fb")
        buf.write("\u01fc\5X-\2\u01fc\u020a\3\2\2\2\u01fd\u01fe\5T+\2\u01fe")
        buf.write("\u01ff\7)\2\2\u01ff\u0200\5X-\2\u0200\u020a\3\2\2\2\u0201")
        buf.write("\u0202\5T+\2\u0202\u0203\7*\2\2\u0203\u0204\5X-\2\u0204")
        buf.write("\u020a\3\2\2\2\u0205\u0206\5T+\2\u0206\u0207\7+\2\2\u0207")
        buf.write("\u0208\5X-\2\u0208\u020a\3\2\2\2\u0209\u01f1\3\2\2\2\u0209")
        buf.write("\u01f5\3\2\2\2\u0209\u01f9\3\2\2\2\u0209\u01fd\3\2\2\2")
        buf.write("\u0209\u0201\3\2\2\2\u0209\u0205\3\2\2\2\u020aS\3\2\2")
        buf.write("\2\u020b\u0212\7\67\2\2\u020c\u020d\7\62\2\2\u020d\u020e")
        buf.write("\5\66\34\2\u020e\u020f\7\63\2\2\u020f\u0211\3\2\2\2\u0210")
        buf.write("\u020c\3\2\2\2\u0211\u0214\3\2\2\2\u0212\u0210\3\2\2\2")
        buf.write("\u0212\u0213\3\2\2\2\u0213\u0216\3\2\2\2\u0214\u0212\3")
        buf.write("\2\2\2\u0215\u0217\5V,\2\u0216\u0215\3\2\2\2\u0216\u0217")
        buf.write("\3\2\2\2\u0217U\3\2\2\2\u0218\u0219\7,\2\2\u0219\u0220")
        buf.write("\7\67\2\2\u021a\u021b\7\62\2\2\u021b\u021c\5\66\34\2\u021c")
        buf.write("\u021d\7\63\2\2\u021d\u021f\3\2\2\2\u021e\u021a\3\2\2")
        buf.write("\2\u021f\u0222\3\2\2\2\u0220\u021e\3\2\2\2\u0220\u0221")
        buf.write("\3\2\2\2\u0221\u0224\3\2\2\2\u0222\u0220\3\2\2\2\u0223")
        buf.write("\u0225\5V,\2\u0224\u0223\3\2\2\2\u0224\u0225\3\2\2\2\u0225")
        buf.write("W\3\2\2\2\u0226\u0227\5\66\34\2\u0227Y\3\2\2\2\u0228\u0229")
        buf.write("\7\3\2\2\u0229\u022a\7.\2\2\u022a\u022b\5\66\34\2\u022b")
        buf.write("\u022c\7/\2\2\u022c\u0230\7\60\2\2\u022d\u022f\5N(\2\u022e")
        buf.write("\u022d\3\2\2\2\u022f\u0232\3\2\2\2\u0230\u022e\3\2\2\2")
        buf.write("\u0230\u0231\3\2\2\2\u0231\u0233\3\2\2\2\u0232\u0230\3")
        buf.write("\2\2\2\u0233\u0237\7\61\2\2\u0234\u0236\5\\/\2\u0235\u0234")
        buf.write("\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235\3\2\2\2\u0237")
        buf.write("\u0238\3\2\2\2\u0238\u023b\3\2\2\2\u0239\u0237\3\2\2\2")
        buf.write("\u023a\u023c\5^\60\2\u023b\u023a\3\2\2\2\u023b\u023c\3")
        buf.write("\2\2\2\u023c[\3\2\2\2\u023d\u023e\7\4\2\2\u023e\u023f")
        buf.write("\7\3\2\2\u023f\u0240\7.\2\2\u0240\u0241\5\66\34\2\u0241")
        buf.write("\u0242\7/\2\2\u0242\u0246\7\60\2\2\u0243\u0245\5N(\2\u0244")
        buf.write("\u0243\3\2\2\2\u0245\u0248\3\2\2\2\u0246\u0244\3\2\2\2")
        buf.write("\u0246\u0247\3\2\2\2\u0247\u0249\3\2\2\2\u0248\u0246\3")
        buf.write("\2\2\2\u0249\u024a\7\61\2\2\u024a]\3\2\2\2\u024b\u024c")
        buf.write("\7\4\2\2\u024c\u0250\7\60\2\2\u024d\u024f\5N(\2\u024e")
        buf.write("\u024d\3\2\2\2\u024f\u0252\3\2\2\2\u0250\u024e\3\2\2\2")
        buf.write("\u0250\u0251\3\2\2\2\u0251\u0253\3\2\2\2\u0252\u0250\3")
        buf.write("\2\2\2\u0253\u0254\7\61\2\2\u0254_\3\2\2\2\u0255\u0258")
        buf.write("\5b\62\2\u0256\u0258\5j\66\2\u0257\u0255\3\2\2\2\u0257")
        buf.write("\u0256\3\2\2\2\u0258a\3\2\2\2\u0259\u025a\7\5\2\2\u025a")
        buf.write("\u025b\5d\63\2\u025b\u025f\7\60\2\2\u025c\u025e\5N(\2")
        buf.write("\u025d\u025c\3\2\2\2\u025e\u0261\3\2\2\2\u025f\u025d\3")
        buf.write("\2\2\2\u025f\u0260\3\2\2\2\u0260\u0262\3\2\2\2\u0261\u025f")
        buf.write("\3\2\2\2\u0262\u0263\7\61\2\2\u0263\u0274\3\2\2\2\u0264")
        buf.write("\u0265\7\5\2\2\u0265\u0266\5f\64\2\u0266\u0267\7\65\2")
        buf.write("\2\u0267\u0268\5d\63\2\u0268\u0269\7\65\2\2\u0269\u026a")
        buf.write("\5h\65\2\u026a\u026e\7\60\2\2\u026b\u026d\5N(\2\u026c")
        buf.write("\u026b\3\2\2\2\u026d\u0270\3\2\2\2\u026e\u026c\3\2\2\2")
        buf.write("\u026e\u026f\3\2\2\2\u026f\u0271\3\2\2\2\u0270\u026e\3")
        buf.write("\2\2\2\u0271\u0272\7\61\2\2\u0272\u0274\3\2\2\2\u0273")
        buf.write("\u0259\3\2\2\2\u0273\u0264\3\2\2\2\u0274c\3\2\2\2\u0275")
        buf.write("\u0276\5\66\34\2\u0276e\3\2\2\2\u0277\u0281\5R*\2\u0278")
        buf.write("\u0279\7\23\2\2\u0279\u027a\7\67\2\2\u027a\u0281\5\16")
        buf.write("\b\2\u027b\u027c\7\23\2\2\u027c\u027d\7\67\2\2\u027d\u027e")
        buf.write("\5\n\6\2\u027e\u027f\5\16\b\2\u027f\u0281\3\2\2\2\u0280")
        buf.write("\u0277\3\2\2\2\u0280\u0278\3\2\2\2\u0280\u027b\3\2\2\2")
        buf.write("\u0281g\3\2\2\2\u0282\u0283\7\67\2\2\u0283\u0284\7\30")
        buf.write("\2\2\u0284\u0295\5\66\34\2\u0285\u0286\7\67\2\2\u0286")
        buf.write("\u0287\7\'\2\2\u0287\u0295\5\66\34\2\u0288\u0289\7\67")
        buf.write("\2\2\u0289\u028a\7(\2\2\u028a\u0295\5\66\34\2\u028b\u028c")
        buf.write("\7\67\2\2\u028c\u028d\7)\2\2\u028d\u0295\5\66\34\2\u028e")
        buf.write("\u028f\7\67\2\2\u028f\u0290\7*\2\2\u0290\u0295\5\66\34")
        buf.write("\2\u0291\u0292\7\67\2\2\u0292\u0293\7+\2\2\u0293\u0295")
        buf.write("\5\66\34\2\u0294\u0282\3\2\2\2\u0294\u0285\3\2\2\2\u0294")
        buf.write("\u0288\3\2\2\2\u0294\u028b\3\2\2\2\u0294\u028e\3\2\2\2")
        buf.write("\u0294\u0291\3\2\2\2\u0295i\3\2\2\2\u0296\u0297\7\5\2")
        buf.write("\2\u0297\u0298\5~@\2\u0298\u0299\7\64\2\2\u0299\u029a")
        buf.write("\5\u0080A\2\u029a\u029b\7\30\2\2\u029b\u029c\7\26\2\2")
        buf.write("\u029c\u029d\5\u0082B\2\u029d\u02a1\7\60\2\2\u029e\u02a0")
        buf.write("\5N(\2\u029f\u029e\3\2\2\2\u02a0\u02a3\3\2\2\2\u02a1\u029f")
        buf.write("\3\2\2\2\u02a1\u02a2\3\2\2\2\u02a2\u02a4\3\2\2\2\u02a3")
        buf.write("\u02a1\3\2\2\2\u02a4\u02a5\7\61\2\2\u02a5k\3\2\2\2\u02a6")
        buf.write("\u02a7\7\25\2\2\u02a7m\3\2\2\2\u02a8\u02a9\7\24\2\2\u02a9")
        buf.write("o\3\2\2\2\u02aa\u02ad\5r:\2\u02ab\u02ad\5v<\2\u02ac\u02aa")
        buf.write("\3\2\2\2\u02ac\u02ab\3\2\2\2\u02adq\3\2\2\2\u02ae\u02b0")
        buf.write("\5t;\2\u02af\u02ae\3\2\2\2\u02b0\u02b1\3\2\2\2\u02b1\u02af")
        buf.write("\3\2\2\2\u02b1\u02b2\3\2\2\2\u02b2\u02b3\3\2\2\2\u02b3")
        buf.write("\u02b4\7\67\2\2\u02b4\u02b6\7.\2\2\u02b5\u02b7\5z>\2\u02b6")
        buf.write("\u02b5\3\2\2\2\u02b6\u02b7\3\2\2\2\u02b7\u02b8\3\2\2\2")
        buf.write("\u02b8\u02b9\7/\2\2\u02b9s\3\2\2\2\u02ba\u02bb\7\67\2")
        buf.write("\2\u02bb\u02bd\7.\2\2\u02bc\u02be\5z>\2\u02bd\u02bc\3")
        buf.write("\2\2\2\u02bd\u02be\3\2\2\2\u02be\u02bf\3\2\2\2\u02bf\u02c0")
        buf.write("\7/\2\2\u02c0\u02c7\7,\2\2\u02c1\u02c3\7\67\2\2\u02c2")
        buf.write("\u02c4\5x=\2\u02c3\u02c2\3\2\2\2\u02c3\u02c4\3\2\2\2\u02c4")
        buf.write("\u02c5\3\2\2\2\u02c5\u02c7\7,\2\2\u02c6\u02ba\3\2\2\2")
        buf.write("\u02c6\u02c1\3\2\2\2\u02c7u\3\2\2\2\u02c8\u02c9\7\67\2")
        buf.write("\2\u02c9\u02cb\7.\2\2\u02ca\u02cc\5z>\2\u02cb\u02ca\3")
        buf.write("\2\2\2\u02cb\u02cc\3\2\2\2\u02cc\u02cd\3\2\2\2\u02cd\u02ce")
        buf.write("\7/\2\2\u02cew\3\2\2\2\u02cf\u02d0\7\62\2\2\u02d0\u02d1")
        buf.write("\5\66\34\2\u02d1\u02d2\7\63\2\2\u02d2\u02d4\3\2\2\2\u02d3")
        buf.write("\u02cf\3\2\2\2\u02d4\u02d5\3\2\2\2\u02d5\u02d3\3\2\2\2")
        buf.write("\u02d5\u02d6\3\2\2\2\u02d6y\3\2\2\2\u02d7\u02dc\5\66\34")
        buf.write("\2\u02d8\u02d9\7\64\2\2\u02d9\u02db\5\66\34\2\u02da\u02d8")
        buf.write("\3\2\2\2\u02db\u02de\3\2\2\2\u02dc\u02da\3\2\2\2\u02dc")
        buf.write("\u02dd\3\2\2\2\u02dd{\3\2\2\2\u02de\u02dc\3\2\2\2\u02df")
        buf.write("\u02e0\7\6\2\2\u02e0\u02e3\5\66\34\2\u02e1\u02e3\7\6\2")
        buf.write("\2\u02e2\u02df\3\2\2\2\u02e2\u02e1\3\2\2\2\u02e3}\3\2")
        buf.write("\2\2\u02e4\u02e5\t\2\2\2\u02e5\177\3\2\2\2\u02e6\u02e7")
        buf.write("\7\67\2\2\u02e7\u0081\3\2\2\2\u02e8\u02e9\5\66\34\2\u02e9")
        buf.write("\u0083\3\2\2\2\u02ea\u02eb\t\3\2\2\u02eb\u0085\3\2\2\2")
        buf.write("\u02ec\u02ed\t\4\2\2\u02ed\u0087\3\2\2\2\u02ee\u02ef\t")
        buf.write("\5\2\2\u02ef\u0089\3\2\2\2\u02f0\u02f1\t\6\2\2\u02f1\u008b")
        buf.write("\3\2\2\2\u02f2\u02fb\7\21\2\2\u02f3\u02fb\78\2\2\u02f4")
        buf.write("\u02fb\79\2\2\u02f5\u02fb\7:\2\2\u02f6\u02fb\7\17\2\2")
        buf.write("\u02f7\u02fb\7\20\2\2\u02f8\u02fb\5\30\r\2\u02f9\u02fb")
        buf.write("\7\67\2\2\u02fa\u02f2\3\2\2\2\u02fa\u02f3\3\2\2\2\u02fa")
        buf.write("\u02f4\3\2\2\2\u02fa\u02f5\3\2\2\2\u02fa\u02f6\3\2\2\2")
        buf.write("\u02fa\u02f7\3\2\2\2\u02fa\u02f8\3\2\2\2\u02fa\u02f9\3")
        buf.write("\2\2\2\u02fb\u008d\3\2\2\2\u02fc\u030a\78\2\2\u02fd\u030a")
        buf.write("\79\2\2\u02fe\u030a\7:\2\2\u02ff\u030a\7\17\2\2\u0300")
        buf.write("\u030a\7\20\2\2\u0301\u030a\7\21\2\2\u0302\u0303\7.\2")
        buf.write("\2\u0303\u0304\5\66\34\2\u0304\u0305\7/\2\2\u0305\u030a")
        buf.write("\3\2\2\2\u0306\u030a\5\22\n\2\u0307\u030a\5\30\r\2\u0308")
        buf.write("\u030a\7\67\2\2\u0309\u02fc\3\2\2\2\u0309\u02fd\3\2\2")
        buf.write("\2\u0309\u02fe\3\2\2\2\u0309\u02ff\3\2\2\2\u0309\u0300")
        buf.write("\3\2\2\2\u0309\u0301\3\2\2\2\u0309\u0302\3\2\2\2\u0309")
        buf.write("\u0306\3\2\2\2\u0309\u0307\3\2\2\2\u0309\u0308\3\2\2\2")
        buf.write("\u030a\u008f\3\2\2\2\u030b\u030c\t\7\2\2\u030c\u0091\3")
        buf.write("\2\2\2\u030d\u030e\t\b\2\2\u030e\u0093\3\2\2\2\u030f\u0310")
        buf.write("\7\65\2\2\u0310\u0095\3\2\2\2D\u0099\u00ac\u00b7\u00bd")
        buf.write("\u00c5\u00d8\u00df\u00e8\u00ef\u00fe\u0106\u010f\u0117")
        buf.write("\u0121\u012b\u0131\u013b\u0141\u014e\u0156\u0164\u0170")
        buf.write("\u017b\u0187\u0193\u019f\u01a6\u01aa\u01af\u01b5\u01b8")
        buf.write("\u01bb\u01c3\u01c7\u01d0\u01eb\u01ef\u0209\u0212\u0216")
        buf.write("\u0220\u0224\u0230\u0237\u023b\u0246\u0250\u0257\u025f")
        buf.write("\u026e\u0273\u0280\u0294\u02a1\u02ac\u02b1\u02b6\u02bd")
        buf.write("\u02c3\u02c6\u02cb\u02d5\u02dc\u02e2\u02fa\u0309")
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
    RULE_prototypeParam = 25
    RULE_expr = 26
    RULE_logicOrExpr = 27
    RULE_logicAndExpr = 28
    RULE_equalityExpr = 29
    RULE_additiveExpr = 30
    RULE_multiplicativeExpr = 31
    RULE_unaryExpr = 32
    RULE_primaryExpr = 33
    RULE_primarySuffix = 34
    RULE_arraySuffix = 35
    RULE_callSuffix = 36
    RULE_argList = 37
    RULE_statement = 38
    RULE_declarationStatement = 39
    RULE_assignStatement = 40
    RULE_assignStateLHS = 41
    RULE_assignTail = 42
    RULE_assignStateRHS = 43
    RULE_ifStatement = 44
    RULE_elseIfStatement = 45
    RULE_elseStatement = 46
    RULE_forStatement = 47
    RULE_basicForStatement = 48
    RULE_forCondition = 49
    RULE_forInitilization = 50
    RULE_forUpdate = 51
    RULE_forRangeStatement = 52
    RULE_breakStatement = 53
    RULE_continueStatement = 54
    RULE_callStatement = 55
    RULE_methodCallStatement = 56
    RULE_methodCallHead = 57
    RULE_funcCallStatement = 58
    RULE_callStatementArrayTail = 59
    RULE_callStatementParam = 60
    RULE_returnStatement = 61
    RULE_index = 62
    RULE_value = 63
    RULE_forArray = 64
    RULE_relationOp = 65
    RULE_addOp = 66
    RULE_mulOp = 67
    RULE_unaryOp = 68
    RULE_noArrayLit = 69
    RULE_term = 70
    RULE_intLitOrConstant = 71
    RULE_baseType = 72
    RULE_endOfStatement = 73

    ruleNames =  [ "program", "decl", "varDecl", "varDetail", "varDeclType", 
                   "arrayType", "varDeclExpr", "constDecl", "arrayLit", 
                   "arrayBlock", "arrayLitContent", "structLit", "optionalStructFields", 
                   "structFieldList", "structFieldAssign", "methodDecl", 
                   "funcDecl", "funcType", "funcParam", "funcListIdentifiers", 
                   "typeDecl", "structDeclBlock", "structDeclField", "interfaceDeclBlock", 
                   "interfaceDeclField", "prototypeParam", "expr", "logicOrExpr", 
                   "logicAndExpr", "equalityExpr", "additiveExpr", "multiplicativeExpr", 
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
            self.state = 149 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 148
                self.decl()
                self.state = 151 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 153
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
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.varDecl()
                self.state = 156
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.funcDecl()
                self.state = 159
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.constDecl()
                self.state = 162
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 164
                self.methodDecl()
                self.state = 165
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 167
                self.typeDecl()
                self.state = 168
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
            self.state = 172
            self.match(MiniGoParser.VAR)
            self.state = 173
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 174
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
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.varDeclType()
                self.state = 177
                self.varDeclExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.varDeclType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
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
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.baseType()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.arrayType()
                self.state = 185
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
            self.state = 193 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 189
                self.match(MiniGoParser.LBRACKET)
                self.state = 190
                self.intLitOrConstant()
                self.state = 191
                self.match(MiniGoParser.RBRACKET)
                self.state = 195 
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
            self.state = 197
            self.match(MiniGoParser.DECLARE)
            self.state = 198
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
            self.state = 200
            self.match(MiniGoParser.CONST)
            self.state = 201
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 202
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
            self.state = 204
            self.arrayType()
            self.state = 205
            self.baseType()
            self.state = 206
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
            self.state = 208
            self.match(MiniGoParser.LBRACE)
            self.state = 209
            self.arrayLitContent()
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 210
                self.match(MiniGoParser.COMMA)
                self.state = 211
                self.arrayLitContent()
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 217
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
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.arrayBlock()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
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
            self.state = 223
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 224
            self.match(MiniGoParser.LBRACE)
            self.state = 225
            self.optionalStructFields()
            self.state = 226
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
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
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
            self.state = 232
            self.structFieldAssign()
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 233
                self.match(MiniGoParser.COMMA)
                self.state = 234
                self.structFieldAssign()
                self.state = 239
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
            self.state = 240
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 241
            self.match(MiniGoParser.COLON)
            self.state = 242
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
            self.state = 244
            self.match(MiniGoParser.FUNC)
            self.state = 245
            self.match(MiniGoParser.LPAREN)
            self.state = 246
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 247
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 248
            self.match(MiniGoParser.RPAREN)
            self.state = 249
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 250
            self.match(MiniGoParser.LPAREN)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 251
                self.funcParam()


            self.state = 254
            self.match(MiniGoParser.RPAREN)
            self.state = 255
            self.funcType()
            self.state = 256
            self.match(MiniGoParser.LBRACE)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 257
                self.statement()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 263
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
            self.state = 265
            self.match(MiniGoParser.FUNC)
            self.state = 266
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 267
            self.match(MiniGoParser.LPAREN)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 268
                self.funcParam()


            self.state = 271
            self.match(MiniGoParser.RPAREN)
            self.state = 272
            self.funcType()
            self.state = 273
            self.match(MiniGoParser.LBRACE)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 274
                self.statement()
                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 280
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
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.baseType()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.arrayType()
                self.state = 284
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
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.funcListIdentifiers()
                self.state = 290
                self.varDeclType()
                self.state = 291
                self.match(MiniGoParser.COMMA)
                self.state = 292
                self.funcParam()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.funcListIdentifiers()
                self.state = 295
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
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 301
                self.match(MiniGoParser.COMMA)
                self.state = 302
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
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.match(MiniGoParser.TYPE)
                self.state = 306
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 307
                self.match(MiniGoParser.STRUCT)
                self.state = 308
                self.structDeclBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.match(MiniGoParser.TYPE)
                self.state = 310
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 311
                self.match(MiniGoParser.INTERFACE)
                self.state = 312
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
            self.state = 315
            self.match(MiniGoParser.LBRACE)
            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 316
                self.structDeclField()
                self.state = 321
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 322
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
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 325
            self.varDeclType()
            self.state = 326
            self.endOfStatement()
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
            self.state = 328
            self.match(MiniGoParser.LBRACE)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 329
                self.interfaceDeclField()
                self.state = 334
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 335
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


        def prototypeParam(self):
            return self.getTypedRuleContext(MiniGoParser.PrototypeParamContext,0)


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
            self.state = 337
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 338
            self.match(MiniGoParser.LPAREN)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 339
                self.prototypeParam()


            self.state = 342
            self.match(MiniGoParser.RPAREN)
            self.state = 343
            self.funcType()
            self.state = 344
            self.endOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrototypeParamContext(ParserRuleContext):
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

        def prototypeParam(self):
            return self.getTypedRuleContext(MiniGoParser.PrototypeParamContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_prototypeParam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrototypeParam" ):
                return visitor.visitPrototypeParam(self)
            else:
                return visitor.visitChildren(self)




    def prototypeParam(self):

        localctx = MiniGoParser.PrototypeParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_prototypeParam)
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.funcListIdentifiers()
                self.state = 347
                self.varDeclType()
                self.state = 348
                self.match(MiniGoParser.COMMA)
                self.state = 349
                self.prototypeParam()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.funcListIdentifiers()
                self.state = 352
                self.varDeclType()
                pass


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
        self.enterRule(localctx, 52, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_logicOrExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.logicAndExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 366
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogicOrExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicOrExpr)
                    self.state = 361
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 362
                    self.match(MiniGoParser.OR)
                    self.state = 363
                    self.logicAndExpr(0) 
                self.state = 368
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_logicAndExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.equalityExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 377
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogicAndExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicAndExpr)
                    self.state = 372
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 373
                    self.match(MiniGoParser.AND)
                    self.state = 374
                    self.equalityExpr(0) 
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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_equalityExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.additiveExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 389
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.EqualityExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpr)
                    self.state = 383
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 384
                    self.relationOp()
                    self.state = 385
                    self.additiveExpr(0) 
                self.state = 391
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_additiveExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.multiplicativeExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 401
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.AdditiveExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpr)
                    self.state = 395
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 396
                    self.addOp()
                    self.state = 397
                    self.multiplicativeExpr(0) 
                self.state = 403
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_multiplicativeExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.unaryExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 413
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.MultiplicativeExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpr)
                    self.state = 407
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 408
                    self.mulOp()
                    self.state = 409
                    self.unaryExpr() 
                self.state = 415
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        self.enterRule(localctx, 64, self.RULE_unaryExpr)
        try:
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.unaryOp()
                self.state = 417
                self.unaryExpr()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.LPAREN, MiniGoParser.LBRACKET, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
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
        self.enterRule(localctx, 66, self.RULE_primaryExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.term()
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 423
                self.callSuffix()


            self.state = 429
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 426
                    self.primarySuffix() 
                self.state = 431
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
        self.enterRule(localctx, 68, self.RULE_primarySuffix)
        try:
            self.state = 441
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.match(MiniGoParser.DOT)
                self.state = 433
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 435
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 434
                    self.callSuffix()


                self.state = 438
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 437
                    self.arraySuffix()


                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 440
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
        self.enterRule(localctx, 70, self.RULE_arraySuffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 443
                    self.match(MiniGoParser.LBRACKET)
                    self.state = 444
                    self.expr()
                    self.state = 445
                    self.match(MiniGoParser.RBRACKET)

                else:
                    raise NoViableAltException(self)
                self.state = 449 
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
        self.enterRule(localctx, 72, self.RULE_callSuffix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(MiniGoParser.LPAREN)
            self.state = 453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 452
                self.argList()


            self.state = 455
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
        self.enterRule(localctx, 74, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.expr()
            self.state = 462
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 458
                self.match(MiniGoParser.COMMA)
                self.state = 459
                self.expr()
                self.state = 464
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
        self.enterRule(localctx, 76, self.RULE_statement)
        try:
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.declarationStatement()
                self.state = 466
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.assignStatement()
                self.state = 469
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 471
                self.ifStatement()
                self.state = 472
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 474
                self.forStatement()
                self.state = 475
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 477
                self.breakStatement()
                self.state = 478
                self.endOfStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 480
                self.continueStatement()
                self.state = 481
                self.endOfStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 483
                self.callStatement()
                self.state = 484
                self.endOfStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 486
                self.returnStatement()
                self.state = 487
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
            self.state = 493
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.varDecl()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 492
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
            self.state = 519
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.assignStateLHS()
                self.state = 496
                self.match(MiniGoParser.ASSIGN)
                self.state = 497
                self.assignStateRHS()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 499
                self.assignStateLHS()
                self.state = 500
                self.match(MiniGoParser.PLUS_ASSIGN)
                self.state = 501
                self.assignStateRHS()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 503
                self.assignStateLHS()
                self.state = 504
                self.match(MiniGoParser.MINUS_ASSIGN)
                self.state = 505
                self.assignStateRHS()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 507
                self.assignStateLHS()
                self.state = 508
                self.match(MiniGoParser.MUL_ASSIGN)
                self.state = 509
                self.assignStateRHS()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 511
                self.assignStateLHS()
                self.state = 512
                self.match(MiniGoParser.DIV_ASSIGN)
                self.state = 513
                self.assignStateRHS()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 515
                self.assignStateLHS()
                self.state = 516
                self.match(MiniGoParser.MOD_ASSIGN)
                self.state = 517
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
        self.enterRule(localctx, 82, self.RULE_assignStateLHS)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 528
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.LBRACKET:
                self.state = 522
                self.match(MiniGoParser.LBRACKET)
                self.state = 523
                self.expr()
                self.state = 524
                self.match(MiniGoParser.RBRACKET)
                self.state = 530
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 532
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.DOT:
                self.state = 531
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
        self.enterRule(localctx, 84, self.RULE_assignTail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.match(MiniGoParser.DOT)
            self.state = 535
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 542
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.LBRACKET:
                self.state = 536
                self.match(MiniGoParser.LBRACKET)
                self.state = 537
                self.expr()
                self.state = 538
                self.match(MiniGoParser.RBRACKET)
                self.state = 544
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 546
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.DOT:
                self.state = 545
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
        self.enterRule(localctx, 86, self.RULE_assignStateRHS)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 548
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
        self.enterRule(localctx, 88, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.match(MiniGoParser.IF)
            self.state = 551
            self.match(MiniGoParser.LPAREN)
            self.state = 552
            self.expr()
            self.state = 553
            self.match(MiniGoParser.RPAREN)
            self.state = 554
            self.match(MiniGoParser.LBRACE)
            self.state = 558
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 555
                self.statement()
                self.state = 560
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 561
            self.match(MiniGoParser.RBRACE)
            self.state = 565
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 562
                    self.elseIfStatement() 
                self.state = 567
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

            self.state = 569
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 568
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
        self.enterRule(localctx, 90, self.RULE_elseIfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self.match(MiniGoParser.ELSE)
            self.state = 572
            self.match(MiniGoParser.IF)
            self.state = 573
            self.match(MiniGoParser.LPAREN)
            self.state = 574
            self.expr()
            self.state = 575
            self.match(MiniGoParser.RPAREN)
            self.state = 576
            self.match(MiniGoParser.LBRACE)
            self.state = 580
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 577
                self.statement()
                self.state = 582
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 583
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
        self.enterRule(localctx, 92, self.RULE_elseStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.match(MiniGoParser.ELSE)
            self.state = 586
            self.match(MiniGoParser.LBRACE)
            self.state = 590
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 587
                self.statement()
                self.state = 592
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 593
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
        self.enterRule(localctx, 94, self.RULE_forStatement)
        try:
            self.state = 597
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 595
                self.basicForStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 596
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
        self.enterRule(localctx, 96, self.RULE_basicForStatement)
        self._la = 0 # Token type
        try:
            self.state = 625
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 599
                self.match(MiniGoParser.FOR)
                self.state = 600
                self.forCondition()
                self.state = 601
                self.match(MiniGoParser.LBRACE)
                self.state = 605
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 602
                    self.statement()
                    self.state = 607
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 608
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 610
                self.match(MiniGoParser.FOR)
                self.state = 611
                self.forInitilization()
                self.state = 612
                self.match(MiniGoParser.SEMI)
                self.state = 613
                self.forCondition()
                self.state = 614
                self.match(MiniGoParser.SEMI)
                self.state = 615
                self.forUpdate()
                self.state = 616
                self.match(MiniGoParser.LBRACE)
                self.state = 620
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 617
                    self.statement()
                    self.state = 622
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 623
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
        self.enterRule(localctx, 98, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 627
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
        self.enterRule(localctx, 100, self.RULE_forInitilization)
        try:
            self.state = 638
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 629
                self.assignStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 630
                self.match(MiniGoParser.VAR)
                self.state = 631
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 632
                self.varDeclExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 633
                self.match(MiniGoParser.VAR)
                self.state = 634
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 635
                self.varDeclType()
                self.state = 636
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
        self.enterRule(localctx, 102, self.RULE_forUpdate)
        try:
            self.state = 658
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 640
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 641
                self.match(MiniGoParser.ASSIGN)
                self.state = 642
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 643
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 644
                self.match(MiniGoParser.PLUS_ASSIGN)
                self.state = 645
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 646
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 647
                self.match(MiniGoParser.MINUS_ASSIGN)
                self.state = 648
                self.expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 649
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 650
                self.match(MiniGoParser.MUL_ASSIGN)
                self.state = 651
                self.expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 652
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 653
                self.match(MiniGoParser.DIV_ASSIGN)
                self.state = 654
                self.expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 655
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 656
                self.match(MiniGoParser.MOD_ASSIGN)
                self.state = 657
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
        self.enterRule(localctx, 104, self.RULE_forRangeStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 660
            self.match(MiniGoParser.FOR)
            self.state = 661
            self.index()
            self.state = 662
            self.match(MiniGoParser.COMMA)
            self.state = 663
            self.value()
            self.state = 664
            self.match(MiniGoParser.ASSIGN)
            self.state = 665
            self.match(MiniGoParser.RANGE)
            self.state = 666
            self.forArray()
            self.state = 667
            self.match(MiniGoParser.LBRACE)
            self.state = 671
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 668
                self.statement()
                self.state = 673
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 674
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
        self.enterRule(localctx, 106, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 676
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
        self.enterRule(localctx, 108, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 678
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
        self.enterRule(localctx, 110, self.RULE_callStatement)
        try:
            self.state = 682
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 680
                self.methodCallStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 681
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
        self.enterRule(localctx, 112, self.RULE_methodCallStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 685 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 684
                    self.methodCallHead()

                else:
                    raise NoViableAltException(self)
                self.state = 687 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

            self.state = 689
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 690
            self.match(MiniGoParser.LPAREN)
            self.state = 692
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 691
                self.callStatementParam()


            self.state = 694
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
        self.enterRule(localctx, 114, self.RULE_methodCallHead)
        self._la = 0 # Token type
        try:
            self.state = 708
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
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
                self.state = 702
                self.match(MiniGoParser.DOT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 703
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 705
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACKET:
                    self.state = 704
                    self.callStatementArrayTail()


                self.state = 707
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
        self.enterRule(localctx, 116, self.RULE_funcCallStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 710
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 711
            self.match(MiniGoParser.LPAREN)
            self.state = 713
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 712
                self.callStatementParam()


            self.state = 715
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
        self.enterRule(localctx, 118, self.RULE_callStatementArrayTail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 721 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 717
                self.match(MiniGoParser.LBRACKET)
                self.state = 718
                self.expr()
                self.state = 719
                self.match(MiniGoParser.RBRACKET)
                self.state = 723 
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
        self.enterRule(localctx, 120, self.RULE_callStatementParam)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 725
            self.expr()
            self.state = 730
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 726
                self.match(MiniGoParser.COMMA)
                self.state = 727
                self.expr()
                self.state = 732
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
        self.enterRule(localctx, 122, self.RULE_returnStatement)
        try:
            self.state = 736
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 733
                self.match(MiniGoParser.RETURN)
                self.state = 734
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 735
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
        self.enterRule(localctx, 124, self.RULE_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 738
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
        self.enterRule(localctx, 126, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 740
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
        self.enterRule(localctx, 128, self.RULE_forArray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 742
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
        self.enterRule(localctx, 130, self.RULE_relationOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 744
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
        self.enterRule(localctx, 132, self.RULE_addOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 746
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
        self.enterRule(localctx, 134, self.RULE_mulOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 748
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
        self.enterRule(localctx, 136, self.RULE_unaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 750
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

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

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
        self.enterRule(localctx, 138, self.RULE_noArrayLit)
        try:
            self.state = 760
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 752
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 753
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 754
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 755
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 756
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 757
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 758
                self.structLit()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 759
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
        self.enterRule(localctx, 140, self.RULE_term)
        try:
            self.state = 775
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 762
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 763
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 764
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 765
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 766
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 767
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 768
                self.match(MiniGoParser.LPAREN)
                self.state = 769
                self.expr()
                self.state = 770
                self.match(MiniGoParser.RPAREN)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 772
                self.arrayLit()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 773
                self.structLit()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 774
                self.match(MiniGoParser.IDENTIFIER)
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
        self.enterRule(localctx, 142, self.RULE_intLitOrConstant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 777
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
        self.enterRule(localctx, 144, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 779
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
        self.enterRule(localctx, 146, self.RULE_endOfStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 781
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
        self._predicates[27] = self.logicOrExpr_sempred
        self._predicates[28] = self.logicAndExpr_sempred
        self._predicates[29] = self.equalityExpr_sempred
        self._predicates[30] = self.additiveExpr_sempred
        self._predicates[31] = self.multiplicativeExpr_sempred
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
         




