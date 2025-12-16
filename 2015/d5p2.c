#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <regex.h>

// #define ENCODE_MAX ((25 * 113) + 25)
// int encode(const char c1, const char c2){
//     return ((c1 - 'a') * 113 ) + c2 - 'a';
// }

int first_seen[26][26] = {-1};

bool is_nice(const char* input){
    int n = strlen(input);

    for ( int i = 0; i < 26; i++){
        for ( int j = 0; j < 26; j++)
            first_seen[i][j] = -1;
    }

    bool double_letter = false;
    bool double_pair = false;
    for ( int i = 0; i < n; i++){
        if ( i > 1 && (input[i-2] == input[i]) )
            double_letter = true;
        if ( i > 0 ){
            int l = input[i-1] - 'a';
            int r = input[i] - 'a';
            if ( first_seen[l][r] == -1 )
                first_seen[l][r] = i-1;
            else if ( (i-1) - first_seen[l][r] >= 2 )
                double_pair = true;
        }
    }

    if (double_letter == false)
        printf("no double letter\n");
    if (double_pair == false)
        printf("no double pair\n");
    return double_letter && double_pair;
}

int main(void){
    // const char* fname = "./puzzle_input/d5.txt";
    const char* fname = "./puzzle_input/d5 copy.txt";
    FILE* fp = fopen(fname, "r");
    if (!fp){
        perror("failed to open file.");
        return EXIT_FAILURE;
    }

    char* line = NULL;
    size_t line_cap = 0;
    ssize_t line_len;
    int nicen = 0;
    while ( (line_len = getline(&line, &line_cap, fp)) > 0 ){
        line[strcspn(line, "\n")] = '\0';
        printf("\n%s\n", line);
        if ( is_nice(line) == true ){
            printf("nice\n");
            nicen += 1;
        }
    }

    printf("%d\n", nicen);
    return EXIT_SUCCESS;
}
