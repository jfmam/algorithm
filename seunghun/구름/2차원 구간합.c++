#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;


int main() {
	ios::sync_with_stdio(false);
	int n;
	cin >> n;
	int p[4];
	vector <vector<int>> v(n, vector<int>(n));
    //vector<type> name(배열 길이 초기화, 베열 값 초기화)
    // 다음과 같이 초기화 값으로 vector를 넣을 수도 있다

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> v[i][j];
		}
	}
	
	for (int i = 0; i < 4; i++) {
		cin >> p[i];
	}
	int sum = 0;

	for (int i = p[0]; i <= p[2]; i++) {
		for (int j = p[1]; j <= p[3]; j++) {
			sum += v[i][j];
		}
	}

	cout << sum;

}