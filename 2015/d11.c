#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_BUFF 8

void increment(char* buff){
    int i = 0;
    size_t n = strlen(buff);
    buff[i]++;
    while ( i < n && buff[i] == ('z' + 1) ){
        buff[i] = 'a';
        if (i + 1 == n)
            buff[i + 1] = 'a';
        else
            buff[i+1]++;
        i++;
    }
}

bool valid(char* buff){
    size_t n = strlen(buff);

    // check for i, o , l (may not have these)
    for (int i = 0; i < n; i++){
        if ( buff[i] == 'i' || buff[i] == 'o' || buff[i] == 'l' )
            return false;
    }

    // check increasing (or decreasing since reversed in array) by 1 for 3 steps
    bool increasing_straight_three = false;
    for (int i = 2; i < n; i++){
        if ( buff[i-2] - buff[i-1] == 1 && buff[i-1] - buff[i] == 1){
            increasing_straight_three = true;
            break;
        }
    }
    if ( !increasing_straight_three)
        return false;

    // check for min two non-overlapping pairs.
    int first_pair = -1;
    bool double_pair = false;
    for (int i = 1; i < n; i++){
        if ( buff[i] == buff[i-1] ){
            if ( first_pair > -1 && (i-1) - first_pair > 1 ){
                double_pair = true;
                break;
            }
            first_pair = i-1;
        }
    }
    if ( !double_pair)
        return false;
    return true;
}

void printbuff(char* buff){
    size_t n = strlen(buff);
    for (int i = n-1; i > -1; i--){
        putchar(buff[i]);
    }
    putchar('\n');
}

char* next_valid_password(const char* s){
    size_t n = strlen(s);
    char* buff = calloc(MAX_BUFF, sizeof (char));
    int bi = 0;
    for (int i = n-1; i > -1; i--){
        buff[bi++] = s[i];
    }

    while (true){
        increment(buff);
        if ( valid(buff) ){
            return buff;
            free(buff);
        }
    }
}

int main(void){
    // char *s = "hijklmmn";
    // char *s = "abbceffg";
    // char *s = "abbcegjk";

    // char *s = "hhcdefhh";
    // size_t n = strlen(s);
    // char* buff = calloc(MAX_BUFF, sizeof (char));
    // int bi = 0;
    // for (int i = n-1; i > -1; i--){
    //     buff[bi++] = s[i];
    // }
    // if (valid(buff))
    //     printbuff(buff);
    // else
    //     printf("fail\n");

    // char *s = "abcdefgh"; // abcdffaa
    // char *s = "ghijklmn"; // ghjaabcc
    // char *s = "vzbxkghb"; // vzbxxyzz
    char *s = "vzbxxyzz"; // ?
    char* buff = next_valid_password(s);
    printbuff(buff);



    // for (int i = 0; i < 100; i++){
    //     printbuff(buff);
    //     increment(buff);
    // }

    return EXIT_SUCCESS;
}
