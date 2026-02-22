#include <stdio.h>
#include <stdlib.h>

int mutex = 1, size = 0, max = 3;

void producer() {
    mutex = 0;
    size++;
    printf("\nProducer produces the item %d", size);
    mutex = 1;
}

void consumer() {
    mutex = 0;
    printf("\nConsumer consumes item %d", size);
    size--;
    mutex = 1;
}

int main() {
    int n;

    printf("\n1.PRODUCER\n2.CONSUMER\n3.EXIT\n");
    while (1) {
        printf("\nEnter your choice: ");
        scanf("%d", &n);
        switch (n) {
        case 1:
            if ((mutex == 1) && (size != max))
                producer();
            else
                printf("\nBUFFER IS FULL!");
            break;
        case 2:
            if ((mutex == 1) && (size != 0))
                consumer();
            else
                printf("\nBUFFER IS EMPTY!");
            break;
        case 3:
            exit(0);
            break;
        }
    }
    return 0;
}
