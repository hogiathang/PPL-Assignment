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
        buf.write("\u017d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\3\2\6")
        buf.write("\2L\n\2\r\2\16\2M\3\2\3\2\3\3\3\3\3\4\3\4\5\4V\n\4\3\5")
        buf.write("\3\5\3\5\3\5\5\5\\\n\5\3\6\3\6\3\6\5\6a\n\6\3\6\3\6\5")
        buf.write("\6e\n\6\3\6\3\6\5\6i\n\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7q")
        buf.write("\n\7\3\7\3\7\5\7u\n\7\3\7\3\7\5\7y\n\7\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\5\n\u0087\n\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\6\f\u0092\n\f\r\f\16")
        buf.write("\f\u0093\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\7\17\u00a4\n\17\f\17\16\17\u00a7")
        buf.write("\13\17\3\17\3\17\3\20\3\20\3\20\7\20\u00ae\n\20\f\20\16")
        buf.write("\20\u00b1\13\20\3\21\3\21\3\21\7\21\u00b6\n\21\f\21\16")
        buf.write("\21\u00b9\13\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u00c2\n\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00d3\n\23\f\23")
        buf.write("\16\23\u00d6\13\23\3\24\3\24\3\24\3\24\5\24\u00dc\n\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00e5\n\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00f0")
        buf.write("\n\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\7\27\u00fe\n\27\f\27\16\27\u0101\13\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\7\27\u0109\n\27\f\27\16\27\u010c")
        buf.write("\13\27\3\27\3\27\5\27\u0110\n\27\3\30\3\30\3\30\3\30\5")
        buf.write("\30\u0116\n\30\3\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\7\32")
        buf.write("\u012a\n\32\f\32\16\32\u012d\13\32\3\32\3\32\5\32\u0131")
        buf.write("\n\32\3\33\3\33\3\33\5\33\u0136\n\33\3\33\3\33\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\5\34\u0141\n\34\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\5#\u015d\n#\3#\3")
        buf.write("#\3#\3#\7#\u0163\n#\f#\16#\u0166\13#\5#\u0168\n#\3#\3")
        buf.write("#\3#\3$\3$\7$\u016f\n$\f$\16$\u0172\13$\3$\3$\3%\3%\3")
        buf.write("%\6%\u0179\n%\r%\16%\u017a\3%\2\3$&\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFH\2")
        buf.write("\n\4\2\13\13\16\20\4\2\30\30$$\3\2\34!\3\2\27\30\3\2\31")
        buf.write("\33\4\2\n\13\17\20\3\2&+\4\2\26\26..\2\u018a\2K\3\2\2")
        buf.write("\2\4Q\3\2\2\2\6U\3\2\2\2\b[\3\2\2\2\n]\3\2\2\2\fl\3\2")
        buf.write("\2\2\16z\3\2\2\2\20~\3\2\2\2\22\u0086\3\2\2\2\24\u0088")
        buf.write("\3\2\2\2\26\u0091\3\2\2\2\30\u0095\3\2\2\2\32\u009a\3")
        buf.write("\2\2\2\34\u009f\3\2\2\2\36\u00aa\3\2\2\2 \u00b2\3\2\2")
        buf.write("\2\"\u00ba\3\2\2\2$\u00c1\3\2\2\2&\u00e4\3\2\2\2(\u00ef")
        buf.write("\3\2\2\2*\u00f3\3\2\2\2,\u010f\3\2\2\2.\u0111\3\2\2\2")
        buf.write("\60\u011b\3\2\2\2\62\u011d\3\2\2\2\64\u0132\3\2\2\2\66")
        buf.write("\u0140\3\2\2\28\u0142\3\2\2\2:\u0146\3\2\2\2<\u0148\3")
        buf.write("\2\2\2>\u014c\3\2\2\2@\u0153\3\2\2\2B\u0156\3\2\2\2D\u0159")
        buf.write("\3\2\2\2F\u016c\3\2\2\2H\u0178\3\2\2\2JL\5\6\4\2KJ\3\2")
        buf.write("\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\7\2\2\3")
        buf.write("P\3\3\2\2\2QR\t\2\2\2R\5\3\2\2\2SV\5\b\5\2TV\5(\25\2U")
        buf.write("S\3\2\2\2UT\3\2\2\2V\7\3\2\2\2W\\\5\n\6\2X\\\5\f\7\2Y")
        buf.write("\\\5\16\b\2Z\\\5\20\t\2[W\3\2\2\2[X\3\2\2\2[Y\3\2\2\2")
        buf.write("[Z\3\2\2\2\\\t\3\2\2\2]^\7\r\2\2^`\7\26\2\2_a\5H%\2`_")
        buf.write("\3\2\2\2`a\3\2\2\2ah\3\2\2\2bi\5\4\3\2ce\5\4\3\2dc\3\2")
        buf.write("\2\2de\3\2\2\2ef\3\2\2\2fg\7%\2\2gi\5$\23\2hb\3\2\2\2")
        buf.write("hd\3\2\2\2ij\3\2\2\2jk\7\66\2\2k\13\3\2\2\2lm\7\7\2\2")
        buf.write("mn\7\26\2\2np\7/\2\2oq\5 \21\2po\3\2\2\2pq\3\2\2\2qr\3")
        buf.write("\2\2\2rt\7\60\2\2su\5\4\3\2ts\3\2\2\2tu\3\2\2\2uv\3\2")
        buf.write("\2\2vx\5F$\2wy\7\66\2\2xw\3\2\2\2xy\3\2\2\2y\r\3\2\2\2")
        buf.write("z{\7\b\2\2{|\7\26\2\2|}\5\22\n\2}\17\3\2\2\2~\177\7\f")
        buf.write("\2\2\177\u0080\7\26\2\2\u0080\u0081\7%\2\2\u0081\u0082")
        buf.write("\5$\23\2\u0082\u0083\7\66\2\2\u0083\21\3\2\2\2\u0084\u0087")
        buf.write("\5\24\13\2\u0085\u0087\5\30\r\2\u0086\u0084\3\2\2\2\u0086")
        buf.write("\u0085\3\2\2\2\u0087\23\3\2\2\2\u0088\u0089\7\t\2\2\u0089")
        buf.write("\u008a\7\61\2\2\u008a\u008b\5\26\f\2\u008b\u008c\7\62")
        buf.write("\2\2\u008c\25\3\2\2\2\u008d\u008e\7\26\2\2\u008e\u008f")
        buf.write("\5\4\3\2\u008f\u0090\7\66\2\2\u0090\u0092\3\2\2\2\u0091")
        buf.write("\u008d\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0091\3\2\2\2")
        buf.write("\u0093\u0094\3\2\2\2\u0094\27\3\2\2\2\u0095\u0096\7\n")
        buf.write("\2\2\u0096\u0097\7\61\2\2\u0097\u0098\5\32\16\2\u0098")
        buf.write("\u0099\7\62\2\2\u0099\31\3\2\2\2\u009a\u009b\7\26\2\2")
        buf.write("\u009b\u009c\5\34\17\2\u009c\u009d\5\4\3\2\u009d\u009e")
        buf.write("\7\66\2\2\u009e\33\3\2\2\2\u009f\u00a5\7/\2\2\u00a0\u00a1")
        buf.write("\5\36\20\2\u00a1\u00a2\5\4\3\2\u00a2\u00a4\3\2\2\2\u00a3")
        buf.write("\u00a0\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2")
        buf.write("\u00a5\u00a6\3\2\2\2\u00a6\u00a8\3\2\2\2\u00a7\u00a5\3")
        buf.write("\2\2\2\u00a8\u00a9\7\60\2\2\u00a9\35\3\2\2\2\u00aa\u00af")
        buf.write("\7\26\2\2\u00ab\u00ac\7\65\2\2\u00ac\u00ae\7\26\2\2\u00ad")
        buf.write("\u00ab\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2")
        buf.write("\u00af\u00b0\3\2\2\2\u00b0\37\3\2\2\2\u00b1\u00af\3\2")
        buf.write("\2\2\u00b2\u00b7\5\"\22\2\u00b3\u00b4\7\65\2\2\u00b4\u00b6")
        buf.write("\5\"\22\2\u00b5\u00b3\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7")
        buf.write("\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8!\3\2\2\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00ba\u00bb\7\26\2\2\u00bb\u00bc\5\4\3")
        buf.write("\2\u00bc#\3\2\2\2\u00bd\u00be\b\23\1\2\u00be\u00bf\t\3")
        buf.write("\2\2\u00bf\u00c2\5&\24\2\u00c0\u00c2\5&\24\2\u00c1\u00bd")
        buf.write("\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\u00d4\3\2\2\2\u00c3")
        buf.write("\u00c4\f\t\2\2\u00c4\u00c5\7#\2\2\u00c5\u00d3\5&\24\2")
        buf.write("\u00c6\u00c7\f\b\2\2\u00c7\u00c8\7\"\2\2\u00c8\u00d3\5")
        buf.write("&\24\2\u00c9\u00ca\f\7\2\2\u00ca\u00cb\t\4\2\2\u00cb\u00d3")
        buf.write("\5&\24\2\u00cc\u00cd\f\6\2\2\u00cd\u00ce\t\5\2\2\u00ce")
        buf.write("\u00d3\5&\24\2\u00cf\u00d0\f\5\2\2\u00d0\u00d1\t\6\2\2")
        buf.write("\u00d1\u00d3\5&\24\2\u00d2\u00c3\3\2\2\2\u00d2\u00c6\3")
        buf.write("\2\2\2\u00d2\u00c9\3\2\2\2\u00d2\u00cc\3\2\2\2\u00d2\u00cf")
        buf.write("\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4")
        buf.write("\u00d5\3\2\2\2\u00d5%\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7")
        buf.write("\u00db\7\26\2\2\u00d8\u00dc\5H%\2\u00d9\u00da\7,\2\2\u00da")
        buf.write("\u00dc\7\26\2\2\u00db\u00d8\3\2\2\2\u00db\u00d9\3\2\2")
        buf.write("\2\u00db\u00dc\3\2\2\2\u00dc\u00e5\3\2\2\2\u00dd\u00e5")
        buf.write("\7\67\2\2\u00de\u00e5\78\2\2\u00df\u00e5\79\2\2\u00e0")
        buf.write("\u00e1\7/\2\2\u00e1\u00e2\5$\23\2\u00e2\u00e3\7\60\2\2")
        buf.write("\u00e3\u00e5\3\2\2\2\u00e4\u00d7\3\2\2\2\u00e4\u00dd\3")
        buf.write("\2\2\2\u00e4\u00de\3\2\2\2\u00e4\u00df\3\2\2\2\u00e4\u00e0")
        buf.write("\3\2\2\2\u00e5\'\3\2\2\2\u00e6\u00f0\5.\30\2\u00e7\u00f0")
        buf.write("\5\62\32\2\u00e8\u00f0\5\64\33\2\u00e9\u00f0\5@!\2\u00ea")
        buf.write("\u00f0\5B\"\2\u00eb\u00f0\5D#\2\u00ec\u00f0\5*\26\2\u00ed")
        buf.write("\u00f0\5\n\6\2\u00ee\u00f0\5\20\t\2\u00ef\u00e6\3\2\2")
        buf.write("\2\u00ef\u00e7\3\2\2\2\u00ef\u00e8\3\2\2\2\u00ef\u00e9")
        buf.write("\3\2\2\2\u00ef\u00ea\3\2\2\2\u00ef\u00eb\3\2\2\2\u00ef")
        buf.write("\u00ec\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3\2\2\2")
        buf.write("\u00f0\u00f1\3\2\2\2\u00f1\u00f2\b\25\1\2\u00f2)\3\2\2")
        buf.write("\2\u00f3\u00f4\7\26\2\2\u00f4\u00f5\7&\2\2\u00f5\u00f6")
        buf.write("\5H%\2\u00f6\u00f7\t\7\2\2\u00f7\u00f8\5,\27\2\u00f8+")
        buf.write("\3\2\2\2\u00f9\u00fa\7\61\2\2\u00fa\u00ff\5,\27\2\u00fb")
        buf.write("\u00fc\7\65\2\2\u00fc\u00fe\5,\27\2\u00fd\u00fb\3\2\2")
        buf.write("\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100")
        buf.write("\3\2\2\2\u0100\u0102\3\2\2\2\u0101\u00ff\3\2\2\2\u0102")
        buf.write("\u0103\7\62\2\2\u0103\u0110\3\2\2\2\u0104\u0105\7\61\2")
        buf.write("\2\u0105\u010a\5$\23\2\u0106\u0107\7\65\2\2\u0107\u0109")
        buf.write("\5$\23\2\u0108\u0106\3\2\2\2\u0109\u010c\3\2\2\2\u010a")
        buf.write("\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010d\3\2\2\2")
        buf.write("\u010c\u010a\3\2\2\2\u010d\u010e\7\62\2\2\u010e\u0110")
        buf.write("\3\2\2\2\u010f\u00f9\3\2\2\2\u010f\u0104\3\2\2\2\u0110")
        buf.write("-\3\2\2\2\u0111\u0115\7\26\2\2\u0112\u0116\5H%\2\u0113")
        buf.write("\u0114\7,\2\2\u0114\u0116\7\26\2\2\u0115\u0112\3\2\2\2")
        buf.write("\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117\3")
        buf.write("\2\2\2\u0117\u0118\5\60\31\2\u0118\u0119\5$\23\2\u0119")
        buf.write("\u011a\7\66\2\2\u011a/\3\2\2\2\u011b\u011c\t\b\2\2\u011c")
        buf.write("\61\3\2\2\2\u011d\u011e\7\3\2\2\u011e\u011f\7/\2\2\u011f")
        buf.write("\u0120\5$\23\2\u0120\u0121\7\60\2\2\u0121\u012b\5F$\2")
        buf.write("\u0122\u0123\7\4\2\2\u0123\u0124\7\3\2\2\u0124\u0125\7")
        buf.write("/\2\2\u0125\u0126\5$\23\2\u0126\u0127\7\60\2\2\u0127\u0128")
        buf.write("\5F$\2\u0128\u012a\3\2\2\2\u0129\u0122\3\2\2\2\u012a\u012d")
        buf.write("\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write("\u0130\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u012f\7\4\2\2")
        buf.write("\u012f\u0131\5F$\2\u0130\u012e\3\2\2\2\u0130\u0131\3\2")
        buf.write("\2\2\u0131\63\3\2\2\2\u0132\u0135\7\5\2\2\u0133\u0136")
        buf.write("\5\66\34\2\u0134\u0136\5> \2\u0135\u0133\3\2\2\2\u0135")
        buf.write("\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138\5F$\2\u0138")
        buf.write("\65\3\2\2\2\u0139\u0141\5:\36\2\u013a\u013b\58\35\2\u013b")
        buf.write("\u013c\7\66\2\2\u013c\u013d\5:\36\2\u013d\u013e\7\66\2")
        buf.write("\2\u013e\u013f\5<\37\2\u013f\u0141\3\2\2\2\u0140\u0139")
        buf.write("\3\2\2\2\u0140\u013a\3\2\2\2\u0141\67\3\2\2\2\u0142\u0143")
        buf.write("\7\26\2\2\u0143\u0144\7&\2\2\u0144\u0145\5$\23\2\u0145")
        buf.write("9\3\2\2\2\u0146\u0147\5$\23\2\u0147;\3\2\2\2\u0148\u0149")
        buf.write("\7\26\2\2\u0149\u014a\5\60\31\2\u014a\u014b\5$\23\2\u014b")
        buf.write("=\3\2\2\2\u014c\u014d\t\t\2\2\u014d\u014e\7\65\2\2\u014e")
        buf.write("\u014f\7\26\2\2\u014f\u0150\7&\2\2\u0150\u0151\7\23\2")
        buf.write("\2\u0151\u0152\7\26\2\2\u0152?\3\2\2\2\u0153\u0154\7\22")
        buf.write("\2\2\u0154\u0155\7\66\2\2\u0155A\3\2\2\2\u0156\u0157\7")
        buf.write("\21\2\2\u0157\u0158\7\66\2\2\u0158C\3\2\2\2\u0159\u015c")
        buf.write("\7\26\2\2\u015a\u015b\7,\2\2\u015b\u015d\7\26\2\2\u015c")
        buf.write("\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e\3\2\2\2")
        buf.write("\u015e\u0167\7/\2\2\u015f\u0164\5$\23\2\u0160\u0161\7")
        buf.write("\65\2\2\u0161\u0163\5$\23\2\u0162\u0160\3\2\2\2\u0163")
        buf.write("\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2")
        buf.write("\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u015f\3")
        buf.write("\2\2\2\u0167\u0168\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a")
        buf.write("\7\60\2\2\u016a\u016b\7\66\2\2\u016bE\3\2\2\2\u016c\u0170")
        buf.write("\7\61\2\2\u016d\u016f\5(\25\2\u016e\u016d\3\2\2\2\u016f")
        buf.write("\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2")
        buf.write("\u0171\u0173\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u0174\7")
        buf.write("\62\2\2\u0174G\3\2\2\2\u0175\u0176\7\63\2\2\u0176\u0177")
        buf.write("\7\67\2\2\u0177\u0179\7\64\2\2\u0178\u0175\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2")
        buf.write("\u017bI\3\2\2\2#MU[`dhptx\u0086\u0093\u00a5\u00af\u00b7")
        buf.write("\u00c1\u00d2\u00d4\u00db\u00e4\u00ef\u00ff\u010a\u010f")
        buf.write("\u0115\u012b\u0130\u0135\u0140\u015c\u0164\u0167\u0170")
        buf.write("\u017a")
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
    RULE_typeDefinition = 8
    RULE_structDefinition = 9
    RULE_structFields = 10
    RULE_interfaceDefinition = 11
    RULE_interfaceFields = 12
    RULE_listParams = 13
    RULE_listIdentifier = 14
    RULE_funcParams = 15
    RULE_funcParam = 16
    RULE_expression = 17
    RULE_term = 18
    RULE_statement = 19
    RULE_arrayLiteral = 20
    RULE_arraysBlock = 21
    RULE_assignStatement = 22
    RULE_assignmentOperator = 23
    RULE_ifStatement = 24
    RULE_forStatement = 25
    RULE_forLoop = 26
    RULE_initilization = 27
    RULE_forCondition = 28
    RULE_forUpdate = 29
    RULE_forIteration = 30
    RULE_breakStatement = 31
    RULE_continueStatement = 32
    RULE_callStatement = 33
    RULE_block = 34
    RULE_arrayDims = 35

    ruleNames =  [ "program", "tYPE", "parserRuleSpec", "decl", "varDecl", 
                   "funcDecl", "typeDecl", "constDecl", "typeDefinition", 
                   "structDefinition", "structFields", "interfaceDefinition", 
                   "interfaceFields", "listParams", "listIdentifier", "funcParams", 
                   "funcParam", "expression", "term", "statement", "arrayLiteral", 
                   "arraysBlock", "assignStatement", "assignmentOperator", 
                   "ifStatement", "forStatement", "forLoop", "initilization", 
                   "forCondition", "forUpdate", "forIteration", "breakStatement", 
                   "continueStatement", "callStatement", "block", "arrayDims" ]

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
            self.state = 73 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                self.parserRuleSpec()
                self.state = 75 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0)):
                    break

            self.state = 77
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
            self.state = 79
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
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
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
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.varDecl()
                pass
            elif token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.funcDecl()
                pass
            elif token in [MiniGoParser.TYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.typeDecl()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
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
            self.state = 91
            self.match(MiniGoParser.VAR)
            self.state = 92
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LSB:
                self.state = 93
                self.arrayDims()


            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 96
                self.tYPE()
                pass

            elif la_ == 2:
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.INTERGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0):
                    self.state = 97
                    self.tYPE()


                self.state = 100
                self.match(MiniGoParser.ASSIGNOP)
                self.state = 101
                self.expression(0)
                pass


            self.state = 104
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
            self.state = 106
            self.match(MiniGoParser.FUNC)
            self.state = 107
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 108
            self.match(MiniGoParser.LP)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.IDENTIFIER:
                self.state = 109
                self.funcParams()


            self.state = 112
            self.match(MiniGoParser.RP)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.INTERGER) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0):
                self.state = 113
                self.tYPE()


            self.state = 116
            self.block()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMI:
                self.state = 117
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
            self.state = 120
            self.match(MiniGoParser.TYPE)
            self.state = 121
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 122
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
            self.state = 124
            self.match(MiniGoParser.CONST)
            self.state = 125
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 126
            self.match(MiniGoParser.ASSIGNOP)
            self.state = 127
            self.expression(0)
            self.state = 128
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
        self.enterRule(localctx, 16, self.RULE_typeDefinition)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRUCT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.structDefinition()
                pass
            elif token in [MiniGoParser.INTERFACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
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
        self.enterRule(localctx, 18, self.RULE_structDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(MiniGoParser.STRUCT)
            self.state = 135
            self.match(MiniGoParser.LB)
            self.state = 136
            self.structFields()
            self.state = 137
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
        self.enterRule(localctx, 20, self.RULE_structFields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 139
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 140
                self.tYPE()
                self.state = 141
                self.match(MiniGoParser.SEMI)
                self.state = 145 
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
        self.enterRule(localctx, 22, self.RULE_interfaceDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(MiniGoParser.INTERFACE)
            self.state = 148
            self.match(MiniGoParser.LB)
            self.state = 149
            self.interfaceFields()
            self.state = 150
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
        self.enterRule(localctx, 24, self.RULE_interfaceFields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 153
            self.listParams()
            self.state = 154
            self.tYPE()
            self.state = 155
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
        self.enterRule(localctx, 26, self.RULE_listParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(MiniGoParser.LP)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.IDENTIFIER:
                self.state = 158
                self.listIdentifier()
                self.state = 159
                self.tYPE()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
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
        self.enterRule(localctx, 28, self.RULE_listIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 169
                self.match(MiniGoParser.COMMA)
                self.state = 170
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 175
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
        self.enterRule(localctx, 30, self.RULE_funcParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.funcParam()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.COMMA:
                self.state = 177
                self.match(MiniGoParser.COMMA)
                self.state = 178
                self.funcParam()
                self.state = 183
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
        self.enterRule(localctx, 32, self.RULE_funcParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 185
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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUBOP, MiniGoParser.NOTOP]:
                self.state = 188
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUBOP or _la==MiniGoParser.NOTOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 189
                self.term()
                pass
            elif token in [MiniGoParser.IDENTIFIER, MiniGoParser.LP, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.STRINGLIT]:
                self.state = 190
                self.term()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 208
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 193
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 194
                        self.match(MiniGoParser.OROP)
                        self.state = 195
                        self.term()
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 196
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 197
                        self.match(MiniGoParser.ANDOP)
                        self.state = 198
                        self.term()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 199
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 200
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUALOP) | (1 << MiniGoParser.NOTEQUALOP) | (1 << MiniGoParser.LESSOP) | (1 << MiniGoParser.LESSEQUALOP) | (1 << MiniGoParser.GREATEROP) | (1 << MiniGoParser.GREATEREQUALOP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 201
                        self.term()
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 202
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 203
                        _la = self._input.LA(1)
                        if not(_la==MiniGoParser.ADDOP or _la==MiniGoParser.SUBOP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 204
                        self.term()
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 205
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 206
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULOP) | (1 << MiniGoParser.DIVOP) | (1 << MiniGoParser.MODOP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 207
                        self.term()
                        pass

             
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self.enterRule(localctx, 36, self.RULE_term)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 217
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 214
                    self.arrayDims()

                elif la_ == 2:
                    self.state = 215
                    self.match(MiniGoParser.DOT)
                    self.state = 216
                    self.match(MiniGoParser.IDENTIFIER)


                pass
            elif token in [MiniGoParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(MiniGoParser.INTLIT)
                pass
            elif token in [MiniGoParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.match(MiniGoParser.FLOATLIT)
                pass
            elif token in [MiniGoParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 221
                self.match(MiniGoParser.STRINGLIT)
                pass
            elif token in [MiniGoParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 222
                self.match(MiniGoParser.LP)
                self.state = 223
                self.expression(0)
                self.state = 224
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
        self.enterRule(localctx, 38, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 228
                self.assignStatement()
                pass

            elif la_ == 2:
                self.state = 229
                self.ifStatement()
                pass

            elif la_ == 3:
                self.state = 230
                self.forStatement()
                pass

            elif la_ == 4:
                self.state = 231
                self.breakStatement()
                pass

            elif la_ == 5:
                self.state = 232
                self.continueStatement()
                pass

            elif la_ == 6:
                self.state = 233
                self.callStatement()
                pass

            elif la_ == 7:
                self.state = 234
                self.arrayLiteral()
                pass

            elif la_ == 8:
                self.state = 235
                self.varDecl()
                pass

            elif la_ == 9:
                self.state = 236
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
        self.enterRule(localctx, 40, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 242
            self.match(MiniGoParser.SHORTASSIGNOP)

            self.state = 243
            self.arrayDims()
            self.state = 244
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INTERFACE) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 245
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
        self.enterRule(localctx, 42, self.RULE_arraysBlock)
        self._la = 0 # Token type
        try:
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(MiniGoParser.LB)
                self.state = 248
                self.arraysBlock()
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 249
                    self.match(MiniGoParser.COMMA)
                    self.state = 250
                    self.arraysBlock()
                    self.state = 255
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 256
                self.match(MiniGoParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.match(MiniGoParser.LB)
                self.state = 259
                self.expression(0)
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 260
                    self.match(MiniGoParser.COMMA)
                    self.state = 261
                    self.expression(0)
                    self.state = 266
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 267
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
        self.enterRule(localctx, 44, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LSB]:
                self.state = 272
                self.arrayDims()
                pass
            elif token in [MiniGoParser.DOT]:
                self.state = 273
                self.match(MiniGoParser.DOT)
                self.state = 274
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.SHORTASSIGNOP, MiniGoParser.INCASSIGNOP, MiniGoParser.DECASSIGNOP, MiniGoParser.MULASSIGNOP, MiniGoParser.DIVASSIGNOP, MiniGoParser.MODASSIGNOP]:
                pass
            else:
                pass
            self.state = 277
            self.assignmentOperator()
            self.state = 278
            self.expression(0)
            self.state = 279
            self.match(MiniGoParser.SEMI)
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
        self.enterRule(localctx, 46, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
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
        self.enterRule(localctx, 48, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(MiniGoParser.IF)
            self.state = 284
            self.match(MiniGoParser.LP)
            self.state = 285
            self.expression(0)
            self.state = 286
            self.match(MiniGoParser.RP)
            self.state = 287
            self.block()
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 288
                    self.match(MiniGoParser.ELSE)
                    self.state = 289
                    self.match(MiniGoParser.IF)
                    self.state = 290
                    self.match(MiniGoParser.LP)
                    self.state = 291
                    self.expression(0)
                    self.state = 292
                    self.match(MiniGoParser.RP)
                    self.state = 293
                    self.block() 
                self.state = 299
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 300
                self.match(MiniGoParser.ELSE)
                self.state = 301
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
        self.enterRule(localctx, 50, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(MiniGoParser.FOR)
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 305
                self.forLoop()
                pass

            elif la_ == 2:
                self.state = 306
                self.forIteration()
                pass


            self.state = 309
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
        self.enterRule(localctx, 52, self.RULE_forLoop)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.forCondition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.initilization()
                self.state = 313
                self.match(MiniGoParser.SEMI)
                self.state = 314
                self.forCondition()
                self.state = 315
                self.match(MiniGoParser.SEMI)
                self.state = 316
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
        self.enterRule(localctx, 54, self.RULE_initilization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 321
            self.match(MiniGoParser.SHORTASSIGNOP)
            self.state = 322
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
        self.enterRule(localctx, 56, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
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
        self.enterRule(localctx, 58, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 327
            self.assignmentOperator()
            self.state = 328
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
        self.enterRule(localctx, 60, self.RULE_forIteration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.IDENTIFIER or _la==MiniGoParser.BLANK):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 331
            self.match(MiniGoParser.COMMA)
            self.state = 332
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 333
            self.match(MiniGoParser.SHORTASSIGNOP)
            self.state = 334
            self.match(MiniGoParser.RANGE)
            self.state = 335
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
        self.enterRule(localctx, 62, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(MiniGoParser.BREAK)
            self.state = 338
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
        self.enterRule(localctx, 64, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(MiniGoParser.CONTINUE)
            self.state = 341
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
        self.enterRule(localctx, 66, self.RULE_callStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.DOT:
                self.state = 344
                self.match(MiniGoParser.DOT)
                self.state = 345
                self.match(MiniGoParser.IDENTIFIER)


            self.state = 348
            self.match(MiniGoParser.LP)
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IDENTIFIER) | (1 << MiniGoParser.SUBOP) | (1 << MiniGoParser.NOTOP) | (1 << MiniGoParser.LP) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.STRINGLIT))) != 0):
                self.state = 349
                self.expression(0)
                self.state = 354
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.COMMA:
                    self.state = 350
                    self.match(MiniGoParser.COMMA)
                    self.state = 351
                    self.expression(0)
                    self.state = 356
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 359
            self.match(MiniGoParser.RP)
            self.state = 360
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
        self.enterRule(localctx, 68, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(MiniGoParser.LB)
            self.state = 366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.IDENTIFIER))) != 0):
                self.state = 363
                self.statement()
                self.state = 368
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 369
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
        self.enterRule(localctx, 70, self.RULE_arrayDims)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 371
                    self.match(MiniGoParser.LSB)
                    self.state = 372
                    self.match(MiniGoParser.INTLIT)
                    self.state = 373
                    self.match(MiniGoParser.RSB)

                else:
                    raise NoViableAltException(self)
                self.state = 376 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
        self._predicates[17] = self.expression_sempred
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
         




