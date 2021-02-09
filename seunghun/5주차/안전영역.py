import sys
sys.setrecursionlimit(1000000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, h):
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if (0 <= xx < n) and (0 <= yy < n) and ch[xx][yy] == 0 and arr[xx][yy] > h:
            ch[xx][yy] = 1
            dfs(xx, yy, h)


n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = 1

for k in range(max(map(max, arr))): # 이차원 배열에서 max 값 구하는법
    ch = [[0]*n for _ in range(n)]
    safe = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k and ch[i][j] == 0:
                safe += 1
                ch[i][j] = 1
                dfs(i, j, k) # dfs의 용도는 영역 체크 용
    ans = max(safe, ans)

print(ans)
