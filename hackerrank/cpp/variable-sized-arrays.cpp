// https://www.hackerrank.com/challenges/variable-sized-arrays

/**
    @author Shovra Das
*/

#include <vector>
#include <iostream>
using namespace std;


int main() {
    int n, q, size, element, row, col;
    cin>>n>>q;
    
    vector<vector<int>*> v;
    for(int i=0; i<n; ++i){
        cin>>size;
        v.push_back(new vector<int>());
        for(int j=0; j<size; ++j){
            cin>>element;
            v[i]->push_back(element);            
        }  
    }    
    
    for(int i=0; i<q; ++i){
        cin>>row>>col;
        cout<<v[row]->at(col)<<endl;
    }
    
    return 0;
}
