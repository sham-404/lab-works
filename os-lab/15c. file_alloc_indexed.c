#include <stdio.h>
#include <stdlib.h>
int f[50], i, j, k, inde[50], n, c, p;
int main() {
    printf("\nINDEXED FILE ALLOCATION TECHNIQUE\n");
    for (i = 0; i < 50; i++)
        f[i] = 0;

x:
    printf("\nEnter index block: ");
    scanf("%d", &p);

    if (f[p] == 0) {
        f[p] = 1;
        printf("Enter number of blocks needed: ");
        scanf("%d", &n);
    } else {
        printf("Block already allocated\n");
        goto x;
    }

    printf("Enter the blocks:\n");
    for (i = 0; i < n; i++)
        scanf("%d", &inde[i]);

    for (i = 0; i < n; i++) {
        if (f[inde[i]] == 1) {
            printf("Block already allocated\n");
            goto x;
        }
    }
    for (j = 0; j < n; j++)
        f[inde[j]] = 1;

    printf("\nAllocated");
    printf("\nFile Indexed\n");

    for (k = 0; k < n; k++)
        printf("\n%d -> %d : %d", p, inde[k], f[inde[k]]);

    printf("\n\nEnter 1 to enter more files and 0 to exit: ");
    scanf("%d", &c);

    if (c == 1)
        goto x;
    else
        exit(0);

    return 0;
}
