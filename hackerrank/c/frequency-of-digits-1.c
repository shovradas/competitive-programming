// https://www.hackerrank.com/challenges/frequency-of-digits-1/problem

/**
    @author Shovra Das
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int counts[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    char* s = malloc(1000 * sizeof(char));
    scanf("%[^\n]", s);
    s = realloc(s, strlen(s));

    for(int i=0; s[i]!='\0'; ++i){        
        if(s[i]>='0' && s[i]<='9'){
            int digit = (int)s[i]-48;
            counts[digit]++;
        }
    }

    for(int i=0; i<10; ++i){
        printf("%d ", counts[i]);
    }

    return 0;
}
