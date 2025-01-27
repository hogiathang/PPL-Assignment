// STUDENT ID: 2213187

grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options{
	language = Python3;
}

//------------------ Parser Rules ------------------
program: EOF;

//------------------ Lexer Rules -------------------
// Keywords
IF      : 'if';
ELSE    : 'else';
FOR     : 'for';
RETURN  : 'return';
FUNC    : 'func';
TYPE    : 'type';
STRUCT  : 'struct';
INTERFACE: 'interface';
STRING  : 'string';
INT     : 'int';
FLOAT   : 'float';
BOOLEAN : 'boolean';
TRUE    : 'true';
FALSE   : 'false';
NIL     : 'nil';
CONST   : 'const';
VAR     : 'var';
CONTINUE: 'continue';
BREAK   : 'break';
RANGE   : 'range';

// Operators
ASSIGN  : '=';
DECLARE : ':=';
PLUS    : '+';
MINUS   : '-';
MUL     : '*';
DIV     : '/';
MOD     : '%';
EQ      : '==';
NEQ     : '!=';
LT      : '<';
LEQ     : '<=';
GT      : '>';
GEQ     : '>=';
AND     : '&&';
OR      : '||';
NOT     : '!';
PLUS_ASSIGN  : '+=';
MINUS_ASSIGN : '-=';
MUL_ASSIGN   : '*=';
DIV_ASSIGN   : '/=';
MOD_ASSIGN   : '%=';
DOT     : '.';

// Separators
LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
LBRACKET: '[';
RBRACKET: ']';
COMMA   : ',';
SEMI    : ';';
COLON   : ':';

// Identifiers
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// Literals
// Integer
INT_LIT: DEC_LIT | BIN_LIT | OCT_LIT | HEX_LIT;
fragment DEC_LIT: '0' | [1-9][0-9]*;
fragment BIN_LIT: '0' [bB] [0-1]+;
fragment OCT_LIT: '0' [oO] [0-7]+ | '0' [0-7]+;
fragment HEX_LIT: '0' [xX] [0-9a-fA-F]+;

// Float
FLOAT_LIT: DEC_PART ('.' DEC_PART? EXPONENT? | EXPONENT);
fragment DEC_PART: [0-9]+;
fragment EXPONENT: [eE] [+-]? [0-9]+;

// String
STRING_LIT: '"' (ESC_SEQ | ~["\\\r\n])* '"' {self.text = self.text[1:-1]};
fragment ESC_SEQ: '\\' [nrt"\\];

// Boolean
BOOL_LIT: TRUE | FALSE;

// Comments
BLOCK_COMMENT: '/*' (BLOCK_COMMENT|.)*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

// Whitespace
WS: [ \t\f\r\n]+ -> skip;

// Error handling
UNCLOSE_STRING: '"' (ESC_SEQ | ~["\\\r\n])* {self.text = self.text[1:]};
ILLEGAL_ESCAPE: '"' (ESC_SEQ | ~["\\\r\n])* '\\' ~[nrt"\\] {self.text = self.text[1:]};
ERROR_CHAR: .;