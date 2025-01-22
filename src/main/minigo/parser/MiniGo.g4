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

program: (parserRuleSpec)+ EOF;

// PARSER RULES

tYPE: INTERGER | FLOAT | STRING | BOOLEAN;
// type: ;
parserRuleSpec: decl | statement;
// Boolean expressions
decl: varDecl | funcDecl | typeDecl | constDecl;
varDecl: VAR IDENTIFIER arrayDims? (tYPE | tYPE? (ASSIGNOP expression)) SEMI;
funcDecl: FUNC IDENTIFIER LP (funcParams)? RP tYPE? block SEMI?;
typeDecl: TYPE IDENTIFIER typeDefinition;
constDecl: CONST IDENTIFIER ASSIGNOP expression SEMI;

// Type definitions
typeDefinition: structDefinition | interfaceDefinition;
structDefinition: STRUCT LB structFields RB;
structFields: (IDENTIFIER tYPE SEMI)+;

// Interface definitions
interfaceDefinition: INTERFACE LB interfaceFields RB;
interfaceFields: IDENTIFIER listParams tYPE SEMI;
listParams: LP (listIdentifier tYPE)* RP;
listIdentifier: IDENTIFIER (COMMA IDENTIFIER)*;


// Function Params
funcParams: funcParam (COMMA funcParam)*;
funcParam: IDENTIFIER tYPE;

// expressions
expression: expression OROP  term
          | expression ANDOP term
          | expression (EQUALOP | NOTEQUALOP | LESSOP | LESSEQUALOP | GREATEROP | GREATEREQUALOP) term
          | expression (ADDOP | SUBOP) term
          | expression (MULOP | DIVOP | MODOP) term
          | (NOTOP | SUBOP) term
          | term;
term: IDENTIFIER (arrayDims | DOT IDENTIFIER)?
    | INTLIT
    | FLOATLIT
    | STRINGLIT
    | LP expression RP;



// Statements
statement: (assignStatement
         | ifStatement
         | forStatement
         | breakStatement
         | continueStatement
         | callStatement
         | arrayLiteral
         | varDecl
         | constDecl) {print($text)};




// Array Literals
arrayLiteral: IDENTIFIER SHORTASSIGNOP (arrayDims) (INTERFACE | FLOAT | STRING | BOOLEAN) arraysBlock;
arraysBlock: LB arraysBlock (COMMA arraysBlock)* RB | LB expression (COMMA expression)* RB;

// Assign Statement
assignStatement: IDENTIFIER (arrayDims | DOT IDENTIFIER)? assignmentOperator expression SEMI;
assignmentOperator: SHORTASSIGNOP | INCASSIGNOP | DECASSIGNOP | MULASSIGNOP | DIVASSIGNOP | MODASSIGNOP;

// If Statement
ifStatement: IF LP expression RP block
             (ELSE IF LP expression RP block)*
             (ELSE block)?;
// For Statement
forStatement: FOR ( forLoop | forIteration) block;

forLoop: forCondition
         | initilization SEMI forCondition SEMI forUpdate;

initilization: IDENTIFIER SHORTASSIGNOP expression;
forCondition: expression;
forUpdate: IDENTIFIER assignmentOperator expression;

forIteration: (IDENTIFIER | BLANK) COMMA IDENTIFIER SHORTASSIGNOP RANGE IDENTIFIER;



// Break Statement
breakStatement: BREAK SEMI;

// Continue Statement
continueStatement: CONTINUE SEMI;

// Call Statement
callStatement: IDENTIFIER (DOT IDENTIFIER)? LP (expression (COMMA expression)*)? RP SEMI;

block: LB (statement)* RB;
arrayDims: (LSB INTLIT RSB)+;


// TOKEN DEFINITION
//KEYWORDS DEFINITION
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
INTERGER: 'int';
FLOAT: 'float';
STRING: 'string';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
BOOLEANLIT: 'true' | 'false';
NILLIT: 'nil';

// IDENTIFIER DEFINITION
IDENTIFIER: [a-zA-Z_] [a-zA-Z_0-9]*;

// OPERATORS DEFINITION
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
MODOP: '%';
EQUALOP: '==';
NOTEQUALOP: '!=';
LESSOP: '<';
LESSEQUALOP: '<=';
GREATEROP: '>';
GREATEREQUALOP: '>=';
ANDOP: '&&';
OROP: '||';
NOTOP: '!';
ASSIGNOP: '=';
SHORTASSIGNOP: ':=';
INCASSIGNOP: '+=';
DECASSIGNOP: '-=';
MULASSIGNOP: '*=';
DIVASSIGNOP: '/=';
MODASSIGNOP: '%=';
DOT: '.';
COLON: ':';
BLANK: '_';

// SEPARATORS DEFINITION
LP: '(';
RP: ')';
LB: '{';
RB: '}';
LSB: '[';
RSB: ']';
COMMA: ',';
SEMI: ';';

// LITERALS DEFINITION
INTLIT: ZERO | DEC | HEX | OCT | BIN;
fragment ZERO: '0'; 
fragment DEC: [1-9] [0-9]*;
fragment HEX: '0' [xX] [0-9a-fA-F]*;
fragment OCT: '0' [o0] [0-7]*;
fragment BIN: '0' [bB] [01]*;

// FLOATLITERALS DEFINITION
FLOATLIT: (INT FRAC FIC| INT FRAC | INT FIC);
fragment INT: [0-9]+;
fragment FRAC: '.' [0-9]*;
fragment FIC: [eE][+-]? [0-9]+; 

// STRING LITERALS DEFINITION
STRINGLIT: '"' (ESCAPE | ~["\\])* '"';
fragment ESCAPE: '\\' [ntr"\\];

// Skip Rules
NL: '\n' -> skip; //skip newlines
WS: [ \t\r]+ -> skip; // skip spaces, tabs
COMMENT: ('//' ~[\r\n]*) -> skip;
MULTI_COMMENT: NESTED_COMMENT -> skip;
fragment NESTED_COMMENT: '/*' (NESTED_COMMENT | ~'*' | '*' ~'/')* '*/';



// Error Rules
ERROR_CHAR: .;
ILLEGAL_ESCAPE: .;
UNCLOSE_STRING: .;