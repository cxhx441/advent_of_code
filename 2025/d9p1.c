#include <stdio.h>
#include <stdlib.h>

#define MIN_ROWS 4


typedef struct{
    int x;
    int y;
} Coordinate;

int main(void){
    // const char* fname = "./puzzle_input/d9p1_example.txt";
    const char* fname = "./puzzle_input/d9p1_input.txt";
    FILE* fp = fopen(fname, "r");
    if (!fp){
        perror("file invalid.");
        return EXIT_FAILURE;
    }

    char *line = NULL;
    size_t len;
    int x, y;
    int capacity = MIN_ROWS;
    int n = 0;
    Coordinate *rows = malloc(sizeof(Coordinate) * capacity);
    while ( getline(&line, &len, fp ) > 0 ){
        sscanf(line, "%d,%d", &x, &y);

        if ( n == capacity ){
            capacity *= 2;
            rows = realloc(rows, sizeof(Coordinate) * capacity);
        }
        rows[n].x = x;
        rows[n].y = y;
        n++;
    }

    free(line);
    fclose(fp);
    // int minx, miny;
    // minx = miny = 1000000000;
    // for (int i = 0; i < n; i++){
    //     if ( rows[i].x < minx )
    //         minx = rows[i].x;
    //     if ( rows[i].y < miny )
    //         miny = rows[i].y;
    // }

    // for (int i = 0; i < n; i++){
    //     rows[i].x -= minx;
    //     rows[i].y -= miny;
    // }

    long largest_area = 0;
    for (int i = 0; i < n; i++){
        for (int j = i + 1; j < n; j++){
            int x1 = rows[i].x;
            int y1 = rows[i].y;
            int x2 = rows[j].x;
            int y2 = rows[j].y;
            int h = abs(y2 - y1) + 1;
            int w = abs(x2 - x1) + 1;

            long area = (long)w * (long)h;
            largest_area = area > largest_area ? area : largest_area;
        }
    }

    for (int i = 0; i < n; i++){
        printf("%d,%d\n", rows[i].x, rows[i].y);
    }
    printf("%lu\n", largest_area);
    free(rows);
    // printf("%lu\n", total_len);
    return EXIT_SUCCESS;
}
