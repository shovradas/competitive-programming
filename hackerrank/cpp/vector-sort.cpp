// https://www.hackerrank.com/challenges/vector-sort

/**
    @author Shovra Das
*/

#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    
    cin>>n;
    vector<int> v(n);
    
    for(int i; i<n; ++i)
        cin>>v[i];
    
    sort(v.begin(), v.end());
    
    for(int i; i<n; ++i)
        cout<<v[i]<<" ";
    
    return 0;
}
