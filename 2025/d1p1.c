#include <stdio.h>
#include <stdlib.h>

#define MAX_INSTRUCTIONS 10000

typedef struct {
    char turn;
    int value;
} Instruction;


int main(void) {
    // const char *fname = "d1p1_input.txt";
    const char *fname = "../puzzle_input/d1p1_input.txt";

    FILE *fp = fopen(fname, "r");
    if (!fp) {
        perror("File opening failed.");
        return EXIT_FAILURE;
    }

    Instruction instr[MAX_INSTRUCTIONS];

    char buf[32];
    char t;
    int v;
    int count = 0;
    while ( fgets( buf, sizeof buf, fp ) ) {
        if ( sscanf(buf, "%c%d", &t, &v) == 2 ) {
            instr[count].turn = t;
            instr[count].value = v;
            count++;
        }
    }
    fclose(fp);

    int result = 0;
    int tick = 50;
    for (int i = 0; i < count; i++){
        // printf("%c%d\n", instr[i].turn, instr[i].value);

        if ( instr[i].turn == 'L' ) {
            tick -= instr[i].value;
        }
        else if ( instr[i].turn == 'R' ) {
            tick += instr[i].value;
        }
        else {
            perror("incompatible turn.");
            return 1;
        }

        tick = tick % 100;
        if ( tick == 0 ){
            result++;
        }
    }
    printf("%d\n", result);

    return 0;
}
