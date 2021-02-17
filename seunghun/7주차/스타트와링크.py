from sys import stdin

n = int(input())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
ch = [0] * n
ans = 9999


def dfs(idx, cnt):
    global ans
    if cnt == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if ch[i] and ch[j]:
                    start += arr[i][j]
                elif not ch[i] and not ch[j]:
                    link += arr[i][j]
        ans = min(ans, abs(start - link))
    for i in range(idx, n):
        if ch[i]:
            continue
        ch[i] = 1
        dfs(i + 1, cnt+1)  # 조합구하는코드
        ch[i] = 0


dfs(0, 0)
print(ans)
