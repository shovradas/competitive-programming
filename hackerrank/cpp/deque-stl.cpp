// https://www.hackerrank.com/challenges/deque-stl/problem

/**
    @author Shovra Das
*/

#include <iostream>
#include <deque> 
using namespace std;

void printKMax(int arr[], int n, int k){
    deque<int> dq;
    
    // first k elements
    for(int i=0; i<k; ++i){
        while(!dq.empty() && arr[dq.back()]<arr[i])
            dq.pop_back();
        dq.push_back(i);
    }
    
    // elements from k to n
    for(int i=k; i<n; ++i){
        cout<<arr[dq.front()]<<" ";
        
        while(!dq.empty() && dq.front()<=i-k)
            dq.pop_front();
            
        while(!dq.empty() && arr[dq.back()]<arr[i])
            dq.pop_back();
            
        dq.push_back(i);
    }
    cout<<arr[dq.front()]<<endl;
}

int main(){  
    int t;
    cin >> t;
    while(t>0) {
        int n, k;
        cin >> n >> k;
        int arr[n];
        for(int i=0;i<n;i++)
            cin >> arr[i];
        printKMax(arr, n, k);
        t--;
    }
    return 0;
}
