// STUDENT ID: 2213187
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options {
    language = Python3;
}

//------------------ Parser Rules ------------------
program: declaration* mainFunction? declaration* EOF;

mainFunction: FUNC 'main' LPAREN RPAREN block {print("main function")};

tYPE: baseType | arrayType | IDENTIFIER;
baseType: INT | FLOAT | STRING | BOOLEAN;
arrayType: (baseType | IDENTIFIER) arrayDims;

endOfStatement: SEMI | EOF;

declaration: varDecl | funcDecl | typeDecl | constDecl | methodDecl;
varDecl: VAR IDENTIFIER (COMMA IDENTIFIER)* arrayDims? (tYPE | tYPE? (ASSIGN expression)) endOfStatement;
funcDecl: FUNC IDENTIFIER LPAREN (funcParams)? RPAREN tYPE? block endOfStatement;
typeDecl: TYPE IDENTIFIER (structDefinition | interfaceDefinition);
constDecl: CONST IDENTIFIER ASSIGN expression endOfStatement;
methodDecl: FUNC LPAREN IDENTIFIER IDENTIFIER RPAREN IDENTIFIER LPAREN (funcParams)? RPAREN tYPE? block endOfStatement;

structDefinition: STRUCT LBRACE structFields* RBRACE endOfStatement;
structFields: IDENTIFIER tYPE endOfStatement;

interfaceDefinition: INTERFACE LBRACE interfaceFields RBRACE endOfStatement;
listParams: LPAREN (listIdentifier tYPE)* RPAREN;
listIdentifier: IDENTIFIER (COMMA IDENTIFIER)*;
interfaceFields: IDENTIFIER listParams tYPE? endOfStatement;

funcParams: funcParam (COMMA funcParam)*;
funcParam: IDENTIFIER tYPE;

expression: expression OR term
          | expression AND term
          | expression (EQ | NEQ | LT | LEQ | GT | GEQ) term
          | expression (PLUS | MINUS) term
          | expression (MUL | DIV | MOD) term
          | (NOT | MINUS) term
          | term;
term: IDENTIFIER (arrayDims | DOT IDENTIFIER)?
    | INT_LIT
    | FLOAT_LIT
    | STRING_LIT
    | LPAREN expression RPAREN;

statement: (assignStatement
         | ifStatement
         | forStatement
         | breakStatement
         | continueStatement
         | callStatement
         | returnStatement
         | arrayLiteral
         | varDecl
         | constDecl);

arrayLiteral: IDENTIFIER DECLARE (arrayDims) (INTERFACE | FLOAT | STRING | BOOLEAN) arraysBlock;
arraysBlock: LBRACE arraysBlock (COMMA arraysBlock)* RBRACE | LBRACE expression (COMMA expression)* RBRACE;

structExpression: IDENTIFIER LBRACE (IDENTIFIER COLON expression COMMA?)* RBRACE;

assignStatement: IDENTIFIER (arrayDims | DOT IDENTIFIER)? assignmentOperator (expression | structExpression) endOfStatement;
assignmentOperator: DECLARE | PLUS_ASSIGN | MINUS_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;

ifStatement: IF LPAREN expression RPAREN block
             (ELSE IF LPAREN expression RPAREN block)*
             (ELSE block)? endOfStatement;

forStatement: FOR ( forLoop | forIteration) block;

forLoop: forCondition
         | initilization SEMI forCondition SEMI forUpdate;

initilization: IDENTIFIER DECLARE expression;
forCondition: expression;
forUpdate: IDENTIFIER assignmentOperator expression;

forIteration: (IDENTIFIER | BLANK) COMMA IDENTIFIER DECLARE RANGE IDENTIFIER;

breakStatement: BREAK endOfStatement;

continueStatement: CONTINUE endOfStatement;

callStatement: IDENTIFIER (DOT IDENTIFIER)? LPAREN (expression (COMMA expression)*)? RPAREN endOfStatement;

returnStatement: RETURN expression? endOfStatement;

block: LBRACE (statement)* RBRACE;
arrayDims: (LBRACKET INT_LIT RBRACKET)+;

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
BLANK   : '_';

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
WS: [ \t\f\r]+ -> skip;

// Whitespace
NEWLINE: '\n' {
    lastToken = self.lastTokenType
    if lastToken in [self.IDENTIFIER, self.INT_LIT, self.FLOAT_LIT, self.STRING_LIT, self.BOOL_LIT, self.RPAREN, self.RBRACE]:
        self.text = ';';
    else:
        self.skip();
};

// Error handling
UNCLOSE_STRING: '"' (ESC_SEQ | ~["\\\r\n])* {self.text = self.text[1:]};
ILLEGAL_ESCAPE: '"' (ESC_SEQ | ~["\\\r\n])* '\\' ~[nrt"\\] {self.text = self.text[1:]};
ERROR_CHAR: .;