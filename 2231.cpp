#include<iostream>
using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	
	int n;
	cin >>n;
	int tmp,res=-1;
	for (int i = 0;i < n;i++) {
		tmp = i;
		int sum = i;
		while (tmp > 0) {
			if (sum > n) break;
			sum += (tmp % 10);
			tmp /= 10;
		}
		if (sum == n) {
			cout << i;
			return 0;
		}
	}
	cout << 0;

}
//분해합 문제
//변수설정 중요!
//제일작은 생성자를 출력!