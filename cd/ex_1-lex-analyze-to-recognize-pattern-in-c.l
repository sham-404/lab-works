/*
To compile:

flex exp1.l
gcc lex.yy.c -o exp1
./exp1

*/

%{
#include <stdio.h>
#include <string.h>

char symtab[100][50];
int symcount = 0;

int isKeyword(char *str) {
    char *keywords[] = {
        "int", "float", "if", "else", "while", "for", "do",
        "break", "continue", "return", "void", "char", "double",
        "long", "short", "switch", "case", "default", "goto", "sizeof"
    };
    int n = sizeof(keywords) / sizeof(keywords[0]);
    for (int i = 0; i < n; i++) {
        if (strcmp(str, keywords[i]) == 0) return 1;
    }
    return 0;
}

void insertSym(char *str) {
    for (int i = 0; i < symcount; i++) {
        if (strcmp(symtab[i], str) == 0) return;
    }
    strcpy(symtab[symcount++], str);
}
%}

%%
[0-9]+                  { printf("%s is a number\n", yytext); }
"=="|"!="|"<="|">="|"<"|">"|"+="|"-="|"*="|"/="|"%="|"="|"+"|"-"|"*"|"/"|"%" { printf("Operator: %s\n", yytext); }
[{}()\[\];,]            { printf("Special character: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]*  { 
                            if (isKeyword(yytext)) 
                                printf("%s is a keyword\n", yytext);
                            else { 
                                printf("%s is an identifier\n", yytext); 
                                insertSym(yytext); 
                            }
                        }
[ \t\n]+                ;
.                       { printf("Unknown token: %s\n", yytext); }
%%

int main() {
    printf("Enter input (Press Ctrl+D to stop and print Symbol Table):\n");
    yylex();
    printf("\nSymbol Table\n");
    for (int i = 0; i < symcount; i++) {
        printf("%d %s\n", i + 1, symtab[i]);
    }
    return 0;
}

int yywrap() {
    return 1;
}
