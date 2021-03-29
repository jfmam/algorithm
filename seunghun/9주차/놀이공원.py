# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
testCase = int(input())
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
Min = 9999

if k == 1:
    print(1)
    exit


def check(i, j):
    global Min
    cnt = 0
    for x in range(i, i+k-1):
        for y in range(j, j+k-1):
            if arr[x][y] == 1:
                cnt += 1
    Min = min(Min, cnt)


for i in range(n-k):
    for j in range(n-k):
        check(i, j)
print(Min)
