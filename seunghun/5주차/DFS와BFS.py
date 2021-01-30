def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n + 1): # i번 노드에서 이동할 수 있는 구간을 찾는다.
        if visit[i] == 0 and s[v][i] == 1: # 가장 핵심이 되는 구문이다. 중복체크와 이동 할 수 있으면 dfs 함수 호출
            dfs(i)


def bfs(v):
    queue = [v] #queue에 start값 저장
    visit[v] = 0 # 방문한 점 0으로 표시, dfs에서 방문한점을 모두 1로 표시하기 때문
    while(queue): #queue가 있을 때 까지
        v = queue[0] # pop
        print(v, end=' ')
        del queue[0] # pop후 제거
        for i in range(1, n + 1): # v 정점에 대해서 탐색
            if visit[i] == 1 and s[v][i] == 1: #방문하지 않은 점에 대해서만 탐색
                queue.append(i) # 다음에 이동하는 것들에 대해 모두 queue에 저장
                visit[i] = 0


n, m, v = map(int, input().split())
s = [[0 for i in range(n+1) ] for i in range(n + 1)] # 이차원 배열 받는 법, for문을 다음과 같이 간단하게 선언 가능
visit = [0 for i in range(n + 1)] #그래프 탐색의 경우 중복되게 이동이 가능하기 때문에 중복체크를 위한 함수를 설정
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1
# 그래프 형의 경우 다음과 같이 이차원 배열을 만들어서 하는 방법이 있다.

dfs(v)
print()
bfs(v)
