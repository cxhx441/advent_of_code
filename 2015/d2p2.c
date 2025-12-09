#include <stdio.h>
#include <stdlib.h>

int bow_len(int l, int w, int h){
    return l*w*h;
}

int ribbon_len(int l, int w, int h){
    // perimieter of any face;
    int p1 = 2*l + 2*w;
    int p2 = 2*l + 2*h;
    int p3 = 2*w + 2*h;

    if ( p1 <= p2 && p1 <= p3){
        return p1;
    }
    else if (p2 <= p1 && p2 <= p3){
        return p2;
    }
    else
        return p3;
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
    long total_len = 0;
    while ( getline(&line, &len, fp ) > 0 ){
        sscanf(line, "%dx%dx%d", &l, &w, &h);
        total_len += bow_len(l, w, h) + ribbon_len(l, w, h);
    }


    free(line);
    fclose(fp);
    printf("%lu\n", total_len);
    return EXIT_SUCCESS;
}
