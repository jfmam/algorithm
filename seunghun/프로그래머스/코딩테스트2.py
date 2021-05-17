# DFS를 이용하여 최소값이 같은 경우를 Count 한다
import sys
Min = sys.maxsize
cnt = 0


def solution(r, c):
    x = [1, 0]
    y = [0, 1]

    def DFS(xx, yy, dis):
        global cnt
        if xx == c and yy == r:
            cnt += 1
        else:
            for i in range(2):
                dx = xx + x[i]
                dy = yy + y[i]
                if  dx <= c and 0 < dy <= r:
                    DFS(dx, dy, dis+1)
    DFS(1, 1, 0)

    return cnt


an = solution(3, 3)
print(an)
