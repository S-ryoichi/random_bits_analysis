#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sysexits.h>
#include<math.h>

#define BITS 2
#define SEQUENCE 1000   // 乱数列長
#define STATE_NUM SEQUENCE/BITS
#define COUNT 1000      // 必要本数
#define VERIFY_COUNT SEQUENCE*COUNT
#define ROUNDMAX 1000   // 検定回数


float diviation(int divisible, int divisor){
    // check the divisor whether the value is 0
    if (divisor == 0){
        divisor = INFINITY;
    }
    return (float)divisible / divisor;
}

void main(int argc, char *argv[]){
    FILE *fp1, *fp2;
    char str;
    char tmp[3] = "";
    unsigned int state_count_sub[4][4] = {};
    char state[4][3] = {"00", "01", "10", "11"};
    unsigned int state_total_sub[4] = {};
    unsigned int count_sum = 0;
    int read_count = 0;
    unsigned int round = 0;
    int i = 0, j = 0;
    int now, next;
    // testing the all random number sequence
    // unsigned int state_count[4][4] = {};
    // unsigned int state_total[4] = {};

    char writefile[256];
    if (argc < 2){
        puts("error");
        exit(-1);
    }

    fp1 = fopen(argv[1], "r");
    if(fp1 == NULL){
        printf("read file can't open.\n");
        exit(-1);
    }

    while ((str = fgetc(fp1)) != EOF){
        if (read_count == VERIFY_COUNT || read_count == 0){
            // initialize
            round++;
            read_count = 0;
            count_sum = 0;
            for (i = 0; i < 4; i++){
                for (j = 0; j < 4; j++){
                    // state_count[i][j] = 0;
                    state_count_sub[i][j] = 0;
                }
                // state_total[i] = 0;
                state_total_sub[i] = 0;
            }
            i = 0;
            j = 0;
    
            // file setup
            sprintf(writefile, "%s_%04d.csv", argv[2], round);
            printf("%s\n", writefile);
            fp2 = fopen(writefile, "w");
            if(fp2 == NULL){
                printf("write file can't open.\n");
                exit(-1);
            }
            // header
            fprintf(fp2, "count,P(00),P(01),P(10),P(11),P(00|00),P(01|00),P(10|00),P(11|00),P(00|01),P(01|01),P(10|01),P(11|01),P(00|10),P(01|10),P(10|10),P(11|10),P(00|11),P(01|11),P(10|11),P(11|11)\n");
        }

        // testing
        read_count++;
        tmp[i++] = str;
        i %= BITS;
        if (i == 0){
            for (next = 0; next < 4; next++)
                // compare the read strings and the template strings
                if(strcmp(state[next], tmp) == 0) break;
            if (count_sum == 0) {
                // the first execution
            }
            else if ((count_sum % SEQUENCE) == 0){
                // state_count[now][next]++;
            }
            else {
                // state_count[now][next]++;
                state_count_sub[now][next]++;
            }
            // state_total[next]++;
            state_total_sub[next]++;
            now = next;
            count_sum++;
        }
        // exception handling
        if(next == 4){
            puts("WHAT HAPPEN??");
            exit(-1);
        }

        if (!(read_count % SEQUENCE)){
            fprintf(fp2, "%d,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n", 
                (int)diviation(read_count, SEQUENCE),
                diviation(state_total_sub[0], STATE_NUM),
                diviation(state_total_sub[1], STATE_NUM),
                diviation(state_total_sub[2], STATE_NUM),
                diviation(state_total_sub[3], STATE_NUM),
                diviation(state_count_sub[0][0], state_total_sub[0]),
                diviation(state_count_sub[0][1], state_total_sub[0]),
                diviation(state_count_sub[0][2], state_total_sub[0]),
                diviation(state_count_sub[0][3], state_total_sub[0]),
                diviation(state_count_sub[1][0], state_total_sub[1]),
                diviation(state_count_sub[1][1], state_total_sub[1]),
                diviation(state_count_sub[1][2], state_total_sub[1]),
                diviation(state_count_sub[1][3], state_total_sub[1]),
                diviation(state_count_sub[2][0], state_total_sub[2]),
                diviation(state_count_sub[2][1], state_total_sub[2]),
                diviation(state_count_sub[2][2], state_total_sub[2]),
                diviation(state_count_sub[2][3], state_total_sub[2]),
                diviation(state_count_sub[3][0], state_total_sub[3]),
                diviation(state_count_sub[3][1], state_total_sub[3]),
                diviation(state_count_sub[3][2], state_total_sub[3]),
                diviation(state_count_sub[3][3], state_total_sub[3])
            );
        // if (!(read_count % SEQUENCE)){
        //     fprintf(fp2, "%d,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f\n", 
        //         read_count / SEQUENCE,
        //         state_total_sub[0] / (float)(SEQUENCE / BITS),
        //         state_total_sub[1] / (float)(SEQUENCE / BITS),
        //         state_total_sub[2] / (float)(SEQUENCE / BITS),
        //         state_total_sub[3] / (float)(SEQUENCE / BITS),
        //         state_count_sub[0][0] / (float)state_total_sub[0], 
        //         state_count_sub[0][1] / (float)state_total_sub[0], 
        //         state_count_sub[0][2] / (float)state_total_sub[0], 
        //         state_count_sub[0][3] / (float)state_total_sub[0], 
        //         state_count_sub[1][0] / (float)state_total_sub[1], 
        //         state_count_sub[1][1] / (float)state_total_sub[1], 
        //         state_count_sub[1][2] / (float)state_total_sub[1], 
        //         state_count_sub[1][3] / (float)state_total_sub[1], 
        //         state_count_sub[2][0] / (float)state_total_sub[2], 
        //         state_count_sub[2][1] / (float)state_total_sub[2], 
        //         state_count_sub[2][2] / (float)state_total_sub[2], 
        //         state_count_sub[2][3] / (float)state_total_sub[2], 
        //         state_count_sub[3][0] / (float)state_total_sub[3], 
        //         state_count_sub[3][1] / (float)state_total_sub[3], 
        //         state_count_sub[3][2] / (float)state_total_sub[3], 
        //         state_count_sub[3][3] / (float)state_total_sub[3]               
        //     );

            for (j = 0; j < 4; j++){
                state_count_sub[j][0] = 0;
                state_count_sub[j][1] = 0;
                state_count_sub[j][2] = 0;
                state_count_sub[j][3] = 0;
                state_total_sub[j] = 0;
            }

            // printf("read count: %d\n", read_count);
            if(read_count == VERIFY_COUNT){
                fclose(fp2);
                if (round == ROUNDMAX) break;
            }
        }
    }
    fclose(fp1);
}
