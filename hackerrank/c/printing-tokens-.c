// https://www.hackerrank.com/challenges/printing-tokens-/problem

/**
    @author Shovra Das
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int main() {
    char *s;
    s = malloc(1000 * sizeof(char));
    scanf("%[^\n]", s);
    s = realloc(s, strlen(s) + 1);
    
    for(int i=0; s[i]!='\0'; ++i){
        printf("%c", s[i]);
        if(s[i]==' ')
            printf("\n");
    }

    return 0;
}