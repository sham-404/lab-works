#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int sno;
    char name[25];
    int m1, m2, m3;
} STD;
STD s;
void display(FILE *fp);
int search(FILE *fp, int sno_key);

int main() {
    int i, n, sno_key, opn;
    FILE *fp;
    printf("How many records? ");
    scanf("%d", &n);
    fp = fopen("stud.dat", "w+b");
    for (i = 0; i < n; i++) {
        printf("Enter student %d (sno Name M1 M2 M3): ", i + 1);
        scanf("%d %s %d %d %d", &s.sno, s.name, &s.m1, &s.m2, &s.m3);
        fwrite(&s, sizeof(s), 1, fp);
    }
    do {
        printf("\n1 - DISPLAY\n2 - SEARCH\n3 - EXIT\nYour option: ");
        scanf("%d", &opn);
        switch (opn) {
        case 1:
            printf("\nStudent Records in the file\n");
            display(fp);
            break;

        case 2:
            printf("Enter student number to search: ");
            scanf("%d", &sno_key);

            if (search(fp, sno_key)) {
                printf("Record Found!\n");
                printf("%d\t%s\t%d\t%d\t%d\n", s.sno, s.name, s.m1, s.m2, s.m3);
            } else {
                printf("Record %d not found\n", sno_key);
            }
            break;
        case 3:
            printf("Exiting program\n");
            break;
        default:
            printf("Invalid option\n");
        }
    } while (opn != 3);
    fclose(fp);
    return 0;
}
void display(FILE *fp) {
    rewind(fp);
    while (fread(&s, sizeof(s), 1, fp)) {
        printf("%d\t%s\t%d\t%d\t%d\n", s.sno, s.name, s.m1, s.m2, s.m3);
    }
}

int search(FILE *fp, int sno_key) {
    rewind(fp);

    while (fread(&s, sizeof(s), 1, fp)) {
        if (s.sno == sno_key)
            return 1;
    }

    return 0;
}
