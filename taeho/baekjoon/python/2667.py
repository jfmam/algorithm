# N = int(input())
# graph = []
# visit = [[False] * N for _ in range(N)]
# iPos = [-1, +1, 0, 0]
# jPos = [0, 0, -1, 1]
# dngs = []
# dng = 1

# for _ in range(N):
#     graph.append(list(map(int, input().strip(" "))))


# def dfs(i, j):
#     global dng
#     visit[i][j] = True
#     for p in range(4):
#         newI, newJ = i + iPos[p], j + jPos[p]
#         if newI < 0 or newI >= N or newJ < 0 or newJ >= N:
#             continue
#         elif graph[newI][newJ] != 1 or visit[newI][newJ]:
#             continue
#         else:
#             dng += 1
#             dfs(newI, newJ)


# cnt = 0
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == 1 and visit[i][j] == False:
#             cnt += 1
#             dfs(i, j)
#             dngs.append(dng)
#             dng = 1
# print(cnt)
# for i in sorted(dngs):
#     print(i)

N = int(input())
graph = []
visit = [[False] * N for _ in range(N)]
dngs = []
dng = 0

for _ in range(N):
    graph.append(list(map(int, input().strip(" "))))


def dfs(i, j):
    global dng
    if i < 0 or i >= N or j < 0 or j >= N:
        return
    if visit[i][j] or graph[i][j] == 0:
        return
    visit[i][j] = True
    dng += 1
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)


cnt = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visit[i][j] == False:
            cnt += 1
            dfs(i, j)
            dngs.append(dng)
            dng = 0
print(cnt)
for i in sorted(dngs):
    print(i)
