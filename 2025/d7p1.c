#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MIN_CAPACITY 4
#define FNAME "./puzzle_input/d7p1_input.txt"
// #define FNAME "./puzzle_input/d7p1_example.txt"


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
    free(line);
    fclose(fp);


    // for (int i = 0; i < count; i++){
    //     printf("%s\n", grid[i]);
    // }
    int m = count;
    int n = strlen(grid[0]);
    for (int j = 0; j < n; j++){
        if (grid[0][j] == 'S')
            grid[1][j] = '|';
    }
    printf("%s\n", grid[0]);
    printf("%s\n", grid[1]);
    int nsplits = 0;
    for (int i = 2; i < m; i++){
        for (int j = 0; j < n; j++){
            if ( grid[i-1][j] == '|' ){
                if (grid[i][j] != '^'){
                    grid[i][j] = '|';
                }
                else if (grid[i][j] == '^'){
                    nsplits++;
                    if ( j - 1 >= 0 && grid[i][j-1] != '^'){
                        grid[i][j-1] = '|';
                    }
                    if ( j + 1 < n && grid[i][j+1] != '^'){
                        grid[i][j+1] = '|';
                    }
                }

            }
        }
        printf("%s\n", grid[i]);
    }
    printf("%d\n", nsplits);
    for (int i = 0; i < m; i++){
        free(grid[i]);
    }
    free(grid);
    // long result = 0;
    // printf("%lu\n", result);
    return EXIT_SUCCESS;
}
