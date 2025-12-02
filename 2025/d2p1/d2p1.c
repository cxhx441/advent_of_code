#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ITEMS 10000

int validation(long val){
    char str[20];
    sprintf(str, "%ld", val);
    size_t len = strlen(str);
    if (len % 2 != 0){
        return 0;
    }

    size_t half_len = len / 2;
    if (strncmp(str, str + half_len, half_len) == 0){
        return 1;
    }
    return 0;
}

typedef struct {
    long lower;
    long upper;
} Range;

int main(void) {
    // const char *fname = "../puzzle_input/d2p1_example.txt";
    const char *fname = "../puzzle_input/d2p1_input.txt";
    FILE *fp = fopen(fname, "r");
    if (!fp) {
        perror("error opening file.");
        return EXIT_FAILURE;
    }

    char buf[100000];
    Range ranges[MAX_ITEMS];
    int count = 0;

    if ( fgets(buf, sizeof (buf), fp) ) {
        char *token = strtok(buf, ",");
        while (token){
            long a;
            long b;
            if ( sscanf(token, "%lu-%lu", &a, &b) == 2) {
                ranges[count].lower = a;
                ranges[count].upper = b;
                count++;
            }
            token = strtok(NULL, ",");
        }
    }
    fclose(fp);

    long result = 0;
    for (int i=0; i < count; i++){
        printf("%lu to %lu\n", ranges[i].lower, ranges[i].upper);
        long cur = ranges[i].lower;
        while ( cur <= ranges[i].upper){
            if (validation(cur) == 1){
                result += cur;
            }
            cur++;
        }
    }
    printf("%lu\n", result);
    return 0;
}
