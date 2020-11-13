// https://www.hackerrank.com/challenges/reverse-array-c/problem

/**
    @author Shovra Das
*/

#include <stdio.h>

int main()
{
    int num, *arr, i;
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++)
        scanf("%d", arr + i);

    for(i = num-1; i > -1; --i)
        printf("%d ", *(arr + i));

    return 0;
}