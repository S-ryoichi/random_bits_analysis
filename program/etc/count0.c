#include<stdio.h>

#define F_READ "../data/rand01.txt"
#define F_WRITE "../data/rand01_out.txt"
#define F_Wcount "../data/rand1024_"

#define MAX 1024 * 1024


int main(void){
    FILE *fp1, *fp2, *fp_;
    char str;
    unsigned int count = 0;

    fp1 = fopen(F_READ, "r");
    if(fp1 == NULL){
        printf("read file can't open.\n");
        return -1;
    }

    fp2 = fopen(F_WRITE, "w");
    if(fp2 == NULL){
        printf("write file can't open.\n");
        return -1;
    }

    while ((str = fgetc(fp1)) != EOF){
        switch (str){
            case '0': fputs("0000", fp2); count += 4; break;
            case '1': fputs("0001", fp2); count += 4; break;
            case '2': fputs("0010", fp2); count += 4; break;
            case '3': fputs("0011", fp2); count += 4; break;
            case '4': fputs("0100", fp2); count += 4; break;
            case '5': fputs("0101", fp2); count += 4; break;
            case '6': fputs("0110", fp2); count += 4; break;
            case '7': fputs("0111", fp2); count += 4; break;
            case '8': fputs("1000", fp2); count += 4; break;
            case '9': fputs("1001", fp2); count += 4; break;
            case 'A': fputs("1010", fp2); count += 4; break;
            case 'B': fputs("1011", fp2); count += 4; break;
            case 'C': fputs("1100", fp2); count += 4; break;
            case 'D': fputs("1101", fp2); count += 4; break;
            case 'E': fputs("1110", fp2); count += 4; break;
            case 'F': fputs("1111", fp2); count += 4; break;
            default: break;
        }
        if (count >= MAX) break;
    }

    printf("total count is %d\n", count);
    fclose(fp1);
    fclose(fp2);

    return 0;
}
