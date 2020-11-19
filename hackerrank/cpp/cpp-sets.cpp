/**
* problem: https://www.hackerrank.com/challenges/cpp-sets
*
* @author Shovra Das    
*/
#include <iostream>
#include <set>
using namespace std;


int main() {
    int n, query, number;
    set<int> s;
    
    cin>>n;
    for(int i=0; i<n; ++i){
        cin>>query>>number;
        if(query==1)
            s.insert(number);    
        else if(query==2)
            s.erase(number);
        else{
            if(s.find(number) == s.end())
                cout<<"No";
            else
                cout<<"Yes";
            cout<<endl;
        }                     
    }
    
    return 0;
}