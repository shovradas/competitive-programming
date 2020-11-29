/**
* problem: https://www.hackerrank.com/challenges/preprocessor-solution
* tutorial: http://www.cplusplus.com/doc/tutorial/preprocessor/
* 
* @author Shovra Das    
*/

// replaces foreach(v, i) by for(auto i=0; i<v.size(); ++i)
#define foreach(v, i) for(auto i=0; i<v.size(); ++i)

// replaces io(v) by cin>>v
#define io(v) cin>>v  

#define INF 100000000  // constraint: -10^8 <= x[i] <= 10^8

#define FUNCTION(name, operator_) void name(int& m, int n){ if(n operator_ m) m = n; }
// FUNCTION(minimum, <) is replaced with void minimum(int& m, int n){ if(n < m) m = n; }
// FUNCTION(maximum, >) is replaced with void maximum(int& m, int n){ if(n > m) m = n; }

#define toStr(whatever) #whatever  // #whatever means double quoted "whaterver"

#include <iostream>
#include <vector>
using namespace std;

#if !defined toStr || !defined io || !defined FUNCTION || !defined INF
#error Missing preprocessor definitions
#endif 

FUNCTION(minimum, <)
FUNCTION(maximum, >)

int main(){
	int n; cin >> n;
	vector<int> v(n);
	foreach(v, i) {
		io(v)[i];
	}
	int mn = INF;
	int mx = -INF;
	foreach(v, i) {
		minimum(mn, v[i]);
		maximum(mx, v[i]);
	}
	int ans = mx - mn;
	cout << toStr(Result =) <<' '<< ans;
	return 0;

}