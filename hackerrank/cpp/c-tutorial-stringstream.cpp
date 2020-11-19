/**
* problem: https://www.hackerrank.com/challenges/c-tutorial-stringstream
*
* @author Shovra Das    
*/
#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	stringstream ss(str);
    vector<int> numbers;    
    char ch;
    int i;
    while(ss>>i){
        numbers.push_back(i);
        ss>>ch;
    }        
    return numbers;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}