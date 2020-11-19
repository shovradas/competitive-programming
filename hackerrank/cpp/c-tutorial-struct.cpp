/**
* problem: https://www.hackerrank.com/challenges/c-tutorial-struct
*
* @author Shovra Das    
*/
#include<iostream>
using std::cin;
using std::cout;

struct Student{    
    int age;
    char first_name[51];
    char last_name[51];    
    int standard;
};

int main() {
    Student st;
    
    cin >> st.age >> st.first_name >> st.last_name >> st.standard;
    cout << st.age << " " << st.first_name << " " << st.last_name << " " << st.standard;
    
    return 0;
}
