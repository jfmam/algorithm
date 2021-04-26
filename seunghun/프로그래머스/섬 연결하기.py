import sys
sys.setrecursionlimit(10 ** 9)


def solution(n, costs):
    ans = 0
    costs.sort(key= lambda x: x[2] ) # cost 기준으로 정렬
    cycle = set([costs[0][0]]) # cycle의 집합
    while len(cycle) != n :
        for i, cost in costs:
            if cost[0] in cycle and cost[1] in cycle:# cycle에 속해 있으면 해당 값 반환
                continue
            if cost[0] in cycle or cost[1] in cycle: # 둘 중 하나만 cycle에 있다는 뜻은 아직 이동하지 않음을 의미
                cycle.update([cost[0], cost[1]]) # cost[0]이 cycle인지 cost[1]이 cycle에 있는지 알 수 없어 둘다 넣는다.
                ans += cost[2]
                del(costs[i])
                break
    return ans

def solution2(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    
    def union(x,y):
        x = find(x)
        y = find(y)

        if x!= y:
            parent[x] = y

    def find(x):
        if parent[x] == x:
            return x
        else:
            return find[x]
    
    costs.sort(key = lambda x: x[2])
    cnt = 0
    for a,b,c in costs:
        if find(a) != find(b):
            union(a,b)
            answer += c
            cnt += 1
            if cnt== n+1:
                return answer
    return answer

ans = solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
print(ans)
