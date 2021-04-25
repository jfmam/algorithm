import sys
sys.setrecursionlimit(10 ** 9)


def solution(n, costs):
    global Min
    visited = [0] * n
    arr = [[] for _ in range(n)]
    Min = 9999

    for i in costs:
        arr[i[0]].append({'a': i[1], 'cost': i[2]})
        arr[i[1]].append({'a': i[0], 'cost': i[2]})

    def DFS(node, idx, cnt):
        global Min
        if idx == n:
            Min = min(Min, cnt)
            return;
        else:
            visited[node] = 1
            for i in arr[node]:
                if visited[i['a']] == 0:
                    visited[i['a']] = 1
                    DFS(i['a'], idx + 1, cnt + i['cost'])
                    visited[i['a']] = 0
                    
    for i in range(n):
        visited =[0] * n
        DFS(i, 1, 0)
    return Min


ans = solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
print(ans)
