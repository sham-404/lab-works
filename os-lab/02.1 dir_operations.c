#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>

struct dirent *dptr;

int main(int argc, char *argv[]) {
    char buff[100];
    DIR *dirp;

    printf("\n\nENTER DIRECTORY NAME: ");
    scanf("%s", buff);

    if ((dirp = opendir(buff)) == NULL) { // reads absolute file path
        printf("The given directory does not exist\n");
        exit(1);
    }

    while ((dptr = readdir(dirp)) != NULL) {
        printf("%s\n", dptr->d_name);
    }

    closedir(dirp);
    return 0;
}
