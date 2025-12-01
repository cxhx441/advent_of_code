#include <stdio.h>

int main(int argc, char **argv) {

    float fahr, celsius;
    float lower, upper, step;

    lower = 0;  /* lower limit */
    upper = 300; /* upper limit */
    step = 20; /* steps */

    fahr = lower;
    // printf("fahr\tcelsius\n");
    printf("%3s\t%6s\n", "fahr", "celsius");
    while (fahr <= upper) {
        celsius = (5.f / 9.f) * (fahr - 32.f);
        printf("%3.0f\t%6.1f\n", fahr, celsius);
        fahr += step;
    }

    printf("\n");

    lower = -20;  /* lower limit */
    upper = 150; /* upper limit */
    step = 12;
    celsius = lower;
    printf("%3s\t%6s\n", "celsius", "fahr");
    while (celsius <= upper) {
        // celsius = (5.f / 9.f) * (fahr - 32.f);
        fahr = (9.f / 5.f) * celsius + 32.f;
        printf("%3.0f\t%6.1f\n", celsius, fahr);
        celsius += step;
    }
    return 0;
}
