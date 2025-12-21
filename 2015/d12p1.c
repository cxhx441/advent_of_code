#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long parse_line(const char *line, size_t linelen){
    size_t i = 0;
    size_t j;
    size_t start;
    char *strnum;
    long result = 0;
    // line = "[1,2,3] and {\"a\":2,\"b\":4}\0";
    // line = "[[[3]]] and {\"a\":{\"b\":4},\"c\":-1}\0";
    // line = "{\"a\":[-1,1]} and [-1,{\"a\":1}]\0";
    // line = "[] and {}\0";
    // linelen = strlen(line);
    while ( i < linelen ){
        if ( line[i] < '0' || line[i] > '9') {
            i++;
            continue;
        }

        j = i + 1;
        start = i;
        while ( j < linelen && line[j] >= '0' && line[j] <= '9')
            j++;
        if ( i > 0 && line[i-1] == '-' )
            start = i-1;
        strnum = strndup(&line[start], j - start);
        result += atol(strnum);
        i = j + 1;
    }
    return result;
}

int main(void){
    const char* fname = "./puzzle_input/d12.txt";
    FILE *fp = fopen(fname, "r");
    if (!fp) {
        perror("error opening file.");
        return EXIT_FAILURE;
    }

    char *line = NULL;
    size_t linecap = 0;
    ssize_t linelen;
    linelen = getline(&line, &linecap, fp);
    long result = parse_line(line, linelen);
    printf("%ld\n", result);

    fclose(fp);
    return EXIT_SUCCESS;
}
