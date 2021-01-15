N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().strip(""))))


xPos = [-1, 1, 0, 0]
yPos = [0, 0, -1, 1]
visit = [[False] * N for _ in range(N)]
dngs = []
dng = 1
count = 0


def dfs(x, y):
    visit[x][y] = True
    global dng
    for i in range(4):
        newX = x + xPos[i]
        newY = y + yPos[i]
        if newX < 0 or newY < 0 or newX >= N or newY >= N:
            continue
        elif visit[newX][newY]:
            continue
        elif graph[newX][newY] != 1:
            continue
        else:
            dng += 1
            dfs(newX, newY)
    return dng


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visit[i][j] == False:
            count += 1
            dngs.append(dfs(i, j))
            dng = 1

print(count)
for i in sorted(dngs):
    print(i)
