// https://www.hackerrank.com/challenges/hello-world-c/problem

/**
    @author Shovra Das
*/

#include <stdio.h>

int main() 
{
	
    char s[100];
    scanf("%[^\n]%*c", &s);
  	
    printf("Hello, World!");
    printf("\n%s", s);
    
    return 0;
}
