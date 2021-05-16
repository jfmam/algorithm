import sys
sys.setrecursionlimit
min_value = sys.maxsize
ch = False

def solution(a, b, c, d):
    arr = [a, b, c]
    global min_value

    def DFS(n, cnt):
        global min_value
        global ch
        if cnt == 4 or n == d:
            if n == d:
                min_value = min(cnt, min_value)
                ch = True
        else:
            for i in arr:
                DFS(n + i, cnt + 1)
                DFS(n - i, cnt + 1)
    DFS(0, 1)

    if ch:
        return min_value
    else:
        return -1


ans = solution(3, 5, 7, 1)
print(ans)
