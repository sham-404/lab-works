#include <stdio.h>
#include <stdlib.h>

struct rr {
    int pno;
    int burst_time;
    int btime;
    int completion_time;
};

int main() {
    int time_slice, n, finished_count = 0;
    struct rr *p_arr;

    printf("Round Robin scheduling...\n");
    printf("Enter no of processes: ");
    scanf("%d", &n);

    p_arr = (struct rr *)malloc(sizeof(struct rr) * n);

    printf("\nEnter the time slice: ");
    scanf("%d", &time_slice);

    for (int i = 0; i < n; i++) {
        printf("Process %d Burst Time: ", i + 1);
        scanf("%d", &p_arr[i].burst_time);
        p_arr[i].btime = p_arr[i].burst_time;
        p_arr[i].pno = i + 1;
        p_arr[i].completion_time = 0;
    }

    int current_time = 0;

    while (finished_count < n) {
        int done_in_this_pass = 0;
        for (int i = 0; i < n; i++) {
            if (p_arr[i].burst_time > 0) {
                int run_time = (p_arr[i].burst_time > time_slice)
                                   ? time_slice
                                   : p_arr[i].burst_time;

                printf("P%d [%d -> %d]\n", p_arr[i].pno, current_time,
                       current_time + run_time);

                current_time += run_time;
                p_arr[i].burst_time -= run_time;

                if (p_arr[i].burst_time == 0) {
                    p_arr[i].completion_time = current_time;
                    finished_count++;
                }
            }
        }
    }

    printf("\nProcess\tBurst \tTurnaround    \tWaiting\n");
    int total_wt = 0, total_tat = 0;

    for (int i = 0; i < n; i++) {
        int tat = p_arr[i].completion_time;
        int wt = tat - p_arr[i].btime; // WT = TAT - Burst

        total_tat += tat;
        total_wt += wt;

        printf("%d\t%d\t%d\t\t%d\n", p_arr[i].pno, p_arr[i].btime, tat, wt);
    }

    printf("\nTotal wait time: %d\n", total_wt);
    printf("Average waiting time: %f\n", (float)total_wt / n);
    printf("Total turnaround time: %d\n", total_tat);
    printf("Average turnaround time: %f\n", (float)total_tat / n);

    free(p_arr);
    return 0;
}
