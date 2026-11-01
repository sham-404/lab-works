/*
To compile:

yacc -d ex_3a.y
flex ex_3a.l
gcc lex.yy.c y.tab.c -o ex_3a
./ex_3a

*/

%{
#include <stdio.h>
#include <stdlib.h>

int yylex(void);
int yyerror(const char *s);
%}

%token NUMBER ID
%left '+' '-'
%left '*' '/'
%right '='

%%
expr
    : expr '+' expr
    | expr '-' expr
    | expr '*' expr
    | expr '/' expr
    | ID '=' expr
    | NUMBER
    | ID
    ;
%%

int main() {
    printf("Enter an expression (Ctrl+D to finish):\n");
    if (yyparse() == 0) {
        printf("Valid Expression\n");
    }
    return 0;
}

int yyerror(const char *s) {
    printf("Invalid Expression\n");
    return 0;
}
