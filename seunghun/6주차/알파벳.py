import sys


def dfs(x, y, ans):
    global answer
    answer = max(ans, answer) #if문이 없는 경우를 항상 고려한다.

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < r and 0 <= yy < c:
            if not alpha[ord(arr[xx][yy]) - 65]: #ord 내장함수
                alpha[ord(arr[xx][yy]) - 65] = 1
                dfs(xx, yy, ans + 1)
                alpha[ord(arr[xx][yy]) - 65] = 0


r, c = map(int, sys.stdin.readline().split())
arr = [list(map(str, input())) for _ in range(r)]
alpha = [0] * 26
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 1
alpha[ord(arr[0][0]) - 65] = 1
dfs(0, 0, 1)
print(answer)
