import sys

n = int(input())
arr = [list(map(str, input())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0


def bfs(x, y): #
    queue = [[x, y]] #
    ch[x][y] = 1 # 
    global cnt
    while(queue):
        a = queue.pop(0)
        i = a[0]
        j = a[1]
        for k in range(4):
            xx = i + dx[k]
            yy = j + dy[k]
            if 0 <= xx < n and 0 <= yy < n:
                if ch[xx][yy] == 0 and arr[x][y] == arr[xx][yy]:
                    queue.append([xx, yy])
                    ch[xx][yy] = 1
    cnt += 1


for i in range(n):
    for j in range(n):
        if ch[i][j] == 0:
            bfs(i, j)
print(cnt, end=' ')
cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] ='R'

ch = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if ch[i][j] == 0:
            bfs(i, j)
print(cnt)
