#include <stdio.h>

struct fcfs {
    int pid;
    int btime;
    int wtime;
    int ttime;
} p[10];

int main() {
    int i, n;
    int towtwtime = 0, totttime = 0;

    printf("\nFCFS scheduling...\n");
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        p[i].pid = i + 1;
        printf("Burst time of process %d: ", p[i].pid);
        scanf("%d", &p[i].btime);
    }

    p[0].wtime = 0;
    p[0].ttime = p[0].btime;
    towtwtime += p[0].wtime;
    totttime += p[0].ttime;

    for (i = 1; i < n; i++) {
        p[i].wtime = p[i - 1].wtime + p[i - 1].btime;
        p[i].ttime = p[i].wtime + p[i].btime;
        towtwtime += p[i].wtime;
        totttime += p[i].ttime;
    }

    printf("\nProcess\tBurst\tWaiting\tTurnaround\n");
    for (i = 0; i < n; i++) {
        printf("P%d\t%d\t%d\t%d\n", p[i].pid, p[i].btime, p[i].wtime,
               p[i].ttime);
    }

    printf("\nTotal waiting time: %d", towtwtime);
    printf("\nAverage waiting time: %.2f", (float)towtwtime / n);
    printf("\nTotal turnaround time: %d", totttime);
    printf("\nAverage turnaround time: %.2f\n", (float)totttime / n);

    return 0;
}
