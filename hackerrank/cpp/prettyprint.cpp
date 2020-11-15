// https://www.hackerrank.com/challenges/prettyprint

/**
    @author Shovra Das
*/

#include <iostream>
#include <iomanip> 
using namespace std;

int main() {
	int T; cin >> T;
	cout << setiosflags(ios::uppercase);
	cout << setw(0xf) << internal;
	while(T--) {
		double A; cin >> A;
		double B; cin >> B;
		double C; cin >> C;
        cout<<hex<<showbase<<nouppercase<<left<<(long long)A<<endl;
        cout<<dec<<showpos<<fixed<<setprecision(2)<<setw(15)<<setfill('_')<<right<<B<<endl;
        cout<<scientific<<noshowpos<<uppercase<<setprecision(9)<<C<<endl;
	}
	return 0;

}