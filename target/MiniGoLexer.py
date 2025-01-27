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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
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
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0103")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\25\3\25\7\25\u010b\n\25\f")
        buf.write("\25\16\25\u010e\13\25\3\26\3\26\3\27\3\27\3\30\3\30\3")
        buf.write("\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\3\66\5\66\u0161\n\66\3\67\3")
        buf.write("\67\38\38\78\u0167\n8\f8\168\u016a\138\39\39\39\79\u016f")
        buf.write("\n9\f9\169\u0172\139\3:\3:\3:\7:\u0177\n:\f:\16:\u017a")
        buf.write("\13:\3;\3;\3;\7;\u017f\n;\f;\16;\u0182\13;\3<\3<\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\3<\5<\u018e\n<\3=\6=\u0191\n=\r=\16=")
        buf.write("\u0192\3>\3>\7>\u0197\n>\f>\16>\u019a\13>\3?\3?\5?\u019e")
        buf.write("\n?\3?\6?\u01a1\n?\r?\16?\u01a2\3@\3@\3@\7@\u01a8\n@\f")
        buf.write("@\16@\u01ab\13@\3@\3@\3A\3A\3A\3B\5B\u01b3\nB\3B\3B\3")
        buf.write("B\3B\3C\6C\u01ba\nC\rC\16C\u01bb\3C\3C\3D\3D\3D\3D\7D")
        buf.write("\u01c4\nD\fD\16D\u01c7\13D\3D\3D\3E\3E\3E\3E\3F\3F\3F")
        buf.write("\3F\3F\3F\3F\7F\u01d6\nF\fF\16F\u01d9\13F\3F\3F\3F\3G")
        buf.write("\3G\3H\3H\3I\3I\2\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\67m\2o\2q\2s\2u\2w8y\2{\2}\2\1779\u0081\2\u0083")
        buf.write(":\u0085;\u0087<\u0089=\u008b\2\u008d>\u008f?\u0091@\3")
        buf.write("\2\24\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2ZZ")
        buf.write("zz\5\2\62;CHch\4\2QQqq\3\2\629\4\2DDdd\3\2\62\63\4\2G")
        buf.write("Ggg\4\2--//\4\2$$^^\7\2$$^^ppttvv\5\2\13\13\16\17\"\"")
        buf.write("\4\2\f\f\17\17\3\2,,\3\2\61\61\2\u01f0\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2w\3\2\2\2\2\177\3\2\2\2\2\u0083\3\2\2\2")
        buf.write("\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0093\3\2\2")
        buf.write("\2\5\u0096\3\2\2\2\7\u009b\3\2\2\2\t\u009f\3\2\2\2\13")
        buf.write("\u00a6\3\2\2\2\r\u00ab\3\2\2\2\17\u00b0\3\2\2\2\21\u00b7")
        buf.write("\3\2\2\2\23\u00c1\3\2\2\2\25\u00c9\3\2\2\2\27\u00cf\3")
        buf.write("\2\2\2\31\u00d3\3\2\2\2\33\u00d7\3\2\2\2\35\u00dd\3\2")
        buf.write("\2\2\37\u00e4\3\2\2\2!\u00ed\3\2\2\2#\u00f3\3\2\2\2%\u0102")
        buf.write("\3\2\2\2\'\u0104\3\2\2\2)\u0108\3\2\2\2+\u010f\3\2\2\2")
        buf.write("-\u0111\3\2\2\2/\u0113\3\2\2\2\61\u0115\3\2\2\2\63\u0117")
        buf.write("\3\2\2\2\65\u0119\3\2\2\2\67\u011c\3\2\2\29\u011f\3\2")
        buf.write("\2\2;\u0121\3\2\2\2=\u0124\3\2\2\2?\u0126\3\2\2\2A\u0129")
        buf.write("\3\2\2\2C\u012c\3\2\2\2E\u012f\3\2\2\2G\u0131\3\2\2\2")
        buf.write("I\u0133\3\2\2\2K\u0136\3\2\2\2M\u0139\3\2\2\2O\u013c\3")
        buf.write("\2\2\2Q\u013f\3\2\2\2S\u0142\3\2\2\2U\u0145\3\2\2\2W\u0147")
        buf.write("\3\2\2\2Y\u0149\3\2\2\2[\u014b\3\2\2\2]\u014d\3\2\2\2")
        buf.write("_\u014f\3\2\2\2a\u0151\3\2\2\2c\u0153\3\2\2\2e\u0155\3")
        buf.write("\2\2\2g\u0157\3\2\2\2i\u0159\3\2\2\2k\u0160\3\2\2\2m\u0162")
        buf.write("\3\2\2\2o\u0164\3\2\2\2q\u016b\3\2\2\2s\u0173\3\2\2\2")
        buf.write("u\u017b\3\2\2\2w\u018d\3\2\2\2y\u0190\3\2\2\2{\u0194\3")
        buf.write("\2\2\2}\u019b\3\2\2\2\177\u01a4\3\2\2\2\u0081\u01ae\3")
        buf.write("\2\2\2\u0083\u01b2\3\2\2\2\u0085\u01b9\3\2\2\2\u0087\u01bf")
        buf.write("\3\2\2\2\u0089\u01ca\3\2\2\2\u008b\u01ce\3\2\2\2\u008d")
        buf.write("\u01dd\3\2\2\2\u008f\u01df\3\2\2\2\u0091\u01e1\3\2\2\2")
        buf.write("\u0093\u0094\7k\2\2\u0094\u0095\7h\2\2\u0095\4\3\2\2\2")
        buf.write("\u0096\u0097\7g\2\2\u0097\u0098\7n\2\2\u0098\u0099\7u")
        buf.write("\2\2\u0099\u009a\7g\2\2\u009a\6\3\2\2\2\u009b\u009c\7")
        buf.write("h\2\2\u009c\u009d\7q\2\2\u009d\u009e\7t\2\2\u009e\b\3")
        buf.write("\2\2\2\u009f\u00a0\7t\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2")
        buf.write("\7v\2\2\u00a2\u00a3\7w\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5")
        buf.write("\7p\2\2\u00a5\n\3\2\2\2\u00a6\u00a7\7h\2\2\u00a7\u00a8")
        buf.write("\7w\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa\7e\2\2\u00aa\f")
        buf.write("\3\2\2\2\u00ab\u00ac\7v\2\2\u00ac\u00ad\7{\2\2\u00ad\u00ae")
        buf.write("\7r\2\2\u00ae\u00af\7g\2\2\u00af\16\3\2\2\2\u00b0\u00b1")
        buf.write("\7u\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4")
        buf.write("\7w\2\2\u00b4\u00b5\7e\2\2\u00b5\u00b6\7v\2\2\u00b6\20")
        buf.write("\3\2\2\2\u00b7\u00b8\7k\2\2\u00b8\u00b9\7p\2\2\u00b9\u00ba")
        buf.write("\7v\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd")
        buf.write("\7h\2\2\u00bd\u00be\7c\2\2\u00be\u00bf\7e\2\2\u00bf\u00c0")
        buf.write("\7g\2\2\u00c0\22\3\2\2\2\u00c1\u00c2\7d\2\2\u00c2\u00c3")
        buf.write("\7q\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5\7n\2\2\u00c5\u00c6")
        buf.write("\7g\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8\7p\2\2\u00c8\24")
        buf.write("\3\2\2\2\u00c9\u00ca\7e\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\u00cd\7u\2\2\u00cd\u00ce\7v\2\2\u00ce\26")
        buf.write("\3\2\2\2\u00cf\u00d0\7x\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2")
        buf.write("\7t\2\2\u00d2\30\3\2\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5")
        buf.write("\7p\2\2\u00d5\u00d6\7v\2\2\u00d6\32\3\2\2\2\u00d7\u00d8")
        buf.write("\7h\2\2\u00d8\u00d9\7n\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7c\2\2\u00db\u00dc\7v\2\2\u00dc\34\3\2\2\2\u00dd\u00de")
        buf.write("\7u\2\2\u00de\u00df\7v\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1")
        buf.write("\7k\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3\7i\2\2\u00e3\36")
        buf.write("\3\2\2\2\u00e4\u00e5\7e\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7")
        buf.write("\7p\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea")
        buf.write("\7p\2\2\u00ea\u00eb\7w\2\2\u00eb\u00ec\7g\2\2\u00ec \3")
        buf.write("\2\2\2\u00ed\u00ee\7d\2\2\u00ee\u00ef\7t\2\2\u00ef\u00f0")
        buf.write("\7g\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2\7m\2\2\u00f2\"")
        buf.write("\3\2\2\2\u00f3\u00f4\7t\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6")
        buf.write("\7p\2\2\u00f6\u00f7\7i\2\2\u00f7\u00f8\7g\2\2\u00f8$\3")
        buf.write("\2\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7w\2\2\u00fc\u0103\7g\2\2\u00fd\u00fe\7h\2\2\u00fe\u00ff")
        buf.write("\7c\2\2\u00ff\u0100\7n\2\2\u0100\u0101\7u\2\2\u0101\u0103")
        buf.write("\7g\2\2\u0102\u00f9\3\2\2\2\u0102\u00fd\3\2\2\2\u0103")
        buf.write("&\3\2\2\2\u0104\u0105\7p\2\2\u0105\u0106\7k\2\2\u0106")
        buf.write("\u0107\7n\2\2\u0107(\3\2\2\2\u0108\u010c\t\2\2\2\u0109")
        buf.write("\u010b\t\3\2\2\u010a\u0109\3\2\2\2\u010b\u010e\3\2\2\2")
        buf.write("\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d*\3\2\2")
        buf.write("\2\u010e\u010c\3\2\2\2\u010f\u0110\7-\2\2\u0110,\3\2\2")
        buf.write("\2\u0111\u0112\7/\2\2\u0112.\3\2\2\2\u0113\u0114\7,\2")
        buf.write("\2\u0114\60\3\2\2\2\u0115\u0116\7\61\2\2\u0116\62\3\2")
        buf.write("\2\2\u0117\u0118\7\'\2\2\u0118\64\3\2\2\2\u0119\u011a")
        buf.write("\7?\2\2\u011a\u011b\7?\2\2\u011b\66\3\2\2\2\u011c\u011d")
        buf.write("\7#\2\2\u011d\u011e\7?\2\2\u011e8\3\2\2\2\u011f\u0120")
        buf.write("\7>\2\2\u0120:\3\2\2\2\u0121\u0122\7>\2\2\u0122\u0123")
        buf.write("\7?\2\2\u0123<\3\2\2\2\u0124\u0125\7@\2\2\u0125>\3\2\2")
        buf.write("\2\u0126\u0127\7@\2\2\u0127\u0128\7?\2\2\u0128@\3\2\2")
        buf.write("\2\u0129\u012a\7(\2\2\u012a\u012b\7(\2\2\u012bB\3\2\2")
        buf.write("\2\u012c\u012d\7~\2\2\u012d\u012e\7~\2\2\u012eD\3\2\2")
        buf.write("\2\u012f\u0130\7#\2\2\u0130F\3\2\2\2\u0131\u0132\7?\2")
        buf.write("\2\u0132H\3\2\2\2\u0133\u0134\7<\2\2\u0134\u0135\7?\2")
        buf.write("\2\u0135J\3\2\2\2\u0136\u0137\7-\2\2\u0137\u0138\7?\2")
        buf.write("\2\u0138L\3\2\2\2\u0139\u013a\7/\2\2\u013a\u013b\7?\2")
        buf.write("\2\u013bN\3\2\2\2\u013c\u013d\7,\2\2\u013d\u013e\7?\2")
        buf.write("\2\u013eP\3\2\2\2\u013f\u0140\7\61\2\2\u0140\u0141\7?")
        buf.write("\2\2\u0141R\3\2\2\2\u0142\u0143\7\'\2\2\u0143\u0144\7")
        buf.write("?\2\2\u0144T\3\2\2\2\u0145\u0146\7\60\2\2\u0146V\3\2\2")
        buf.write("\2\u0147\u0148\7<\2\2\u0148X\3\2\2\2\u0149\u014a\7a\2")
        buf.write("\2\u014aZ\3\2\2\2\u014b\u014c\7*\2\2\u014c\\\3\2\2\2\u014d")
        buf.write("\u014e\7+\2\2\u014e^\3\2\2\2\u014f\u0150\7}\2\2\u0150")
        buf.write("`\3\2\2\2\u0151\u0152\7\177\2\2\u0152b\3\2\2\2\u0153\u0154")
        buf.write("\7]\2\2\u0154d\3\2\2\2\u0155\u0156\7_\2\2\u0156f\3\2\2")
        buf.write("\2\u0157\u0158\7.\2\2\u0158h\3\2\2\2\u0159\u015a\7=\2")
        buf.write("\2\u015aj\3\2\2\2\u015b\u0161\5m\67\2\u015c\u0161\5o8")
        buf.write("\2\u015d\u0161\5q9\2\u015e\u0161\5s:\2\u015f\u0161\5u")
        buf.write(";\2\u0160\u015b\3\2\2\2\u0160\u015c\3\2\2\2\u0160\u015d")
        buf.write("\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u015f\3\2\2\2\u0161")
        buf.write("l\3\2\2\2\u0162\u0163\7\62\2\2\u0163n\3\2\2\2\u0164\u0168")
        buf.write("\t\4\2\2\u0165\u0167\t\5\2\2\u0166\u0165\3\2\2\2\u0167")
        buf.write("\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2")
        buf.write("\u0169p\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016c\7\62\2")
        buf.write("\2\u016c\u0170\t\6\2\2\u016d\u016f\t\7\2\2\u016e\u016d")
        buf.write("\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0170")
        buf.write("\u0171\3\2\2\2\u0171r\3\2\2\2\u0172\u0170\3\2\2\2\u0173")
        buf.write("\u0174\7\62\2\2\u0174\u0178\t\b\2\2\u0175\u0177\t\t\2")
        buf.write("\2\u0176\u0175\3\2\2\2\u0177\u017a\3\2\2\2\u0178\u0176")
        buf.write("\3\2\2\2\u0178\u0179\3\2\2\2\u0179t\3\2\2\2\u017a\u0178")
        buf.write("\3\2\2\2\u017b\u017c\7\62\2\2\u017c\u0180\t\n\2\2\u017d")
        buf.write("\u017f\t\13\2\2\u017e\u017d\3\2\2\2\u017f\u0182\3\2\2")
        buf.write("\2\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181v\3\2")
        buf.write("\2\2\u0182\u0180\3\2\2\2\u0183\u0184\5y=\2\u0184\u0185")
        buf.write("\5{>\2\u0185\u0186\5}?\2\u0186\u018e\3\2\2\2\u0187\u0188")
        buf.write("\5y=\2\u0188\u0189\5{>\2\u0189\u018e\3\2\2\2\u018a\u018b")
        buf.write("\5y=\2\u018b\u018c\5}?\2\u018c\u018e\3\2\2\2\u018d\u0183")
        buf.write("\3\2\2\2\u018d\u0187\3\2\2\2\u018d\u018a\3\2\2\2\u018e")
        buf.write("x\3\2\2\2\u018f\u0191\t\5\2\2\u0190\u018f\3\2\2\2\u0191")
        buf.write("\u0192\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2")
        buf.write("\u0193z\3\2\2\2\u0194\u0198\7\60\2\2\u0195\u0197\t\5\2")
        buf.write("\2\u0196\u0195\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196")
        buf.write("\3\2\2\2\u0198\u0199\3\2\2\2\u0199|\3\2\2\2\u019a\u0198")
        buf.write("\3\2\2\2\u019b\u019d\t\f\2\2\u019c\u019e\t\r\2\2\u019d")
        buf.write("\u019c\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u01a0\3\2\2\2")
        buf.write("\u019f\u01a1\t\5\2\2\u01a0\u019f\3\2\2\2\u01a1\u01a2\3")
        buf.write("\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3~")
        buf.write("\3\2\2\2\u01a4\u01a9\7$\2\2\u01a5\u01a8\5\u0081A\2\u01a6")
        buf.write("\u01a8\n\16\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a6\3\2\2")
        buf.write("\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa")
        buf.write("\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac")
        buf.write("\u01ad\7$\2\2\u01ad\u0080\3\2\2\2\u01ae\u01af\7^\2\2\u01af")
        buf.write("\u01b0\t\17\2\2\u01b0\u0082\3\2\2\2\u01b1\u01b3\7\17\2")
        buf.write("\2\u01b2\u01b1\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b4")
        buf.write("\3\2\2\2\u01b4\u01b5\7\f\2\2\u01b5\u01b6\3\2\2\2\u01b6")
        buf.write("\u01b7\bB\2\2\u01b7\u0084\3\2\2\2\u01b8\u01ba\t\20\2\2")
        buf.write("\u01b9\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01b9\3")
        buf.write("\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01be")
        buf.write("\bC\2\2\u01be\u0086\3\2\2\2\u01bf\u01c0\7\61\2\2\u01c0")
        buf.write("\u01c1\7\61\2\2\u01c1\u01c5\3\2\2\2\u01c2\u01c4\n\21\2")
        buf.write("\2\u01c3\u01c2\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c3")
        buf.write("\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c8\3\2\2\2\u01c7")
        buf.write("\u01c5\3\2\2\2\u01c8\u01c9\bD\2\2\u01c9\u0088\3\2\2\2")
        buf.write("\u01ca\u01cb\5\u008bF\2\u01cb\u01cc\3\2\2\2\u01cc\u01cd")
        buf.write("\bE\2\2\u01cd\u008a\3\2\2\2\u01ce\u01cf\7\61\2\2\u01cf")
        buf.write("\u01d0\7,\2\2\u01d0\u01d7\3\2\2\2\u01d1\u01d6\5\u008b")
        buf.write("F\2\u01d2\u01d6\n\22\2\2\u01d3\u01d4\7,\2\2\u01d4\u01d6")
        buf.write("\n\23\2\2\u01d5\u01d1\3\2\2\2\u01d5\u01d2\3\2\2\2\u01d5")
        buf.write("\u01d3\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3\2\2\2")
        buf.write("\u01d7\u01d8\3\2\2\2\u01d8\u01da\3\2\2\2\u01d9\u01d7\3")
        buf.write("\2\2\2\u01da\u01db\7,\2\2\u01db\u01dc\7\61\2\2\u01dc\u008c")
        buf.write("\3\2\2\2\u01dd\u01de\13\2\2\2\u01de\u008e\3\2\2\2\u01df")
        buf.write("\u01e0\13\2\2\2\u01e0\u0090\3\2\2\2\u01e1\u01e2\13\2\2")
        buf.write("\2\u01e2\u0092\3\2\2\2\26\2\u0102\u010c\u0160\u0168\u0170")
        buf.write("\u0178\u0180\u018d\u0192\u0198\u019d\u01a2\u01a7\u01a9")
        buf.write("\u01b2\u01bb\u01c5\u01d5\u01d7\3\b\2\2")
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
    BOOLEAN = 9
    CONST = 10
    VAR = 11
    INTERGER = 12
    FLOAT = 13
    STRING = 14
    CONTINUE = 15
    BREAK = 16
    RANGE = 17
    BOOLEANLIT = 18
    NILLIT = 19
    IDENTIFIER = 20
    ADDOP = 21
    SUBOP = 22
    MULOP = 23
    DIVOP = 24
    MODOP = 25
    EQUALOP = 26
    NOTEQUALOP = 27
    LESSOP = 28
    LESSEQUALOP = 29
    GREATEROP = 30
    GREATEREQUALOP = 31
    ANDOP = 32
    OROP = 33
    NOTOP = 34
    ASSIGNOP = 35
    SHORTASSIGNOP = 36
    INCASSIGNOP = 37
    DECASSIGNOP = 38
    MULASSIGNOP = 39
    DIVASSIGNOP = 40
    MODASSIGNOP = 41
    DOT = 42
    COLON = 43
    BLANK = 44
    LP = 45
    RP = 46
    LB = 47
    RB = 48
    LSB = 49
    RSB = 50
    COMMA = 51
    SEMI = 52
    INTLIT = 53
    FLOATLIT = 54
    STRINGLIT = 55
    NL = 56
    WS = 57
    COMMENT = 58
    MULTI_COMMENT = 59
    ERROR_CHAR = 60
    ILLEGAL_ESCAPE = 61
    UNCLOSE_STRING = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", "'struct'", 
            "'interface'", "'boolean'", "'const'", "'var'", "'int'", "'float'", 
            "'string'", "'continue'", "'break'", "'range'", "'nil'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'&&'", "'||'", "'!'", "'='", "':='", "'+='", "'-='", 
            "'*='", "'/='", "'%='", "'.'", "':'", "'_'", "'('", "')'", "'{'", 
            "'}'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "BOOLEAN", "CONST", "VAR", "INTERGER", "FLOAT", "STRING", "CONTINUE", 
            "BREAK", "RANGE", "BOOLEANLIT", "NILLIT", "IDENTIFIER", "ADDOP", 
            "SUBOP", "MULOP", "DIVOP", "MODOP", "EQUALOP", "NOTEQUALOP", 
            "LESSOP", "LESSEQUALOP", "GREATEROP", "GREATEREQUALOP", "ANDOP", 
            "OROP", "NOTOP", "ASSIGNOP", "SHORTASSIGNOP", "INCASSIGNOP", 
            "DECASSIGNOP", "MULASSIGNOP", "DIVASSIGNOP", "MODASSIGNOP", 
            "DOT", "COLON", "BLANK", "LP", "RP", "LB", "RB", "LSB", "RSB", 
            "COMMA", "SEMI", "INTLIT", "FLOATLIT", "STRINGLIT", "NL", "WS", 
            "COMMENT", "MULTI_COMMENT", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING" ]

    ruleNames = [ "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", 
                  "INTERFACE", "BOOLEAN", "CONST", "VAR", "INTERGER", "FLOAT", 
                  "STRING", "CONTINUE", "BREAK", "RANGE", "BOOLEANLIT", 
                  "NILLIT", "IDENTIFIER", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
                  "MODOP", "EQUALOP", "NOTEQUALOP", "LESSOP", "LESSEQUALOP", 
                  "GREATEROP", "GREATEREQUALOP", "ANDOP", "OROP", "NOTOP", 
                  "ASSIGNOP", "SHORTASSIGNOP", "INCASSIGNOP", "DECASSIGNOP", 
                  "MULASSIGNOP", "DIVASSIGNOP", "MODASSIGNOP", "DOT", "COLON", 
                  "BLANK", "LP", "RP", "LB", "RB", "LSB", "RSB", "COMMA", 
                  "SEMI", "INTLIT", "ZERO", "DEC", "HEX", "OCT", "BIN", 
                  "FLOATLIT", "INT", "FRAC", "FIC", "STRINGLIT", "ESCAPE", 
                  "NL", "WS", "COMMENT", "MULTI_COMMENT", "NESTED_COMMENT", 
                  "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

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


