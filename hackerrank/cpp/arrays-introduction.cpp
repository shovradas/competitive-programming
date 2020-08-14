// Problem Link: https://www.hackerrank.com/challenges/arrays-introduction/problem

#include <iostream>
using namespace std;

int main() {
    int a[1000], n, element;

    cin>>n;

    for(int i=0; i<n; ++i){
        cin>>element;
        a[i] = element;
    }

    for(int i=n-1; i>-1; --i){        
        cout<<a[i]<<" ";
    }

    return 0;
}