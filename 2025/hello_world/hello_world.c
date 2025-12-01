#include <stdio.h>

int main(int argc, char *argv[]) {
    if (argc == 1) {
        printf("argv[0] == %s\n", argv[0]);
    }
    else if (argc == 2) {
        printf("argv[1] == %s\n", argv[1]);
    }
    printf("Hello,");
    printf(" World!");
    printf("\n");
    return 0;
}
