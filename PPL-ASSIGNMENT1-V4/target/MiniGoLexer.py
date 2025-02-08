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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01ea\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\7\67\u015a\n\67\f\67\16\67\u015d")
        buf.write("\13\67\38\38\38\38\58\u0163\n8\39\39\39\79\u0168\n9\f")
        buf.write("9\169\u016b\139\59\u016d\n9\3:\3:\3:\6:\u0172\n:\r:\16")
        buf.write(":\u0173\3;\3;\3;\6;\u0179\n;\r;\16;\u017a\3;\3;\6;\u017f")
        buf.write("\n;\r;\16;\u0180\5;\u0183\n;\3<\3<\3<\6<\u0188\n<\r<\16")
        buf.write("<\u0189\3=\3=\3=\5=\u018f\n=\3=\5=\u0192\n=\3=\5=\u0195")
        buf.write("\n=\3>\6>\u0198\n>\r>\16>\u0199\3?\3?\5?\u019e\n?\3?\6")
        buf.write("?\u01a1\n?\r?\16?\u01a2\3@\3@\3@\7@\u01a8\n@\f@\16@\u01ab")
        buf.write("\13@\3@\3@\3A\3A\3A\3B\3B\3B\3B\3B\7B\u01b7\nB\fB\16B")
        buf.write("\u01ba\13B\3B\3B\3B\3B\3B\3C\3C\3C\3C\7C\u01c5\nC\fC\16")
        buf.write("C\u01c8\13C\3C\3C\3D\6D\u01cd\nD\rD\16D\u01ce\3D\3D\3")
        buf.write("E\3E\3E\3F\3F\3F\7F\u01d9\nF\fF\16F\u01dc\13F\3G\3G\3")
        buf.write("G\7G\u01e1\nG\fG\16G\u01e4\13G\3G\3G\3G\3H\3H\3\u01b8")
        buf.write("\2I\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write("\2s\2u\2w\2y:{\2}\2\177;\u0081\2\u0083<\u0085=\u0087>")
        buf.write("\u0089?\u008b@\u008dA\u008fB\3\2\22\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2\63;\3\2\62;\4\2DDdd\3\2\62\63\4\2QQqq\3\2")
        buf.write("\629\4\2ZZzz\5\2\62;CHch\4\2GGgg\4\2--//\4\2$$^^\7\2$")
        buf.write("$^^ppttvv\4\2\f\f\17\17\5\2\13\13\16\17\"\"\2\u01fd\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2y")
        buf.write("\3\2\2\2\2\177\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\3\u0091\3\2\2\2\5\u0096\3\2\2")
        buf.write("\2\7\u0099\3\2\2\2\t\u009e\3\2\2\2\13\u00a2\3\2\2\2\r")
        buf.write("\u00a9\3\2\2\2\17\u00ae\3\2\2\2\21\u00b3\3\2\2\2\23\u00ba")
        buf.write("\3\2\2\2\25\u00c4\3\2\2\2\27\u00cb\3\2\2\2\31\u00cf\3")
        buf.write("\2\2\2\33\u00d5\3\2\2\2\35\u00dd\3\2\2\2\37\u00e2\3\2")
        buf.write("\2\2!\u00e8\3\2\2\2#\u00ec\3\2\2\2%\u00f2\3\2\2\2\'\u00f6")
        buf.write("\3\2\2\2)\u00ff\3\2\2\2+\u0105\3\2\2\2-\u010b\3\2\2\2")
        buf.write("/\u010d\3\2\2\2\61\u0110\3\2\2\2\63\u0112\3\2\2\2\65\u0114")
        buf.write("\3\2\2\2\67\u0116\3\2\2\29\u0118\3\2\2\2;\u011a\3\2\2")
        buf.write("\2=\u011d\3\2\2\2?\u0120\3\2\2\2A\u0122\3\2\2\2C\u0125")
        buf.write("\3\2\2\2E\u0127\3\2\2\2G\u012a\3\2\2\2I\u012d\3\2\2\2")
        buf.write("K\u0130\3\2\2\2M\u0132\3\2\2\2O\u0135\3\2\2\2Q\u0138\3")
        buf.write("\2\2\2S\u013b\3\2\2\2U\u013e\3\2\2\2W\u0141\3\2\2\2Y\u0143")
        buf.write("\3\2\2\2[\u0145\3\2\2\2]\u0147\3\2\2\2_\u0149\3\2\2\2")
        buf.write("a\u014b\3\2\2\2c\u014d\3\2\2\2e\u014f\3\2\2\2g\u0151\3")
        buf.write("\2\2\2i\u0153\3\2\2\2k\u0155\3\2\2\2m\u0157\3\2\2\2o\u0162")
        buf.write("\3\2\2\2q\u016c\3\2\2\2s\u016e\3\2\2\2u\u0182\3\2\2\2")
        buf.write("w\u0184\3\2\2\2y\u018b\3\2\2\2{\u0197\3\2\2\2}\u019b\3")
        buf.write("\2\2\2\177\u01a4\3\2\2\2\u0081\u01ae\3\2\2\2\u0083\u01b1")
        buf.write("\3\2\2\2\u0085\u01c0\3\2\2\2\u0087\u01cc\3\2\2\2\u0089")
        buf.write("\u01d2\3\2\2\2\u008b\u01d5\3\2\2\2\u008d\u01dd\3\2\2\2")
        buf.write("\u008f\u01e8\3\2\2\2\u0091\u0092\7o\2\2\u0092\u0093\7")
        buf.write("c\2\2\u0093\u0094\7k\2\2\u0094\u0095\7p\2\2\u0095\4\3")
        buf.write("\2\2\2\u0096\u0097\7k\2\2\u0097\u0098\7h\2\2\u0098\6\3")
        buf.write("\2\2\2\u0099\u009a\7g\2\2\u009a\u009b\7n\2\2\u009b\u009c")
        buf.write("\7u\2\2\u009c\u009d\7g\2\2\u009d\b\3\2\2\2\u009e\u009f")
        buf.write("\7h\2\2\u009f\u00a0\7q\2\2\u00a0\u00a1\7t\2\2\u00a1\n")
        buf.write("\3\2\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4\7g\2\2\u00a4\u00a5")
        buf.write("\7v\2\2\u00a5\u00a6\7w\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8")
        buf.write("\7p\2\2\u00a8\f\3\2\2\2\u00a9\u00aa\7h\2\2\u00aa\u00ab")
        buf.write("\7w\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad\7e\2\2\u00ad\16")
        buf.write("\3\2\2\2\u00ae\u00af\7v\2\2\u00af\u00b0\7{\2\2\u00b0\u00b1")
        buf.write("\7r\2\2\u00b1\u00b2\7g\2\2\u00b2\20\3\2\2\2\u00b3\u00b4")
        buf.write("\7u\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6\7t\2\2\u00b6\u00b7")
        buf.write("\7w\2\2\u00b7\u00b8\7e\2\2\u00b8\u00b9\7v\2\2\u00b9\22")
        buf.write("\3\2\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc\7p\2\2\u00bc\u00bd")
        buf.write("\7v\2\2\u00bd\u00be\7g\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0")
        buf.write("\7h\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7e\2\2\u00c2\u00c3")
        buf.write("\7g\2\2\u00c3\24\3\2\2\2\u00c4\u00c5\7u\2\2\u00c5\u00c6")
        buf.write("\7v\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9")
        buf.write("\7p\2\2\u00c9\u00ca\7i\2\2\u00ca\26\3\2\2\2\u00cb\u00cc")
        buf.write("\7k\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7v\2\2\u00ce\30")
        buf.write("\3\2\2\2\u00cf\u00d0\7h\2\2\u00d0\u00d1\7n\2\2\u00d1\u00d2")
        buf.write("\7q\2\2\u00d2\u00d3\7c\2\2\u00d3\u00d4\7v\2\2\u00d4\32")
        buf.write("\3\2\2\2\u00d5\u00d6\7d\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8")
        buf.write("\7q\2\2\u00d8\u00d9\7n\2\2\u00d9\u00da\7g\2\2\u00da\u00db")
        buf.write("\7c\2\2\u00db\u00dc\7p\2\2\u00dc\34\3\2\2\2\u00dd\u00de")
        buf.write("\7v\2\2\u00de\u00df\7t\2\2\u00df\u00e0\7w\2\2\u00e0\u00e1")
        buf.write("\7g\2\2\u00e1\36\3\2\2\2\u00e2\u00e3\7h\2\2\u00e3\u00e4")
        buf.write("\7c\2\2\u00e4\u00e5\7n\2\2\u00e5\u00e6\7u\2\2\u00e6\u00e7")
        buf.write("\7g\2\2\u00e7 \3\2\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea")
        buf.write("\7k\2\2\u00ea\u00eb\7n\2\2\u00eb\"\3\2\2\2\u00ec\u00ed")
        buf.write("\7e\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0")
        buf.write("\7u\2\2\u00f0\u00f1\7v\2\2\u00f1$\3\2\2\2\u00f2\u00f3")
        buf.write("\7x\2\2\u00f3\u00f4\7c\2\2\u00f4\u00f5\7t\2\2\u00f5&\3")
        buf.write("\2\2\2\u00f6\u00f7\7e\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9")
        buf.write("\7p\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb\7k\2\2\u00fb\u00fc")
        buf.write("\7p\2\2\u00fc\u00fd\7w\2\2\u00fd\u00fe\7g\2\2\u00fe(\3")
        buf.write("\2\2\2\u00ff\u0100\7d\2\2\u0100\u0101\7t\2\2\u0101\u0102")
        buf.write("\7g\2\2\u0102\u0103\7c\2\2\u0103\u0104\7m\2\2\u0104*\3")
        buf.write("\2\2\2\u0105\u0106\7t\2\2\u0106\u0107\7c\2\2\u0107\u0108")
        buf.write("\7p\2\2\u0108\u0109\7i\2\2\u0109\u010a\7g\2\2\u010a,\3")
        buf.write("\2\2\2\u010b\u010c\7?\2\2\u010c.\3\2\2\2\u010d\u010e\7")
        buf.write("<\2\2\u010e\u010f\7?\2\2\u010f\60\3\2\2\2\u0110\u0111")
        buf.write("\7-\2\2\u0111\62\3\2\2\2\u0112\u0113\7/\2\2\u0113\64\3")
        buf.write("\2\2\2\u0114\u0115\7,\2\2\u0115\66\3\2\2\2\u0116\u0117")
        buf.write("\7\61\2\2\u01178\3\2\2\2\u0118\u0119\7\'\2\2\u0119:\3")
        buf.write("\2\2\2\u011a\u011b\7?\2\2\u011b\u011c\7?\2\2\u011c<\3")
        buf.write("\2\2\2\u011d\u011e\7#\2\2\u011e\u011f\7?\2\2\u011f>\3")
        buf.write("\2\2\2\u0120\u0121\7>\2\2\u0121@\3\2\2\2\u0122\u0123\7")
        buf.write(">\2\2\u0123\u0124\7?\2\2\u0124B\3\2\2\2\u0125\u0126\7")
        buf.write("@\2\2\u0126D\3\2\2\2\u0127\u0128\7@\2\2\u0128\u0129\7")
        buf.write("?\2\2\u0129F\3\2\2\2\u012a\u012b\7(\2\2\u012b\u012c\7")
        buf.write("(\2\2\u012cH\3\2\2\2\u012d\u012e\7~\2\2\u012e\u012f\7")
        buf.write("~\2\2\u012fJ\3\2\2\2\u0130\u0131\7#\2\2\u0131L\3\2\2\2")
        buf.write("\u0132\u0133\7-\2\2\u0133\u0134\7?\2\2\u0134N\3\2\2\2")
        buf.write("\u0135\u0136\7/\2\2\u0136\u0137\7?\2\2\u0137P\3\2\2\2")
        buf.write("\u0138\u0139\7,\2\2\u0139\u013a\7?\2\2\u013aR\3\2\2\2")
        buf.write("\u013b\u013c\7\61\2\2\u013c\u013d\7?\2\2\u013dT\3\2\2")
        buf.write("\2\u013e\u013f\7\'\2\2\u013f\u0140\7?\2\2\u0140V\3\2\2")
        buf.write("\2\u0141\u0142\7\60\2\2\u0142X\3\2\2\2\u0143\u0144\7a")
        buf.write("\2\2\u0144Z\3\2\2\2\u0145\u0146\7*\2\2\u0146\\\3\2\2\2")
        buf.write("\u0147\u0148\7+\2\2\u0148^\3\2\2\2\u0149\u014a\7}\2\2")
        buf.write("\u014a`\3\2\2\2\u014b\u014c\7\177\2\2\u014cb\3\2\2\2\u014d")
        buf.write("\u014e\7]\2\2\u014ed\3\2\2\2\u014f\u0150\7_\2\2\u0150")
        buf.write("f\3\2\2\2\u0151\u0152\7.\2\2\u0152h\3\2\2\2\u0153\u0154")
        buf.write("\7=\2\2\u0154j\3\2\2\2\u0155\u0156\7<\2\2\u0156l\3\2\2")
        buf.write("\2\u0157\u015b\t\2\2\2\u0158\u015a\t\3\2\2\u0159\u0158")
        buf.write("\3\2\2\2\u015a\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015b")
        buf.write("\u015c\3\2\2\2\u015cn\3\2\2\2\u015d\u015b\3\2\2\2\u015e")
        buf.write("\u0163\5q9\2\u015f\u0163\5s:\2\u0160\u0163\5u;\2\u0161")
        buf.write("\u0163\5w<\2\u0162\u015e\3\2\2\2\u0162\u015f\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0162\u0161\3\2\2\2\u0163p\3\2\2\2\u0164")
        buf.write("\u016d\7\62\2\2\u0165\u0169\t\4\2\2\u0166\u0168\t\5\2")
        buf.write("\2\u0167\u0166\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167")
        buf.write("\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016d\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016c\u0164\3\2\2\2\u016c\u0165\3\2\2\2")
        buf.write("\u016dr\3\2\2\2\u016e\u016f\7\62\2\2\u016f\u0171\t\6\2")
        buf.write("\2\u0170\u0172\t\7\2\2\u0171\u0170\3\2\2\2\u0172\u0173")
        buf.write("\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("t\3\2\2\2\u0175\u0176\7\62\2\2\u0176\u0178\t\b\2\2\u0177")
        buf.write("\u0179\t\t\2\2\u0178\u0177\3\2\2\2\u0179\u017a\3\2\2\2")
        buf.write("\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u0183\3")
        buf.write("\2\2\2\u017c\u017e\7\62\2\2\u017d\u017f\t\t\2\2\u017e")
        buf.write("\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u017e\3\2\2\2")
        buf.write("\u0180\u0181\3\2\2\2\u0181\u0183\3\2\2\2\u0182\u0175\3")
        buf.write("\2\2\2\u0182\u017c\3\2\2\2\u0183v\3\2\2\2\u0184\u0185")
        buf.write("\7\62\2\2\u0185\u0187\t\n\2\2\u0186\u0188\t\13\2\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u0187\3\2\2\2")
        buf.write("\u0189\u018a\3\2\2\2\u018ax\3\2\2\2\u018b\u0194\5{>\2")
        buf.write("\u018c\u018e\7\60\2\2\u018d\u018f\5{>\2\u018e\u018d\3")
        buf.write("\2\2\2\u018e\u018f\3\2\2\2\u018f\u0191\3\2\2\2\u0190\u0192")
        buf.write("\5}?\2\u0191\u0190\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0195")
        buf.write("\3\2\2\2\u0193\u0195\5}?\2\u0194\u018c\3\2\2\2\u0194\u0193")
        buf.write("\3\2\2\2\u0195z\3\2\2\2\u0196\u0198\t\5\2\2\u0197\u0196")
        buf.write("\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u0197\3\2\2\2\u0199")
        buf.write("\u019a\3\2\2\2\u019a|\3\2\2\2\u019b\u019d\t\f\2\2\u019c")
        buf.write("\u019e\t\r\2\2\u019d\u019c\3\2\2\2\u019d\u019e\3\2\2\2")
        buf.write("\u019e\u01a0\3\2\2\2\u019f\u01a1\t\5\2\2\u01a0\u019f\3")
        buf.write("\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3")
        buf.write("\3\2\2\2\u01a3~\3\2\2\2\u01a4\u01a9\7$\2\2\u01a5\u01a8")
        buf.write("\5\u0081A\2\u01a6\u01a8\n\16\2\2\u01a7\u01a5\3\2\2\2\u01a7")
        buf.write("\u01a6\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2")
        buf.write("\u01a9\u01aa\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab\u01a9\3")
        buf.write("\2\2\2\u01ac\u01ad\7$\2\2\u01ad\u0080\3\2\2\2\u01ae\u01af")
        buf.write("\7^\2\2\u01af\u01b0\t\17\2\2\u01b0\u0082\3\2\2\2\u01b1")
        buf.write("\u01b2\7\61\2\2\u01b2\u01b3\7,\2\2\u01b3\u01b8\3\2\2\2")
        buf.write("\u01b4\u01b7\5\u0083B\2\u01b5\u01b7\13\2\2\2\u01b6\u01b4")
        buf.write("\3\2\2\2\u01b6\u01b5\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01bb\3\2\2\2")
        buf.write("\u01ba\u01b8\3\2\2\2\u01bb\u01bc\7,\2\2\u01bc\u01bd\7")
        buf.write("\61\2\2\u01bd\u01be\3\2\2\2\u01be\u01bf\bB\2\2\u01bf\u0084")
        buf.write("\3\2\2\2\u01c0\u01c1\7\61\2\2\u01c1\u01c2\7\61\2\2\u01c2")
        buf.write("\u01c6\3\2\2\2\u01c3\u01c5\n\20\2\2\u01c4\u01c3\3\2\2")
        buf.write("\2\u01c5\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7")
        buf.write("\3\2\2\2\u01c7\u01c9\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9")
        buf.write("\u01ca\bC\2\2\u01ca\u0086\3\2\2\2\u01cb\u01cd\t\21\2\2")
        buf.write("\u01cc\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cc\3")
        buf.write("\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1")
        buf.write("\bD\2\2\u01d1\u0088\3\2\2\2\u01d2\u01d3\7\f\2\2\u01d3")
        buf.write("\u01d4\bE\3\2\u01d4\u008a\3\2\2\2\u01d5\u01da\7$\2\2\u01d6")
        buf.write("\u01d9\5\u0081A\2\u01d7\u01d9\n\16\2\2\u01d8\u01d6\3\2")
        buf.write("\2\2\u01d8\u01d7\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01d8")
        buf.write("\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u008c\3\2\2\2\u01dc")
        buf.write("\u01da\3\2\2\2\u01dd\u01e2\7$\2\2\u01de\u01e1\5\u0081")
        buf.write("A\2\u01df\u01e1\n\16\2\2\u01e0\u01de\3\2\2\2\u01e0\u01df")
        buf.write("\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2")
        buf.write("\u01e3\3\2\2\2\u01e3\u01e5\3\2\2\2\u01e4\u01e2\3\2\2\2")
        buf.write("\u01e5\u01e6\7^\2\2\u01e6\u01e7\n\17\2\2\u01e7\u008e\3")
        buf.write("\2\2\2\u01e8\u01e9\13\2\2\2\u01e9\u0090\3\2\2\2\34\2\u015b")
        buf.write("\u0162\u0169\u016c\u0173\u017a\u0180\u0182\u0189\u018e")
        buf.write("\u0191\u0194\u0199\u019d\u01a2\u01a7\u01a9\u01b6\u01b8")
        buf.write("\u01c6\u01ce\u01d8\u01da\u01e0\u01e2\4\b\2\2\3E\2")
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
    BLOCK_COMMENT = 58
    LINE_COMMENT = 59
    WS = 60
    NEWLINE = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    ERROR_CHAR = 64

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
            "BLOCK_COMMENT", "LINE_COMMENT", "WS", "NEWLINE", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
                  "EXPONENT", "STRING_LIT", "ESC_SEQ", "BLOCK_COMMENT", 
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
            actions[67] = self.NEWLINE_action 
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

     


