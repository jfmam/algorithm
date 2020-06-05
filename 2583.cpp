#include<iostream>
#include<vector>
#include <algorithm>
#include<queue>


using namespace std;


int dx[4] = { -1,0,1,0 };//x좌표이동
int dy[4] = { 0,1,0,-1 };//y좌표 이동
int arr[101][101];//배열의 정보를 담는다
int main() {
	ios_base::sync_with_stdio(false);//대량의 값을 빠르게 처리하는 방법
	int Max = -1;
	int n, m, k;
	cin >> m >> n>> k;
	int cnt = 0;
	vector<int>v;//도형의 넓이를 저장한다
	int a, b, c, d;
	for (int i = 0;i < k;i++) {
		cin >> a >> b >> c >> d;
		for (int j = b;j < d;j++) {
			for (int r = a;r < c;r++) {
				arr[j][r] = 1;
			}
		}
	}
	queue<pair<int,int>>q;//BFS사용을 위한 queue
	for (int j = 0;j < n;j++) {
		for (int i =m-1;i >= 0;i--) {
			if (arr[i][j] == 0) {
				q.push({ i,j });
				arr[i][j] = 1;
				Max=1;//push되어서 넣어지는 값부터 시작한다.
			}
			else continue;//arr[i][j]가 0값을 갖지않을시에 skip
			while (!q.empty()) {
				int x = q.front().first;
				int y = q.front().second;
				q.pop();
				for (int r = 0;r < 4;r++) {
					int xx = x + dx[r];
					int yy = y + dy[r];
					if (xx < 0 || xx >= m || yy < 0 || yy >= n || arr[xx][yy] != 0) continue;
					else {
						q.push({ xx,yy });
						arr[xx][yy] = 1;
						Max++;
					}
				}
			}
			cnt++;
			v.push_back(Max);
			Max = 0;
		}
	}
	sort(v.begin(), v.end());
	cout << cnt << endl;
	for (int i = 0;i < v.size();i++) {
		cout << v[i] << " ";
	}
}

// 백준 문제 2583
// BFS풀이 사용
// 사용한 이유:내가 이동할 수 있는곳의 좌표로 트리를 만들어서 더이상 Q에 PUSH되는 값이 없을 때 넓이를 반환 하려했다.
// 헷갈렸던 것:
// 1.넓이를 구했어야 했는데 이동거리를 구했다.
// 2.지역변수에서 배열을 선언 하였을경우 초기화 시키지 않으면 NULL값을 갖는다.