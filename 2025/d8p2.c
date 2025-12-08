#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// #define TESTING
#ifdef TESTING
    char* const fname = "./puzzle_input/d8p1_example.txt";
    // #define NPAIRS_TARGET 10
#else
    char* const fname = "./puzzle_input/d8p1_input.txt";
    // #define NPAIRS_TARGET 1000
#endif

#define MIN_LINE_LEN 64
#define CAPACITY 1

typedef struct{
    int x;
    int y;
    int z;
} Coordinate;

typedef struct{
    int a;
    int b;
    double len;
} Edge;

int edgecmp(const void *a, const void *b){
    Edge *e1 = (Edge*) a;
    Edge *e2 = (Edge*) b;

    if ( e1->len < e2->len )
        return -1;
    else if (e1->len > e2->len)
        return 1;
    else
        return 0;
}

int ufcmp(const void *a, const void *b){
    int ai = *(int*)a;
    int bi = *(int*)b;

    if ( ai < bi )
        return -1;
    else if (ai > bi)
        return 1;
    else
        return 0;
}

int get_parent(int* uf, int i){
    if (uf[i] < 0)
        return i;
    // return uf[i] = get_parent(uf, uf[i]); avoiding recursion.
    int cur = i;
    // compression...
    // implement a dynamic stack to track seen and compress.
    int seen_capacity = 1;
    int* seen_stack = malloc(sizeof(int) * seen_capacity);
    int seen_count = 0;

    while ( uf[cur] >= 0 ){

        if ( seen_count == seen_capacity ){
            seen_capacity *= 2;
            seen_stack = realloc(seen_stack, sizeof(int) * seen_capacity);
            if ( seen_stack == NULL ){
                perror("failled realloc on seen_stack");
                return EXIT_FAILURE;
            }
        }

        seen_stack[seen_count++] = cur;
        cur = uf[cur];
    }

    int parent = cur;
    for ( int i = 0; i < seen_count; i++ ){
        uf[seen_stack[i]] = parent;
    }

    return parent;
}

int union_edge(int *uf, int a, int b, int parent_a, int parent_b){
    int rank_a = -uf[parent_a];
    int rank_b = -uf[parent_b];
    int rank_ab = rank_a + rank_b;

    if ( rank_a >= rank_b ){
        uf[parent_a] = -1 * rank_ab;
        uf[parent_b] = parent_a;
    }
    else {
        uf[parent_b] = -1 * rank_ab;
        uf[parent_a] = parent_b;
    }
    return rank_ab;
}

int main(void){

    FILE *fp = fopen(fname, "r");
    if (fp == NULL){
        perror("file not found.");
        return EXIT_FAILURE;
    }

    int capacity = CAPACITY;
    int nboxes = 0;
    Coordinate *junction_boxes = malloc(capacity * sizeof (Coordinate));

    char buf[MIN_LINE_LEN];
    while ( fgets(buf, sizeof (buf), fp) != NULL ){
        Coordinate new_coord;
        sscanf(buf, "%d,%d,%d", &new_coord.x, &new_coord.y, &new_coord.z);
        if (nboxes == capacity){
            capacity *= 2;
            junction_boxes = realloc(junction_boxes, capacity * sizeof (Coordinate));
            if ( junction_boxes == NULL ){
                perror("fail reallocation");
                return EXIT_FAILURE;
            }

        }
        junction_boxes[nboxes++] = new_coord;
        // printf("%d: %d,%d,%d\n", size-1, junction_boxes[size-1].x, junction_boxes[size-1].y, junction_boxes[size-1].z);
    }
    fclose(fp);

    // for (int i = 0; i < nboxes; i++){
    //     printf("%d: %d,%d,%d\n", i, junction_boxes[i].x, junction_boxes[i].y, junction_boxes[i].z);
    // }

    // create edges
    int nedges = ( nboxes * (nboxes - 1) ) / 2;
    Edge* edges = malloc(nedges * sizeof (Edge) );
    int i = 0;
    for (int a = 0; a < nboxes; a++) {
        for ( int b = a + 1; b < nboxes; b++ ){
            edges[i].a = a;
            edges[i].b = b;

            Coordinate n1 = junction_boxes[a];
            Coordinate n2 = junction_boxes[b];
            edges[i].len = sqrt(
                pow(n1.x - n2.x, 2) +
                pow(n1.y - n2.y, 2) +
                pow(n1.z - n2.z, 2)
            );
            i++;
        }
    }

    // sort the edges
    qsort(edges, nedges, sizeof (Edge), edgecmp);

    // connect w unionfind
    int* uf = malloc(nboxes * sizeof (int) );
    for ( int i = 0; i < nboxes; i++)
        uf[i] = -1;
    int merged = 0;
    int edge_idx = 0;
    // for (int looped = 0; looped < NPAIRS_TARGET; looped++){
    int last_a, last_b;
    // while ( merged < 10 ){
    while ( 1 ){
        // merged++;
        Edge e = edges[edge_idx++];
        last_a = e.a;
        last_b = e.b;
        // if (e.a == e.b){
        //     continue;
        // }
        // find
        // printf("%d,%d,%d\n", junction_boxes[e.a].x, junction_boxes[e.a].y, junction_boxes[e.a].z);
        // printf("%d,%d,%d\n", junction_boxes[e.b].x, junction_boxes[e.b].y, junction_boxes[e.b].z);
        int parent_a = get_parent(uf, e.a);
        int parent_b = get_parent(uf, e.b);
        if ( parent_a == parent_b ){
            // printf("same_parent!\n");
            continue;
        }

        // union
        if (union_edge(uf, e.a, e.b, parent_a, parent_b) == nboxes)
            break;
        // printf("%d: unioned\n", npairs+1);
        // for (int i = 0; i < nboxes; i++){
        //     printf("%d, ", uf[i]);
        // }
        // printf("\n");
        merged++;
    }

    // int result = 1;
    // for ( int i = 0; i < nboxes; i++){
    //     if ( uf[i] < 0 ){
    //         result *= (-1 * uf[i]);
    //     }
    // }
    // printf("%d\n", result);

    // // for (int i = 0; i < nboxes; i++){
    // //     printf("%d, ", uf[i]);
    // // }
    // // printf("\n");

    // qsort(uf, nboxes, sizeof (int), ufcmp);
    // for (int i = 0; i < nboxes; i++){
    //     printf("%d, ", uf[i]);
    // }
    // printf("\n");
    // printf("%d*%d*%d = %d\n", -uf[0], -uf[1], -uf[2], -uf[0]*-uf[1]*-uf[2]);

    printf("%d,%d,%d\n", junction_boxes[last_a].x, junction_boxes[last_a].y, junction_boxes[last_a].z);
    printf("%d,%d,%d\n", junction_boxes[last_b].x, junction_boxes[last_b].y, junction_boxes[last_b].z);
    printf("%lu\n", (long)junction_boxes[last_a].x * (long)junction_boxes[last_b].x);
    printf("ok\n");
    return EXIT_SUCCESS;
}
