# 解説
前回例題として挙げた問題を解きます。

総当りにしていけば解けそうですが単純に解くと、  
'dream'と'dreamer'、'erase'と'eraser'は途中まで同じスペルになっているおかげで、  
判定に失敗します(ex.普通に処理を組むと'dreamer'を'dream'だと判定してまい、その後の処理で失敗する)
この問題は判定する単語を逆にして処理を組むことで解決する(問題文の方も忘れずに)。  
```CPP
//判定に使用する変数を逆から読んだ状態にしておく
string dream="maerd",dreamer="remaerd",erase="esare", eraser="resare";
```

### 問題文
英小文字からなる文字列 $S$ が与えられます。  
$T$ が空文字列である状態から始め、以下の操作を好きな回数繰り返すことで **$S = T$** とすることができるか判定してください。

* $T$ の末尾に `dream`, `dreamer`, `erase`, `eraser` のいずれかを追加する。

---

### 制約
* $1 \le \vert{}S\vert{} \le 10^5$
* $S$ は英小文字からなる。

---

### 入力
入力は以下の形式で標準入力から与えられます。

```text
S
```

### 出力
S=T とすることができる場合 YES を、そうでない場合 NO を出力せよ。

## コード
``` C++
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
```