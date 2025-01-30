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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u01ef\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\3\2\7\2`\n\2\f\2\16\2c\13\2\3\2\5\2f\n\2\3\2\7\2")
        buf.write("i\n\2\f\2\16\2l\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6\u0080\n\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\7\7\u0088\n\7\f\7\16\7\u008b\13")
        buf.write("\7\3\7\5\7\u008e\n\7\3\7\3\7\5\7\u0092\n\7\3\7\3\7\5\7")
        buf.write("\u0096\n\7\3\b\3\b\3\b\3\b\5\b\u009c\n\b\3\b\3\b\5\b\u00a0")
        buf.write("\n\b\3\b\5\b\u00a3\n\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u00ab")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\5\13\u00ba\n\13\3\13\3\13\5\13\u00be\n\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\7\f\u00c5\n\f\f\f\16\f\u00c8\13\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\7\16\u00d3\n\16")
        buf.write("\f\16\16\16\u00d6\13\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\7\17\u00de\n\17\f\17\16\17\u00e1\13\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\7\20\u00e8\n\20\f\20\16\20\u00eb\13\20\3\21")
        buf.write("\3\21\3\21\5\21\u00f0\n\21\3\21\3\21\3\22\3\22\3\22\7")
        buf.write("\22\u00f7\n\22\f\22\16\22\u00fa\13\22\3\23\3\23\5\23\u00fe")
        buf.write("\n\23\3\23\3\23\3\24\3\24\3\25\3\25\3\25\7\25\u0107\n")
        buf.write("\25\f\25\16\25\u010a\13\25\3\26\3\26\3\26\7\26\u010f\n")
        buf.write("\26\f\26\16\26\u0112\13\26\3\27\3\27\3\27\7\27\u0117\n")
        buf.write("\27\f\27\16\27\u011a\13\27\3\30\3\30\3\30\7\30\u011f\n")
        buf.write("\30\f\30\16\30\u0122\13\30\3\31\3\31\3\31\7\31\u0127\n")
        buf.write("\31\f\31\16\31\u012a\13\31\3\32\3\32\3\32\5\32\u012f\n")
        buf.write("\32\3\33\3\33\3\33\3\33\3\33\5\33\u0136\n\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0142\n")
        buf.write("\34\3\34\5\34\u0145\n\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0153\n\35\3\35\3")
        buf.write("\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\7\37\u0161\n\37\f\37\16\37\u0164\13\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\7\37\u016c\n\37\f\37\16\37\u016f\13\37")
        buf.write("\3\37\3\37\5\37\u0173\n\37\3 \3 \3 \3 \3 \3 \5 \u017b")
        buf.write("\n \7 \u017d\n \f \16 \u0180\13 \3 \3 \3!\3!\3!\3!\5!")
        buf.write("\u0188\n!\3!\3!\3!\5!\u018d\n!\3\"\3\"\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\3#\7#\u0199\n#\f#\16#\u019c\13#\3#\3#\5#\u01a0")
        buf.write("\n#\3$\3$\3$\5$\u01a5\n$\3$\3$\3%\3%\3%\3%\3%\3%\3%\5")
        buf.write("%\u01b0\n%\3&\3&\3&\3&\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3*\3*\3+\3+\3,\3,\3,\5,\u01ca\n,\3,\3,\3,\3")
        buf.write(",\7,\u01d0\n,\f,\16,\u01d3\13,\5,\u01d5\n,\3,\3,\3-\3")
        buf.write("-\5-\u01db\n-\3.\3.\7.\u01df\n.\f.\16.\u01e2\13.\3.\3")
        buf.write(".\3/\3/\5/\u01e8\n/\3/\6/\u01eb\n/\r/\16/\u01ec\3/\2\2")
        buf.write("\60\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\\2\n\4\2\f\1788\4\3\66\66")
        buf.write("??\3\2\37$\3\2\32\33\3\2\34\36\4\2\33\33\'\'\4\2\31\31")
        buf.write("(,\4\2..88\2\u0206\2a\3\2\2\2\4o\3\2\2\2\6v\3\2\2\2\b")
        buf.write("x\3\2\2\2\n\177\3\2\2\2\f\u0083\3\2\2\2\16\u0097\3\2\2")
        buf.write("\2\20\u00a6\3\2\2\2\22\u00ac\3\2\2\2\24\u00b1\3\2\2\2")
        buf.write("\26\u00c1\3\2\2\2\30\u00cb\3\2\2\2\32\u00cf\3\2\2\2\34")
        buf.write("\u00d9\3\2\2\2\36\u00e4\3\2\2\2 \u00ec\3\2\2\2\"\u00f3")
        buf.write("\3\2\2\2$\u00fb\3\2\2\2&\u0101\3\2\2\2(\u0103\3\2\2\2")
        buf.write("*\u010b\3\2\2\2,\u0113\3\2\2\2.\u011b\3\2\2\2\60\u0123")
        buf.write("\3\2\2\2\62\u012e\3\2\2\2\64\u0135\3\2\2\2\66\u0144\3")
        buf.write("\2\2\28\u0152\3\2\2\2:\u0156\3\2\2\2<\u0172\3\2\2\2>\u0174")
        buf.write("\3\2\2\2@\u0183\3\2\2\2B\u018e\3\2\2\2D\u0190\3\2\2\2")
        buf.write("F\u01a1\3\2\2\2H\u01af\3\2\2\2J\u01b1\3\2\2\2L\u01b5\3")
        buf.write("\2\2\2N\u01b7\3\2\2\2P\u01bb\3\2\2\2R\u01c2\3\2\2\2T\u01c4")
        buf.write("\3\2\2\2V\u01c6\3\2\2\2X\u01d8\3\2\2\2Z\u01dc\3\2\2\2")
        buf.write("\\\u01ea\3\2\2\2^`\5\n\6\2_^\3\2\2\2`c\3\2\2\2a_\3\2\2")
        buf.write("\2ab\3\2\2\2be\3\2\2\2ca\3\2\2\2df\5\4\3\2ed\3\2\2\2e")
        buf.write("f\3\2\2\2fj\3\2\2\2gi\5\n\6\2hg\3\2\2\2il\3\2\2\2jh\3")
        buf.write("\2\2\2jk\3\2\2\2km\3\2\2\2lj\3\2\2\2mn\7\2\2\3n\3\3\2")
        buf.write("\2\2op\7\b\2\2pq\7\3\2\2qr\7/\2\2rs\7\60\2\2st\5Z.\2t")
        buf.write("u\5\b\5\2u\5\3\2\2\2vw\t\2\2\2w\7\3\2\2\2xy\t\3\2\2y\t")
        buf.write("\3\2\2\2z\u0080\5\f\7\2{\u0080\5\16\b\2|\u0080\5\20\t")
        buf.write("\2}\u0080\5\22\n\2~\u0080\5\24\13\2\177z\3\2\2\2\177{")
        buf.write("\3\2\2\2\177|\3\2\2\2\177}\3\2\2\2\177~\3\2\2\2\u0080")
        buf.write("\u0081\3\2\2\2\u0081\u0082\5\b\5\2\u0082\13\3\2\2\2\u0083")
        buf.write("\u0084\7\24\2\2\u0084\u0089\78\2\2\u0085\u0086\7\65\2")
        buf.write("\2\u0086\u0088\78\2\2\u0087\u0085\3\2\2\2\u0088\u008b")
        buf.write("\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a")
        buf.write("\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u008e\5\\/\2")
        buf.write("\u008d\u008c\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u0095\3")
        buf.write("\2\2\2\u008f\u0096\5\6\4\2\u0090\u0092\5\6\4\2\u0091\u0090")
        buf.write("\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\3\2\2\2\u0093")
        buf.write("\u0094\7\30\2\2\u0094\u0096\5&\24\2\u0095\u008f\3\2\2")
        buf.write("\2\u0095\u0091\3\2\2\2\u0096\r\3\2\2\2\u0097\u0098\7\b")
        buf.write("\2\2\u0098\u0099\78\2\2\u0099\u009b\7/\2\2\u009a\u009c")
        buf.write("\5\"\22\2\u009b\u009a\3\2\2\2\u009b\u009c\3\2\2\2\u009c")
        buf.write("\u009d\3\2\2\2\u009d\u00a2\7\60\2\2\u009e\u00a0\5\\/\2")
        buf.write("\u009f\u009e\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3")
        buf.write("\2\2\2\u00a1\u00a3\5\6\4\2\u00a2\u009f\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\5Z.\2\u00a5\17")
        buf.write("\3\2\2\2\u00a6\u00a7\7\t\2\2\u00a7\u00aa\78\2\2\u00a8")
        buf.write("\u00ab\5\26\f\2\u00a9\u00ab\5\32\16\2\u00aa\u00a8\3\2")
        buf.write("\2\2\u00aa\u00a9\3\2\2\2\u00ab\21\3\2\2\2\u00ac\u00ad")
        buf.write("\7\23\2\2\u00ad\u00ae\78\2\2\u00ae\u00af\7\30\2\2\u00af")
        buf.write("\u00b0\5&\24\2\u00b0\23\3\2\2\2\u00b1\u00b2\7\b\2\2\u00b2")
        buf.write("\u00b3\7/\2\2\u00b3\u00b4\78\2\2\u00b4\u00b5\78\2\2\u00b5")
        buf.write("\u00b6\7\60\2\2\u00b6\u00b7\78\2\2\u00b7\u00b9\7/\2\2")
        buf.write("\u00b8\u00ba\5\"\22\2\u00b9\u00b8\3\2\2\2\u00b9\u00ba")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bd\7\60\2\2\u00bc")
        buf.write("\u00be\5\6\4\2\u00bd\u00bc\3\2\2\2\u00bd\u00be\3\2\2\2")
        buf.write("\u00be\u00bf\3\2\2\2\u00bf\u00c0\5Z.\2\u00c0\25\3\2\2")
        buf.write("\2\u00c1\u00c2\7\n\2\2\u00c2\u00c6\7\61\2\2\u00c3\u00c5")
        buf.write("\5\30\r\2\u00c4\u00c3\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c9\3\2\2\2")
        buf.write("\u00c8\u00c6\3\2\2\2\u00c9\u00ca\7\62\2\2\u00ca\27\3\2")
        buf.write("\2\2\u00cb\u00cc\78\2\2\u00cc\u00cd\5\6\4\2\u00cd\u00ce")
        buf.write("\5\b\5\2\u00ce\31\3\2\2\2\u00cf\u00d0\7\13\2\2\u00d0\u00d4")
        buf.write("\7\61\2\2\u00d1\u00d3\5 \21\2\u00d2\u00d1\3\2\2\2\u00d3")
        buf.write("\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2")
        buf.write("\u00d5\u00d7\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8\7")
        buf.write("\62\2\2\u00d8\33\3\2\2\2\u00d9\u00df\7/\2\2\u00da\u00db")
        buf.write("\5\36\20\2\u00db\u00dc\5\6\4\2\u00dc\u00de\3\2\2\2\u00dd")
        buf.write("\u00da\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2")
        buf.write("\u00df\u00e0\3\2\2\2\u00e0\u00e2\3\2\2\2\u00e1\u00df\3")
        buf.write("\2\2\2\u00e2\u00e3\7\60\2\2\u00e3\35\3\2\2\2\u00e4\u00e9")
        buf.write("\78\2\2\u00e5\u00e6\7\65\2\2\u00e6\u00e8\78\2\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3\2\2\2")
        buf.write("\u00e9\u00ea\3\2\2\2\u00ea\37\3\2\2\2\u00eb\u00e9\3\2")
        buf.write("\2\2\u00ec\u00ed\78\2\2\u00ed\u00ef\5\34\17\2\u00ee\u00f0")
        buf.write("\5\6\4\2\u00ef\u00ee\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0")
        buf.write("\u00f1\3\2\2\2\u00f1\u00f2\5\b\5\2\u00f2!\3\2\2\2\u00f3")
        buf.write("\u00f8\5$\23\2\u00f4\u00f5\7\65\2\2\u00f5\u00f7\5$\23")
        buf.write("\2\u00f6\u00f4\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6")
        buf.write("\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9#\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fb\u00fd\78\2\2\u00fc\u00fe\5\\/\2\u00fd\u00fc")
        buf.write("\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff")
        buf.write("\u0100\5\6\4\2\u0100%\3\2\2\2\u0101\u0102\5(\25\2\u0102")
        buf.write("\'\3\2\2\2\u0103\u0108\5*\26\2\u0104\u0105\7&\2\2\u0105")
        buf.write("\u0107\5(\25\2\u0106\u0104\3\2\2\2\u0107\u010a\3\2\2\2")
        buf.write("\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109)\3\2\2")
        buf.write("\2\u010a\u0108\3\2\2\2\u010b\u0110\5,\27\2\u010c\u010d")
        buf.write("\7%\2\2\u010d\u010f\5*\26\2\u010e\u010c\3\2\2\2\u010f")
        buf.write("\u0112\3\2\2\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2")
        buf.write("\u0111+\3\2\2\2\u0112\u0110\3\2\2\2\u0113\u0118\5.\30")
        buf.write("\2\u0114\u0115\t\4\2\2\u0115\u0117\5.\30\2\u0116\u0114")
        buf.write("\3\2\2\2\u0117\u011a\3\2\2\2\u0118\u0116\3\2\2\2\u0118")
        buf.write("\u0119\3\2\2\2\u0119-\3\2\2\2\u011a\u0118\3\2\2\2\u011b")
        buf.write("\u0120\5\60\31\2\u011c\u011d\t\5\2\2\u011d\u011f\5\60")
        buf.write("\31\2\u011e\u011c\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e")
        buf.write("\3\2\2\2\u0120\u0121\3\2\2\2\u0121/\3\2\2\2\u0122\u0120")
        buf.write("\3\2\2\2\u0123\u0128\5\62\32\2\u0124\u0125\t\6\2\2\u0125")
        buf.write("\u0127\5\62\32\2\u0126\u0124\3\2\2\2\u0127\u012a\3\2\2")
        buf.write("\2\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129\61\3")
        buf.write("\2\2\2\u012a\u0128\3\2\2\2\u012b\u012c\t\7\2\2\u012c\u012f")
        buf.write("\5\62\32\2\u012d\u012f\5\64\33\2\u012e\u012b\3\2\2\2\u012e")
        buf.write("\u012d\3\2\2\2\u012f\63\3\2\2\2\u0130\u0136\5\66\34\2")
        buf.write("\u0131\u0132\7/\2\2\u0132\u0133\5&\24\2\u0133\u0134\7")
        buf.write("\60\2\2\u0134\u0136\3\2\2\2\u0135\u0130\3\2\2\2\u0135")
        buf.write("\u0131\3\2\2\2\u0136\65\3\2\2\2\u0137\u0145\79\2\2\u0138")
        buf.write("\u0145\7:\2\2\u0139\u0145\7;\2\2\u013a\u0145\7\20\2\2")
        buf.write("\u013b\u0145\7\21\2\2\u013c\u0145\7\22\2\2\u013d\u0141")
        buf.write("\78\2\2\u013e\u0142\5\\/\2\u013f\u0140\7-\2\2\u0140\u0142")
        buf.write("\78\2\2\u0141\u013e\3\2\2\2\u0141\u013f\3\2\2\2\u0141")
        buf.write("\u0142\3\2\2\2\u0142\u0145\3\2\2\2\u0143\u0145\5V,\2\u0144")
        buf.write("\u0137\3\2\2\2\u0144\u0138\3\2\2\2\u0144\u0139\3\2\2\2")
        buf.write("\u0144\u013a\3\2\2\2\u0144\u013b\3\2\2\2\u0144\u013c\3")
        buf.write("\2\2\2\u0144\u013d\3\2\2\2\u0144\u0143\3\2\2\2\u0145\67")
        buf.write("\3\2\2\2\u0146\u0153\5@!\2\u0147\u0153\5D#\2\u0148\u0153")
        buf.write("\5F$\2\u0149\u0153\5R*\2\u014a\u0153\5T+\2\u014b\u0153")
        buf.write("\5V,\2\u014c\u0153\5X-\2\u014d\u0153\5:\36\2\u014e\u0153")
        buf.write("\5\f\7\2\u014f\u0153\5\20\t\2\u0150\u0153\5\24\13\2\u0151")
        buf.write("\u0153\5\22\n\2\u0152\u0146\3\2\2\2\u0152\u0147\3\2\2")
        buf.write("\2\u0152\u0148\3\2\2\2\u0152\u0149\3\2\2\2\u0152\u014a")
        buf.write("\3\2\2\2\u0152\u014b\3\2\2\2\u0152\u014c\3\2\2\2\u0152")
        buf.write("\u014d\3\2\2\2\u0152\u014e\3\2\2\2\u0152\u014f\3\2\2\2")
        buf.write("\u0152\u0150\3\2\2\2\u0152\u0151\3\2\2\2\u0153\u0154\3")
        buf.write("\2\2\2\u0154\u0155\5\b\5\2\u01559\3\2\2\2\u0156\u0157")
        buf.write("\78\2\2\u0157\u0158\7\31\2\2\u0158\u0159\5\\/\2\u0159")
        buf.write("\u015a\5\6\4\2\u015a\u015b\5<\37\2\u015b;\3\2\2\2\u015c")
        buf.write("\u015d\7\61\2\2\u015d\u0162\5<\37\2\u015e\u015f\7\65\2")
        buf.write("\2\u015f\u0161\5<\37\2\u0160\u015e\3\2\2\2\u0161\u0164")
        buf.write("\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("\u0165\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u0166\7\62\2")
        buf.write("\2\u0166\u0173\3\2\2\2\u0167\u0168\7\61\2\2\u0168\u016d")
        buf.write("\5&\24\2\u0169\u016a\7\65\2\2\u016a\u016c\5&\24\2\u016b")
        buf.write("\u0169\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2")
        buf.write("\u016d\u016e\3\2\2\2\u016e\u0170\3\2\2\2\u016f\u016d\3")
        buf.write("\2\2\2\u0170\u0171\7\62\2\2\u0171\u0173\3\2\2\2\u0172")
        buf.write("\u015c\3\2\2\2\u0172\u0167\3\2\2\2\u0173=\3\2\2\2\u0174")
        buf.write("\u0175\78\2\2\u0175\u017e\7\61\2\2\u0176\u0177\78\2\2")
        buf.write("\u0177\u0178\7\67\2\2\u0178\u017a\5&\24\2\u0179\u017b")
        buf.write("\7\65\2\2\u017a\u0179\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write("\u017d\3\2\2\2\u017c\u0176\3\2\2\2\u017d\u0180\3\2\2\2")
        buf.write("\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0181\3")
        buf.write("\2\2\2\u0180\u017e\3\2\2\2\u0181\u0182\7\62\2\2\u0182")
        buf.write("?\3\2\2\2\u0183\u0187\78\2\2\u0184\u0188\5\\/\2\u0185")
        buf.write("\u0186\7-\2\2\u0186\u0188\78\2\2\u0187\u0184\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\3\2\2\2")
        buf.write("\u0189\u018c\5B\"\2\u018a\u018d\5&\24\2\u018b\u018d\5")
        buf.write("> \2\u018c\u018a\3\2\2\2\u018c\u018b\3\2\2\2\u018dA\3")
        buf.write("\2\2\2\u018e\u018f\t\b\2\2\u018fC\3\2\2\2\u0190\u0191")
        buf.write("\7\4\2\2\u0191\u0192\5&\24\2\u0192\u019a\5Z.\2\u0193\u0194")
        buf.write("\7\5\2\2\u0194\u0195\7\4\2\2\u0195\u0196\5&\24\2\u0196")
        buf.write("\u0197\5Z.\2\u0197\u0199\3\2\2\2\u0198\u0193\3\2\2\2\u0199")
        buf.write("\u019c\3\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2")
        buf.write("\u019b\u019f\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u019e\7")
        buf.write("\5\2\2\u019e\u01a0\5Z.\2\u019f\u019d\3\2\2\2\u019f\u01a0")
        buf.write("\3\2\2\2\u01a0E\3\2\2\2\u01a1\u01a4\7\6\2\2\u01a2\u01a5")
        buf.write("\5H%\2\u01a3\u01a5\5P)\2\u01a4\u01a2\3\2\2\2\u01a4\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a7\5Z.\2\u01a7G")
        buf.write("\3\2\2\2\u01a8\u01b0\5L\'\2\u01a9\u01aa\5J&\2\u01aa\u01ab")
        buf.write("\7\66\2\2\u01ab\u01ac\5L\'\2\u01ac\u01ad\7\66\2\2\u01ad")
        buf.write("\u01ae\5N(\2\u01ae\u01b0\3\2\2\2\u01af\u01a8\3\2\2\2\u01af")
        buf.write("\u01a9\3\2\2\2\u01b0I\3\2\2\2\u01b1\u01b2\78\2\2\u01b2")
        buf.write("\u01b3\7\31\2\2\u01b3\u01b4\5&\24\2\u01b4K\3\2\2\2\u01b5")
        buf.write("\u01b6\5&\24\2\u01b6M\3\2\2\2\u01b7\u01b8\78\2\2\u01b8")
        buf.write("\u01b9\5B\"\2\u01b9\u01ba\5&\24\2\u01baO\3\2\2\2\u01bb")
        buf.write("\u01bc\t\t\2\2\u01bc\u01bd\7\65\2\2\u01bd\u01be\78\2\2")
        buf.write("\u01be\u01bf\7\31\2\2\u01bf\u01c0\7\27\2\2\u01c0\u01c1")
        buf.write("\78\2\2\u01c1Q\3\2\2\2\u01c2\u01c3\7\26\2\2\u01c3S\3\2")
        buf.write("\2\2\u01c4\u01c5\7\25\2\2\u01c5U\3\2\2\2\u01c6\u01c9\7")
        buf.write("8\2\2\u01c7\u01c8\7-\2\2\u01c8\u01ca\78\2\2\u01c9\u01c7")
        buf.write("\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb")
        buf.write("\u01d4\7/\2\2\u01cc\u01d1\5&\24\2\u01cd\u01ce\7\65\2\2")
        buf.write("\u01ce\u01d0\5&\24\2\u01cf\u01cd\3\2\2\2\u01d0\u01d3\3")
        buf.write("\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d5")
        buf.write("\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d4\u01cc\3\2\2\2\u01d4")
        buf.write("\u01d5\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d7\7\60\2")
        buf.write("\2\u01d7W\3\2\2\2\u01d8\u01da\7\7\2\2\u01d9\u01db\5&\24")
        buf.write("\2\u01da\u01d9\3\2\2\2\u01da\u01db\3\2\2\2\u01dbY\3\2")
        buf.write("\2\2\u01dc\u01e0\7\61\2\2\u01dd\u01df\58\35\2\u01de\u01dd")
        buf.write("\3\2\2\2\u01df\u01e2\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0")
        buf.write("\u01e1\3\2\2\2\u01e1\u01e3\3\2\2\2\u01e2\u01e0\3\2\2\2")
        buf.write("\u01e3\u01e4\7\62\2\2\u01e4[\3\2\2\2\u01e5\u01e7\7\63")
        buf.write("\2\2\u01e6\u01e8\5&\24\2\u01e7\u01e6\3\2\2\2\u01e7\u01e8")
        buf.write("\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01eb\7\64\2\2\u01ea")
        buf.write("\u01e5\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ea\3\2\2\2")
        buf.write("\u01ec\u01ed\3\2\2\2\u01ed]\3\2\2\2\63aej\177\u0089\u008d")
        buf.write("\u0091\u0095\u009b\u009f\u00a2\u00aa\u00b9\u00bd\u00c6")
        buf.write("\u00d4\u00df\u00e9\u00ef\u00f8\u00fd\u0108\u0110\u0118")
        buf.write("\u0120\u0128\u012e\u0135\u0141\u0144\u0152\u0162\u016d")
        buf.write("\u0172\u017a\u017e\u0187\u018c\u019a\u019f\u01a4\u01af")
        buf.write("\u01c9\u01d1\u01d4\u01da\u01e0\u01e7\u01ec")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'if'", "'else'", "'for'", "'return'", 
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

    symbolicNames = [ "<INVALID>", "<INVALID>", "IF", "ELSE", "FOR", "RETURN", 
                      "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                      "FLOAT", "BOOLEAN", "TRUE", "FALSE", "NIL", "CONST", 
                      "VAR", "CONTINUE", "BREAK", "RANGE", "ASSIGN", "DECLARE", 
                      "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQ", "NEQ", 
                      "LT", "LEQ", "GT", "GEQ", "AND", "OR", "NOT", "PLUS_ASSIGN", 
                      "MINUS_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "DOT", "BLANK", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACKET", "RBRACKET", "COMMA", "SEMI", "COLON", 
                      "IDENTIFIER", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "BLOCK_COMMENT", "LINE_COMMENT", "WS", "NEWLINE", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_mainFunction = 1
    RULE_baseType = 2
    RULE_endOfStatement = 3
    RULE_declaration = 4
    RULE_varDecl = 5
    RULE_funcDecl = 6
    RULE_typeDecl = 7
    RULE_constDecl = 8
    RULE_methodDecl = 9
    RULE_structDefinition = 10
    RULE_structFields = 11
    RULE_interfaceDefinition = 12
    RULE_listParams = 13
    RULE_listIdentifier = 14
    RULE_interfaceFields = 15
    RULE_funcParams = 16
    RULE_funcParam = 17
    RULE_expression = 18
    RULE_logicOrExp = 19
    RULE_logicAndExp = 20
    RULE_equalityExp = 21
    RULE_additiveExp = 22
    RULE_multiplicativeExp = 23
    RULE_unaryExp = 24
    RULE_primaryExp = 25
    RULE_term = 26
    RULE_statement = 27
    RULE_arrayLiteral = 28
    RULE_arraysBlock = 29
    RULE_structExpression = 30
    RULE_assignStatement = 31
    RULE_assignmentOperator = 32
    RULE_ifStatement = 33
    RULE_forStatement = 34
    RULE_forLoop = 35
    RULE_initilization = 36
    RULE_forCondition = 37
    RULE_forUpdate = 38
    RULE_forIteration = 39
    RULE_breakStatement = 40
    RULE_continueStatement = 41
    RULE_callStatement = 42
    RULE_returnStatement = 43
    RULE_block = 44
    RULE_arrayDims = 45

    ruleNames =  [ "program", "mainFunction", "baseType", "endOfStatement", 
                   "declaration", "varDecl", "funcDecl", "typeDecl", "constDecl", 
                   "methodDecl", "structDefinition", "structFields", "interfaceDefinition", 
                   "listParams", "listIdentifier", "interfaceFields", "funcParams", 
                   "funcParam", "expression", "logicOrExp", "logicAndExp", 
                   "equalityExp", "additiveExp", "multiplicativeExp", "unaryExp", 
                   "primaryExp", "term", "statement", "arrayLiteral", "arraysBlock", 
                   "structExpression", "assignStatement", "assignmentOperator", 
                   "ifStatement", "forStatement", "forLoop", "initilization", 
                   "forCondition", "forUpdate", "forIteration", "breakStatement", 
                   "continueStatement", "callStatement", "returnStatement", 
                   "block", "arrayDims" ]

    EOF = Token.EOF
    T__0=1
    IF=2
    ELSE=3
    FOR=4
    RETURN=5
    FUNC=6
    TYPE=7
    STRUCT=8
    INTERFACE=9
    STRING=10
    INT=11
    FLOAT=12
    BOOLEAN=13
    TRUE=14
    FALSE=15
    NIL=16
    CONST=17
    VAR=18
    CONTINUE=19
    BREAK=20
    RANGE=21
    ASSIGN=22
    DECLARE=23
    PLUS=24
    MINUS=25
    MUL=26
    DIV=27
    MOD=28
    EQ=29
    NEQ=30
    LT=31
    LEQ=32
    GT=33
    GEQ=34
    AND=35
    OR=36
    NOT=37
    PLUS_ASSIGN=38
    MINUS_ASSIGN=39
    MUL_ASSIGN=40
    DIV_ASSIGN=41
    MOD_ASSIGN=42
    DOT=43
    BLANK=44
    LPAREN=45
    RPAREN=46
    LBRACE=47
    RBRACE=48
    LBRACKET=49
    RBRACKET=50
    COMMA=51
    SEMI=52
    COLON=53
    IDENTIFIER=54
    INT_LIT=55
    FLOAT_LIT=56
    STRING_LIT=57
    BLOCK_COMMENT=58
    LINE_COMMENT=59
    WS=60
    NEWLINE=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    ERROR_CHAR=64

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


        def mainFunction(self):
            return self.getTypedRuleContext(MiniGoParser.MainFunctionContext,0)


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
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 92
                    self.declaration() 
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 98
                self.mainFunction()


            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0):
                self.state = 101
                self.declaration()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_mainFunction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainFunction" ):
                return visitor.visitMainFunction(self)
            else:
                return visitor.visitChildren(self)




    def mainFunction(self):

        localctx = MiniGoParser.MainFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mainFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(MiniGoParser.FUNC)
            self.state = 110
            self.match(MiniGoParser.T__0)
            self.state = 111
            self.match(MiniGoParser.LPAREN)
            self.state = 112
            self.match(MiniGoParser.RPAREN)
            self.state = 113
            self.block()
            self.state = 114
            self.endOfStatement()
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
        self.enterRule(localctx, 4, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
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

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

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
        self.enterRule(localctx, 6, self.RULE_endOfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not(((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.SEMI - -1)) | (1 << (MiniGoParser.NEWLINE - -1)))) != 0)):
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


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


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
            return MiniGoParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MiniGoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 120
                self.varDecl()
                pass

            elif la_ == 2:
                self.state = 121
                self.funcDecl()
                pass

            elif la_ == 3:
                self.state = 122
                self.typeDecl()
                pass

            elif la_ == 4:
                self.state = 123
                self.constDecl()
                pass

            elif la_ == 5:
                self.state = 124
                self.methodDecl()
                pass


            self.state = 127
            self.endOfStatement()
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

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
        self.enterRule(localctx, 10, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(MiniGoParser.VAR)
            self.state = 130
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 131
                self.match(MiniGoParser.COMMA)
                self.state = 132
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 138
                self.arrayDims()


            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 141
                self.baseType()
                pass

            elif la_ == 2:
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 142
                    self.baseType()


                self.state = 145
                self.match(MiniGoParser.ASSIGN)
                self.state = 146
                self.expression()
                pass


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

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def funcParams(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamsContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = MiniGoParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(MiniGoParser.FUNC)
            self.state = 150
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 151
            self.match(MiniGoParser.LPAREN)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 152
                self.funcParams()


            self.state = 155
            self.match(MiniGoParser.RPAREN)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACKET:
                    self.state = 156
                    self.arrayDims()


                self.state = 159
                self.baseType()


            self.state = 162
            self.block()
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

        def structDefinition(self):
            return self.getTypedRuleContext(MiniGoParser.StructDefinitionContext,0)


        def interfaceDefinition(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceDefinitionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typeDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeDecl" ):
                return visitor.visitTypeDecl(self)
            else:
                return visitor.visitChildren(self)




    def typeDecl(self):

        localctx = MiniGoParser.TypeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(MiniGoParser.TYPE)
            self.state = 165
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.state = 166
                self.structDefinition()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 167
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


    class ConstDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDecl" ):
                return visitor.visitConstDecl(self)
            else:
                return visitor.visitChildren(self)




    def constDecl(self):

        localctx = MiniGoParser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(MiniGoParser.CONST)
            self.state = 171
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 172
            self.match(MiniGoParser.ASSIGN)
            self.state = 173
            self.expression()
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

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def funcParams(self):
            return self.getTypedRuleContext(MiniGoParser.FuncParamsContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = MiniGoParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(MiniGoParser.FUNC)
            self.state = 176
            self.match(MiniGoParser.LPAREN)
            self.state = 177
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 178
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 179
            self.match(MiniGoParser.RPAREN)
            self.state = 180
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 181
            self.match(MiniGoParser.LPAREN)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 182
                self.funcParams()


            self.state = 185
            self.match(MiniGoParser.RPAREN)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 186
                self.baseType()


            self.state = 189
            self.block()
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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def structFields(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StructFieldsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StructFieldsContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(MiniGoParser.STRUCT)
            self.state = 192
            self.match(MiniGoParser.LBRACE)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 193
                self.structFields()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199
            self.match(MiniGoParser.RBRACE)
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

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 202
            self.baseType()
            self.state = 203
            self.endOfStatement()
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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def interfaceFields(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.InterfaceFieldsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.InterfaceFieldsContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(MiniGoParser.INTERFACE)
            self.state = 206
            self.match(MiniGoParser.LBRACE)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 207
                self.interfaceFields()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 213
            self.match(MiniGoParser.RBRACE)
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

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def listIdentifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ListIdentifierContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ListIdentifierContext,i)


        def baseType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BaseTypeContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_listParams

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListParams" ):
                return visitor.visitListParams(self)
            else:
                return visitor.visitChildren(self)




    def listParams(self):

        localctx = MiniGoParser.ListParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_listParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(MiniGoParser.LPAREN)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 216
                self.listIdentifier()
                self.state = 217
                self.baseType()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 224
            self.match(MiniGoParser.RPAREN)
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
        self.enterRule(localctx, 28, self.RULE_listIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 227
                self.match(MiniGoParser.COMMA)
                self.state = 228
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceFields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceFields" ):
                return visitor.visitInterfaceFields(self)
            else:
                return visitor.visitChildren(self)




    def interfaceFields(self):

        localctx = MiniGoParser.InterfaceFieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_interfaceFields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 235
            self.listParams()
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 236
                self.baseType()


            self.state = 239
            self.endOfStatement()
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
            self.state = 241
            self.funcParam()
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 242
                self.match(MiniGoParser.COMMA)
                self.state = 243
                self.funcParam()
                self.state = 248
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

        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(MiniGoParser.IDENTIFIER)

            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 250
                self.arrayDims()


            self.state = 253
            self.baseType()
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

        def logicOrExp(self):
            return self.getTypedRuleContext(MiniGoParser.LogicOrExpContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniGoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.logicOrExp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicOrExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicAndExp(self):
            return self.getTypedRuleContext(MiniGoParser.LogicAndExpContext,0)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.OR)
            else:
                return self.getToken(MiniGoParser.OR, i)

        def logicOrExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.LogicOrExpContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.LogicOrExpContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_logicOrExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOrExp" ):
                return visitor.visitLogicOrExp(self)
            else:
                return visitor.visitChildren(self)




    def logicOrExp(self):

        localctx = MiniGoParser.LogicOrExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_logicOrExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.logicAndExp()
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 258
                    self.match(MiniGoParser.OR)
                    self.state = 259
                    self.logicOrExp() 
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicAndExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExp(self):
            return self.getTypedRuleContext(MiniGoParser.EqualityExpContext,0)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.AND)
            else:
                return self.getToken(MiniGoParser.AND, i)

        def logicAndExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.LogicAndExpContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.LogicAndExpContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_logicAndExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicAndExp" ):
                return visitor.visitLogicAndExp(self)
            else:
                return visitor.visitChildren(self)




    def logicAndExp(self):

        localctx = MiniGoParser.LogicAndExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_logicAndExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.equalityExp()
            self.state = 270
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 266
                    self.match(MiniGoParser.AND)
                    self.state = 267
                    self.logicAndExp() 
                self.state = 272
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.AdditiveExpContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.AdditiveExpContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.EQ)
            else:
                return self.getToken(MiniGoParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEQ)
            else:
                return self.getToken(MiniGoParser.NEQ, i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LT)
            else:
                return self.getToken(MiniGoParser.LT, i)

        def LEQ(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LEQ)
            else:
                return self.getToken(MiniGoParser.LEQ, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.GT)
            else:
                return self.getToken(MiniGoParser.GT, i)

        def GEQ(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.GEQ)
            else:
                return self.getToken(MiniGoParser.GEQ, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_equalityExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExp" ):
                return visitor.visitEqualityExp(self)
            else:
                return visitor.visitChildren(self)




    def equalityExp(self):

        localctx = MiniGoParser.EqualityExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_equalityExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.additiveExp()
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LEQ) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GEQ))) != 0):
                self.state = 274
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LEQ) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 275
                self.additiveExp()
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.MultiplicativeExpContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.MultiplicativeExpContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.PLUS)
            else:
                return self.getToken(MiniGoParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.MINUS)
            else:
                return self.getToken(MiniGoParser.MINUS, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_additiveExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExp" ):
                return visitor.visitAdditiveExp(self)
            else:
                return visitor.visitChildren(self)




    def additiveExp(self):

        localctx = MiniGoParser.AdditiveExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_additiveExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.multiplicativeExp()
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS:
                self.state = 282
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 283
                self.multiplicativeExp()
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.UnaryExpContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.UnaryExpContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.MUL)
            else:
                return self.getToken(MiniGoParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DIV)
            else:
                return self.getToken(MiniGoParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.MOD)
            else:
                return self.getToken(MiniGoParser.MOD, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_multiplicativeExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExp" ):
                return visitor.visitMultiplicativeExp(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExp(self):

        localctx = MiniGoParser.MultiplicativeExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_multiplicativeExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.unaryExp()
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0):
                self.state = 290
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 291
                self.unaryExp()
                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExp(self):
            return self.getTypedRuleContext(MiniGoParser.UnaryExpContext,0)


        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def primaryExp(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExpContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_unaryExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExp" ):
                return visitor.visitUnaryExp(self)
            else:
                return visitor.visitChildren(self)




    def unaryExp(self):

        localctx = MiniGoParser.UnaryExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_unaryExp)
        self._la = 0 # Token type
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 298
                self.unaryExp()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.LPAREN, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.primaryExp()
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


    class PrimaryExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(MiniGoParser.TermContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primaryExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExp" ):
                return visitor.visitPrimaryExp(self)
            else:
                return visitor.visitChildren(self)




    def primaryExp(self):

        localctx = MiniGoParser.PrimaryExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_primaryExp)
        try:
            self.state = 307
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.term()
                pass
            elif token in [MiniGoParser.LPAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.match(MiniGoParser.LPAREN)
                self.state = 304
                self.expression()
                self.state = 305
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def callStatement(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = MiniGoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_term)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 311
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 312
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 313
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 314
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 315
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 319
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.LBRACKET]:
                    self.state = 316
                    self.arrayDims()
                    pass
                elif token in [MiniGoParser.DOT]:
                    self.state = 317
                    self.match(MiniGoParser.DOT)
                    self.state = 318
                    self.match(MiniGoParser.IDENTIFIER)
                    pass
                elif token in [MiniGoParser.EOF, MiniGoParser.PLUS, MiniGoParser.MINUS, MiniGoParser.MUL, MiniGoParser.DIV, MiniGoParser.MOD, MiniGoParser.EQ, MiniGoParser.NEQ, MiniGoParser.LT, MiniGoParser.LEQ, MiniGoParser.GT, MiniGoParser.GEQ, MiniGoParser.AND, MiniGoParser.OR, MiniGoParser.RPAREN, MiniGoParser.LBRACE, MiniGoParser.RBRACE, MiniGoParser.RBRACKET, MiniGoParser.COMMA, MiniGoParser.SEMI, MiniGoParser.IDENTIFIER, MiniGoParser.NEWLINE]:
                    pass
                else:
                    pass
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 321
                self.callStatement()
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


        def arrayLiteral(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLiteralContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def typeDecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypeDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclContext,0)


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
        self.enterRule(localctx, 54, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 324
                self.assignStatement()
                pass

            elif la_ == 2:
                self.state = 325
                self.ifStatement()
                pass

            elif la_ == 3:
                self.state = 326
                self.forStatement()
                pass

            elif la_ == 4:
                self.state = 327
                self.breakStatement()
                pass

            elif la_ == 5:
                self.state = 328
                self.continueStatement()
                pass

            elif la_ == 6:
                self.state = 329
                self.callStatement()
                pass

            elif la_ == 7:
                self.state = 330
                self.returnStatement()
                pass

            elif la_ == 8:
                self.state = 331
                self.arrayLiteral()
                pass

            elif la_ == 9:
                self.state = 332
                self.varDecl()
                pass

            elif la_ == 10:
                self.state = 333
                self.typeDecl()
                pass

            elif la_ == 11:
                self.state = 334
                self.methodDecl()
                pass

            elif la_ == 12:
                self.state = 335
                self.constDecl()
                pass


            self.state = 338
            self.endOfStatement()
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

        def DECLARE(self):
            return self.getToken(MiniGoParser.DECLARE, 0)

        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def arraysBlock(self):
            return self.getTypedRuleContext(MiniGoParser.ArraysBlockContext,0)


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
        self.enterRule(localctx, 56, self.RULE_arrayLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 341
            self.match(MiniGoParser.DECLARE)

            self.state = 342
            self.arrayDims()
            self.state = 343
            self.baseType()
            self.state = 344
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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def arraysBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ArraysBlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ArraysBlockContext,i)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

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
        self.enterRule(localctx, 58, self.RULE_arraysBlock)
        self._la = 0 # Token type
        try:
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.match(MiniGoParser.LBRACE)
                self.state = 347
                self.arraysBlock()
                self.state = 352
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 348
                    self.match(MiniGoParser.COMMA)
                    self.state = 349
                    self.arraysBlock()
                    self.state = 354
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 355
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.match(MiniGoParser.LBRACE)
                self.state = 358
                self.expression()
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 359
                    self.match(MiniGoParser.COMMA)
                    self.state = 360
                    self.expression()
                    self.state = 365
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 366
                self.match(MiniGoParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COLON)
            else:
                return self.getToken(MiniGoParser.COLON, i)

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
            return MiniGoParser.RULE_structExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructExpression" ):
                return visitor.visitStructExpression(self)
            else:
                return visitor.visitChildren(self)




    def structExpression(self):

        localctx = MiniGoParser.StructExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_structExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 371
            self.match(MiniGoParser.LBRACE)
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 372
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 373
                self.match(MiniGoParser.COLON)
                self.state = 374
                self.expression()
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.COMMA:
                    self.state = 375
                    self.match(MiniGoParser.COMMA)


                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 383
            self.match(MiniGoParser.RBRACE)
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


        def structExpression(self):
            return self.getTypedRuleContext(MiniGoParser.StructExpressionContext,0)


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
        self.enterRule(localctx, 62, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACKET]:
                self.state = 386
                self.arrayDims()
                pass
            elif token in [MiniGoParser.DOT]:
                self.state = 387
                self.match(MiniGoParser.DOT)
                self.state = 388
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.DECLARE, MiniGoParser.PLUS_ASSIGN, MiniGoParser.MINUS_ASSIGN, MiniGoParser.MUL_ASSIGN, MiniGoParser.DIV_ASSIGN, MiniGoParser.MOD_ASSIGN]:
                pass
            else:
                pass
            self.state = 391
            self.assignmentOperator()
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 392
                self.expression()
                pass

            elif la_ == 2:
                self.state = 393
                self.structExpression()
                pass


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

        def DECLARE(self):
            return self.getToken(MiniGoParser.DECLARE, 0)

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
            return MiniGoParser.RULE_assignmentOperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = MiniGoParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DECLARE) | (1 << MiniGoParser.PLUS_ASSIGN) | (1 << MiniGoParser.MINUS_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


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
        self.enterRule(localctx, 66, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(MiniGoParser.IF)
            self.state = 399
            self.expression()
            self.state = 400
            self.block()
            self.state = 408
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 401
                    self.match(MiniGoParser.ELSE)
                    self.state = 402
                    self.match(MiniGoParser.IF)
                    self.state = 403
                    self.expression()
                    self.state = 404
                    self.block() 
                self.state = 410
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 411
                self.match(MiniGoParser.ELSE)
                self.state = 412
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
        self.enterRule(localctx, 68, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(MiniGoParser.FOR)
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 416
                self.forLoop()
                pass

            elif la_ == 2:
                self.state = 417
                self.forIteration()
                pass


            self.state = 420
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
        self.enterRule(localctx, 70, self.RULE_forLoop)
        try:
            self.state = 429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.forCondition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.initilization()
                self.state = 424
                self.match(MiniGoParser.SEMI)
                self.state = 425
                self.forCondition()
                self.state = 426
                self.match(MiniGoParser.SEMI)
                self.state = 427
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

        def DECLARE(self):
            return self.getToken(MiniGoParser.DECLARE, 0)

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
        self.enterRule(localctx, 72, self.RULE_initilization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 432
            self.match(MiniGoParser.DECLARE)
            self.state = 433
            self.expression()
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
        self.enterRule(localctx, 74, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.expression()
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
        self.enterRule(localctx, 76, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 438
            self.assignmentOperator()
            self.state = 439
            self.expression()
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

        def DECLARE(self):
            return self.getToken(MiniGoParser.DECLARE, 0)

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
        self.enterRule(localctx, 78, self.RULE_forIteration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.BLANK or _la==MiniGoParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 442
            self.match(MiniGoParser.COMMA)
            self.state = 443
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 444
            self.match(MiniGoParser.DECLARE)
            self.state = 445
            self.match(MiniGoParser.RANGE)
            self.state = 446
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

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = MiniGoParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
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
        self.enterRule(localctx, 82, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

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
        self.enterRule(localctx, 84, self.RULE_callStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.DOT:
                self.state = 453
                self.match(MiniGoParser.DOT)
                self.state = 454
                self.match(MiniGoParser.IDENTIFIER)


            self.state = 457
            self.match(MiniGoParser.LPAREN)
            self.state = 466
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 458
                self.expression()
                self.state = 463
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 459
                    self.match(MiniGoParser.COMMA)
                    self.state = 460
                    self.expression()
                    self.state = 465
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 468
            self.match(MiniGoParser.RPAREN)
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
        self.enterRule(localctx, 86, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(MiniGoParser.RETURN)
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 471
                self.expression()


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
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(MiniGoParser.LBRACE)
            self.state = 478
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 475
                self.statement()
                self.state = 480
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 481
            self.match(MiniGoParser.RBRACE)
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

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LBRACKET)
            else:
                return self.getToken(MiniGoParser.LBRACKET, i)

        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RBRACKET)
            else:
                return self.getToken(MiniGoParser.RBRACKET, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayDims

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDims" ):
                return visitor.visitArrayDims(self)
            else:
                return visitor.visitChildren(self)




    def arrayDims(self):

        localctx = MiniGoParser.ArrayDimsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_arrayDims)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 483
                self.match(MiniGoParser.LBRACKET)
                self.state = 485
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 484
                    self.expression()


                self.state = 487
                self.match(MiniGoParser.RBRACKET)
                self.state = 490 
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





