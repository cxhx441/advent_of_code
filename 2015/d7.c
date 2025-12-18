#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_WIRE_HASH_VALUE (26 * 26) + 26

typedef struct {
    char * w1;
    char * w2;
    char op;
    char * w3;
} logic_gate;

int indeg[MAX_WIRE_HASH_VALUE] = {0};
int wires[MAX_WIRE_HASH_VALUE] = {-1};


int hash(const char* s){
    /* one or two lower case letters can be encoded to (26 * 26) + 26 values. */
    if (strlen(s) > 2){
        perror("wire label too long.");
        return EXIT_FAILURE;
    }

    if (strlen(s) == 1)
        return (26*26) + s[0] - 'a';
    return 26*(s[1] - 'a') + (s[0] - 'a');
}

int main(void){
    const char *fname = "./puzzle_input/d7_ex.txt";
    FILE *fp = fopen(fname, "r");
    if (!fp){
        perror("file opening error.\n");
        return EXIT_FAILURE;
    }

    char *line = NULL;
    size_t linecap = 0;
    size_t linelen;
    char *input = NULL;
    char *output = NULL;
    char *op = NULL;
    printf("starting.\n");
    while ( (linelen = getline(&line, &linecap, fp) > 0) ){
        logic_gate lg;
        line[ strcspn(line, "\n") ] = '\0';
        input = strtok(line, "@");
        output = strtok(NULL, "@");
        printf("%s|%s\n", input, output);

        strcpy(lg.w3, output);
        if (input[0] == '!'){
            lg.op = '!';
            strcpy(lg.w1, input[1]);
        }
        else{
            /* AND OR LSHIFT RSHIFT */
            if (strchr(input, '&') != NULL){
                lg.w1 = strtok(input, "&");
                lg.w2 = strtok(NULL, "&");
                lg.op = '&';
            }
            else if (strchr(input, '|') != NULL){
                lg.w1 = strtok(input, "|");
                lg.w2 = strtok(NULL, "|");
                lg.op = '|';
            }
            else if (strchr(input, '<') != NULL){
                lg.w1 = strtok(input, "<");
                lg.w2 = strtok(NULL, "<");
                lg.op = '<';
            }
            else if (strchr(input, '>') != NULL){
                lg.w1 = strtok(input, ">");
                lg.w2 = strtok(NULL, ">");
                lg.op = '>';
            }
            else{
                wires[hash(lg.w3)] = atio(input);
            }

        }
    }
    printf("done.\n");

    return EXIT_SUCCESS;
}
