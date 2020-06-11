#include<iostream>
#include<algorithm>
#include <vector>
#include <utility>
#include <cstdlib>

using namespace std;

int map[10][10];
vector <pair<int, int>>v;

bool ccheck(int r, int num) {
	for (int c = 0; c < 9; c++) {
		if (map[r][c] == num) {
			return false;
		}
	}
	return true;
}

bool rcheck(int c, int num) {
	for (int r = 0; r < 9; r++) {
		if (map[r][c] == num) {
			return false;
		}
	}
	return true;
}
bool scheck(int r, int c, int num) {
	r = r / 3;
	c = c / 3;
	for (int rr = r * 3; rr < (r * 3) + 3; rr++) {
		for (int cc = c * 3; cc < (c * 3) + 3; cc++) {
			if (map[rr][cc] == num) {
				return false;
			}
		}
	}
	return true;
}

void DFS(int idx) {
	if (idx == v.size()) {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				cout << map[i][j] << " ";
			}
			cout << endl;
		}
		exit(0);
	}
	else {
		for (int i = 1;i <= 9;i++) {
			int x = v[idx].first;
			int y = v[idx].second;
			if (ccheck(x, i) && rcheck(y, i) && scheck(x, y, i)) {
				map[x][y] = i;
				DFS(idx+1);
				map[x][y] = 0;
			}
		}
	}

}

	

int main() {
	ios::sync_with_stdio(false);

	for (int i = 0;i < 9;i++) {
		for (int j = 0;j < 9;j++) {
			cin >> map[i][j];
			if (map[i][j] == 0) {
				v.push_back({ i,j });
			}
		}
	}
	for (int i = 1;i <= 9;i++) {
		int x = v[0].first;
		int y = v[0].second;
		if (ccheck(x, i) && rcheck(y, i) && scheck(x, y, i)) {
			map[x][y] = i;
			DFS(1);
			map[x][y] = 0;
		}
	}
	
}

//푸는방법은 가로 세로 정사각형을 모두검사한뒤에 들어 갈 수 있는 숫자를 모두 넣고
//모든칸에 숫자가 들어갈 수 있으면 그대로 종료시켜버린다.=>exit(0)
//어떠한 position이 주어졌을 때 정사각형 범위를 구하는 방법을 유심히봐야함.
//DFS트리를 구성하는 방법에 대해 몰랐었다.
//DFS는 빈칸을 찾아서 숫자를 넣는 방식으로 이동하면된다.

//map[x][y]가 0일때 0인칸을 수로 채워넣어라=>빈칸을 이동하면서 찾아라 (핵심)
