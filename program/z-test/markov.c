#include<stdio.h>
#include<string.h>

// #define F_READ "../data/rand01_out.txt"
// #define F_WRITE "../markov_result.csv"

#define BITS 2
#define SEQUENCE 1000
#define COUNT 1000
#define VERIFY_COUNT SEQUENCE*COUNT



int main(int argc, char *argv[]){
    FILE *fp1, *fp2;
    char str;
    char tmp[2];
    unsigned int state_count[4][4] = {};
    unsigned int state_count_sub[4][4] = {};
    char state[4][3] = {"00", "01", "10", "11"};
    unsigned int state_total[4] = {};
    unsigned int state_total_sub[4] = {};
    unsigned int count_sum = 0;
    unsigned int read_count = 0;
    int i = 0, j = 0;
    int now, next;

    if (argc < 2){
        puts("error");
        return -1;
    }

    // input from "rand01_out.txt"
    fp1 = fopen(argv[1], "r");
    if(fp1 == NULL){
        printf("read file can't open.\n");
        return -1;
    }

    // output to "markov_result.csv"
    fp2 = fopen(argv[2], "w");
    if(fp2 == NULL){
        printf("write file can't open.\n");
        return -1;
    }

    // fprintf(fp2, ",state transition probablity,,,,00,,,,01,,,,10,,,,11,,,\n");
    fprintf(fp2, "count,00,01,10,11,0000,0001,0010,0011,0100,0101,0110,0111,1000,1001,1010,1011,1100,1101,1110,1111\n");
    
    while ((str = fgetc(fp1)) != EOF){
        read_count++;
        tmp[i++] = str;
        i %= BITS;
        if (i == 0){
            for (next = 0; next < 4; next++)
                // 文字列比較（現状態がどの状態なのか）
                if(strcmp(state[next], tmp) == 0) break;
            // 初回以降適用される
            if (count_sum == 0) {
            }
            else if ((count_sum % SEQUENCE) == 0){
                state_count[now][next]++;
            }
            else {
                state_count[now][next]++;
                state_count_sub[now][next]++;
            }
            state_total[next]++;
            state_total_sub[next]++;
            now = next;
            count_sum++;
        }
        if (read_count % SEQUENCE == 0){
            fprintf(fp2, "%d,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n", 
                read_count / SEQUENCE,
                state_total_sub[0] / (float)(SEQUENCE / BITS),
                state_total_sub[1] / (float)(SEQUENCE / BITS),
                state_total_sub[2] / (float)(SEQUENCE / BITS),
                state_total_sub[3] / (float)(SEQUENCE / BITS),
                state_count_sub[0][0] / (float)state_total_sub[0], 
                state_count_sub[0][1] / (float)state_total_sub[0], 
                state_count_sub[0][2] / (float)state_total_sub[0], 
                state_count_sub[0][3] / (float)state_total_sub[0], 
                state_count_sub[1][0] / (float)state_total_sub[1], 
                state_count_sub[1][1] / (float)state_total_sub[1], 
                state_count_sub[1][2] / (float)state_total_sub[1], 
                state_count_sub[1][3] / (float)state_total_sub[1], 
                state_count_sub[2][0] / (float)state_total_sub[2], 
                state_count_sub[2][1] / (float)state_total_sub[2], 
                state_count_sub[2][2] / (float)state_total_sub[2], 
                state_count_sub[2][3] / (float)state_total_sub[2], 
                state_count_sub[3][0] / (float)state_total_sub[3], 
                state_count_sub[3][1] / (float)state_total_sub[3], 
                state_count_sub[3][2] / (float)state_total_sub[3], 
                state_count_sub[3][3] / (float)state_total_sub[3]
            );

            for (j = 0; j < 4; j++){
                state_count_sub[j][0] = 0;
                state_count_sub[j][1] = 0;
                state_count_sub[j][2] = 0;
                state_count_sub[j][3] = 0;
                state_total_sub[j] = 0;
            }
        }
        if (read_count == VERIFY_COUNT) {
            break;
        }
    }

    fclose(fp1);

    // fprintf(fp2, "total\n");
    // fprintf(fp2, ",%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n", 
    //     state_total[0] / (float)(VERIFY_COUNT / BITS),
    //     state_total[1] / (float)(VERIFY_COUNT / BITS),
    //     state_total[2] / (float)(VERIFY_COUNT / BITS),
    //     state_total[3] / (float)(VERIFY_COUNT / BITS),
    //     state_count[0][0] / (float)state_total[0], 
    //     state_count[0][1] / (float)state_total[0], 
    //     state_count[0][2] / (float)state_total[0], 
    //     state_count[0][3] / (float)state_total[0], 
    //     state_count[1][0] / (float)state_total[1], 
    //     state_count[1][1] / (float)state_total[1], 
    //     state_count[1][2] / (float)state_total[1], 
    //     state_count[1][3] / (float)state_total[1], 
    //     state_count[2][0] / (float)state_total[2], 
    //     state_count[2][1] / (float)state_total[2], 
    //     state_count[2][2] / (float)state_total[2], 
    //     state_count[2][3] / (float)state_total[2], 
    //     state_count[3][0] / (float)state_total[3], 
    //     state_count[3][1] / (float)state_total[3], 
    //     state_count[3][2] / (float)state_total[3], 
    //     state_count[3][3] / (float)state_total[3]
    // );

    fclose(fp2);
    return 0;
}
