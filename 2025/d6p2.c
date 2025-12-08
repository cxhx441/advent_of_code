#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// #define FNAME "./puzzle_input/d6p1_input.txt"
// #define MAX_ROWS 5
#define MAX_PROBLEMS 4096
#define FNAME "./puzzle_input/d6p1_example.txt"
#define MAX_ROWS 4

char *rows[MAX_ROWS];

int all_blank(int i){
    char cur;
    for (int row = 0; row < MAX_ROWS; row++ ) {
        cur = rows[row][i];
        if ( cur != ' ' && cur != '\0')
            return 0;
    }
    return 1;
}

int build_num(int i){
    int cur = 0;
    for (int row = 0; row < MAX_ROWS - 1; row++ ) {
        if ( rows[row][i] == ' ' || rows[row][i] == '\0'){
            continue;
        }
        cur *= 10;
        cur += rows[row][i] - '0';
    }
    return cur;
}

int main(void){
    char *fname = FNAME;

    FILE *fp = fopen(fname, "r");
    if ( fp == NULL ){
        perror("fopen error...");
        return EXIT_FAILURE;
    }

    /* process input */
    int n = 0;
    size_t len;
    size_t line_len;
    for (int i = 0; i < MAX_ROWS; i++){
        rows[i] = NULL;
        len = 0;
        if ( (line_len = getline(&rows[i], &len, fp)) < 0 ) {
            perror("getline failed");
            return EXIT_FAILURE;
        }

        if ( rows[i][line_len-1] == '\n' ) {
            rows[i][line_len-1] = '\0';
            line_len--;
        }

        if ( line_len > n )
            n = line_len;

    }
    fclose(fp);

    int new = 1;
    long cur = 0;
    char operator;
    long result = 0;
    for ( int i = 0; i < n; i++ ){
        if ( all_blank(i) == 1 ){
            new = 1;
            continue;
        }

        if ( new == 1 ) {
            operator = rows[MAX_ROWS - 1][i];
            new = 0;
            result += cur;
            if ( operator == '*' )
                cur = 1;
            else if ( operator == '+' )
                cur = 0;
        }

        int num = build_num(i);
        if ( operator == '*' )
            cur *= num;
        else if ( operator == '+' )
            cur += num;

    }
    result += cur;

    for (int i = 0; i < MAX_ROWS; i++){
        free(rows[i]);
    }
    printf("%lu\n", result);
    return EXIT_SUCCESS;
}
