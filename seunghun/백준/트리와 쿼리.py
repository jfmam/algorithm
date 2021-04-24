import sys
sys.setrecursionlimit(10 ** 9
)
n, r, q = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)

def DFS(node):
    visited[node] = 1
    for i in arr[node]:
        if visited[i] == 0:
            DFS(visited[i])
            visited[i] += visited[node]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)


DFS(r)
ans = []

for _ in len(q):
    c = int(input())
    print(visited[c])