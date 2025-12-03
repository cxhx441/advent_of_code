#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINES 1024
#define MAX_LINE_LEN 256

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
    int result = 0;
    int mbatteries = strlen(banks[0]) - 1; // ignore newline
    int max;
    int tens_place;
    int ones_place;
    for ( int i = 0; i < nbanks; i++ ){
        max = 0;
        for ( int j = 0; j < mbatteries - 1; j++){
            if ( (banks[i][j] - '0') > max ){
                max = banks[i][j] - '0';
                tens_place = j;
            }
        }

        max = 0;
        for ( int j = tens_place + 1; j < mbatteries; j++){
            if ( (banks[i][j] - '0') > max ){
                max = banks[i][j] - '0';
                ones_place = j;
            }
        }
        int val = ( banks[i][tens_place] - '0' ) * 10 + ( banks[i][ones_place] - '0');
        printf("%d\n", val);
        result += val;
    }

    printf("%d\n", result);

    return EXIT_SUCCESS;
}
