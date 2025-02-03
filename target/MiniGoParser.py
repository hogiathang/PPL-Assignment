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
        buf.write("\u0273\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\3\2\7\2l\n\2\f\2\16\2o\13\2\3\2\5\2r\n\2\3")
        buf.write("\2\7\2u\n\2\f\2\16\2x\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6\u008c")
        buf.write("\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0096\n\6\5\6")
        buf.write("\u0098\n\6\3\7\3\7\3\7\3\7\7\7\u009e\n\7\f\7\16\7\u00a1")
        buf.write("\13\7\3\7\5\7\u00a4\n\7\3\7\3\7\5\7\u00a8\n\7\3\7\3\7")
        buf.write("\5\7\u00ac\n\7\3\b\3\b\3\b\3\b\5\b\u00b2\n\b\3\b\3\b\5")
        buf.write("\b\u00b6\n\b\3\b\5\b\u00b9\n\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\5\t\u00c1\n\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00d0\n\13\3\13\3\13\5\13\u00d4")
        buf.write("\n\13\3\13\3\13\3\f\3\f\3\f\7\f\u00db\n\f\f\f\16\f\u00de")
        buf.write("\13\f\3\f\3\f\3\r\3\r\5\r\u00e4\n\r\3\r\3\r\5\r\u00e8")
        buf.write("\n\r\3\r\3\r\3\16\3\16\3\16\7\16\u00ef\n\16\f\16\16\16")
        buf.write("\u00f2\13\16\3\16\3\16\3\17\3\17\3\17\3\17\7\17\u00fa")
        buf.write("\n\17\f\17\16\17\u00fd\13\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\7\20\u0104\n\20\f\20\16\20\u0107\13\20\3\21\3\21\3\21")
        buf.write("\5\21\u010c\n\21\3\21\3\21\3\22\3\22\3\22\7\22\u0113\n")
        buf.write("\22\f\22\16\22\u0116\13\22\3\23\3\23\5\23\u011a\n\23\3")
        buf.write("\23\3\23\3\24\3\24\3\25\3\25\3\25\7\25\u0123\n\25\f\25")
        buf.write("\16\25\u0126\13\25\3\26\3\26\3\26\7\26\u012b\n\26\f\26")
        buf.write("\16\26\u012e\13\26\3\27\3\27\3\27\7\27\u0133\n\27\f\27")
        buf.write("\16\27\u0136\13\27\3\30\3\30\3\30\7\30\u013b\n\30\f\30")
        buf.write("\16\30\u013e\13\30\3\31\3\31\3\31\7\31\u0143\n\31\f\31")
        buf.write("\16\31\u0146\13\31\3\32\3\32\3\32\5\32\u014b\n\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\5\33\u0152\n\33\3\34\3\34\3\34\3")
        buf.write("\34\3\34\5\34\u0159\n\34\3\34\7\34\u015c\n\34\f\34\16")
        buf.write("\34\u015f\13\34\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0167")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0171")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\5\37\u0196\n\37\5\37\u0198\n\37\3 \3 ")
        buf.write("\3 \3 \3!\3!\3!\3!\7!\u01a2\n!\f!\16!\u01a5\13!\3!\3!")
        buf.write("\3!\3!\3!\3!\7!\u01ad\n!\f!\16!\u01b0\13!\3!\3!\5!\u01b4")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\7\"\u01bb\n\"\f\"\16\"\u01be\13")
        buf.write("\"\3\"\5\"\u01c1\n\"\5\"\u01c3\n\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\5#\u01ce\n#\3#\3#\3#\3#\5#\u01d4\n#\3#\7#\u01d7")
        buf.write("\n#\f#\16#\u01da\13#\3#\5#\u01dd\n#\5#\u01df\n#\3#\3#")
        buf.write("\5#\u01e3\n#\3$\3$\3$\3$\3%\3%\3%\7%\u01ec\n%\f%\16%\u01ef")
        buf.write("\13%\3%\3%\3%\3%\7%\u01f5\n%\f%\16%\u01f8\13%\3&\3&\3")
        buf.write("&\7&\u01fd\n&\f&\16&\u0200\13&\3&\5&\u0203\n&\3\'\3\'")
        buf.write("\3\'\5\'\u0208\n\'\3(\3(\3)\3)\3)\3)\5)\u0210\n)\3)\3")
        buf.write(")\3)\3)\3)\5)\u0217\n)\7)\u0219\n)\f)\16)\u021c\13)\3")
        buf.write(")\3)\5)\u0220\n)\3*\3*\3*\5*\u0225\n*\3*\3*\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\5+\u0230\n+\3,\3,\3,\3,\3-\3-\3.\3.\3.\3.\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\62")
        buf.write("\5\62\u024a\n\62\3\62\3\62\3\62\3\62\7\62\u0250\n\62\f")
        buf.write("\62\16\62\u0253\13\62\5\62\u0255\n\62\3\62\3\62\3\63\3")
        buf.write("\63\3\63\3\63\3\63\3\63\5\63\u025f\n\63\3\64\3\64\7\64")
        buf.write("\u0263\n\64\f\64\16\64\u0266\13\64\3\64\3\64\3\65\3\65")
        buf.write("\5\65\u026c\n\65\3\65\6\65\u026f\n\65\r\65\16\65\u0270")
        buf.write("\3\65\2\2\66\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh\2\n\4\2\f")
        buf.write("\1788\4\3\66\66??\3\2\37$\3\2\32\33\3\2\34\36\4\2\33\33")
        buf.write("\'\'\4\2\31\31(,\4\2..88\2\u0299\2m\3\2\2\2\4{\3\2\2\2")
        buf.write("\6\u0082\3\2\2\2\b\u0084\3\2\2\2\n\u0097\3\2\2\2\f\u0099")
        buf.write("\3\2\2\2\16\u00ad\3\2\2\2\20\u00bc\3\2\2\2\22\u00c2\3")
        buf.write("\2\2\2\24\u00c7\3\2\2\2\26\u00d7\3\2\2\2\30\u00e1\3\2")
        buf.write("\2\2\32\u00eb\3\2\2\2\34\u00f5\3\2\2\2\36\u0100\3\2\2")
        buf.write("\2 \u0108\3\2\2\2\"\u010f\3\2\2\2$\u0117\3\2\2\2&\u011d")
        buf.write("\3\2\2\2(\u011f\3\2\2\2*\u0127\3\2\2\2,\u012f\3\2\2\2")
        buf.write(".\u0137\3\2\2\2\60\u013f\3\2\2\2\62\u014a\3\2\2\2\64\u0151")
        buf.write("\3\2\2\2\66\u0158\3\2\2\28\u0166\3\2\2\2:\u0170\3\2\2")
        buf.write("\2<\u0197\3\2\2\2>\u0199\3\2\2\2@\u01b3\3\2\2\2B\u01b5")
        buf.write("\3\2\2\2D\u01e2\3\2\2\2F\u01e4\3\2\2\2H\u01e8\3\2\2\2")
        buf.write("J\u01f9\3\2\2\2L\u0207\3\2\2\2N\u0209\3\2\2\2P\u020b\3")
        buf.write("\2\2\2R\u0221\3\2\2\2T\u022f\3\2\2\2V\u0231\3\2\2\2X\u0235")
        buf.write("\3\2\2\2Z\u0237\3\2\2\2\\\u023b\3\2\2\2^\u0242\3\2\2\2")
        buf.write("`\u0244\3\2\2\2b\u0246\3\2\2\2d\u0258\3\2\2\2f\u0260\3")
        buf.write("\2\2\2h\u026e\3\2\2\2jl\5\n\6\2kj\3\2\2\2lo\3\2\2\2mk")
        buf.write("\3\2\2\2mn\3\2\2\2nq\3\2\2\2om\3\2\2\2pr\5\4\3\2qp\3\2")
        buf.write("\2\2qr\3\2\2\2rv\3\2\2\2su\5\n\6\2ts\3\2\2\2ux\3\2\2\2")
        buf.write("vt\3\2\2\2vw\3\2\2\2wy\3\2\2\2xv\3\2\2\2yz\7\2\2\3z\3")
        buf.write("\3\2\2\2{|\7\b\2\2|}\7\3\2\2}~\7/\2\2~\177\7\60\2\2\177")
        buf.write("\u0080\5f\64\2\u0080\u0081\5\b\5\2\u0081\5\3\2\2\2\u0082")
        buf.write("\u0083\t\2\2\2\u0083\7\3\2\2\2\u0084\u0085\t\3\2\2\u0085")
        buf.write("\t\3\2\2\2\u0086\u0087\5\f\7\2\u0087\u0088\5\b\5\2\u0088")
        buf.write("\u0098\3\2\2\2\u0089\u008b\5\16\b\2\u008a\u008c\5\b\5")
        buf.write("\2\u008b\u008a\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u0098")
        buf.write("\3\2\2\2\u008d\u008e\5\20\t\2\u008e\u008f\5\b\5\2\u008f")
        buf.write("\u0098\3\2\2\2\u0090\u0091\5\22\n\2\u0091\u0092\5\b\5")
        buf.write("\2\u0092\u0098\3\2\2\2\u0093\u0095\5\24\13\2\u0094\u0096")
        buf.write("\5\b\5\2\u0095\u0094\3\2\2\2\u0095\u0096\3\2\2\2\u0096")
        buf.write("\u0098\3\2\2\2\u0097\u0086\3\2\2\2\u0097\u0089\3\2\2\2")
        buf.write("\u0097\u008d\3\2\2\2\u0097\u0090\3\2\2\2\u0097\u0093\3")
        buf.write("\2\2\2\u0098\13\3\2\2\2\u0099\u009a\7\24\2\2\u009a\u009f")
        buf.write("\78\2\2\u009b\u009c\7\65\2\2\u009c\u009e\78\2\2\u009d")
        buf.write("\u009b\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2\2")
        buf.write("\u009f\u00a0\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f\3")
        buf.write("\2\2\2\u00a2\u00a4\5h\65\2\u00a3\u00a2\3\2\2\2\u00a3\u00a4")
        buf.write("\3\2\2\2\u00a4\u00ab\3\2\2\2\u00a5\u00ac\5\6\4\2\u00a6")
        buf.write("\u00a8\5\6\4\2\u00a7\u00a6\3\2\2\2\u00a7\u00a8\3\2\2\2")
        buf.write("\u00a8\u00a9\3\2\2\2\u00a9\u00aa\7\30\2\2\u00aa\u00ac")
        buf.write("\5&\24\2\u00ab\u00a5\3\2\2\2\u00ab\u00a7\3\2\2\2\u00ac")
        buf.write("\r\3\2\2\2\u00ad\u00ae\7\b\2\2\u00ae\u00af\78\2\2\u00af")
        buf.write("\u00b1\7/\2\2\u00b0\u00b2\5\"\22\2\u00b1\u00b0\3\2\2\2")
        buf.write("\u00b1\u00b2\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b8\7")
        buf.write("\60\2\2\u00b4\u00b6\5h\65\2\u00b5\u00b4\3\2\2\2\u00b5")
        buf.write("\u00b6\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b9\5\6\4\2")
        buf.write("\u00b8\u00b5\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\3")
        buf.write("\2\2\2\u00ba\u00bb\5f\64\2\u00bb\17\3\2\2\2\u00bc\u00bd")
        buf.write("\7\t\2\2\u00bd\u00c0\78\2\2\u00be\u00c1\5\26\f\2\u00bf")
        buf.write("\u00c1\5\32\16\2\u00c0\u00be\3\2\2\2\u00c0\u00bf\3\2\2")
        buf.write("\2\u00c1\21\3\2\2\2\u00c2\u00c3\7\23\2\2\u00c3\u00c4\7")
        buf.write("8\2\2\u00c4\u00c5\7\30\2\2\u00c5\u00c6\5&\24\2\u00c6\23")
        buf.write("\3\2\2\2\u00c7\u00c8\7\b\2\2\u00c8\u00c9\7/\2\2\u00c9")
        buf.write("\u00ca\78\2\2\u00ca\u00cb\78\2\2\u00cb\u00cc\7\60\2\2")
        buf.write("\u00cc\u00cd\78\2\2\u00cd\u00cf\7/\2\2\u00ce\u00d0\5\"")
        buf.write("\22\2\u00cf\u00ce\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1")
        buf.write("\3\2\2\2\u00d1\u00d3\7\60\2\2\u00d2\u00d4\5\6\4\2\u00d3")
        buf.write("\u00d2\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\3\2\2\2")
        buf.write("\u00d5\u00d6\5f\64\2\u00d6\25\3\2\2\2\u00d7\u00d8\7\n")
        buf.write("\2\2\u00d8\u00dc\7\61\2\2\u00d9\u00db\5\30\r\2\u00da\u00d9")
        buf.write("\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc")
        buf.write("\u00dd\3\2\2\2\u00dd\u00df\3\2\2\2\u00de\u00dc\3\2\2\2")
        buf.write("\u00df\u00e0\7\62\2\2\u00e0\27\3\2\2\2\u00e1\u00e7\78")
        buf.write("\2\2\u00e2\u00e4\5h\65\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4")
        buf.write("\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e8\5\6\4\2\u00e6")
        buf.write("\u00e8\5\26\f\2\u00e7\u00e3\3\2\2\2\u00e7\u00e6\3\2\2")
        buf.write("\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\5\b\5\2\u00ea\31\3")
        buf.write("\2\2\2\u00eb\u00ec\7\13\2\2\u00ec\u00f0\7\61\2\2\u00ed")
        buf.write("\u00ef\5 \21\2\u00ee\u00ed\3\2\2\2\u00ef\u00f2\3\2\2\2")
        buf.write("\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f3\3")
        buf.write("\2\2\2\u00f2\u00f0\3\2\2\2\u00f3\u00f4\7\62\2\2\u00f4")
        buf.write("\33\3\2\2\2\u00f5\u00fb\7/\2\2\u00f6\u00f7\5\36\20\2\u00f7")
        buf.write("\u00f8\5\6\4\2\u00f8\u00fa\3\2\2\2\u00f9\u00f6\3\2\2\2")
        buf.write("\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3")
        buf.write("\2\2\2\u00fc\u00fe\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00ff")
        buf.write("\7\60\2\2\u00ff\35\3\2\2\2\u0100\u0105\78\2\2\u0101\u0102")
        buf.write("\7\65\2\2\u0102\u0104\78\2\2\u0103\u0101\3\2\2\2\u0104")
        buf.write("\u0107\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2")
        buf.write("\u0106\37\3\2\2\2\u0107\u0105\3\2\2\2\u0108\u0109\78\2")
        buf.write("\2\u0109\u010b\5\34\17\2\u010a\u010c\5\6\4\2\u010b\u010a")
        buf.write("\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\3\2\2\2\u010d")
        buf.write("\u010e\5\b\5\2\u010e!\3\2\2\2\u010f\u0114\5$\23\2\u0110")
        buf.write("\u0111\7\65\2\2\u0111\u0113\5$\23\2\u0112\u0110\3\2\2")
        buf.write("\2\u0113\u0116\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115")
        buf.write("\3\2\2\2\u0115#\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u0119")
        buf.write("\78\2\2\u0118\u011a\5h\65\2\u0119\u0118\3\2\2\2\u0119")
        buf.write("\u011a\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011c\5\6\4\2")
        buf.write("\u011c%\3\2\2\2\u011d\u011e\5(\25\2\u011e\'\3\2\2\2\u011f")
        buf.write("\u0124\5*\26\2\u0120\u0121\7&\2\2\u0121\u0123\5(\25\2")
        buf.write("\u0122\u0120\3\2\2\2\u0123\u0126\3\2\2\2\u0124\u0122\3")
        buf.write("\2\2\2\u0124\u0125\3\2\2\2\u0125)\3\2\2\2\u0126\u0124")
        buf.write("\3\2\2\2\u0127\u012c\5,\27\2\u0128\u0129\7%\2\2\u0129")
        buf.write("\u012b\5*\26\2\u012a\u0128\3\2\2\2\u012b\u012e\3\2\2\2")
        buf.write("\u012c\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d+\3\2\2")
        buf.write("\2\u012e\u012c\3\2\2\2\u012f\u0134\5.\30\2\u0130\u0131")
        buf.write("\t\4\2\2\u0131\u0133\5.\30\2\u0132\u0130\3\2\2\2\u0133")
        buf.write("\u0136\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2")
        buf.write("\u0135-\3\2\2\2\u0136\u0134\3\2\2\2\u0137\u013c\5\60\31")
        buf.write("\2\u0138\u0139\t\5\2\2\u0139\u013b\5\60\31\2\u013a\u0138")
        buf.write("\3\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a\3\2\2\2\u013c")
        buf.write("\u013d\3\2\2\2\u013d/\3\2\2\2\u013e\u013c\3\2\2\2\u013f")
        buf.write("\u0144\5\62\32\2\u0140\u0141\t\6\2\2\u0141\u0143\5\62")
        buf.write("\32\2\u0142\u0140\3\2\2\2\u0143\u0146\3\2\2\2\u0144\u0142")
        buf.write("\3\2\2\2\u0144\u0145\3\2\2\2\u0145\61\3\2\2\2\u0146\u0144")
        buf.write("\3\2\2\2\u0147\u0148\t\7\2\2\u0148\u014b\5\62\32\2\u0149")
        buf.write("\u014b\5\64\33\2\u014a\u0147\3\2\2\2\u014a\u0149\3\2\2")
        buf.write("\2\u014b\63\3\2\2\2\u014c\u0152\5\66\34\2\u014d\u014e")
        buf.write("\7/\2\2\u014e\u014f\5&\24\2\u014f\u0150\7\60\2\2\u0150")
        buf.write("\u0152\3\2\2\2\u0151\u014c\3\2\2\2\u0151\u014d\3\2\2\2")
        buf.write("\u0152\65\3\2\2\2\u0153\u0159\5:\36\2\u0154\u0155\7/\2")
        buf.write("\2\u0155\u0156\5&\24\2\u0156\u0157\7\60\2\2\u0157\u0159")
        buf.write("\3\2\2\2\u0158\u0153\3\2\2\2\u0158\u0154\3\2\2\2\u0159")
        buf.write("\u015d\3\2\2\2\u015a\u015c\58\35\2\u015b\u015a\3\2\2\2")
        buf.write("\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3")
        buf.write("\2\2\2\u015e\67\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0161")
        buf.write("\7\63\2\2\u0161\u0162\5&\24\2\u0162\u0163\7\64\2\2\u0163")
        buf.write("\u0167\3\2\2\2\u0164\u0165\7-\2\2\u0165\u0167\5:\36\2")
        buf.write("\u0166\u0160\3\2\2\2\u0166\u0164\3\2\2\2\u01679\3\2\2")
        buf.write("\2\u0168\u0171\79\2\2\u0169\u0171\7:\2\2\u016a\u0171\7")
        buf.write(";\2\2\u016b\u0171\7\20\2\2\u016c\u0171\7\21\2\2\u016d")
        buf.write("\u0171\7\22\2\2\u016e\u0171\5b\62\2\u016f\u0171\78\2\2")
        buf.write("\u0170\u0168\3\2\2\2\u0170\u0169\3\2\2\2\u0170\u016a\3")
        buf.write("\2\2\2\u0170\u016b\3\2\2\2\u0170\u016c\3\2\2\2\u0170\u016d")
        buf.write("\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u016f\3\2\2\2\u0171")
        buf.write(";\3\2\2\2\u0172\u0173\5H%\2\u0173\u0174\5\b\5\2\u0174")
        buf.write("\u0198\3\2\2\2\u0175\u0176\5P)\2\u0176\u0177\5\b\5\2\u0177")
        buf.write("\u0198\3\2\2\2\u0178\u0179\5R*\2\u0179\u017a\5\b\5\2\u017a")
        buf.write("\u0198\3\2\2\2\u017b\u017c\5^\60\2\u017c\u017d\5\b\5\2")
        buf.write("\u017d\u0198\3\2\2\2\u017e\u017f\5`\61\2\u017f\u0180\5")
        buf.write("\b\5\2\u0180\u0198\3\2\2\2\u0181\u0182\5b\62\2\u0182\u0183")
        buf.write("\5\b\5\2\u0183\u0198\3\2\2\2\u0184\u0185\5d\63\2\u0185")
        buf.write("\u0186\5\b\5\2\u0186\u0198\3\2\2\2\u0187\u0188\5\f\7\2")
        buf.write("\u0188\u0189\5\b\5\2\u0189\u0198\3\2\2\2\u018a\u018b\5")
        buf.write("\20\t\2\u018b\u018c\5\b\5\2\u018c\u0198\3\2\2\2\u018d")
        buf.write("\u018e\5\24\13\2\u018e\u018f\5\b\5\2\u018f\u0198\3\2\2")
        buf.write("\2\u0190\u0191\5\22\n\2\u0191\u0192\5\b\5\2\u0192\u0198")
        buf.write("\3\2\2\2\u0193\u0195\5f\64\2\u0194\u0196\5\b\5\2\u0195")
        buf.write("\u0194\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0198\3\2\2\2")
        buf.write("\u0197\u0172\3\2\2\2\u0197\u0175\3\2\2\2\u0197\u0178\3")
        buf.write("\2\2\2\u0197\u017b\3\2\2\2\u0197\u017e\3\2\2\2\u0197\u0181")
        buf.write("\3\2\2\2\u0197\u0184\3\2\2\2\u0197\u0187\3\2\2\2\u0197")
        buf.write("\u018a\3\2\2\2\u0197\u018d\3\2\2\2\u0197\u0190\3\2\2\2")
        buf.write("\u0197\u0193\3\2\2\2\u0198=\3\2\2\2\u0199\u019a\5h\65")
        buf.write("\2\u019a\u019b\5\6\4\2\u019b\u019c\5@!\2\u019c?\3\2\2")
        buf.write("\2\u019d\u019e\7\61\2\2\u019e\u01a3\5@!\2\u019f\u01a0")
        buf.write("\7\65\2\2\u01a0\u01a2\5@!\2\u01a1\u019f\3\2\2\2\u01a2")
        buf.write("\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a4\u01a6\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01a7\7")
        buf.write("\62\2\2\u01a7\u01b4\3\2\2\2\u01a8\u01a9\7\61\2\2\u01a9")
        buf.write("\u01ae\5&\24\2\u01aa\u01ab\7\65\2\2\u01ab\u01ad\5&\24")
        buf.write("\2\u01ac\u01aa\3\2\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01ac")
        buf.write("\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b1\3\2\2\2\u01b0")
        buf.write("\u01ae\3\2\2\2\u01b1\u01b2\7\62\2\2\u01b2\u01b4\3\2\2")
        buf.write("\2\u01b3\u019d\3\2\2\2\u01b3\u01a8\3\2\2\2\u01b4A\3\2")
        buf.write("\2\2\u01b5\u01b6\78\2\2\u01b6\u01c2\7\61\2\2\u01b7\u01bc")
        buf.write("\5F$\2\u01b8\u01b9\7\65\2\2\u01b9\u01bb\5F$\2\u01ba\u01b8")
        buf.write("\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2")
        buf.write("\u01bf\u01c1\7\65\2\2\u01c0\u01bf\3\2\2\2\u01c0\u01c1")
        buf.write("\3\2\2\2\u01c1\u01c3\3\2\2\2\u01c2\u01b7\3\2\2\2\u01c2")
        buf.write("\u01c3\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5\7\62\2")
        buf.write("\2\u01c5C\3\2\2\2\u01c6\u01e3\5&\24\2\u01c7\u01e3\5> ")
        buf.write("\2\u01c8\u01e3\5B\"\2\u01c9\u01ca\5\26\f\2\u01ca\u01de")
        buf.write("\7\61\2\2\u01cb\u01cc\78\2\2\u01cc\u01ce\7\67\2\2\u01cd")
        buf.write("\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf\3\2\2\2")
        buf.write("\u01cf\u01d8\5&\24\2\u01d0\u01d3\7\65\2\2\u01d1\u01d2")
        buf.write("\78\2\2\u01d2\u01d4\7\67\2\2\u01d3\u01d1\3\2\2\2\u01d3")
        buf.write("\u01d4\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d7\5&\24\2")
        buf.write("\u01d6\u01d0\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3")
        buf.write("\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01d8")
        buf.write("\3\2\2\2\u01db\u01dd\7\65\2\2\u01dc\u01db\3\2\2\2\u01dc")
        buf.write("\u01dd\3\2\2\2\u01dd\u01df\3\2\2\2\u01de\u01cd\3\2\2\2")
        buf.write("\u01de\u01df\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e1\7")
        buf.write("\62\2\2\u01e1\u01e3\3\2\2\2\u01e2\u01c6\3\2\2\2\u01e2")
        buf.write("\u01c7\3\2\2\2\u01e2\u01c8\3\2\2\2\u01e2\u01c9\3\2\2\2")
        buf.write("\u01e3E\3\2\2\2\u01e4\u01e5\78\2\2\u01e5\u01e6\7\67\2")
        buf.write("\2\u01e6\u01e7\5D#\2\u01e7G\3\2\2\2\u01e8\u01ed\5J&\2")
        buf.write("\u01e9\u01ea\7\65\2\2\u01ea\u01ec\5J&\2\u01eb\u01e9\3")
        buf.write("\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee")
        buf.write("\3\2\2\2\u01ee\u01f0\3\2\2\2\u01ef\u01ed\3\2\2\2\u01f0")
        buf.write("\u01f1\5N(\2\u01f1\u01f6\5L\'\2\u01f2\u01f3\7\65\2\2\u01f3")
        buf.write("\u01f5\5L\'\2\u01f4\u01f2\3\2\2\2\u01f5\u01f8\3\2\2\2")
        buf.write("\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7I\3\2\2")
        buf.write("\2\u01f8\u01f6\3\2\2\2\u01f9\u01fe\78\2\2\u01fa\u01fb")
        buf.write("\7-\2\2\u01fb\u01fd\78\2\2\u01fc\u01fa\3\2\2\2\u01fd\u0200")
        buf.write("\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff")
        buf.write("\u0202\3\2\2\2\u0200\u01fe\3\2\2\2\u0201\u0203\5h\65\2")
        buf.write("\u0202\u0201\3\2\2\2\u0202\u0203\3\2\2\2\u0203K\3\2\2")
        buf.write("\2\u0204\u0208\5&\24\2\u0205\u0208\5> \2\u0206\u0208\5")
        buf.write("B\"\2\u0207\u0204\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0206")
        buf.write("\3\2\2\2\u0208M\3\2\2\2\u0209\u020a\t\b\2\2\u020aO\3\2")
        buf.write("\2\2\u020b\u020c\7\4\2\2\u020c\u020d\5&\24\2\u020d\u020f")
        buf.write("\5f\64\2\u020e\u0210\7?\2\2\u020f\u020e\3\2\2\2\u020f")
        buf.write("\u0210\3\2\2\2\u0210\u021a\3\2\2\2\u0211\u0212\7\5\2\2")
        buf.write("\u0212\u0213\7\4\2\2\u0213\u0214\5&\24\2\u0214\u0216\5")
        buf.write("f\64\2\u0215\u0217\7?\2\2\u0216\u0215\3\2\2\2\u0216\u0217")
        buf.write("\3\2\2\2\u0217\u0219\3\2\2\2\u0218\u0211\3\2\2\2\u0219")
        buf.write("\u021c\3\2\2\2\u021a\u0218\3\2\2\2\u021a\u021b\3\2\2\2")
        buf.write("\u021b\u021f\3\2\2\2\u021c\u021a\3\2\2\2\u021d\u021e\7")
        buf.write("\5\2\2\u021e\u0220\5f\64\2\u021f\u021d\3\2\2\2\u021f\u0220")
        buf.write("\3\2\2\2\u0220Q\3\2\2\2\u0221\u0224\7\6\2\2\u0222\u0225")
        buf.write("\5T+\2\u0223\u0225\5\\/\2\u0224\u0222\3\2\2\2\u0224\u0223")
        buf.write("\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0227\5f\64\2\u0227")
        buf.write("S\3\2\2\2\u0228\u0230\5X-\2\u0229\u022a\5V,\2\u022a\u022b")
        buf.write("\7\66\2\2\u022b\u022c\5X-\2\u022c\u022d\7\66\2\2\u022d")
        buf.write("\u022e\5Z.\2\u022e\u0230\3\2\2\2\u022f\u0228\3\2\2\2\u022f")
        buf.write("\u0229\3\2\2\2\u0230U\3\2\2\2\u0231\u0232\78\2\2\u0232")
        buf.write("\u0233\7\31\2\2\u0233\u0234\5&\24\2\u0234W\3\2\2\2\u0235")
        buf.write("\u0236\5&\24\2\u0236Y\3\2\2\2\u0237\u0238\78\2\2\u0238")
        buf.write("\u0239\5N(\2\u0239\u023a\5&\24\2\u023a[\3\2\2\2\u023b")
        buf.write("\u023c\t\t\2\2\u023c\u023d\7\65\2\2\u023d\u023e\78\2\2")
        buf.write("\u023e\u023f\7\31\2\2\u023f\u0240\7\27\2\2\u0240\u0241")
        buf.write("\78\2\2\u0241]\3\2\2\2\u0242\u0243\7\26\2\2\u0243_\3\2")
        buf.write("\2\2\u0244\u0245\7\25\2\2\u0245a\3\2\2\2\u0246\u0249\7")
        buf.write("8\2\2\u0247\u0248\7-\2\2\u0248\u024a\78\2\2\u0249\u0247")
        buf.write("\3\2\2\2\u0249\u024a\3\2\2\2\u024a\u024b\3\2\2\2\u024b")
        buf.write("\u0254\7/\2\2\u024c\u0251\5&\24\2\u024d\u024e\7\65\2\2")
        buf.write("\u024e\u0250\5&\24\2\u024f\u024d\3\2\2\2\u0250\u0253\3")
        buf.write("\2\2\2\u0251\u024f\3\2\2\2\u0251\u0252\3\2\2\2\u0252\u0255")
        buf.write("\3\2\2\2\u0253\u0251\3\2\2\2\u0254\u024c\3\2\2\2\u0254")
        buf.write("\u0255\3\2\2\2\u0255\u0256\3\2\2\2\u0256\u0257\7\60\2")
        buf.write("\2\u0257c\3\2\2\2\u0258\u025e\7\7\2\2\u0259\u025f\5&\24")
        buf.write("\2\u025a\u025b\5h\65\2\u025b\u025c\5\6\4\2\u025c\u025d")
        buf.write("\5@!\2\u025d\u025f\3\2\2\2\u025e\u0259\3\2\2\2\u025e\u025a")
        buf.write("\3\2\2\2\u025e\u025f\3\2\2\2\u025fe\3\2\2\2\u0260\u0264")
        buf.write("\7\61\2\2\u0261\u0263\5<\37\2\u0262\u0261\3\2\2\2\u0263")
        buf.write("\u0266\3\2\2\2\u0264\u0262\3\2\2\2\u0264\u0265\3\2\2\2")
        buf.write("\u0265\u0267\3\2\2\2\u0266\u0264\3\2\2\2\u0267\u0268\7")
        buf.write("\62\2\2\u0268g\3\2\2\2\u0269\u026b\7\63\2\2\u026a\u026c")
        buf.write("\5&\24\2\u026b\u026a\3\2\2\2\u026b\u026c\3\2\2\2\u026c")
        buf.write("\u026d\3\2\2\2\u026d\u026f\7\64\2\2\u026e\u0269\3\2\2")
        buf.write("\2\u026f\u0270\3\2\2\2\u0270\u026e\3\2\2\2\u0270\u0271")
        buf.write("\3\2\2\2\u0271i\3\2\2\2Fmqv\u008b\u0095\u0097\u009f\u00a3")
        buf.write("\u00a7\u00ab\u00b1\u00b5\u00b8\u00c0\u00cf\u00d3\u00dc")
        buf.write("\u00e3\u00e7\u00f0\u00fb\u0105\u010b\u0114\u0119\u0124")
        buf.write("\u012c\u0134\u013c\u0144\u014a\u0151\u0158\u015d\u0166")
        buf.write("\u0170\u0195\u0197\u01a3\u01ae\u01b3\u01bc\u01c0\u01c2")
        buf.write("\u01cd\u01d3\u01d8\u01dc\u01de\u01e2\u01ed\u01f6\u01fe")
        buf.write("\u0202\u0207\u020f\u0216\u021a\u021f\u0224\u022f\u0249")
        buf.write("\u0251\u0254\u025e\u0264\u026b\u0270")
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
    RULE_postfixExp = 26
    RULE_postfixOp = 27
    RULE_term = 28
    RULE_statement = 29
    RULE_arrayLit = 30
    RULE_arraysBlock = 31
    RULE_structExpression = 32
    RULE_structBlock = 33
    RULE_structFieldsAssign = 34
    RULE_assignStatement = 35
    RULE_a1 = 36
    RULE_a2 = 37
    RULE_assignmentOperator = 38
    RULE_ifStatement = 39
    RULE_forStatement = 40
    RULE_forLoop = 41
    RULE_initilization = 42
    RULE_forCondition = 43
    RULE_forUpdate = 44
    RULE_forIteration = 45
    RULE_breakStatement = 46
    RULE_continueStatement = 47
    RULE_callStatement = 48
    RULE_returnStatement = 49
    RULE_block = 50
    RULE_arrayDims = 51

    ruleNames =  [ "program", "mainFunction", "baseType", "endOfStatement", 
                   "declaration", "varDecl", "funcDecl", "typeDecl", "constDecl", 
                   "methodDecl", "structDefinition", "structFields", "interfaceDefinition", 
                   "listParams", "listIdentifier", "interfaceFields", "funcParams", 
                   "funcParam", "expression", "logicOrExp", "logicAndExp", 
                   "equalityExp", "additiveExp", "multiplicativeExp", "unaryExp", 
                   "primaryExp", "postfixExp", "postfixOp", "term", "statement", 
                   "arrayLit", "arraysBlock", "structExpression", "structBlock", 
                   "structFieldsAssign", "assignStatement", "a1", "a2", 
                   "assignmentOperator", "ifStatement", "forStatement", 
                   "forLoop", "initilization", "forCondition", "forUpdate", 
                   "forIteration", "breakStatement", "continueStatement", 
                   "callStatement", "returnStatement", "block", "arrayDims" ]

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
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 104
                    self.declaration() 
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 110
                self.mainFunction()


            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0):
                self.state = 113
                self.declaration()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
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
            self.state = 121
            self.match(MiniGoParser.FUNC)
            self.state = 122
            self.match(MiniGoParser.T__0)
            self.state = 123
            self.match(MiniGoParser.LPAREN)
            self.state = 124
            self.match(MiniGoParser.RPAREN)
            self.state = 125
            self.block()
            self.state = 126
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
            self.state = 128
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
            self.state = 130
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

        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


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
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.varDecl()
                self.state = 133
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.funcDecl()
                self.state = 137
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 136
                    self.endOfStatement()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.typeDecl()
                self.state = 140
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.constDecl()
                self.state = 143
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 145
                self.methodDecl()
                self.state = 147
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 146
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
            self.state = 151
            self.match(MiniGoParser.VAR)
            self.state = 152
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 153
                self.match(MiniGoParser.COMMA)
                self.state = 154
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 160
                self.arrayDims()


            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 163
                self.baseType()
                pass

            elif la_ == 2:
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                    self.state = 164
                    self.baseType()


                self.state = 167
                self.match(MiniGoParser.ASSIGN)
                self.state = 168
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
            self.state = 171
            self.match(MiniGoParser.FUNC)
            self.state = 172
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 173
            self.match(MiniGoParser.LPAREN)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 174
                self.funcParams()


            self.state = 177
            self.match(MiniGoParser.RPAREN)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LBRACKET) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACKET:
                    self.state = 178
                    self.arrayDims()


                self.state = 181
                self.baseType()


            self.state = 184
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
            self.state = 186
            self.match(MiniGoParser.TYPE)
            self.state = 187
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.state = 188
                self.structDefinition()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.state = 189
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
            self.state = 192
            self.match(MiniGoParser.CONST)
            self.state = 193
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 194
            self.match(MiniGoParser.ASSIGN)
            self.state = 195
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
            self.state = 197
            self.match(MiniGoParser.FUNC)
            self.state = 198
            self.match(MiniGoParser.LPAREN)
            self.state = 199
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 200
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 201
            self.match(MiniGoParser.RPAREN)
            self.state = 202
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 203
            self.match(MiniGoParser.LPAREN)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 204
                self.funcParams()


            self.state = 207
            self.match(MiniGoParser.RPAREN)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 208
                self.baseType()


            self.state = 211
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
            self.state = 213
            self.match(MiniGoParser.STRUCT)
            self.state = 214
            self.match(MiniGoParser.LBRACE)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 215
                self.structFields()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 221
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

        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def structDefinition(self):
            return self.getTypedRuleContext(MiniGoParser.StructDefinitionContext,0)


        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


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
            self.state = 223
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOLEAN, MiniGoParser.LBRACKET, MiniGoParser.IDENTIFIER]:
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LBRACKET:
                    self.state = 224
                    self.arrayDims()


                self.state = 227
                self.baseType()
                pass
            elif token in [MiniGoParser.STRUCT]:
                self.state = 228
                self.structDefinition()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 231
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
            self.state = 233
            self.match(MiniGoParser.INTERFACE)
            self.state = 234
            self.match(MiniGoParser.LBRACE)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 235
                self.interfaceFields()
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 241
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
            self.state = 243
            self.match(MiniGoParser.LPAREN)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 244
                self.listIdentifier()
                self.state = 245
                self.baseType()
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 252
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
            self.state = 254
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 255
                self.match(MiniGoParser.COMMA)
                self.state = 256
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 261
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
            self.state = 262
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 263
            self.listParams()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 264
                self.baseType()


            self.state = 267
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
            self.state = 269
            self.funcParam()
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 270
                self.match(MiniGoParser.COMMA)
                self.state = 271
                self.funcParam()
                self.state = 276
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
            self.state = 277
            self.match(MiniGoParser.IDENTIFIER)

            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 278
                self.arrayDims()


            self.state = 281
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
            self.state = 283
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
            self.state = 285
            self.logicAndExp()
            self.state = 290
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 286
                    self.match(MiniGoParser.OR)
                    self.state = 287
                    self.logicOrExp() 
                self.state = 292
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
            self.state = 293
            self.equalityExp()
            self.state = 298
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 294
                    self.match(MiniGoParser.AND)
                    self.state = 295
                    self.logicAndExp() 
                self.state = 300
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
            self.state = 301
            self.additiveExp()
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LEQ) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GEQ))) != 0):
                self.state = 302
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LEQ) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 303
                self.additiveExp()
                self.state = 308
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
            self.state = 309
            self.multiplicativeExp()
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS:
                self.state = 310
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 311
                self.multiplicativeExp()
                self.state = 316
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
            self.state = 317
            self.unaryExp()
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0):
                self.state = 318
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 319
                self.unaryExp()
                self.state = 324
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
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 326
                self.unaryExp()
                pass
            elif token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.LPAREN, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
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

        def postfixExp(self):
            return self.getTypedRuleContext(MiniGoParser.PostfixExpContext,0)


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
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.postfixExp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.match(MiniGoParser.LPAREN)
                self.state = 332
                self.expression()
                self.state = 333
                self.match(MiniGoParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixExpContext(ParserRuleContext):
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

        def postfixOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.PostfixOpContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.PostfixOpContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_postfixExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixExp" ):
                return visitor.visitPostfixExp(self)
            else:
                return visitor.visitChildren(self)




    def postfixExp(self):

        localctx = MiniGoParser.PostfixExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_postfixExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 337
                self.term()
                pass
            elif token in [MiniGoParser.LPAREN]:
                self.state = 338
                self.match(MiniGoParser.LPAREN)
                self.state = 339
                self.expression()
                self.state = 340
                self.match(MiniGoParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.DOT or _la==MiniGoParser.LBRACKET:
                self.state = 344
                self.postfixOp()
                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def term(self):
            return self.getTypedRuleContext(MiniGoParser.TermContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_postfixOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixOp" ):
                return visitor.visitPostfixOp(self)
            else:
                return visitor.visitChildren(self)




    def postfixOp(self):

        localctx = MiniGoParser.PostfixOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_postfixOp)
        try:
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.match(MiniGoParser.LBRACKET)
                self.state = 351
                self.expression()
                self.state = 352
                self.match(MiniGoParser.RBRACKET)
                pass
            elif token in [MiniGoParser.DOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.match(MiniGoParser.DOT)
                self.state = 355
                self.term()
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

        def callStatement(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementContext,0)


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
        self.enterRule(localctx, 56, self.RULE_term)
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 360
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 361
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 362
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 363
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 364
                self.callStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 365
                self.match(MiniGoParser.IDENTIFIER)
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

        def assignStatement(self):
            return self.getTypedRuleContext(MiniGoParser.AssignStatementContext,0)


        def endOfStatement(self):
            return self.getTypedRuleContext(MiniGoParser.EndOfStatementContext,0)


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


        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def typeDecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypeDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(MiniGoParser.MethodDeclContext,0)


        def constDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.assignStatement()
                self.state = 369
                self.endOfStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.ifStatement()
                self.state = 372
                self.endOfStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 374
                self.forStatement()
                self.state = 375
                self.endOfStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 377
                self.breakStatement()
                self.state = 378
                self.endOfStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 380
                self.continueStatement()
                self.state = 381
                self.endOfStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 383
                self.callStatement()
                self.state = 384
                self.endOfStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 386
                self.returnStatement()
                self.state = 387
                self.endOfStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 389
                self.varDecl()
                self.state = 390
                self.endOfStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 392
                self.typeDecl()
                self.state = 393
                self.endOfStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 395
                self.methodDecl()
                self.state = 396
                self.endOfStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 398
                self.constDecl()
                self.state = 399
                self.endOfStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 401
                self.block()
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.SEMI - -1)) | (1 << (MiniGoParser.NEWLINE - -1)))) != 0):
                    self.state = 402
                    self.endOfStatement()


                pass


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

        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def arraysBlock(self):
            return self.getTypedRuleContext(MiniGoParser.ArraysBlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLit" ):
                return visitor.visitArrayLit(self)
            else:
                return visitor.visitChildren(self)




    def arrayLit(self):

        localctx = MiniGoParser.ArrayLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_arrayLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.arrayDims()
            self.state = 408
            self.baseType()
            self.state = 409
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
        self.enterRule(localctx, 62, self.RULE_arraysBlock)
        self._la = 0 # Token type
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.match(MiniGoParser.LBRACE)
                self.state = 412
                self.arraysBlock()
                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 413
                    self.match(MiniGoParser.COMMA)
                    self.state = 414
                    self.arraysBlock()
                    self.state = 419
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 420
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.match(MiniGoParser.LBRACE)
                self.state = 423
                self.expression()
                self.state = 428
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 424
                    self.match(MiniGoParser.COMMA)
                    self.state = 425
                    self.expression()
                    self.state = 430
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 431
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

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def structFieldsAssign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StructFieldsAssignContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StructFieldsAssignContext,i)


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
        self.enterRule(localctx, 64, self.RULE_structExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 436
            self.match(MiniGoParser.LBRACE)
            self.state = 448
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 437
                self.structFieldsAssign()
                self.state = 442
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 438
                        self.match(MiniGoParser.COMMA)
                        self.state = 439
                        self.structFieldsAssign() 
                    self.state = 444
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

                self.state = 446
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.COMMA:
                    self.state = 445
                    self.match(MiniGoParser.COMMA)




            self.state = 450
            self.match(MiniGoParser.RBRACE)
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def structExpression(self):
            return self.getTypedRuleContext(MiniGoParser.StructExpressionContext,0)


        def structDefinition(self):
            return self.getTypedRuleContext(MiniGoParser.StructDefinitionContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COLON)
            else:
                return self.getToken(MiniGoParser.COLON, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructBlock" ):
                return visitor.visitStructBlock(self)
            else:
                return visitor.visitChildren(self)




    def structBlock(self):

        localctx = MiniGoParser.StructBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_structBlock)
        self._la = 0 # Token type
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 454
                self.structExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 455
                self.structDefinition()
                self.state = 456
                self.match(MiniGoParser.LBRACE)
                self.state = 476
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 459
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        self.state = 457
                        self.match(MiniGoParser.IDENTIFIER)
                        self.state = 458
                        self.match(MiniGoParser.COLON)


                    self.state = 461
                    self.expression()
                    self.state = 470
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 462
                            self.match(MiniGoParser.COMMA)
                            self.state = 465
                            self._errHandler.sync(self)
                            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                            if la_ == 1:
                                self.state = 463
                                self.match(MiniGoParser.IDENTIFIER)
                                self.state = 464
                                self.match(MiniGoParser.COLON)


                            self.state = 467
                            self.expression() 
                        self.state = 472
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

                    self.state = 474
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MiniGoParser.COMMA:
                        self.state = 473
                        self.match(MiniGoParser.COMMA)




                self.state = 478
                self.match(MiniGoParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructFieldsAssignContext(ParserRuleContext):
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
            return MiniGoParser.RULE_structFieldsAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructFieldsAssign" ):
                return visitor.visitStructFieldsAssign(self)
            else:
                return visitor.visitChildren(self)




    def structFieldsAssign(self):

        localctx = MiniGoParser.StructFieldsAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_structFieldsAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 483
            self.match(MiniGoParser.COLON)
            self.state = 484
            self.structBlock()
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

        def assignmentOperator(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentOperatorContext,0)


        def a2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.A2Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.A2Context,i)


        def a1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.A1Context)
            else:
                return self.getTypedRuleContext(MiniGoParser.A1Context,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.COMMA)
            else:
                return self.getToken(MiniGoParser.COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignStatement(self):

        localctx = MiniGoParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_assignStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.a1()
            self.state = 491
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 487
                self.match(MiniGoParser.COMMA)
                self.state = 488
                self.a1()
                self.state = 493
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 494
            self.assignmentOperator()
            self.state = 495
            self.a2()
            self.state = 500
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 496
                self.match(MiniGoParser.COMMA)
                self.state = 497
                self.a2()
                self.state = 502
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class A1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.DOT)
            else:
                return self.getToken(MiniGoParser.DOT, i)

        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_a1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA1" ):
                return visitor.visitA1(self)
            else:
                return visitor.visitChildren(self)




    def a1(self):

        localctx = MiniGoParser.A1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_a1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 508
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.DOT:
                self.state = 504
                self.match(MiniGoParser.DOT)
                self.state = 505
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 510
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 512
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LBRACKET:
                self.state = 511
                self.arrayDims()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class A2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def arrayLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayLitContext,0)


        def structExpression(self):
            return self.getTypedRuleContext(MiniGoParser.StructExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_a2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA2" ):
                return visitor.visitA2(self)
            else:
                return visitor.visitChildren(self)




    def a2(self):

        localctx = MiniGoParser.A2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_a2)
        try:
            self.state = 517
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 514
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.arrayLit()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 516
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
        self.enterRule(localctx, 76, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
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


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

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
        self.enterRule(localctx, 78, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(MiniGoParser.IF)
            self.state = 522
            self.expression()
            self.state = 523
            self.block()
            self.state = 525
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.state = 524
                self.match(MiniGoParser.NEWLINE)


            self.state = 536
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 527
                    self.match(MiniGoParser.ELSE)
                    self.state = 528
                    self.match(MiniGoParser.IF)
                    self.state = 529
                    self.expression()
                    self.state = 530
                    self.block()
                    self.state = 532
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                    if la_ == 1:
                        self.state = 531
                        self.match(MiniGoParser.NEWLINE)

             
                self.state = 538
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

            self.state = 541
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 539
                self.match(MiniGoParser.ELSE)
                self.state = 540
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
        self.enterRule(localctx, 80, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
            self.match(MiniGoParser.FOR)
            self.state = 546
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.state = 544
                self.forLoop()
                pass

            elif la_ == 2:
                self.state = 545
                self.forIteration()
                pass


            self.state = 548
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
        self.enterRule(localctx, 82, self.RULE_forLoop)
        try:
            self.state = 557
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 550
                self.forCondition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 551
                self.initilization()
                self.state = 552
                self.match(MiniGoParser.SEMI)
                self.state = 553
                self.forCondition()
                self.state = 554
                self.match(MiniGoParser.SEMI)
                self.state = 555
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
        self.enterRule(localctx, 84, self.RULE_initilization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 560
            self.match(MiniGoParser.DECLARE)
            self.state = 561
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
        self.enterRule(localctx, 86, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
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
        self.enterRule(localctx, 88, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 566
            self.assignmentOperator()
            self.state = 567
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
        self.enterRule(localctx, 90, self.RULE_forIteration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.BLANK or _la==MiniGoParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 570
            self.match(MiniGoParser.COMMA)
            self.state = 571
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 572
            self.match(MiniGoParser.DECLARE)
            self.state = 573
            self.match(MiniGoParser.RANGE)
            self.state = 574
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
        self.enterRule(localctx, 92, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
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
        self.enterRule(localctx, 94, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
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
        self.enterRule(localctx, 96, self.RULE_callStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 583
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.DOT:
                self.state = 581
                self.match(MiniGoParser.DOT)
                self.state = 582
                self.match(MiniGoParser.IDENTIFIER)


            self.state = 585
            self.match(MiniGoParser.LPAREN)
            self.state = 594
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 586
                self.expression()
                self.state = 591
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 587
                    self.match(MiniGoParser.COMMA)
                    self.state = 588
                    self.expression()
                    self.state = 593
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 596
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


        def arrayDims(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayDimsContext,0)


        def baseType(self):
            return self.getTypedRuleContext(MiniGoParser.BaseTypeContext,0)


        def arraysBlock(self):
            return self.getTypedRuleContext(MiniGoParser.ArraysBlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MiniGoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 598
            self.match(MiniGoParser.RETURN)
            self.state = 604
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.NIL, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.IDENTIFIER, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.state = 599
                self.expression()
                pass
            elif token in [MiniGoParser.LBRACKET]:
                self.state = 600
                self.arrayDims()
                self.state = 601
                self.baseType()
                self.state = 602
                self.arraysBlock()
                pass
            elif token in [MiniGoParser.EOF, MiniGoParser.SEMI, MiniGoParser.NEWLINE]:
                pass
            else:
                pass
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
        self.enterRule(localctx, 100, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self.match(MiniGoParser.LBRACE)
            self.state = 610
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.LBRACE) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 607
                self.statement()
                self.state = 612
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 613
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
        self.enterRule(localctx, 102, self.RULE_arrayDims)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 620 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 615
                self.match(MiniGoParser.LBRACKET)
                self.state = 617
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.NIL) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                    self.state = 616
                    self.expression()


                self.state = 619
                self.match(MiniGoParser.RBRACKET)
                self.state = 622 
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





