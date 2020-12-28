#include<iostream>
#include<algorithm>
#include <vector>

 
using namespace std;

int map[21][21];
int ch[21];
int n;
int Min = 9999;
void DFS(int s,int L) {
	if (L == n/2+1) {
		int ssum=0;
		int lsum = 0;
		for (int i = 1;i <= n;i++) {
			for (int j = 1;j <= n;j++) {
				if (ch[i] == 1 && ch[i] == ch[j]) ssum += map[i][j];
				else if (ch[i] == 0 && ch[i] == ch[j])lsum += map[i][j];
			}
		}
		Min = min(abs(ssum - lsum), Min);
		return;
	}
	else {
		for (int i = s;i <= n;i++) {
			ch[i] =1;
			DFS(i + 1, L + 1);
			ch[i] = 0;
		}
	}
}


int main() {
	ios::sync_with_stdio(false);
	cin >> n;
	for (int i = 1;i <= n;i++) {
		for (int j = 1;j <= n;j++) {
			cin >> map[i][j];
		}
	}
	DFS(1,1);
	cout << Min;
}

//조합을 value에 차례대로 넣는방법
//조합에 해당되는 인덱스에 1값을 넣는방법을 구분하여서 코딩 할 수 있어야한다.

//조합(중요!)