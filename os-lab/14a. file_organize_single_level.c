#include <stdio.h>

int main() {
    int count, i;
    char fname[10][20];

    printf("\n===== Single Level Directory Structure =====\n\n");

    printf("Enter number of files: ");
    scanf("%d", &count);

    for (i = 0; i < count; i++) {
        printf("Enter file name %d: ", i + 1);
        scanf("%s", fname[i]);
    }

    printf("\nRoot Directory\n");

    for (i = 0; i < count; i++) {
        printf(" |-- %s\n", fname[i]);
    }

    return 0;
}
