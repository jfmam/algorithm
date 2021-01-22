import sys
n, m = map(int, input().split())

nar = []
mar = []
cnt = 0
nar = {sys.stdin.readline() for i in range(n)}

for j in range(m):
    tmp = sys.stdin.readline()
    if tmp in nar:
        cnt += 1

print(cnt)
