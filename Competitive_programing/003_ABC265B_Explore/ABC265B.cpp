#include <bits/stdc++.h>
using namespace std;
#define rep(i,n)for (int i =0 ;i<(n); i++)

int main() {
	int n, m;
	long long t;
	cin>> n>>m>>t;
	vector<int> a(n-1);
	rep(i,n-1) cin >> a[i];

	vector<int> b(n);
	rep(i,m){
		int x,y;
		cin >> x >> y;
		b[x-1]=y;
	}

	rep(i,n-1){
		t += b[i];
		t -= a[i];
		if(t<=0) {
			cout << "No"<<endl;
			return 0;
		}
	}
	cout <<"Yes"<<endl;
	return 0;
}