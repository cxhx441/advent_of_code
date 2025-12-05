#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ROWS 256
#define MAX_COLS 256

typedef struct {
    int di;
    int dj;
} Offset;

Offset neighbors[] = {
    {0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, 1}, {1, -1}, {-1, -1}, {-1, 1}
};

int m;
int n;
char *room[MAX_ROWS];

int count_adj_rolls(int i, int j){
    int ni;
    int nj;
    int nrolls = 0;
    for (int k = 0; k < 8; k++) {
        ni = i + neighbors[k].di;
        nj = j + neighbors[k].dj;
        if ( ni < 0 || ni >= m || nj < 0 || nj >= n  ){
            continue;
        }
        if ( room[ni][nj] == '@' ){
            nrolls++;
        }
    }
    if (nrolls < 4) {
        return 1;
    }
    return 0;
}

int main(void){
    // const char *fname = "./puzzle_input/d4p1_example.txt";
    const char *fname = "./puzzle_input/d4p1_input.txt";

    FILE *fp = fopen(fname, "r");
    if (fp == NULL){
        perror("file not opened correctly.");
        return EXIT_FAILURE;
    }

    char buf[MAX_COLS];
    int count = 0;
    while ( fgets(buf, sizeof (buf), fp) != NULL ){
        buf[strcspn(buf, "\n")] = '\0';
        room[count] = strdup(buf);
        // printf("%s\n", room[count]);
        count++;
    }

    m = count;
    n = strlen(room[0]);
    int result = 0;
    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            if ( room[i][j] == '@' ){
                result += count_adj_rolls(i, j);
            }
        }
    }
    printf("%d\n", result);
    return EXIT_SUCCESS;
}
