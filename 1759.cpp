#include<iostream>
#include<algorithm>
#include <vector>

using namespace std;
int L, C;
char ch[16];
vector <char> v;
void DFS(int s, int n, int mo, int ja) {//parameter를 쓰는경우는 자동적으로 초기화 시키고 싶을때 사용하자.
	if (n == L) {
		if (mo >= 1 && ja >= 2) {
			for (int i = 0;i < n;i++) {
				cout << ch[i] ;
			}
			cout << endl;
		}
	}
	else {
		for (int i = s;i < C;i++) {//index의 경우 start param을 보내준 값을 사용
			ch[n] = v[i];//array[Level]=value;조합을 완성하기 위해 넣어주고싶은값을 대입.
			if (v[i] == 'a' || v[i] == 'e' || v[i] == 'i' || v[i] == 'o' || v[i] == 'u') {
				DFS(i + 1, n + 1, mo + 1, ja);//DFS로 param을 보내줄때 start값으로 +1을보내준다
                //이미 고른 값을 i+1로 보내주면서다신 안뽑히게 만든다.
			}
			else
				DFS(i + 1, n + 1, mo, ja + 1);
		}
	}
}
int main() {
    ios::sync_with_stdio(false);
	cin >> L >> C;
	char a;
	for (int i = 0; i < C; i++) {
		cin >> a;
		v.push_back(a);
	}
	sort(v.begin(), v.end());
	DFS(0, 0, 0, 0);
	return 0;
}

//순서가 알파벳순이여야 해서 sort문으로 먼저정리
//또힌 순서는 다르지만 암호에 쓰인 알파벳이 모든똑같은경우도 배제=>조합을 사용한다.
//if(n==L)//0,1,2,3 4개 뽑고 n==4일때 return 시켜야하기때문에 n==L-1이면 안된다.