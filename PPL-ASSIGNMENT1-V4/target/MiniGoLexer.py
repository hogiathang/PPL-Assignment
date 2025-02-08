# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01e3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3")
        buf.write("+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\7\66\u0153")
        buf.write("\n\66\f\66\16\66\u0156\13\66\3\67\3\67\3\67\3\67\5\67")
        buf.write("\u015c\n\67\38\38\38\78\u0161\n8\f8\168\u0164\138\58\u0166")
        buf.write("\n8\39\39\39\69\u016b\n9\r9\169\u016c\3:\3:\3:\6:\u0172")
        buf.write("\n:\r:\16:\u0173\3:\3:\6:\u0178\n:\r:\16:\u0179\5:\u017c")
        buf.write("\n:\3;\3;\3;\6;\u0181\n;\r;\16;\u0182\3<\3<\3<\5<\u0188")
        buf.write("\n<\3<\5<\u018b\n<\3<\5<\u018e\n<\3=\6=\u0191\n=\r=\16")
        buf.write("=\u0192\3>\3>\5>\u0197\n>\3>\6>\u019a\n>\r>\16>\u019b")
        buf.write("\3?\3?\3?\7?\u01a1\n?\f?\16?\u01a4\13?\3?\3?\3@\3@\3@")
        buf.write("\3A\3A\3A\3A\3A\7A\u01b0\nA\fA\16A\u01b3\13A\3A\3A\3A")
        buf.write("\3A\3A\3B\3B\3B\3B\7B\u01be\nB\fB\16B\u01c1\13B\3B\3B")
        buf.write("\3C\6C\u01c6\nC\rC\16C\u01c7\3C\3C\3D\3D\3D\3E\3E\3E\7")
        buf.write("E\u01d2\nE\fE\16E\u01d5\13E\3F\3F\3F\7F\u01da\nF\fF\16")
        buf.write("F\u01dd\13F\3F\3F\3F\3G\3G\3\u01b1\2H\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o\2q\2s\2u\2w9y\2{\2}:\177")
        buf.write("\2\u0081;\u0083<\u0085=\u0087>\u0089?\u008b@\u008dA\3")
        buf.write("\2\22\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2DD")
        buf.write("dd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2G")
        buf.write("Ggg\4\2--//\4\2$$^^\7\2$$^^ppttvv\4\2\f\f\17\17\5\2\13")
        buf.write("\13\16\17\"\"\2\u01f6\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2w\3\2\2\2\2}\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\3\u008f\3\2\2\2\5\u0092")
        buf.write("\3\2\2\2\7\u0097\3\2\2\2\t\u009b\3\2\2\2\13\u00a2\3\2")
        buf.write("\2\2\r\u00a7\3\2\2\2\17\u00ac\3\2\2\2\21\u00b3\3\2\2\2")
        buf.write("\23\u00bd\3\2\2\2\25\u00c4\3\2\2\2\27\u00c8\3\2\2\2\31")
        buf.write("\u00ce\3\2\2\2\33\u00d6\3\2\2\2\35\u00db\3\2\2\2\37\u00e1")
        buf.write("\3\2\2\2!\u00e5\3\2\2\2#\u00eb\3\2\2\2%\u00ef\3\2\2\2")
        buf.write("\'\u00f8\3\2\2\2)\u00fe\3\2\2\2+\u0104\3\2\2\2-\u0106")
        buf.write("\3\2\2\2/\u0109\3\2\2\2\61\u010b\3\2\2\2\63\u010d\3\2")
        buf.write("\2\2\65\u010f\3\2\2\2\67\u0111\3\2\2\29\u0113\3\2\2\2")
        buf.write(";\u0116\3\2\2\2=\u0119\3\2\2\2?\u011b\3\2\2\2A\u011e\3")
        buf.write("\2\2\2C\u0120\3\2\2\2E\u0123\3\2\2\2G\u0126\3\2\2\2I\u0129")
        buf.write("\3\2\2\2K\u012b\3\2\2\2M\u012e\3\2\2\2O\u0131\3\2\2\2")
        buf.write("Q\u0134\3\2\2\2S\u0137\3\2\2\2U\u013a\3\2\2\2W\u013c\3")
        buf.write("\2\2\2Y\u013e\3\2\2\2[\u0140\3\2\2\2]\u0142\3\2\2\2_\u0144")
        buf.write("\3\2\2\2a\u0146\3\2\2\2c\u0148\3\2\2\2e\u014a\3\2\2\2")
        buf.write("g\u014c\3\2\2\2i\u014e\3\2\2\2k\u0150\3\2\2\2m\u015b\3")
        buf.write("\2\2\2o\u0165\3\2\2\2q\u0167\3\2\2\2s\u017b\3\2\2\2u\u017d")
        buf.write("\3\2\2\2w\u0184\3\2\2\2y\u0190\3\2\2\2{\u0194\3\2\2\2")
        buf.write("}\u019d\3\2\2\2\177\u01a7\3\2\2\2\u0081\u01aa\3\2\2\2")
        buf.write("\u0083\u01b9\3\2\2\2\u0085\u01c5\3\2\2\2\u0087\u01cb\3")
        buf.write("\2\2\2\u0089\u01ce\3\2\2\2\u008b\u01d6\3\2\2\2\u008d\u01e1")
        buf.write("\3\2\2\2\u008f\u0090\7k\2\2\u0090\u0091\7h\2\2\u0091\4")
        buf.write("\3\2\2\2\u0092\u0093\7g\2\2\u0093\u0094\7n\2\2\u0094\u0095")
        buf.write("\7u\2\2\u0095\u0096\7g\2\2\u0096\6\3\2\2\2\u0097\u0098")
        buf.write("\7h\2\2\u0098\u0099\7q\2\2\u0099\u009a\7t\2\2\u009a\b")
        buf.write("\3\2\2\2\u009b\u009c\7t\2\2\u009c\u009d\7g\2\2\u009d\u009e")
        buf.write("\7v\2\2\u009e\u009f\7w\2\2\u009f\u00a0\7t\2\2\u00a0\u00a1")
        buf.write("\7p\2\2\u00a1\n\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3\u00a4")
        buf.write("\7w\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6\7e\2\2\u00a6\f")
        buf.write("\3\2\2\2\u00a7\u00a8\7v\2\2\u00a8\u00a9\7{\2\2\u00a9\u00aa")
        buf.write("\7r\2\2\u00aa\u00ab\7g\2\2\u00ab\16\3\2\2\2\u00ac\u00ad")
        buf.write("\7u\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7t\2\2\u00af\u00b0")
        buf.write("\7w\2\2\u00b0\u00b1\7e\2\2\u00b1\u00b2\7v\2\2\u00b2\20")
        buf.write("\3\2\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6")
        buf.write("\7v\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9")
        buf.write("\7h\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb\7e\2\2\u00bb\u00bc")
        buf.write("\7g\2\2\u00bc\22\3\2\2\2\u00bd\u00be\7u\2\2\u00be\u00bf")
        buf.write("\7v\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2")
        buf.write("\7p\2\2\u00c2\u00c3\7i\2\2\u00c3\24\3\2\2\2\u00c4\u00c5")
        buf.write("\7k\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7v\2\2\u00c7\26")
        buf.write("\3\2\2\2\u00c8\u00c9\7h\2\2\u00c9\u00ca\7n\2\2\u00ca\u00cb")
        buf.write("\7q\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd\7v\2\2\u00cd\30")
        buf.write("\3\2\2\2\u00ce\u00cf\7d\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d1")
        buf.write("\7q\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4")
        buf.write("\7c\2\2\u00d4\u00d5\7p\2\2\u00d5\32\3\2\2\2\u00d6\u00d7")
        buf.write("\7v\2\2\u00d7\u00d8\7t\2\2\u00d8\u00d9\7w\2\2\u00d9\u00da")
        buf.write("\7g\2\2\u00da\34\3\2\2\2\u00db\u00dc\7h\2\2\u00dc\u00dd")
        buf.write("\7c\2\2\u00dd\u00de\7n\2\2\u00de\u00df\7u\2\2\u00df\u00e0")
        buf.write("\7g\2\2\u00e0\36\3\2\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3")
        buf.write("\7k\2\2\u00e3\u00e4\7n\2\2\u00e4 \3\2\2\2\u00e5\u00e6")
        buf.write("\7e\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9")
        buf.write("\7u\2\2\u00e9\u00ea\7v\2\2\u00ea\"\3\2\2\2\u00eb\u00ec")
        buf.write("\7x\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee\7t\2\2\u00ee$\3")
        buf.write("\2\2\2\u00ef\u00f0\7e\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2")
        buf.write("\7p\2\2\u00f2\u00f3\7v\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5")
        buf.write("\7p\2\2\u00f5\u00f6\7w\2\2\u00f6\u00f7\7g\2\2\u00f7&\3")
        buf.write("\2\2\2\u00f8\u00f9\7d\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb")
        buf.write("\7g\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd\7m\2\2\u00fd(\3")
        buf.write("\2\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7c\2\2\u0100\u0101")
        buf.write("\7p\2\2\u0101\u0102\7i\2\2\u0102\u0103\7g\2\2\u0103*\3")
        buf.write("\2\2\2\u0104\u0105\7?\2\2\u0105,\3\2\2\2\u0106\u0107\7")
        buf.write("<\2\2\u0107\u0108\7?\2\2\u0108.\3\2\2\2\u0109\u010a\7")
        buf.write("-\2\2\u010a\60\3\2\2\2\u010b\u010c\7/\2\2\u010c\62\3\2")
        buf.write("\2\2\u010d\u010e\7,\2\2\u010e\64\3\2\2\2\u010f\u0110\7")
        buf.write("\61\2\2\u0110\66\3\2\2\2\u0111\u0112\7\'\2\2\u01128\3")
        buf.write("\2\2\2\u0113\u0114\7?\2\2\u0114\u0115\7?\2\2\u0115:\3")
        buf.write("\2\2\2\u0116\u0117\7#\2\2\u0117\u0118\7?\2\2\u0118<\3")
        buf.write("\2\2\2\u0119\u011a\7>\2\2\u011a>\3\2\2\2\u011b\u011c\7")
        buf.write(">\2\2\u011c\u011d\7?\2\2\u011d@\3\2\2\2\u011e\u011f\7")
        buf.write("@\2\2\u011fB\3\2\2\2\u0120\u0121\7@\2\2\u0121\u0122\7")
        buf.write("?\2\2\u0122D\3\2\2\2\u0123\u0124\7(\2\2\u0124\u0125\7")
        buf.write("(\2\2\u0125F\3\2\2\2\u0126\u0127\7~\2\2\u0127\u0128\7")
        buf.write("~\2\2\u0128H\3\2\2\2\u0129\u012a\7#\2\2\u012aJ\3\2\2\2")
        buf.write("\u012b\u012c\7-\2\2\u012c\u012d\7?\2\2\u012dL\3\2\2\2")
        buf.write("\u012e\u012f\7/\2\2\u012f\u0130\7?\2\2\u0130N\3\2\2\2")
        buf.write("\u0131\u0132\7,\2\2\u0132\u0133\7?\2\2\u0133P\3\2\2\2")
        buf.write("\u0134\u0135\7\61\2\2\u0135\u0136\7?\2\2\u0136R\3\2\2")
        buf.write("\2\u0137\u0138\7\'\2\2\u0138\u0139\7?\2\2\u0139T\3\2\2")
        buf.write("\2\u013a\u013b\7\60\2\2\u013bV\3\2\2\2\u013c\u013d\7a")
        buf.write("\2\2\u013dX\3\2\2\2\u013e\u013f\7*\2\2\u013fZ\3\2\2\2")
        buf.write("\u0140\u0141\7+\2\2\u0141\\\3\2\2\2\u0142\u0143\7}\2\2")
        buf.write("\u0143^\3\2\2\2\u0144\u0145\7\177\2\2\u0145`\3\2\2\2\u0146")
        buf.write("\u0147\7]\2\2\u0147b\3\2\2\2\u0148\u0149\7_\2\2\u0149")
        buf.write("d\3\2\2\2\u014a\u014b\7.\2\2\u014bf\3\2\2\2\u014c\u014d")
        buf.write("\7=\2\2\u014dh\3\2\2\2\u014e\u014f\7<\2\2\u014fj\3\2\2")
        buf.write("\2\u0150\u0154\t\2\2\2\u0151\u0153\t\3\2\2\u0152\u0151")
        buf.write("\3\2\2\2\u0153\u0156\3\2\2\2\u0154\u0152\3\2\2\2\u0154")
        buf.write("\u0155\3\2\2\2\u0155l\3\2\2\2\u0156\u0154\3\2\2\2\u0157")
        buf.write("\u015c\5o8\2\u0158\u015c\5q9\2\u0159\u015c\5s:\2\u015a")
        buf.write("\u015c\5u;\2\u015b\u0157\3\2\2\2\u015b\u0158\3\2\2\2\u015b")
        buf.write("\u0159\3\2\2\2\u015b\u015a\3\2\2\2\u015cn\3\2\2\2\u015d")
        buf.write("\u0166\7\62\2\2\u015e\u0162\t\4\2\2\u015f\u0161\t\5\2")
        buf.write("\2\u0160\u015f\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160")
        buf.write("\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0166\3\2\2\2\u0164")
        buf.write("\u0162\3\2\2\2\u0165\u015d\3\2\2\2\u0165\u015e\3\2\2\2")
        buf.write("\u0166p\3\2\2\2\u0167\u0168\7\62\2\2\u0168\u016a\t\6\2")
        buf.write("\2\u0169\u016b\t\7\2\2\u016a\u0169\3\2\2\2\u016b\u016c")
        buf.write("\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("r\3\2\2\2\u016e\u016f\7\62\2\2\u016f\u0171\t\b\2\2\u0170")
        buf.write("\u0172\t\t\2\2\u0171\u0170\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u017c\3")
        buf.write("\2\2\2\u0175\u0177\7\62\2\2\u0176\u0178\t\t\2\2\u0177")
        buf.write("\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u0177\3\2\2\2")
        buf.write("\u0179\u017a\3\2\2\2\u017a\u017c\3\2\2\2\u017b\u016e\3")
        buf.write("\2\2\2\u017b\u0175\3\2\2\2\u017ct\3\2\2\2\u017d\u017e")
        buf.write("\7\62\2\2\u017e\u0180\t\n\2\2\u017f\u0181\t\13\2\2\u0180")
        buf.write("\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0180\3\2\2\2")
        buf.write("\u0182\u0183\3\2\2\2\u0183v\3\2\2\2\u0184\u018d\5y=\2")
        buf.write("\u0185\u0187\7\60\2\2\u0186\u0188\5y=\2\u0187\u0186\3")
        buf.write("\2\2\2\u0187\u0188\3\2\2\2\u0188\u018a\3\2\2\2\u0189\u018b")
        buf.write("\5{>\2\u018a\u0189\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018e")
        buf.write("\3\2\2\2\u018c\u018e\5{>\2\u018d\u0185\3\2\2\2\u018d\u018c")
        buf.write("\3\2\2\2\u018ex\3\2\2\2\u018f\u0191\t\5\2\2\u0190\u018f")
        buf.write("\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0190\3\2\2\2\u0192")
        buf.write("\u0193\3\2\2\2\u0193z\3\2\2\2\u0194\u0196\t\f\2\2\u0195")
        buf.write("\u0197\t\r\2\2\u0196\u0195\3\2\2\2\u0196\u0197\3\2\2\2")
        buf.write("\u0197\u0199\3\2\2\2\u0198\u019a\t\5\2\2\u0199\u0198\3")
        buf.write("\2\2\2\u019a\u019b\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c")
        buf.write("\3\2\2\2\u019c|\3\2\2\2\u019d\u01a2\7$\2\2\u019e\u01a1")
        buf.write("\5\177@\2\u019f\u01a1\n\16\2\2\u01a0\u019e\3\2\2\2\u01a0")
        buf.write("\u019f\3\2\2\2\u01a1\u01a4\3\2\2\2\u01a2\u01a0\3\2\2\2")
        buf.write("\u01a2\u01a3\3\2\2\2\u01a3\u01a5\3\2\2\2\u01a4\u01a2\3")
        buf.write("\2\2\2\u01a5\u01a6\7$\2\2\u01a6~\3\2\2\2\u01a7\u01a8\7")
        buf.write("^\2\2\u01a8\u01a9\t\17\2\2\u01a9\u0080\3\2\2\2\u01aa\u01ab")
        buf.write("\7\61\2\2\u01ab\u01ac\7,\2\2\u01ac\u01b1\3\2\2\2\u01ad")
        buf.write("\u01b0\5\u0081A\2\u01ae\u01b0\13\2\2\2\u01af\u01ad\3\2")
        buf.write("\2\2\u01af\u01ae\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01b2")
        buf.write("\3\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b4\3\2\2\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b4\u01b5\7,\2\2\u01b5\u01b6\7\61\2\2")
        buf.write("\u01b6\u01b7\3\2\2\2\u01b7\u01b8\bA\2\2\u01b8\u0082\3")
        buf.write("\2\2\2\u01b9\u01ba\7\61\2\2\u01ba\u01bb\7\61\2\2\u01bb")
        buf.write("\u01bf\3\2\2\2\u01bc\u01be\n\20\2\2\u01bd\u01bc\3\2\2")
        buf.write("\2\u01be\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0")
        buf.write("\3\2\2\2\u01c0\u01c2\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2")
        buf.write("\u01c3\bB\2\2\u01c3\u0084\3\2\2\2\u01c4\u01c6\t\21\2\2")
        buf.write("\u01c5\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c5\3")
        buf.write("\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca")
        buf.write("\bC\2\2\u01ca\u0086\3\2\2\2\u01cb\u01cc\7\f\2\2\u01cc")
        buf.write("\u01cd\bD\3\2\u01cd\u0088\3\2\2\2\u01ce\u01d3\7$\2\2\u01cf")
        buf.write("\u01d2\5\177@\2\u01d0\u01d2\n\16\2\2\u01d1\u01cf\3\2\2")
        buf.write("\2\u01d1\u01d0\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1")
        buf.write("\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u008a\3\2\2\2\u01d5")
        buf.write("\u01d3\3\2\2\2\u01d6\u01db\7$\2\2\u01d7\u01da\5\177@\2")
        buf.write("\u01d8\u01da\n\16\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01d8")
        buf.write("\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01d9\3\2\2\2\u01db")
        buf.write("\u01dc\3\2\2\2\u01dc\u01de\3\2\2\2\u01dd\u01db\3\2\2\2")
        buf.write("\u01de\u01df\7^\2\2\u01df\u01e0\n\17\2\2\u01e0\u008c\3")
        buf.write("\2\2\2\u01e1\u01e2\13\2\2\2\u01e2\u008e\3\2\2\2\34\2\u0154")
        buf.write("\u015b\u0162\u0165\u016c\u0173\u0179\u017b\u0182\u0187")
        buf.write("\u018a\u018d\u0192\u0196\u019b\u01a0\u01a2\u01af\u01b1")
        buf.write("\u01bf\u01c7\u01d1\u01d3\u01d9\u01db\4\b\2\2\3D\2")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ELSE = 2
    FOR = 3
    RETURN = 4
    FUNC = 5
    TYPE = 6
    STRUCT = 7
    INTERFACE = 8
    STRING = 9
    INT = 10
    FLOAT = 11
    BOOLEAN = 12
    TRUE = 13
    FALSE = 14
    NIL = 15
    CONST = 16
    VAR = 17
    CONTINUE = 18
    BREAK = 19
    RANGE = 20
    ASSIGN = 21
    DECLARE = 22
    PLUS = 23
    MINUS = 24
    MUL = 25
    DIV = 26
    MOD = 27
    EQ = 28
    NEQ = 29
    LT = 30
    LEQ = 31
    GT = 32
    GEQ = 33
    AND = 34
    OR = 35
    NOT = 36
    PLUS_ASSIGN = 37
    MINUS_ASSIGN = 38
    MUL_ASSIGN = 39
    DIV_ASSIGN = 40
    MOD_ASSIGN = 41
    DOT = 42
    BLANK = 43
    LPAREN = 44
    RPAREN = 45
    LBRACE = 46
    RBRACE = 47
    LBRACKET = 48
    RBRACKET = 49
    COMMA = 50
    SEMI = 51
    COLON = 52
    IDENTIFIER = 53
    INT_LIT = 54
    FLOAT_LIT = 55
    STRING_LIT = 56
    BLOCK_COMMENT = 57
    LINE_COMMENT = 58
    WS = 59
    NEWLINE = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'true'", "'false'", "'nil'", "'const'", "'var'", "'continue'", 
            "'break'", "'range'", "'='", "':='", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", 
            "'||'", "'!'", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "'_'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'", 
            "':'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "TRUE", "FALSE", "NIL", 
            "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "ASSIGN", "DECLARE", 
            "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQ", "NEQ", "LT", "LEQ", 
            "GT", "GEQ", "AND", "OR", "NOT", "PLUS_ASSIGN", "MINUS_ASSIGN", 
            "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "BLANK", "LPAREN", 
            "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "COMMA", 
            "SEMI", "COLON", "IDENTIFIER", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
            "BLOCK_COMMENT", "LINE_COMMENT", "WS", "NEWLINE", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", "TRUE", 
                  "FALSE", "NIL", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                  "ASSIGN", "DECLARE", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
                  "EQ", "NEQ", "LT", "LEQ", "GT", "GEQ", "AND", "OR", "NOT", 
                  "PLUS_ASSIGN", "MINUS_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
                  "MOD_ASSIGN", "DOT", "BLANK", "LPAREN", "RPAREN", "LBRACE", 
                  "RBRACE", "LBRACKET", "RBRACKET", "COMMA", "SEMI", "COLON", 
                  "IDENTIFIER", "INT_LIT", "DEC_LIT", "BIN_LIT", "OCT_LIT", 
                  "HEX_LIT", "FLOAT_LIT", "DEC_PART", "EXPONENT", "STRING_LIT", 
                  "ESC_SEQ", "BLOCK_COMMENT", "LINE_COMMENT", "WS", "NEWLINE", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    lastTokenType = None;
    def emit(self):
        tk = self.type
        self.lastTokenType = tk
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[66] = self.NEWLINE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                listAllowedToken = [
                    self.IDENTIFIER, self.INT_LIT, self.FLOAT_LIT, self.STRING_LIT,
                    self.RPAREN, self.RBRACE, self.RBRACKET,
                    self.INT, self.FLOAT, self.STRING, self.BOOLEAN,
                    self.TRUE, self.FALSE, self.BREAK, self.CONTINUE, self.RETURN
                ];
                if self.lastTokenType in listAllowedToken:
                    self.text = ';';
                else:
                    self.skip();

     


