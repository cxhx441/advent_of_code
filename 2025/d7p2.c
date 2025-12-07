#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MIN_CAPACITY 4
// #define FNAME "./puzzle_input/d7p1_input.txt"
#define FNAME "./puzzle_input/d7p1_example.txt"

int main(void){
    char *fname = FNAME;

    FILE *fp = fopen(fname, "r");
    if ( fp == NULL ){
        perror("fopen error...");
        return EXIT_FAILURE;
    }

    size_t capacity = MIN_CAPACITY;
    char **grid = malloc( capacity * sizeof (char*) );

    /* process input */
    size_t nread;
    char *line = NULL;
    int count = 0;
    while ( getline(&line, &nread, fp) != -1 ) {
        /* NEED TO GROW IF EXCEEDS CAPACITY */
        line[strcspn(line, "\n")] = '\0';
        if ( count == capacity ){
            capacity *= 2;
            grid = realloc(grid, capacity * sizeof (char*));
        }

        grid[count] = strdup(line);
        count++;
    }


    int m = count;
    int n = strlen(grid[0]);

    long **grid_count = malloc(m * sizeof (long));
    if (grid_count == NULL){
        perror("error on malloc");
        return EXIT_FAILURE;
    }
    for (int i=0; i < m;i++){
        grid_count[i] = malloc(n * sizeof(long));
        if (grid_count[i] == NULL){
            for ( int j = 0; j < i; j++ ){
                free(grid_count[i]);
            }
            free(grid_count);
            perror("error on malloc");
            return EXIT_FAILURE;
        }
    }

    for (int j = 0; j < n; j++){
        if (grid[0][j] == 'S'){
            grid[1][j] = '|';
            grid_count[1][j] += 1;
        }
    }
    printf("%s\n", grid[0]);
    printf("%s\n", grid[1]);
    for (int i = 2; i < m; i++){
        for (int j = 0; j < n; j++){
            if ( grid[i-1][j] == '|' ){
                if (grid[i][j] != '^'){
                    grid[i][j] = '|';
                    grid_count[i][j] += grid_count[i-1][j];
                }
                else if (grid[i][j] == '^'){
                    // nsplits++;
                    if ( j - 1 >= 0 && grid[i][j-1] != '^'){
                        grid[i][j-1] = '|';
                        grid_count[i][j-1] += grid_count[i-1][j];
                    }
                    if ( j + 1 < n && grid[i][j+1] != '^'){
                        grid[i][j+1] = '|';
                        grid_count[i][j+1] += grid_count[i-1][j];
                    }
                }

            }
        }
        printf("%s\n", grid[i]);
    }

    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            if ( grid_count[i][j] > 0){
                printf("%lX", grid_count[i][j]);
            }
            else {
                printf("%c", grid[i][j]);
            }
        }
        printf("\n");
    }

    long result = 0;
    for (int i = 0; i < n; i++){
        result += grid_count[m-1][i];
    }
    printf("%lu\n", result);
    return EXIT_SUCCESS;
}
