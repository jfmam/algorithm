#include<iostream>
#include<algorithm>
#include <vector>
#include <queue>
#include <string>
using namespace std;




int main() {
	ios::sync_with_stdio(false);
	//FSGUD 건물층,자기가있는층,이동층,up,down
	//도달하지 못하는 걸어떻게 표현할까
	int F, S, G, U, D;
	cin >> F >> S >> G >> U >> D;
	vector<int>ch(F + 1);
	queue<int>q;
	q.push(S);
	ch[S]= 1;
	while (!q.empty()) {
		int x = q.front();
		q.pop();
		int u = x + U;
		int d = x - D;
		if (x== G) {
			cout << ch[x]-1;
			exit(0);
		}


		if (ch[u]==0&&u<=F) { 
			ch[u] = ch[x] + 1;
			q.push(u);
		}
		if (ch[d]==0&&d>=1) { 
			ch[d]=ch[x] + 1;
			q.push(d); 
		}
		
	}
	cout << "use the stairs";
}

//BFS문제//
//BFS로 탐색시 queue에서 모든값들이 pop 되었을때 결과값이 나오지 않는다면 그땐 경우의 수를 찾을 수 없는것이다.
//맨마지막에 use the stairs를 써주는 경우가 그런경우이다.