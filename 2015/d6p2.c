#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define EXAMPLE false
#define MAXN 1000

int matrix[MAXN][MAXN] = {0};

void turnon(int x0, int y0, int x1, int y1){
    for (int i = y0; i <= y1; i++){
        for (int j = x0; j <= x1; j++){
            matrix[i][j] += 1;
        }
    }
}

void turnoff(int x0, int y0, int x1, int y1){
    for (int i = y0; i <= y1; i++){
        for (int j = x0; j <= x1; j++){
            matrix[i][j] -= 1;
            if (matrix[i][j] < 0) matrix[i][j] = 0;
        }
    }
}

void toggle(int x0, int y0, int x1, int y1){
    for (int i = y0; i <= y1; i++){
        for (int j = x0; j <= x1; j++){
            matrix[i][j] += 2;
        }
    }
}

int count(){
    int n = 0;
    for (int i = 0; i < MAXN; i++){
        for (int j = 0; j < MAXN; j++){
            n += matrix[i][j];
        }
    }
    return n;
}

int main(void){
    char* fname;
    if ( EXAMPLE == true )
        fname = "./puzzle_input/d6_ex.txt";
    else
        fname = "./puzzle_input/d6.txt";

    FILE* fp = fopen(fname, "r");
    if (!fp){
        perror("Error opening file.\n");
        return EXIT_FAILURE;
    }

    char *line = NULL;
    size_t linecap = 0;
    ssize_t linelen;
    int x0, y0, x1, y1;
    // char* s0, s1;
    while ( (linelen = getline(&line, &linecap, fp)) > 0 ){
        line[strcspn(line, "\n")] = '\0';
        if ( strncmp(line, "turn on", 7) == 0 ){
            sscanf(line, "%*s %*s %d,%d %*s %d,%d", &x0, &y0, &x1, &y1);
            turnon(x0, y0, x1, y1);
        }
        else if ( strncmp(line, "turn off", 8) == 0 ){
            sscanf(line, "%*s %*s %d,%d %*s %d,%d", &x0, &y0, &x1, &y1);
            turnoff(x0, y0, x1, y1);
        }
        else if ( strncmp(line, "toggle", 6) == 0 ){
            sscanf(line, "%*s %d,%d %*s %d,%d", &x0, &y0, &x1, &y1);
            toggle(x0, y0, x1, y1);
        }
        else{
            // break;
            perror("Line read incorrectly.\n");
            return EXIT_FAILURE;
        }
    }

    printf("result: %d\n", count());
    return EXIT_SUCCESS;
}
