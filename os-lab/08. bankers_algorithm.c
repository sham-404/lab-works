#include <stdio.h>

int max[100][100], alloc[100][100], avail[100];
int n, r;

void input();
void show();
void cal();

int main() {
    printf("********** Banker's Algo ************\n");
    input();
    show();
    cal();
    return 0;
}

void input() {
    int i, j;

    printf("Enter the no of Processes\t");
    scanf("%d", &n);

    printf("Enter the no of resources instances\t");
    scanf("%d", &r);

    printf("Enter the Max Matrix\n");
    for (i = 0; i < n; i++)
        for (j = 0; j < r; j++)
            scanf("%d", &max[i][j]);

    printf("Enter the Allocation Matrix\n");
    for (i = 0; i < n; i++)
        for (j = 0; j < r; j++)
            scanf("%d", &alloc[i][j]);

    printf("Enter the available Resources\n");
    for (j = 0; j < r; j++)
        scanf("%d", &avail[j]);
}

void show() {
    int i, j;

    printf("Process\t Allocation\t Max\t Available\t");
    for (i = 0; i < n; i++) {
        printf("\nP%d\t ", i + 1);

        for (j = 0; j < r; j++)
            printf("%d ", alloc[i][j]);

        printf("\t");

        for (j = 0; j < r; j++)
            printf("%d ", max[i][j]);

        printf("\t");

        if (i == 0)
            for (j = 0; j < r; j++)
                printf("%d ", avail[j]);
    }
}

void cal() {
    int finish[100] = {0};
    int need[100][100];
    int i, j, k, flag, count = 0;

    // Calculate Need matrix
    for (i = 0; i < n; i++)
        for (j = 0; j < r; j++)
            need[i][j] = max[i][j] - alloc[i][j];

    printf("\n");

    do {
        flag = 0;

        for (i = 0; i < n; i++) {
            if (!finish[i]) {

                int possible = 1;

                for (j = 0; j < r; j++) {
                    if (need[i][j] > avail[j]) {
                        possible = 0;
                        break;
                    }
                }

                if (possible) {
                    for (k = 0; k < r; k++)
                        avail[k] += alloc[i][k];

                    finish[i] = 1;
                    printf("P%d -> ", i + 1);
                    flag = 1;
                    count++;
                }
            }
        }
    } while (flag);

    for (i = 0; i < n; i++)
        if (!finish[i])
            printf("P%d->", i + 1);

    if (count == n)
        printf("\n The system is in safe state");
    else {
        printf("\n Process are in dead lock");
        printf("\n System is in unsafe state");
    }
}
// https://wormhole.app/eE5jjo#eSOkgKq9ntNlb9SqGYj8Rw
// https://wormhole.app/YZRmE9#XcaLDO4x7bgSAdmniXDfmw
