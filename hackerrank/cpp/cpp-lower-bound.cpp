/**
* problem: https://www.hackerrank.com/challenges/cpp-lower-bound
*
* @author Shovra Das    
*/
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, q, number, index;
    
    cin>>n;    
    vector<int> v(n);
    for(int i=0; i<n; ++i)
        cin>>v[i];
    sort(v.begin(), v.end()); 
    
    std::vector<int>::iterator low;
    cin>>q;
    for(int i=0; i<q; ++i){
        cin>>number;
        low = lower_bound(v.begin(), v.end(), number);
        index = low - v.begin();
        if(v[index] == number)
            cout<<"Yes ";
        else
            cout<<"No ";
        cout<<index+1<<endl;
    }
        
    return 0;
}
