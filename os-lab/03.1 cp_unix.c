#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main(int a1gc, char *argv[]) {
    FILE *fp;
    char ch;
    int sc = 0;
    fp = fopen(argv[1], "r");

    if (fp == NULL)
        printf("unable to open a file %s", argv[1]);
    else {
        while ((ch = fgetc(fp)) != EOF) {
            if (ch == ' ')
                sc++;
        }

        printf("no of spaces %d", sc);
        printf("\n");
        fclose(fp);
    }
}
