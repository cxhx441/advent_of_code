#include <stdio.h>
#include <stdlib.h>

int main(void){
    const char* fname = "./puzzle_input/d1p1.txt";
    FILE* fp = fopen(fname, "r");
    if (!fp){
        perror("file invalid.");
        return EXIT_FAILURE;
    }
    int floor = 0;
    int c;
    int count = 0;
    while ( (c = fgetc(fp)) != EOF ){
        if ( c == '('){
            floor++;
            count++;
        }
        else if (c == ')'){
            floor--;
            count++;
        }

        if ( floor == -1 ){
            break;
        }
    }
    fclose(fp);
    printf("result: %d\n", count);
    return EXIT_SUCCESS;
}
