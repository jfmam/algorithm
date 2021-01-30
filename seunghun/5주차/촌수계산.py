import sys

n = int(input())
a, b = map(int, sys.stdin.readline().split())
m = int(input())
arr = [[0] * (n+1) for i in range(n+1)]
visit = [0] * (n+1)

for i in range(m):
    c, d = map(int, sys.stdin.readline().split())
    arr[c][d] = 1
    arr[d][c] = 1

queue = [a]
while(queue):
    v = queue.pop(0)
    for i in range(1, n+1):
        if visit[i] == 0 and arr[v][i] == 1:
            queue.append(i)
            visit[i] = visit[v] + 1 # bfs에서 count 세는 법
print(visit[b] if visit[b] else -1)