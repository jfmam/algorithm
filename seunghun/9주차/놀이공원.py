# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
testCase = int(input())

def execute(n, k, arr):
    Min = 9999
    for i in range(n-k+1):
        for j in range(n-k+1):
            cnt = 0
            for x in range(i, i+k):
                for y in range(j, j+k):
                    if arr[x][y] == 1:
                        cnt += 1
            Min = min(Min, cnt)
    print(Min)

for _ in range(testCase):
	n, k = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(n)]
	execute(n, k, arr)
