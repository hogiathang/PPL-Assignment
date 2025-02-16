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

options{
	language=Python3;
}
program  : declaration+ EOF ;

declaration: varDecl endOfStatement
           | funcDecl endOfStatement
           | constDecl endOfStatement
           | methodDecl endOfStatement
           | typeDecl endOfStatement;
        
        

varDecl: VAR IDENTIFIER varDetail;
varDetail: varDeclType varDeclExpr
         | varDeclType 
         | varDeclExpr;


varDeclType: baseType 
           | arrayType baseType;
arrayType: LBRACKET intLitOrConstant RBRACKET arrayType | LBRACKET intLitOrConstant RBRACKET;
varDeclExpr: DECLARE expr;

constDecl: CONST IDENTIFIER varDeclExpr;

arrayLit: arrayType baseType arrayBlock;
arrayBlock: LBRACE arrayLitList RBRACE;
arrayLitList: arrayLitContent arrayLitListTail;
arrayLitListTail: COMMA arrayLitContent arrayLitListTail |;
arrayLitContent: arrayBlock | noArrayLit;

structLit: IDENTIFIER LBRACE optionalStructFields RBRACE;
optionalStructFields: structFieldList |;
structFieldList: structFieldAssign structFieldListTail;
structFieldListTail: COMMA structFieldAssign structFieldListTail |;
structFieldAssign: IDENTIFIER COLON structBlock;
structBlock: expr;

methodDecl: FUNC LPAREN IDENTIFIER IDENTIFIER RPAREN IDENTIFIER LPAREN funcParam RPAREN funcType LBRACE statement* RBRACE;
funcDecl: FUNC IDENTIFIER LPAREN funcParam RPAREN funcType LBRACE statement* RBRACE;
funcType: baseType
        | arrayType baseType
        |;
funcParam: funcListIdentifiers varDeclType COMMA funcParam
         | funcListIdentifiers varDeclType 
         |;
funcListIdentifiers: IDENTIFIER | IDENTIFIER COMMA funcListIdentifiers;

typeDecl: TYPE IDENTIFIER STRUCT structDeclBlock | TYPE IDENTIFIER INTERFACE interfaceDeclBlock;

structType: baseType | arrayType baseType;
structDeclBlock: LBRACE structDeclField RBRACE;
structDeclField: IDENTIFIER  structType endOfStatement structDeclField |;

interfaceDeclBlock: LBRACE interfaceDeclField RBRACE;
interfaceDeclField: IDENTIFIER LPAREN funcParam RPAREN funcType endOfStatement interfaceDeclField |;

expr: logicOrExpr | arrayLit | structLit;
logicOrExpr: logicOrExpr OR logicAndExpr | logicAndExpr;
logicAndExpr: logicAndExpr AND equalityExpr | equalityExpr;
equalityExpr: equalityExpr relationOp additiveExpr | additiveExpr;
additiveExpr: additiveExpr addOp multiplicativeExpr | multiplicativeExpr;
multiplicativeExpr: multiplicativeExpr mulOp unaryExpr | unaryExpr;
unaryExpr: unaryOp unaryExpr | primaryExpr;
primaryExpr
    : term primarySuffix*;

primarySuffix
    : DOT IDENTIFIER                         
    | LBRACKET expr RBRACKET                 
    | LPAREN argList? RPAREN;

argList
    : expr (COMMA expr)*;
statement: declarationStatement endOfStatement
        | assignStatement endOfStatement
        | ifStatement endOfStatement
        | forStatement endOfStatement
        | breakStatement endOfStatement
        | continueStatement endOfStatement
        | callStatement endOfStatement
        | returnStatement endOfStatement;
// Declaration Statement
declarationStatement: varDecl
                   | constDecl;
// Assign Statement
assignStatement: assignStateLHS ASSIGN assignStateRHS
               | assignStateLHS PLUS_ASSIGN assignStateRHS
               | assignStateLHS MINUS_ASSIGN assignStateRHS
               | assignStateLHS MUL_ASSIGN assignStateRHS
               | assignStateLHS DIV_ASSIGN assignStateRHS
               | assignStateLHS MOD_ASSIGN assignStateRHS;

assignStateLHS: IDENTIFIER assignStateLHSTail;
assignStateLHSTail: DOT IDENTIFIER assignStateLHSTail | LBRACKET expr RBRACKET assignStateLHSTail |;

assignStateRHS: expr;
// If Statement
ifStatement: IF LPAREN expr RPAREN LBRACE statement* RBRACE
           | IF LPAREN expr RPAREN LBRACE statement* RBRACE elseIfStatement ELSE LBRACE statement* RBRACE;
elseIfStatement: ELSE IF LPAREN expr RPAREN LBRACE statement* RBRACE elseIfStatement |;

// For Statement
forStatement: basicForStatement | forRangeStatement;

basicForStatement: FOR forCondition LBRACE statement* RBRACE
                 | FOR forInitilization SEMI forCondition SEMI forUpdate LBRACE statement* RBRACE;
forCondition: expr;
forInitilization: assignStatement | varDecl;
forUpdate: assignStatement;

forRangeStatement: FOR index COMMA value ASSIGN RANGE forArray LBRACE statement* RBRACE;

// break statement
breakStatement: BREAK;
// continue statement
continueStatement: CONTINUE;
// Call Statement
callStatement: IDENTIFIER callStatementArrayTail DOT callStatement
             | IDENTIFIER LPAREN callStatementParam RPAREN DOT callStatement
             | IDENTIFIER LPAREN callStatementParam RPAREN;
callStatementArrayTail: LBRACKET expr RBRACKET callStatementArrayTail |;
callStatementParam: expr COMMA callStatementParam | expr |;

// Return Statement
returnStatement: RETURN expr | RETURN;

index: IDENTIFIER | BLANK;
value: IDENTIFIER;
forArray: expr;
relationOp: EQ | NEQ | LT | LEQ | GT | GEQ;
addOp: PLUS | MINUS;
mulOp: MUL | DIV | MOD;
unaryOp: MINUS | NOT;
noArrayLit: INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL | structLit | IDENTIFIER;
term: IDENTIFIER | INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL | LPAREN expr RPAREN;
intLitOrConstant: INT_LIT | IDENTIFIER;
baseType: INT | FLOAT | STRING | BOOLEAN | IDENTIFIER;
endOfStatement: SEMI;




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
DECLARE  : '=';
ASSIGN : ':=';
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
fragment OCT_LIT: '0' [oO] [0-7]+;
fragment HEX_LIT: '0' [xX] [0-9a-fA-F]+;

// Float
FLOAT_LIT: DEC_PART '.' DEC_PART? EXPONENT?;
fragment DEC_PART: '0' | [1-9][0-9]*;
fragment EXPONENT: [eE] [+-]? [0-9]+;

// String
STRING_LIT: '"' (ESC_SEQ | ~["\\\r\n])* '"';
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
        self.type = self.SEMI;
    else:
        self.skip();
};

UNCLOSE_STRING: '"' (ESC_SEQ | ~["\\\r\n])* ([\r\n] | EOF);
ILLEGAL_ESCAPE: '"' (ESC_SEQ | ~["\\\r\n])* '\\' ~[nrt"\\];
ERROR_CHAR: .;