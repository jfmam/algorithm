import sys
sys.setrecursionlimit(10 ** 9)


def solution(n, costs):
    ans = 0
    costs.sort(key= lambda x: x[2] ) # cost 기준으로 정렬
    cycle = set([costs[0][0]]) # cycle의 집합
    while len(cycle) != n :
        for i, cost in enumerate(costs):
            if cost[0] in cycle and cost[1] in cycle:# cycle에 속해 있으면 해당 값 반환
                continue
            if cost[0] in cycle or cost[1] in cycle:
                cycle.update([cost[0], cost[1]])
                ans += cost[2]
                del(costs[i])
                break
    return ans

ans = solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
print(ans)
