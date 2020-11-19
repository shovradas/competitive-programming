/**
* problem: https://www.hackerrank.com/challenges/bitwise-operators-in-c
*
* @author Shovra Das    
*/
#include <stdio.h>

void calculate_the_maximum(int n, int k) {
    int maxAnd, maxOr, maxXor, and, or, xor;
    maxAnd = maxOr = maxXor = 0;
    for(int i=1; i<=n; ++i){
        for(int j=i+1; j<=n; ++j){
            and = i&j, or=i|j, xor = i^j;            
            if(and<k && and > maxAnd)
                maxAnd = and;
            if(or<k && or > maxOr)
                maxOr = or;
            if(xor<k && xor > maxXor)
                maxXor = xor;
        }
    }
    printf("%d\n%d\n%d", maxAnd, maxOr, maxXor);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}