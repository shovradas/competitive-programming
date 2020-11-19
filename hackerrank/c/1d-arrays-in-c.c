/**
* problem: https://www.hackerrank.com/challenges/1d-arrays-in-c
*
* @author Shovra Das    
*/
#include <stdio.h>
#define MAX_LEN 1000

int main() {
    int array[MAX_LEN], n, sum=0;
    
    scanf("%d", &n);

    for(int i=0; i<n; ++i){
        scanf("%d", array+i);
        sum += array[i];
    }
    
    printf("%d", sum);

    return 0;
}
