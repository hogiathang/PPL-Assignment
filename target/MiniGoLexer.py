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
        buf.write("\u01f3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3")
        buf.write("\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3")
        buf.write("-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\78\u015e")
        buf.write("\n8\f8\168\u0161\138\39\39\39\39\59\u0167\n9\3:\3:\3:")
        buf.write("\7:\u016c\n:\f:\16:\u016f\13:\5:\u0171\n:\3;\3;\3;\6;")
        buf.write("\u0176\n;\r;\16;\u0177\3<\3<\3<\6<\u017d\n<\r<\16<\u017e")
        buf.write("\3<\3<\6<\u0183\n<\r<\16<\u0184\5<\u0187\n<\3=\3=\3=\6")
        buf.write("=\u018c\n=\r=\16=\u018d\3>\3>\3>\5>\u0193\n>\3>\5>\u0196")
        buf.write("\n>\3>\5>\u0199\n>\3?\6?\u019c\n?\r?\16?\u019d\3@\3@\5")
        buf.write("@\u01a2\n@\3@\6@\u01a5\n@\r@\16@\u01a6\3A\3A\3A\7A\u01ac")
        buf.write("\nA\fA\16A\u01af\13A\3A\3A\3A\3B\3B\3B\3C\3C\5C\u01b9")
        buf.write("\nC\3D\3D\3D\3D\3D\7D\u01c0\nD\fD\16D\u01c3\13D\3D\3D")
        buf.write("\3D\3D\3D\3E\3E\3E\3E\7E\u01ce\nE\fE\16E\u01d1\13E\3E")
        buf.write("\3E\3F\6F\u01d6\nF\rF\16F\u01d7\3F\3F\3G\3G\3G\7G\u01df")
        buf.write("\nG\fG\16G\u01e2\13G\3G\3G\3H\3H\3H\7H\u01e9\nH\fH\16")
        buf.write("H\u01ec\13H\3H\3H\3H\3H\3I\3I\3\u01c1\2J\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q:s\2u\2w\2y\2{;}\2\177")
        buf.write("\2\u0081<\u0083\2\u0085=\u0087>\u0089?\u008b@\u008dA\u008f")
        buf.write("B\u0091C\3\2\22\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2")
        buf.write("\62;\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62")
        buf.write(";CHch\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\7\2$$^^ppttvv")
        buf.write("\4\2\f\f\17\17\5\2\13\f\16\17\"\"\2\u0207\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2{")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5\u0098\3\2\2")
        buf.write("\2\7\u009a\3\2\2\2\t\u009d\3\2\2\2\13\u00a2\3\2\2\2\r")
        buf.write("\u00a6\3\2\2\2\17\u00ad\3\2\2\2\21\u00b2\3\2\2\2\23\u00b7")
        buf.write("\3\2\2\2\25\u00be\3\2\2\2\27\u00c8\3\2\2\2\31\u00cf\3")
        buf.write("\2\2\2\33\u00d3\3\2\2\2\35\u00d9\3\2\2\2\37\u00e1\3\2")
        buf.write("\2\2!\u00e6\3\2\2\2#\u00ec\3\2\2\2%\u00f0\3\2\2\2\'\u00f6")
        buf.write("\3\2\2\2)\u00fa\3\2\2\2+\u0103\3\2\2\2-\u0109\3\2\2\2")
        buf.write("/\u010f\3\2\2\2\61\u0111\3\2\2\2\63\u0114\3\2\2\2\65\u0116")
        buf.write("\3\2\2\2\67\u0118\3\2\2\29\u011a\3\2\2\2;\u011c\3\2\2")
        buf.write("\2=\u011e\3\2\2\2?\u0121\3\2\2\2A\u0124\3\2\2\2C\u0126")
        buf.write("\3\2\2\2E\u0129\3\2\2\2G\u012b\3\2\2\2I\u012e\3\2\2\2")
        buf.write("K\u0131\3\2\2\2M\u0134\3\2\2\2O\u0136\3\2\2\2Q\u0139\3")
        buf.write("\2\2\2S\u013c\3\2\2\2U\u013f\3\2\2\2W\u0142\3\2\2\2Y\u0145")
        buf.write("\3\2\2\2[\u0147\3\2\2\2]\u0149\3\2\2\2_\u014b\3\2\2\2")
        buf.write("a\u014d\3\2\2\2c\u014f\3\2\2\2e\u0151\3\2\2\2g\u0153\3")
        buf.write("\2\2\2i\u0155\3\2\2\2k\u0157\3\2\2\2m\u0159\3\2\2\2o\u015b")
        buf.write("\3\2\2\2q\u0166\3\2\2\2s\u0170\3\2\2\2u\u0172\3\2\2\2")
        buf.write("w\u0186\3\2\2\2y\u0188\3\2\2\2{\u018f\3\2\2\2}\u019b\3")
        buf.write("\2\2\2\177\u019f\3\2\2\2\u0081\u01a8\3\2\2\2\u0083\u01b3")
        buf.write("\3\2\2\2\u0085\u01b8\3\2\2\2\u0087\u01ba\3\2\2\2\u0089")
        buf.write("\u01c9\3\2\2\2\u008b\u01d5\3\2\2\2\u008d\u01db\3\2\2\2")
        buf.write("\u008f\u01e5\3\2\2\2\u0091\u01f1\3\2\2\2\u0093\u0094\7")
        buf.write("o\2\2\u0094\u0095\7c\2\2\u0095\u0096\7k\2\2\u0096\u0097")
        buf.write("\7p\2\2\u0097\4\3\2\2\2\u0098\u0099\7\f\2\2\u0099\6\3")
        buf.write("\2\2\2\u009a\u009b\7k\2\2\u009b\u009c\7h\2\2\u009c\b\3")
        buf.write("\2\2\2\u009d\u009e\7g\2\2\u009e\u009f\7n\2\2\u009f\u00a0")
        buf.write("\7u\2\2\u00a0\u00a1\7g\2\2\u00a1\n\3\2\2\2\u00a2\u00a3")
        buf.write("\7h\2\2\u00a3\u00a4\7q\2\2\u00a4\u00a5\7t\2\2\u00a5\f")
        buf.write("\3\2\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9")
        buf.write("\7v\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab\7t\2\2\u00ab\u00ac")
        buf.write("\7p\2\2\u00ac\16\3\2\2\2\u00ad\u00ae\7h\2\2\u00ae\u00af")
        buf.write("\7w\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1\7e\2\2\u00b1\20")
        buf.write("\3\2\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7{\2\2\u00b4\u00b5")
        buf.write("\7r\2\2\u00b5\u00b6\7g\2\2\u00b6\22\3\2\2\2\u00b7\u00b8")
        buf.write("\7u\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb")
        buf.write("\7w\2\2\u00bb\u00bc\7e\2\2\u00bc\u00bd\7v\2\2\u00bd\24")
        buf.write("\3\2\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3\7t\2\2\u00c3\u00c4")
        buf.write("\7h\2\2\u00c4\u00c5\7c\2\2\u00c5\u00c6\7e\2\2\u00c6\u00c7")
        buf.write("\7g\2\2\u00c7\26\3\2\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca")
        buf.write("\7v\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd")
        buf.write("\7p\2\2\u00cd\u00ce\7i\2\2\u00ce\30\3\2\2\2\u00cf\u00d0")
        buf.write("\7k\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2\7v\2\2\u00d2\32")
        buf.write("\3\2\2\2\u00d3\u00d4\7h\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6")
        buf.write("\7q\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8\7v\2\2\u00d8\34")
        buf.write("\3\2\2\2\u00d9\u00da\7d\2\2\u00da\u00db\7q\2\2\u00db\u00dc")
        buf.write("\7q\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de\7g\2\2\u00de\u00df")
        buf.write("\7c\2\2\u00df\u00e0\7p\2\2\u00e0\36\3\2\2\2\u00e1\u00e2")
        buf.write("\7v\2\2\u00e2\u00e3\7t\2\2\u00e3\u00e4\7w\2\2\u00e4\u00e5")
        buf.write("\7g\2\2\u00e5 \3\2\2\2\u00e6\u00e7\7h\2\2\u00e7\u00e8")
        buf.write("\7c\2\2\u00e8\u00e9\7n\2\2\u00e9\u00ea\7u\2\2\u00ea\u00eb")
        buf.write("\7g\2\2\u00eb\"\3\2\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee")
        buf.write("\7k\2\2\u00ee\u00ef\7n\2\2\u00ef$\3\2\2\2\u00f0\u00f1")
        buf.write("\7e\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4")
        buf.write("\7u\2\2\u00f4\u00f5\7v\2\2\u00f5&\3\2\2\2\u00f6\u00f7")
        buf.write("\7x\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9\7t\2\2\u00f9(\3")
        buf.write("\2\2\2\u00fa\u00fb\7e\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd")
        buf.write("\7p\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100")
        buf.write("\7p\2\2\u0100\u0101\7w\2\2\u0101\u0102\7g\2\2\u0102*\3")
        buf.write("\2\2\2\u0103\u0104\7d\2\2\u0104\u0105\7t\2\2\u0105\u0106")
        buf.write("\7g\2\2\u0106\u0107\7c\2\2\u0107\u0108\7m\2\2\u0108,\3")
        buf.write("\2\2\2\u0109\u010a\7t\2\2\u010a\u010b\7c\2\2\u010b\u010c")
        buf.write("\7p\2\2\u010c\u010d\7i\2\2\u010d\u010e\7g\2\2\u010e.\3")
        buf.write("\2\2\2\u010f\u0110\7?\2\2\u0110\60\3\2\2\2\u0111\u0112")
        buf.write("\7<\2\2\u0112\u0113\7?\2\2\u0113\62\3\2\2\2\u0114\u0115")
        buf.write("\7-\2\2\u0115\64\3\2\2\2\u0116\u0117\7/\2\2\u0117\66\3")
        buf.write("\2\2\2\u0118\u0119\7,\2\2\u01198\3\2\2\2\u011a\u011b\7")
        buf.write("\61\2\2\u011b:\3\2\2\2\u011c\u011d\7\'\2\2\u011d<\3\2")
        buf.write("\2\2\u011e\u011f\7?\2\2\u011f\u0120\7?\2\2\u0120>\3\2")
        buf.write("\2\2\u0121\u0122\7#\2\2\u0122\u0123\7?\2\2\u0123@\3\2")
        buf.write("\2\2\u0124\u0125\7>\2\2\u0125B\3\2\2\2\u0126\u0127\7>")
        buf.write("\2\2\u0127\u0128\7?\2\2\u0128D\3\2\2\2\u0129\u012a\7@")
        buf.write("\2\2\u012aF\3\2\2\2\u012b\u012c\7@\2\2\u012c\u012d\7?")
        buf.write("\2\2\u012dH\3\2\2\2\u012e\u012f\7(\2\2\u012f\u0130\7(")
        buf.write("\2\2\u0130J\3\2\2\2\u0131\u0132\7~\2\2\u0132\u0133\7~")
        buf.write("\2\2\u0133L\3\2\2\2\u0134\u0135\7#\2\2\u0135N\3\2\2\2")
        buf.write("\u0136\u0137\7-\2\2\u0137\u0138\7?\2\2\u0138P\3\2\2\2")
        buf.write("\u0139\u013a\7/\2\2\u013a\u013b\7?\2\2\u013bR\3\2\2\2")
        buf.write("\u013c\u013d\7,\2\2\u013d\u013e\7?\2\2\u013eT\3\2\2\2")
        buf.write("\u013f\u0140\7\61\2\2\u0140\u0141\7?\2\2\u0141V\3\2\2")
        buf.write("\2\u0142\u0143\7\'\2\2\u0143\u0144\7?\2\2\u0144X\3\2\2")
        buf.write("\2\u0145\u0146\7\60\2\2\u0146Z\3\2\2\2\u0147\u0148\7a")
        buf.write("\2\2\u0148\\\3\2\2\2\u0149\u014a\7*\2\2\u014a^\3\2\2\2")
        buf.write("\u014b\u014c\7+\2\2\u014c`\3\2\2\2\u014d\u014e\7}\2\2")
        buf.write("\u014eb\3\2\2\2\u014f\u0150\7\177\2\2\u0150d\3\2\2\2\u0151")
        buf.write("\u0152\7]\2\2\u0152f\3\2\2\2\u0153\u0154\7_\2\2\u0154")
        buf.write("h\3\2\2\2\u0155\u0156\7.\2\2\u0156j\3\2\2\2\u0157\u0158")
        buf.write("\7=\2\2\u0158l\3\2\2\2\u0159\u015a\7<\2\2\u015an\3\2\2")
        buf.write("\2\u015b\u015f\t\2\2\2\u015c\u015e\t\3\2\2\u015d\u015c")
        buf.write("\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u015d\3\2\2\2\u015f")
        buf.write("\u0160\3\2\2\2\u0160p\3\2\2\2\u0161\u015f\3\2\2\2\u0162")
        buf.write("\u0167\5s:\2\u0163\u0167\5u;\2\u0164\u0167\5w<\2\u0165")
        buf.write("\u0167\5y=\2\u0166\u0162\3\2\2\2\u0166\u0163\3\2\2\2\u0166")
        buf.write("\u0164\3\2\2\2\u0166\u0165\3\2\2\2\u0167r\3\2\2\2\u0168")
        buf.write("\u0171\7\62\2\2\u0169\u016d\t\4\2\2\u016a\u016c\t\5\2")
        buf.write("\2\u016b\u016a\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b")
        buf.write("\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u0171\3\2\2\2\u016f")
        buf.write("\u016d\3\2\2\2\u0170\u0168\3\2\2\2\u0170\u0169\3\2\2\2")
        buf.write("\u0171t\3\2\2\2\u0172\u0173\7\62\2\2\u0173\u0175\t\6\2")
        buf.write("\2\u0174\u0176\t\7\2\2\u0175\u0174\3\2\2\2\u0176\u0177")
        buf.write("\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178")
        buf.write("v\3\2\2\2\u0179\u017a\7\62\2\2\u017a\u017c\t\b\2\2\u017b")
        buf.write("\u017d\t\t\2\2\u017c\u017b\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0187\3")
        buf.write("\2\2\2\u0180\u0182\7\62\2\2\u0181\u0183\t\t\2\2\u0182")
        buf.write("\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0182\3\2\2\2")
        buf.write("\u0184\u0185\3\2\2\2\u0185\u0187\3\2\2\2\u0186\u0179\3")
        buf.write("\2\2\2\u0186\u0180\3\2\2\2\u0187x\3\2\2\2\u0188\u0189")
        buf.write("\7\62\2\2\u0189\u018b\t\n\2\2\u018a\u018c\t\13\2\2\u018b")
        buf.write("\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018b\3\2\2\2")
        buf.write("\u018d\u018e\3\2\2\2\u018ez\3\2\2\2\u018f\u0198\5}?\2")
        buf.write("\u0190\u0192\7\60\2\2\u0191\u0193\5}?\2\u0192\u0191\3")
        buf.write("\2\2\2\u0192\u0193\3\2\2\2\u0193\u0195\3\2\2\2\u0194\u0196")
        buf.write("\5\177@\2\u0195\u0194\3\2\2\2\u0195\u0196\3\2\2\2\u0196")
        buf.write("\u0199\3\2\2\2\u0197\u0199\5\177@\2\u0198\u0190\3\2\2")
        buf.write("\2\u0198\u0197\3\2\2\2\u0199|\3\2\2\2\u019a\u019c\t\5")
        buf.write("\2\2\u019b\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019b")
        buf.write("\3\2\2\2\u019d\u019e\3\2\2\2\u019e~\3\2\2\2\u019f\u01a1")
        buf.write("\t\f\2\2\u01a0\u01a2\t\r\2\2\u01a1\u01a0\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u01a4\3\2\2\2\u01a3\u01a5\t\5\2\2")
        buf.write("\u01a4\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a4\3")
        buf.write("\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u0080\3\2\2\2\u01a8\u01ad")
        buf.write("\7$\2\2\u01a9\u01ac\5\u0083B\2\u01aa\u01ac\n\16\2\2\u01ab")
        buf.write("\u01a9\3\2\2\2\u01ab\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2")
        buf.write("\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01b0\3")
        buf.write("\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b1\7$\2\2\u01b1\u01b2")
        buf.write("\bA\2\2\u01b2\u0082\3\2\2\2\u01b3\u01b4\7^\2\2\u01b4\u01b5")
        buf.write("\t\17\2\2\u01b5\u0084\3\2\2\2\u01b6\u01b9\5\37\20\2\u01b7")
        buf.write("\u01b9\5!\21\2\u01b8\u01b6\3\2\2\2\u01b8\u01b7\3\2\2\2")
        buf.write("\u01b9\u0086\3\2\2\2\u01ba\u01bb\7\61\2\2\u01bb\u01bc")
        buf.write("\7,\2\2\u01bc\u01c1\3\2\2\2\u01bd\u01c0\5\u0087D\2\u01be")
        buf.write("\u01c0\13\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01be\3\2\2")
        buf.write("\2\u01c0\u01c3\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c1\u01bf")
        buf.write("\3\2\2\2\u01c2\u01c4\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4")
        buf.write("\u01c5\7,\2\2\u01c5\u01c6\7\61\2\2\u01c6\u01c7\3\2\2\2")
        buf.write("\u01c7\u01c8\bD\3\2\u01c8\u0088\3\2\2\2\u01c9\u01ca\7")
        buf.write("\61\2\2\u01ca\u01cb\7\61\2\2\u01cb\u01cf\3\2\2\2\u01cc")
        buf.write("\u01ce\n\20\2\2\u01cd\u01cc\3\2\2\2\u01ce\u01d1\3\2\2")
        buf.write("\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d2")
        buf.write("\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d2\u01d3\bE\3\2\u01d3")
        buf.write("\u008a\3\2\2\2\u01d4\u01d6\t\21\2\2\u01d5\u01d4\3\2\2")
        buf.write("\2\u01d6\u01d7\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8")
        buf.write("\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\bF\3\2\u01da")
        buf.write("\u008c\3\2\2\2\u01db\u01e0\7$\2\2\u01dc\u01df\5\u0083")
        buf.write("B\2\u01dd\u01df\n\16\2\2\u01de\u01dc\3\2\2\2\u01de\u01dd")
        buf.write("\3\2\2\2\u01df\u01e2\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0")
        buf.write("\u01e1\3\2\2\2\u01e1\u01e3\3\2\2\2\u01e2\u01e0\3\2\2\2")
        buf.write("\u01e3\u01e4\bG\4\2\u01e4\u008e\3\2\2\2\u01e5\u01ea\7")
        buf.write("$\2\2\u01e6\u01e9\5\u0083B\2\u01e7\u01e9\n\16\2\2\u01e8")
        buf.write("\u01e6\3\2\2\2\u01e8\u01e7\3\2\2\2\u01e9\u01ec\3\2\2\2")
        buf.write("\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ed\3")
        buf.write("\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01ee\7^\2\2\u01ee\u01ef")
        buf.write("\n\17\2\2\u01ef\u01f0\bH\5\2\u01f0\u0090\3\2\2\2\u01f1")
        buf.write("\u01f2\13\2\2\2\u01f2\u0092\3\2\2\2\35\2\u015f\u0166\u016d")
        buf.write("\u0170\u0177\u017e\u0184\u0186\u018d\u0192\u0195\u0198")
        buf.write("\u019d\u01a1\u01a6\u01ab\u01ad\u01b8\u01bf\u01c1\u01cf")
        buf.write("\u01d7\u01de\u01e0\u01e8\u01ea\6\3A\2\b\2\2\3G\3\3H\4")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    IF = 3
    ELSE = 4
    FOR = 5
    RETURN = 6
    FUNC = 7
    TYPE = 8
    STRUCT = 9
    INTERFACE = 10
    STRING = 11
    INT = 12
    FLOAT = 13
    BOOLEAN = 14
    TRUE = 15
    FALSE = 16
    NIL = 17
    CONST = 18
    VAR = 19
    CONTINUE = 20
    BREAK = 21
    RANGE = 22
    ASSIGN = 23
    DECLARE = 24
    PLUS = 25
    MINUS = 26
    MUL = 27
    DIV = 28
    MOD = 29
    EQ = 30
    NEQ = 31
    LT = 32
    LEQ = 33
    GT = 34
    GEQ = 35
    AND = 36
    OR = 37
    NOT = 38
    PLUS_ASSIGN = 39
    MINUS_ASSIGN = 40
    MUL_ASSIGN = 41
    DIV_ASSIGN = 42
    MOD_ASSIGN = 43
    DOT = 44
    BLANK = 45
    LPAREN = 46
    RPAREN = 47
    LBRACE = 48
    RBRACE = 49
    LBRACKET = 50
    RBRACKET = 51
    COMMA = 52
    SEMI = 53
    COLON = 54
    IDENTIFIER = 55
    INT_LIT = 56
    FLOAT_LIT = 57
    STRING_LIT = 58
    BOOL_LIT = 59
    BLOCK_COMMENT = 60
    LINE_COMMENT = 61
    WS = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'\n'", "'if'", "'else'", "'for'", "'return'", "'func'", 
            "'type'", "'struct'", "'interface'", "'string'", "'int'", "'float'", 
            "'boolean'", "'true'", "'false'", "'nil'", "'const'", "'var'", 
            "'continue'", "'break'", "'range'", "'='", "':='", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'&&'", "'||'", "'!'", "'+='", "'-='", "'*='", "'/='", "'%='", 
            "'.'", "'_'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", 
            "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "TRUE", "FALSE", "NIL", 
            "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "ASSIGN", "DECLARE", 
            "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQ", "NEQ", "LT", "LEQ", 
            "GT", "GEQ", "AND", "OR", "NOT", "PLUS_ASSIGN", "MINUS_ASSIGN", 
            "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "BLANK", "LPAREN", 
            "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "COMMA", 
            "SEMI", "COLON", "IDENTIFIER", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
            "BOOL_LIT", "BLOCK_COMMENT", "LINE_COMMENT", "WS", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                  "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                  "BOOLEAN", "TRUE", "FALSE", "NIL", "CONST", "VAR", "CONTINUE", 
                  "BREAK", "RANGE", "ASSIGN", "DECLARE", "PLUS", "MINUS", 
                  "MUL", "DIV", "MOD", "EQ", "NEQ", "LT", "LEQ", "GT", "GEQ", 
                  "AND", "OR", "NOT", "PLUS_ASSIGN", "MINUS_ASSIGN", "MUL_ASSIGN", 
                  "DIV_ASSIGN", "MOD_ASSIGN", "DOT", "BLANK", "LPAREN", 
                  "RPAREN", "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", 
                  "COMMA", "SEMI", "COLON", "IDENTIFIER", "INT_LIT", "DEC_LIT", 
                  "BIN_LIT", "OCT_LIT", "HEX_LIT", "FLOAT_LIT", "DEC_PART", 
                  "EXPONENT", "STRING_LIT", "ESC_SEQ", "BOOL_LIT", "BLOCK_COMMENT", 
                  "LINE_COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
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
            actions[63] = self.STRING_LIT_action 
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
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:]
     


