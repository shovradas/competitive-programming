// https://www.hackerrank.com/challenges/sum-of-digits-of-a-five-digit-number/problem

#include <stdio.h>

int main() {
	
    int n;
    scanf("%d", &n);

    int sum = 0;
    while(n){
        sum += n%10;
        n /= 10;
    }
    printf("%d", sum);

    return 0;
}