#include <stdio.h>
#include <stdlib.h>

int min_side_area(int l, int w, int h){
    int s1 = l*w;
    int s2 = l*h;
    int s3 = w*h;

    if ( s1 <= s2 && s1 <= s3){
        return s1;
    }
    else if (s2 <= s1 && s2 <= s3){
        return s2;
    }
    else
        return s3;
}

int main(void){
    const char* fname = "./puzzle_input/d2p1.txt";
    FILE* fp = fopen(fname, "r");
    if (!fp){
        perror("file invalid.");
        return EXIT_FAILURE;
    }

    char *line = NULL;
    size_t len;
    int l, w, h;
    int total_area = 0;
    while ( getline(&line, &len, fp ) > 0 ){
        sscanf(line, "%dx%dx%d", &l, &w, &h);
        total_area += 2*l*w + 2*w*h + 2*h*l + min_side_area(l, w, h);
    }


    free(line);
    fclose(fp);
    printf("%d\n", total_area);
    return EXIT_SUCCESS;
}
