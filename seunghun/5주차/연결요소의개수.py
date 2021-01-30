import sys
sys.setrecursionlimit(10000)
n, m = map(int, sys.stdin.readline().split())
arr = [[0] * (n + 1) for _ in range(n+1)]
ch = [0] * (n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1

def dfs(v):
    ch[v] = 1
    for i in range(n+1):
        if ch[i] == 0 and arr[v][i] == 1:
            dfs(i)
cnt = 0
for i in range(1, n+1):
    if(ch[i] == 0):
        dfs(i)
        cnt += 1

print(cnt)