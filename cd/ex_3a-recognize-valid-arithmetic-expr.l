/*
To compile:

yacc -d ex_3a.y
flex ex_3a.l
gcc lex.yy.c y.tab.c -o ex_3a
./ex_3a

*/

%{
#include "y.tab.h"
%}

%%
[0-9]+                  { return NUMBER; }
[a-zA-Z_][a-zA-Z0-9_]*  { return ID; }
"+"|"-"|"*"|"/"|"="     { return yytext[0]; }
[ \t\n]+                ;
.                       { return yytext[0]; }
%%

int yywrap() {
    return 1;
}
