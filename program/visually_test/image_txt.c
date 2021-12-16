#include<stdio.h>

#define F_READ "../data/rand01_out.txt"
#define F_WRITE "../data/image.txt"

#define LINE 32


int main(void){
    FILE *fp1, *fp2;
    char str;
    unsigned int i = 0, j = 0;

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
            case '0': fputs("0", fp2); break;
            case '1': fputs("1", fp2); break;
        }
        if (i == (LINE - 1)){
            i = 0;
            j++;
            fputs("\n", fp2);
        } else{
            i++;
        }
        if (j == LINE) break;
    }

    fclose(fp1);
    fclose(fp2);

    return 0;
}
