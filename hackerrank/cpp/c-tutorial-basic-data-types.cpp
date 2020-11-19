/**
* problem: https://www.hackerrank.com/challenges/c-tutorial-basic-data-types
*
* @author Shovra Das    
*/
#include <iostream>
#include <iomanip>
using std::cin;
using std::cout;
using std::endl;
using std::fixed;
using std::setprecision;

int main() {
    int xInt; 
    long xLong;
    char xChar;
    float xFloat; 
    double xDouble;

    cin>>xInt>>xLong>>xChar>>xFloat>>xDouble;
    
    cout<<xInt<<endl<<xLong<<endl<<xChar<<endl;
    cout<<fixed<<setprecision(3)<<xFloat<<endl<<setprecision(9)<<xDouble<<endl;

    return 0;
}
