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

options{
	language=Python3;
}

program  : declaration+ EOF ;

// mainFunction: FUNC 'main' LPAREN RPAREN LBRACE statement* RBRACE endOfStatement?;

baseType: INT | FLOAT | STRING | BOOLEAN | IDENTIFIER;

endOfStatement: SEMI | NEWLINE | EOF;

declaration: varDecl endOfStatement 
           | funcDecl endOfStatement
           | typeDecl endOfStatement
           | constDecl endOfStatement 
           | methodDecl endOfStatement;

varDecl: VAR IDENTIFIER (COMMA IDENTIFIER)* (baseType |assignDecl | arrayDecl | arrayLitDecl);
arrayDecl : (LBRACKET (INT_LIT | IDENTIFIER) RBRACKET)+ baseType (ASSIGN arraysBlock)?;
arrayLitDecl: ((LBRACKET (INT_LIT | IDENTIFIER) RBRACKET)+ baseType)? ASSIGN (LBRACKET (INT_LIT | IDENTIFIER) RBRACKET)+ baseType arraysBlock;
assignDecl: (baseType? ASSIGN (expression | structLit));

funcDecl: FUNC IDENTIFIER listParams (arrayDims? baseType)? LBRACE statement* RBRACE;
typeDecl: TYPE IDENTIFIER (structDefinition | interfaceDefinition);
constDecl: CONST IDENTIFIER ASSIGN expression;
methodDecl: FUNC LPAREN IDENTIFIER IDENTIFIER RPAREN IDENTIFIER listParams (arrayDims? baseType)? LBRACE statement* RBRACE;

structDefinition: STRUCT LBRACE structFields* RBRACE;
structFields: IDENTIFIER arrayDims? baseType endOfStatement;

interfaceDefinition: INTERFACE LBRACE interfaceFields* RBRACE;
interfaceFields: IDENTIFIER listParams (arrayDims? baseType)? endOfStatement;

listParams: LPAREN listIdentifier? RPAREN;
listIdentifier: listGroup (COMMA listGroup)*;
listGroup: funcParam (COMMA funcParam)* baseType;
funcParam: IDENTIFIER arrayDims?;

expression: logicOrExp;
logicOrExp: logicAndExp (OR logicOrExp)*;
logicAndExp: equalityExp (AND logicAndExp)*;
equalityExp: additiveExp ((EQ | NEQ | LT | LEQ | GT | GEQ) additiveExp)*;
additiveExp: multiplicativeExp ((PLUS | MINUS) multiplicativeExp)*;
multiplicativeExp: unaryExp ((MUL | DIV | MOD) unaryExp)*;
unaryExp: (MINUS | NOT)* postfixExp;

postfixExp: primaryExp 
          | postfixExp LBRACKET expression RBRACKET
          | postfixExp DOT IDENTIFIER
          | postfixExp LPAREN arguments? RPAREN;

primaryExp: LPAREN expression RPAREN
          | literal
          | callStatement
          | IDENTIFIER;

literal: INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL;


statement: assignStatement endOfStatement
         | ifStatement endOfStatement
         | forStatement endOfStatement
         | breakStatement endOfStatement
         | continueStatement endOfStatement
         | callStatement endOfStatement
         | returnStatement endOfStatement
         | varDecl endOfStatement
         | typeDecl endOfStatement
         | methodDecl endOfStatement
         | constDecl endOfStatement;


arrayLit: arrayDims baseType arraysBlock;
arraysBlock: LBRACE arraysBlock (COMMA arraysBlock)* RBRACE 
           | LBRACE (literals (COMMA literals)* COMMA?)? RBRACE;

literals: INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL | structLit;

structLit: IDENTIFIER LBRACE (structFieldsAssign (COMMA structFieldsAssign)* COMMA?)? RBRACE;
structBlock: expression 
           | arrayLit 
           | structLit;
structFieldsAssign: IDENTIFIER COLON structBlock;

assignStatement: (a1 (COMMA a1)*) assignmentOperator a2 (COMMA a2)*;
a1: (callStatement | IDENTIFIER) DOT a1 
  | IDENTIFIER arrayDims? (DOT a1)?;
a2: expression | arrayLit | structLit;
assignmentOperator: DECLARE | PLUS_ASSIGN | MINUS_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;

ifStatement: IF expression block NEWLINE?
             (ELSE IF expression block NEWLINE?)*
             (ELSE block)?;

forStatement: FOR ( forLoop | forIteration) block;

forLoop: forCondition
         | initilization SEMI forCondition SEMI forUpdate;

initilization: IDENTIFIER DECLARE expression;
forCondition: expression;
forUpdate: IDENTIFIER assignmentOperator expression;

forIteration: (IDENTIFIER | BLANK) COMMA IDENTIFIER DECLARE RANGE IDENTIFIER;

breakStatement: BREAK;

continueStatement: CONTINUE;

primaryCall: IDENTIFIER LPAREN arguments? RPAREN;
callStatement: IDENTIFIER arrayDims? DOT callStatement 
            |  primaryCall (DOT callStatement)?;

returnStatement: RETURN (expression | arrayLit | structLit)?;

arguments: expression (COMMA expression)*;
block: LBRACE statement+ RBRACE;
arrayDims: (LBRACKET expression? RBRACKET)+;

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
STRING_LIT: '"' (ESC_SEQ | ~["\\\r\n])* '"' {self.text = self.text[1:-1];};
fragment ESC_SEQ: '\\' [nrt"\\];

// Comments
BLOCK_COMMENT: '/*' (BLOCK_COMMENT|.)*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\f\r]+ -> skip;

NEWLINE: '\n' {
    listAllowedToken = [
        self.IDENTIFIER, self.INT_LIT, self.FLOAT_LIT, self.STRING_LIT,
        self.RPAREN, self.RBRACE, self.RBRACKET,
        self.INT, self.FLOAT, self.STRING, self.BOOLEAN,
        self.TRUE, self.FALSE, self.BREAK, self.CONTINUE, self.RETURN, self.NIL
    ];
    if self.lastTokenType in listAllowedToken:
        self.text = ';';
    else:
        self.skip();
};

UNCLOSE_STRING: '"' (ESC_SEQ | ~["\\\r\n])* ([\r\n] | EOF);
ILLEGAL_ESCAPE: '"' (ESC_SEQ | ~["\\\r\n])* '\\' ~[nrt"\\];
ERROR_CHAR: .;