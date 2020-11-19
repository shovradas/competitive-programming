/**
* problem: https://www.hackerrank.com/challenges/c-tutorial-for-loop
*
* @author Shovra Das    
*/
#include <iostream>
using std::cin;
using std::cout;
using std::endl;

int main() {
    int a, b;
    
    cin>>a>>b;
    
    for(int n=a; n<=b; ++n){
        if(n==1)
            cout<<"one";
        else if(n==2)
            cout<<"two";
        else if(n==3)
            cout<<"three";
        else if(n==4)
            cout<<"four";
        else if(n==5)
            cout<<"five";
        else if(n==6)
            cout<<"six";
        else if(n==7)
            cout<<"seven";
        else if(n==8)
            cout<<"eight";
        else if(n==9)
            cout<<"nine";
        else
            if((n&1) == 1)
                cout<<"odd";
            else
                cout<<"even";
        cout<<endl;     
    }   
        
    return 0;
}