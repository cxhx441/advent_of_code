#include <stdio.h>
#include <stdlib.h>

int main(void){
    // const char* fname = "./puzzle_input/d3p1_ex.txt";
    const char* fname = "./puzzle_input/d3p1.txt";

    FILE* fp = fopen(fname, "r");
    if (!fp){
        return EXIT_FAILURE;
    }
    int c = 0;
    int min_y = 0;
    int max_y = 0;
    int min_x = 0;
    int max_x = 0;
    int x = 0;
    int y = 0;
    while ( (c = fgetc(fp)) != EOF ){
        if ( c == 'v' )
            y++;
        else if ( c == '^' )
            y--;
        else if ( c == '>' )
            x++;
        else if ( c == '<' )
            x--;

        if ( y > max_y )
            max_y = y;
        else if ( y < min_y )
            min_y = y;

        if ( x > max_x )
            max_x = x;
        else if ( x < min_x )
            min_x = x;
    }

    int m = max_y - min_y + 1;
    int n = max_x - min_x + 1;
    int** grid = malloc(m * sizeof (int*));
    for (int i = 0; i < m; i++){
        grid[i] = malloc(n * sizeof (int));
        for (int j = 0; j < n; j++){
            grid[i][j] = 0;
        }
    }

    rewind(fp);
    y = -min_y;
    x = -min_x;
    grid[y][x]++;
    while ( (c = fgetc(fp)) != EOF ){
        if ( c == 'v' )
            y++;
        else if ( c == '^' )
            y--;
        else if ( c == '>' )
            x++;
        else if ( c == '<' )
            x--;
        grid[y][x]++;
    }

    int unique = 0;
    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            if (grid[i][j] > 0){
                unique++;
            }
        }
    }
    fclose(fp);
    for (int i = 0; i < n; i++){
        free(grid[i]);
    }
    free(grid);

    printf("Result: %d\n", unique);
}
