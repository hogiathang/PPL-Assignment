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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u0199\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\3\2\6\2P\n\2\r\2\16\2Q\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\5\4Z\n\4\3\5\3\5\3\5\3\5\3\5\5\5a\n\5\3\6\3\6\3\6\5")
        buf.write("\6f\n\6\3\6\3\6\5\6j\n\6\3\6\3\6\5\6n\n\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\5\7v\n\7\3\7\3\7\5\7z\n\7\3\7\3\7\5\7~\n")
        buf.write("\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0094\n\n\3\n\3\n\5\n")
        buf.write("\u0098\n\n\3\13\3\13\5\13\u009c\n\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\6\r\u00a7\n\r\r\r\16\r\u00a8\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\7\20\u00b9\n\20\f\20\16\20\u00bc\13\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\7\21\u00c3\n\21\f\21\16\21\u00c6")
        buf.write("\13\21\3\22\3\22\3\22\7\22\u00cb\n\22\f\22\16\22\u00ce")
        buf.write("\13\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\5\24\u00d7\n")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\7\24\u00e8\n\24\f\24\16\24\u00eb")
        buf.write("\13\24\3\25\3\25\3\25\3\25\5\25\u00f1\n\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\5\25\u00fa\n\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0106\n\26\3")
        buf.write("\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\7\30\u0114\n\30\f\30\16\30\u0117\13\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\7\30\u011f\n\30\f\30\16\30\u0122")
        buf.write("\13\30\3\30\3\30\5\30\u0126\n\30\3\31\3\31\3\31\3\31\5")
        buf.write("\31\u012c\n\31\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\7\33")
        buf.write("\u0140\n\33\f\33\16\33\u0143\13\33\3\33\3\33\5\33\u0147")
        buf.write("\n\33\3\34\3\34\3\34\5\34\u014c\n\34\3\34\3\34\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\5\35\u0157\n\35\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\5$\u0173\n$\3$\3$\3$\3")
        buf.write("$\7$\u0179\n$\f$\16$\u017c\13$\5$\u017e\n$\3$\3$\3$\3")
        buf.write("%\3%\7%\u0185\n%\f%\16%\u0188\13%\3%\3%\3&\3&\3&\6&\u018f")
        buf.write("\n&\r&\16&\u0190\3\'\3\'\5\'\u0195\n\'\3\'\3\'\3\'\2\3")
        buf.write("&(\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJL\2\13\4\2\13\13\16\20\4\2\30\30$$")
        buf.write("\3\2\34!\3\2\27\30\3\2\31\33\4\2\n\13\17\20\4\2\66\66")
        buf.write("::\3\2&+\4\2\26\26..\2\u01a9\2O\3\2\2\2\4U\3\2\2\2\6Y")
        buf.write("\3\2\2\2\b`\3\2\2\2\nb\3\2\2\2\fq\3\2\2\2\16\177\3\2\2")
        buf.write("\2\20\u0083\3\2\2\2\22\u0089\3\2\2\2\24\u009b\3\2\2\2")
        buf.write("\26\u009d\3\2\2\2\30\u00a6\3\2\2\2\32\u00aa\3\2\2\2\34")
        buf.write("\u00af\3\2\2\2\36\u00b4\3\2\2\2 \u00bf\3\2\2\2\"\u00c7")
        buf.write("\3\2\2\2$\u00cf\3\2\2\2&\u00d6\3\2\2\2(\u00f9\3\2\2\2")
        buf.write("*\u0105\3\2\2\2,\u0109\3\2\2\2.\u0125\3\2\2\2\60\u0127")
        buf.write("\3\2\2\2\62\u0131\3\2\2\2\64\u0133\3\2\2\2\66\u0148\3")
        buf.write("\2\2\28\u0156\3\2\2\2:\u0158\3\2\2\2<\u015c\3\2\2\2>\u015e")
        buf.write("\3\2\2\2@\u0162\3\2\2\2B\u0169\3\2\2\2D\u016c\3\2\2\2")
        buf.write("F\u016f\3\2\2\2H\u0182\3\2\2\2J\u018e\3\2\2\2L\u0192\3")
        buf.write("\2\2\2NP\5\6\4\2ON\3\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2")
        buf.write("\2RS\3\2\2\2ST\7\2\2\3T\3\3\2\2\2UV\t\2\2\2V\5\3\2\2\2")
        buf.write("WZ\5\b\5\2XZ\5*\26\2YW\3\2\2\2YX\3\2\2\2Z\7\3\2\2\2[a")
        buf.write("\5\n\6\2\\a\5\f\7\2]a\5\16\b\2^a\5\20\t\2_a\5\22\n\2`")
        buf.write("[\3\2\2\2`\\\3\2\2\2`]\3\2\2\2`^\3\2\2\2`_\3\2\2\2a\t")
        buf.write("\3\2\2\2bc\7\r\2\2ce\7\26\2\2df\5J&\2ed\3\2\2\2ef\3\2")
        buf.write("\2\2fm\3\2\2\2gn\5\4\3\2hj\5\4\3\2ih\3\2\2\2ij\3\2\2\2")
        buf.write("jk\3\2\2\2kl\7%\2\2ln\5&\24\2mg\3\2\2\2mi\3\2\2\2no\3")
        buf.write("\2\2\2op\7\66\2\2p\13\3\2\2\2qr\7\7\2\2rs\7\26\2\2su\7")
        buf.write("/\2\2tv\5\"\22\2ut\3\2\2\2uv\3\2\2\2vw\3\2\2\2wy\7\60")
        buf.write("\2\2xz\5\4\3\2yx\3\2\2\2yz\3\2\2\2z{\3\2\2\2{}\5H%\2|")
        buf.write("~\7\66\2\2}|\3\2\2\2}~\3\2\2\2~\r\3\2\2\2\177\u0080\7")
        buf.write("\b\2\2\u0080\u0081\7\26\2\2\u0081\u0082\5\24\13\2\u0082")
        buf.write("\17\3\2\2\2\u0083\u0084\7\f\2\2\u0084\u0085\7\26\2\2\u0085")
        buf.write("\u0086\7%\2\2\u0086\u0087\5&\24\2\u0087\u0088\7\66\2\2")
        buf.write("\u0088\21\3\2\2\2\u0089\u008a\7\7\2\2\u008a\u008b\7/\2")
        buf.write("\2\u008b\u008c\7\26\2\2\u008c\u008d\7\26\2\2\u008d\u008e")
        buf.write("\7\60\2\2\u008e\u008f\7\26\2\2\u008f\u0090\7/\2\2\u0090")
        buf.write("\u0091\5\"\22\2\u0091\u0093\7\60\2\2\u0092\u0094\5\4\3")
        buf.write("\2\u0093\u0092\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095")
        buf.write("\3\2\2\2\u0095\u0097\5H%\2\u0096\u0098\7\66\2\2\u0097")
        buf.write("\u0096\3\2\2\2\u0097\u0098\3\2\2\2\u0098\23\3\2\2\2\u0099")
        buf.write("\u009c\5\26\f\2\u009a\u009c\5\32\16\2\u009b\u0099\3\2")
        buf.write("\2\2\u009b\u009a\3\2\2\2\u009c\25\3\2\2\2\u009d\u009e")
        buf.write("\7\t\2\2\u009e\u009f\7\61\2\2\u009f\u00a0\5\30\r\2\u00a0")
        buf.write("\u00a1\7\62\2\2\u00a1\27\3\2\2\2\u00a2\u00a3\7\26\2\2")
        buf.write("\u00a3\u00a4\5\4\3\2\u00a4\u00a5\7\66\2\2\u00a5\u00a7")
        buf.write("\3\2\2\2\u00a6\u00a2\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8")
        buf.write("\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\31\3\2\2\2\u00aa")
        buf.write("\u00ab\7\n\2\2\u00ab\u00ac\7\61\2\2\u00ac\u00ad\5\34\17")
        buf.write("\2\u00ad\u00ae\7\62\2\2\u00ae\33\3\2\2\2\u00af\u00b0\7")
        buf.write("\26\2\2\u00b0\u00b1\5\36\20\2\u00b1\u00b2\5\4\3\2\u00b2")
        buf.write("\u00b3\7\66\2\2\u00b3\35\3\2\2\2\u00b4\u00ba\7/\2\2\u00b5")
        buf.write("\u00b6\5 \21\2\u00b6\u00b7\5\4\3\2\u00b7\u00b9\3\2\2\2")
        buf.write("\u00b8\u00b5\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3")
        buf.write("\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bd\3\2\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bd\u00be\7\60\2\2\u00be\37\3\2\2\2\u00bf\u00c4")
        buf.write("\7\26\2\2\u00c0\u00c1\7\65\2\2\u00c1\u00c3\7\26\2\2\u00c2")
        buf.write("\u00c0\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2")
        buf.write("\u00c4\u00c5\3\2\2\2\u00c5!\3\2\2\2\u00c6\u00c4\3\2\2")
        buf.write("\2\u00c7\u00cc\5$\23\2\u00c8\u00c9\7\65\2\2\u00c9\u00cb")
        buf.write("\5$\23\2\u00ca\u00c8\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc")
        buf.write("\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd#\3\2\2\2\u00ce")
        buf.write("\u00cc\3\2\2\2\u00cf\u00d0\7\26\2\2\u00d0\u00d1\5\4\3")
        buf.write("\2\u00d1%\3\2\2\2\u00d2\u00d3\b\24\1\2\u00d3\u00d4\t\3")
        buf.write("\2\2\u00d4\u00d7\5(\25\2\u00d5\u00d7\5(\25\2\u00d6\u00d2")
        buf.write("\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\u00e9\3\2\2\2\u00d8")
        buf.write("\u00d9\f\t\2\2\u00d9\u00da\7#\2\2\u00da\u00e8\5(\25\2")
        buf.write("\u00db\u00dc\f\b\2\2\u00dc\u00dd\7\"\2\2\u00dd\u00e8\5")
        buf.write("(\25\2\u00de\u00df\f\7\2\2\u00df\u00e0\t\4\2\2\u00e0\u00e8")
        buf.write("\5(\25\2\u00e1\u00e2\f\6\2\2\u00e2\u00e3\t\5\2\2\u00e3")
        buf.write("\u00e8\5(\25\2\u00e4\u00e5\f\5\2\2\u00e5\u00e6\t\6\2\2")
        buf.write("\u00e6\u00e8\5(\25\2\u00e7\u00d8\3\2\2\2\u00e7\u00db\3")
        buf.write("\2\2\2\u00e7\u00de\3\2\2\2\u00e7\u00e1\3\2\2\2\u00e7\u00e4")
        buf.write("\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9")
        buf.write("\u00ea\3\2\2\2\u00ea\'\3\2\2\2\u00eb\u00e9\3\2\2\2\u00ec")
        buf.write("\u00f0\7\26\2\2\u00ed\u00f1\5J&\2\u00ee\u00ef\7,\2\2\u00ef")
        buf.write("\u00f1\7\26\2\2\u00f0\u00ed\3\2\2\2\u00f0\u00ee\3\2\2")
        buf.write("\2\u00f0\u00f1\3\2\2\2\u00f1\u00fa\3\2\2\2\u00f2\u00fa")
        buf.write("\7\67\2\2\u00f3\u00fa\78\2\2\u00f4\u00fa\79\2\2\u00f5")
        buf.write("\u00f6\7/\2\2\u00f6\u00f7\5&\24\2\u00f7\u00f8\7\60\2\2")
        buf.write("\u00f8\u00fa\3\2\2\2\u00f9\u00ec\3\2\2\2\u00f9\u00f2\3")
        buf.write("\2\2\2\u00f9\u00f3\3\2\2\2\u00f9\u00f4\3\2\2\2\u00f9\u00f5")
        buf.write("\3\2\2\2\u00fa)\3\2\2\2\u00fb\u0106\5\60\31\2\u00fc\u0106")
        buf.write("\5\64\33\2\u00fd\u0106\5\66\34\2\u00fe\u0106\5B\"\2\u00ff")
        buf.write("\u0106\5D#\2\u0100\u0106\5F$\2\u0101\u0106\5L\'\2\u0102")
        buf.write("\u0106\5,\27\2\u0103\u0106\5\n\6\2\u0104\u0106\5\20\t")
        buf.write("\2\u0105\u00fb\3\2\2\2\u0105\u00fc\3\2\2\2\u0105\u00fd")
        buf.write("\3\2\2\2\u0105\u00fe\3\2\2\2\u0105\u00ff\3\2\2\2\u0105")
        buf.write("\u0100\3\2\2\2\u0105\u0101\3\2\2\2\u0105\u0102\3\2\2\2")
        buf.write("\u0105\u0103\3\2\2\2\u0105\u0104\3\2\2\2\u0106\u0107\3")
        buf.write("\2\2\2\u0107\u0108\b\26\1\2\u0108+\3\2\2\2\u0109\u010a")
        buf.write("\7\26\2\2\u010a\u010b\7&\2\2\u010b\u010c\5J&\2\u010c\u010d")
        buf.write("\t\7\2\2\u010d\u010e\5.\30\2\u010e-\3\2\2\2\u010f\u0110")
        buf.write("\7\61\2\2\u0110\u0115\5.\30\2\u0111\u0112\7\65\2\2\u0112")
        buf.write("\u0114\5.\30\2\u0113\u0111\3\2\2\2\u0114\u0117\3\2\2\2")
        buf.write("\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0118\3")
        buf.write("\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119\7\62\2\2\u0119")
        buf.write("\u0126\3\2\2\2\u011a\u011b\7\61\2\2\u011b\u0120\5&\24")
        buf.write("\2\u011c\u011d\7\65\2\2\u011d\u011f\5&\24\2\u011e\u011c")
        buf.write("\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0120")
        buf.write("\u0121\3\2\2\2\u0121\u0123\3\2\2\2\u0122\u0120\3\2\2\2")
        buf.write("\u0123\u0124\7\62\2\2\u0124\u0126\3\2\2\2\u0125\u010f")
        buf.write("\3\2\2\2\u0125\u011a\3\2\2\2\u0126/\3\2\2\2\u0127\u012b")
        buf.write("\7\26\2\2\u0128\u012c\5J&\2\u0129\u012a\7,\2\2\u012a\u012c")
        buf.write("\7\26\2\2\u012b\u0128\3\2\2\2\u012b\u0129\3\2\2\2\u012b")
        buf.write("\u012c\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012e\5\62\32")
        buf.write("\2\u012e\u012f\5&\24\2\u012f\u0130\t\b\2\2\u0130\61\3")
        buf.write("\2\2\2\u0131\u0132\t\t\2\2\u0132\63\3\2\2\2\u0133\u0134")
        buf.write("\7\3\2\2\u0134\u0135\7/\2\2\u0135\u0136\5&\24\2\u0136")
        buf.write("\u0137\7\60\2\2\u0137\u0141\5H%\2\u0138\u0139\7\4\2\2")
        buf.write("\u0139\u013a\7\3\2\2\u013a\u013b\7/\2\2\u013b\u013c\5")
        buf.write("&\24\2\u013c\u013d\7\60\2\2\u013d\u013e\5H%\2\u013e\u0140")
        buf.write("\3\2\2\2\u013f\u0138\3\2\2\2\u0140\u0143\3\2\2\2\u0141")
        buf.write("\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0146\3\2\2\2")
        buf.write("\u0143\u0141\3\2\2\2\u0144\u0145\7\4\2\2\u0145\u0147\5")
        buf.write("H%\2\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147\65")
        buf.write("\3\2\2\2\u0148\u014b\7\5\2\2\u0149\u014c\58\35\2\u014a")
        buf.write("\u014c\5@!\2\u014b\u0149\3\2\2\2\u014b\u014a\3\2\2\2\u014c")
        buf.write("\u014d\3\2\2\2\u014d\u014e\5H%\2\u014e\67\3\2\2\2\u014f")
        buf.write("\u0157\5<\37\2\u0150\u0151\5:\36\2\u0151\u0152\7\66\2")
        buf.write("\2\u0152\u0153\5<\37\2\u0153\u0154\7\66\2\2\u0154\u0155")
        buf.write("\5> \2\u0155\u0157\3\2\2\2\u0156\u014f\3\2\2\2\u0156\u0150")
        buf.write("\3\2\2\2\u01579\3\2\2\2\u0158\u0159\7\26\2\2\u0159\u015a")
        buf.write("\7&\2\2\u015a\u015b\5&\24\2\u015b;\3\2\2\2\u015c\u015d")
        buf.write("\5&\24\2\u015d=\3\2\2\2\u015e\u015f\7\26\2\2\u015f\u0160")
        buf.write("\5\62\32\2\u0160\u0161\5&\24\2\u0161?\3\2\2\2\u0162\u0163")
        buf.write("\t\n\2\2\u0163\u0164\7\65\2\2\u0164\u0165\7\26\2\2\u0165")
        buf.write("\u0166\7&\2\2\u0166\u0167\7\23\2\2\u0167\u0168\7\26\2")
        buf.write("\2\u0168A\3\2\2\2\u0169\u016a\7\22\2\2\u016a\u016b\7\66")
        buf.write("\2\2\u016bC\3\2\2\2\u016c\u016d\7\21\2\2\u016d\u016e\7")
        buf.write("\66\2\2\u016eE\3\2\2\2\u016f\u0172\7\26\2\2\u0170\u0171")
        buf.write("\7,\2\2\u0171\u0173\7\26\2\2\u0172\u0170\3\2\2\2\u0172")
        buf.write("\u0173\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u017d\7/\2\2")
        buf.write("\u0175\u017a\5&\24\2\u0176\u0177\7\65\2\2\u0177\u0179")
        buf.write("\5&\24\2\u0178\u0176\3\2\2\2\u0179\u017c\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017e\3\2\2\2")
        buf.write("\u017c\u017a\3\2\2\2\u017d\u0175\3\2\2\2\u017d\u017e\3")
        buf.write("\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\7\60\2\2\u0180")
        buf.write("\u0181\7\66\2\2\u0181G\3\2\2\2\u0182\u0186\7\61\2\2\u0183")
        buf.write("\u0185\5*\26\2\u0184\u0183\3\2\2\2\u0185\u0188\3\2\2\2")
        buf.write("\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0189\3")
        buf.write("\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a\7\62\2\2\u018a")
        buf.write("I\3\2\2\2\u018b\u018c\7\63\2\2\u018c\u018d\7\67\2\2\u018d")
        buf.write("\u018f\7\64\2\2\u018e\u018b\3\2\2\2\u018f\u0190\3\2\2")
        buf.write("\2\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191K\3\2")
        buf.write("\2\2\u0192\u0194\7\6\2\2\u0193\u0195\5&\24\2\u0194\u0193")
        buf.write("\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0196\3\2\2\2\u0196")
        buf.write("\u0197\7\66\2\2\u0197M\3\2\2\2&QY`eimuy}\u0093\u0097\u009b")
        buf.write("\u00a8\u00ba\u00c4\u00cc\u00d6\u00e7\u00e9\u00f0\u00f9")
        buf.write("\u0105\u0115\u0120\u0125\u012b\u0141\u0146\u014b\u0156")
        buf.write("\u0172\u017a\u017d\u0186\u0190\u0194")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'boolean'", 
                     "'const'", "'var'", "'int'", "'float'", "'string'", 
                     "'continue'", "'break'", "'range'", "<INVALID>", "'nil'", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "':='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "':'", "'_'", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "','", "';'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "BOOLEAN", "CONST", 
                      "VAR", "INTERGER", "FLOAT", "STRING", "CONTINUE", 
                      "BREAK", "RANGE", "BOOLEANLIT", "NILLIT", "IDENTIFIER", 
                      "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "EQUALOP", 
                      "NOTEQUALOP", "LESSOP", "LESSEQUALOP", "GREATEROP", 
                      "GREATEREQUALOP", "ANDOP", "OROP", "NOTOP", "ASSIGNOP", 
                      "SHORTASSIGNOP", "INCASSIGNOP", "DECASSIGNOP", "MULASSIGNOP", 
                      "DIVASSIGNOP", "MODASSIGNOP", "DOT", "COLON", "BLANK", 
                      "LP", "RP", "LB", "RB", "LSB", "RSB", "COMMA", "SEMI", 
                      "INTLIT", "FLOATLIT", "STRINGLIT", "NL", "WS", "COMMENT", 
                      "MULTI_COMMENT", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_tYPE = 1
    RULE_parserRuleSpec = 2
    RULE_decl = 3
    RULE_varDecl = 4
    RULE_funcDecl = 5
    RULE_typeDecl = 6
    RULE_constDecl = 7
    RULE_methodDecl = 8
    RULE_typeDefinition = 9
    RULE_structDefinition = 10
    RULE_structFields = 11
    RULE_interfaceDefinition = 12
    RULE_interfaceFields = 13
    RULE_listParams = 14
    RULE_listIdentifier = 15
    RULE_funcParams = 16
    RULE_funcParam = 17
    RULE_expression = 18
    RULE_term = 19
    RULE_statement = 20
    RULE_arrayLiteral = 21
    RULE_arraysBlock = 22
    RULE_assignStatement = 23
    RULE_assignmentOperator = 24
    RULE_ifStatement = 25
    RULE_forStatement = 26
    RULE_forLoop = 27
    RULE_initilization = 28
    RULE_forCondition = 29
    RULE_forUpdate = 30
    RULE_forIteration = 31
    RULE_breakStatement = 32
    RULE_continueStatement = 33
    RULE_callStatement = 34
    RULE_block = 35
    RULE_arrayDims = 36
    RULE_returnStatement = 37

    ruleNames =  [ "program", "tYPE", "parserRuleSpec", "decl", "varDecl", 
                   "funcDecl", "typeDecl", "constDecl", "methodDecl", "typeDefinition", 
                   "structDefinition", "structFields", "interfaceDefinition", 
                   "interfaceFields", "listParams", "listIdentifier", "funcParams", 
                   "funcParam", "expression", "term", "statement", "arrayLiteral", 
                   "arraysBlock", "assignStatement", "assignmentOperator", 
                   "ifStatement", "forStatement", "forLoop", "initilization", 
                   "forCondition", "forUpdate", "forIteration", "breakStatement", 
                   "continueStatement", "callStatement", "block", "arrayDims", 
                   "returnStatement" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    BOOLEAN=9
    CONST=10
    VAR=11
    INTERGER=12
    FLOAT=13
    STRING=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    BOOLEANLIT=18
    NILLIT=19
    IDENTIFIER=20
    ADDOP=21
    SUBOP=22
    MULOP=23
    DIVOP=24
    MODOP=25
    EQUALOP=26
    NOTEQUALOP=27
    LESSOP=28
    LESSEQUALOP=29
    GREATEROP=30
    GREATEREQUALOP=31
    ANDOP=32
    OROP=33
    NOTOP=34
    ASSIGNOP=35
    SHORTASSIGNOP=36
    INCASSIGNOP=37
    DECASSIGNOP=38
    MULASSIGNOP=39
    DIVASSIGNOP=40
    MODASSIGNOP=41
    DOT=42
    COLON=43
    BLANK=44
    LP=45
    RP=46
    LB=47
    RB=48
    LSB=49
    RSB=50
    COMMA=51
    SEMI=52
    INTLIT=53
    FLOATLIT=54
    STRINGLIT=55
    NL=56
    WS=57
    COMMENT=58
    MULTI_COMMENT=59
    ERROR_CHAR=60
    ILLEGAL_ESCAPE=61
    UNCLOSE_STRING=62

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

        def parserRuleSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParserRuleSpecContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParserRuleSpecContext,i)


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
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.parserRuleSpec()
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                    break

            self.state = 81
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TYPEContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERGER(self):
            return self.getToken(MiniGoParser.INTERGER, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_tYPE

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTYPE" ):
                return visitor.visitTYPE(self)
            else:
                return visitor.visitChildren(self)




    def tYPE(self):

        localctx = MiniGoParser.TYPEContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tYPE)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.INTERGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0)):
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


    class ParserRuleSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parserRuleSpec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParserRuleSpec" ):
                return visitor.visitParserRuleSpec(self)
            else:
                return visitor.visitChildren(self)




    def parserRuleSpec(self):

        localctx = MiniGoParser.ParserRuleSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parserRuleSpec)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.statement()
                pass


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


        def funcDecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncDeclContext,0)


        def typeDecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypeDeclContext,0)


        def constDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.funcDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.typeDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 92
                self.constDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 93
                self.methodDecl()
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

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def tYPE(self):
            return self.getTypedRuleContext(MiniGoParser.TYPEContext,0)


        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def ASSIGNOP(self):
            return self.getToken(MiniGoParser.ASSIGNOP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = MiniGoParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(MiniGoParser.VAR)
            self.state = 97
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LSB:
                self.state = 98
                self.arrayDims()


            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 101
                self.tYPE()
                pass

            elif la_ == 2:
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.INTERGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0):
                    self.state = 102
                    self.tYPE()


                self.state = 105
                self.match(MiniGoParser.ASSIGNOP)
                self.state = 106
                self.expression(0)
                pass


            self.state = 109
            self.match(MiniGoParser.SEMI)
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

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def funcParams(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamsContext,0)


        def tYPE(self):
            return self.getTypedRuleContext(MiniGoParser.TYPEContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = MiniGoParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(MiniGoParser.FUNC)
            self.state = 112
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 113
            self.match(MiniGoParser.LP)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 114
                self.funcParams()


            self.state = 117
            self.match(MiniGoParser.RP)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.INTERGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0):
                self.state = 118
                self.tYPE()


            self.state = 121
            self.block()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 122
                self.match(MiniGoParser.SEMI)


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

        def typeDefinition(self):
            return self.getTypedRuleContext(MiniGoParser.TypeDefinitionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typeDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDecl" ):
                return visitor.visitTypeDecl(self)
            else:
                return visitor.visitChildren(self)




    def typeDecl(self):

        localctx = MiniGoParser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(MiniGoParser.TYPE)
            self.state = 126
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 127
            self.typeDefinition()
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

        def ASSIGNOP(self):
            return self.getToken(MiniGoParser.ASSIGNOP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

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
            self.state = 129
            self.match(MiniGoParser.CONST)
            self.state = 130
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 131
            self.match(MiniGoParser.ASSIGNOP)
            self.state = 132
            self.expression(0)
            self.state = 133
            self.match(MiniGoParser.SEMI)
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

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LP)
            else:
                return self.getToken(MiniGoParser.LP, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RP)
            else:
                return self.getToken(MiniGoParser.RP, i)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def funcParams(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamsContext,0)


        def tYPE(self):
            return self.getTypedRuleContext(MiniGoParser.TYPEContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_methodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = MiniGoParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(MiniGoParser.FUNC)
            self.state = 136
            self.match(MiniGoParser.LP)
            self.state = 137
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 138
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 139
            self.match(MiniGoParser.RP)
            self.state = 140
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 141
            self.match(MiniGoParser.LP)

            self.state = 142
            self.funcParams()
            self.state = 143
            self.match(MiniGoParser.RP)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.INTERGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0):
                self.state = 144
                self.tYPE()


            self.state = 147
            self.block()
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 148
                self.match(MiniGoParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structDefinition(self):
            return self.getTypedRuleContext(MiniGoParser.StructDefinitionContext,0)


        def interfaceDefinition(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceDefinitionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typeDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDefinition" ):
                return visitor.visitTypeDefinition(self)
            else:
                return visitor.visitChildren(self)




    def typeDefinition(self):

        localctx = MiniGoParser.TypeDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_typeDefinition)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.structDefinition()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.interfaceDefinition()
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


    class StructDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def structFields(self):
            return self.getTypedRuleContext(MiniGoParser.StructFieldsContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDefinition" ):
                return visitor.visitStructDefinition(self)
            else:
                return visitor.visitChildren(self)




    def structDefinition(self):

        localctx = MiniGoParser.StructDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_structDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(MiniGoParser.STRUCT)
            self.state = 156
            self.match(MiniGoParser.LB)
            self.state = 157
            self.structFields()
            self.state = 158
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructFieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def tYPE(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.TYPEContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.TYPEContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structFields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFields" ):
                return visitor.visitStructFields(self)
            else:
                return visitor.visitChildren(self)




    def structFields(self):

        localctx = MiniGoParser.StructFieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_structFields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 160
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 161
                self.tYPE()
                self.state = 162
                self.match(MiniGoParser.SEMI)
                self.state = 166 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.IDENTIFIER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def interfaceFields(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceFieldsContext,0)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceDefinition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDefinition" ):
                return visitor.visitInterfaceDefinition(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDefinition(self):

        localctx = MiniGoParser.InterfaceDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_interfaceDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(MiniGoParser.INTERFACE)
            self.state = 169
            self.match(MiniGoParser.LB)
            self.state = 170
            self.interfaceFields()
            self.state = 171
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceFieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def listParams(self):
            return self.getTypedRuleContext(MiniGoParser.ListParamsContext,0)


        def tYPE(self):
            return self.getTypedRuleContext(MiniGoParser.TYPEContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceFields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceFields" ):
                return visitor.visitInterfaceFields(self)
            else:
                return visitor.visitChildren(self)




    def interfaceFields(self):

        localctx = MiniGoParser.InterfaceFieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_interfaceFields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 174
            self.listParams()
            self.state = 175
            self.tYPE()
            self.state = 176
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def listIdentifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ListIdentifierContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ListIdentifierContext,i)


        def tYPE(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.TYPEContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.TYPEContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_listParams

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListParams" ):
                return visitor.visitListParams(self)
            else:
                return visitor.visitChildren(self)




    def listParams(self):

        localctx = MiniGoParser.ListParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(MiniGoParser.LP)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 179
                self.listIdentifier()
                self.state = 180
                self.tYPE()
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
            self.match(MiniGoParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_listIdentifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListIdentifier" ):
                return visitor.visitListIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def listIdentifier(self):

        localctx = MiniGoParser.ListIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_listIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 190
                self.match(MiniGoParser.COMMA)
                self.state = 191
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcParam(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FuncParamContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FuncParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcParams

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncParams" ):
                return visitor.visitFuncParams(self)
            else:
                return visitor.visitChildren(self)




    def funcParams(self):

        localctx = MiniGoParser.FuncParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_funcParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.funcParam()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 198
                self.match(MiniGoParser.COMMA)
                self.state = 199
                self.funcParam()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def tYPE(self):
            return self.getTypedRuleContext(MiniGoParser.TYPEContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcParam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncParam" ):
                return visitor.visitFuncParam(self)
            else:
                return visitor.visitChildren(self)




    def funcParam(self):

        localctx = MiniGoParser.FuncParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_funcParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 206
            self.tYPE()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(MiniGoParser.TermContext,0)


        def NOTOP(self):
            return self.getToken(MiniGoParser.NOTOP, 0)

        def SUBOP(self):
            return self.getToken(MiniGoParser.SUBOP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def OROP(self):
            return self.getToken(MiniGoParser.OROP, 0)

        def ANDOP(self):
            return self.getToken(MiniGoParser.ANDOP, 0)

        def EQUALOP(self):
            return self.getToken(MiniGoParser.EQUALOP, 0)

        def NOTEQUALOP(self):
            return self.getToken(MiniGoParser.NOTEQUALOP, 0)

        def LESSOP(self):
            return self.getToken(MiniGoParser.LESSOP, 0)

        def LESSEQUALOP(self):
            return self.getToken(MiniGoParser.LESSEQUALOP, 0)

        def GREATEROP(self):
            return self.getToken(MiniGoParser.GREATEROP, 0)

        def GREATEREQUALOP(self):
            return self.getToken(MiniGoParser.GREATEREQUALOP, 0)

        def ADDOP(self):
            return self.getToken(MiniGoParser.ADDOP, 0)

        def MULOP(self):
            return self.getToken(MiniGoParser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(MiniGoParser.DIVOP, 0)

        def MODOP(self):
            return self.getToken(MiniGoParser.MODOP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUBOP, MiniGoParser.NOTOP]:
                self.state = 209
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUBOP or _la==MiniGoParser.NOTOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 210
                self.term()
                pass
            elif token in [MiniGoParser.IDENTIFIER, MiniGoParser.LP, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT]:
                self.state = 211
                self.term()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 229
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 214
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 215
                        self.match(MiniGoParser.OROP)
                        self.state = 216
                        self.term()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 217
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 218
                        self.match(MiniGoParser.ANDOP)
                        self.state = 219
                        self.term()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 220
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 221
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUALOP) | (1 << MiniGoParser.NOTEQUALOP) | (1 << MiniGoParser.LESSOP) | (1 << MiniGoParser.LESSEQUALOP) | (1 << MiniGoParser.GREATEROP) | (1 << MiniGoParser.GREATEREQUALOP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 222
                        self.term()
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 223
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 224
                        _la = self._input.LA(1)
                        if not(_la==MiniGoParser.ADDOP or _la==MiniGoParser.SUBOP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 225
                        self.term()
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 226
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 227
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULOP) | (1 << MiniGoParser.DIVOP) | (1 << MiniGoParser.MODOP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 228
                        self.term()
                        pass

             
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MiniGoParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MiniGoParser.STRINGLIT, 0)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = MiniGoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_term)
        try:
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 238
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 235
                    self.arrayDims()

                elif la_ == 2:
                    self.state = 236
                    self.match(MiniGoParser.DOT)
                    self.state = 237
                    self.match(MiniGoParser.IDENTIFIER)


                pass
            elif token in [MiniGoParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(MiniGoParser.INTLIT)
                pass
            elif token in [MiniGoParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 241
                self.match(MiniGoParser.FLOATLIT)
                pass
            elif token in [MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 242
                self.match(MiniGoParser.STRINGLIT)
                pass
            elif token in [MiniGoParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 243
                self.match(MiniGoParser.LP)
                self.state = 244
                self.expression(0)
                self.state = 245
                self.match(MiniGoParser.RP)
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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


        def arrayLiteral(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLiteralContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def constDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 249
                self.assignStatement()
                pass

            elif la_ == 2:
                self.state = 250
                self.ifStatement()
                pass

            elif la_ == 3:
                self.state = 251
                self.forStatement()
                pass

            elif la_ == 4:
                self.state = 252
                self.breakStatement()
                pass

            elif la_ == 5:
                self.state = 253
                self.continueStatement()
                pass

            elif la_ == 6:
                self.state = 254
                self.callStatement()
                pass

            elif la_ == 7:
                self.state = 255
                self.returnStatement()
                pass

            elif la_ == 8:
                self.state = 256
                self.arrayLiteral()
                pass

            elif la_ == 9:
                self.state = 257
                self.varDecl()
                pass

            elif la_ == 10:
                self.state = 258
                self.constDecl()
                pass


            print(self._input.getText(localctx.start, self._input.LT(-1)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def SHORTASSIGNOP(self):
            return self.getToken(MiniGoParser.SHORTASSIGNOP, 0)

        def arraysBlock(self):
            return self.getTypedRuleContext(MiniGoParser.ArraysBlockContext,0)


        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = MiniGoParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 264
            self.match(MiniGoParser.SHORTASSIGNOP)

            self.state = 265
            self.arrayDims()
            self.state = 266
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INTERFACE) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 267
            self.arraysBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraysBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def arraysBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ArraysBlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ArraysBlockContext,i)


        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arraysBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraysBlock" ):
                return visitor.visitArraysBlock(self)
            else:
                return visitor.visitChildren(self)




    def arraysBlock(self):

        localctx = MiniGoParser.ArraysBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_arraysBlock)
        self._la = 0 # Token type
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(MiniGoParser.LB)
                self.state = 270
                self.arraysBlock()
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 271
                    self.match(MiniGoParser.COMMA)
                    self.state = 272
                    self.arraysBlock()
                    self.state = 277
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 278
                self.match(MiniGoParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.match(MiniGoParser.LB)
                self.state = 281
                self.expression(0)
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 282
                    self.match(MiniGoParser.COMMA)
                    self.state = 283
                    self.expression(0)
                    self.state = 288
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 289
                self.match(MiniGoParser.RB)
                pass


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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def assignmentOperator(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentOperatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignStatement(self):

        localctx = MiniGoParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assignStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LSB]:
                self.state = 294
                self.arrayDims()
                pass
            elif token in [MiniGoParser.DOT]:
                self.state = 295
                self.match(MiniGoParser.DOT)
                self.state = 296
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.SHORTASSIGNOP, MiniGoParser.INCASSIGNOP, MiniGoParser.DECASSIGNOP, MiniGoParser.MULASSIGNOP, MiniGoParser.DIVASSIGNOP, MiniGoParser.MODASSIGNOP]:
                pass
            else:
                pass
            self.state = 299
            self.assignmentOperator()
            self.state = 300
            self.expression(0)
            self.state = 301
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMI or _la==MiniGoParser.NL):
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


    class AssignmentOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHORTASSIGNOP(self):
            return self.getToken(MiniGoParser.SHORTASSIGNOP, 0)

        def INCASSIGNOP(self):
            return self.getToken(MiniGoParser.INCASSIGNOP, 0)

        def DECASSIGNOP(self):
            return self.getToken(MiniGoParser.DECASSIGNOP, 0)

        def MULASSIGNOP(self):
            return self.getToken(MiniGoParser.MULASSIGNOP, 0)

        def DIVASSIGNOP(self):
            return self.getToken(MiniGoParser.DIVASSIGNOP, 0)

        def MODASSIGNOP(self):
            return self.getToken(MiniGoParser.MODASSIGNOP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignmentOperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = MiniGoParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.SHORTASSIGNOP) | (1 << MiniGoParser.INCASSIGNOP) | (1 << MiniGoParser.DECASSIGNOP) | (1 << MiniGoParser.MULASSIGNOP) | (1 << MiniGoParser.DIVASSIGNOP) | (1 << MiniGoParser.MODASSIGNOP))) != 0)):
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


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IF)
            else:
                return self.getToken(MiniGoParser.IF, i)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LP)
            else:
                return self.getToken(MiniGoParser.LP, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RP)
            else:
                return self.getToken(MiniGoParser.RP, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ELSE)
            else:
                return self.getToken(MiniGoParser.ELSE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniGoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(MiniGoParser.IF)
            self.state = 306
            self.match(MiniGoParser.LP)
            self.state = 307
            self.expression(0)
            self.state = 308
            self.match(MiniGoParser.RP)
            self.state = 309
            self.block()
            self.state = 319
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 310
                    self.match(MiniGoParser.ELSE)
                    self.state = 311
                    self.match(MiniGoParser.IF)
                    self.state = 312
                    self.match(MiniGoParser.LP)
                    self.state = 313
                    self.expression(0)
                    self.state = 314
                    self.match(MiniGoParser.RP)
                    self.state = 315
                    self.block() 
                self.state = 321
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 322
                self.match(MiniGoParser.ELSE)
                self.state = 323
                self.block()


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

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(MiniGoParser.ForLoopContext,0)


        def forIteration(self):
            return self.getTypedRuleContext(MiniGoParser.ForIterationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = MiniGoParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(MiniGoParser.FOR)
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 327
                self.forLoop()
                pass

            elif la_ == 2:
                self.state = 328
                self.forIteration()
                pass


            self.state = 331
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forCondition(self):
            return self.getTypedRuleContext(MiniGoParser.ForConditionContext,0)


        def initilization(self):
            return self.getTypedRuleContext(MiniGoParser.InitilizationContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def forUpdate(self):
            return self.getTypedRuleContext(MiniGoParser.ForUpdateContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




    def forLoop(self):

        localctx = MiniGoParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_forLoop)
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.forCondition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.initilization()
                self.state = 335
                self.match(MiniGoParser.SEMI)
                self.state = 336
                self.forCondition()
                self.state = 337
                self.match(MiniGoParser.SEMI)
                self.state = 338
                self.forUpdate()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitilizationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def SHORTASSIGNOP(self):
            return self.getToken(MiniGoParser.SHORTASSIGNOP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_initilization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitilization" ):
                return visitor.visitInitilization(self)
            else:
                return visitor.visitChildren(self)




    def initilization(self):

        localctx = MiniGoParser.InitilizationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_initilization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 343
            self.match(MiniGoParser.SHORTASSIGNOP)
            self.state = 344
            self.expression(0)
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

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forCondition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




    def forCondition(self):

        localctx = MiniGoParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.expression(0)
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

        def assignmentOperator(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentOperatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forUpdate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = MiniGoParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 349
            self.assignmentOperator()
            self.state = 350
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForIterationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def SHORTASSIGNOP(self):
            return self.getToken(MiniGoParser.SHORTASSIGNOP, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def BLANK(self):
            return self.getToken(MiniGoParser.BLANK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_forIteration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForIteration" ):
                return visitor.visitForIteration(self)
            else:
                return visitor.visitChildren(self)




    def forIteration(self):

        localctx = MiniGoParser.ForIterationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_forIteration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.IDENTIFIER or _la==MiniGoParser.BLANK):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 353
            self.match(MiniGoParser.COMMA)
            self.state = 354
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 355
            self.match(MiniGoParser.SHORTASSIGNOP)
            self.state = 356
            self.match(MiniGoParser.RANGE)
            self.state = 357
            self.match(MiniGoParser.IDENTIFIER)
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

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = MiniGoParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(MiniGoParser.BREAK)
            self.state = 360
            self.match(MiniGoParser.SEMI)
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

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continueStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = MiniGoParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(MiniGoParser.CONTINUE)
            self.state = 363
            self.match(MiniGoParser.SEMI)
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def LP(self):
            return self.getToken(MiniGoParser.LP, 0)

        def RP(self):
            return self.getToken(MiniGoParser.RP, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_callStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def callStatement(self):

        localctx = MiniGoParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_callStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.DOT:
                self.state = 366
                self.match(MiniGoParser.DOT)
                self.state = 367
                self.match(MiniGoParser.IDENTIFIER)


            self.state = 370
            self.match(MiniGoParser.LP)
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.SUBOP) | (1 << MiniGoParser.NOTOP) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 371
                self.expression(0)
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 372
                    self.match(MiniGoParser.COMMA)
                    self.state = 373
                    self.expression(0)
                    self.state = 378
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 381
            self.match(MiniGoParser.RP)
            self.state = 382
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MiniGoParser.LB, 0)

        def RB(self):
            return self.getToken(MiniGoParser.RB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(MiniGoParser.LB)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 385
                self.statement()
                self.state = 390
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 391
            self.match(MiniGoParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDimsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LSB)
            else:
                return self.getToken(MiniGoParser.LSB, i)

        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INTLIT)
            else:
                return self.getToken(MiniGoParser.INTLIT, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RSB)
            else:
                return self.getToken(MiniGoParser.RSB, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayDims

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDims" ):
                return visitor.visitArrayDims(self)
            else:
                return visitor.visitChildren(self)




    def arrayDims(self):

        localctx = MiniGoParser.ArrayDimsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_arrayDims)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 393
                    self.match(MiniGoParser.LSB)
                    self.state = 394
                    self.match(MiniGoParser.INTLIT)
                    self.state = 395
                    self.match(MiniGoParser.RSB)

                else:
                    raise NoViableAltException(self)
                self.state = 398 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MiniGoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(MiniGoParser.RETURN)
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.SUBOP) | (1 << MiniGoParser.NOTOP) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 401
                self.expression(0)


            self.state = 404
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
        self._predicates[18] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




