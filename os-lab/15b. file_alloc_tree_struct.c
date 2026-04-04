#include <stdio.h>
struct record {
    char empname[20];
    int age;
    float salary;
    long next; // pointer to next record
};
typedef struct record person;

int main() {
    person employee;
    FILE *fp;
    int i, n;
    long pos;
    printf("Linked File Organization Program\n");
    printf("How many records: ");
    scanf("%d", &n);
    fp = fopen("people.dat", "wb");
    for (i = 0; i < n; i++) {
        printf("Enter employee %d (Name Age Salary): ", i + 1);
        scanf("%s%d%f", employee.empname, &employee.age, &employee.salary);

        if (i == n - 1)
            employee.next = -1; // last record
        else
            employee.next = (i + 1) * sizeof(employee);

        fwrite(&employee, sizeof(employee), 1, fp);
    }
    fclose(fp);
    printf("\nRecords stored using linked organization.\n");
    fp = fopen("people.dat", "rb");

    pos = 0;
    printf("\nReading records using links:\n\n");

    while (pos != -1) {
        fseek(fp, pos, SEEK_SET);
        fread(&employee, sizeof(employee), 1, fp);

        printf("Name: %s\n", employee.empname);
        printf("Age: %d\n", employee.age);
        printf("Salary: %.2f\n\n", employee.salary);
        pos = employee.next;
    }
    fclose(fp);
    return 0;
}
