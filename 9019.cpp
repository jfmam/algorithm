//다시풀어보기

#include<iostream>
#include<algorithm>
#include <vector>
#include <utility>
#include <cstdlib>
#include <queue>
#include <string>
using namespace std;




int main() {
	ios::sync_with_stdio(false);
	int n;
	cin >> n;
	vector <int> v1(n);
	vector <int>v2(n);
	for (int i = 0;i < n;i++) {
		cin >> v1[i]>>v2[i];
	}	
	
	for (int i = 0;i < n;i++) {
		queue<pair<int, string>>q;//q는 i값이 올라가면서 다시시작해야한다
		q.push({v1[i], ""});
		vector <bool> visited(10000, 0);//visited도 다시시작해야한다!!=>방문한곳은 다시 방문하지 않게 만들어준다.
		visited[v1[i]] = true;
		while (!q.empty()) {
			int a = q.front().first;
			string cnt = q.front().second;
			q.pop();

			if (a == v2[i]) {
				cout << cnt<<endl;
				break;
			}
			int tmp = a;	
			tmp = (a * 2) % 10000;
			if (!visited[tmp]) {
				visited[tmp] = true;
			q.push({ tmp,cnt+ 'D' });
			}
                //D
			if (a == 0) tmp = 9999;
			else tmp = a - 1;
			if (!visited[tmp]) {
				visited[tmp] = true;
				q.push({ tmp,cnt + 'S' });
			}
            //S
			if (a != 0) {//조건문 잘쓰기
				tmp = (a % 1000) * 10 + (a / 1000);//숫자 로테이트 돌리는방법1(모름)
				if (!visited[tmp]) {
					visited[tmp] = true;
					q.push({ tmp,cnt + 'L' });
				}
            //L
				tmp = (a / 10) + (a % 10) * 1000;//숫자 로테이트 돌리는방법2(모름)
				if (!visited[tmp]) {
					visited[tmp] = true;
					q.push({ tmp,cnt + 'R' });
				}
			}
			//R

		}
	}
}

//visited 개념 없었음,L,R 작성부분 몰랐음
//BFS경우 겹치는 경우가 생길때 visited 배열을 꼭만들어주자.
//어느부분에서 변수가 다시 초기화 되어야하는지 잘 생각하자=>26.28줄
