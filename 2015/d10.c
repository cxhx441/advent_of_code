#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFF_LEN 10000000
size_t look_and_say(const char* seed, int n_iterations){
    // char buff0[BUFF_LEN];
    // char buff1[BUFF_LEN];
    char *buff0 = malloc(BUFF_LEN * sizeof (char));
    char *buff1 = malloc(BUFF_LEN * sizeof (char));
    long i0 = 0;
    long i1 = 0;

    // Put seed in buff0
    for ( long i = 0; i < strlen(seed); i++){
        buff0[i0++] = seed[i];
    }

    for ( int i_iter = 0; i_iter < n_iterations; i_iter++){
        // count vals in buff0, additing them to buff 1.
        i0 = i1 = 0;
        char prev = buff0[0];
        i0++;
        int count = 1;
        while (buff0[i0] != '\0'){
            if (buff0[i0] != prev){
                sprintf(&buff1[i1++], "%d", count);
                buff1[i1++] = prev;
                count = 0;
            }
            prev = buff0[i0++];
            count++;
        }
        sprintf(&buff1[i1++], "%d", count);
        buff1[i1++] = prev;

        buff1[i1] = '\0';
        // put buff1 into buff0, ensure the last value is NULL terminator.
        i0 = 0;
        i1 = 0;
        while (buff1[i1] != '\0'){
            buff0[i0++] = buff1[i1++];
        }
        buff0[i0] = '\0';
        buff1[0] = '\0';
        // printf("%s\n", buff0);
    }
    // printf("%s\n", buff0);
    size_t nbuff0 = strlen(buff0);
    free(buff0);
    free(buff1);
    return nbuff0;
}


int main(void){
    // look_and_say("1", 1); // return "11"
    // look_and_say("11", 1); // return "21"
    // look_and_say("21", 1); // return "1211"
    // look_and_say("1211", 1); // return "111221"
    // look_and_say("111221", 1); // return "312211"
    // look_and_say("1", 5); // return "312211"
    // printf("%zu\n", look_and_say("1", 5));

    // printf("40:\n");
    // printf("%zu\n", look_and_say("1321131112", 40)); // 492982
    // printf("50:\n");
    // printf("%zu\n", look_and_say("1321131112", 50)); // 6989950

    return EXIT_SUCCESS;
}

// 100027 too low.
