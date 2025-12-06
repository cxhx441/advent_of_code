#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_RANGES 256
#define MAX_IDS 2048

typedef struct {
    long lower;
    long upper;
} Range;

int rangecmp(const void *a, const void *b){
    Range *ra = (Range*) a;
    Range *rb = (Range*) b;

    if ( ra->lower < rb->lower )
        return -1;
    else if (ra->lower > rb->lower)
        return 1;
    else
        return 0;
}

int main(void){
    // char *const fname = "./puzzle_input/d5p1_example2.txt";
    char *const fname = "./puzzle_input/d5p1_input.txt";
    FILE *fp = fopen(fname, "r");
    if ( fp == NULL ){
        perror("fopen error...");
        return EXIT_FAILURE;
    }
    /* process input */
    char buf[64];
    Range ranges[MAX_RANGES];
    int nranges = 0;
    // first get ranges
    while ( strcmp( fgets(buf, sizeof (buf), fp), "\n") ){
        long a, b;
        sscanf(buf, "%lu-%lu", &a, &b);
        ranges[nranges].lower = a;
        ranges[nranges].upper = b;
        nranges++;
    }
    fclose(fp);


    /* do work */
    // for ( int i = 0; i < nranges; i++ ){
    //     printf("%lu-%lu\n", ranges[i].lower, ranges[i].upper);
    // }

    // printf("\nafter sort\n");
    qsort(ranges, nranges, sizeof (Range), rangecmp);

    Range comp_ranges[MAX_RANGES];
    // comp_ranges[0].lower = ranges[0].lower;
    // comp_ranges[0].upper = ranges[0].upper;
    comp_ranges[0] = ranges[0];
    long ncompranges = 1;
    long pa, pb;
    long na, nb;
    for ( int i = 1; i < nranges; i++ ){
        pa = comp_ranges[ncompranges-1].lower;
        pb = comp_ranges[ncompranges-1].upper;
        na = ranges[i].lower;
        nb = ranges[i].upper;

        if ( pb >= nb )
            continue;
        else if ( na > pb ){ // fully above
            // comp_ranges[ncompranges].lower = ranges[i].lower;
            // comp_ranges[ncompranges].upper = ranges[i].upper;
            comp_ranges[ncompranges] = ranges[i];
            ncompranges++;
        }
        else if ( na <= pb ){
            comp_ranges[ncompranges-1].upper = nb;
        }
    }

    for ( int i = 0; i < nranges; i++ ){
        printf("%lu-%lu\n", ranges[i].lower, ranges[i].upper);
    }
    printf("\n");
    for ( int i = 0; i < ncompranges; i++ ){
        printf("%lu-%lu\n", comp_ranges[i].lower, comp_ranges[i].upper);
    }

    /* real work */
    long nfreshids = 0;
    for ( int i = 0; i < ncompranges; i++ ){
        nfreshids += comp_ranges[i].upper - comp_ranges[i].lower + 1;
    }

    // long diff_fresh = ranges[0].upper - ranges[0].lower + 1;
    // for ( int i = 1; i < nranges; i++ ){
    //     if ( ranges[i].lower > ranges[i-1].upper )
    //         diff_fresh += ranges[i].upper - ranges[i].lower + 1;
    //     else{
    //         diff_fresh += ranges[i].upper - ranges[i].lower + 1;
    //     }
    // }

    printf("\nnum fresh ids: %lu\n", nfreshids);
    // printf("\nnum difffresh ids: %lu\n", diff_fresh);

    return EXIT_SUCCESS;
}
