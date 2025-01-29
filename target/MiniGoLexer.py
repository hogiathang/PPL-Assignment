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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u01f4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\66\3\66\3\67\3\67\7\67\u015c\n\67\f\67")
        buf.write("\16\67\u015f\13\67\38\38\38\38\58\u0165\n8\39\39\39\7")
        buf.write("9\u016a\n9\f9\169\u016d\139\59\u016f\n9\3:\3:\3:\6:\u0174")
        buf.write("\n:\r:\16:\u0175\3;\3;\3;\6;\u017b\n;\r;\16;\u017c\3;")
        buf.write("\3;\6;\u0181\n;\r;\16;\u0182\5;\u0185\n;\3<\3<\3<\6<\u018a")
        buf.write("\n<\r<\16<\u018b\3=\3=\3=\5=\u0191\n=\3=\5=\u0194\n=\3")
        buf.write("=\5=\u0197\n=\3>\6>\u019a\n>\r>\16>\u019b\3?\3?\5?\u01a0")
        buf.write("\n?\3?\6?\u01a3\n?\r?\16?\u01a4\3@\3@\3@\7@\u01aa\n@\f")
        buf.write("@\16@\u01ad\13@\3@\3@\3@\3A\3A\3A\3B\3B\5B\u01b7\nB\3")
        buf.write("C\3C\3C\3C\3C\7C\u01be\nC\fC\16C\u01c1\13C\3C\3C\3C\3")
        buf.write("C\3C\3D\3D\3D\3D\7D\u01cc\nD\fD\16D\u01cf\13D\3D\3D\3")
        buf.write("E\6E\u01d4\nE\rE\16E\u01d5\3E\3E\3F\3F\3F\3G\3G\3G\7G")
        buf.write("\u01e0\nG\fG\16G\u01e3\13G\3G\3G\3H\3H\3H\7H\u01ea\nH")
        buf.write("\fH\16H\u01ed\13H\3H\3H\3H\3H\3I\3I\3\u01bf\2J\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q\2s\2u\2w\2y")
        buf.write(":{\2}\2\177;\u0081\2\u0083<\u0085=\u0087>\u0089?\u008b")
        buf.write("@\u008dA\u008fB\u0091C\3\2\22\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\3\2\63;\3\2\62;\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4")
        buf.write("\2ZZzz\5\2\62;CHch\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\7")
        buf.write("\2$$^^ppttvv\4\2\f\f\17\17\5\2\13\13\16\17\"\"\2\u0208")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2y")
        buf.write("\3\2\2\2\2\177\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0093\3\2\2")
        buf.write("\2\5\u0098\3\2\2\2\7\u009b\3\2\2\2\t\u00a0\3\2\2\2\13")
        buf.write("\u00a4\3\2\2\2\r\u00ab\3\2\2\2\17\u00b0\3\2\2\2\21\u00b5")
        buf.write("\3\2\2\2\23\u00bc\3\2\2\2\25\u00c6\3\2\2\2\27\u00cd\3")
        buf.write("\2\2\2\31\u00d1\3\2\2\2\33\u00d7\3\2\2\2\35\u00df\3\2")
        buf.write("\2\2\37\u00e4\3\2\2\2!\u00ea\3\2\2\2#\u00ee\3\2\2\2%\u00f4")
        buf.write("\3\2\2\2\'\u00f8\3\2\2\2)\u0101\3\2\2\2+\u0107\3\2\2\2")
        buf.write("-\u010d\3\2\2\2/\u010f\3\2\2\2\61\u0112\3\2\2\2\63\u0114")
        buf.write("\3\2\2\2\65\u0116\3\2\2\2\67\u0118\3\2\2\29\u011a\3\2")
        buf.write("\2\2;\u011c\3\2\2\2=\u011f\3\2\2\2?\u0122\3\2\2\2A\u0124")
        buf.write("\3\2\2\2C\u0127\3\2\2\2E\u0129\3\2\2\2G\u012c\3\2\2\2")
        buf.write("I\u012f\3\2\2\2K\u0132\3\2\2\2M\u0134\3\2\2\2O\u0137\3")
        buf.write("\2\2\2Q\u013a\3\2\2\2S\u013d\3\2\2\2U\u0140\3\2\2\2W\u0143")
        buf.write("\3\2\2\2Y\u0145\3\2\2\2[\u0147\3\2\2\2]\u0149\3\2\2\2")
        buf.write("_\u014b\3\2\2\2a\u014d\3\2\2\2c\u014f\3\2\2\2e\u0151\3")
        buf.write("\2\2\2g\u0153\3\2\2\2i\u0155\3\2\2\2k\u0157\3\2\2\2m\u0159")
        buf.write("\3\2\2\2o\u0164\3\2\2\2q\u016e\3\2\2\2s\u0170\3\2\2\2")
        buf.write("u\u0184\3\2\2\2w\u0186\3\2\2\2y\u018d\3\2\2\2{\u0199\3")
        buf.write("\2\2\2}\u019d\3\2\2\2\177\u01a6\3\2\2\2\u0081\u01b1\3")
        buf.write("\2\2\2\u0083\u01b6\3\2\2\2\u0085\u01b8\3\2\2\2\u0087\u01c7")
        buf.write("\3\2\2\2\u0089\u01d3\3\2\2\2\u008b\u01d9\3\2\2\2\u008d")
        buf.write("\u01dc\3\2\2\2\u008f\u01e6\3\2\2\2\u0091\u01f2\3\2\2\2")
        buf.write("\u0093\u0094\7o\2\2\u0094\u0095\7c\2\2\u0095\u0096\7k")
        buf.write("\2\2\u0096\u0097\7p\2\2\u0097\4\3\2\2\2\u0098\u0099\7")
        buf.write("k\2\2\u0099\u009a\7h\2\2\u009a\6\3\2\2\2\u009b\u009c\7")
        buf.write("g\2\2\u009c\u009d\7n\2\2\u009d\u009e\7u\2\2\u009e\u009f")
        buf.write("\7g\2\2\u009f\b\3\2\2\2\u00a0\u00a1\7h\2\2\u00a1\u00a2")
        buf.write("\7q\2\2\u00a2\u00a3\7t\2\2\u00a3\n\3\2\2\2\u00a4\u00a5")
        buf.write("\7t\2\2\u00a5\u00a6\7g\2\2\u00a6\u00a7\7v\2\2\u00a7\u00a8")
        buf.write("\7w\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa\7p\2\2\u00aa\f")
        buf.write("\3\2\2\2\u00ab\u00ac\7h\2\2\u00ac\u00ad\7w\2\2\u00ad\u00ae")
        buf.write("\7p\2\2\u00ae\u00af\7e\2\2\u00af\16\3\2\2\2\u00b0\u00b1")
        buf.write("\7v\2\2\u00b1\u00b2\7{\2\2\u00b2\u00b3\7r\2\2\u00b3\u00b4")
        buf.write("\7g\2\2\u00b4\20\3\2\2\2\u00b5\u00b6\7u\2\2\u00b6\u00b7")
        buf.write("\7v\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9\7w\2\2\u00b9\u00ba")
        buf.write("\7e\2\2\u00ba\u00bb\7v\2\2\u00bb\22\3\2\2\2\u00bc\u00bd")
        buf.write("\7k\2\2\u00bd\u00be\7p\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0")
        buf.write("\7g\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2\7h\2\2\u00c2\u00c3")
        buf.write("\7c\2\2\u00c3\u00c4\7e\2\2\u00c4\u00c5\7g\2\2\u00c5\24")
        buf.write("\3\2\2\2\u00c6\u00c7\7u\2\2\u00c7\u00c8\7v\2\2\u00c8\u00c9")
        buf.write("\7t\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc")
        buf.write("\7i\2\2\u00cc\26\3\2\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf")
        buf.write("\7p\2\2\u00cf\u00d0\7v\2\2\u00d0\30\3\2\2\2\u00d1\u00d2")
        buf.write("\7h\2\2\u00d2\u00d3\7n\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5")
        buf.write("\7c\2\2\u00d5\u00d6\7v\2\2\u00d6\32\3\2\2\2\u00d7\u00d8")
        buf.write("\7d\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7n\2\2\u00db\u00dc\7g\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de")
        buf.write("\7p\2\2\u00de\34\3\2\2\2\u00df\u00e0\7v\2\2\u00e0\u00e1")
        buf.write("\7t\2\2\u00e1\u00e2\7w\2\2\u00e2\u00e3\7g\2\2\u00e3\36")
        buf.write("\3\2\2\2\u00e4\u00e5\7h\2\2\u00e5\u00e6\7c\2\2\u00e6\u00e7")
        buf.write("\7n\2\2\u00e7\u00e8\7u\2\2\u00e8\u00e9\7g\2\2\u00e9 \3")
        buf.write("\2\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed")
        buf.write("\7n\2\2\u00ed\"\3\2\2\2\u00ee\u00ef\7e\2\2\u00ef\u00f0")
        buf.write("\7q\2\2\u00f0\u00f1\7p\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f3")
        buf.write("\7v\2\2\u00f3$\3\2\2\2\u00f4\u00f5\7x\2\2\u00f5\u00f6")
        buf.write("\7c\2\2\u00f6\u00f7\7t\2\2\u00f7&\3\2\2\2\u00f8\u00f9")
        buf.write("\7e\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc")
        buf.write("\7v\2\2\u00fc\u00fd\7k\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff")
        buf.write("\7w\2\2\u00ff\u0100\7g\2\2\u0100(\3\2\2\2\u0101\u0102")
        buf.write("\7d\2\2\u0102\u0103\7t\2\2\u0103\u0104\7g\2\2\u0104\u0105")
        buf.write("\7c\2\2\u0105\u0106\7m\2\2\u0106*\3\2\2\2\u0107\u0108")
        buf.write("\7t\2\2\u0108\u0109\7c\2\2\u0109\u010a\7p\2\2\u010a\u010b")
        buf.write("\7i\2\2\u010b\u010c\7g\2\2\u010c,\3\2\2\2\u010d\u010e")
        buf.write("\7?\2\2\u010e.\3\2\2\2\u010f\u0110\7<\2\2\u0110\u0111")
        buf.write("\7?\2\2\u0111\60\3\2\2\2\u0112\u0113\7-\2\2\u0113\62\3")
        buf.write("\2\2\2\u0114\u0115\7/\2\2\u0115\64\3\2\2\2\u0116\u0117")
        buf.write("\7,\2\2\u0117\66\3\2\2\2\u0118\u0119\7\61\2\2\u01198\3")
        buf.write("\2\2\2\u011a\u011b\7\'\2\2\u011b:\3\2\2\2\u011c\u011d")
        buf.write("\7?\2\2\u011d\u011e\7?\2\2\u011e<\3\2\2\2\u011f\u0120")
        buf.write("\7#\2\2\u0120\u0121\7?\2\2\u0121>\3\2\2\2\u0122\u0123")
        buf.write("\7>\2\2\u0123@\3\2\2\2\u0124\u0125\7>\2\2\u0125\u0126")
        buf.write("\7?\2\2\u0126B\3\2\2\2\u0127\u0128\7@\2\2\u0128D\3\2\2")
        buf.write("\2\u0129\u012a\7@\2\2\u012a\u012b\7?\2\2\u012bF\3\2\2")
        buf.write("\2\u012c\u012d\7(\2\2\u012d\u012e\7(\2\2\u012eH\3\2\2")
        buf.write("\2\u012f\u0130\7~\2\2\u0130\u0131\7~\2\2\u0131J\3\2\2")
        buf.write("\2\u0132\u0133\7#\2\2\u0133L\3\2\2\2\u0134\u0135\7-\2")
        buf.write("\2\u0135\u0136\7?\2\2\u0136N\3\2\2\2\u0137\u0138\7/\2")
        buf.write("\2\u0138\u0139\7?\2\2\u0139P\3\2\2\2\u013a\u013b\7,\2")
        buf.write("\2\u013b\u013c\7?\2\2\u013cR\3\2\2\2\u013d\u013e\7\61")
        buf.write("\2\2\u013e\u013f\7?\2\2\u013fT\3\2\2\2\u0140\u0141\7\'")
        buf.write("\2\2\u0141\u0142\7?\2\2\u0142V\3\2\2\2\u0143\u0144\7\60")
        buf.write("\2\2\u0144X\3\2\2\2\u0145\u0146\7a\2\2\u0146Z\3\2\2\2")
        buf.write("\u0147\u0148\7*\2\2\u0148\\\3\2\2\2\u0149\u014a\7+\2\2")
        buf.write("\u014a^\3\2\2\2\u014b\u014c\7}\2\2\u014c`\3\2\2\2\u014d")
        buf.write("\u014e\7\177\2\2\u014eb\3\2\2\2\u014f\u0150\7]\2\2\u0150")
        buf.write("d\3\2\2\2\u0151\u0152\7_\2\2\u0152f\3\2\2\2\u0153\u0154")
        buf.write("\7.\2\2\u0154h\3\2\2\2\u0155\u0156\7=\2\2\u0156j\3\2\2")
        buf.write("\2\u0157\u0158\7<\2\2\u0158l\3\2\2\2\u0159\u015d\t\2\2")
        buf.write("\2\u015a\u015c\t\3\2\2\u015b\u015a\3\2\2\2\u015c\u015f")
        buf.write("\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e")
        buf.write("n\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0165\5q9\2\u0161")
        buf.write("\u0165\5s:\2\u0162\u0165\5u;\2\u0163\u0165\5w<\2\u0164")
        buf.write("\u0160\3\2\2\2\u0164\u0161\3\2\2\2\u0164\u0162\3\2\2\2")
        buf.write("\u0164\u0163\3\2\2\2\u0165p\3\2\2\2\u0166\u016f\7\62\2")
        buf.write("\2\u0167\u016b\t\4\2\2\u0168\u016a\t\5\2\2\u0169\u0168")
        buf.write("\3\2\2\2\u016a\u016d\3\2\2\2\u016b\u0169\3\2\2\2\u016b")
        buf.write("\u016c\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2")
        buf.write("\u016e\u0166\3\2\2\2\u016e\u0167\3\2\2\2\u016fr\3\2\2")
        buf.write("\2\u0170\u0171\7\62\2\2\u0171\u0173\t\6\2\2\u0172\u0174")
        buf.write("\t\7\2\2\u0173\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175")
        buf.write("\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176t\3\2\2\2\u0177")
        buf.write("\u0178\7\62\2\2\u0178\u017a\t\b\2\2\u0179\u017b\t\t\2")
        buf.write("\2\u017a\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017a")
        buf.write("\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u0185\3\2\2\2\u017e")
        buf.write("\u0180\7\62\2\2\u017f\u0181\t\t\2\2\u0180\u017f\3\2\2")
        buf.write("\2\u0181\u0182\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183")
        buf.write("\3\2\2\2\u0183\u0185\3\2\2\2\u0184\u0177\3\2\2\2\u0184")
        buf.write("\u017e\3\2\2\2\u0185v\3\2\2\2\u0186\u0187\7\62\2\2\u0187")
        buf.write("\u0189\t\n\2\2\u0188\u018a\t\13\2\2\u0189\u0188\3\2\2")
        buf.write("\2\u018a\u018b\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c")
        buf.write("\3\2\2\2\u018cx\3\2\2\2\u018d\u0196\5{>\2\u018e\u0190")
        buf.write("\7\60\2\2\u018f\u0191\5{>\2\u0190\u018f\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191\u0193\3\2\2\2\u0192\u0194\5}?\2\u0193")
        buf.write("\u0192\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0197\3\2\2\2")
        buf.write("\u0195\u0197\5}?\2\u0196\u018e\3\2\2\2\u0196\u0195\3\2")
        buf.write("\2\2\u0197z\3\2\2\2\u0198\u019a\t\5\2\2\u0199\u0198\3")
        buf.write("\2\2\2\u019a\u019b\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c")
        buf.write("\3\2\2\2\u019c|\3\2\2\2\u019d\u019f\t\f\2\2\u019e\u01a0")
        buf.write("\t\r\2\2\u019f\u019e\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0")
        buf.write("\u01a2\3\2\2\2\u01a1\u01a3\t\5\2\2\u01a2\u01a1\3\2\2\2")
        buf.write("\u01a3\u01a4\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3")
        buf.write("\2\2\2\u01a5~\3\2\2\2\u01a6\u01ab\7$\2\2\u01a7\u01aa\5")
        buf.write("\u0081A\2\u01a8\u01aa\n\16\2\2\u01a9\u01a7\3\2\2\2\u01a9")
        buf.write("\u01a8\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9\3\2\2\2")
        buf.write("\u01ab\u01ac\3\2\2\2\u01ac\u01ae\3\2\2\2\u01ad\u01ab\3")
        buf.write("\2\2\2\u01ae\u01af\7$\2\2\u01af\u01b0\b@\2\2\u01b0\u0080")
        buf.write("\3\2\2\2\u01b1\u01b2\7^\2\2\u01b2\u01b3\t\17\2\2\u01b3")
        buf.write("\u0082\3\2\2\2\u01b4\u01b7\5\35\17\2\u01b5\u01b7\5\37")
        buf.write("\20\2\u01b6\u01b4\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7\u0084")
        buf.write("\3\2\2\2\u01b8\u01b9\7\61\2\2\u01b9\u01ba\7,\2\2\u01ba")
        buf.write("\u01bf\3\2\2\2\u01bb\u01be\5\u0085C\2\u01bc\u01be\13\2")
        buf.write("\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01bc\3\2\2\2\u01be\u01c1")
        buf.write("\3\2\2\2\u01bf\u01c0\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0")
        buf.write("\u01c2\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c3\7,\2\2")
        buf.write("\u01c3\u01c4\7\61\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c6")
        buf.write("\bC\3\2\u01c6\u0086\3\2\2\2\u01c7\u01c8\7\61\2\2\u01c8")
        buf.write("\u01c9\7\61\2\2\u01c9\u01cd\3\2\2\2\u01ca\u01cc\n\20\2")
        buf.write("\2\u01cb\u01ca\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01cb")
        buf.write("\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01d0\3\2\2\2\u01cf")
        buf.write("\u01cd\3\2\2\2\u01d0\u01d1\bD\3\2\u01d1\u0088\3\2\2\2")
        buf.write("\u01d2\u01d4\t\21\2\2\u01d3\u01d2\3\2\2\2\u01d4\u01d5")
        buf.write("\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6")
        buf.write("\u01d7\3\2\2\2\u01d7\u01d8\bE\3\2\u01d8\u008a\3\2\2\2")
        buf.write("\u01d9\u01da\7\f\2\2\u01da\u01db\bF\4\2\u01db\u008c\3")
        buf.write("\2\2\2\u01dc\u01e1\7$\2\2\u01dd\u01e0\5\u0081A\2\u01de")
        buf.write("\u01e0\n\16\2\2\u01df\u01dd\3\2\2\2\u01df\u01de\3\2\2")
        buf.write("\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e2")
        buf.write("\3\2\2\2\u01e2\u01e4\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e4")
        buf.write("\u01e5\bG\5\2\u01e5\u008e\3\2\2\2\u01e6\u01eb\7$\2\2\u01e7")
        buf.write("\u01ea\5\u0081A\2\u01e8\u01ea\n\16\2\2\u01e9\u01e7\3\2")
        buf.write("\2\2\u01e9\u01e8\3\2\2\2\u01ea\u01ed\3\2\2\2\u01eb\u01e9")
        buf.write("\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ee\3\2\2\2\u01ed")
        buf.write("\u01eb\3\2\2\2\u01ee\u01ef\7^\2\2\u01ef\u01f0\n\17\2\2")
        buf.write("\u01f0\u01f1\bH\6\2\u01f1\u0090\3\2\2\2\u01f2\u01f3\13")
        buf.write("\2\2\2\u01f3\u0092\3\2\2\2\35\2\u015d\u0164\u016b\u016e")
        buf.write("\u0175\u017c\u0182\u0184\u018b\u0190\u0193\u0196\u019b")
        buf.write("\u019f\u01a4\u01a9\u01ab\u01b6\u01bd\u01bf\u01cd\u01d5")
        buf.write("\u01df\u01e1\u01e9\u01eb\7\3@\2\b\2\2\3F\3\3G\4\3H\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    IF = 2
    ELSE = 3
    FOR = 4
    RETURN = 5
    FUNC = 6
    TYPE = 7
    STRUCT = 8
    INTERFACE = 9
    STRING = 10
    INT = 11
    FLOAT = 12
    BOOLEAN = 13
    TRUE = 14
    FALSE = 15
    NIL = 16
    CONST = 17
    VAR = 18
    CONTINUE = 19
    BREAK = 20
    RANGE = 21
    ASSIGN = 22
    DECLARE = 23
    PLUS = 24
    MINUS = 25
    MUL = 26
    DIV = 27
    MOD = 28
    EQ = 29
    NEQ = 30
    LT = 31
    LEQ = 32
    GT = 33
    GEQ = 34
    AND = 35
    OR = 36
    NOT = 37
    PLUS_ASSIGN = 38
    MINUS_ASSIGN = 39
    MUL_ASSIGN = 40
    DIV_ASSIGN = 41
    MOD_ASSIGN = 42
    DOT = 43
    BLANK = 44
    LPAREN = 45
    RPAREN = 46
    LBRACE = 47
    RBRACE = 48
    LBRACKET = 49
    RBRACKET = 50
    COMMA = 51
    SEMI = 52
    COLON = 53
    IDENTIFIER = 54
    INT_LIT = 55
    FLOAT_LIT = 56
    STRING_LIT = 57
    BOOL_LIT = 58
    BLOCK_COMMENT = 59
    LINE_COMMENT = 60
    WS = 61
    NEWLINE = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
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
            "BOOL_LIT", "BLOCK_COMMENT", "LINE_COMMENT", "WS", "NEWLINE", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                  "TRUE", "FALSE", "NIL", "CONST", "VAR", "CONTINUE", "BREAK", 
                  "RANGE", "ASSIGN", "DECLARE", "PLUS", "MINUS", "MUL", 
                  "DIV", "MOD", "EQ", "NEQ", "LT", "LEQ", "GT", "GEQ", "AND", 
                  "OR", "NOT", "PLUS_ASSIGN", "MINUS_ASSIGN", "MUL_ASSIGN", 
                  "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "BLANK", "LPAREN", 
                  "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
                  "COMMA", "SEMI", "COLON", "IDENTIFIER", "INT_LIT", "DEC_LIT", 
                  "BIN_LIT", "OCT_LIT", "HEX_LIT", "FLOAT_LIT", "DEC_PART", 
                  "EXPONENT", "STRING_LIT", "ESC_SEQ", "BOOL_LIT", "BLOCK_COMMENT", 
                  "LINE_COMMENT", "WS", "NEWLINE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

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
            actions[62] = self.STRING_LIT_action 
            actions[68] = self.NEWLINE_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                lastToken = self.lastTokenType
                if lastToken in [self.IDENTIFIER, self.INT_LIT, self.FLOAT_LIT, self.STRING_LIT, self.BOOL_LIT, self.RBRACKET, self.RPAREN]:
                    self.text = ';';
                else:
                    self.skip();

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text[1:]
     


