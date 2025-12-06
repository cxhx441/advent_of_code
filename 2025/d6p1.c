#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_PROBLEMS 4096
// #define FNAME "./puzzle_input/d6p1_input.txt"
// #define MAX_ROWS 4
#define FNAME "./puzzle_input/d6p1_example.txt"
#define MAX_ROWS 3


int main(void){
    char *fname = FNAME;

    FILE *fp = fopen(fname, "r");
    if ( fp == NULL ){
        perror("fopen error...");
        return EXIT_FAILURE;
    }

    /* process input */
    int problems[MAX_ROWS][MAX_PROBLEMS];
    char buf[MAX_PROBLEMS];
    int ncols;
    char *num;
    for (int i = 0; i < MAX_ROWS; i++){
        ncols = 0;
        fgets(buf, sizeof (buf), fp);
        buf[strcspn(buf, "\n")] = '\0';
        num = strtok(buf, " ");
        while ( num != NULL ){
            problems[i][ncols] = atoi(num);
            ncols++;
            num = strtok(NULL, " ");
        }
    }

    char operators[MAX_PROBLEMS];
    char *operator;
    fgets(buf, sizeof (buf), fp);
    buf[strcspn(buf, "\n")] = '\0';
    operator = strtok(buf, " ");
    int i = 0;
    while ( operator != NULL ){
        operators[i] = operator[0];
        i++;
        operator = strtok(NULL, " ");
    }
    fclose(fp);

    long result = 0;
    long cur;
    for (int j = 0; j < ncols; j++){
        if (operators[j] == '+')
            cur = 0;
        else if (operators[j] == '*')
            cur = 1;

        for (int i = 0; i < MAX_ROWS; i++){
            if (operators[j] == '+'){
                cur += problems[i][j];
            }
            else if (operators[j] == '*'){
                cur *= problems[i][j];
            }
        }
        result += cur;
    }

    printf("%lu\n", result);
    return EXIT_SUCCESS;
}
