#include<iostream>
#include<algorithm>
#include <vector>
#include <queue>

using namespace std;

int R, C;
int ch[26];
int dx[4] = { -1,0,1,0 };
int dy[4] = { 0,1,0,-1 };
char map[21][21];
int cnt[21][21];
int Max = 1;

void DFS(int r,int c,int cnt) {
	Max=max(Max, cnt);//몰랐던 부분
	for (int k = 0;k < 4;k++) {
		int xx = r + dx[k];
		int yy = c + dy[k];
		if (ch[map[xx][yy]-'A']!=0||xx<1 || yy<1 || xx>R || yy>C) continue;//문자열을 직접 빼주도록하자
		else {
			ch[map[xx][yy] - 'A'] = 1;
			DFS(xx, yy, cnt + 1);
			ch[map[xx][yy] - 'A'] = 0;
		}
	}

}
int main() {
	ios::sync_with_stdio(false);

	cin >> R >> C;
	for (int i = 1;i <= R;i++) {		
		for (int j = 1;j <= C;j++) {
			cin >> map[i][j];
		}
	}
	ch[map[1][1] - 'A'] = 1;
	DFS(1, 1, 1);
	cout << Max;
}

//DFS문제
//보통의 DFS 는 if else문을 쓰이지만 여기서는 최대값을 찾고 끝내는 방식이라 if else 형식을 따르지않는다
//최대값을 구하는 방법은 재귀시 첫부분에서 계속해서 Max 값을 갱신하는 방법을 사용하면된다.