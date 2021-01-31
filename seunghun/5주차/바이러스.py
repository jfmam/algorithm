import sys

n = int(input())
m = int(input())

arr = [[0 for col in range(n)] for row in range(n)]
visit = [0 for i in range(n)]
for i in range(m):
     a, b = sys.stdin.readline().split()
     a = int(a)
     b = int(b)
     arr[a-1][b-1] = 1
     arr[b-1][a-1] = 1

def dfs(v):
    visit[v] = 1
    for i in range(n):
        if arr[v][i] == 1 and visit[i] == 0: # 한번 방문한 것에 대해서는 방문하지 않는다.
            dfs(i)


dfs(0)
cnt = 0
for i in range(1, n):
    if visit[i] == 1:
        cnt += 1
print(cnt)

     

