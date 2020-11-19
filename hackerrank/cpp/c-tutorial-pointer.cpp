/**
* problem: https://www.hackerrank.com/challenges/c-tutorial-pointer
*
* @author Shovra Das    
*/
#include<iostream>
#include<cmath>
using std::cin;
using std::cout;
using std::endl;
using std::abs;

void update(int *a,int *b) {
    int x = *a + *b;
    *b = abs(*a - *b);
    *a = x;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    cin>>a>>b;
    update(pa, pb);
    cout<<a<<endl<<b;

    return 0;
}