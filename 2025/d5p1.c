#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_RANGES 256
#define MAX_IDS 2048

typedef struct {
    long lower;
    long upper;
} Range;

int main(void){
    char *const fname = "./puzzle_input/d5p1_example.txt";
    // char *const fname = "./puzzle_input/d5p1_input.txt";
    FILE *fp = fopen(fname, "r");
    if ( fp == NULL ){
        perror("fopen error...");
        return EXIT_FAILURE;
    }
    /* process input */
    char buf[64];
    Range ranges[MAX_RANGES];
    long ids[MAX_IDS];
    int nranges, nids;
    nranges = nids = 0;
    // first get ranges
    while ( strcmp( fgets(buf, sizeof (buf), fp), "\n") ){
        long a, b;
        sscanf(buf, "%lu-%lu", &a, &b);
        ranges[nranges].lower = a;
        ranges[nranges].upper = b;
        nranges++;
    }
    // then get item IDs
    while ( fgets(buf, sizeof (buf), fp) != NULL ){
        long a;
        sscanf(buf, "%lu", &a);
        ids[nids] = a;
        nids++;
    }
    fclose(fp);

    /* do work */
    // for ( int i = 0; i < nranges; i++ ){
    //     printf("%lu-%lu\n", ranges[i].lower, ranges[i].upper);
    // }
    // printf("\n");
    // for ( int i = 0; i < nids; i++ ){
    //     printf("%lu\n", ids[i]);
    // }
    long nfresh = 0;
    for ( int i = 0; i < nids; i++ ){
        for ( int j = 0; j < nranges; j++ ){
            if ( ids[i] >= ranges[j].lower && ids[i] <= ranges[j].upper ){
                nfresh++;
                break;
            }
        }
    }
    printf("\nnum fresh ids: %lu\n", nfresh);

    return EXIT_SUCCESS;
}
