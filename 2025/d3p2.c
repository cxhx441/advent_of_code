#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_LINES 1024
#define MAX_LINE_LEN 256
#define MAX_BATTERIES 12

long recurse(char *bank, int start, int place, int mbatteries){
    if (place == -1){
        return 0;
    }
    long max = -1;
    int maxi = -1;
    for ( int i = start; i < mbatteries - place; i++){
        if ( (bank[i] - '0') > max ){
            max = bank[i] - '0';
            maxi = i;
        }
    }

    long val = ( max * pow(10, place) ) + recurse(bank, maxi + 1, place - 1, mbatteries);
    return val;
}

int main(void){
    // const char *fname = "./puzzle_input/d3p1_example.txt";
    const char *fname = "./puzzle_input/d3p1_input.txt";
    FILE *fp = fopen(fname, "r");
    if (fp == NULL){
        perror("file not valid");
        return EXIT_FAILURE;
    }

    char banks[MAX_LINES][MAX_LINE_LEN];
    int count = 0;
    while ( count < MAX_LINES && fgets( banks[count], MAX_LINE_LEN, fp ) != NULL ){
        count++;
    }
    fclose(fp);

    int nbanks = count;

    /* do work */
    long result = 0;
    long val;
    int mbatteries = strlen(banks[0]) - 1; // ignore newline
    for ( int i = 0; i < nbanks; i++ ){
        val = recurse(banks[i], 0, MAX_BATTERIES - 1, mbatteries);
        printf("%lu\n", val);
        result += val;
    }

    printf("%lu\n", result);

    return EXIT_SUCCESS;
}
