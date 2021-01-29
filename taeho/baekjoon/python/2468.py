import sys

sys.setrecursionlimit(10 ** 6)
rl = sys.stdin.readline


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n or visited[x][y]:
        return
    if local[x][y] == 0:
        return
    visited[x][y] = True
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)


n = int(rl())
arr = []
maxHeight = []
for _ in range(n):
    l = list(map(int, rl().split()))
    maxHeight.append(max(l))
    arr.append(l)
maxH = max(maxHeight)
local = [[1 for _ in range(n)] for _ in range(n)]
maxLocal = []
visited = [[False for _ in range(n)] for _ in range(n)]
cnt = 0

for s in range(maxH + 1):
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= s:
                local[i][j] = 0
    for i in range(n):
        for j in range(n):
            cnt += 1
            dfs(i, j)
    maxLocal.append(cnt)
    cnt = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
print(max(maxLocal))