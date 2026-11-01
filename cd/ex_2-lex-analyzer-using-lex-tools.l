/*
To compile:

flex ex_2.l
gcc lex.yy.c -o ex_2
./ex_2

*/

%{
#include <stdio.h>
#include <stdlib.h>
%}

IDENTIFIER          [a-zA-Z_][a-zA-Z0-9_]*
NUMBER              [0-9]+
WHITESPACE          [ \t\n]+
OPERATORS           "+"|"-"|"*"|"/"|"%"|"="|"=="|"!="|"<="|">="|"<"|">"|"+="|"-="|"*="|"/="|"%="
SPECIAL_CHARACTER   [{}()\[\];,]

%%
"if"                { printf("KEYWORD: if\n"); }
"else"              { printf("KEYWORD: else\n"); }
"while"             { printf("KEYWORD: while\n"); }
{IDENTIFIER}        { printf("IDENTIFIER: %s\n", yytext); }
{NUMBER}            { printf("NUMBER: %s\n", yytext); }
{OPERATORS}         { printf("OPERATOR: %s\n", yytext); }
{SPECIAL_CHARACTER} { printf("SPECIAL CHARACTER: %s\n", yytext); }
{WHITESPACE}        { /* Ignore whitespace */ }
.                   { printf("UNKNOWN CHARACTER: %s\n", yytext); }
%%

int main() {
    printf("Enter input (Press Ctrl+D to Exit):\n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
