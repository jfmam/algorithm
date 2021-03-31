import sys

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
p = list(map(int, sys.stdin.readline().split()))
Sum= 0

for i in range(p[0], p[2]+1):
    for j in range(p[1], p[3]+1):
        Sum += arr[i][j]

print(Sum)