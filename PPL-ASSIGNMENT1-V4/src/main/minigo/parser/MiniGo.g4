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

program  : (declaration | statement | mainFunction)+ EOF ;

mainFunction: FUNC 'main' LPAREN RPAREN block endOfStatement?;

baseType: INT | FLOAT | STRING | BOOLEAN | IDENTIFIER;

endOfStatement: SEMI | EOF | NEWLINE;

declaration: varDecl endOfStatement 
           | funcDecl endOfStatement?
           | typeDecl endOfStatement
           | constDecl endOfStatement 
           | methodDecl endOfStatement?;


varDecl: VAR IDENTIFIER (COMMA IDENTIFIER)* arrayDims? (baseType | baseType? (ASSIGN expression));
funcDecl: FUNC IDENTIFIER LPAREN (funcParams)? RPAREN (arrayDims? baseType)? block;
typeDecl: TYPE IDENTIFIER (structDefinition | interfaceDefinition);
constDecl: CONST IDENTIFIER ASSIGN expression;
methodDecl: FUNC LPAREN IDENTIFIER IDENTIFIER RPAREN IDENTIFIER LPAREN (funcParams)? RPAREN baseType? block;

structDefinition: STRUCT LBRACE structFields* RBRACE;
structFields: IDENTIFIER (arrayDims? baseType | structDefinition) endOfStatement;

interfaceDefinition: INTERFACE LBRACE interfaceFields* RBRACE;
listParams: LPAREN (listIdentifier baseType)* RPAREN;
listIdentifier: IDENTIFIER (COMMA IDENTIFIER)*;
interfaceFields: IDENTIFIER listParams baseType? endOfStatement;

funcParams: funcParam (COMMA funcParam)*;
funcParam: IDENTIFIER (arrayDims? baseType);

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
         | constDecl endOfStatement
         | block endOfStatement?;


arrayLit: arrayDims baseType arraysBlock;
arraysBlock: LBRACE arraysBlock (COMMA arraysBlock)* RBRACE | LBRACE expression (COMMA expression)* RBRACE;

structExpression: IDENTIFIER LBRACE (structFieldsAssign (COMMA structFieldsAssign)* COMMA?)? RBRACE;
structBlock: expression 
           | arrayLit 
           | structExpression;
          // | structDefinition LBRACE ((IDENTIFIER COLON)? expression (COMMA (IDENTIFIER COLON)? expression)* COMMA?)? RBRACE;
structFieldsAssign: IDENTIFIER COLON structBlock;

assignStatement: (a1 (COMMA a1)*) assignmentOperator a2 (COMMA a2)*;
a1: (callStatement | IDENTIFIER) DOT a1 
  | IDENTIFIER arrayDims?;
a2: expression | arrayLit | structExpression;
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

returnStatement: RETURN (expression | arrayLit)?;

arguments: expression (COMMA expression)*;
block: LBRACE statement* RBRACE;
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
STRING_LIT: '"' (ESC_SEQ | ~["\\])* '"';
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
        self.TRUE, self.FALSE, self.BREAK, self.CONTINUE, self.RETURN
    ];
    if self.lastTokenType in listAllowedToken:
        self.text = ';';
    else:
        self.skip();
};

UNCLOSE_STRING: '"' (ESC_SEQ | ~["\\])*;
ILLEGAL_ESCAPE: '"' (ESC_SEQ | ~["\\])* '\\' ~[nrt"\\];
ERROR_CHAR: .;