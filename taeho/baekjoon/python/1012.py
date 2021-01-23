import sys

sys.setrecursionlimit(10000)
rl = sys.stdin.readline

arr = []
visit = []
xPos = [1, 0, -1, 0]
yPos = [0, 1, 0, -1]


def dfs(x, y):
    global arr, visit
    visit[x][y] = True
    for i in range(4):
        newX, newY = x + xPos[i], y + yPos[i]
        if arr[newX][newY] == 0 or visit[newX][newY]:
            continue
        dfs(newX, newY)


def main():
    global arr, visit
    result = 0
    M, N, K = map(int, rl().split())
    arr = [[0 for _ in range(M + 2)] for _ in range(N + 2)]
    visit = [[False for _ in range(M + 2)] for _ in range(N + 2)]
    for _ in range(K):
        X, Y = map(int, rl().split())
        arr[Y + 1][X + 1] = 1
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if arr[i][j] == 0 or visit[i][j]:
                continue
            dfs(i, j)
            result += 1
    print(result)


for _ in range(int(rl())):
    main()
