#include<stdio.h>
#include<string.h>

// #define F_READ "../data/rand01_out.txt"
// #define F_WRITE "../markov_result.txt"

#define BITS 2
#define VERIFY_COUNT 1024*1000

int main(int argc, char *argv[]){
    FILE *fp1, *fp2;
    char str;
    char tmp[2];
    unsigned int state_count[4][4] = {};
    char state[4][3] = {"00", "01", "10", "11"};
    unsigned int state_total[4] = {};
    unsigned int count_sum = 0;
    int i = 0;
    int now, next;

    if (argc < 2){
        puts("error");
        return -1;
    }

    fp1 = fopen(argv[1], "r");
    if(fp1 == NULL){
        printf("read file can't open.\n");
        return -1;
    }
    while ((str = fgetc(fp1)) != EOF){
        tmp[i++] = str;
        i %= BITS;
        if (i == 0){
            for (next = 0; next < 4; next++)
                if(strcmp(state[next], tmp) == 0) break;
            if (count_sum != 0) state_count[now][next]++;
            state_total[next]++;
            now = next;
            count_sum++;
        }
        if (count_sum == (VERIFY_COUNT / BITS)) {
            break;
        }
    }

    fclose(fp1);

    // output to "result.txt"
    fp2 = fopen(argv[2], "w");
    if(fp2 == NULL){
        printf("write file can't open.\n");
        return -1;
    }

    fprintf(fp2, "result\n");
    fprintf(fp2, "input file is %s\n", argv[1]);
    for (i = 0; i < 4; i++){
        fprintf(fp2, "\n----------state \"%s\"----------\n\n", state[i]);
        fprintf(fp2, "total : %d\n", state_total[i]);
        fprintf(fp2, "\"%s\" : total      %d\n", state[0], state_count[i][0]);
        fprintf(fp2, "       Probability %f\n", state_count[i][0] / (float)state_total[i]);
        fprintf(fp2, "\"%s\" : total      %d\n", state[1], state_count[i][1]);
        fprintf(fp2, "       Probability %f\n", state_count[i][1] / (float)state_total[i]);
        fprintf(fp2, "\"%s\" : total      %d\n", state[2], state_count[i][2]);
        fprintf(fp2, "       Probability %f\n", state_count[i][2] / (float)state_total[i]);
        fprintf(fp2, "\"%s\" : total      %d\n", state[3], state_count[i][3]);
        fprintf(fp2, "       Probability %f\n", state_count[i][3] / (float)state_total[i]);
    }
    fprintf(fp2, "\n\n-------Total Probablity-------\n");
    fprintf(fp2, "total count is : %d\n", count_sum);
    fprintf(fp2, "\"%s\" : %.4f\n", state[0], (state_total[0] / (float)count_sum));
    fprintf(fp2, "\"%s\" : %.4f\n", state[1], (state_total[1] / (float)count_sum));
    fprintf(fp2, "\"%s\" : %.4f\n", state[2], (state_total[2] / (float)count_sum));
    fprintf(fp2, "\"%s\" : %.4f\n", state[3], (state_total[3] / (float)count_sum));
    fprintf(fp2, "------------------------------\n");
    fclose(fp2);

    return 0;
}
