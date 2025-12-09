#include <stdio.h>
#include <stdlib.h>

#define MIN_ROWS 4


typedef struct{
    int x;
    int y;
} Coordinate;

int in_set(Coordinate *rows, int n, Coordinate target){
    for (int i = 0; i < n; i++){
        if ( rows[i].x == target.x && rows[i].y == target.y )
            return 1;
    }
    return 0;
}

int between_points(Coordinate *rows, int n, Coordinate target ){
    int x0;
    int x1;
    int y0;
    int y1;
    for (int i = 1; i < n; i++){
        x0 = rows[i].x;
        x1 = rows[i-1].x;
        y0 = rows[i].y;
        y1 = rows[i-1].y;
        if ( x0 == x1 && x0 == target.x){
            if ( target.y >= y0 && target.y <= y1 )
                return 1;
            if ( target.y >= y1 && target.y <= y0 )
                return 1;
        }
        else if (y0 == y1 && y0 == target.y){
            if ( target.x >= x0 && target.x <= x1 )
                return 1;
            if ( target.x >= x1 && target.x <= x0 )
                return 1;
        }
    }

    x0 = rows[0].x;
    x1 = rows[n-1].x;
    y0 = rows[0].y;
    y1 = rows[n-1].y;
    if ( x0 == x1 && x0 == target.x){
        if ( target.y >= y0 && target.y <= y1 )
            return 1;
        if ( target.y >= y1 && target.y <= y0 )
            return 1;
    }
    else if (y0 == y1 && y0 == target.y){
        if ( target.x >= x0 && target.x <= x1 )
            return 1;
        if ( target.x >= x1 && target.x <= x0 )
            return 1;
    }
    return 0;
}

int main(void){
    const char* fname = "./puzzle_input/d9p1_example.txt";
    // const char* fname = "./puzzle_input/d9p1_input.txt";
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
            // // area is larger && both mirrored points are either red or between two red points
            if (area > largest_area){
                Coordinate mirrored1;
                Coordinate mirrored2;
                mirrored1.x = x2;
                mirrored1.y = y1;
                mirrored2.x = x1;
                mirrored2.y = y2;

                if (in_set(rows, n, mirrored1) == 0 ){
                    if ( between_points(rows, n, mirrored1) == 0){
                        if ( within_boundary(rows, n, mirrored1) == 1 )
                            break;
                    }
                }
                if (in_set(rows, n, mirrored2) == 0){
                    if (between_points(rows, n, mirrored2) == 0){
                        if ( within_boundary(rows, n, mirrored1) == 1 )
                            break;
                    }
                }
                largest_area = area;
                printf("%lu: %d, %d ,, %d, %d\n", largest_area, x1, y1, x2, y2);
            }
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
