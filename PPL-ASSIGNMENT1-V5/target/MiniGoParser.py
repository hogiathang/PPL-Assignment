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
        buf.write("\u02d1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\6\3\6\5\6\u00be\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\5\7\u00c9\n\7\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00d1\n\b")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\5\r\u00e7\n\r\3\16\3\16")
        buf.write("\5\16\u00eb\n\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\5")
        buf.write("\20\u00f4\n\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u00fe\n\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\5")
        buf.write("\24\u0107\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\6\25\u0115\n\25\r\25\16\25\u0116")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\6\26")
        buf.write("\u0123\n\26\r\26\16\26\u0124\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u012e\n\27\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\5\30\u0139\n\30\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u013f\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\5\32\u0149\n\32\3\33\3\33\3\33\3\33\5\33\u014f\n\33")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\5\35\u015e\n\35\3\36\3\36\3\36\3\36\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u016d\n\37")
        buf.write("\3 \3 \3!\3!\3!\3!\3!\3!\7!\u0177\n!\f!\16!\u017a\13!")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u0182\n\"\f\"\16\"\u0185")
        buf.write("\13\"\3#\3#\3#\3#\3#\3#\3#\7#\u018e\n#\f#\16#\u0191\13")
        buf.write("#\3$\3$\3$\3$\3$\3$\3$\7$\u019a\n$\f$\16$\u019d\13$\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\7%\u01a6\n%\f%\16%\u01a9\13%\3&\3")
        buf.write("&\3&\3&\5&\u01af\n&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\5(\u01c2\n(\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u01dc")
        buf.write("\n)\3*\3*\5*\u01e0\n*\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u01fa\n+\3")
        buf.write(",\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0208\n-\3.\3.\3")
        buf.write(".\5.\u020d\n.\3/\3/\3/\3/\3/\3/\6/\u0215\n/\r/\16/\u0216")
        buf.write("\3/\3/\3/\3/\3/\3/\3/\3/\6/\u0221\n/\r/\16/\u0222\3/\3")
        buf.write("/\3/\3/\3/\6/\u022a\n/\r/\16/\u022b\3/\3/\5/\u0230\n/")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\6\60\u0239\n\60\r")
        buf.write("\60\16\60\u023a\3\60\3\60\3\60\3\60\5\60\u0241\n\60\3")
        buf.write("\61\3\61\5\61\u0245\n\61\3\62\3\62\3\62\3\62\6\62\u024b")
        buf.write("\n\62\r\62\16\62\u024c\3\62\3\62\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\6\62\u0259\n\62\r\62\16\62\u025a\3")
        buf.write("\62\3\62\5\62\u025f\n\62\3\63\3\63\3\64\3\64\5\64\u0265")
        buf.write("\n\64\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\6\66\u0272\n\66\r\66\16\66\u0273\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\39\39\3:\3:\3:\3:\3:\3:\5:\u0286\n:")
        buf.write("\3;\3;\3;\3;\3;\3;\5;\u028e\n;\3<\3<\3<\3<\5<\u0294\n")
        buf.write("<\3=\3=\3=\3=\3=\5=\u029b\n=\3>\3>\3>\3?\3?\3?\3?\5?\u02a4")
        buf.write("\n?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3")
        buf.write("G\3G\3G\3G\3G\3G\5G\u02bc\nG\3H\3H\3H\3H\3H\3H\3H\3H\3")
        buf.write("H\3H\3H\5H\u02c9\nH\3I\3I\3J\3J\3K\3K\3K\2\7@BDFHL\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094\2\n\4")
        buf.write("\2--\67\67\3\2\36#\3\2\31\32\3\2\33\35\4\2\32\32&&\3\2")
        buf.write("\678\4\2\13\16\67\67\4\2\65\65>>\2\u02dd\2\u0097\3\2\2")
        buf.write("\2\4\u00ac\3\2\2\2\6\u00ae\3\2\2\2\b\u00b7\3\2\2\2\n\u00bd")
        buf.write("\3\2\2\2\f\u00c8\3\2\2\2\16\u00d0\3\2\2\2\20\u00d2\3\2")
        buf.write("\2\2\22\u00d6\3\2\2\2\24\u00da\3\2\2\2\26\u00de\3\2\2")
        buf.write("\2\30\u00e6\3\2\2\2\32\u00ea\3\2\2\2\34\u00ec\3\2\2\2")
        buf.write("\36\u00f3\3\2\2\2 \u00f5\3\2\2\2\"\u00fd\3\2\2\2$\u00ff")
        buf.write("\3\2\2\2&\u0106\3\2\2\2(\u0108\3\2\2\2*\u011a\3\2\2\2")
        buf.write(",\u012d\3\2\2\2.\u0138\3\2\2\2\60\u013e\3\2\2\2\62\u0148")
        buf.write("\3\2\2\2\64\u014e\3\2\2\2\66\u0150\3\2\2\28\u015d\3\2")
        buf.write("\2\2:\u015f\3\2\2\2<\u016c\3\2\2\2>\u016e\3\2\2\2@\u0170")
        buf.write("\3\2\2\2B\u017b\3\2\2\2D\u0186\3\2\2\2F\u0192\3\2\2\2")
        buf.write("H\u019e\3\2\2\2J\u01ae\3\2\2\2L\u01b0\3\2\2\2N\u01c1\3")
        buf.write("\2\2\2P\u01db\3\2\2\2R\u01df\3\2\2\2T\u01f9\3\2\2\2V\u01fb")
        buf.write("\3\2\2\2X\u0207\3\2\2\2Z\u020c\3\2\2\2\\\u022f\3\2\2\2")
        buf.write("^\u0240\3\2\2\2`\u0244\3\2\2\2b\u025e\3\2\2\2d\u0260\3")
        buf.write("\2\2\2f\u0264\3\2\2\2h\u0266\3\2\2\2j\u0268\3\2\2\2l\u0277")
        buf.write("\3\2\2\2n\u0279\3\2\2\2p\u027b\3\2\2\2r\u0285\3\2\2\2")
        buf.write("t\u028d\3\2\2\2v\u0293\3\2\2\2x\u029a\3\2\2\2z\u029c\3")
        buf.write("\2\2\2|\u02a3\3\2\2\2~\u02a5\3\2\2\2\u0080\u02a7\3\2\2")
        buf.write("\2\u0082\u02a9\3\2\2\2\u0084\u02ab\3\2\2\2\u0086\u02ad")
        buf.write("\3\2\2\2\u0088\u02af\3\2\2\2\u008a\u02b1\3\2\2\2\u008c")
        buf.write("\u02bb\3\2\2\2\u008e\u02c8\3\2\2\2\u0090\u02ca\3\2\2\2")
        buf.write("\u0092\u02cc\3\2\2\2\u0094\u02ce\3\2\2\2\u0096\u0098\5")
        buf.write("\4\3\2\u0097\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u0097")
        buf.write("\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2\u009b")
        buf.write("\u009c\7\2\2\3\u009c\3\3\2\2\2\u009d\u009e\5\6\4\2\u009e")
        buf.write("\u009f\5\u0094K\2\u009f\u00ad\3\2\2\2\u00a0\u00a1\5*\26")
        buf.write("\2\u00a1\u00a2\5\u0094K\2\u00a2\u00ad\3\2\2\2\u00a3\u00a4")
        buf.write("\5\20\t\2\u00a4\u00a5\5\u0094K\2\u00a5\u00ad\3\2\2\2\u00a6")
        buf.write("\u00a7\5(\25\2\u00a7\u00a8\5\u0094K\2\u00a8\u00ad\3\2")
        buf.write("\2\2\u00a9\u00aa\5\62\32\2\u00aa\u00ab\5\u0094K\2\u00ab")
        buf.write("\u00ad\3\2\2\2\u00ac\u009d\3\2\2\2\u00ac\u00a0\3\2\2\2")
        buf.write("\u00ac\u00a3\3\2\2\2\u00ac\u00a6\3\2\2\2\u00ac\u00a9\3")
        buf.write("\2\2\2\u00ad\5\3\2\2\2\u00ae\u00af\7\23\2\2\u00af\u00b0")
        buf.write("\7\67\2\2\u00b0\u00b1\5\b\5\2\u00b1\7\3\2\2\2\u00b2\u00b3")
        buf.write("\5\n\6\2\u00b3\u00b4\5\16\b\2\u00b4\u00b8\3\2\2\2\u00b5")
        buf.write("\u00b8\5\n\6\2\u00b6\u00b8\5\16\b\2\u00b7\u00b2\3\2\2")
        buf.write("\2\u00b7\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\t\3\2")
        buf.write("\2\2\u00b9\u00be\5\u0092J\2\u00ba\u00bb\5\f\7\2\u00bb")
        buf.write("\u00bc\5\u0092J\2\u00bc\u00be\3\2\2\2\u00bd\u00b9\3\2")
        buf.write("\2\2\u00bd\u00ba\3\2\2\2\u00be\13\3\2\2\2\u00bf\u00c0")
        buf.write("\7\62\2\2\u00c0\u00c1\5\u0090I\2\u00c1\u00c2\7\63\2\2")
        buf.write("\u00c2\u00c3\5\f\7\2\u00c3\u00c9\3\2\2\2\u00c4\u00c5\7")
        buf.write("\62\2\2\u00c5\u00c6\5\u0090I\2\u00c6\u00c7\7\63\2\2\u00c7")
        buf.write("\u00c9\3\2\2\2\u00c8\u00bf\3\2\2\2\u00c8\u00c4\3\2\2\2")
        buf.write("\u00c9\r\3\2\2\2\u00ca\u00cb\7\27\2\2\u00cb\u00d1\5> ")
        buf.write("\2\u00cc\u00cd\7\27\2\2\u00cd\u00d1\5\22\n\2\u00ce\u00cf")
        buf.write("\7\27\2\2\u00cf\u00d1\5\34\17\2\u00d0\u00ca\3\2\2\2\u00d0")
        buf.write("\u00cc\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\17\3\2\2\2\u00d2")
        buf.write("\u00d3\7\22\2\2\u00d3\u00d4\7\67\2\2\u00d4\u00d5\5\16")
        buf.write("\b\2\u00d5\21\3\2\2\2\u00d6\u00d7\5\f\7\2\u00d7\u00d8")
        buf.write("\5\u0092J\2\u00d8\u00d9\5\24\13\2\u00d9\23\3\2\2\2\u00da")
        buf.write("\u00db\7\60\2\2\u00db\u00dc\5\26\f\2\u00dc\u00dd\7\61")
        buf.write("\2\2\u00dd\25\3\2\2\2\u00de\u00df\5\32\16\2\u00df\u00e0")
        buf.write("\5\30\r\2\u00e0\27\3\2\2\2\u00e1\u00e2\7\64\2\2\u00e2")
        buf.write("\u00e3\5\32\16\2\u00e3\u00e4\5\30\r\2\u00e4\u00e7\3\2")
        buf.write("\2\2\u00e5\u00e7\3\2\2\2\u00e6\u00e1\3\2\2\2\u00e6\u00e5")
        buf.write("\3\2\2\2\u00e7\31\3\2\2\2\u00e8\u00eb\5\24\13\2\u00e9")
        buf.write("\u00eb\5\u008cG\2\u00ea\u00e8\3\2\2\2\u00ea\u00e9\3\2")
        buf.write("\2\2\u00eb\33\3\2\2\2\u00ec\u00ed\7\67\2\2\u00ed\u00ee")
        buf.write("\7\60\2\2\u00ee\u00ef\5\36\20\2\u00ef\u00f0\7\61\2\2\u00f0")
        buf.write("\35\3\2\2\2\u00f1\u00f4\5 \21\2\u00f2\u00f4\3\2\2\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4\37\3\2\2\2\u00f5")
        buf.write("\u00f6\5$\23\2\u00f6\u00f7\5\"\22\2\u00f7!\3\2\2\2\u00f8")
        buf.write("\u00f9\7\64\2\2\u00f9\u00fa\5$\23\2\u00fa\u00fb\5\"\22")
        buf.write("\2\u00fb\u00fe\3\2\2\2\u00fc\u00fe\3\2\2\2\u00fd\u00f8")
        buf.write("\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe#\3\2\2\2\u00ff\u0100")
        buf.write("\7\67\2\2\u0100\u0101\7\66\2\2\u0101\u0102\5&\24\2\u0102")
        buf.write("%\3\2\2\2\u0103\u0107\5> \2\u0104\u0107\5\22\n\2\u0105")
        buf.write("\u0107\5\34\17\2\u0106\u0103\3\2\2\2\u0106\u0104\3\2\2")
        buf.write("\2\u0106\u0105\3\2\2\2\u0107\'\3\2\2\2\u0108\u0109\7\7")
        buf.write("\2\2\u0109\u010a\7.\2\2\u010a\u010b\7\67\2\2\u010b\u010c")
        buf.write("\7\67\2\2\u010c\u010d\7/\2\2\u010d\u010e\7\67\2\2\u010e")
        buf.write("\u010f\7.\2\2\u010f\u0110\5.\30\2\u0110\u0111\7/\2\2\u0111")
        buf.write("\u0112\5,\27\2\u0112\u0114\7\60\2\2\u0113\u0115\5P)\2")
        buf.write("\u0114\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0114\3")
        buf.write("\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0119")
        buf.write("\7\61\2\2\u0119)\3\2\2\2\u011a\u011b\7\7\2\2\u011b\u011c")
        buf.write("\7\67\2\2\u011c\u011d\7.\2\2\u011d\u011e\5.\30\2\u011e")
        buf.write("\u011f\7/\2\2\u011f\u0120\5,\27\2\u0120\u0122\7\60\2\2")
        buf.write("\u0121\u0123\5P)\2\u0122\u0121\3\2\2\2\u0123\u0124\3\2")
        buf.write("\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0126")
        buf.write("\3\2\2\2\u0126\u0127\7\61\2\2\u0127+\3\2\2\2\u0128\u012e")
        buf.write("\5\u0092J\2\u0129\u012a\5\f\7\2\u012a\u012b\5\u0092J\2")
        buf.write("\u012b\u012e\3\2\2\2\u012c\u012e\3\2\2\2\u012d\u0128\3")
        buf.write("\2\2\2\u012d\u0129\3\2\2\2\u012d\u012c\3\2\2\2\u012e-")
        buf.write("\3\2\2\2\u012f\u0130\5\60\31\2\u0130\u0131\5\n\6\2\u0131")
        buf.write("\u0132\7\64\2\2\u0132\u0133\5.\30\2\u0133\u0139\3\2\2")
        buf.write("\2\u0134\u0135\5\60\31\2\u0135\u0136\5\n\6\2\u0136\u0139")
        buf.write("\3\2\2\2\u0137\u0139\3\2\2\2\u0138\u012f\3\2\2\2\u0138")
        buf.write("\u0134\3\2\2\2\u0138\u0137\3\2\2\2\u0139/\3\2\2\2\u013a")
        buf.write("\u013f\7\67\2\2\u013b\u013c\7\67\2\2\u013c\u013d\7\64")
        buf.write("\2\2\u013d\u013f\5\60\31\2\u013e\u013a\3\2\2\2\u013e\u013b")
        buf.write("\3\2\2\2\u013f\61\3\2\2\2\u0140\u0141\7\b\2\2\u0141\u0142")
        buf.write("\7\67\2\2\u0142\u0143\7\t\2\2\u0143\u0149\5\66\34\2\u0144")
        buf.write("\u0145\7\b\2\2\u0145\u0146\7\67\2\2\u0146\u0147\7\n\2")
        buf.write("\2\u0147\u0149\5:\36\2\u0148\u0140\3\2\2\2\u0148\u0144")
        buf.write("\3\2\2\2\u0149\63\3\2\2\2\u014a\u014f\5\u0092J\2\u014b")
        buf.write("\u014c\5\f\7\2\u014c\u014d\5\u0092J\2\u014d\u014f\3\2")
        buf.write("\2\2\u014e\u014a\3\2\2\2\u014e\u014b\3\2\2\2\u014f\65")
        buf.write("\3\2\2\2\u0150\u0151\7\60\2\2\u0151\u0152\58\35\2\u0152")
        buf.write("\u0153\7\61\2\2\u0153\67\3\2\2\2\u0154\u0155\7\67\2\2")
        buf.write("\u0155\u0156\5\64\33\2\u0156\u0157\5\u0094K\2\u0157\u0158")
        buf.write("\58\35\2\u0158\u015e\3\2\2\2\u0159\u015a\7\67\2\2\u015a")
        buf.write("\u015b\5\64\33\2\u015b\u015c\5\u0094K\2\u015c\u015e\3")
        buf.write("\2\2\2\u015d\u0154\3\2\2\2\u015d\u0159\3\2\2\2\u015e9")
        buf.write("\3\2\2\2\u015f\u0160\7\60\2\2\u0160\u0161\5<\37\2\u0161")
        buf.write("\u0162\7\61\2\2\u0162;\3\2\2\2\u0163\u0164\7\67\2\2\u0164")
        buf.write("\u0165\7.\2\2\u0165\u0166\5.\30\2\u0166\u0167\7/\2\2\u0167")
        buf.write("\u0168\5,\27\2\u0168\u0169\5\u0094K\2\u0169\u016a\5<\37")
        buf.write("\2\u016a\u016d\3\2\2\2\u016b\u016d\3\2\2\2\u016c\u0163")
        buf.write("\3\2\2\2\u016c\u016b\3\2\2\2\u016d=\3\2\2\2\u016e\u016f")
        buf.write("\5@!\2\u016f?\3\2\2\2\u0170\u0171\b!\1\2\u0171\u0172\5")
        buf.write("B\"\2\u0172\u0178\3\2\2\2\u0173\u0174\f\4\2\2\u0174\u0175")
        buf.write("\7%\2\2\u0175\u0177\5B\"\2\u0176\u0173\3\2\2\2\u0177\u017a")
        buf.write("\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179")
        buf.write("A\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u017c\b\"\1\2\u017c")
        buf.write("\u017d\5D#\2\u017d\u0183\3\2\2\2\u017e\u017f\f\4\2\2\u017f")
        buf.write("\u0180\7$\2\2\u0180\u0182\5D#\2\u0181\u017e\3\2\2\2\u0182")
        buf.write("\u0185\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184C\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u0187\b#\1\2")
        buf.write("\u0187\u0188\5F$\2\u0188\u018f\3\2\2\2\u0189\u018a\f\4")
        buf.write("\2\2\u018a\u018b\5\u0084C\2\u018b\u018c\5F$\2\u018c\u018e")
        buf.write("\3\2\2\2\u018d\u0189\3\2\2\2\u018e\u0191\3\2\2\2\u018f")
        buf.write("\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190E\3\2\2\2\u0191")
        buf.write("\u018f\3\2\2\2\u0192\u0193\b$\1\2\u0193\u0194\5H%\2\u0194")
        buf.write("\u019b\3\2\2\2\u0195\u0196\f\4\2\2\u0196\u0197\5\u0086")
        buf.write("D\2\u0197\u0198\5H%\2\u0198\u019a\3\2\2\2\u0199\u0195")
        buf.write("\3\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2\u019b")
        buf.write("\u019c\3\2\2\2\u019cG\3\2\2\2\u019d\u019b\3\2\2\2\u019e")
        buf.write("\u019f\b%\1\2\u019f\u01a0\5J&\2\u01a0\u01a7\3\2\2\2\u01a1")
        buf.write("\u01a2\f\4\2\2\u01a2\u01a3\5\u0088E\2\u01a3\u01a4\5J&")
        buf.write("\2\u01a4\u01a6\3\2\2\2\u01a5\u01a1\3\2\2\2\u01a6\u01a9")
        buf.write("\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8")
        buf.write("I\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01ab\5\u008aF\2\u01ab")
        buf.write("\u01ac\5J&\2\u01ac\u01af\3\2\2\2\u01ad\u01af\5L\'\2\u01ae")
        buf.write("\u01aa\3\2\2\2\u01ae\u01ad\3\2\2\2\u01afK\3\2\2\2\u01b0")
        buf.write("\u01b1\5\u008eH\2\u01b1\u01b2\5N(\2\u01b2M\3\2\2\2\u01b3")
        buf.write("\u01b4\7,\2\2\u01b4\u01b5\7\67\2\2\u01b5\u01c2\5N(\2\u01b6")
        buf.write("\u01b7\7\62\2\2\u01b7\u01b8\5> \2\u01b8\u01b9\7\63\2\2")
        buf.write("\u01b9\u01ba\5N(\2\u01ba\u01c2\3\2\2\2\u01bb\u01bc\7.")
        buf.write("\2\2\u01bc\u01bd\5v<\2\u01bd\u01be\7/\2\2\u01be\u01bf")
        buf.write("\5N(\2\u01bf\u01c2\3\2\2\2\u01c0\u01c2\3\2\2\2\u01c1\u01b3")
        buf.write("\3\2\2\2\u01c1\u01b6\3\2\2\2\u01c1\u01bb\3\2\2\2\u01c1")
        buf.write("\u01c0\3\2\2\2\u01c2O\3\2\2\2\u01c3\u01c4\5R*\2\u01c4")
        buf.write("\u01c5\5\u0094K\2\u01c5\u01dc\3\2\2\2\u01c6\u01c7\5T+")
        buf.write("\2\u01c7\u01c8\5\u0094K\2\u01c8\u01dc\3\2\2\2\u01c9\u01ca")
        buf.write("\5\\/\2\u01ca\u01cb\5\u0094K\2\u01cb\u01dc\3\2\2\2\u01cc")
        buf.write("\u01cd\5`\61\2\u01cd\u01ce\5\u0094K\2\u01ce\u01dc\3\2")
        buf.write("\2\2\u01cf\u01d0\5l\67\2\u01d0\u01d1\5\u0094K\2\u01d1")
        buf.write("\u01dc\3\2\2\2\u01d2\u01d3\5n8\2\u01d3\u01d4\5\u0094K")
        buf.write("\2\u01d4\u01dc\3\2\2\2\u01d5\u01d6\5p9\2\u01d6\u01d7\5")
        buf.write("\u0094K\2\u01d7\u01dc\3\2\2\2\u01d8\u01d9\5z>\2\u01d9")
        buf.write("\u01da\5\u0094K\2\u01da\u01dc\3\2\2\2\u01db\u01c3\3\2")
        buf.write("\2\2\u01db\u01c6\3\2\2\2\u01db\u01c9\3\2\2\2\u01db\u01cc")
        buf.write("\3\2\2\2\u01db\u01cf\3\2\2\2\u01db\u01d2\3\2\2\2\u01db")
        buf.write("\u01d5\3\2\2\2\u01db\u01d8\3\2\2\2\u01dcQ\3\2\2\2\u01dd")
        buf.write("\u01e0\5\6\4\2\u01de\u01e0\5\20\t\2\u01df\u01dd\3\2\2")
        buf.write("\2\u01df\u01de\3\2\2\2\u01e0S\3\2\2\2\u01e1\u01e2\5V,")
        buf.write("\2\u01e2\u01e3\7\30\2\2\u01e3\u01e4\5Z.\2\u01e4\u01fa")
        buf.write("\3\2\2\2\u01e5\u01e6\5V,\2\u01e6\u01e7\7\'\2\2\u01e7\u01e8")
        buf.write("\5Z.\2\u01e8\u01fa\3\2\2\2\u01e9\u01ea\5V,\2\u01ea\u01eb")
        buf.write("\7(\2\2\u01eb\u01ec\5Z.\2\u01ec\u01fa\3\2\2\2\u01ed\u01ee")
        buf.write("\5V,\2\u01ee\u01ef\7)\2\2\u01ef\u01f0\5Z.\2\u01f0\u01fa")
        buf.write("\3\2\2\2\u01f1\u01f2\5V,\2\u01f2\u01f3\7*\2\2\u01f3\u01f4")
        buf.write("\5Z.\2\u01f4\u01fa\3\2\2\2\u01f5\u01f6\5V,\2\u01f6\u01f7")
        buf.write("\7+\2\2\u01f7\u01f8\5Z.\2\u01f8\u01fa\3\2\2\2\u01f9\u01e1")
        buf.write("\3\2\2\2\u01f9\u01e5\3\2\2\2\u01f9\u01e9\3\2\2\2\u01f9")
        buf.write("\u01ed\3\2\2\2\u01f9\u01f1\3\2\2\2\u01f9\u01f5\3\2\2\2")
        buf.write("\u01faU\3\2\2\2\u01fb\u01fc\7\67\2\2\u01fc\u01fd\5X-\2")
        buf.write("\u01fdW\3\2\2\2\u01fe\u01ff\7,\2\2\u01ff\u0200\7\67\2")
        buf.write("\2\u0200\u0208\5X-\2\u0201\u0202\7\62\2\2\u0202\u0203")
        buf.write("\5> \2\u0203\u0204\7\63\2\2\u0204\u0205\5X-\2\u0205\u0208")
        buf.write("\3\2\2\2\u0206\u0208\3\2\2\2\u0207\u01fe\3\2\2\2\u0207")
        buf.write("\u0201\3\2\2\2\u0207\u0206\3\2\2\2\u0208Y\3\2\2\2\u0209")
        buf.write("\u020d\5> \2\u020a\u020d\5\22\n\2\u020b\u020d\5\34\17")
        buf.write("\2\u020c\u0209\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020b")
        buf.write("\3\2\2\2\u020d[\3\2\2\2\u020e\u020f\7\3\2\2\u020f\u0210")
        buf.write("\7.\2\2\u0210\u0211\5> \2\u0211\u0212\7/\2\2\u0212\u0214")
        buf.write("\7\60\2\2\u0213\u0215\5P)\2\u0214\u0213\3\2\2\2\u0215")
        buf.write("\u0216\3\2\2\2\u0216\u0214\3\2\2\2\u0216\u0217\3\2\2\2")
        buf.write("\u0217\u0218\3\2\2\2\u0218\u0219\7\61\2\2\u0219\u0230")
        buf.write("\3\2\2\2\u021a\u021b\7\3\2\2\u021b\u021c\7.\2\2\u021c")
        buf.write("\u021d\5> \2\u021d\u021e\7/\2\2\u021e\u0220\7\60\2\2\u021f")
        buf.write("\u0221\5P)\2\u0220\u021f\3\2\2\2\u0221\u0222\3\2\2\2\u0222")
        buf.write("\u0220\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0224\3\2\2\2")
        buf.write("\u0224\u0225\7\61\2\2\u0225\u0226\5^\60\2\u0226\u0227")
        buf.write("\7\4\2\2\u0227\u0229\7\60\2\2\u0228\u022a\5P)\2\u0229")
        buf.write("\u0228\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u0229\3\2\2\2")
        buf.write("\u022b\u022c\3\2\2\2\u022c\u022d\3\2\2\2\u022d\u022e\7")
        buf.write("\61\2\2\u022e\u0230\3\2\2\2\u022f\u020e\3\2\2\2\u022f")
        buf.write("\u021a\3\2\2\2\u0230]\3\2\2\2\u0231\u0232\7\4\2\2\u0232")
        buf.write("\u0233\7\3\2\2\u0233\u0234\7.\2\2\u0234\u0235\5> \2\u0235")
        buf.write("\u0236\7/\2\2\u0236\u0238\7\60\2\2\u0237\u0239\5P)\2\u0238")
        buf.write("\u0237\3\2\2\2\u0239\u023a\3\2\2\2\u023a\u0238\3\2\2\2")
        buf.write("\u023a\u023b\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u023d\7")
        buf.write("\61\2\2\u023d\u023e\5^\60\2\u023e\u0241\3\2\2\2\u023f")
        buf.write("\u0241\3\2\2\2\u0240\u0231\3\2\2\2\u0240\u023f\3\2\2\2")
        buf.write("\u0241_\3\2\2\2\u0242\u0245\5b\62\2\u0243\u0245\5j\66")
        buf.write("\2\u0244\u0242\3\2\2\2\u0244\u0243\3\2\2\2\u0245a\3\2")
        buf.write("\2\2\u0246\u0247\7\5\2\2\u0247\u0248\5d\63\2\u0248\u024a")
        buf.write("\7\60\2\2\u0249\u024b\5P)\2\u024a\u0249\3\2\2\2\u024b")
        buf.write("\u024c\3\2\2\2\u024c\u024a\3\2\2\2\u024c\u024d\3\2\2\2")
        buf.write("\u024d\u024e\3\2\2\2\u024e\u024f\7\61\2\2\u024f\u025f")
        buf.write("\3\2\2\2\u0250\u0251\7\5\2\2\u0251\u0252\5f\64\2\u0252")
        buf.write("\u0253\7\65\2\2\u0253\u0254\5d\63\2\u0254\u0255\7\65\2")
        buf.write("\2\u0255\u0256\5h\65\2\u0256\u0258\7\60\2\2\u0257\u0259")
        buf.write("\5P)\2\u0258\u0257\3\2\2\2\u0259\u025a\3\2\2\2\u025a\u0258")
        buf.write("\3\2\2\2\u025a\u025b\3\2\2\2\u025b\u025c\3\2\2\2\u025c")
        buf.write("\u025d\7\61\2\2\u025d\u025f\3\2\2\2\u025e\u0246\3\2\2")
        buf.write("\2\u025e\u0250\3\2\2\2\u025fc\3\2\2\2\u0260\u0261\5> ")
        buf.write("\2\u0261e\3\2\2\2\u0262\u0265\5T+\2\u0263\u0265\5\6\4")
        buf.write("\2\u0264\u0262\3\2\2\2\u0264\u0263\3\2\2\2\u0265g\3\2")
        buf.write("\2\2\u0266\u0267\5T+\2\u0267i\3\2\2\2\u0268\u0269\7\5")
        buf.write("\2\2\u0269\u026a\5~@\2\u026a\u026b\7\64\2\2\u026b\u026c")
        buf.write("\5\u0080A\2\u026c\u026d\7\30\2\2\u026d\u026e\7\26\2\2")
        buf.write("\u026e\u026f\5\u0082B\2\u026f\u0271\7\60\2\2\u0270\u0272")
        buf.write("\5P)\2\u0271\u0270\3\2\2\2\u0272\u0273\3\2\2\2\u0273\u0271")
        buf.write("\3\2\2\2\u0273\u0274\3\2\2\2\u0274\u0275\3\2\2\2\u0275")
        buf.write("\u0276\7\61\2\2\u0276k\3\2\2\2\u0277\u0278\7\25\2\2\u0278")
        buf.write("m\3\2\2\2\u0279\u027a\7\24\2\2\u027ao\3\2\2\2\u027b\u027c")
        buf.write("\7\67\2\2\u027c\u027d\5r:\2\u027d\u027e\5t;\2\u027eq\3")
        buf.write("\2\2\2\u027f\u0280\7\62\2\2\u0280\u0281\5> \2\u0281\u0282")
        buf.write("\7\63\2\2\u0282\u0283\5r:\2\u0283\u0286\3\2\2\2\u0284")
        buf.write("\u0286\3\2\2\2\u0285\u027f\3\2\2\2\u0285\u0284\3\2\2\2")
        buf.write("\u0286s\3\2\2\2\u0287\u0288\7,\2\2\u0288\u028e\5p9\2\u0289")
        buf.write("\u028a\7.\2\2\u028a\u028b\5v<\2\u028b\u028c\7/\2\2\u028c")
        buf.write("\u028e\3\2\2\2\u028d\u0287\3\2\2\2\u028d\u0289\3\2\2\2")
        buf.write("\u028eu\3\2\2\2\u028f\u0290\5> \2\u0290\u0291\5x=\2\u0291")
        buf.write("\u0294\3\2\2\2\u0292\u0294\3\2\2\2\u0293\u028f\3\2\2\2")
        buf.write("\u0293\u0292\3\2\2\2\u0294w\3\2\2\2\u0295\u0296\7\64\2")
        buf.write("\2\u0296\u0297\5> \2\u0297\u0298\5x=\2\u0298\u029b\3\2")
        buf.write("\2\2\u0299\u029b\3\2\2\2\u029a\u0295\3\2\2\2\u029a\u0299")
        buf.write("\3\2\2\2\u029by\3\2\2\2\u029c\u029d\7\6\2\2\u029d\u029e")
        buf.write("\5|?\2\u029e{\3\2\2\2\u029f\u02a4\5> \2\u02a0\u02a4\5")
        buf.write("\22\n\2\u02a1\u02a4\5\34\17\2\u02a2\u02a4\3\2\2\2\u02a3")
        buf.write("\u029f\3\2\2\2\u02a3\u02a0\3\2\2\2\u02a3\u02a1\3\2\2\2")
        buf.write("\u02a3\u02a2\3\2\2\2\u02a4}\3\2\2\2\u02a5\u02a6\t\2\2")
        buf.write("\2\u02a6\177\3\2\2\2\u02a7\u02a8\7\67\2\2\u02a8\u0081")
        buf.write("\3\2\2\2\u02a9\u02aa\5> \2\u02aa\u0083\3\2\2\2\u02ab\u02ac")
        buf.write("\t\3\2\2\u02ac\u0085\3\2\2\2\u02ad\u02ae\t\4\2\2\u02ae")
        buf.write("\u0087\3\2\2\2\u02af\u02b0\t\5\2\2\u02b0\u0089\3\2\2\2")
        buf.write("\u02b1\u02b2\t\6\2\2\u02b2\u008b\3\2\2\2\u02b3\u02bc\7")
        buf.write("8\2\2\u02b4\u02bc\79\2\2\u02b5\u02bc\7:\2\2\u02b6\u02bc")
        buf.write("\7\17\2\2\u02b7\u02bc\7\20\2\2\u02b8\u02bc\7\21\2\2\u02b9")
        buf.write("\u02bc\5\34\17\2\u02ba\u02bc\7\67\2\2\u02bb\u02b3\3\2")
        buf.write("\2\2\u02bb\u02b4\3\2\2\2\u02bb\u02b5\3\2\2\2\u02bb\u02b6")
        buf.write("\3\2\2\2\u02bb\u02b7\3\2\2\2\u02bb\u02b8\3\2\2\2\u02bb")
        buf.write("\u02b9\3\2\2\2\u02bb\u02ba\3\2\2\2\u02bc\u008d\3\2\2\2")
        buf.write("\u02bd\u02c9\7\67\2\2\u02be\u02c9\78\2\2\u02bf\u02c9\7")
        buf.write("9\2\2\u02c0\u02c9\7:\2\2\u02c1\u02c9\7\17\2\2\u02c2\u02c9")
        buf.write("\7\20\2\2\u02c3\u02c9\7\21\2\2\u02c4\u02c5\7.\2\2\u02c5")
        buf.write("\u02c6\5> \2\u02c6\u02c7\7/\2\2\u02c7\u02c9\3\2\2\2\u02c8")
        buf.write("\u02bd\3\2\2\2\u02c8\u02be\3\2\2\2\u02c8\u02bf\3\2\2\2")
        buf.write("\u02c8\u02c0\3\2\2\2\u02c8\u02c1\3\2\2\2\u02c8\u02c2\3")
        buf.write("\2\2\2\u02c8\u02c3\3\2\2\2\u02c8\u02c4\3\2\2\2\u02c9\u008f")
        buf.write("\3\2\2\2\u02ca\u02cb\t\7\2\2\u02cb\u0091\3\2\2\2\u02cc")
        buf.write("\u02cd\t\b\2\2\u02cd\u0093\3\2\2\2\u02ce\u02cf\t\t\2\2")
        buf.write("\u02cf\u0095\3\2\2\2\65\u0099\u00ac\u00b7\u00bd\u00c8")
        buf.write("\u00d0\u00e6\u00ea\u00f3\u00fd\u0106\u0116\u0124\u012d")
        buf.write("\u0138\u013e\u0148\u014e\u015d\u016c\u0178\u0183\u018f")
        buf.write("\u019b\u01a7\u01ae\u01c1\u01db\u01df\u01f9\u0207\u020c")
        buf.write("\u0216\u0222\u022b\u022f\u023a\u0240\u0244\u024c\u025a")
        buf.write("\u025e\u0264\u0273\u0285\u028d\u0293\u029a\u02a3\u02bb")
        buf.write("\u02c8")
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
    RULE_primaryExprTail = 38
    RULE_statement = 39
    RULE_declarationStatement = 40
    RULE_assignStatement = 41
    RULE_assignStateLHS = 42
    RULE_assignStateLHSTail = 43
    RULE_assignStateRHS = 44
    RULE_ifStatement = 45
    RULE_elseIfStatement = 46
    RULE_forStatement = 47
    RULE_basicForStatement = 48
    RULE_forCondition = 49
    RULE_forInitilization = 50
    RULE_forUpdate = 51
    RULE_forRangeStatement = 52
    RULE_breakStatement = 53
    RULE_continueStatement = 54
    RULE_callStatement = 55
    RULE_callStatementArrayTail = 56
    RULE_callStatementTail = 57
    RULE_callArguments = 58
    RULE_callArgumentsTail = 59
    RULE_returnStatement = 60
    RULE_returnStatementTail = 61
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

    ruleNames =  [ "program", "declaration", "varDecl", "varDetail", "varDeclType", 
                   "arrayType", "varDeclExpr", "constDecl", "arrayLit", 
                   "arrayBlock", "arrayLitList", "arrayLitListTail", "arrayLitContent", 
                   "structLit", "optionalStructFields", "structFieldList", 
                   "structFieldListTail", "structFieldAssign", "structBlock", 
                   "methodDecl", "funcDecl", "funcType", "funcParam", "funcListIdentifiers", 
                   "typeDecl", "structType", "structDeclBlock", "structDeclField", 
                   "interfaceDeclBlock", "interfaceDeclField", "expr", "logicOrExpr", 
                   "logicAndExpr", "equalityExpr", "additiveExpr", "multiplicativeExpr", 
                   "unaryExpr", "primaryExpr", "primaryExprTail", "statement", 
                   "declarationStatement", "assignStatement", "assignStateLHS", 
                   "assignStateLHSTail", "assignStateRHS", "ifStatement", 
                   "elseIfStatement", "forStatement", "basicForStatement", 
                   "forCondition", "forInitilization", "forUpdate", "forRangeStatement", 
                   "breakStatement", "continueStatement", "callStatement", 
                   "callStatementArrayTail", "callStatementTail", "callArguments", 
                   "callArgumentsTail", "returnStatement", "returnStatementTail", 
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
            self.state = 149 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 148
                self.declaration()
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
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(MiniGoParser.LBRACKET)
                self.state = 190
                self.intLitOrConstant()
                self.state = 191
                self.match(MiniGoParser.RBRACKET)
                self.state = 192
                self.arrayType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.match(MiniGoParser.LBRACKET)
                self.state = 195
                self.intLitOrConstant()
                self.state = 196
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
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(MiniGoParser.DECLARE)
                self.state = 201
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.match(MiniGoParser.DECLARE)
                self.state = 203
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.match(MiniGoParser.DECLARE)
                self.state = 205
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
            self.state = 208
            self.match(MiniGoParser.CONST)
            self.state = 209
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 210
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
            self.state = 212
            self.arrayType()
            self.state = 213
            self.baseType()
            self.state = 214
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
            self.state = 216
            self.match(MiniGoParser.LBRACE)
            self.state = 217
            self.arrayLitList()
            self.state = 218
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
            self.state = 220
            self.arrayLitContent()
            self.state = 221
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
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.match(MiniGoParser.COMMA)
                self.state = 224
                self.arrayLitContent()
                self.state = 225
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
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.arrayBlock()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
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
            self.state = 234
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 235
            self.match(MiniGoParser.LBRACE)
            self.state = 236
            self.optionalStructFields()
            self.state = 237
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
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
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
            self.state = 243
            self.structFieldAssign()
            self.state = 244
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
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(MiniGoParser.COMMA)
                self.state = 247
                self.structFieldAssign()
                self.state = 248
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
            self.state = 253
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 254
            self.match(MiniGoParser.COLON)
            self.state = 255
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
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 259
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
            self.state = 262
            self.match(MiniGoParser.FUNC)
            self.state = 263
            self.match(MiniGoParser.LPAREN)
            self.state = 264
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 265
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 266
            self.match(MiniGoParser.RPAREN)
            self.state = 267
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 268
            self.match(MiniGoParser.LPAREN)
            self.state = 269
            self.funcParam()
            self.state = 270
            self.match(MiniGoParser.RPAREN)
            self.state = 271
            self.funcType()
            self.state = 272
            self.match(MiniGoParser.LBRACE)
            self.state = 274 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 273
                self.statement()
                self.state = 276 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                    break

            self.state = 278
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
            self.state = 280
            self.match(MiniGoParser.FUNC)
            self.state = 281
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 282
            self.match(MiniGoParser.LPAREN)
            self.state = 283
            self.funcParam()
            self.state = 284
            self.match(MiniGoParser.RPAREN)
            self.state = 285
            self.funcType()
            self.state = 286
            self.match(MiniGoParser.LBRACE)
            self.state = 288 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 287
                self.statement()
                self.state = 290 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                    break

            self.state = 292
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
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.baseType()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.arrayType()
                self.state = 296
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
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.funcListIdentifiers()
                self.state = 302
                self.varDeclType()
                self.state = 303
                self.match(MiniGoParser.COMMA)
                self.state = 304
                self.funcParam()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.funcListIdentifiers()
                self.state = 307
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
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 314
                self.match(MiniGoParser.COMMA)
                self.state = 315
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
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(MiniGoParser.TYPE)
                self.state = 319
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 320
                self.match(MiniGoParser.STRUCT)
                self.state = 321
                self.structDeclBlock()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.match(MiniGoParser.TYPE)
                self.state = 323
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 324
                self.match(MiniGoParser.INTERFACE)
                self.state = 325
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
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.baseType()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.arrayType()
                self.state = 330
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
            self.state = 334
            self.match(MiniGoParser.LBRACE)
            self.state = 335
            self.structDeclField()
            self.state = 336
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
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 339
                self.structType()
                self.state = 340
                self.endOfStatement()
                self.state = 341
                self.structDeclField()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 344
                self.structType()
                self.state = 345
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
            self.state = 349
            self.match(MiniGoParser.LBRACE)
            self.state = 350
            self.interfaceDeclField()
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
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
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
                self.state = 359
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
            self.state = 364
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
            self.state = 367
            self.logicAndExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogicOrExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicOrExpr)
                    self.state = 369
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 370
                    self.match(MiniGoParser.OR)
                    self.state = 371
                    self.logicAndExpr(0) 
                self.state = 376
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
            self.state = 378
            self.equalityExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 385
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogicAndExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicAndExpr)
                    self.state = 380
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 381
                    self.match(MiniGoParser.AND)
                    self.state = 382
                    self.equalityExpr(0) 
                self.state = 387
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
            self.state = 389
            self.additiveExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 397
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.EqualityExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpr)
                    self.state = 391
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 392
                    self.relationOp()
                    self.state = 393
                    self.additiveExpr(0) 
                self.state = 399
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
            self.state = 401
            self.multiplicativeExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 409
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.AdditiveExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpr)
                    self.state = 403
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 404
                    self.addOp()
                    self.state = 405
                    self.multiplicativeExpr(0) 
                self.state = 411
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
            self.state = 413
            self.unaryExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 421
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.MultiplicativeExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpr)
                    self.state = 415
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 416
                    self.mulOp()
                    self.state = 417
                    self.unaryExpr() 
                self.state = 423
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
            self.state = 428
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.unaryOp()
                self.state = 425
                self.unaryExpr()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.LPAREN, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
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


        def primaryExprTail(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExprTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_primaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpr(self):

        localctx = MiniGoParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_primaryExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.term()
            self.state = 431
            self.primaryExprTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExprTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def primaryExprTail(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExprTailContext,0)


        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def callArguments(self):
            return self.getTypedRuleContext(MiniGoParser.CallArgumentsContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primaryExprTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExprTail" ):
                return visitor.visitPrimaryExprTail(self)
            else:
                return visitor.visitChildren(self)




    def primaryExprTail(self):

        localctx = MiniGoParser.PrimaryExprTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_primaryExprTail)
        try:
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.match(MiniGoParser.DOT)
                self.state = 434
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 435
                self.primaryExprTail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.match(MiniGoParser.LBRACKET)
                self.state = 437
                self.expr()
                self.state = 438
                self.match(MiniGoParser.RBRACKET)
                self.state = 439
                self.primaryExprTail()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 441
                self.match(MiniGoParser.LPAREN)
                self.state = 442
                self.callArguments()
                self.state = 443
                self.match(MiniGoParser.RPAREN)
                self.state = 444
                self.primaryExprTail()
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
        self.enterRule(localctx, 78, self.RULE_statement)
        try:
            self.state = 473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.declarationStatement()
                self.state = 450
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.assignStatement()
                self.state = 453
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 455
                self.ifStatement()
                self.state = 456
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 458
                self.forStatement()
                self.state = 459
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 461
                self.breakStatement()
                self.state = 462
                self.endOfStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 464
                self.continueStatement()
                self.state = 465
                self.endOfStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 467
                self.callStatement()
                self.state = 468
                self.endOfStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 470
                self.returnStatement()
                self.state = 471
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
        self.enterRule(localctx, 80, self.RULE_declarationStatement)
        try:
            self.state = 477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                self.varDecl()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 476
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
        self.enterRule(localctx, 82, self.RULE_assignStatement)
        try:
            self.state = 503
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 479
                self.assignStateLHS()
                self.state = 480
                self.match(MiniGoParser.ASSIGN)
                self.state = 481
                self.assignStateRHS()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.assignStateLHS()
                self.state = 484
                self.match(MiniGoParser.PLUS_ASSIGN)
                self.state = 485
                self.assignStateRHS()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 487
                self.assignStateLHS()
                self.state = 488
                self.match(MiniGoParser.MINUS_ASSIGN)
                self.state = 489
                self.assignStateRHS()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 491
                self.assignStateLHS()
                self.state = 492
                self.match(MiniGoParser.MUL_ASSIGN)
                self.state = 493
                self.assignStateRHS()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 495
                self.assignStateLHS()
                self.state = 496
                self.match(MiniGoParser.DIV_ASSIGN)
                self.state = 497
                self.assignStateRHS()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 499
                self.assignStateLHS()
                self.state = 500
                self.match(MiniGoParser.MOD_ASSIGN)
                self.state = 501
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
        self.enterRule(localctx, 84, self.RULE_assignStateLHS)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 506
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
        self.enterRule(localctx, 86, self.RULE_assignStateLHSTail)
        try:
            self.state = 517
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 508
                self.match(MiniGoParser.DOT)
                self.state = 509
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 510
                self.assignStateLHSTail()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 511
                self.match(MiniGoParser.LBRACKET)
                self.state = 512
                self.expr()
                self.state = 513
                self.match(MiniGoParser.RBRACKET)
                self.state = 514
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
        self.enterRule(localctx, 88, self.RULE_assignStateRHS)
        try:
            self.state = 522
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 519
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 520
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 521
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
        self.enterRule(localctx, 90, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.state = 557
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.match(MiniGoParser.IF)
                self.state = 525
                self.match(MiniGoParser.LPAREN)
                self.state = 526
                self.expr()
                self.state = 527
                self.match(MiniGoParser.RPAREN)
                self.state = 528
                self.match(MiniGoParser.LBRACE)
                self.state = 530 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 529
                    self.statement()
                    self.state = 532 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                        break

                self.state = 534
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 536
                self.match(MiniGoParser.IF)
                self.state = 537
                self.match(MiniGoParser.LPAREN)
                self.state = 538
                self.expr()
                self.state = 539
                self.match(MiniGoParser.RPAREN)
                self.state = 540
                self.match(MiniGoParser.LBRACE)
                self.state = 542 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 541
                    self.statement()
                    self.state = 544 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                        break

                self.state = 546
                self.match(MiniGoParser.RBRACE)
                self.state = 547
                self.elseIfStatement()
                self.state = 548
                self.match(MiniGoParser.ELSE)
                self.state = 549
                self.match(MiniGoParser.LBRACE)
                self.state = 551 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 550
                    self.statement()
                    self.state = 553 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                        break

                self.state = 555
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
        self.enterRule(localctx, 92, self.RULE_elseIfStatement)
        self._la = 0 # Token type
        try:
            self.state = 574
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 559
                self.match(MiniGoParser.ELSE)
                self.state = 560
                self.match(MiniGoParser.IF)
                self.state = 561
                self.match(MiniGoParser.LPAREN)
                self.state = 562
                self.expr()
                self.state = 563
                self.match(MiniGoParser.RPAREN)
                self.state = 564
                self.match(MiniGoParser.LBRACE)
                self.state = 566 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 565
                    self.statement()
                    self.state = 568 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                        break

                self.state = 570
                self.match(MiniGoParser.RBRACE)
                self.state = 571
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
        self.enterRule(localctx, 94, self.RULE_forStatement)
        try:
            self.state = 578
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.basicForStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 577
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
            self.state = 604
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 580
                self.match(MiniGoParser.FOR)
                self.state = 581
                self.forCondition()
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
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                        break

                self.state = 588
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 590
                self.match(MiniGoParser.FOR)
                self.state = 591
                self.forInitilization()
                self.state = 592
                self.match(MiniGoParser.SEMI)
                self.state = 593
                self.forCondition()
                self.state = 594
                self.match(MiniGoParser.SEMI)
                self.state = 595
                self.forUpdate()
                self.state = 596
                self.match(MiniGoParser.LBRACE)
                self.state = 598 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 597
                    self.statement()
                    self.state = 600 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                        break

                self.state = 602
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
            self.state = 606
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
        self.enterRule(localctx, 100, self.RULE_forInitilization)
        try:
            self.state = 610
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 608
                self.assignStatement()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 609
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
        self.enterRule(localctx, 102, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
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
        self.enterRule(localctx, 104, self.RULE_forRangeStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            self.match(MiniGoParser.FOR)
            self.state = 615
            self.index()
            self.state = 616
            self.match(MiniGoParser.COMMA)
            self.state = 617
            self.value()
            self.state = 618
            self.match(MiniGoParser.ASSIGN)
            self.state = 619
            self.match(MiniGoParser.RANGE)
            self.state = 620
            self.forArray()
            self.state = 621
            self.match(MiniGoParser.LBRACE)
            self.state = 623 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 622
                self.statement()
                self.state = 625 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                    break

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
        self.enterRule(localctx, 106, self.RULE_breakStatement)
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
        self.enterRule(localctx, 108, self.RULE_continueStatement)
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


        def callStatementTail(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementTailContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 634
            self.callStatementArrayTail()
            self.state = 635
            self.callStatementTail()
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
        self.enterRule(localctx, 112, self.RULE_callStatementArrayTail)
        try:
            self.state = 643
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 637
                self.match(MiniGoParser.LBRACKET)
                self.state = 638
                self.expr()
                self.state = 639
                self.match(MiniGoParser.RBRACKET)
                self.state = 640
                self.callStatementArrayTail()
                pass
            elif token in [MiniGoParser.DOT, MiniGoParser.LPAREN]:
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


    class CallStatementTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def callStatement(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def callArguments(self):
            return self.getTypedRuleContext(MiniGoParser.CallArgumentsContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_callStatementTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatementTail" ):
                return visitor.visitCallStatementTail(self)
            else:
                return visitor.visitChildren(self)




    def callStatementTail(self):

        localctx = MiniGoParser.CallStatementTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_callStatementTail)
        try:
            self.state = 651
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 645
                self.match(MiniGoParser.DOT)
                self.state = 646
                self.callStatement()
                pass
            elif token in [MiniGoParser.LPAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 647
                self.match(MiniGoParser.LPAREN)
                self.state = 648
                self.callArguments()
                self.state = 649
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


    class CallArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def callArgumentsTail(self):
            return self.getTypedRuleContext(MiniGoParser.CallArgumentsTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callArguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallArguments" ):
                return visitor.visitCallArguments(self)
            else:
                return visitor.visitChildren(self)




    def callArguments(self):

        localctx = MiniGoParser.CallArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_callArguments)
        try:
            self.state = 657
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 653
                self.expr()
                self.state = 654
                self.callArgumentsTail()
                pass
            elif token in [MiniGoParser.RPAREN]:
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


    class CallArgumentsTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def callArgumentsTail(self):
            return self.getTypedRuleContext(MiniGoParser.CallArgumentsTailContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callArgumentsTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallArgumentsTail" ):
                return visitor.visitCallArgumentsTail(self)
            else:
                return visitor.visitChildren(self)




    def callArgumentsTail(self):

        localctx = MiniGoParser.CallArgumentsTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_callArgumentsTail)
        try:
            self.state = 664
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 659
                self.match(MiniGoParser.COMMA)
                self.state = 660
                self.expr()
                self.state = 661
                self.callArgumentsTail()
                pass
            elif token in [MiniGoParser.RPAREN]:
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
        self.enterRule(localctx, 120, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 666
            self.match(MiniGoParser.RETURN)
            self.state = 667
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
        self.enterRule(localctx, 122, self.RULE_returnStatementTail)
        try:
            self.state = 673
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 669
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 670
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 671
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
        self.enterRule(localctx, 124, self.RULE_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 675
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
            self.state = 677
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
            self.state = 679
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
            self.state = 681
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
            self.state = 683
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
            self.state = 685
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
            self.state = 687
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
        self.enterRule(localctx, 138, self.RULE_noArrayLit)
        try:
            self.state = 697
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 689
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 690
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 691
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 692
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 693
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 694
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 695
                self.structLit()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 696
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
        self.enterRule(localctx, 140, self.RULE_term)
        try:
            self.state = 710
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 699
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 700
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 701
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 702
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 703
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 704
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 7)
                self.state = 705
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.LPAREN]:
                self.enterOuterAlt(localctx, 8)
                self.state = 706
                self.match(MiniGoParser.LPAREN)
                self.state = 707
                self.expr()
                self.state = 708
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
        self.enterRule(localctx, 142, self.RULE_intLitOrConstant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 712
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
            self.state = 714
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
        self.enterRule(localctx, 146, self.RULE_endOfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 716
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
         




