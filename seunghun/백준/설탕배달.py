import sys
input = sys.stdin.readline

n = int(input())
temp = n
cnt = 0

while temp > 0:
    if temp % 5 == 0:
        cnt += temp // 5
        temp = 0
        break
    temp -= 3
    cnt += 1

if temp == 0:
    print(cnt)
else:
    print(-1)
