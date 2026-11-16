#include <bits/stdc++.h>
using namespace std;
#define rep(I,N)for (int I =0 ;I<(N); I++)// 条件式は都度変える
#define rep1(I,N) for(int I=0;I<(N);) // 予備

int main() {
	//変数と入力
	string s;
	string dream="maerd",dreamer="remaerd",erase="esare", eraser="resare";//dreamから5文字,7文字,5文字,6文字
	cin>> s;
	int count=0,s_count=0;
	string ss[4]={dream,dreamer,erase,eraser};

	//処理
	bool can=true;
	reverse(s.begin(),s.end());
	rep1(i,s.size()){//文字列sに対するループ
		bool can2=false;
		rep(j,4){
			string d =ss[j];
			if(s.substr(i,d.size())==d){
				can2=true;
				i+=d.size();
			}
		}
		if(!can2){
			can=false;
			break;
		}
	}
	//答えとか
	cout<<(can?"YES":"NO");
	return 0;
}