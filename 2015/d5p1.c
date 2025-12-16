#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int counts[26];
char* vowels = "aeiou";
int is_nice(const char* input){
    int n = strlen(input);


    for ( int i = 0; i < 26; i++)
        counts[i] = 0;

    int double_letter = 0;
    for ( int i = 0; i < n; i++){
        if ( i > 0 && input[i-1] == input[i] )
            double_letter = 1;
        if (strncmp(&input[i], "ab", 2) == 0)
            return 0;
        if (strncmp(&input[i], "cd", 2) == 0)
            return 0;
        if (strncmp(&input[i], "pq", 2) == 0)
            return 0;
        if (strncmp(&input[i], "xy", 2) == 0)
            return 0;
        counts[input[i] - 'a']++;
    }

    int voweln = 0;
    for ( int i = 0; i < strlen(vowels); i++){
        voweln += counts[ vowels[i] - 'a' ];
    }

    if (voweln < 3)
        return 0;

    return double_letter;
}

int main(void){
    const char* fname = "./puzzle_input/d5.txt";
    FILE* fp = fopen(fname, "r");
    if (!fp){
        perror("failed to open file.");
        return EXIT_FAILURE;
    }

    char* line = NULL;
    size_t line_cap = 0;
    ssize_t line_len;
    int naughtyn = 0;
    while ( (line_len = getline(&line, &line_cap, fp) > 0 ) ){
        line[strcspn(line, "\n")] = '\0';
        if ( is_nice(line) == 1 )
            naughtyn += 1;
    }

    printf("%d\n", naughtyn);
    return EXIT_SUCCESS;
}
