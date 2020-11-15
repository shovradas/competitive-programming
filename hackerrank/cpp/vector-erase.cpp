// https://www.hackerrank.com/challenges/vector-erase

/**
    @author Shovra Das
*/

#include <vector>
#include <iostream>
using namespace std;


int main() {
    int n, x, a, b;
    
    cin>>n;
    vector<int> v(n);
    for(int i=0; i<n; ++i){
        cin>>v[i];
    }
    
    cin>>x>>a>>b;
    --x, --a, --b; // converting position to index
    v.erase(v.begin()+x);
    v.erase(v.begin()+a, v.begin()+b);
    
    cout<<v.size()<<endl;
    for(int i: v)
        cout<<i<<" ";
    
    return 0;
}
