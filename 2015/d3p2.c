#include <stdio.h>
#include <stdlib.h>

// const char* fname = "./puzzle_input/d3p1_ex.txt";
const char* fname = "./puzzle_input/d3p1.txt";

int santa_visited(){
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
            max_y++;
        else if ( c == '^' )
            min_y--;
        else if ( c == '>' )
            max_x++;
        else if ( c == '<' )
            min_x--;
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
        if ( (c = fgetc(fp)) == EOF )
            break;
    }
    // robo santa
    rewind(fp);
    c = fgetc(fp);
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
        if ( (c = fgetc(fp)) == EOF )
            break;
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

    return unique;
}

int main(void){
    int total = santa_visited();
    printf("Result: %d\n", total);

    return EXIT_SUCCESS;
}
