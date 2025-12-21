#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    long result;
    size_t i;
} recurse_obj;

recurse_obj parse_line(const char *line, size_t linelen, int open_bracket, size_t i){
    // size_t i = 0;
    size_t j;
    size_t start;
    char *strnum;
    // long result = 0;
    recurse_obj ro;
    ro.result = 0;
    ro.i = i;
    int starting_bracket_count = open_bracket;
    while ( ro.i < linelen ){
        if (line[ro.i] == '{'){
            recurse_obj ro_n = parse_line(line, linelen, open_bracket + 1, ro.i + 1);
            ro.result += ro_n.result;
            ro.i = ro_n.i;
        }
        else if (line[ro.i] == '}'){
            ro.i++;
            return ro;
        } else if (open_bracket > 0 && ro.i + 4 < linelen ){
            if (strncmp(&line[ro.i], ":\"red",5) == 0){
                while (open_bracket >= starting_bracket_count) {
                    if (line[ro.i] ==  '{') open_bracket++;
                    if (line[ro.i] ==  '}') open_bracket--;
                    ro.i++;
                }
                ro.result = 0;
                return ro;
            }
        }
        if ( line[ro.i] < '0' || line[ro.i] > '9') {
            ro.i++;
            continue;
        }

        j = ro.i + 1;
        start = ro.i;
        while ( j < linelen && line[j] >= '0' && line[j] <= '9')
            j++;
        if ( ro.i > 0 && line[ro.i-1] == '-' )
            start = ro.i-1;
        strnum = strndup(&line[start], j - start);
        ro.result += atol(strnum);
        ro.i = j;
    }
    return ro;
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

    // line = "[1,2,3] and {\"a\":2,\"b\":4}\0";
    // line = "[1,2,3]\0";
    // line = "[[[3]]] and {\"a\":{\"b\":4},\"c\":-1}\0";
    // line = "{\"a\":[-1,1]} and [-1,{\"a\":1}]\0";
    // line = "[] and {}\0";
    // line = "[1,{\"c\":\"red\",\"b\":2},3]\0";
    // line = "{\"d\":\"red\",\"e\":[1,2,3,4],\"f\":5}";
    // line = "[ {\"a\": 1, \"b\": [{\"c\":\"red\", \"d\": {\"e\": 2000}}] } ]";
    // line = "[ \"red\", {\"a\": 1, \"b\": [{\"aa\": 4000, \"c\":\"red\", \"d\": {\"e\": 2000}}] } ]";
    // line = "[1,\"red\",5]";
    linelen = strlen(line);
    recurse_obj result = parse_line(line, linelen, 0, 0);
    printf("%ld\n", result.result);

    fclose(fp);
    return EXIT_SUCCESS;
}

// 100375 too high
// 333 too low
