#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

// #define F_READ "../data/rand01_out.txt"
// #define F_WRITE "../prediction_02.txt"
#define MAX 100000000

#define PATTERN 2

#define BIT_WIDTH 2
#define ARRAY_SIZE (BIT_WIDTH * BIT_WIDTH)

//char state[4][3] = {"00", "01", "10", "11"};

//struct Data{
//    char state[BIT_WIDTH + 1];
//    unsigned int state_count[2 ** BIT_WIDTH];
//    unsigned int state_total;
//};

int read(unsigned int state_count[ARRAY_SIZE][PATTERN], unsigned int state_total[], unsigned int count_sum, char *fname){
    FILE *fpr;
    char str;
    // tmp -> {state(BIT_WIDTH[bit]), next_bit(1[bit])}
    unsigned int tmp = 0;
    int now, next;

    fpr = fopen(fname, "r");
    if(fpr == NULL){
        printf("file can't open.\n");
        return -1;
    }
    while ((str = fgetc(fpr)) != EOF){
        tmp += str - '0';
        if (count_sum >= 3){
            now = tmp >> 1;
            next = tmp & 0b1;
            state_count[now][next]++;
            state_total[now]++;
        }
        tmp = (tmp << 1) & 0b111;
        count_sum++;
        if (count_sum == MAX) {
            break;
        }
    }

    fclose(fpr);

    return 0;
}

int main(int argc, char *argv[]){
    //struct Data data[0];
    //struct Data data[1];
    //struct Data data[2];
    //struct Data data[3];
    FILE *fpw;

    unsigned int (*state_count)[PATTERN] = malloc(ARRAY_SIZE * PATTERN * sizeof(unsigned int));
    unsigned int *state_total = malloc(ARRAY_SIZE * sizeof(unsigned int));
    unsigned int count_sum = 0;
    int i = 0;

    if (read(state_count, state_total, count_sum, argv[1]) == -1) return -1;
    if (argc < 2){
        puts("error");
        return -1;
    }

    fpw = fopen(argv[2], "w");
    if(fpw == NULL){
        printf("file can't open.\n");
        return -1;
    }

    fprintf(fpw, "result\n");
    fprintf(fpw, "input file is %s\n", argv[1]);
    for (i = 0; i < ARRAY_SIZE; i++){
        fprintf(fpw, "\n----------state \"%5d\"----------\n\n", i);
        fprintf(fpw, "total : %d\n", state_total[i]);
        fprintf(fpw, "\"%1d\" : total      %d\n", 0, state_count[i][0]);
        fprintf(fpw, "       Probability %f\n", state_count[i][0] / (float)state_total[i]);
        fprintf(fpw, "\"%1d\" : total      %d\n", 1, state_count[i][1]);
        fprintf(fpw, "       Probability %f\n", state_count[i][1] / (float)state_total[i]);
    }

    free(state_count);
    free(state_total);

    return 0;
}
