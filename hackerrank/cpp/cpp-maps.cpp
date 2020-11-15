// https://www.hackerrank.com/challenges/cpp-maps

/**
    @author Shovra Das
*/

#include<iostream>
#include<map>
using namespace std;


int main() {
    int n, query, value;
    string key;
    map<string,int> m;
    map<string,int>::iterator itr;
    
    cin>>n;
    for(int i=0; i<n; ++i){
        cin>>query;
        cin>>key;
        if(query==1){
            cin>>value;
            if(m.find(key) != m.end())
                m[key] += value;
            else
                m.insert(make_pair(key, value));
        }                
        else if(query==2)            
            m.erase(key);
        else{
            itr = m.find(key);
            if(itr == m.end())
                cout<<0;
            else
                cout<<itr->second;
            cout<<endl;
        }                     
    }
    
    // print all pairs
    // for (const auto& x : m) {
    //     std::cout << x.first << ": " << x.second << "\n";
    // }
    
    return 0;
}