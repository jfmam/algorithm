import sys
sys.setrecursionlimit(10 ** 9)


def solution(n, costs):
    ans = 0
    costs.sort(key= lambda x: x[2] ) # cost 기준으로 정렬
    routes = set([costs[0][0]])
    while len(routes) != n :
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[i] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return ans

ans = solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
print(ans)
