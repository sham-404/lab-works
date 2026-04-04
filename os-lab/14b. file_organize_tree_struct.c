#include <stdio.h>
#include <stdlib.h>
struct tree {
    char name[20];
    int child_count;
    struct tree *child[5];
};
typedef struct tree node;
void create(node *root) {
    int i;
    printf("Enter number of children for %s: ", root->name);

    scanf("%d", &root->child_count);
    for (i = 0; i < root->child_count; i++) {
        root->child[i] = (node *)malloc(sizeof(node));
        printf("Enter name of child %d of %s: ", i + 1, root->name);
        scanf("%s", root->child[i]->name);
        create(root->child[i]);
    }
}
void display(node *root, int level) {
    int i;
    for (i = 0; i < level; i++)
        printf("   ");

    printf("|-- %s\n", root->name);

    for (i = 0; i < root->child_count; i++)
        display(root->child[i], level + 1);
}

int main() {
    node *root;

    root = (node *)malloc(sizeof(node));

    printf("\n===== Tree Structured Directory =====\n\n");

    printf("Enter root directory name: ");
    scanf("%s", root->name);

    create(root);

    printf("\nDirectory Structure:\n");
    display(root, 0);

    return 0;
}
