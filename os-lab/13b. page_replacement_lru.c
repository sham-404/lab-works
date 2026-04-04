#include <stdio.h>

int main() {
    int p[50], frame[20];
    int n, f, i, j, k = 0, count = 0;
    int found, lru_index, min;

    printf("Enter number of pages: ");
    scanf("%d", &n);

    printf("Enter the reference string:\n");
    for (i = 0; i < n; i++) {
        scanf("%d", &p[i]);
    }

    printf("Enter number of frames: ");
    scanf("%d", &f);

    for (i = 0; i < f; i++) {
        frame[i] = -1;
    }

    printf("\nFrame status:\n");

    for (i = 0; i < n; i++) {
        found = 0;

        for (j = 0; j < f; j++) {
            if (frame[j] == p[i]) {
                found = 1;
                break;
            }
        }

        if (!found) {
            count++;

            if (k < f) {
                frame[k] = p[i];
                k++;
            } else {
                min = 9999;

                for (j = 0; j < f; j++) {
                    int last_used = -1;

                    for (int m = i - 1; m >= 0; m--) {
                        if (frame[j] == p[m]) {
                            last_used = m;
                            break;
                        }
                    }

                    if (last_used < min) {
                        min = last_used;
                        lru_index = j;
                    }
                }

                frame[lru_index] = p[i];
            }
        }

        for (j = 0; j < f; j++) {
            if (frame[j] != -1)
                printf("\t%d", frame[j]);
            else
                printf("\t-");
        }
        printf("\n");
    }

    printf("\nTotal Page Faults = %d\n", count);

    return 0;
}
