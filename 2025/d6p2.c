#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FNAME "./puzzle_input/d6p1_input.txt"
#define MAX_ROWS 5
#define MAX_PROBLEMS 4096
// #define FNAME "./puzzle_input/d6p1_example.txt"
// #define MAX_ROWS 4

char input[MAX_ROWS][MAX_PROBLEMS];

int all_blank(int i){
    char cur;
    for (int row = 0; row < MAX_ROWS; row++ ) {
        cur = input[row][i];
        if ( cur != ' ' && cur != '\0')
            return 0;
    }
    return 1;
}

int build_num(int i){
    int cur = 0;
    for (int row = 0; row < MAX_ROWS - 1; row++ ) {
        if ( input[row][i] == ' ' || input[row][i] == '\0'){
            continue;
        }
        cur *= 10;
        cur += input[row][i] - '0';
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
    for (int i = 0; i < MAX_ROWS; i++){
        fgets(input[i], sizeof (input[i]), fp);
        input[i][strcspn(input[i], "\n")] = '\0';
        if (strlen(input[i]) > n){
            n = strlen(input[i]);
        }
    }

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
            operator = input[MAX_ROWS - 1][i];
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

    printf("%lu\n", result);
    return EXIT_SUCCESS;
}
