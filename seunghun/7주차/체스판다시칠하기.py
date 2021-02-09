import sys

n, m = map(int, input().split())

arr = [list(map(str, input())) for _ in range(n)]
Min = 64

for i in range(n-7):
    for j in range(m-7):
        cnt1 = 0
        cnt2 = 0
        for a in range(i, i+8): # 처음 B에서 시작하는 경우
            for b in range(j, j+8):
                if a % 2 == 0 and b % 2 == 0:
                    if arr[a][b] == 'B':
                        cnt1 += 1
                elif a % 2 == 1 and b % 2 == 1:
                    if arr[a][b] == 'B':
                        cnt1 += 1
                elif a % 2 == 0 and b % 2 == 1:
                    if arr[a][b] == 'W':
                        cnt1 += 1
                elif a % 2 == 1 and b % 2 == 0:
                    if arr[a][b] == 'W':
                        cnt1 += 1
        for a in range(i, i+8):
            for b in range(j, j+8):
                if a % 2 == 0 and b % 2 == 0: # 처음 W에서 시작하는 경우
                    if arr[a][b] == 'W':
                        cnt2 += 1
                elif a % 2 == 1 and b % 2 == 1: # 다음 줄
                    if arr[a][b] == 'W':
                        cnt2 += 1
                elif a % 2 == 0 and b % 2 == 1:
                    if arr[a][b] == 'B':
                        cnt2 += 1
                elif a % 2 == 1 and b % 2 == 0:
                    if arr[a][b] == 'B':
                        cnt2 += 1
        Min = min(cnt1, cnt2, Min)
print(Min)
