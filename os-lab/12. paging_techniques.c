#include <stdio.h>

int main() {
    int page_table[10];
    int logical_address, page_number, offset;
    int page_size, frame_number, physical_address;
    int n, i;

    printf("Enter the number of pages: ");
    scanf("%d", &n);
    printf("Enter the page table (frame numbers):\n");

    for (i = 0; i < n; i++) {
        printf("Page %d -> Frame: ", i);
        scanf("%d", &page_table[i]);
    }

    printf("Enter the page size: ");
    scanf("%d", &page_size);
    printf("Enter the logical address: ");
    scanf("%d", &logical_address);

    page_number = logical_address / page_size;
    offset = logical_address % page_size;

    if (page_number >= n) {
        printf("Invalid Page Number\n");
    } else {
        frame_number = page_table[page_number];
        physical_address = (frame_number * page_size) + offset;
        printf("\nPage Number: %d\n", page_number);
        printf("Offset: %d\n", offset);
        printf("Frame Number: %d\n", frame_number);
        printf("Physical Address: %d\n", physical_address);
    }

    return 0;
}
