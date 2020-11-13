// https://www.hackerrank.com/challenges/playing-with-characters/problem

/**
    @author Shovra Das
*/

#include <stdio.h>
#define MAX_LEN 99

int main() 
{
    char ch;
    char s[MAX_LEN];
    char sen[MAX_LEN];

    scanf("%c", &ch);
    scanf("%s%*c", &s);
    scanf("%[^\n]", &sen);

    printf("%c\n%s\n%s", ch, s, sen);

    return 0;
}
