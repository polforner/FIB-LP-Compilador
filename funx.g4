grammar funx;
root : func* expr? EOF;


func: 
    FUNC expr* bloque #DeclaracionFunc
    ;

bloque : '{' stat+ '}';

stat : expr #Expressions
    | ID '<-' expr #Assig
    | 'if' boolexpr bloque ('else' bloque)? #IfElse
    | 'while' boolexpr bloque #While
    ;

boolexpr : expr ('=' | '!=' | '<' | '>' | '<=' | '>=') expr;

expr : '(' expr ')' #Par
    | <assoc=right> expr '^' expr #Bin 
    | expr ('*'|'/'|'%') expr #Bin
    | expr ('+'|'-') expr #Bin
    | FUNC expr* #LlamadaFunc
    | NUM  #Valor
    | ID #Variable
    ;

FUNC: [A-Z][a-zA-Z0-9]*;
ID : [a-z][a-zA-Z0-9]*;  
NUM : [0-9]+ ;
MES : '+' ;
COMENT : '#'~[\n]*[\n]? -> skip ;
WS : [ \n]+ -> skip ;