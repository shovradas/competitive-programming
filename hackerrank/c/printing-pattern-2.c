/**
* problem: https://www.hackerrank.com/challenges/printing-pattern-2
*
* @author Shovra Das    
*/
#include <stdio.h>

int main() 
{
    int n, size, x;
    scanf("%d", &n);
  	
    size = n*2-1;
    for(int i=1; i<=size/2+1; ++i){
        for(int j=1; j<=i; ++j){
            x = n-j+1;
            printf("%d ", x);
        }
        for(int j=i; j<=size/2; ++j){
            printf("%d ", x);
        }
        for(int j=i; j<=size/2; ++j){
            printf("%d ", x);
        }     
        for(int j=1; j<i; ++j){
            printf("%d ", x+j);
        }  
        printf("\n");        
    }
    for(int i=size/2; i>=1; --i){
        for(int j=1; j<=i; ++j){
            x = n-j+1;
            printf("%d ", x);
        }
        for(int j=i; j<=size/2; ++j){
            printf("%d ", x);
        }
        for(int j=i; j<=size/2; ++j){
            printf("%d ", x);
        }     
        for(int j=1; j<i; ++j){
            printf("%d ", x+j);
        }  
        printf("\n");
    }

    return 0;
}
